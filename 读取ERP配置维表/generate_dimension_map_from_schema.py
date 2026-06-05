#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从《中络项目ERP 系统数据库表结构V1.0.md》解析全部表关联，生成 erp_dimension_joins.map。

与 MES 维表映射分离：ERP 使用 recId / *Id 外键、T_User 等思方云 ERP 表，不含 TBL_* MES 表。

用法：python3 generate_dimension_map_from_schema.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent
MD_FILE = ROOT.parent / "中络项目ERP 系统数据库表结构V1.0.md"
OUT_MAP = ROOT / "erp_dimension_joins.map"

TABLE_NAME = (
    r"(?:T_|FGI_|M_|S_|F_|G_|P_|W_|I_|C_|H_|A_|V_|E_|EQ_|PM_|TBL_|VW_|VM_|VIEW_)[A-Za-z0-9_]+"
)
TABLE_HEADER = re.compile(
    rf"^#### \d+ (.+?) \(\s*({TABLE_NAME})\s*\)\s*$",
    re.MULTILINE,
)
FIELD_ROW = re.compile(
    r"^\| ([^|]+?) \| [^|]+ \| [^|]+ \| [^|]+ \| (.+?) \|?\s*$",
    re.MULTILINE,
)
REL_LINE = re.compile(
    rf"^\s+-\s+({TABLE_NAME})\.([^\s/=]+)\s*=\s*([^\s]+)\.([^\s=]+)\s*$",
    re.MULTILINE,
)
FK_REF = re.compile(rf"对应\s*({TABLE_NAME})\.([A-Za-z0-9_]+)")

CHILD_TABLE_MARKERS = (
    "_ITEM",
    "_ITEMS",
    "_MAP",
    "_LINK",
    "_LOG_ITEM",
    "_DETAIL",
    "_RECORD_ITEM",
    "_EXT",
    "_DTL",
    "_LINE",
    "_HISTORY",
    "_RESULT",
)

# 文档关联行中的别名/笔误 → 正式表名
TABLE_REF_ALIASES: Dict[str, str] = {
    "物料批次库存": "M_InventoryBatch",
    "T_Step": "T_Steps",
    "T_Steps": "T_Steps",
    "s_job": "S_Job",
    "S_JOB": "S_Job",
    "S_SalePart": "S_SalesParts",
    "T_flowType": "T_FlowType",
    "T_Warehousing": "M_Warehousing",
    "inventoryMiscBatch": "M_InventoryMiscBatch",
    "M_BomPicklistItemBatch": "M_BOMPicklistItemBatch",
    "FGI_stockFormItem": "FGI_StockFormItem",
    "EQ_Equipments": "EQ_Equipments",
}

INVALID_REF_MARKERS = (
    "测试",
    "空数据",
    "作废",
    "序号",
    "工具,物料",
    "进站,2上机",
)

# ERP 枚举列中文名覆盖
ENUM_COL_AS: Dict[Tuple[str, str], str] = {
    ("M_BOMPicklist", "approveStatus"): "审批状态",
    ("M_BOMPicklist", "status"): "状态",
    ("P_MO", "status"): "单据状态",
    ("P_MO", "type"): "投产类型",
    ("P_MO", "saleType"): "销售类型",
    ("P_WO", "status"): "工单状态",
    ("S_Job", "approveStatus"): "审批状态",
    ("FGI_Receipt", "type"): "来源类型",
    ("M_Receipt", "type"): "接收类型",
    ("M_ReceiptItem", "poType"): "采购类型",
    ("M_Requisitions", "status"): "请购单状态",
}

FORCE_YN_FIELDS: Dict[Tuple[str, str], str] = {}

FORCE_CODE_ENUMS: Dict[Tuple[str, str], Tuple[str, List[Tuple[str, str]]]] = {
    ("M_BOMPicklist", "approveStatus"): (
        "审批状态",
        [("Pending", "制作中"), ("Approved", "审批通过")],
    ),
    ("P_MO", "saleType"): (
        "销售类型",
        [
            ("Bonded", "保税"),
            ("ForDomestic", "内销"),
            ("ForExport", "外销"),
        ],
    ),
    ("P_MO", "type"): (
        "投产类型",
        [
            ("SO", "正常投产(销售订单)"),
            ("ReturnRepair", "退货返修"),
            ("Replenishment", "补货"),
            ("StockRepair", "仓库返修"),
            ("ProVote", "生产补投"),
            ("Merger", "合拼"),
            ("MakeToStock", "存货补投"),
        ],
    ),
    ("FGI_Receipt", "type"): (
        "来源类型",
        [("Customer", "客户"), ("Outsourcing", "供应商")],
    ),
    ("M_Receipt", "type"): (
        "接收类型",
        [
            ("PO", "有采购接收"),
            ("NPO", "无采购接收"),
            ("MiscPO", "杂项采购接收"),
            ("C", "寄售接收"),
        ],
    ),
    ("M_ReceiptItem", "poType"): (
        "采购类型",
        [("S", "采购"), ("M", "杂项")],
    ),
    ("M_Requisitions", "status"): (
        "请购单状态",
        [("Valid", "已审核"), ("Active", "审核中")],
    ),
    ("FGI_ReceiptItem", "orderType"): (
        "订单类型",
        [("Outsourcing", "供应商"), ("Exchange", "客户")],
    ),
    ("P_MO", "status"): (
        "单据状态",
        [
            ("Active", "激活"),
            ("Order", "已下单"),
            ("WOWX", "外协"),
            ("WOWFF", "未发放"),
            ("WOYFF", "已发放"),
            ("WOZT", "暂停"),
            ("WOQX", "取消"),
            ("WOWC", "完成"),
        ],
    ),
    ("P_MO", "synchro"): (
        "同步状态",
        [("0", "-未同步"), ("1", "-已同步"), ("2", "-不同步")],
    ),
    ("P_MO", "dev"): (
        "研发标识",
        [("1", "是"), ("0", "否")],
    ),
}

FORCE_NUMERIC_ENUMS: Dict[Tuple[str, str], Tuple[str, List[Tuple[str, str]]]] = {
    ("P_WO", "status"): (
        "工单状态",
        [
            ("1", "外协"),
            ("2", "未发放"),
            ("3", "已发放"),
            ("4", "暂停"),
            ("5", "取消"),
            ("6", "完成"),
        ],
    ),
    ("P_MRBRequisition", "status"): (
        "单据状态",
        [("0", "待检"), ("1", "完成")],
    ),
}

ENUM_MAPPING_ID = {
    "status": "status",
    "approveStatus": "approve_status",
    "saleType": "sale_type",
    "type": "type",
    "originalStatus": "original_status",
}

