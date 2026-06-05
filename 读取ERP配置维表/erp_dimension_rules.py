#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据 erp_dimension_joins.json 为指定事实表生成【维表映射规则】文本，供 Dify 注入
【新加强制约束】/ query_rules。

Dify 代码节点示例入参：
  - fact_table: "FGI_ReceiptItem"（可空，空则从 user_question 推断）
  - user_question: "查最近一个月生产记录"
  - mapping_ids: 可选，逗号分隔或列表，只生成部分映射（如 "work_center,process"）
  - config_json: 可选，erp_dimension_joins.json 全文（字符串）；Dify 无法读本地文件时用
  - config_path: 可选，json 文件路径（代码节点与 json 同目录上传时一般不必传）

配置加载优先级：config_json 参数 > 环境变量 ERP_DIMENSION_JOINS_JSON > config_path > 与 .py 同目录的 erp_dimension_joins.json

出参：
  - query_rules: 注入 LLM 的 Markdown 规则块
  - fact_table: 实际使用的事实表名
  - join_tables: 本次涉及维表列表（去重）

本地 CLI：
  python erp_dimension_rules.py FGI_ReceiptItem
  python erp_dimension_rules.py --question "制成品接收明细" 
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Union

try:
    _CONFIG_PATH = Path(__file__).resolve().parent / "erp_dimension_joins.json"
except NameError:
    _CONFIG_PATH = Path("erp_dimension_joins.json")
# 由 build_dify_bundle.py 注入；Dify 单文件代码节点依赖此项，无需同目录 json
_EMBEDDED_CONFIG: Optional[Dict[str, Any]] = None


def load_config(
    path: Optional[Union[str, Path]] = None,
    config_json: str = "",
) -> Dict[str, Any]:
    """加载映射配置。Dify 等环境优先传 config_json 或设环境变量 ERP_DIMENSION_JOINS_JSON。"""
    raw = (config_json or os.environ.get("ERP_DIMENSION_JOINS_JSON") or "").strip()
    if raw:
        return json.loads(raw)
    if path:
        p = Path(path)
        with p.open(encoding="utf-8") as f:
            return json.load(f)
    if _EMBEDDED_CONFIG is not None:
        return _EMBEDDED_CONFIG
    with _CONFIG_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def _normalize_table_name(name: str) -> str:
    """ERP 表名保留文档中的大小写（如 FGI_ReceiptItem）。"""
    return (name or "").strip()


def _resolve_table_key(name: str, tables: Dict[str, Any]) -> str:
    """与 parse_dimension_map 写入的大写表名对齐。"""
    n = _normalize_table_name(name)
    if not n:
        return n
    if n in tables:
        return n
    upper = n.upper()
    if upper in tables:
        return upper
    for key in tables:
        if key.upper() == upper:
            return key
    return upper


def infer_fact_table(
    user_question: str = "",
    fact_table: str = "",
    config: Optional[Dict[str, Any]] = None,
) -> str:
    cfg = config or load_config()
    tables: Dict[str, Any] = cfg.get("tables", {})
    explicit = _resolve_table_key(fact_table, tables) if fact_table else ""
    if explicit and explicit in tables:
        return explicit

    q = (user_question or "").strip()
    default_table = explicit or _resolve_table_key("FGI_ReceiptItem", tables)
    if default_table not in tables and tables:
        default_table = next(iter(tables))
    if not q:
        return default_table

    detail_hints = ("明细", "详情", "列表", "列出", "展示", "查看")
    scores: Dict[str, int] = {}
    for tname, tcfg in tables.items():
        score = 0
        for kw in tcfg.get("default_for_keywords") or []:
            if kw and kw in q:
                score += max(len(kw), 2)
        scores[tname] = score

    has_detail = any(h in q for h in detail_hints)
    item_key = _resolve_table_key("FGI_ReceiptItem", tables)
    receipt_key = _resolve_table_key("FGI_Receipt", tables)
    if has_detail and item_key:
        scores[item_key] = scores.get(item_key, 0) + 15
    if "接收" in q and not has_detail and receipt_key:
        scores[receipt_key] = scores.get(receipt_key, 0) + 12

    best_table = ""
    best_score = 0
    for tname, score in scores.items():
        if score > best_score:
            best_score = score
            best_table = tname
    if best_table:
        return best_table

    for tname in tables:
        if tname in q or tname.upper() in q.upper():
            return tname
    m = re.search(
        r"\b((?:T_|FGI_|M_|S_|F_|G_|P_|W_)[A-Za-z0-9_]+)\b",
        q,
    )
    if m:
        cand = _resolve_table_key(m.group(1), tables)
        if cand in tables:
            return cand

    return default_table


