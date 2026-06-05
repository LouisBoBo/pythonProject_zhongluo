#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dify「代码」节点：LLM 生成 SQL → 本节点 → rookie_text2data

入参（任一名称均可）：sql / query_sql / generated_sql / text
出参：fixed_sql（必须接到 text2data，禁止仍用 LLM 原始 sql）

修复项：WITH (NOLOCK) 拆行；P_MO.status/synchro/dev 数字 CASE → string（error 245）
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from erp_sql_fix_core import fix_erp_sql, fix_erp_sql_with_meta, coerce_erp_sql_input


def _coerce_sql(
    sql: Optional[str] = None,
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> str:
    merged: Dict[str, Any] = {}
    if inputs:
        merged.update(inputs)
    merged.update(kwargs)
    if sql is not None:
        merged.setdefault("sql", sql)
    return coerce_erp_sql_input(**merged)


def main(
    sql: Optional[str] = None,
    query_sql: Optional[str] = None,
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, str]:
    merged: Dict[str, Any] = {}
    if inputs:
        merged.update(inputs)
    merged.update(kwargs)
    if sql is not None:
        merged.setdefault("sql", sql)
    if query_sql is not None:
        merged.setdefault("query_sql", query_sql)
    return fix_erp_sql_with_meta(**merged)


# --- Dify 入口（复制 build 生成的 dify_erp_sql_fix_node.py 全文）---