FACT_ALIAS = {
    "FGI_Receipt": "fr",
    "FGI_ReceiptItem": "fri",
    "M_BOMPicklist": "bp",
    "M_Materials": "mat",
    "M_InventoryBatch": "ib",
    "M_PurchaseOrder": "po",
    "S_Job": "job",
    "P_MO": "mo",
    "P_WO": "wo",
    "S_Customer": "cust",
    "M_Suppliers": "supp",
}

FACT_KEYWORDS = {
    "FGI_Receipt": ["制成品接收", "接收单", "FGI_Receipt"],
    "FGI_ReceiptItem": ["制成品接收明细", "接收明细", "FGI_ReceiptItem"],
    "M_BOMPicklist": ["BOM领料", "领料单", "BOMPicklist"],
    "M_BOMIssue": ["BOM发料", "发料单"],
    "M_Materials": ["物料", "材料", "M_Materials"],
    "M_InventoryBatch": ["物料批次", "批次库存", "InventoryBatch"],
    "M_PurchaseOrder": ["采购订单", "采购单", "PurchaseOrder"],
    "M_Receipt": ["物料接收", "收货单"],
    "M_Requisitions": ["请购单", "请购", "M_Requisitions"],
    "M_RequisitionsItem": ["请购明细", "请购单明细"],
    "S_Customer": ["客户", "S_Customer"],
    "M_Suppliers": ["供应商", "M_Suppliers"],
    "S_Job": ["产品型号", "生产部件", "S_Job"],
    "P_MO": ["制造订单", "制造单", "P_MO"],
    "P_WO": ["工单", "工作单", "P_WO"],
    "T_User": ["用户", "登录账号", "T_User"],
    "T_Company": ["公司", "T_Company"],
    "T_Plants": ["工厂", "T_Plants"],
    "T_Department": ["部门"],
    "T_Warehouse": ["仓库"],
    "EQ_Equipments": ["设备", "EQ_Equipments"],
}

ERP_DIM_PROFILES: Dict[str, List[Tuple[str, str]]] = {
    "T_User": [
        ("employeeName", "用户名称"),
        ("loginName", "登录账号"),
        ("userCode", "用户代码"),
    ],
    "T_Company": [("name", "公司名称"), ("code", "公司代码")],
    "T_Plants": [("name", "工厂名称"), ("code", "工厂代码")],
    "T_Department": [("name", "部门名称"), ("code", "部门代码")],
    "T_Warehouse": [("name", "仓库名称"), ("code", "仓库代码")],
    "T_Location": [("name", "储区名称"), ("code", "储区代码")],
    "T_Unit": [("name", "单位名称"), ("code", "单位代码")],
    "T_PostRole": [("name", "岗位名称"), ("code", "岗位代码")],
    "T_Steps": [("name", "工序名称"), ("code", "工序代码")],
    "T_Process": [("name", "工艺名称"), ("code", "工艺代码")],
    "T_Category": [("name", "类别名称"), ("code", "类别代码")],
    "T_Currency": [("name", "币种名称"), ("code", "币种代码")],
    "T_FlowType": [("name", "流程类型"), ("code", "流程代码")],
    "T_Group": [("name", "用户组名称"), ("code", "用户组代码")],
    "T_Area": [("name", "区域名称"), ("code", "区域代码")],
    "T_Cate": [("name", "等级名称"), ("code", "等级代码")],
    "T_Tax": [("name", "税率名称"), ("code", "税率代码")],
    "T_PaymentMethod": [("name", "付款方式"), ("code", "付款方式代码")],
    "T_PaymentTerm": [("name", "付款周期"), ("code", "付款周期代码")],
    "T_Shipping": [("name", "运输方式"), ("code", "运输方式代码")],
    "T_FOB": [("name", "贸易方式"), ("code", "贸易方式代码")],
    "T_FunctionRight": [("name", "功能名称"), ("code", "功能代码")],
    "T_Module": [("name", "模块名称"), ("code", "模块代码")],
    "M_Suppliers": [("name", "供应商名称"), ("code", "供应商代码")],
    "S_Customer": [("name", "客户名称"), ("code", "客户代码")],
    "M_Materials": [("name", "物料名称"), ("code", "物料代码")],
    "M_InventoryBatch": [
        ("internalBatchNo", "内部批号"),
        ("suppBatchNo", "供应商批号"),
    ],
    "S_Job": [("partNum", "产品编码"), ("partName", "部件名称")],
    "S_SalesParts": [("partNum", "销售部件编码"), ("partName", "销售部件名称")],
    "P_MO": [("moNumber", "制造订单号")],
    "P_WO": [("partnum", "制造部件编码")],
    "F_Accounts": [("name", "科目名称"), ("code", "科目代码")],
    "FGI_Receipt": [("code", "接收单号")],
    "EQ_Equipments": [("eqName", "设备名称"), ("eqCode", "设备编号")],
    "S_BusinessMan": [("name", "业务员名称"), ("code", "业务员代码")],
    "E_JobMfgParts": [("partNum", "制造部件编码"), ("partName", "制造部件名称")],
}

ERP_USER_FK_COLS = {
    "creatorId": "创建人",
    "userId": "用户",
    "myId": "操作人",
    "checkorId": "检验员",
    "approverId": "审批人",
    "businessManId": "业务员",
    "keeperId": "仓管员",
    "inspectorId": "检验员",
    "receiverId": "接收人",
    "issuerId": "发料人",
}

ERP_NAME_PRIORITY = (
    "name",
    "code",
    "partNum",
    "partName",
    "partnum",
    "moNumber",
    "woNumber",
    "eqName",
    "eqCode",
    "internalBatchNo",
    "suppBatchNo",
    "employeeName",
    "loginName",
    "userCode",
)

IMPORTANT_DIM_ENUM_COLS = frozenset(
    {
        "type", "status", "approveStatus", "saleType", "poType", "originalStatus",
        "additionalStatus", "orderType", "postType", "prodType", "woType",
        "sourceType", "transType", "ttype", "way", "fileType", "miscType",
        "requisitionsType", "eqType", "buildMode", "jobStatus", "orderStatus",
        "os_PO_Type", "os_PR_Type", "ecnType", "flagPM", "result", "ab", "d_c",
    }
)

ENUM_LIKE_COLS = frozenset(
    IMPORTANT_DIM_ENUM_COLS
    | {
        "ifActive", "ifBonded", "ifInspection", "ifConsignment", "ifForeign",
        "ifReactionary", "ifReconcile", "ifCheck", "ifassign", "ifOutPut",
        "ifStock", "ifEnd", "ifJob", "ifBarcodEntry", "ifSpecifySuppId",
        "ifLifeSpan", "ifMI", "ifRigid", "ifFlex", "ifMfgPart", "ifBOMIssue",
        "ifLackMatCheck", "ifBusinessMan", "ifEmployee", "ifAssistant",
        "ifMaterials", "ifProduct", "ifWIP", "ifSpecial", "ifNew", "isActive",
        "isDemand", "isPreventive", "isLock", "non_Planned", "locked", "vmi",
        "enableApproval", "consignmentFlg", "taxFree", "remaining", "dev",
        "outsoucing", "contract", "salesOrder", "onhold", "inActive", "operating",
    }
)