# 事实表混查时，除 JOIN 别名外常见的「直接 FROM」别名（ERP 主从表联查）
_COMPANION_DIRECT_ALIASES: Dict[str, Dict[str, str]] = {
    "FGI_ReceiptItem": {"fr": "FGI_Receipt"},
    "M_BOMIssueItem": {"mbi": "M_BOMIssue"},
    "M_BOMPicklistItem": {"bp": "M_BOMPicklist"},
    "P_WO": {"mo": "P_MO"},
}

# 用户问「××明细/详情」且未点名只要某几列时，SELECT 须包含该表全部展示列与映射列
_FULL_DETAIL_SELECT_TABLES: Set[str] = {
    "FGI_ReceiptItem",
    "M_PurchaseOrderItem",
    "M_BOMPicklistItem",
    "M_BOMIssueItem",
    "S_COMPLAINMENT",
}

# 同名 status/type 等字段在不同 ERP 表含义不同，混查时须分表译码
_STATUS_FIELD_DISAMBIG: Dict[str, str] = {
    "P_MO": "制造订单单据状态/投产类型 → 列名 [单据状态]/[投产类型]（与 P_WO.status 不同）",
    "P_WO": "工单状态（1外协/2未发放/3已发放/4暂停/5取消/6完成）→ 列名 [工单状态]",
    "M_BOMPicklist": "领料单审批状态（Pending/Approved）→ 列名 [审批状态]",
    "M_Requisitions": "请购单状态（Valid已审核/Active审核中）→ 列名 [请购单状态]",
    "S_Job": "产品型号审批状态 → 列名 [审批状态]（与 M_BOMPicklist 不同）",
    "FGI_Receipt": "接收单来源类型（Customer/Outsourcing）→ 列名 [来源类型]",
}


def _apply_alias(template: str, fact_alias: str) -> str:
    return template.replace(" l.", f" {fact_alias}.").replace("= l.", f"= {fact_alias}.")


def _replace_sql_alias(expr: str, old_alias: str, new_alias: str) -> str:
    if old_alias == new_alias:
        return expr
    return re.sub(
        rf"(?<![\w.]){re.escape(old_alias)}\.",
        f"{new_alias}.",
        expr,
    )


def _collect_join_aliases(fact_table: str, config: Dict[str, Any]) -> Dict[str, str]:
    """SQL 别名 → 维表名（来自事实表 mappings 中的 JOIN + 常见直接 FROM 别名）。"""
    tcfg = (config.get("tables") or {}).get(fact_table) or {}
    out: Dict[str, str] = {}
    for mp in tcfg.get("mappings") or []:
        for j in mp.get("joins") or []:
            alias = (j.get("alias") or "").strip()
            table = _normalize_table_name(j.get("table") or "")
            if alias and table:
                out[alias] = table
    for alias, table in (_COMPANION_DIRECT_ALIASES.get(fact_table) or {}).items():
        out.setdefault(alias, table)
    return out


def _iter_table_enum_selects(
    tcfg: Dict[str, Any],
    target_alias: str,
    *,
    config: Optional[Dict[str, Any]] = None,
) -> List[Tuple[str, str, List[str]]]:
    """(expr, as_name, fact_columns) — 将配置默认别名替换为 target_alias。"""
    cfg = config or {}
    default_alias = (
        tcfg.get("fact_alias") or cfg.get("default_fact_alias") or "l"
    ).strip()
    out: List[Tuple[str, str, List[str]]] = []
    seen: Set[str] = set()

    def _push(expr: str, as_name: str, fcols: Sequence[str]) -> None:
        if not expr.upper().startswith("CASE "):
            return
        sql = _replace_sql_alias(expr, default_alias, target_alias)
        key = f"{sql}|{as_name}"
        if key in seen:
            return
        seen.add(key)
        out.append((sql, as_name, list(fcols)))

    for mp in tcfg.get("mappings") or []:
        if mp.get("match_type") != "enum":
            continue
        fcols = mp.get("fact_columns") or []
        for sel in mp.get("select") or []:
            _push(sel.get("expr") or "", sel.get("as") or "", fcols)
    return out


