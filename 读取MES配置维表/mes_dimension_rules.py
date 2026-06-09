#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据 mes_dimension_joins.json 为指定事实表生成【维表映射规则】文本，供 Dify 注入
【新加强制约束】/ query_rules。

Dify 代码节点示例入参：
  - fact_table: "TBL_SFC_WS_LOG"（可空，空则从 user_question 推断）
  - user_question: "查最近一个月生产记录"
  - mapping_ids: 可选，逗号分隔或列表，只生成部分映射（如 "work_center,process"）
  - config_json: 可选，mes_dimension_joins.json 全文（字符串）；Dify 无法读本地文件时用
  - config_path: 可选，json 文件路径（代码节点与 json 同目录上传时一般不必传）

配置加载优先级：config_json 参数 > 环境变量 MES_DIMENSION_JOINS_JSON > config_path > 与 .py 同目录的 mes_dimension_joins.json

出参：
  - query_rules: 注入 LLM 的 Markdown 规则块
  - fact_table: 实际使用的事实表名
  - join_tables: 本次涉及维表列表（去重）

本地 CLI：
  python mes_dimension_rules.py TBL_SFC_WS_LOG
  python mes_dimension_rules.py --question "生产记录" 
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Union

_CONFIG_PATH = Path(__file__).resolve().parent / "mes_dimension_joins.json"
# 由 build_dify_bundle.py 注入；Dify 单文件代码节点依赖此项，无需同目录 json
_EMBEDDED_CONFIG: Optional[Dict[str, Any]] = None


def load_config(
    path: Optional[Union[str, Path]] = None,
    config_json: str = "",
) -> Dict[str, Any]:
    """加载映射配置。Dify 等环境优先传 config_json 或设环境变量 MES_DIMENSION_JOINS_JSON。"""
    raw = (config_json or os.environ.get("MES_DIMENSION_JOINS_JSON") or "").strip()
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
    n = (name or "").strip().upper()
    if not n:
        return ""
    if not n.startswith("TBL_"):
        if n.startswith("SFC_") or n.startswith("BD_") or n.startswith("MO"):
            n = "TBL_" + n
    return n