# 码值说明泄漏为列名（英文码+中文说明）
_LEAKED_ENUM_AS = re.compile(
    r"[A-Za-z]{2,}\s*[：:]\s*[\u4e00-\u9fff]"
    r"|[A-Za-z]{2,}\s+[\u4e00-\u9fff]"
    r"|'[A-Za-z]+'"
    r"|Valid|Pending|Approved|Active|Outsourcing|ForDomestic|Bonded"
)


def _sql_escape(s: str) -> str:
    return s.replace("'", "''")


def _sql_col_ref(alias: str, col: str) -> str:
    if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", col):
        return f"{alias}.{col}"
    return f"{alias}.[{col}]"


_BAD_ENUM_LABEL = ("精度", "decimal", "varchar", "允许为空", "类型，", "长度")


def _valid_enum_label(label: str) -> bool:
    label = (label or "").strip()
    if not label or len(label) > 48:
        return False
    return not any(h in label for h in _BAD_ENUM_LABEL)


def _is_yn_enum_desc(desc: str) -> bool:
    text = (desc or "").strip()
    if not text:
        return False
    return bool(
        re.search(r"Y\s*代表\s*是", text, re.I)
        or re.search(r"Y\s*[：:]\s*是", text, re.I)
    ) and bool(
        re.search(r"N\s*代表\s*否", text, re.I)
        or re.search(r"N\s*[：:；;]\s*否", text, re.I)
    )


def _label_from_yn_desc(desc: str) -> str:
    text = (desc or "").strip()
    for pat in (
        r"^(.+?)[（(]",
        r"^(.+?)，\s*Y\s*代表",
        r"^(.+?)，\s*Y\s*[：:]",
        r"^(.+?)\s*Y\s*代表",
        r"^(.+?)\s*Y\s*[：:]",
        r"^(.+?)[，,]\s*Y\s*[：:]",
    ):
        m = re.match(pat, text, re.I)
        if m:
            return m.group(1).strip().rstrip("，,;；")
    return ""


def _build_yn_case_expr(fact_alias: str, col: str) -> str:
    col_ref = _sql_col_ref(fact_alias, col)
    return (
        f"CASE UPPER(RTRIM({col_ref})) WHEN 'Y' THEN N'是' WHEN 'N' THEN N'否' "
        f"ELSE {col_ref} END"
    )


def _parse_multi_labeled_code_pairs(desc: str) -> List[Tuple[str, str]]:
    """解析「Valid：已审核  Active：审核中」等多组 Code：中文 说明。"""
    text = (desc or "").strip()
    pairs: List[Tuple[str, str]] = []
    for m in re.finditer(
        r"([A-Za-z][A-Za-z0-9_]*)\s*[：:]\s*"
        r"([\u4e00-\u9fff（(][^A-Za-z：:;；]*?)"
        r"(?=\s+[A-Za-z][A-Za-z0-9_]*\s*[：:]|$)",
        text,
    ):
        label = m.group(2).strip().rstrip("。，,;；")
        if label and _valid_enum_label(label):
            pairs.append((m.group(1), label))
    return _dedupe_pairs(pairs)


def _parse_string_code_pairs(desc: str) -> List[Tuple[str, str]]:
    text = (desc or "").strip()
    pairs: List[Tuple[str, str]] = []
    for m in re.finditer(r"([A-Za-z][A-Za-z0-9_]*)\s*[：:]\s*([^；;]+)", text):
        code, label = m.group(1), m.group(2).strip().rstrip("；;、,")
        if len(code) >= 2 and label and _valid_enum_label(label):
            pairs.append((code, label))
    return pairs


def _parse_compact_code_pairs(desc: str) -> List[Tuple[str, str]]:
    """解析「PO 有采购接收 NPO无采购接收 MiscPO 杂项采购接收」类紧凑码值说明。"""
    text = (desc or "").strip()
    pairs: List[Tuple[str, str]] = []
    for m in re.finditer(
        r"([A-Za-z][A-Za-z0-9]*)\s*([\u4e00-\u9fff][^A-Za-z\s]*)", text
    ):
        code, label = m.group(1), m.group(2).strip().rstrip("，,;；")
        if label and _valid_enum_label(label):
            pairs.append((code, label))
    return _dedupe_pairs(pairs)


    return _dedupe_pairs(pairs)


def _is_false_positive_enum(col: str, desc: str) -> bool:
    if re.search(r"balance_\d|beg_balance|end_balance", col, re.I):
        return True
    text = (desc or "").strip()
    if re.match(r"^\d+月", text):
        return True
    if text.startswith("对应") and "recId" in text:
        return True
    if "对应" in text and "recId" in text and len(text) < 36:
        return True
    return False


def _parse_quoted_code_pairs(desc: str) -> List[Tuple[str, str]]:
    """'Pending'制作中，'Approved' 生效"""
    pairs: List[Tuple[str, str]] = []
    for m in re.finditer(r"'([A-Za-z][A-Za-z0-9_]*)'([^'，,;；]*)", desc or ""):
        label = re.sub(r"^[\s:：]+", "", m.group(2)).strip().rstrip("，,;；")
        if label and _valid_enum_label(label[:24]):
            pairs.append((m.group(1), label[:24]))
    return _dedupe_pairs(pairs)


def _parse_code_space_label_pairs(desc: str) -> List[Tuple[str, str]]:
    """Valid 生效、Approved 通过、Active 有效"""
    pairs: List[Tuple[str, str]] = []
    for m in re.finditer(
        r"(?<![A-Za-z0-9_])([A-Za-z][A-Za-z0-9_]{0,15})\s+([\u4e00-\u9fff][^A-Za-z，,;；.]{0,24})",
        desc or "",
    ):
        label = m.group(2).strip().rstrip("的").rstrip("。").rstrip("，,;；")
        if label and _valid_enum_label(label):
            pairs.append((m.group(1), label))
    return _dedupe_pairs(pairs)


def _parse_code_chinese_pairs(desc: str) -> List[Tuple[str, str]]:
    """Outsourcing：供应商，Exchange客户"""
    pairs: List[Tuple[str, str]] = []
    for m in re.finditer(
        r"(?<![A-Za-z0-9_])([A-Za-z][A-Za-z0-9_]*)([\u4e00-\u9fff][^A-Za-z，,;；]*)",
        desc or "",
    ):
        label = m.group(2).strip().rstrip("，,;；")
        if label and _valid_enum_label(label):
            pairs.append((m.group(1), label))
    return _dedupe_pairs(pairs)


