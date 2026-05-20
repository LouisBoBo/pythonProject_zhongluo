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
from typing import Any, Dict, List, Optional, Sequence, Set, Union

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

    for tname, tcfg in tables.items():
        keywords: List[str] = tcfg.get("default_for_keywords") or []
        for kw in keywords:
            if kw and kw in q:
                return tname

    m = re.search(r"\b(TBL_[A-Z0-9_]+)\b", q, re.I)
    if m:
        cand = _normalize_table_name(m.group(1))
        if cand in tables:
            return cand

    return explicit or "TBL_SFC_WS_LOG"


def _apply_alias(template: str, fact_alias: str) -> str:
    return template.replace(" l.", f" {fact_alias}.").replace("= l.", f"= {fact_alias}.")


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

    lines: List[str] = [
        f"【维表映射规则·自动生成】事实表：**{tname}**（{label}），别名 **`{alias}`**。",
        "生成 SQL 时**必须**按下述 JOIN 与 SELECT 展示列执行（片段无对应维表则跳过该条并在【相关表】说明）。",
        "**列表/明细查询**：`SELECT` 中**每一个**输出列都必须 `AS [中文列名]`，禁止裸写 `l.CSTART_TIME` 等英文字段名作为表头。",
        "",
    ]

    display_cols: List[Dict[str, Any]] = tcfg.get("display_columns") or []
    if display_cols:
        lines.append("### 事实表本表列（须 `AS` 中文别名，勿裸列名）")
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

        lines.append("- **JOIN**（逐条写出，勿省略 `ON`）：")
        for j in mp.get("joins") or []:
            jl = _join_line(
                j.get("alias") or "dim",
                j.get("table") or "",
                j.get("on") or "",
                alias,
            )
            if jl not in seen_joins:
                seen_joins.add(jl)
            lines.append(f"  - `{jl}`")

        lines.append("- **SELECT 推荐列**（替代裸 ID/裸账号）：")
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

    return "\n".join(lines).strip()


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
    return {
        "query_rules": rules,
        "fact_table": table,
        "join_tables": ",".join(list_join_tables(table, cfg)),
    }


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