def infer_fact_table(
    user_question: str = "",
    fact_table: str = "",
    config: Optional[Dict[str, Any]] = None,
) -> str:
    explicit = _normalize_table_name(fact_table)
    if explicit and (config is None or explicit in config.get("tables", {})):
        return explicit

    cfg = config or load_config()
    tables: Dict[str, Any] = cfg.get("tables", {})
    q = (user_question or "").strip()
    if not q:
        return explicit or "TBL_SFC_WS_LOG"

    ws_log_hints = (
        "生产记录", "报工", "工位", "WS_LOG", "开工", "完工",
        "是否已审核", "是否完工", "是否已过数", "工作数量", "工作类型",
    )
    mo_hints = ("工单", "MO_LOT", "批次", "生产工单")
    detail_hints = ("明细", "详情", "列表", "列出", "展示", "查看")
    agg_hints = ("统计", "数量", "多少", "个数", "合计", "总计", "COUNT")

    scores: Dict[str, int] = {}
    for tname, tcfg in tables.items():
        score = 0
        for kw in tcfg.get("default_for_keywords") or []:
            if kw and kw in q:
                score += max(len(kw), 2)
        scores[tname] = score

    has_detail = any(h in q for h in detail_hints)
    has_agg = any(h in q for h in agg_hints)
    has_ws = any(h in q for h in ws_log_hints)
    has_mo = any(h in q for h in mo_hints)

    if has_ws:
        scores["TBL_SFC_WS_LOG"] = scores.get("TBL_SFC_WS_LOG", 0) + 12
    if has_detail and has_ws:
        scores["TBL_SFC_WS_LOG"] = scores.get("TBL_SFC_WS_LOG", 0) + 25
    if has_detail and has_mo and not has_agg:
        scores["TBL_SFC_WS_LOG"] = scores.get("TBL_SFC_WS_LOG", 0) + 18
    if has_mo and has_agg and not has_ws:
        scores["TBL_MO"] = scores.get("TBL_MO", 0) + 20
    if "生产工单" in q and has_agg:
        scores["TBL_MO"] = scores.get("TBL_MO", 0) + 15

    po_detail_hints = (
        "采购订单明细", "采购单明细", "采购明细", "PO明细", "采购订单行",
    )
    po_detail_context = has_detail or any(
        h in q for h in ("明细", "详情", "行项目", "物料行")
    )
    if any(h in q for h in po_detail_hints) or (
        po_detail_context and re.search(r"\bP[OA]\w+", q, re.I)
    ):
        scores["TBL_SRM_PO_DETAIL"] = scores.get("TBL_SRM_PO_DETAIL", 0) + 30

    po_master_hints = ("采购单", "采购订单", "SRM采购")
    if (
        any(h in q for h in po_master_hints)
        and not po_detail_context
        and "交付" not in q
    ):
        scores["TBL_SRM_PO"] = scores.get("TBL_SRM_PO", 0) + 28

    maintain_hints = ("保养任务", "保养计划", "设备保养")
    if any(h in q for h in maintain_hints) and "维修" not in q:
        scores["TBL_EAM_MAINTAIN_TASK"] = scores.get("TBL_EAM_MAINTAIN_TASK", 0) + 22

    best_table = ""
    best_score = 0
    for tname, score in scores.items():
        if score > best_score:
            best_score = score
            best_table = tname
    if best_table:
        return best_table

    m = re.search(r"\b(TBL_[A-Z0-9_]+)\b", q, re.I)
    if m:
        cand = _normalize_table_name(m.group(1))
        if cand in tables:
            return cand

    return explicit or "TBL_SFC_WS_LOG"


# 事实表混查时，除 JOIN 别名外常见的「直接 FROM」别名（如工单语境下仍 FROM 生产记录表 l）
_COMPANION_DIRECT_ALIASES: Dict[str, Dict[str, str]] = {
    "TBL_MO": {"l": "TBL_SFC_WS_LOG"},
}

# 用户问「××明细/详情」且未点名只要某几列时，SELECT 须包含该表全部展示列与映射列
_FULL_DETAIL_SELECT_TABLES: Set[str] = {"TBL_SRM_PO_DETAIL"}

# 同名 CSTATUS 等字段在不同表含义不同，混查时须分表译码
_STATUS_FIELD_DISAMBIG: Dict[str, str] = {
    "TBL_SFC_WS_LOG": "生产记录审核状态（0待审核/1已通过/2已驳回）→ 列名 [状态]",
    "TBL_MO": "工单发放状态（2已发放/5已取消/6已暂停/7外协）→ 列名 [工单状态]",
    "TBL_EAM_REPAIR": "维修工单状态（英文码）→ 列名 [工单状态]",
    "TBL_QM_INSPECT_RECORD": "检验状态 → 列名 [状态]（与生产记录 [状态] 不同）",
    "TBL_SFC_PACKAGE": "包装条码状态 → JOIN TBL_SYS_DICTIONARY 取 CDIC_DESC，列名 [状态]（非库存状态）",
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
    """工单/生产记录等混查：为 JOIN 表及常见别名追加独立枚举 CASE，避免 CSTATUS 等同名字段串表。"""
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
        f"- 事实表 `{fact_table}`（别名 `{fact_alias}`）与下列表**同名不同义**（尤其 `CSTATUS`），"
        "不可互用 CASE 或裸字段。"
    )
    lines.extend(blocks)


def _join_line(alias: str, table: str, on: str, fact_alias: str) -> str:
    on_sql = _apply_alias(on, fact_alias)
    return f"LEFT JOIN dbo.{table} {alias} WITH (NOLOCK) ON {on_sql}"