def _parse_comma_segment_pairs(desc: str) -> List[Tuple[str, str]]:
    """Outsourcing：供应商，Exchange客户"""
    pairs: List[Tuple[str, str]] = []
    for seg in re.split(r"[，,；;]", desc or ""):
        seg = seg.strip()
        if not seg:
            continue
        m = re.match(
            r"([A-Za-z][A-Za-z0-9_]*)\s*[：:]\s*([\u4e00-\u9fff][^A-Za-z]*)", seg
        )
        if m:
            label = m.group(2).strip().rstrip("，,;；")
            if label and _valid_enum_label(label):
                pairs.append((m.group(1), label))
            continue
        m2 = re.match(r"([A-Za-z][A-Za-z0-9_]*)\s+([\u4e00-\u9fff][^A-Za-z]*)", seg)
        if m2:
            label = m2.group(2).strip().rstrip("，,;；")
            if label and _valid_enum_label(label):
                pairs.append((m2.group(1), label))
    return _dedupe_pairs(pairs)


def _parse_short_code_pairs(desc: str) -> List[Tuple[str, str]]:
    """D:借方 C 贷方、S:标准请购 M 杂项"""
    pairs: List[Tuple[str, str]] = []
    for m in re.finditer(
        r"(?<![A-Za-z0-9_])([A-Z]{1,4})\s*[：:]\s*([\u4e00-\u9fff][^A-Za-z，,;；]*)",
        desc or "",
    ):
        label = m.group(2).strip().rstrip("，,;；")
        if label and _valid_enum_label(label):
            pairs.append((m.group(1), label))
    for m in re.finditer(
        r"(?<![A-Za-z0-9_])([A-Z]{1,4})\s+([\u4e00-\u9fff][^A-Za-z，,;；]*)",
        desc or "",
    ):
        label = m.group(2).strip().rstrip("，,;；")
        if label and _valid_enum_label(label):
            pairs.append((m.group(1), label))
    return _dedupe_pairs(pairs)


def _parse_letter_list_pairs(desc: str) -> List[Tuple[str, str]]:
    """AB板类型  A,B,AB"""
    text = desc or ""
    m = re.search(r"类型[^A-Z]*([A-Z](?:,[A-Z])+)", text)
    if not m:
        return []
    labels = {
        "A": "A板",
        "B": "B板",
        "AB": "AB板",
    }
    out: List[Tuple[str, str]] = []
    for letter in m.group(1).split(","):
        letter = letter.strip()
        if letter:
            out.append((letter, labels.get(letter, letter)))
    return out


def _parse_bool01_pairs(desc: str) -> List[Tuple[str, str]]:
    text = desc or ""
    if not re.search(r"\d", text):
        return []
    if not re.search(r"是否|否|是|启用|禁用|激活|检验|寄售|锁定|审核|有效|通过|关闭", text):
        return []
    pairs: List[Tuple[str, str]] = []
    for m in re.finditer(r"(\d+)\s*\.?\s*([\u4e00-\u9fff]{1,8})", text):
        label = m.group(2).strip()
        if _valid_enum_label(label):
            pairs.append((m.group(1), label))
    return _dedupe_pairs(pairs)


def _parse_digit_space_label_pairs(desc: str) -> List[Tuple[str, str]]:
    """0 待检 1 完成"""
    pairs: List[Tuple[str, str]] = []
    for m in re.finditer(
        r"(?<![\d:：])(\d+)\s+([\u4e00-\u9fff]{1,8})", desc or ""
    ):
        label = m.group(2).strip()
        if _valid_enum_label(label):
            pairs.append((m.group(1), label))
    return _dedupe_pairs(pairs)


def _collect_enum_pair_candidates(desc: str) -> List[Tuple[str, str]]:
    best: List[Tuple[str, str]] = []
    for fn in (
        _parse_multi_labeled_code_pairs,
        _parse_comma_segment_pairs,
        _parse_code_chinese_pairs,
        _parse_quoted_code_pairs,
        _parse_code_space_label_pairs,
        _parse_string_code_pairs,
        _parse_compact_code_pairs,
        _parse_short_code_pairs,
        _parse_letter_list_pairs,
        _parse_bool01_pairs,
        _parse_digit_space_label_pairs,
        _parse_enum_pairs,
    ):
        pairs = fn(desc)
        if len(pairs) > len(best):
            best = pairs
    return best


def _label_from_field_desc(desc: str, fact_table: str, col: str) -> str:
    text = (desc or "").strip()
    for pat in (
        r"^([\u4e00-\u9fff]{2,12})[：:，,\s]",
        r"^([\u4e00-\u9fff]{2,12})[；;]",
        r"^([\u4e00-\u9fff]{2,12})\s*\d",
        r"^([\u4e00-\u9fff]{2,12})$",
    ):
        m = re.match(pat, text)
        if m:
            return m.group(1)
    return _enum_as_name(fact_table, col)


def detect_enum_spec(
    fact_table: str, col: str, desc: str
) -> Optional[Dict[str, Any]]:
    """从表结构字段说明自动识别枚举/码值译码规则。"""
    if _is_false_positive_enum(col, desc):
        return None
    text = (desc or "").strip()
    if not text or text == "-":
        return None
    tbl_col = (fact_table, col)

    if tbl_col in FORCE_CODE_ENUMS:
        as_name, pairs = FORCE_CODE_ENUMS[tbl_col]
        return {
            "pairs": pairs,
            "as_name": as_name,
            "kind": "string",
            "notes": f"状态码译码：{text[:80]}",
        }
    if tbl_col in FORCE_NUMERIC_ENUMS:
        as_name, pairs = FORCE_NUMERIC_ENUMS[tbl_col]
        return {
            "pairs": pairs,
            "as_name": as_name,
            "kind": "numeric",
            "notes": f"枚举译码（{fact_table}·{col}）：{text[:80]}",
        }
    if tbl_col in FORCE_YN_FIELDS or _is_yn_enum_desc(text):
        return {
            "pairs": [],
            "as_name": (
                FORCE_YN_FIELDS.get(tbl_col)
                or _label_from_yn_desc(text)
                or _enum_as_name(fact_table, col)
            ),
            "kind": "yn",
            "notes": f"Y/N译码（Y=是，N=否）：{text[:80]}",
        }

    pairs = _collect_enum_pair_candidates(text)
    min_pairs = 2
    if col in ENUM_LIKE_COLS or col.lower().startswith(("if", "is")):
        min_pairs = 1
    if len(pairs) < min_pairs:
        return None

    if all(p[0].isdigit() for p in pairs):
        return {
            "pairs": pairs,
            "as_name": _label_from_numeric_enum_desc(text, fact_table, col),
            "kind": "numeric",
            "notes": f"枚举译码：{text[:80]}",
        }
    return {
        "pairs": pairs,
        "as_name": _label_from_field_desc(text, fact_table, col),
        "kind": "string",
        "notes": f"状态码译码：{text[:80]}",
    }


