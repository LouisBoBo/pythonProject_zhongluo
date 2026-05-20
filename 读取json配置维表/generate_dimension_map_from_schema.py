#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从《中络项目MES 系统数据库表结构V1.1.md》解析全部表关联，生成 mes_dimension_joins.map。

用法：python3 generate_dimension_map_from_schema.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent
MD_FILE = ROOT.parent / "中络项目MES 系统数据库表结构V1.1.md"
OUT_MAP = ROOT / "mes_dimension_joins.map"

# 高频事实表 SQL 别名（其余表按表名自动生成）
FACT_ALIAS = {
    "TBL_SFC_WS_LOG": "l",
    "TBL_MO": "m",
    "TBL_SFC_WS_LOG_ITEM": "i",
    "TBL_WMS_PI": "pi",
    "TBL_WMS_PS": "ps",
    "TBL_WMS_MI": "mi",
}

# 用户问题关键词（用于 infer_fact_table）
FACT_KEYWORDS = {
    "TBL_SFC_WS_LOG": ["生产记录", "报工", "工位", "WS_LOG"],
    "TBL_MO": ["工单", "MO_LOT", "批次"],
    "TBL_WMS_PI": ["入库", "PI"],
    "TBL_WMS_PS": ["出库", "PS"],
    "TBL_QM_INSPECT_RECORD": ["检验记录", "IPQC", "FQC"],
    "TBL_EAP_ALARM": ["设备报警", "报警记录"],
    "TBL_EAM_REPAIR": ["维修", "报修"],
}

TABLE_RE = re.compile(
    r"^-{6,}\s*\n(\d+)\.\s+(TBL_[A-Z0-9_]+)（([^）]+)）\n"
    r"- 业务含义：([^\n]+)\n"
    r"- 字段列表：\n((?:  - [^\n]+\n)*)"
    r"(?:- 关联关系：\n((?:  - [^\n]+\n)*))?",
    re.MULTILINE,
)
FIELD_RE = re.compile(r"  - (\w+) [\w?]+ ([^\n]+)")
REL_RE = re.compile(r"  - (TBL_[A-Z0-9_]+)\.(\w+) = (TBL_[A-Z0-9_]+)\.(\w+)")


def parse_schema(md_text: str) -> Dict[str, Dict[str, Any]]:
    tables: Dict[str, Dict[str, Any]] = {}
    for m in TABLE_RE.finditer(md_text):
        tname = m.group(2)
        fields = {fm.group(1): fm.group(2).strip() for fm in FIELD_RE.finditer(m.group(5))}
        rels = [(rm.group(2), rm.group(3), rm.group(4)) for rm in REL_RE.finditer(m.group(6) or "")]
        tables[tname] = {
            "short_label": m.group(3),
            "meaning": m.group(4).strip(),
            "fields": fields,
            "relations": rels,
        }
    return tables


def _alias_from_table(tname: str) -> str:
    if tname in FACT_ALIAS:
        return FACT_ALIAS[tname]
    # TBL_XXX_YYY -> 取末段首字母
    parts = tname.replace("TBL_", "").split("_")
    if len(parts) >= 2:
        return "".join(p[0].lower() for p in parts[:3])
    return parts[0][0].lower() if parts else "t"


# 人员账号 JOIN 固定别名（与 SQL 提示词一致）
USER_ACCOUNT_ALIASES = {
    "CSTART_USER_NAME": "u_s",
    "CEND_USER_NAME": "u_e",
    "CCHECK_USER_NAME": "u_c",
}