def _append_mixed_table_enum_rules(
    lines: List[str],
    fact_table: str,
    fact_alias: str,
    config: Dict[str, Any],
) -> None:
    """ERP 主从/联表混查：为 JOIN 表及常见别名追加独立枚举 CASE，避免 status/type 等同名字段串表。"""
    join_aliases = _collect_join_aliases(fact_table, config)
    if not join_aliases:
        return

    blocks: List[str] = []
    for join_alias, joined_table in sorted(join_aliases.items()):
        if joined_table == fact_table:
            continue
        jtcfg = (config.get("tables") or {}).get(joined_table)
        if not jtcfg:
            continue
        enums = _iter_table_enum_selects(jtcfg, join_alias, config=config)
        if not enums:
            continue
        jlabel = jtcfg.get("label") or joined_table
        disambig = _STATUS_FIELD_DISAMBIG.get(joined_table, "")
        block_lines = [
            f"#### `{joined_table}`（{jlabel}）·SQL 别名 **`{join_alias}`**",
        ]
        if disambig:
            block_lines.append(
                f"- **分表说明**：{disambig}；**禁止**与 `{fact_table}`/`{fact_alias}` 同名字段混用裸码。"
            )
        for expr, as_name, fcols in enums:
            fcol_txt = ", ".join(fcols) if fcols else "见表达式"
            block_lines.append(f"- 字段 **{fcol_txt}**：必须 `{expr} AS [{as_name}]`")
            if fcols:
                block_lines.append(
                    f"  - 禁止：`{join_alias}.{fcols[0]} AS [{as_name}]`"
                )
            else:
                block_lines.append(f"  - 禁止裸码 AS [{as_name}]")
        blocks.extend(block_lines)
        blocks.append("")

    if not blocks:
        return

    lines.append(
        "### 【混查·关联表枚举译码】（与事实表**分表处理**；"
        "SELECT 含下列列且来自关联表时，**必须**用本段 CASE，禁止裸 `0`/`Y`/`N`）"
    )
    lines.append(
        f"- 事实表 `{fact_table}`（别名 `{fact_alias}`）与下列表**同名不同义**（尤其 `status`/`type`），"
        "不可互用 CASE 或裸字段。"
    )
    lines.extend(blocks)


def _join_line(alias: str, table: str, on: str, fact_alias: str) -> str:
    on_sql = _apply_alias(on, fact_alias)
    return f"LEFT JOIN dbo.{table} {alias} WITH (NOLOCK) ON {on_sql}"