def _build_expr_from_enum_spec(
    fact_alias: str, col: str, spec: Dict[str, Any]
) -> str:
    kind = spec.get("kind") or "string"
    if kind == "yn":
        return _build_yn_case_expr(fact_alias, col)
    pairs = spec.get("pairs") or []
    if kind == "numeric":
        return _build_enum_case_expr(fact_alias, col, pairs)
    return _build_string_code_case_expr(fact_alias, col, pairs)


def _label_from_code_enum_desc(desc: str, fact_table: str, col: str) -> str:
    first = re.split(r"[；;]", (desc or "").strip(), maxsplit=1)[0].strip()
    if first and not re.match(r"^[A-Z][A-Z0-9_]+\s*[：:]", first):
        return first
    return _enum_as_name(fact_table, col)


def _build_string_code_case_expr(
    fact_alias: str, col: str, pairs: List[Tuple[str, str]]
) -> str:
    col_ref = _sql_col_ref(fact_alias, col)
    whens = " ".join(
        f"WHEN '{_sql_escape(k.upper())}' THEN N'{_sql_escape(v)}'" for k, v in pairs
    )
    return f"CASE UPPER(RTRIM({col_ref})) {whens} ELSE {col_ref} END"


def _dedupe_pairs(pairs: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    seen: set = set()
    out: List[Tuple[str, str]] = []
    for k, v in pairs:
        if k in seen:
            continue
        seen.add(k)
        out.append((k, v))
    return out


def _parse_enum_pairs(desc: str) -> List[Tuple[str, str]]:
    text = (desc or "").strip()
    if not text:
        return []
    scan = text
    m_paren = re.search(r"[（(]([^）)]+)[）)]\s*$", text)
    if m_paren and len(re.findall(r"\d+\s*[：:]", m_paren.group(1))) >= 2:
        scan = m_paren.group(1)
    else:
        m0 = re.search(r"\d+\s*[：:]", text)
        if m0:
            scan = text[m0.start() :]

    pairs: List[Tuple[str, str]] = []
    for seg in re.split(r"[、,；;]", scan):
        m = re.match(r"\s*(\d+)\s*[:：]\s*([^；;]+)", seg.strip())
        if m:
            label = m.group(2).strip().rstrip("；;、,")
            if label and (_valid_enum_label(label) or "（" in label or "）" in label):
                pairs.append((m.group(1), label))
    if len(pairs) >= 2:
        return _dedupe_pairs(pairs)

    pairs = []
    for m in re.finditer(r"(\d+)\s*[:：]\s*([^,，;；、]+)", scan):
        label = m.group(2).strip().rstrip("；;、,")
        if _valid_enum_label(label):
            pairs.append((m.group(1), label))
    if len(pairs) >= 2:
        return _dedupe_pairs(pairs)

    for m in re.finditer(r"(\d+)\s*([^,，;；、\d:：\s][^,，;；、]{1,40})", scan):
        label = m.group(2).strip().rstrip("）；)）")
        if _valid_enum_label(label):
            pairs.append((m.group(1), label))
    if len(pairs) >= 2:
        return _dedupe_pairs(pairs)

    for m in re.finditer(r"(\d+)([^、,;；\d:：][^、,;；]*)", text):
        label = m.group(2).strip().rstrip("；;、,")
        if _valid_enum_label(label) and not label.startswith(":"):
            pairs.append((m.group(1), label))
    return _dedupe_pairs(pairs)


def _label_from_numeric_enum_desc(desc: str, fact_table: str, col: str) -> str:
    text = (desc or "").strip()
    for pat in (
        r"^(.+?)[（(]\s*\d",
        r"^(.+?)[：:]\s*\d",
        r"^(.+?)[，,]\s*\d",
        r"^(.+?)\s+\d",
    ):
        m = re.match(pat, text)
        if m:
            name = m.group(1).strip().rstrip("，,;；")
            if name and len(name) <= 20:
                return name
    if re.match(r"^[\u4e00-\u9fff]+$", col):
        return col
    return _enum_as_name(fact_table, col)


def _build_enum_case_expr(fact_alias: str, col: str, pairs: List[Tuple[str, str]]) -> str:
    col_ref = _sql_col_ref(fact_alias, col)
    whens = " ".join(f"WHEN {k} THEN N'{_sql_escape(v)}'" for k, v in pairs)
    return f"CASE {col_ref} {whens} ELSE CAST({col_ref} AS NVARCHAR(20)) END"


def _enum_as_name(fact_table: str, col: str) -> str:
    if (fact_table, col) in ENUM_COL_AS:
        return ENUM_COL_AS[(fact_table, col)]
    if col in ("status", "approveStatus", "originalStatus", "additionalStatus", "orderStatus"):
        return "状态"
    if col in ("saleType",):
        return "销售类型"
    if col in ("type", "orderType", "poType", "ecnType", "os_PO_Type", "os_PR_Type"):
        return "类型"
    if col.lower().startswith("if") or col.lower().startswith("is") or col in (
        "locked", "vmi", "enableApproval", "consignmentFlg", "onhold",
    ):
        return col
    if re.match(r"^[\u4e00-\u9fff]+$", col):
        return col
    return col


def _enum_mapping_id(col: str) -> str:
    if col in ENUM_MAPPING_ID:
        return ENUM_MAPPING_ID[col]
    if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", col):
        return col.lower() or "enum"
    return f"enum_{abs(hash(col)) % 100000}"


def build_enum_mappings(
    fact_table: str,
    fact_alias: str,
    fields: Dict[str, str],
) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    seen_ids: set = set()
    for col, desc in fields.items():
        spec = detect_enum_spec(fact_table, col, desc)
        if not spec:
            continue
        as_name = spec["as_name"]
        if col.lower().startswith(("if", "is")) or col in (
            "locked", "vmi", "enableApproval", "consignmentFlg", "onhold",
        ):
            as_name = _label_from_field_desc(desc, fact_table, col)
        expr = _build_expr_from_enum_spec(fact_alias, col, spec)
        mid = _enum_mapping_id(col)
        if mid in seen_ids:
            mid = f"{mid}_{col.lower()}"
        seen_ids.add(mid)
        out.append(
            {
                "id": mid,
                "fact_columns": [col],
                "joins": [],
                "select": [{"expr": expr, "as": as_name}],
                "forbidden": [f"{_sql_col_ref(fact_alias, col)} AS [{as_name}]"],
                "notes": spec.get("notes") or "",
                "match_type": "enum",
            }
        )
    return out


def _enum_select_for_field(
    dim_table: str,
    dim_alias: str,
    col: str,
    dim_fields: Dict[str, str],
) -> Optional[Tuple[str, str]]:
    """维表 JOIN 列若为码值字段，返回 (CASE 表达式, 中文列名)。"""
    spec = detect_enum_spec(dim_table, col, dim_fields.get(col, ""))
    if not spec:
        return None
    as_name = spec["as_name"]
    desc = dim_fields.get(col, "")
    if col.lower().startswith(("if", "is")):
        as_name = _label_from_field_desc(desc, dim_table, col)
    expr = _build_expr_from_enum_spec(dim_alias, col, spec)
    return expr, as_name


def _is_enum_field(dim_table: str, col: str, desc: str) -> bool:
    return detect_enum_spec(dim_table, col, desc) is not None


def _build_ref_index(tables: Dict[str, Dict[str, Any]]) -> Dict[str, str]:
    index: Dict[str, str] = {}
    for tname, info in tables.items():
        for key in (tname, tname.upper(), tname.lower()):
            index[key] = tname
        label = info.get("short_label") or ""
        if label:
            index[label] = tname
            clean = re.sub(r"[（(].+[）)]", "", label).strip()
            if clean:
                index[clean] = tname
    for alias, target in TABLE_REF_ALIASES.items():
        resolved = index.get(target, target)
        if resolved in tables:
            index[alias] = resolved
            index[alias.lower()] = resolved
            index[alias.upper()] = resolved
    return index


def _resolve_table_ref(raw: str, ref_index: Dict[str, str], tables: Dict[str, Any]) -> str:
    token = (raw or "").strip()
    if not token:
        return ""
    if any(m in token for m in INVALID_REF_MARKERS):
        return ""
    if token in ref_index:
        return ref_index[token]
    upper = token.upper()
    for key, tname in ref_index.items():
        if key.upper() == upper:
            return tname
    if re.match(rf"^{TABLE_NAME}$", token, re.I):
        for tname in tables:
            if tname.upper() == upper:
                return tname
    return ""


def _is_child_table_link(fact_col: str, dim_table: str, dim_col: str) -> bool:
    if dim_col != "recId":
        return False
    if any(m in dim_table.upper() for m in CHILD_TABLE_MARKERS):
        return True
    if dim_table.endswith("Item") or dim_table.endswith("Detail"):
        return True
    return False


def _is_valid_dim_join(
    fact_col: str,
    dim_table: str,
    dim_col: str,
    dim_fields: Dict[str, str],
) -> bool:
    if not dim_fields:
        return False
    if _is_child_table_link(fact_col, dim_table, dim_col):
        return False
    if dim_col == "recId":
        if fact_col.endswith("Id") or fact_col.endswith("ID"):
            return True
        if fact_col in ("userId", "myId"):
            return True
    if fact_col == dim_col and dim_col != "recId":
        return True
    return False


def parse_schema(md_text: str) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, str]]:
    tables: Dict[str, Dict[str, Any]] = {}
    headers = list(TABLE_HEADER.finditer(md_text))
    for i, m in enumerate(headers):
        short_label = m.group(1).strip()
        tname = m.group(2)
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(md_text)
        block = md_text[start:end]

        meaning_m = re.search(r"- \*\*业务含义\*\*：(.+)", block)
        meaning = meaning_m.group(1).strip() if meaning_m else ""

        fields: Dict[str, str] = {}
        for fm in FIELD_ROW.finditer(block):
            fname = fm.group(1).strip()
            if fname in ("字段名", "--------"):
                continue
            fields[fname] = fm.group(2).strip()

        rels_set: set[Tuple[str, str, str]] = set()
        if "- **关联关系**：无" not in block:
            for rm in REL_LINE.finditer(block):
                lt, lc, rt_raw, rc = rm.group(1), rm.group(2), rm.group(3), rm.group(4)
                if lt != tname:
                    continue
                for rt in re.split(r"/", rt_raw):
                    rt = rt.strip()
                    if rt:
                        rels_set.add((lc, rt, rc))

        for fname, desc in fields.items():
            for fk in FK_REF.finditer(desc):
                rels_set.add((fname, fk.group(1), fk.group(2)))

        tables[tname] = {
            "short_label": short_label,
            "meaning": meaning,
            "fields": fields,
            "relations": sorted(rels_set),
        }

    ref_index = _build_ref_index(tables)
    for tname, info in tables.items():
        resolved: List[Tuple[str, str, str]] = []
        for fc, dt_raw, dc in info["relations"]:
            dt = _resolve_table_ref(dt_raw, ref_index, tables)
            if dt and dt in tables:
                resolved.append((fc, dt, dc))
        info["relations"] = sorted(set(resolved))
    return tables, ref_index