def _dim_alias(dim_table: str, fact_col: str, used: set) -> str:
    if dim_table == "TBL_SYS_USER" and _is_user_account_col(fact_col):
        if fact_col in USER_ACCOUNT_ALIASES:
            a = USER_ACCOUNT_ALIASES[fact_col]
            used.add(a)
            return a
    presets = {
        ("TBL_BD_WC", "CWC_ID"): "wc",
        ("TBL_BD_PROCESS", "CPROCESS_ID"): "p",
        ("TBL_BD_ITEM", "CITEM_ID"): "i",
        ("TBL_BD_ITEM_TYPE", "CITEM_TYPE_ID"): "typ",
        ("TBL_BD_CUSTOMER", "CUSTOMER_CODE"): "cust",
        ("TBL_BD_CUSTOMER", "CUST_CODE"): "cust",
        ("TBL_EAP_DEVICE", "CDEVICE_ID"): "d",
        ("TBL_EAP_TAG", "CTAG_ID"): "tag",
        ("TBL_WMS_LOCATION", "CLOCATION_ID"): "loc",
        ("TBL_WMS_WAREHOUSE", "CWAREHOUSE_ID"): "wh",
        ("TBL_SYS_USER", "CUSER_ID"): "u",
        ("TBL_SYS_ORGANIZATION", "CORG_ID"): "org",
        ("TBL_SYS_ROLE", "CROLE_ID"): "role",
        ("TBL_BD_SUPPLIER", "CSUPPLIER_ID"): "sup",
        ("TBL_BD_GROUP", "GROUP_ID"): "grp",
        ("TBL_MO", "CMO_ID"): "mo",
        ("TBL_MO", "CMO_LOT"): "mo",
    }
    key = (dim_table, fact_col)
    if key in presets:
        a = presets[key]
    else:
        base = dim_table.replace("TBL_", "").lower()[:6]
        a = re.sub(r"[^a-z0-9]", "", base) or "dim"
    n = 1
    cand = a
    while cand in used:
        n += 1
        cand = f"{a}{n}"
    used.add(cand)
    return cand


def _mapping_id(fact_col: str, dim_table: str) -> str:
    known = {
        ("CWC_ID", "TBL_BD_WC"): "work_center",
        ("CPROCESS_ID", "TBL_BD_PROCESS"): "process",
        ("CITEM_ID", "TBL_BD_ITEM"): "item",
        ("CITEM_TYPE_ID", "TBL_BD_ITEM_TYPE"): "item_type",
        ("CUSTOMER_CODE", "TBL_BD_CUSTOMER"): "customer",
        ("CUST_CODE", "TBL_BD_CUSTOMER"): "customer",
        ("CDEVICE_ID", "TBL_EAP_DEVICE"): "device",
        ("CTAG_ID", "TBL_EAP_TAG"): "tag",
        ("CLOCATION_ID", "TBL_WMS_LOCATION"): "location",
        ("CWAREHOUSE_ID", "TBL_WMS_WAREHOUSE"): "warehouse",
        ("CORG_ID", "TBL_SYS_ORGANIZATION"): "organization",
        ("CROLE_ID", "TBL_SYS_ROLE"): "role",
        ("CSUPPLIER_ID", "TBL_BD_SUPPLIER"): "supplier",
        ("GROUP_ID", "TBL_BD_GROUP"): "group",
        ("CUSER_ID", "TBL_SYS_USER"): "user",
        ("USER_ID", "TBL_SYS_USER"): "user",
        ("CSTART_USER_NAME", "TBL_SYS_USER"): "start_user",
        ("CEND_USER_NAME", "TBL_SYS_USER"): "end_user",
        ("CCHECK_USER_NAME", "TBL_SYS_USER"): "check_user",
        ("CMO_ID", "TBL_MO"): "mo",
        ("CMO_LOT", "TBL_MO"): "mo_lot",
        ("CWS_LOG_ID", "TBL_SFC_WS_LOG"): "ws_log",
        ("CCONFIRMED_USER", "TBL_SYS_USER"): "confirmed_user",
        ("CUSER_CREATED", "TBL_SYS_USER"): "user_created",
        ("CUSER_MODIFIED", "TBL_SYS_USER"): "user_modified",
    }
    if (fact_col, dim_table) in known:
        return known[(fact_col, dim_table)]
    base = fact_col.lower().lstrip("c")
    dim_s = dim_table.replace("TBL_", "").lower()[:12]
    return f"{base}_to_{dim_s}"