def build_query_rules(
    fact_table: str,
    *,
    config: Optional[Dict[str, Any]] = None,
    mapping_ids: Optional[Sequence[str]] = None,
    fact_alias: Optional[str] = None,
) -> str:
    cfg = config or load_config()
    tables: Dict[str, Any] = cfg.get("tables", {})
    tname = _resolve_table_key(fact_table, tables)
    if tname not in tables:
        known = ", ".join(sorted(tables.keys()))
        return (
            f"【维表映射规则】未配置事实表 `{tname}`。"
            f"请在 erp_dimension_joins.json 的 tables 中补充。当前已配置：{known}"
        )

    tcfg = tables[tname]
    alias = (fact_alias or tcfg.get("fact_alias") or cfg.get("default_fact_alias") or "l").strip()
    label = tcfg.get("label") or tname
    mappings: List[Dict[str, Any]] = tcfg.get("mappings") or []

    id_filter: Optional[Set[str]] = None
    if mapping_ids:
        id_filter = {str(x).strip() for x in mapping_ids if str(x).strip()}

    full_detail = tname in _FULL_DETAIL_SELECT_TABLES
    lines: List[str] = [
        f"【维表映射规则·自动生成】事实表：**{tname}**（{label}），别名 **`{alias}`**。",
        "生成 SQL 时**必须**按下述 JOIN 与 SELECT 展示列执行（片段无对应维表则跳过该条并在【相关表】说明）。",
        "**列表/明细查询**：`SELECT` 中**每一个**输出列都必须 `AS [中文列名]`，禁止裸写 `fr.code` 等英文字段名作为表头。",
    ]
    if full_detail:
        lines.append(
            "**本表为 ERP 明细表**：用户问某单号+明细/详情且**未**点名只要某几列时，"
            "`SELECT` 须包含下文**全部**「事实表本表列」与各映射「必须列」，"
            "禁止只输出主键、外键 ID、单号、单位、数量、备注等少量列。"
        )
    default_ob = (tcfg.get("default_order_by") or "").strip()
    if default_ob:
        lines.append(
            f"**无时间 WHERE 的明细列表**：末尾须 `ORDER BY {default_ob}`（由近到远）；"
            "用户只要 `COUNT(*)` 或含 `GROUP BY` 汇总时除外。"
        )
    lines.append("")

    mandatory_decodes: List[str] = []
    for mp in mappings:
        for sel in mp.get("select") or []:
            expr = sel.get("expr") or ""
            if expr.upper().startswith("CASE "):
                mandatory_decodes.append(
                    f"{_apply_alias(expr, alias)} AS [{sel.get('as') or ''}]"
                )
    for dc in tcfg.get("display_columns") or []:
        expr = dc.get("expr") or ""
        if expr.upper().startswith("CASE "):
            mandatory_decodes.append(
                f"{_apply_alias(expr, alias)} AS [{dc.get('as') or ''}]"
            )
    enum_mps = [mp for mp in mappings if mp.get("match_type") == "enum"]
    if enum_mps:
        lines.append(
            "### 【最高优先级·枚举/码值译码】（下列列必须**整段**写入 SELECT，"
            "禁止 `er.status`/`er.approveStatus` 等裸字段或裸码值）"
        )
        for mp in enum_mps:
            fcols = ", ".join(mp.get("fact_columns") or [])
            lines.append(f"- 字段 **{fcols}**：")
            for sel in mp.get("select") or []:
                expr = _apply_alias(sel.get("expr") or "", alias)
                as_name = sel.get("as") or ""
                lines.append(f"  - 必须：`{expr} AS [{as_name}]`")
            for fb in mp.get("forbidden") or []:
                lines.append(f"  - 禁止：{fb}")
        lines.append("")

    _append_mixed_table_enum_rules(lines, tname, alias, cfg)

    if mandatory_decodes:
        lines.append("### 【强制·状态码译码】（下列表达式必须原样写入 SELECT，禁止改为裸数字/码值列）")
        for item in mandatory_decodes:
            lines.append(f"  - `{item}`")
        lines.append("")

    display_cols: List[Dict[str, Any]] = tcfg.get("display_columns") or []
    if display_cols:
        dc_title = (
            "### 【必须·事实表本表列】（须**全部**写入 SELECT，禁止只选子集）"
            if full_detail
            else "### 事实表本表列（须 `AS` 中文别名，勿裸列名）"
        )
        lines.append(dc_title)
        for dc in display_cols:
            expr = _apply_alias(dc.get("expr") or "", alias)
            as_name = dc.get("as") or ""
            lines.append(f"  - `{expr} AS [{as_name}]`")
        lines.append("- **禁止**：本表列无 `AS`（如 `fr.status`）；外键 *Id 列单独展示（须用下方维表中文列替代）。")
        lines.append("")

    seen_joins: Set[str] = set()
    select_parts: List[str] = []

    for mp in mappings:
        mid = mp.get("id") or ""
        if id_filter is not None and mid not in id_filter:
            continue
        if mp.get("optional") and id_filter is None:
            pass

        fact_cols = mp.get("fact_columns") or []
        lines.append(f"### 映射 `{mid}`（事实列：{', '.join(fact_cols)}）")
        if mp.get("notes"):
            lines.append(f"- 说明：{mp['notes']}")
        elif mp.get("match_type") == "enum":
            lines.append("- 类型：**枚举译码**（本表字段，无需 JOIN；`SELECT` 必须用下方 CASE，禁止裸数字列）。")

        joins = mp.get("joins") or []
        if joins:
            lines.append("- **JOIN**（逐条写出，勿省略 `ON`）：")
        elif mp.get("match_type") != "enum":
            lines.append("- **JOIN**（逐条写出，勿省略 `ON`）：")
        for j in joins:
            jl = _join_line(
                j.get("alias") or "dim",
                j.get("table") or "",
                j.get("on") or "",
                alias,
            )
            if jl not in seen_joins:
                seen_joins.add(jl)
            lines.append(f"  - `{jl}`")

        sel_label = (
            "- **SELECT 必须列**（须写入 SELECT，替代裸 ID/裸账号）："
            if full_detail
            else "- **SELECT 推荐列**（替代裸 ID/裸账号）："
        )
        lines.append(sel_label)
        for sel in mp.get("select") or []:
            expr = _apply_alias(sel.get("expr") or "", alias)
            as_name = sel.get("as") or ""
            select_parts.append(f"{expr} AS [{as_name}]")
            lines.append(f"  - `{expr} AS [{as_name}]`")

        for fb in mp.get("forbidden") or []:
            lines.append(f"- **禁止**：{fb}")
        lines.append("")

    globals_fb: List[str] = cfg.get("global_forbidden") or []
    if globals_fb:
        lines.append("### 全局禁止")
        for fb in globals_fb:
            lines.append(f"- {fb}")
        lines.append("")

    lines.append("### 定稿自检")
    lines.append(
        f"- 是否已 `FROM dbo.{tname} {alias} WITH (NOLOCK)`（hint 与表名**同一行**，禁止换行写 `WITH`）；"
        f"是否已包含上述全部 LEFT JOIN；"
        f"人员/工厂/物料/客户等列是否来自对应维表（T_User.recId、M_Materials.recId 等）而非裸 ID；"
        f"**SELECT 每一列是否均有 `AS [中文名]`（含本表时间/状态/备注等列）**。"
    )
    if default_ob:
        lines.append(
            f"- 无时间条件的明细是否已 `ORDER BY {default_ob}`（由近到远）；纯 `COUNT(*)` 除外。"
        )
    if full_detail:
        lines.append(
            "- **明细列全集**：`SELECT` 是否已包含上文全部「事实表本表列」与各映射「必须列」；"
            "是否**未**裸输出 `*Id` 外键；是否**未**只选少量列子集。"
        )

    return "\n".join(lines).strip()