def _alias_from_table(tname: str) -> str:
    if tname in FACT_ALIAS:
        return FACT_ALIAS[tname]
    parts = re.split(r"[_]", tname, maxsplit=1)
    if len(parts) == 2:
        prefix, rest = parts
        segs = rest.split("_")
        if len(segs) >= 2:
            return (prefix[0] + segs[0][:2] + segs[1][:1]).lower()
        return (prefix[0] + rest[:3]).lower()
    return tname[:3].lower()


def _dim_alias(dim_table: str, fact_col: str, used: set) -> str:
    presets = {
        ("T_User", "creatorId"): "tu",
        ("T_User", "userId"): "tu",
        ("T_Plants", "plantsId"): "tp",
        ("T_Company", "companyId"): "tc",
        ("T_Department", "departmentId"): "td",
        ("T_Warehouse", "warehouseId"): "tw",
        ("M_Materials", "materialsId"): "mm",
        ("S_Job", "jobId"): "sj",
        ("S_Customer", "customerId"): "sc",
        ("M_Suppliers", "suppliersId"): "ms",
        ("P_MO", "moId"): "pmo",
        ("P_WO", "woId"): "pwo",
    }
    key = (dim_table, fact_col)
    if key in presets:
        base = presets[key]
    else:
        base = re.sub(r"[^a-z0-9]", "", dim_table.lower())[:6] or "dim"
    n = 1
    cand = base
    while cand in used:
        n += 1
        cand = f"{base}{n}"
    used.add(cand)
    return cand