def _is_user_account_col(col: str) -> bool:
    if col in USER_ACCOUNT_ALIASES:
        return True
    if col.endswith("_USER_NAME"):
        return True
    if col in (
        "CCONFIRMED_USER",
        "CUSER_CREATED",
        "CUSER_MODIFIED",
        "CASSAY_USER",
        "CLOGIN_USER",
        "CMACHINE_USER",
        "COPERATOR",
    ):
        return True
    return False


def _pick_display_cols(
    dim_table: str,
    dim_fields: Dict[str, str],
    dim_col: str,
) -> List[Tuple[str, str]]:
    """返回 [(sql_expr_suffix, 中文列名), ...]，expr 不含别名前缀。"""
    # 预置维表展示列
    profiles: Dict[str, List[Tuple[str, str]]] = {
        "TBL_BD_WC": [
            ("CWC_NAME", "工作中心名称"),
            ("CWC_NO", "工作中心编码"),
        ],
        "TBL_BD_PROCESS": [
            ("CPROCESS_NAME", "工序名称"),
            ("CPROCESS_NO", "工序编码"),
        ],
        "TBL_BD_ITEM": [
            ("CITEM_NO", "料号"),
            ("CITEM_NAME", "品名"),
        ],
        "TBL_BD_ITEM_TYPE": [
            ("CITEM_TYPE_NAME", "物料类型名称"),
            ("CITEM_TYPE_NO", "物料类型编码"),
        ],
        "TBL_BD_CUSTOMER": [
            ("CUSTOMER_NAME", "客户名称"),
            ("CUSTOMER_NO", "客户编号"),
        ],
        "TBL_EAP_DEVICE": [
            ("CDEVICE_NAME", "设备名称"),
            ("CDEVICE_ID", "设备编号"),
        ],
        "TBL_EAP_TAG": [
            ("CTAG_NAME", "测点名称"),
            ("CTAG_ID", "测点ID"),
        ],
        "TBL_WMS_LOCATION": [
            ("CLOCATION_NAME", "货位名称"),
            ("CLOCATION_CODE", "货位编码"),
        ],
        "TBL_WMS_WAREHOUSE": [
            ("CWAREHOUSE_NAME", "仓库名称"),
            ("CWAREHOUSE_CODE", "仓库编码"),
        ],
        "TBL_SYS_USER": [
            ("CDISPLAY_NAME", "用户姓名"),
            ("CUSER_NAME", "用户账号"),
        ],
        "TBL_SYS_ORGANIZATION": [
            ("CORG_NAME", "组织名称"),
            ("CORG_NO", "组织编码"),
        ],
        "TBL_SYS_ROLE": [
            ("CROLE_NAME", "角色名称"),
            ("CROLE_CODE", "角色编码"),
        ],
        "TBL_BD_SUPPLIER": [
            ("CSUPPLIER_NAME", "供应商名称"),
            ("CSUPPLIER_NO", "供应商编码"),
        ],
        "TBL_BD_GROUP": [
            ("CGROUP_NAME", "组别名称"),
            ("CGROUP_NO", "组别编码"),
        ],
        "TBL_MO": [
            ("CORDER_NO", "工单编号"),
            ("CMO_LOT", "工单批次"),
        ],
        "TBL_MSG_GROUP": [
            ("CGROUP_NAME", "群组名称"),
            ("CGROUP_CODE", "群组编码"),
        ],
        "TBL_MSG_TEMPLATE": [
            ("CTEMPLATE_NAME", "模板名称"),
        ],
        "TBL_MSG_EVENT": [
            ("CEVENT_NAME", "事件名称"),
        ],
        "TBL_MSG_ROBOT": [
            ("CROBOT_NAME", "机器人名称"),
        ],
        "TBL_NP_TEMPLATE": [
            ("CTEMPLATE_NAME", "模板名称"),
            ("CTEMPLATE_NO", "模板编码"),
        ],
        "TBL_SFC_WS_LOG": [
            ("CSCAN_BARCODE", "扫描条码"),
            ("CSTART_TIME", "开工时间"),
        ],
    }
    if dim_table in profiles:
        out = []
        for col, cn in profiles[dim_table]:
            if col in dim_fields:
                out.append((col, cn))
        if out:
            return out

    # 自动：优先 NAME/NO/编号类
    priority_suffix = ("_NAME", "_NO", "_CODE", "_LOT", "_NUMBER")
    candidates = []
    for col, cn in dim_fields.items():
        if col == "CID" or col == dim_col:
            continue
        for suf in priority_suffix:
            if col.endswith(suf) or suf.strip("_") in col:
                candidates.append((col, cn))
                break
    if not candidates and dim_fields:
        # 取第一个非 CID 字段
        for col, cn in dim_fields.items():
            if col != "CID":
                candidates.append((col, cn))
                break
    return candidates[:4]


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

    # ---- 工作中心两级 ----
    if dim_table == "TBL_BD_WC" and fact_col == "CWC_ID" and dim_col == "CID":
        joins.append(
            {
                "alias": "wc_p",
                "table": "TBL_BD_WC",
                "on": "wc_p.CID = wc.CPARENT",
                "depends_on": "wc",
            }
        )
        # 修正首个别名为 wc
        joins[0]["alias"] = "wc"
        on = f"wc.CID = {fact_alias}.CWC_ID"
        joins[0]["on"] = on
        used_aliases.add("wc_p")
        select = [
            {"expr": "COALESCE(wc_p.CWC_NAME, wc.CWC_NAME)", "as": "工作中心名称"},
            {"expr": "COALESCE(wc_p.CWC_NO, wc.CWC_NO)", "as": "工作中心编码"},
            {"expr": "wc.CWC_NAME", "as": "机台名称"},
            {"expr": "wc.CWC_NO", "as": "机台编码"},
        ]
        notes = "工作中心两级：父级如开料/钻孔；子级如1#开料机。报工 CWC_ID 多为机台。"
        if fact_table == "TBL_SFC_WS_LOG":
            forbidden = [
                "用 TBL_EAP_DEVICE 解析 CWC_ID",
                "p.CPROCESS_NAME AS [工作中心名称]",
                "仅 wc.CWC_NAME AS [工作中心名称] 且不输出 [机台名称]",
                "wc.CID = l.CPROCESS_ID 或 p.CID = l.CWC_ID",
            ]
        return {
            "id": mid,
            "fact_columns": [fact_col],
            "joins": joins,
            "select": select,
            "forbidden": forbidden,
            "notes": notes,
        }

    # ---- 人员账号 ----
    if dim_table == "TBL_SYS_USER" and _is_user_account_col(fact_col):
        match_type = "account"
        if fact_col == "CCHECK_USER_NAME":
            optional = True
        name_map = {
            "CSTART_USER_NAME": ("开工人账号", "开工人姓名"),
            "CEND_USER_NAME": ("完工人账号", "完工人姓名"),
            "CCHECK_USER_NAME": ("审核人账号", "审核人姓名"),
            "CCONFIRMED_USER": ("确认人账号", "确认人姓名"),
            "CUSER_CREATED": ("创建人账号", "创建人姓名"),
            "CUSER_MODIFIED": ("修改人账号", "修改人姓名"),
            "CASSAY_USER": ("化验人账号", "化验人姓名"),
            "CLOGIN_USER": ("登录人账号", "登录人姓名"),
            "CMACHINE_USER": ("操作用户账号", "操作用户姓名"),
            "COPERATOR": ("操作员账号", "操作员姓名"),
        }
        if fact_col in name_map:
            acc_cn, name_cn = name_map[fact_col]
        elif fact_col.endswith("_USER_NAME"):
            base = fact_cn.replace("账号", "").replace("用户", "") or fact_col
            acc_cn = f"{base}账号" if "账号" not in fact_cn else fact_cn
            name_cn = f"{base}姓名" if "姓名" not in fact_cn else fact_cn.replace("账号", "姓名")
        else:
            acc_cn = fact_cn if "账号" in fact_cn else f"{fact_cn}账号"
            name_cn = fact_cn.replace("账号", "姓名") if "账号" in fact_cn else f"{fact_cn}姓名"
        select = [
            {"expr": f"{fact_alias}.{fact_col}", "as": acc_cn},
            {"expr": f"{dim_a}.CDISPLAY_NAME", "as": name_cn},
        ]
        if fact_col == "CSTART_USER_NAME":
            forbidden = [f"{fact_col} AS [开工人姓名] 且无 JOIN TBL_SYS_USER"]
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

    # ---- 用户 ID ----
    if dim_table == "TBL_SYS_USER" and fact_col in ("CUSER_ID", "USER_ID"):
        on = f"{dim_a}.CID = {fact_alias}.{fact_col}"
        joins[0]["on"] = on
        select = [
            {"expr": f"{dim_a}.CDISPLAY_NAME", "as": "用户姓名"},
            {"expr": f"{dim_a}.CUSER_NAME", "as": "用户账号"},
        ]
        return {
            "id": mid,
            "fact_columns": [fact_col],
            "joins": joins,
            "select": select,
            "forbidden": forbidden,
            "notes": notes,
        }

    # ---- 标准维表列 ----
    display = _pick_display_cols(dim_table, dim_fields, dim_col)
    for col, cn in display:
        as_name = cn
        select.append({"expr": f"{dim_a}.{col}", "as": as_name})

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


