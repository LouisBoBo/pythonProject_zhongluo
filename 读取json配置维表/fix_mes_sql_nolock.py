#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dify「代码」节点：修复 LLM 常犯的 T-SQL 写法——表名/别名与 WITH (NOLOCK) 被拆成多行。

放在 SQL 生成 LLM 与 rookie_text2data 之间，入参 sql（或 query_sql），出参 fixed_sql。

典型坏写法（会 error 102 near 'wc' / 'u_s'）：
  FROM dbo.TBL_QM_ASSAY_LOG qal\\n\\nWITH (NOLOCK) LEFT JOIN dbo.TBL_BD_WC wc\\n\\nWITH (NOLOCK) ON ...
"""

from __future__ import annotations

import re
from typing import Any, Dict, Optional


def _coerce_sql(
    sql: Optional[str] = None,
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> str:
    merged: Dict[str, Any] = {}
    if inputs:
        merged.update(inputs)
    merged.update(kwargs)
    for key in ("sql", "query_sql", "generated_sql", "text"):
        v = merged.get(key)
        if v is not None and str(v).strip():
            return str(v)
    return (sql or "").strip()


def fix_nolock_linebreaks(sql: str) -> str:
    """把「别名换行 WITH (NOLOCK)」合并为「别名 WITH (NOLOCK)」。"""
    if not sql or not sql.strip():
        return sql

    s = sql.replace("\\n", "\n").strip()
    s = re.sub(r"\]\s*$", "", s)  # 截断残留的 ]

    # FROM/JOIN dbo.TBL_xxx alias \n WITH (NOLOCK)
    pat = re.compile(
        r"((?:FROM|(?:LEFT|INNER|RIGHT)\s+JOIN)\s+dbo\.\w+\s+\w+)"
        r"\s*(?:\r?\n\s*)+WITH\s*\(\s*NOLOCK\s*\)",
        re.IGNORECASE,
    )
    prev = None
    while prev != s:
        prev = s
        s = pat.sub(r"\1 WITH (NOLOCK)", s)

    # 极少数：别名后换行 WITH 再跟 LEFT JOIN（无 ON）
    s = re.sub(
        r"(\b\w+)\s*(?:\r?\n\s*)+WITH\s*\(\s*NOLOCK\s*\)\s+(LEFT\s+JOIN)",
        r"\1 WITH (NOLOCK) \2",
        s,
        flags=re.IGNORECASE,
    )
    return s.strip()


# 化验任务：取样人 JOIN 别名 → ON 条件（LLM 常在 sysus4 / u_s 处截断）
_ASSAY_SAMPLE_USER_ON = {
    "sysus4": "sysus4.CUSER_NAME = qal.CSAMPLE_USER",
    "u_s": "u_s.CUSER_NAME = qal.CSAMPLE_USER",
}


def repair_truncated_assay_user_join(sql: str) -> str:
    """化验任务：末尾取样人 JOIN 被截断时补全 WITH (NOLOCK) ON …。"""
    if "TBL_QM_ASSAY_LOG" not in sql.upper():
        return sql
    for alias, on_clause in _ASSAY_SAMPLE_USER_ON.items():
        if re.search(rf"{alias}\s+WITH\s*\(\s*NOLOCK\s*\)\s+ON\s+", sql, re.I):
            continue
        if re.search(
            rf"LEFT\s+JOIN\s+dbo\.TBL_SYS_USER\s+{alias}\s+WITH\s*\(\s*NOLOCK\s*\)\s*$",
            sql,
            re.I,
        ):
            return sql + f" ON {on_clause}"
        if re.search(
            rf"LEFT\s+JOIN\s+dbo\.TBL_SYS_USER\s+{alias}\s*$",
            sql,
            re.I,
        ):
            return sql + f" WITH (NOLOCK) ON {on_clause}"
    return sql


def fix_orphan_nolock_lines(sql: str) -> str:
    """独立成行的 WITH (NOLOCK)（前后都是换行）并入上一行表别名。"""
    pat = re.compile(
        r"(dbo\.\w+\s+\w+|\bqal\b|\bwc\b|\bqmmed\b|\bsysus\d?\b|\bu_[a-z]\b)"
        r"\s*(?:\r?\n\s*)+WITH\s*\(\s*NOLOCK\s*\)\s*(?:\r?\n\s*)+",
        re.IGNORECASE,
    )
    prev = None
    s = sql
    while prev != s:
        prev = s
        s = pat.sub(r"\1 WITH (NOLOCK) ", s)
    return s


def fix_mes_sql(sql: str) -> str:
    s = fix_nolock_linebreaks(sql)
    s = fix_orphan_nolock_lines(s)
    s = fix_nolock_linebreaks(s)
    s = repair_truncated_assay_user_join(s)
    return s


def main(
    sql: Optional[str] = None,
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, str]:
    raw = _coerce_sql(sql, inputs, **kwargs)
    fixed = fix_mes_sql(raw)
    return {"fixed_sql": fixed, "sql": fixed}