def _mapping_id(fact_col: str, dim_table: str) -> str:
    known = {
        ("plantsId", "T_Plants"): "plants",
        ("companyId", "T_Company"): "company",
        ("departmentId", "T_Department"): "department",
        ("warehouseId", "T_Warehouse"): "warehouse",
        ("creatorId", "T_User"): "creator",
        ("userId", "T_User"): "user",
        ("myId", "T_User"): "operator",
        ("materialsId", "M_Materials"): "materials",
        ("jobId", "S_Job"): "job",
        ("customerId", "S_Customer"): "customer",
        ("suppliersId", "M_Suppliers"): "supplier",
        ("moId", "P_MO"): "mo",
        ("woId", "P_WO"): "wo",
        ("stepsId", "T_Steps"): "steps",
        ("processId", "T_Process"): "process",
        ("postRoleId", "T_PostRole"): "post_role",
        ("stockUnitId", "T_Unit"): "unit",
        ("inventoryBatchId", "M_InventoryBatch"): "inventory_batch",
        ("equipmentId", "EQ_Equipments"): "equipment",
    }
    if (fact_col, dim_table) in known:
        return known[(fact_col, dim_table)]
    base = fact_col.lower().removesuffix("id") or fact_col.lower()
    dim_s = dim_table.split("_", 1)[-1].lower()[:12]
    return f"{base}_to_{dim_s}"


def _is_erp_user_fk_col(col: str) -> bool:
    if col in ERP_USER_FK_COLS:
        return True
    if col.endswith("UserId"):
        return True
    return False


def _pick_display_cols(
    dim_table: str,
    dim_fields: Dict[str, str],
    dim_col: str,
) -> List[Tuple[str, str]]:
    if dim_table in ERP_DIM_PROFILES:
        out = []
        for col, cn in ERP_DIM_PROFILES[dim_table]:
            if col in dim_fields:
                label = cn or dim_fields[col] or col
                out.append((col, label))
        if out:
            return out

    skip_cols = {
        "recId",
        "version",
        "lastModifyDate",
        "modifiedBy",
        "note",
        dim_col,
    }
    candidates: List[Tuple[str, str, int]] = []
    for col in ERP_NAME_PRIORITY:
        if col in dim_fields and col not in skip_cols:
            desc = dim_fields[col]
            candidates.append((col, desc or col, 0))

    for col, desc in dim_fields.items():
        if col in skip_cols or any(c[0] == col for c in candidates):
            continue
        if _is_enum_field(dim_table, col, desc):
            continue
        score = 10
        if any(k in (desc or "") for k in ("名称", "代码", "编号", "单号", "批号", "账号")):
            score = 2
        elif col.endswith("Id"):
            continue
        candidates.append((col, desc or col, score))

    candidates.sort(key=lambda x: (x[2], len(x[0])))
    out = [(c, d if d and d != c else c) for c, d, _ in candidates[:4]]
    if not out and dim_col in dim_fields:
        out = [(dim_col, dim_fields[dim_col] or dim_col)]
    return out


def build_mapping(
    fact_table: str,
    fact_col: str,
    dim_table: str,
    dim_col: str,
    fact_alias: str,
    dim_fields: Dict[str, str],
    fact_fields: Dict[str, str],
    used_aliases: set,
) -> Dict[str, Any]:
    mid = _mapping_id(fact_col, dim_table)
    dim_a = _dim_alias(dim_table, fact_col, used_aliases)
    on = f"{dim_a}.{dim_col} = {fact_alias}.{fact_col}"
    joins: List[Dict[str, str]] = [{"alias": dim_a, "table": dim_table, "on": on}]
    select: List[Dict[str, str]] = []
    forbidden: List[str] = []
    notes = ""
    match_type = ""
    optional = False
    fact_cn = fact_fields.get(fact_col, fact_col)

    if dim_table == "T_User" and _is_erp_user_fk_col(fact_col):
        role = ERP_USER_FK_COLS.get(fact_col, fact_cn.replace("，对应T_User.recId", ""))
        if not role or role == fact_col:
            role = fact_cn.split("，")[0] if "，" in fact_cn else fact_col
        name_cn = role if role.endswith("名称") else f"{role}名称"
        select = [
            {"expr": f"{dim_a}.employeeName", "as": name_cn},
            {"expr": f"{dim_a}.loginName", "as": f"{role}账号" if "账号" not in role else f"{role}登录账号"},
            {"expr": f"{dim_a}.userCode", "as": f"{role}代码" if "代码" not in role else role},
        ]
        forbidden = [f"{fact_alias}.{fact_col} AS [{name_cn}]"]
        return {
            "id": mid,
            "fact_columns": [fact_col],
            "joins": joins,
            "select": select,
            "forbidden": forbidden,
            "notes": notes,
            "match_type": match_type,
            "optional": optional,
        }

    display = _pick_display_cols(dim_table, dim_fields, dim_col)
    for col, cn in display:
        enum_sel = _enum_select_for_field(dim_table, dim_a, col, dim_fields)
        if enum_sel:
            select.append({"expr": enum_sel[0], "as": enum_sel[1]})
        else:
            select.append({"expr": f"{dim_a}.{col}", "as": cn})

    selected_as = {sel["as"] for sel in select}
    selected_cols = {
        re.search(r"\.(\w+)\s*$", sel.get("expr", "")).group(1)
        for sel in select
        if re.search(r"\.(\w+)\s*$", sel.get("expr", ""))
    }
    for col in dim_fields:
        if col in selected_cols:
            continue
        enum_sel = _enum_select_for_field(dim_table, dim_a, col, dim_fields)
        if not enum_sel or enum_sel[1] in selected_as:
            continue
        select.append({"expr": enum_sel[0], "as": enum_sel[1]})
        selected_as.add(enum_sel[1])

    if not select:
        select.append({"expr": f"{dim_a}.{dim_col}", "as": fact_cn or fact_col})

    return {
        "id": mid,
        "fact_columns": [fact_col],
        "joins": joins,
        "select": select,
        "forbidden": forbidden,
        "notes": notes,
        "match_type": match_type,
        "optional": optional,
    }


def _build_display_columns(
    fact_table: str,
    fact_alias: str,
    fields: Dict[str, str],
    mappings: List[Dict[str, Any]],
) -> List[Dict[str, str]]:
    mapped: set = set()
    for mp in mappings:
        mapped.update(mp.get("fact_columns") or [])
    skip: Set[str] = set(mapped)
    for col in fields:
        if _is_erp_user_fk_col(col):
            skip.add(col)
        if col.endswith("Id") or col.endswith("ID"):
            skip.add(col)
    enum_mapped = {
        c
        for mp in mappings
        if mp.get("match_type") == "enum"
        for c in (mp.get("fact_columns") or [])
    }
    skip |= enum_mapped
    out: List[Dict[str, str]] = []
    for col, cn in fields.items():
        if col in skip:
            continue
        if detect_enum_spec(fact_table, col, cn):
            continue
        as_name = cn
        if _LEAKED_ENUM_AS.search(cn or "") or (cn and len(cn) > 24 and re.search(r"[A-Za-z]{2,}", cn)):
            as_name = _label_from_field_desc(cn, fact_table, col)
            if _LEAKED_ENUM_AS.search(as_name):
                as_name = _enum_as_name(fact_table, col)
        out.append({"expr": _sql_col_ref(fact_alias, col), "as": as_name})
    return out