# 已由维表 JOIN 展示、禁止裸输出的外键/关联列
SKIP_FACT_COLS = {
    "CITEM_ID",
    "CPROCESS_ID",
    "CWC_ID",
    "CITEM_TYPE_ID",
    "CDEVICE_ID",
    "CLOCATION_ID",
    "CWAREHOUSE_ID",
    "CUSER_ID",
    "USER_ID",
    "CMO_ID",
    "CWS_LOG_ID",
    "CMAIN_ID",
    "CSUPPLIER_ID",
    "CORG_ID",
    "CROLE_ID",
    "GROUP_ID",
    "CMO_LOT",
    "CUSTOMER_CODE",
    "CUST_CODE",
}


def _build_display_columns(
    fact_alias: str,
    fields: Dict[str, str],
    mappings: List[Dict[str, Any]],
) -> List[Dict[str, str]]:
    """本表非外键列：列表查询须 AS 中文字段名。"""
    mapped: set = set()
    for mp in mappings:
        mapped.update(mp.get("fact_columns") or [])
    skip = set(SKIP_FACT_COLS) | mapped
    for col in fields:
        if _is_user_account_col(col):
            skip.add(col)
    out: List[Dict[str, str]] = []
    for col, cn in fields.items():
        if col in skip:
            continue
        out.append({"expr": f"{fact_alias}.{col}", "as": cn})
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
        if mp.get("match_type") == "account":
            lines.append("类型=账号")
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
    # 收集 fact -> edges
    fact_edges: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)
    for fact, info in tables.items():
        for fc, dt, dc in info["relations"]:
            if fact == dt:
                continue
            fact_edges[fact].append((fc, dt, dc))

    # 优先输出顺序
    priority_facts = [
        "TBL_SFC_WS_LOG",
        "TBL_MO",
        "TBL_SFC_WS_LOG_ITEM",
        "TBL_QM_INSPECT_RECORD",
        "TBL_WMS_PI",
        "TBL_WMS_PS",
        "TBL_EAP_ALARM",
        "TBL_EAM_REPAIR",
        "TBL_MEP_MATERIAL_PARAM",
    ]
    ordered_facts = []
    for f in priority_facts:
        if f in fact_edges:
            ordered_facts.append(f)
    for f in sorted(fact_edges.keys()):
        if f not in ordered_facts:
            ordered_facts.append(f)

    header = """# =============================================================================
# 维表映射配置（由 generate_dimension_map_from_schema.py 根据表结构 V1.1 生成）
# 改完后运行：python3 build_dify_bundle.py → 复制 dify_mes_dimension_node.py 到 Dify
# 手工微调后可重新运行本脚本（会覆盖）；或只改本文件后 build_dify_bundle.py
# =============================================================================
#
# 写法说明：
#   [表 表名]           一张业务主表
#   标签=               中文说明
#   关键词=             用户问题里出现这些词时，选中该表（逗号分隔）
#   别名=               SQL 里事实表别名，如 l、m
#
#   [映射 英文名]       一组「事实字段 → 维表 → 中文列」
#   字段=               事实表上的列，多个用逗号分隔
#   类型=账号           仅人员账号字段填写（开工人、完工人等）
#   可选=是             不需要时可不写；写了表示可不生成该组
#   说明=               给维护人看的备注
#   关联=别名 | 维表 | ON条件 [| 依赖=上一别名]
#   列=SQL表达式 | 中文列名
#   展示列=表达式 | 中文列名   （本表非外键列，列表须 AS 中文表头）
#   禁止=               不要这样写 SQL
#
# [全局] 下「禁止=」对所有表生效

[全局]
默认别名=l
禁止=TBL_SFC_WS_LOG 上使用 CCUSTOMER_CODE（须 CUSTOMER_CODE）
禁止=TBL_SFC_WS_LOG 上使用 CSCANNED_BARCODE（须 CSCAN_BARCODE）
禁止=FROM/JOIN 表名与 WITH (NOLOCK) 拆成两行
禁止=用 TBL_EAP_DEVICE 解析 CWC_ID（工作中心/机台须 TBL_BD_WC）
禁止=p.CPROCESS_ID 作工序主键（须 p.CID = 事实表.CPROCESS_ID）
禁止=wc.CWC_NAME AS [工序名称] 或 p.CPROCESS_NAME AS [工作中心名称]

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
            if fc not in fact_info["fields"]:
                # 关联字段可能未在字段列表（如 GROUP_ID）
                pass
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
                # 同 id 合并字段（罕见）
                for existing in mappings:
                    if existing["id"] == mp["id"]:
                        existing["fact_columns"] = list(
                            dict.fromkeys(existing["fact_columns"] + mp["fact_columns"])
                        )
                        break
            else:
                seen_ids.add(mp["id"])
                mappings.append(mp)

        # 补充账号类字段 → TBL_SYS_USER（关系节未声明但列表需显示姓名）
        user_fields = [
            c
            for c in fact_info["fields"]
            if _is_user_account_col(c) and c not in {fc for fc, _, _ in edges}
        ]
        for col in user_fields:
            mid = _mapping_id(col, "TBL_SYS_USER")
            if mid not in seen_ids:
                mp = build_mapping(
                    fact_table,
                    col,
                    "TBL_SYS_USER",
                    "CUSER_NAME",
                    fact_alias,
                    tables["TBL_SYS_USER"]["fields"],
                    fact_info["fields"],
                    used_aliases,
                )
                seen_ids.add(mp["id"])
                mappings.append(mp)

        keywords = FACT_KEYWORDS.get(fact_table, [])
        if not keywords:
            keywords = [fact_info["short_label"]]

        display_columns = _build_display_columns(
            fact_alias, fact_info["fields"], mappings
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
    tables = parse_schema(md)
    content = generate_map(tables)
    OUT_MAP.write_text(content, encoding="utf-8")
    # 统计
    n_tables = content.count("[表 ")
    n_maps = content.count("[映射 ")
    print(f"已写入 {OUT_MAP.name}")
    print(f"  事实表: {n_tables}, 映射块: {n_maps}")


if __name__ == "__main__":
    main()
