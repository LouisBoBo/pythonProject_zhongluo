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


def _cstate_case_sql(alias: str) -> str:
    return (
        f"CASE UPPER(RTRIM({alias}.CSTATE)) WHEN 'A' THEN N'有效' "
        f"WHEN 'D' THEN N'无效' ELSE {alias}.CSTATE END AS [状态标识]"
    )


_CSTATE_CASE_BLOCK = re.compile(
    r"CASE\s+UPPER\s*\(\s*RTRIM\s*\(\s*(\w+)\.CSTATE\s*\)\s*\)\s+"
    r"WHEN\s+'A'\s+THEN\s+N'有效'[\s\S]*?END\s+AS\s+\[[^\]]+\]",
    re.I,
)
_CSTATE_BARE = re.compile(
    r",?\s*(\w+)\.CSTATE\s+AS\s+\[[^\]]+\]",
    re.I,
)


def _cleanup_select_commas(sql: str) -> str:
    out = re.sub(r",\s*,", ",", sql)
    out = re.sub(r"SELECT\s+,", "SELECT ", out, flags=re.I)
    out = re.sub(r",\s+(?=FROM\b)", " ", out, flags=re.I)
    return out


def _fix_cstate_columns(sql: str) -> str:
    """CSTATE 只保留一列 [状态标识]：A→有效，D→无效；去掉 [状态中文] 等重复列。"""
    if ".CSTATE" not in sql.upper():
        return sql

    alias_m = re.search(r"(\w+)\.CSTATE\b", sql, re.I)
    if not alias_m:
        return sql
    alias = alias_m.group(1)
    canonical = _cstate_case_sql(alias)

    out = sql
    # 错误写法：缺少 D 分支或 ELSE 全标有效
    out = re.sub(
        r"CASE\s+UPPER\s*\(\s*RTRIM\s*\(\s*(\w+)\.CSTATE\s*\)\s*\)\s+"
        r"WHEN\s+'A'\s+THEN\s+N'有效'\s+ELSE\s+N'有效'\s+END\s+AS\s+\[[^\]]+\]",
        lambda m: _cstate_case_sql(m.group(1)),
        out,
        flags=re.I,
    )

    blocks = list(_CSTATE_CASE_BLOCK.finditer(out))
    if blocks:
        first = True
        new_out = ""
        last = 0
        for m in blocks:
            header = out[m.start() : m.end()]
            is_status_cn = "状态中文" in header
            is_dup_status_id = "状态标识" in header and not first
            if is_status_cn or is_dup_status_id:
                new_out += out[last : m.start()]
                last = m.end()
                continue
            if first:
                new_out += out[last : m.start()] + canonical
                first = False
            else:
                new_out += out[last : m.start()]
            last = m.end()
        out = new_out + out[last:]
    else:
        out = _CSTATE_BARE.sub(lambda m: _cstate_case_sql(m.group(1)), out)

    if canonical not in out and ".CSTATE" in out.upper():
        out = re.sub(
            r"(SELECT\s+)",
            r"\1" + canonical + ", ",
            out,
            count=1,
            flags=re.I,
        )

    return _cleanup_select_commas(out)