def mappings_to_map_lines(fact_table: str, tcfg: Dict[str, Any]) -> List[str]:
    lines: List[str] = []
    alias = tcfg["fact_alias"]
    label = tcfg["label"]
    keywords = tcfg.get("default_for_keywords") or []
    kw = ", ".join(keywords) if keywords else label

    lines.append(f"[表 {fact_table}]")
    lines.append(f"标签={label}")
    lines.append(f"关键词={kw}")
    lines.append(f"别名={alias}")
    lines.append("")

    for mp in tcfg["mappings"]:
        lines.append(f"[映射 {mp['id']}]")
        lines.append(f"字段={', '.join(mp['fact_columns'])}")
        if mp.get("match_type") == "enum":
            lines.append("类型=枚举")
        if mp.get("optional"):
            lines.append("可选=是")
        if mp.get("notes"):
            lines.append(f"说明={mp['notes']}")
        for j in mp.get("joins") or []:
            parts = [j["alias"], j["table"], j["on"]]
            if j.get("depends_on"):
                parts.append(f"依赖={j['depends_on']}")
            lines.append(f"关联={' | '.join(parts)}")
        for sel in mp.get("select") or []:
            lines.append(f"列={sel['expr']} | {sel['as']}")
        for fb in mp.get("forbidden") or []:
            lines.append(f"禁止={fb}")
        lines.append("")

    for dc in tcfg.get("display_columns") or []:
        lines.append(f"展示列={dc['expr']} | {dc['as']}")
    if tcfg.get("display_columns"):
        lines.append("")
    return lines


def generate_map(tables: Dict[str, Dict[str, Any]]) -> str:
    fact_edges: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)
    for fact, info in tables.items():
        for fc, dt, dc in info["relations"]:
            if fact == dt:
                continue
            if fc not in info["fields"]:
                continue
            dim_fields = tables.get(dt, {}).get("fields", {})
            if not _is_valid_dim_join(fc, dt, dc, dim_fields):
                continue
            fact_edges[fact].append((fc, dt, dc))

    priority_facts = [
        "FGI_Receipt",
        "FGI_ReceiptItem",
        "M_BOMPicklist",
        "M_Materials",
        "M_InventoryBatch",
        "M_PurchaseOrder",
        "S_Job",
        "P_MO",
        "P_WO",
        "S_Customer",
        "M_Suppliers",
        "T_User",
        "T_Company",
        "T_Plants",
    ]
    tables_with_enum: set = set()
    for tname, info in tables.items():
        alias = _alias_from_table(tname)
        if build_enum_mappings(tname, alias, info["fields"]):
            tables_with_enum.add(tname)

    all_facts = set(fact_edges.keys()) | tables_with_enum
    ordered_facts: List[str] = []
    for f in priority_facts:
        if f in all_facts:
            ordered_facts.append(f)
    for f in sorted(all_facts):
        if f not in ordered_facts:
            ordered_facts.append(f)

    header = """# =============================================================================
# 维表映射配置（由 generate_dimension_map_from_schema.py 根据 ERP 表结构 V1.0 生成）
# 与 MES 维表映射（mes_dimension_joins.map）分离维护，勿混用 TBL_* / CID 等 MES 约定
# 改完后运行：python3 build_dify_bundle.py → 复制 dify_erp_dimension_node.py 到 Dify
# =============================================================================
#
# 写法说明：
#   [表 表名]           一张 ERP 业务主表（外键多为 *Id → 维表.recId）
#   标签=               中文说明
#   关键词=             用户问题里出现这些词时，选中该表（逗号分隔）
#   别名=               SQL 里事实表别名
#
#   [映射 英文名]       一组「事实字段 → 维表 → 中文列」
#   字段=               事实表上的列，多个用逗号分隔
#   类型=枚举           状态/类型等码值字段，SELECT 须用 CASE 译码
#   关联=别名 | 维表 | ON条件
#   列=SQL表达式 | 中文列名
#   展示列=表达式 | 中文列名
#   禁止=               不要这样写 SQL
#
# [全局] 下「禁止=」对所有表生效

[全局]
默认别名=fr
禁止=FROM/JOIN 表名与 WITH (NOLOCK) 拆成两行
禁止=无时间条件的明细列表查询省略 ORDER BY（须按主时间列 DESC 由近到远）
禁止=使用 MES 表名/字段（TBL_*、CID、CWC_ID 等）解析 ERP 业务

"""

    body_lines: List[str] = []
    for fact_table in ordered_facts:
        edges = fact_edges[fact_table]
        fact_info = tables[fact_table]
        fact_alias = _alias_from_table(fact_table)
        used_aliases: set = set()
        mappings: List[Dict[str, Any]] = []
        seen_ids: set = set()

        for fc, dt, dc in edges:
            mp = build_mapping(
                fact_table,
                fc,
                dt,
                dc,
                fact_alias,
                tables.get(dt, {}).get("fields", {}),
                fact_info["fields"],
                used_aliases,
            )
            if mp["id"] in seen_ids:
                for existing in mappings:
                    if existing["id"] == mp["id"]:
                        existing["fact_columns"] = list(
                            dict.fromkeys(existing["fact_columns"] + mp["fact_columns"])
                        )
                        break
            else:
                seen_ids.add(mp["id"])
                mappings.append(mp)

        enum_maps = build_enum_mappings(fact_table, fact_alias, fact_info["fields"])
        prepend: List[Dict[str, Any]] = []
        for emp in enum_maps:
            if emp["id"] in seen_ids:
                continue
            seen_ids.add(emp["id"])
            prepend.append(emp)
        mappings = prepend + mappings

        keywords = FACT_KEYWORDS.get(fact_table, [])
        if not keywords:
            keywords = [fact_info["short_label"]]

        display_columns = _build_display_columns(
            fact_table, fact_alias, fact_info["fields"], mappings
        )
        tcfg = {
            "fact_alias": fact_alias,
            "label": fact_info["short_label"],
            "default_for_keywords": keywords,
            "mappings": mappings,
            "display_columns": display_columns,
        }
        body_lines.extend(mappings_to_map_lines(fact_table, tcfg))

    return header + "\n".join(body_lines)


def main() -> None:
    md = MD_FILE.read_text(encoding="utf-8")
    tables, _ = parse_schema(md)
    content = generate_map(tables)
    OUT_MAP.write_text(content, encoding="utf-8")
    n_tables = content.count("[表 ")
    n_maps = content.count("[映射 ")
    print(f"已写入 {OUT_MAP.name}")
    print(f"  事实表: {n_tables}, 映射块: {n_maps}")


if __name__ == "__main__":
    main()