# 查询结果列名 -> 码值 -> 中文（LLM 仍输出裸码时的兜底，键统一为字符串）
RESULT_COLUMN_VALUE_MAPS: Dict[str, Dict[str, str]] = {
    "审批状态": {
        "Pending": "制作中",
        "Approved": "审批通过",
        "Submit": "提交",
        "Waiting": "审批中",
        "Rejected": "拒绝",
    },
    "销售类型": {
        "Bonded": "保税",
        "ForDomestic": "内销",
        "ForExport": "外销",
    },
    "投产类型": {
        "SO": "正常投产(销售订单)",
        "ReturnRepair": "退货返修",
        "Replenishment": "补货",
        "StockRepair": "仓库返修",
        "ProVote": "生产补投",
        "Merger": "合拼",
        "MakeToStock": "存货补投",
    },
    "来源类型": {
        "Customer": "客户",
        "Outsourcing": "供应商",
    },
    "接收类型": {
        "PO": "有采购接收",
        "NPO": "无采购接收",
        "MiscPO": "杂项采购接收",
        "C": "寄售接收",
    },
    "采购类型": {
        "S": "采购",
        "M": "杂项",
    },
    "请购单状态": {
        "Valid": "已审核",
        "Active": "审核中",
    },
    "工单状态": {
        "1": "外协",
        "2": "未发放",
        "3": "已发放",
        "4": "暂停",
        "5": "取消",
        "6": "完成",
    },
    "是否已审核": {"Y": "是", "N": "否", "y": "是", "n": "否"},
}