# 化验任务枚举兜底（Dify 未部署打包 fix 节点时仍生效）
_ASSAY_ENUM_FALLBACK = [
    (
        re.compile(r"(\w+)\.CTASK_TYPE\s+AS\s+\[任务类型\]", re.I),
        (
            "CASE \\1.CTASK_TYPE WHEN 1 THEN N'常规化验' WHEN 2 THEN N'异常化验' "
            "ELSE CAST(\\1.CTASK_TYPE AS NVARCHAR(20)) END AS [任务类型]"
        ),
    ),
    (
        re.compile(r"(\w+)\.CTASK_STATUS\s+AS\s+\[任务状态\]", re.I),
        (
            "CASE \\1.CTASK_STATUS WHEN 0 THEN N'待执行' WHEN 1 THEN N'已执行' WHEN 2 THEN N'已关闭' "
            "ELSE CAST(\\1.CTASK_STATUS AS NVARCHAR(20)) END AS [任务状态]"
        ),
    ),
    (
        re.compile(r"(\w+)\.CASSAY_STATUS\s+AS\s+\[化验状态\]", re.I),
        (
            "CASE \\1.CASSAY_STATUS WHEN 0 THEN N'待取样' WHEN 1 THEN N'待接收' WHEN 2 THEN N'待化验' "
            "WHEN 3 THEN N'化验中' WHEN 4 THEN N'待审核' WHEN 5 THEN N'已审核' "
            "ELSE CAST(\\1.CASSAY_STATUS AS NVARCHAR(20)) END AS [化验状态]"
        ),
    ),
    (
        re.compile(r"(\w+)\.CASSAY_RESULT\s+AS\s+\[化验结果\]", re.I),
        (
            "CASE \\1.CASSAY_RESULT WHEN 1 THEN N'正常' WHEN 2 THEN N'异常' "
            "ELSE CAST(\\1.CASSAY_RESULT AS NVARCHAR(20)) END AS [化验结果]"
        ),
    ),
    (
        re.compile(r"(\w+)\.CCHECK_STATUS\s+AS\s+\[审核状态\]", re.I),
        (
            "CASE \\1.CCHECK_STATUS WHEN 1 THEN N'已审核' WHEN 0 THEN N'未审核' "
            "ELSE CAST(\\1.CCHECK_STATUS AS NVARCHAR(20)) END AS [审核状态]"
        ),
    ),
    (
        re.compile(r"(\w+)\.CIS_OPEN_LINE\s+AS\s+\[是否开线前分析\]", re.I),
        (
            "CASE UPPER(RTRIM(\\1.CIS_OPEN_LINE)) WHEN 'Y' THEN N'是' WHEN 'N' THEN N'否' "
            "ELSE \\1.CIS_OPEN_LINE END AS [是否开线前分析]"
        ),
    ),
]


def fix_enum_display_columns(sql: str) -> str:
    """将裸码值列替换为 CASE 译码（映射表已配置但 LLM 常仍输出裸字段）。"""
    out = sql
    try:
        from mes_dimension_rules import apply_sql_display_rewrites

        out = apply_sql_display_rewrites(out)
    except ImportError:
        for pat, repl in _ASSAY_ENUM_FALLBACK:
            out = pat.sub(repl, out)

    patterns = [
        (
            re.compile(r"(\w+)\.CIS_ONLINE\s+AS\s+\[是否在线\]", re.I),
            r"CASE UPPER(RTRIM(\1.CIS_ONLINE)) WHEN 'Y' THEN N'是' WHEN 'N' THEN N'否' ELSE \1.CIS_ONLINE END AS [是否在线]",
        ),
        (
            re.compile(r"(\w+)\.CIS_LOCKED_OUT\s+AS\s+\[是否锁定\]", re.I),
            r"CASE UPPER(RTRIM(\1.CIS_LOCKED_OUT)) WHEN 'Y' THEN N'是' WHEN 'N' THEN N'否' ELSE \1.CIS_LOCKED_OUT END AS [是否锁定]",
        ),
    ]
    for pat, repl in patterns:
        out = pat.sub(repl, out)
    return _fix_cstate_columns(out)


def fix_mes_sql(sql: str, user_question: str = "") -> str:
    s = fix_nolock_linebreaks(sql)
    s = fix_orphan_nolock_lines(s)
    s = fix_nolock_linebreaks(s)
    s = repair_truncated_assay_user_join(s)
    s = fix_enum_display_columns(s)
    try:
        from mes_sql_multijoin import fix_multijoin_top

        s = fix_multijoin_top(s, user_question=user_question)
    except ImportError:
        pass
    return s


def main(
    sql: Optional[str] = None,
    inputs: Optional[Dict[str, Any]] = None,
    user_question: str = "",
    **kwargs: Any,
) -> Dict[str, str]:
    merged: Dict[str, Any] = {}
    if inputs:
        merged.update(inputs)
    merged.update(kwargs)
    q = str(
        user_question
        or merged.get("user_question")
        or merged.get("query")
        or ""
    ).strip()
    raw = _coerce_sql(sql, inputs, **kwargs)
    fixed = fix_mes_sql(raw, user_question=q)
    return {"fixed_sql": fixed, "sql": fixed}


# --- Dify 入口（复制到 fix 代码节点；user_question 接 {{#sys.query#}} 或上游同问题）---
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

_out = main(sql=sql or query_sql, user_question=user_question)
fixed_sql = _out["fixed_sql"]