def _compact_join_triggers(mappings: List[Dict[str, Any]]) -> str:
    """从映射推导「按需 JOIN」触发词，避免 EAM 文案套到 SFC 等表。"""
    hints: List[str] = []
    dim_tables: set[str] = set()
    has_account = False
    for mp in mappings:
        if mp.get("match_type") == "enum" or not mp.get("joins"):
            continue
        if mp.get("match_type") == "account":
            has_account = True
        for j in mp.get("joins") or []:
            dim_tables.add((j.get("table") or "").upper())
    if has_account:
        hints.append("人员/姓名/账号")
    if "TBL_BD_WC" in dim_tables:
        hints.append("机台/工作中心")
    if "TBL_BD_CUSTOMER" in dim_tables:
        hints.append("客户名称/客户编号")
    if "TBL_BD_ITEM" in dim_tables:
        hints.append("料号/品名/物料")
    if "TBL_BD_PROCESS" in dim_tables:
        hints.append("工序名称/工序编码")
    if "TBL_MO" in dim_tables:
        hints.append("工单编号/工单批次")
    if "TBL_NP_TEMPLATE" in dim_tables:
        hints.append("模板名称")
    hints.append("明细/详情/全部字段")
    return "、".join(hints)


def _compact_forbidden_join_cols(mappings: List[Dict[str, Any]]) -> List[str]:
    """列表默认禁止裸输出的外键/工号列（仅含实际配置了 JOIN 的映射）。"""
    cols: List[str] = []
    for mp in mappings:
        if mp.get("match_type") == "enum" or not mp.get("joins"):
            continue
        cols.extend(mp.get("fact_columns") or [])
    return sorted(set(cols))