def _select_rewrite_pairs(
    tcfg: Dict[str, Any],
    alias: str,
    *,
    config: Optional[Dict[str, Any]] = None,
) -> List[Tuple[str, str]]:
    """返回 (裸 SELECT 片段, CASE 片段) 列表。"""
    cfg = config or {}
    default_alias = (
        tcfg.get("fact_alias") or cfg.get("default_fact_alias") or "l"
    ).strip()
    pairs: List[Tuple[str, str]] = []
    seen: Set[str] = set()

    def _add(case_expr: str, as_name: str, fact_cols: Sequence[str]) -> None:
        case_sql = _replace_sql_alias(case_expr, default_alias, alias)
        full = f"{case_sql} AS [{as_name}]"
        if full in seen:
            return
        seen.add(full)
        cols = list(fact_cols) or []
        if not cols:
            m = re.search(rf"\b{re.escape(alias)}\.(\w+)", case_sql, re.I)
            if m:
                cols = [m.group(1)]
        for fc in cols:
            col_ref = fc
            if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", fc):
                col_ref = f"[{fc}]"
            for bare in (
                f"{alias}.{col_ref} AS [{as_name}]",
                f"{alias}.{fc} AS [{as_name}]",
                f"{fc} AS [{as_name}]",
                f"{alias}.{fc} AS [状态]",
            ):
                pairs.append((bare, full))

    for mp in tcfg.get("mappings") or []:
        fcols = mp.get("fact_columns") or []
        for sel in mp.get("select") or []:
            expr = sel.get("expr") or ""
            if expr.upper().startswith("CASE "):
                _add(expr, sel.get("as") or "", fcols)
    for dc in tcfg.get("display_columns") or []:
        expr = dc.get("expr") or ""
        if expr.upper().startswith("CASE "):
            _add(expr, dc.get("as") or "", [])
    return pairs


def _detect_sql_table_aliases(sql: str) -> Dict[str, str]:
    """SQL 别名 → 表名（FROM/JOIN dbo.ERP表 alias WITH (NOLOCK)）。"""
    out: Dict[str, str] = {}
    for m in re.finditer(
        r"(?:FROM|JOIN)\s+dbo\.("
        r"(?:T_|FGI_|M_|S_|F_|G_|P_|W_|E_|EQ_|PM_)[A-Za-z0-9_]+"
        r")\s+(\w+)\s+WITH\s*(?:\(\s*)?NOLOCK",
        sql,
        re.I,
    ):
        out[m.group(2)] = m.group(1)
    return out


def apply_sql_display_rewrites(
    sql: str,
    fact_table: str = "",
    config: Optional[Dict[str, Any]] = None,
) -> str:
    """将 SELECT 中的裸状态列替换为配置里的 CASE 译码表达式。"""
    if not sql or not str(sql).strip():
        return sql
    cfg = config or load_config()
    tables: Dict[str, Any] = cfg.get("tables") or {}
    out = sql

    alias_map = _detect_sql_table_aliases(sql)
    if alias_map:
        for alias, tname in alias_map.items():
            tcfg = tables.get(_resolve_table_key(tname, tables))
            if not tcfg:
                continue
            for bare, full in _select_rewrite_pairs(tcfg, alias, config=cfg):
                out = re.sub(re.escape(bare), full, out, flags=re.IGNORECASE)
        return out

    check_tables: List[str] = []
    if fact_table:
        t = _resolve_table_key(fact_table, tables)
        if t in tables:
            check_tables.append(t)
    else:
        upper = sql.upper()
        for tname in tables:
            if tname in upper:
                check_tables.append(tname)

    for tname in check_tables:
        tcfg = tables[tname]
        alias = (tcfg.get("fact_alias") or cfg.get("default_fact_alias") or "l").strip()
        for bare, full in _select_rewrite_pairs(tcfg, alias, config=cfg):
            out = re.sub(re.escape(bare), full, out, flags=re.IGNORECASE)
    return out


