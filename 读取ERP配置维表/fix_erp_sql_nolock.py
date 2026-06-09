#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dify「代码」节点：修复 LLM 常犯的 ERP T-SQL 写法。

放在 SQL 生成 LLM 与 rookie_text2data 之间，入参 sql（或 query_sql），出参 fixed_sql。

修复项：
  - WITH (NOLOCK) 拆行（error 102）
  - P_MO.status/synchro/dev 数字 CASE → string（error 245）
  - P_WO 无效列、modifiedBy 误 JOIN 等（error 207）
  - 主从 JOIN 缺 TOP (1000) 兜底

维护：改 erp_sql_fix_core.py → python3 build_dify_bundle.py → 复制 dify_erp_sql_fix_node.py
本文件为本地调试 / 与 MES fix_mes_sql_nolock.py 对照用；Dify 请用 build 生成的单文件节点。
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from erp_sql_fix_core import fix_erp_sql, fix_erp_sql_with_meta


def main(
    sql: Optional[str] = None,
    query_sql: Optional[str] = None,
    user_question: str = "",
    **kwargs: Any,
) -> Dict[str, str]:
    merged: Dict[str, Any] = dict(kwargs)
    if sql is not None:
        merged.setdefault("sql", sql)
    if query_sql is not None:
        merged.setdefault("query_sql", query_sql)
    if user_question:
        merged.setdefault("user_question", user_question)
    return fix_erp_sql_with_meta(**merged)


# --- Dify 入口（也可直接复制 dify_erp_sql_fix_node.py 全文）---
try:
    sql
except NameError:
    sql = ""
try:
    query_sql
except NameError:
    query_sql = ""
try:
    user_question
except NameError:
    user_question = ""

_out = main(sql=sql or "", query_sql=query_sql or "", user_question=user_question or "")
fixed_sql = str(_out.get("fixed_sql") or "")
sql = str(_out.get("sql") or fixed_sql)
query_sql = str(_out.get("query_sql") or fixed_sql)
was_changed = str(_out.get("was_changed") or "false")
fix_error = str(_out.get("fix_error") or "")