def _build_query_rules_compact(
    tname: str,
    tcfg: Dict[str, Any],
    alias: str,
    label: str,
    mappings: List[Dict[str, Any]],
    cfg: Dict[str, Any],
    *,
    id_filter: Optional[Set[str]] = None,
    full_detail: bool = False,
) -> str:
    """精简版维表规则：合并 JOIN/SELECT，跳过混查枚举与重复译码段。"""
    default_ob = (tcfg.get("default_order_by") or "").strip()
    list_main_only = bool(tcfg.get("list_default_main_only"))
    enum_mps = [
        mp
        for mp in mappings
        if mp.get("match_type") == "enum"
        and (id_filter is None or (mp.get("id") or "") in id_filter)
    ]

    lines: List[str] = [
        f"【维表映射·{tname}】{label}，别名 **`{alias}`**。",
    ]
    if enum_mps:
        lines.append(
            "**【最高优先级·枚举译码】** "
            "凡下列字段出现在 SELECT 中，**必须**用对应 CASE 表达式，"
            "**禁止** `alias.字段 AS [中文名]` 裸输出数字/码值。"
        )
        for mp in enum_mps:
            fcols = ", ".join(mp.get("fact_columns") or [])
            for sel in mp.get("select") or []:
                expr = _apply_alias(sel.get("expr") or "", alias)
                as_name = sel.get("as") or ""
                lines.append(f"- **{fcols}** → `[{as_name}]`：`{expr} AS [{as_name}]`")
        lines.append("")

    lines.append(
        f"`FROM dbo.{tname} {alias} WITH (NOLOCK)`；SELECT 每列须 `AS [中文名]`，禁裸英文字段作表头。"
    )
    if list_main_only:
        lines.append(
            "**列表默认（用户未点名关联维表字段/明细/详情/全部字段）**："
            "只 SELECT **本表列 + 枚举译码**，**不要** JOIN 维表；"
            "用户点名或要求明细时再 JOIN 下方维表。"
        )
    if default_ob:
        lines.append(
            f"无时间 WHERE 的明细列表须 `ORDER BY {default_ob}`；仅 `COUNT(*)` 或 `GROUP BY` 除外。"
        )
    lines.append("")

    display_cols: List[Dict[str, Any]] = tcfg.get("display_columns") or []
    if display_cols:
        dc_title = (
            "### 本表列（列表默认只输出这些 + 枚举，禁 JOIN 维表列）"
            if list_main_only
            else "### 本表列"
        )
        lines.append(dc_title)
        for dc in display_cols:
            expr = _apply_alias(dc.get("expr") or "", alias)
            as_name = dc.get("as") or ""
            lines.append(f"- `{expr} AS [{as_name}]`")
        lines.append("")

    seen_joins: Set[str] = set()
    join_lines: List[str] = []
    dim_select_lines: List[str] = []
    forbidden_lines: List[str] = []
    join_fact_cols: List[str] = []

    for mp in mappings:
        mid = mp.get("id") or ""
        if id_filter is not None and mid not in id_filter:
            continue
        if mp.get("match_type") == "enum":
            for fb in mp.get("forbidden") or []:
                forbidden_lines.append(fb)
            continue
        if not mp.get("joins"):
            continue

        fact_cols = ", ".join(mp.get("fact_columns") or [])
        note = (mp.get("notes") or "").strip()
        hint = f"（{note}）" if note else ""
        joins = mp.get("joins") or []
        for j in joins:
            jl = _join_line(
                j.get("alias") or "dim",
                j.get("table") or "",
                j.get("on") or "",
                alias,
            )
            if jl not in seen_joins:
                seen_joins.add(jl)
                join_lines.append(f"- `{jl}`  ← {fact_cols}{hint}")

        sel_parts: List[str] = []
        for sel in mp.get("select") or []:
            expr = _apply_alias(sel.get("expr") or "", alias)
            as_name = sel.get("as") or ""
            sel_parts.append(f"`{expr} AS [{as_name}]`")
        if sel_parts:
            dim_select_lines.append(
                f"- {fact_cols}{hint}：{'；'.join(sel_parts)}"
            )
        for fc in mp.get("fact_columns") or []:
            join_fact_cols.append(fc)
        for fb in mp.get("forbidden") or []:
            forbidden_lines.append(fb)

    if join_lines:
        join_title = (
            "### 按需 JOIN（列表默认**跳过**；用户提下列信息时才写）"
            if list_main_only
            else "### JOIN（须全部写出，勿省略 ON）"
        )
        lines.append(join_title)
        if list_main_only:
            lines.append(f"- 触发示例：{_compact_join_triggers(mappings)}")
        lines.extend(join_lines)
        lines.append("")

    if dim_select_lines:
        dim_title = (
            "### 按需维表列（列表默认**不 SELECT**；与上方 JOIN 同开同关）"
            if list_main_only
            else "### 维表列（替代裸 ID/工号）"
        )
        lines.append(dim_title)
        lines.extend(dim_select_lines)
        lines.append("")

    fb_set: List[str] = []
    seen_fb: Set[str] = set()
    for fb in forbidden_lines:
        if fb and fb not in seen_fb:
            seen_fb.add(fb)
            fb_set.append(fb)
    if list_main_only and join_fact_cols:
        bare_cols = _compact_forbidden_join_cols(mappings)
        if bare_cols:
            man_cols = ", ".join(bare_cols)
            fb_set.append(
                f"列表默认禁止裸输出外键/工号：{man_cols}（须按需 JOIN 维表列或整段省略）"
            )
    if fb_set:
        lines.append("### 禁止")
        for fb in fb_set:
            lines.append(f"- {fb}")
        lines.append("")

    lines.append("### 自检")
    if list_main_only:
        lines.append(
            f"- 列表默认：仅 `FROM dbo.{tname} {alias}` + 本表列 + 枚举 CASE，无维表 JOIN；"
            f"按需场景才补 JOIN 与维表列。"
        )
    else:
        lines.append(
            f"- `FROM dbo.{tname} {alias} WITH (NOLOCK)` 与上述全部 LEFT JOIN；"
            f"枚举列已 CASE 译码；人员/故障/工作中心列来自维表而非裸外键。"
        )
    if default_ob:
        lines.append(f"- 无时间条件明细已 `ORDER BY {default_ob}`。")
    return "\n".join(lines).strip()