def decode_result_rows(
    rows: List[Dict[str, Any]],
    fact_table: str = "",
    config: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """结果集展示兜底：将仍为数字/字符串码的列译成中文。"""
    if not rows:
        return rows
    maps = dict(RESULT_COLUMN_VALUE_MAPS)
    cfg = config or load_config()
    tname = _resolve_table_key(fact_table, cfg.get("tables") or {})
    tcfg = (cfg.get("tables") or {}).get(tname) or {}
    def _merge_case_map(expr: str, as_name: str) -> None:
        if not as_name or not expr.upper().startswith("CASE "):
            return
        value_map: Dict[str, str] = {}
        for m in re.finditer(r"WHEN\s+(\d+)\s+THEN\s+N'([^']*)'", expr, re.I):
            value_map[str(m.group(1))] = m.group(2)
        for m in re.finditer(
            r"WHEN\s+(?:N')?'([^']+)'\s+THEN\s+N'([^']*)'", expr, re.I
        ):
            code = m.group(1)
            value_map[code] = m.group(2)
            value_map[code.upper()] = m.group(2)
        if value_map:
            maps[as_name] = value_map

    for mp in tcfg.get("mappings") or []:
        for sel in mp.get("select") or []:
            _merge_case_map(sel.get("expr") or "", sel.get("as") or "")
    for dc in tcfg.get("display_columns") or []:
        _merge_case_map(dc.get("expr") or "", dc.get("as") or "")

    out: List[Dict[str, Any]] = []
    for row in rows:
        new_row = dict(row)
        for col, value_map in maps.items():
            if col not in new_row:
                continue
            val = new_row[col]
            if val is None:
                continue
            key = str(val).strip()
            if key in value_map:
                new_row[col] = value_map[key]
        out.append(new_row)
    return out


def list_join_tables(fact_table: str, config: Optional[Dict[str, Any]] = None) -> List[str]:
    cfg = config or load_config()
    tname = _resolve_table_key(fact_table, cfg.get("tables") or {})
    tcfg = (cfg.get("tables") or {}).get(tname) or {}
    out: List[str] = []
    seen: Set[str] = set()
    for mp in tcfg.get("mappings") or []:
        for j in mp.get("joins") or []:
            tbl = j.get("table")
            if tbl and tbl not in seen:
                seen.add(tbl)
                out.append(tbl)
    return out


def build_enrichment_plan(
    fact_table: str,
    column_names: Sequence[str],
    config: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """
    查询结果仍为 ID/账号时，生成补全用的探测 SQL 模板（由下游执行后把结果传入 enrich_rows）。

    返回列表项：dim_table, key_column, value_columns, sql_template
    """
    cfg = config or load_config()
    tname = _resolve_table_key(fact_table, cfg.get("tables") or {})
    tcfg = (cfg.get("tables") or {}).get(tname) or {}
    alias = tcfg.get("fact_alias") or "l"
    cols = {c.upper() for c in column_names}
    plans: List[Dict[str, Any]] = []

    for mp in tcfg.get("mappings") or []:
        fact_cols = [c.upper() for c in (mp.get("fact_columns") or [])]
        if not any(fc in cols for fc in fact_cols):
            continue
        match_type = mp.get("match_type") or "id"
        for j in mp.get("joins") or []:
            dim = j.get("table")
            if not dim:
                continue
            if match_type == "account":
                fc = fact_cols[0]
                plans.append(
                    {
                        "mapping_id": mp.get("id"),
                        "dim_table": dim,
                        "fact_column": fc,
                        "sql": (
                            f"SELECT DISTINCT u.recId, u.employeeName, u.loginName "
                            f"FROM dbo.{dim} u WITH (NOLOCK) "
                            f"WHERE u.loginName IN ({{values}})"
                        ),
                    }
                )
            else:
                on = _apply_alias(j.get("on") or "", alias)
                m = re.search(
                    r"(\w+)\.recId\s*=\s*" + re.escape(alias) + r"\.(\w+)",
                    on,
                    re.I,
                )
                if m:
                    dim_key, fact_col = m.group(1), m.group(2)
                    name_cols = []
                    for sel in mp.get("select") or []:
                        ex = sel.get("expr") or ""
                        if dim_key in ex:
                            name_cols.append(ex.split(".")[-1])
                    plans.append(
                        {
                            "mapping_id": mp.get("id"),
                            "dim_table": dim,
                            "fact_column": fact_col,
                            "sql": (
                                f"SELECT d.recId, d.{name_cols[0] if name_cols else 'name'} "
                                f"FROM dbo.{dim} d WITH (NOLOCK) WHERE d.recId IN ({{values}})"
                            ),
                        }
                    )
            break
    return plans


def enrich_rows(
    rows: List[Dict[str, Any]],
    fact_table: str,
    lookups: Dict[str, Dict[Any, Dict[str, Any]]],
    config: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """
  用已查回的维表字典补全结果行。

  lookups 结构示例：
    {
      "work_center": { 123: {"工作中心名称": "开料", "机台名称": "1#开料机"}, ... },
      "start_user": { "001855": {"开工人姓名": "张三"}, ... }
    }
  键为 erp_dimension_joins.json 中的 mapping id。
    """
    if not rows or not lookups:
        return rows

    cfg = config or load_config()
    tname = _resolve_table_key(fact_table, cfg.get("tables") or {})
    tcfg = (cfg.get("tables") or {}).get(tname) or {}
    col_to_mapping: Dict[str, str] = {}
    for mp in tcfg.get("mappings") or []:
        mid = mp.get("id") or ""
        for fc in mp.get("fact_columns") or []:
            col_to_mapping[fc.upper()] = mid

    out: List[Dict[str, Any]] = []
    for row in rows:
        new_row = dict(row)
        for fc, mid in col_to_mapping.items():
            if fc not in {k.upper(): k for k in row.keys()}:
                continue
            raw_key = next((k for k in row if k.upper() == fc), None)
            if raw_key is None:
                continue
            val = row[raw_key]
            lk = lookups.get(mid) or {}
            extra = lk.get(val) or lk.get(str(val)) or {}
            for k, v in extra.items():
                if k not in new_row or new_row.get(k) in (None, "", val):
                    new_row[k] = v
        out.append(new_row)
    return out


def main(
    fact_table: str = "",
    user_question: str = "",
    mapping_ids: Any = None,
    config_path: str = "",
    config_json: str = "",
) -> Dict[str, Any]:
    if (config_json or "").strip():
        cfg = load_config(config_json=config_json)
    elif config_path:
        cfg = load_config(path=config_path)
    else:
        cfg = load_config()
    table = infer_fact_table(user_question, fact_table, cfg)

    mids: Optional[List[str]] = None
    if mapping_ids:
        if isinstance(mapping_ids, str):
            mids = [x.strip() for x in mapping_ids.split(",") if x.strip()]
        elif isinstance(mapping_ids, (list, tuple)):
            mids = [str(x).strip() for x in mapping_ids if str(x).strip()]

    rules = build_query_rules(table, config=cfg, mapping_ids=mids)
    out: Dict[str, Any] = {
        "query_rules": rules,
        "fact_table": table,
        "join_tables": ",".join(list_join_tables(table, cfg)),
    }
    return out


def main_with_sql(
    user_question: str = "",
    query_sql: str = "",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Dify 扩展：可选传入 query_sql，返回修正后的 query_sql。"""
    out = main(user_question=user_question, **kwargs)
    sql = (query_sql or "").strip()
    if sql:
        cfg = load_config(
            config_json=kwargs.get("config_json") or "",
            path=kwargs.get("config_path") or None,
        )
        out["query_sql"] = sql
        rewritten = apply_sql_display_rewrites(
            sql, fact_table=out.get("fact_table") or "", config=cfg
        )
        from erp_sql_fix_core import fix_erp_sql

        out["query_sql_fixed"] = fix_erp_sql(rewritten)
        out["fixed_sql"] = out["query_sql_fixed"]
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="生成 ERP 维表映射规则文本")
    parser.add_argument(
        "fact_table",
        nargs="?",
        default="",
        help="事实表名，如 FGI_ReceiptItem（配置内为大写 FGI_RECEIPTITEM）",
    )
    parser.add_argument("-q", "--question", default="", help="用户问题，用于推断事实表")
    parser.add_argument("-m", "--mappings", default="", help="只包含的 mapping id，逗号分隔")
    parser.add_argument("-c", "--config", default="", help="json 配置路径")
    args = parser.parse_args()

    mids = [x.strip() for x in args.mappings.split(",") if x.strip()] or None
    cfg = load_config(args.config) if args.config else load_config()
    table = infer_fact_table(args.question, args.fact_table, cfg)
    text = build_query_rules(table, config=cfg, mapping_ids=mids)
    print(text)
    print("\n--- join_tables ---")
    print(", ".join(list_join_tables(table, cfg)))