def build_query_rules(
    fact_table: str,
    *,
    config: Optional[Dict[str, Any]] = None,
    mapping_ids: Optional[Sequence[str]] = None,
    fact_alias: Optional[str] = None,
) -> str:
    cfg = config or load_config()
    tname = _normalize_table_name(fact_table)
    tables: Dict[str, Any] = cfg.get("tables", {})
    if tname not in tables:
        known = ", ".join(sorted(tables.keys()))
        return (
            f"【维表映射规则】未配置事实表 `{tname}`。"
            f"请在 mes_dimension_joins.json 的 tables 中补充。当前已配置：{known}"
        )

    tcfg = tables[tname]
    alias = (fact_alias or tcfg.get("fact_alias") or cfg.get("default_fact_alias") or "l").strip()
    label = tcfg.get("label") or tname
    mappings: List[Dict[str, Any]] = tcfg.get("mappings") or []

    id_filter: Optional[Set[str]] = None
    if mapping_ids:
        id_filter = {str(x).strip() for x in mapping_ids if str(x).strip()}

    full_detail = tname in _FULL_DETAIL_SELECT_TABLES
    if tcfg.get("compact_rules"):
        return _build_query_rules_compact(
            tname,
            tcfg,
            alias,
            label,
            mappings,
            cfg,
            id_filter=id_filter,
            full_detail=full_detail,
        )

    lines: List[str] = [
        f"【维表映射规则·自动生成】事实表：**{tname}**（{label}），别名 **`{alias}`**。",
        "生成 SQL 时**必须**按下述 JOIN 与 SELECT 展示列执行（片段无对应维表则跳过该条并在【相关表】说明）。",
        "**列表/明细查询**：`SELECT` 中**每一个**输出列都必须 `AS [中文列名]`，禁止裸写 `l.CSTART_TIME` 等英文字段名作为表头。",
    ]
    if full_detail:
        lines.append(
            "**本表为采购类明细**：用户问某单号+明细/详情且**未**点名只要某几列时，"
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
            "禁止 `er.CSTATUS`/`er.CIS_PRODUCT` 等裸字段或裸码值）"
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
        lines.append("- **禁止**：本表列无 `AS`（如 `l.CSTATUS`）；外键 ID 列单独展示（须用下方维表中文列替代）。")
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
        if mp.get("match_type") == "account":
            lines.append("- 类型：**账号字符串** → `TBL_SYS_USER.CUSER_NAME`，姓名取 `CDISPLAY_NAME`。")
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
        f"工作中心/工序/人员列是否来自对应维表而非同源；"
        f"**SELECT 每一列是否均有 `AS [中文名]`（含本表时间/状态/备注等列）**。"
    )
    if default_ob:
        lines.append(
            f"- 无时间条件的明细是否已 `ORDER BY {default_ob}`（由近到远）；纯 `COUNT(*)` 除外。"
        )
    if full_detail:
        lines.append(
            "- **采购明细列全集**：`SELECT` 是否已包含上文全部「事实表本表列」与各映射「必须列」；"
            "是否**未**裸输出 `spd.CITEM_ID`/`spd.CPO_ID`；是否**未**只选 6 列左右子集。"
        )

    return "\n".join(lines).strip()


# 查询结果列名 -> 码值 -> 中文（LLM 仍输出裸码时的兜底，键统一为字符串）
RESULT_COLUMN_VALUE_MAPS: Dict[str, Dict[str, str]] = {
    "任务状态": {"0": "待执行", "1": "已执行", "2": "已关闭(未执行)"},
    "工单状态": {
        "2": "已发放",
        "5": "已取消",
        "6": "已暂停",
        "7": "外协",
    },
    "状态": {"0": "待审核", "1": "已通过", "2": "已驳回"},
    "工作类型": {
        "1": "正常生产记录(检验生产记录)",
        "2": "批量生产记录",
        "3": "无工单生产记录",
        "4": "历史记录新增",
        "5": "FQC生产记录",
    },
    "是否已审核": {"Y": "是", "N": "否", "y": "是", "n": "否"},
    "是否完工": {"Y": "是", "N": "否", "y": "是", "n": "否"},
    "是否已过数": {"Y": "是", "N": "否", "y": "是", "n": "否"},
    "是否停产": {"Y": "是", "N": "否", "y": "是", "n": "否"},
    "是否紧急": {"Y": "是", "N": "否", "y": "是", "n": "否"},
    "是否在线": {"Y": "是", "N": "否", "y": "是", "n": "否"},
    "是否锁定": {"Y": "是", "N": "否", "y": "是", "n": "否"},
    "状态标识": {"A": "有效", "D": "无效", "a": "有效", "d": "无效"},
    "类型": {
        "Merger": "合拼",
        "MERGER": "合拼",
        "Sample": "样本",
        "SAMPLE": "样本",
        "Batch": "批量生产",
        "BATCH": "批量生产",
    },
    "工单状态": {
        "EAM_REPAIR_STATUS_ASSIGNMENT": "维修指派",
        "EAM_REPAIR_STATUS_COMPLETE": "维修完成",
        "EAM_REPAIR_STATUS_CLOSE": "维修取消",
    },
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
                f"{alias}.{fc} AS [状态中文]",
                f"{alias}.{fc} AS [状态标识，A：有效；D：无效]",
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


_SQL_KEYWORD_ALIASES = frozenset(
    {
        "WITH",
        "ON",
        "LEFT",
        "RIGHT",
        "INNER",
        "OUTER",
        "JOIN",
        "WHERE",
        "ORDER",
        "GROUP",
        "BY",
        "AND",
        "OR",
        "AS",
        "SELECT",
        "FROM",
    }
)


def _detect_sql_table_aliases(sql: str) -> Dict[str, str]:
    """SQL 别名 → 表名（FROM/JOIN dbo.TBL_xxx alias，优先匹配 WITH (NOLOCK)）。"""
    out: Dict[str, str] = {}
    for m in re.finditer(
        r"(?:FROM|(?:LEFT|RIGHT|INNER|CROSS)\s+JOIN)\s+dbo\.(\w+)\s+(\w+)\s+WITH\s*(?:\(\s*)?NOLOCK",
        sql,
        re.I,
    ):
        out[m.group(2)] = _normalize_table_name(m.group(1))
    for m in re.finditer(
        r"(?:FROM|(?:LEFT|RIGHT|INNER|CROSS)\s+JOIN)\s+dbo\.(\w+)\s+(\w+)\b",
        sql,
        re.I,
    ):
        alias = m.group(2)
        if alias.upper() in _SQL_KEYWORD_ALIASES:
            continue
        if alias not in out:
            out[alias] = _normalize_table_name(m.group(1))
    return out


def _apply_flexible_enum_rewrites(
    sql: str,
    tcfg: Dict[str, Any],
    alias: str,
    *,
    config: Optional[Dict[str, Any]] = None,
) -> str:
    """宽松匹配 alias.col AS [中文名]（含多余空格），替换为 CASE 译码。"""
    cfg = config or {}
    default_alias = (
        tcfg.get("fact_alias") or cfg.get("default_fact_alias") or "l"
    ).strip()
    out = sql
    for mp in tcfg.get("mappings") or []:
        for sel in mp.get("select") or []:
            expr = sel.get("expr") or ""
            if not expr.upper().startswith("CASE "):
                continue
            as_name = (sel.get("as") or "").strip()
            if not as_name:
                continue
            case_sql = _replace_sql_alias(expr, default_alias, alias)
            full = f"{case_sql} AS [{as_name}]"
            cols = list(mp.get("fact_columns") or [])
            if not cols:
                m = re.search(rf"\b{re.escape(alias)}\.(\w+)", case_sql, re.I)
                if m:
                    cols = [m.group(1)]
            for fc in cols:
                pat = (
                    rf"\b{re.escape(alias)}\.{re.escape(fc)}\s+AS\s+"
                    rf"\[{re.escape(as_name)}\]"
                )
                out = re.sub(pat, full, out, flags=re.IGNORECASE)
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
            tcfg = tables.get(tname)
            if not tcfg:
                continue
            for bare, full in _select_rewrite_pairs(tcfg, alias, config=cfg):
                out = re.sub(re.escape(bare), full, out, flags=re.IGNORECASE)
            out = _apply_flexible_enum_rewrites(out, tcfg, alias, config=cfg)
    else:
        check_tables: List[str] = []
        if fact_table:
            t = _normalize_table_name(fact_table)
            if t in tables:
                check_tables.append(t)
        else:
            upper = sql.upper()
            for tname in tables:
                if tname in upper:
                    check_tables.append(tname)

        for tname in check_tables:
            tcfg = tables[tname]
            alias = (
                tcfg.get("fact_alias") or cfg.get("default_fact_alias") or "l"
            ).strip()
            for bare, full in _select_rewrite_pairs(tcfg, alias, config=cfg):
                out = re.sub(re.escape(bare), full, out, flags=re.IGNORECASE)
            out = _apply_flexible_enum_rewrites(out, tcfg, alias, config=cfg)
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
    tname = _normalize_table_name(fact_table)
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
    tname = _normalize_table_name(fact_table)
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
    tname = _normalize_table_name(fact_table)
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
                            f"SELECT DISTINCT u.CUSER_NAME, u.CDISPLAY_NAME "
                            f"FROM dbo.{dim} u WITH (NOLOCK) "
                            f"WHERE u.CUSER_NAME IN ({{values}})"
                        ),
                    }
                )
            else:
                on = _apply_alias(j.get("on") or "", alias)
                # wc.CID = l.CWC_ID -> dim key CID
                m = re.search(r"(\w+)\.CID\s*=\s*" + re.escape(alias) + r"\.(\w+)", on, re.I)
                if m:
                    dim_key, fact_col = m.group(1), m.group(2)
                    name_cols = []
                    for sel in mp.get("select") or []:
                        ex = sel.get("expr") or ""
                        if dim_key in ex and "NAME" in ex.upper():
                            name_cols.append(ex.split(".")[-1])
                    plans.append(
                        {
                            "mapping_id": mp.get("id"),
                            "dim_table": dim,
                            "fact_column": fact_col,
                            "sql": (
                                f"SELECT d.CID, d.{name_cols[0] if name_cols else 'CWC_NAME'} "
                                f"FROM dbo.{dim} d WITH (NOLOCK) WHERE d.CID IN ({{values}})"
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
  键为 mes_dimension_joins.json 中的 mapping id。
    """
    if not rows or not lookups:
        return rows

    cfg = config or load_config()
    tname = _normalize_table_name(fact_table)
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
    try:
        from mes_sql_multijoin import build_multijoin_query_hints

        mj_hints = build_multijoin_query_hints(user_question, table, cfg)
        if mj_hints:
            rules = rules.rstrip() + "\n\n" + mj_hints
    except ImportError:
        pass
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
        out["query_sql_fixed"] = apply_sql_display_rewrites(
            sql, fact_table=out.get("fact_table") or "", config=cfg
        )
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="生成 MES 维表映射规则文本")
    parser.add_argument("fact_table", nargs="?", default="", help="事实表名，如 TBL_SFC_WS_LOG")
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
