#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ERP SQL 执行前修复（NOLOCK 拆行、P_MO string 枚举 error 245）。供 fix 节点与 build 脚本复用。"""

from __future__ import annotations

import re
from typing import List, Tuple

# LLM 高频错误写法 → 正确 string 译码（整段替换，最可靠）
_DIRECT_PMO_REPLACEMENTS: List[Tuple[str, str]] = [
    (
        "CASE mo.status WHEN 1 THEN N'外协' WHEN 2 THEN N'未发放' WHEN 3 THEN N'已发放' WHEN 4 THEN N'暂停' WHEN 5 THEN N'取消' WHEN 6 THEN N'完成' ELSE CAST(mo.status AS NVARCHAR(20)) END",
        "CASE UPPER(RTRIM(mo.status)) WHEN 'ACTIVE' THEN N'激活' WHEN 'ORDER' THEN N'已下单' WHEN 'WOWX' THEN N'外协' WHEN 'WOWFF' THEN N'未发放' WHEN 'WOYFF' THEN N'已发放' WHEN 'WOZT' THEN N'暂停' WHEN 'WOQX' THEN N'取消' WHEN 'WOWC' THEN N'完成' ELSE mo.status END",
    ),
    (
        "CASE pmo.status WHEN 1 THEN N'外协' WHEN 2 THEN N'未发放' WHEN 3 THEN N'已发放' WHEN 4 THEN N'暂停' WHEN 5 THEN N'取消' WHEN 6 THEN N'完成' ELSE CAST(pmo.status AS NVARCHAR(20)) END",
        "CASE UPPER(RTRIM(pmo.status)) WHEN 'ACTIVE' THEN N'激活' WHEN 'ORDER' THEN N'已下单' WHEN 'WOWX' THEN N'外协' WHEN 'WOWFF' THEN N'未发放' WHEN 'WOYFF' THEN N'已发放' WHEN 'WOZT' THEN N'暂停' WHEN 'WOQX' THEN N'取消' WHEN 'WOWC' THEN N'完成' ELSE pmo.status END",
    ),
    (
        "CASE mo.synchro WHEN 0 THEN N'-未同步' WHEN 1 THEN N'-已同步' WHEN 2 THEN N'-不同步' ELSE CAST(mo.synchro AS NVARCHAR(20)) END",
        "CASE UPPER(RTRIM(mo.synchro)) WHEN '0' THEN N'-未同步' WHEN '1' THEN N'-已同步' WHEN '2' THEN N'-不同步' ELSE mo.synchro END",
    ),
    (
        "CASE pmo.synchro WHEN 0 THEN N'-未同步' WHEN 1 THEN N'-已同步' WHEN 2 THEN N'-不同步' ELSE CAST(pmo.synchro AS NVARCHAR(20)) END",
        "CASE UPPER(RTRIM(pmo.synchro)) WHEN '0' THEN N'-未同步' WHEN '1' THEN N'-已同步' WHEN '2' THEN N'-不同步' ELSE pmo.synchro END",
    ),
    (
        "CASE mo.dev WHEN 1 THEN N'是' WHEN 0 THEN N'否' ELSE CAST(mo.dev AS NVARCHAR(20)) END",
        "CASE UPPER(RTRIM(mo.dev)) WHEN '1' THEN N'是' WHEN '0' THEN N'否' ELSE mo.dev END",
    ),
    (
        "CASE pmo.dev WHEN 1 THEN N'是' WHEN 0 THEN N'否' ELSE CAST(pmo.dev AS NVARCHAR(20)) END",
        "CASE UPPER(RTRIM(pmo.dev)) WHEN '1' THEN N'是' WHEN '0' THEN N'否' ELSE pmo.dev END",
    ),
    (
        "CASE atit.synchro WHEN 0 THEN N'-未同步' WHEN 1 THEN N'-已同步' WHEN 2 THEN N'-不同步' ELSE CAST(atit.synchro AS NVARCHAR(20)) END",
        "CASE WHEN UPPER(RTRIM(CAST(atit.synchro AS NVARCHAR(20)))) IN (N'0', N'-未同步') THEN N'-未同步' WHEN UPPER(RTRIM(CAST(atit.synchro AS NVARCHAR(20)))) IN (N'1', N'-已同步') THEN N'-已同步' WHEN UPPER(RTRIM(CAST(atit.synchro AS NVARCHAR(20)))) IN (N'2', N'-不同步') THEN N'-不同步' ELSE CAST(atit.synchro AS NVARCHAR(20)) END",
    ),
]

_SYNCHRO_SAFE = (
    "CASE WHEN UPPER(RTRIM(CAST({a}.synchro AS NVARCHAR(20)))) IN (N'0', N'-未同步') THEN N'-未同步' "
    "WHEN UPPER(RTRIM(CAST({a}.synchro AS NVARCHAR(20)))) IN (N'1', N'-已同步') THEN N'-已同步' "
    "WHEN UPPER(RTRIM(CAST({a}.synchro AS NVARCHAR(20)))) IN (N'2', N'-不同步') THEN N'-不同步' "
    "ELSE CAST({a}.synchro AS NVARCHAR(20)) END"
)
_UNIT_ID_OF_BOM_SAFE = (
    "CASE UPPER(RTRIM(CAST({a}.unitIdOfBom AS NVARCHAR(20)))) "
    "WHEN '1' THEN N'PCS' WHEN '2' THEN N'SET' WHEN '3' THEN N'PNL' "
    "ELSE CAST({a}.unitIdOfBom AS NVARCHAR(20)) END"
)
_LAYER_TYPE_SAFE = (
    "CASE UPPER(RTRIM(CAST({a}.layerType AS NVARCHAR(20)))) "
    "WHEN '0' THEN N'外层' WHEN '2' THEN N'内层' "
    "ELSE CAST({a}.layerType AS NVARCHAR(20)) END"
)
def _cast_upper(alias: str, col: str) -> str:
    return f"UPPER(RTRIM(CAST({alias}.{col} AS NVARCHAR(20))))"


def _when_match_expr(cast_expr: str, num: str, label: str) -> str:
    """避免 IN (N'0',N'否') 被优化成按 bit 比较导致 error 245。"""
    label_esc = label.replace("'", "''")
    if label == "否":
        return (
            f"({cast_expr} IN (N'0', N'FALSE', N'N', N'NO') OR {cast_expr} = N'否')"
        )
    if label == "是":
        return (
            f"({cast_expr} IN (N'1', N'TRUE', N'Y', N'YES') OR {cast_expr} = N'是')"
        )
    if label == num:
        return f"({cast_expr} IN (N'{num}'))"
    return f"({cast_expr} IN (N'{num}') OR {cast_expr} = N'{label_esc}')"


_IF_BARCOD_ENTRY_SAFE = (
    "CASE WHEN {c} IN (N'0', N'FALSE', N'N', N'NO') OR {c} = N'否' THEN N'否' "
    "WHEN {c} IN (N'1', N'TRUE', N'Y', N'YES') OR {c} = N'是' THEN N'是' "
    "ELSE CAST({a}.ifBarcodEntry AS NVARCHAR(20)) END"
)
_STEP_HOLD_SAFE = (
    "CASE WHEN {c} IN (N'1', N'TRUE', N'Y', N'YES') OR {c} = N'是' THEN N'打勾' "
    "WHEN {c} IN (N'0', N'FALSE', N'N', N'NO') OR {c} = N'否' THEN N'不打勾' "
    "ELSE CAST({a}.step_HOLD AS NVARCHAR(20)) END"
)

_PMO_STATUS_CASE = (
    "CASE UPPER(RTRIM({a}.status)) WHEN 'ACTIVE' THEN N'激活' WHEN 'ORDER' THEN N'已下单' "
    "WHEN 'WOWX' THEN N'外协' WHEN 'WOWFF' THEN N'未发放' WHEN 'WOYFF' THEN N'已发放' "
    "WHEN 'WOZT' THEN N'暂停' WHEN 'WOQX' THEN N'取消' WHEN 'WOWC' THEN N'完成' "
    "ELSE {a}.status END"
)
_PMO_SYNCHRO_CASE = _SYNCHRO_SAFE
_PMO_DEV_CASE = (
    "CASE WHEN {c} IN (N'1', N'TRUE', N'Y', N'YES') OR {c} = N'是' THEN N'是' "
    "WHEN {c} IN (N'0', N'FALSE', N'N', N'NO') OR {c} = N'否' THEN N'否' "
    "ELSE CAST({a}.dev AS NVARCHAR(20)) END"
)
_BAD_PMO_PATTERNS: List[Tuple[re.Pattern[str], str]] = [
    (
        re.compile(
            r"CASE\s+(?P<alias>mo|pmo)\.status\s+WHEN\s+1\s+THEN\s+N'外协'",
            re.I,
        ),
        _PMO_STATUS_CASE,
    ),
    (
        re.compile(
            r"CASE\s+(?P<alias>\w+)\.synchro\s+WHEN\s+0\s+THEN\s+N'-未同步'",
            re.I,
        ),
        _SYNCHRO_SAFE,
    ),
    (
        re.compile(
            r"CASE\s+UPPER\s*\(\s*RTRIM\s*\(\s*(?P<alias>\w+)\.synchro\s*\)\s*\)\s+WHEN\s+'0'\s+THEN\s+N'-未同步'",
            re.I,
        ),
        _SYNCHRO_SAFE,
    ),
    (
        re.compile(
            r"CASE\s+(?P<alias>\w+)\.unitIdOfBom\s+WHEN\s+1\s+THEN\s+N'PCS'",
            re.I,
        ),
        _UNIT_ID_OF_BOM_SAFE,
    ),
    (
        re.compile(
            r"CASE\s+(?P<alias>\w+)\.layerType\s+WHEN\s+0\s+THEN\s+N'外层'",
            re.I,
        ),
        _LAYER_TYPE_SAFE,
    ),
    (
        re.compile(
            r"CASE\s+(?P<alias>mo|pmo)\.dev\s+WHEN\s+1\s+THEN\s+N'是'",
            re.I,
        ),
        _PMO_DEV_CASE,
    ),
    (
        re.compile(
            r"CASE\s+(?P<alias>\w+)\.ifBarcodEntry\s+WHEN\s+0\s+THEN\s+N'否'",
            re.I,
        ),
        _IF_BARCOD_ENTRY_SAFE,
    ),
    (
        re.compile(
            r"CASE\s+(?P<alias>\w+)\.step_HOLD\s+WHEN\s+1\s+THEN\s+N'打勾'",
            re.I,
        ),
        _STEP_HOLD_SAFE,
    ),
]


def fix_nolock_linebreaks(sql: str) -> str:
    if not sql or not sql.strip():
        return sql
    s = sql.replace("\\n", "\n").strip()
    s = re.sub(r"\]\s*$", "", s)
    pat = re.compile(
        r"((?:FROM|(?:LEFT|INNER|RIGHT)\s+JOIN)\s+dbo\.\w+\s+\w+)"
        r"\s*(?:\r?\n\s*)+WITH\s*\(\s*NOLOCK\s*\)",
        re.IGNORECASE,
    )
    prev = None
    while prev != s:
        prev = s
        s = pat.sub(r"\1 WITH (NOLOCK)", s)
    s = re.sub(
        r"(\b\w+)\s*(?:\r?\n\s*)+WITH\s*\(\s*NOLOCK\s*\)\s+(LEFT\s+JOIN)",
        r"\1 WITH (NOLOCK) \2",
        s,
        flags=re.IGNORECASE,
    )
    return s.strip()


def fix_orphan_nolock_lines(sql: str) -> str:
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


def _replace_bad_pmo_case(sql: str, bad_pat: re.Pattern[str], template: str) -> str:
    out = sql
    while True:
        m = bad_pat.search(out)
        if not m:
            break
        alias = m.group("alias")
        start = m.start()
        depth = 0
        i = start
        replaced = False
        while i < len(out):
            if out[i : i + 4].upper() == "CASE":
                depth += 1
                i += 4
                continue
            if out[i : i + 3].upper() == "END" and (
                i + 3 >= len(out) or not out[i + 3].isalnum()
            ):
                depth -= 1
                i += 3
                if depth == 0:
                    out = out[:start] + _format_case_template(template, alias) + out[i:]
                    replaced = True
                    break
                continue
            i += 1
        if not replaced:
            break
    return out


def fix_pmo_string_enum_cases(sql: str) -> str:
    if not sql:
        return sql
    s = sql
    for old, new in _DIRECT_PMO_REPLACEMENTS:
        s = s.replace(old, new)
    for bad_pat, template in _BAD_PMO_PATTERNS:
        s = _replace_bad_pmo_case(s, bad_pat, template)
    return s


_NUMERIC_SIMPLE_CASE_START = re.compile(
    r"CASE\s+(?P<alias>\w+)\.(?P<col>\w+)\s+WHEN\s+\d+\s+THEN\s+N'",
    re.I,
)
_WHEN_NUM_THEN = re.compile(r"WHEN\s+(\d+)\s+THEN\s+N'([^']*)'", re.I)
_SKIP_GENERIC_NUMERIC_CASE = re.compile(r"^(?:mo|pmo)\.status$", re.I)


def _case_block_end(sql: str, start: int) -> int | None:
    depth = 0
    i = start
    n = len(sql)
    while i < n:
        if sql[i : i + 4].upper() == "CASE":
            depth += 1
            i += 4
            continue
        if sql[i : i + 3].upper() == "END" and (i + 3 >= n or not sql[i + 3].isalnum()):
            depth -= 1
            i += 3
            if depth == 0:
                return i
            continue
        i += 1
    return None


def _format_case_template(template: str, alias: str) -> str:
    if "{c}" in template:
        m = re.search(r"\{a\}\.(\w+)", template)
        col = m.group(1) if m else "x"
        return template.format(a=alias, c=_cast_upper(alias, col))
    return template.format(a=alias)


def _build_safe_numeric_case(
    alias: str, col: str, branches: List[Tuple[str, str]]
) -> str:
    cast = _cast_upper(alias, col)
    when_parts = []
    for num, label in branches:
        label_esc = label.replace("'", "''")
        when_parts.append(
            f"WHEN {_when_match_expr(cast, num, label)} THEN N'{label_esc}'"
        )
    return (
        f"CASE {' '.join(when_parts)} "
        f"ELSE CAST({alias}.{col} AS NVARCHAR(20)) END"
    )


_CAST_UPPER_RE = re.compile(
    r"UPPER\s*\(\s*RTRIM\s*\(\s*CAST\s*\(\s*(?P<alias>\w+)\.(?P<col>\w+)\s+AS\s+NVARCHAR\s*\(\s*\d+\s*\)\s*\)\s*\)\s*\)",
    re.I,
)
_IN_NUM_LABEL = re.compile(
    r"(?P<cast>UPPER\s*\(\s*RTRIM\s*\(\s*CAST\s*\(\s*\w+\.\w+\s+AS\s+NVARCHAR\s*\(\s*\d+\s*\)\s*\)\s*\)\s*\))\s+IN\s*\(\s*N'(?P<num>\d+)'\s*,\s*N'(?P<label>[^']+)'\s*\)",
    re.I,
)
_UPPER_RTRIM_COL = re.compile(
    r"CASE\s+UPPER\s*\(\s*RTRIM\s*\(\s*(?P<alias>\w+)\.(?P<col>\w+)\s*\)\s*\)",
    re.I,
)
_BOOL_COL = re.compile(
    r"^(?:if[A-Z]\w*|is[A-Z]\w*|planOnhold|releaseOnhold|soOnhold|halogenFree|"
    r"preQualify|inActive|enableApproval|locked|dev|archiveStatus|consignmentFlg|"
    r"taxFree|remaining|ifOutPut|ifStock|ifCreateJob|ifBarcodEntry|step_HOLD|ifActive)$",
    re.I,
)
_RAW_BOOL_SELECT = re.compile(
    r"(?P<prefix>(?:SELECT|,\s*))(?P<alias>\w+)\.(?P<col>\w+)\s+AS\s+(?P<as>\[[^\]]+\])",
    re.I,
)


def fix_in_list_chinese_bit_collision(sql: str) -> str:
    """将 IN (N'0',N'否') 拆成 OR，避免 SQL Server 按 bit 解析 IN 列表。"""

    def repl(m: re.Match[str]) -> str:
        return _when_match_expr(m.group("cast"), m.group("num"), m.group("label"))

    return _IN_NUM_LABEL.sub(repl, sql)


def fix_upper_rtrim_bool_without_cast(sql: str) -> str:
    out = sql
    for m in list(_UPPER_RTRIM_COL.finditer(out)):
        col = m.group("col")
        if not _BOOL_COL.match(col):
            continue
        alias = m.group("alias")
        cast = _cast_upper(alias, col)
        if col == "dev":
            repl = (
                f"CASE WHEN {cast} IN (N'1', N'TRUE', N'Y', N'YES') OR {cast} = N'是' THEN N'是' "
                f"WHEN {cast} IN (N'0', N'FALSE', N'N', N'NO') OR {cast} = N'否' THEN N'否' "
                f"ELSE CAST({alias}.dev AS NVARCHAR(20)) END"
            )
        else:
            continue
        start = m.start()
        end = _case_block_end(out, start)
        if end is None:
            continue
        out = out[:start] + repl + out[end:]
    return out


def fix_raw_bool_selects(sql: str) -> str:
    def repl(m: re.Match[str]) -> str:
        col = m.group("col")
        if not _BOOL_COL.match(col):
            return m.group(0)
        alias = m.group("alias")
        return (
            f"{m.group('prefix')}CAST({alias}.{col} AS NVARCHAR(20)) AS {m.group('as')}"
        )

    return _RAW_BOOL_SELECT.sub(repl, sql)


def fix_numeric_simple_case_expressions(sql: str) -> str:
    """CASE alias.col WHEN 0/1 THEN …：列内混存 0/1 与中文时避免 error 245。"""
    if not sql:
        return sql
    out = sql
    pos = 0
    while True:
        m = _NUMERIC_SIMPLE_CASE_START.search(out, pos)
        if not m:
            break
        alias, col = m.group("alias"), m.group("col")
        if _SKIP_GENERIC_NUMERIC_CASE.match(f"{alias}.{col}"):
            pos = m.end()
            continue
        start = m.start()
        end = _case_block_end(out, start)
        if end is None:
            pos = m.end()
            continue
        case_text = out[start:end]
        if re.search(
            rf"CAST\s*\(\s*{re.escape(alias)}\.{re.escape(col)}\s+AS\s+NVARCHAR",
            case_text,
            re.I,
        ) and re.search(r"\bIN\s*\(\s*N'", case_text, re.I):
            pos = end
            continue
        branches = _WHEN_NUM_THEN.findall(case_text)
        if not branches:
            pos = m.end()
            continue
        new_case = _build_safe_numeric_case(alias, col, branches)
        out = out[:start] + new_case + out[end:]
        pos = start + len(new_case)
    return out


_MODIFIED_BY_JOIN = re.compile(
    r"(?P<join>(?:LEFT|INNER|RIGHT)\s+JOIN\s+dbo\.T_User\s+(?P<tu>\w+)"
    r"(?:\s+WITH\s*\(\s*NOLOCK\s*\))?\s+ON\s+(?P=tu)\.recId\s*=\s*(?P<fact>\w+)\.modifiedBy\b)",
    re.I,
)


def fix_string_modified_by_join(sql: str) -> str:
    """modifiedBy 多为字符串用户名，LLM 误 JOIN T_User.recId 会触发 error 245。"""
    out = sql
    while True:
        m = _MODIFIED_BY_JOIN.search(out)
        if not m:
            break
        tu, fact = m.group("tu"), m.group("fact")
        out = out[: m.start()] + " " + out[m.end() :]
        out = re.sub(
            rf"{re.escape(tu)}\.\[?userCode\]?\s+AS\s+(\[[^\]]+\])",
            rf"{fact}.modifiedBy AS \1",
            out,
            flags=re.I,
        )
    return re.sub(r"\s{2,}", " ", out).strip()


_BUSINESSMAN_JOIN = re.compile(
    r"(?P<join>(?:LEFT|INNER|RIGHT)\s+JOIN\s+dbo\.S_BusinessMan\s+(?P<bm>\w+)"
    r"(?:\s+WITH\s*\(\s*NOLOCK\s*\))?\s+ON\s+(?P=bm)\.recId\s*=\s*(?P<fact>\w+)\.businessManId\b)",
    re.I,
)

# 表结构确认无 businessManId 列（LLM 常误加雇员 JOIN）
_FACTS_WITHOUT_BUSINESS_MAN_ID = (
    re.compile(r"dbo\.S_Complainment\b", re.I),
)


def _drop_alias_select_columns(sql: str, alias: str) -> str:
    pat = re.compile(
        rf",?\s*{re.escape(alias)}\.(?:\[\w+\]|\w+)\s+AS\s+\[[^\]]+\]",
        re.I,
    )
    return pat.sub("", sql)


def fix_invalid_businessman_join(sql: str) -> str:
    """S_Complainment 等表无 businessManId，误 JOIN S_BusinessMan 会 error 207。"""
    if not any(p.search(sql) for p in _FACTS_WITHOUT_BUSINESS_MAN_ID):
        return sql
    out = sql
    while True:
        m = _BUSINESSMAN_JOIN.search(out)
        if not m:
            break
        bm = m.group("bm")
        out = out[: m.start()] + " " + out[m.end() :]
        out = _drop_alias_select_columns(out, bm)
    return re.sub(r"\s{2,}", " ", out).strip()


_INVALID_SALE_COL = re.compile(
    r",?\s*\w+\.sale\s+AS\s+\[[^\]]*\]",
    re.I,
)


def fix_nonexistent_sale_column(sql: str) -> str:
    """S_CustomerHistory/WF 实际库无 sale 列（文档误录），须从 SELECT 剔除。"""
    if not re.search(r"dbo\.S_Customer(?:History|WF)\b", sql, re.I):
        return sql
    return _INVALID_SALE_COL.sub("", sql)


def fix_material_tyep_id_typo(sql: str) -> str:
    """S_SalesPartsLayers 外键在库中为 materialTyepId（ERP 拼写）。"""
    if not re.search(r"dbo\.S_SalesPartsLayers\b", sql, re.I):
        return sql
    return re.sub(r"\b(\w+)\.materialTypeId\b", r"\1.materialTyepId", sql, flags=re.I)


_SALESPARTNUM_EQ = re.compile(
    r"(?P<alias>\w+)\.salesPartNum\s*=\s*N'(?P<num>\d+)'",
    re.I,
)


def fix_salespartnum_or_recid(sql: str) -> str:
    """纯数字「249」可能是 salesPartNum 或 recId，扩展 WHERE 避免查空。"""
    def _repl(m: re.Match[str]) -> str:
        a, n = m.group("alias"), m.group("num")
        return f"({a}.salesPartNum = N'{n}' OR {a}.recId = {n})"

    return _SALESPARTNUM_EQ.sub(_repl, sql)


_INNER_SALESPARTS_LAYERS = re.compile(
    r"\bINNER\s+JOIN\s+dbo\.S_SalesPartsLayers\b",
    re.I,
)


def fix_inner_join_salesparts_layers(sql: str) -> str:
    """查销售部件层信息时 INNER JOIN 会丢掉无层行或匹配失败行。"""
    if not re.search(r"dbo\.S_SalesParts(?:Layers)?\b", sql, re.I):
        return sql
    return _INNER_SALESPARTS_LAYERS.sub("LEFT JOIN dbo.S_SalesPartsLayers", sql)


_SOSW_FACT = re.compile(r"dbo\.S_OSWO\b", re.I)
_SOSW_POITEM_JOIN = re.compile(r"JOIN\s+dbo\.S_OS_POItem\b", re.I)
_SOSW_PO_JOIN = re.compile(r"JOIN\s+dbo\.S_OS_PO\b", re.I)


def _ensure_sosw_po_chain(sql: str, fact_alias: str) -> str:
    if _SOSW_POITEM_JOIN.search(sql) and _SOSW_PO_JOIN.search(sql):
        return sql
    insert = (
        f" LEFT JOIN dbo.S_OS_POItem sospoi WITH (NOLOCK) ON sospoi.recId = {fact_alias}.poItemId"
        f" LEFT JOIN dbo.S_OS_PO sospo WITH (NOLOCK) ON sospo.recId = sospoi.os_PO_Id"
    )
    m = re.search(
        rf"dbo\.S_OSWO\s+{re.escape(fact_alias)}(?:\s+WITH\s*\(\s*NOLOCK\s*\))?",
        sql,
        re.I,
    )
    if not m:
        return sql
    return sql[: m.end()] + insert + sql[m.end() :]


def fix_sosw_plant_supplier_join(sql: str) -> str:
    """S_OSWO 无 plantsId/suppliersId/modifiedBy，工厂与供应商经 poItemId→S_OS_POItem→S_OS_PO。"""
    if not _SOSW_FACT.search(sql):
        return sql
    m = re.search(r"dbo\.S_OSWO\s+(?P<fa>\w+)", sql, re.I)
    fact_alias = m.group("fa") if m else "sosw"
    out = sql
    needs_po_chain = False
    for fk in ("plantsId", "suppliersId"):
        if re.search(rf"\b{re.escape(fact_alias)}\.{fk}\b", out, re.I):
            needs_po_chain = True
            out = re.sub(
                rf"((?:LEFT|INNER|RIGHT)\s+JOIN\s+dbo\.(?:T_Plants|M_Suppliers)\s+\w+"
                rf"(?:\s+WITH\s*\(\s*NOLOCK\s*\))?\s+ON\s+\w+\.recId\s*=\s*)"
                rf"{re.escape(fact_alias)}\.{fk}\b",
                rf"\1sospo.{fk}",
                out,
                flags=re.I,
            )
    if needs_po_chain:
        out = _ensure_sosw_po_chain(out, fact_alias)
    out = re.sub(
        rf",?\s*{re.escape(fact_alias)}\.modifiedBy\s+AS\s+\[[^\]]+\]",
        "",
        out,
        flags=re.I,
    )
    return re.sub(r"\s{2,}", " ", out).strip()


_TABLE_ALIAS_IN_SQL = re.compile(
    r"(?:FROM|JOIN)\s+dbo\.(?P<table>\w+)\s+(?P<alias>\w+)"
    r"(?:\s+WITH\s*\(\s*NOLOCK\s*\)|\s+(?:LEFT|INNER|RIGHT|ON)|\s*,|\s+ORDER|\s+WHERE|\s+GROUP|\s+HAVING|$)",
    re.I,
)
# 表结构无 modifiedBy，LLM 常从全局规则误加
_TABLES_WITHOUT_MODIFIED_BY = frozenset(
    {
        "FGI_IQCRESULT",
        "FGI_IQCITEM",
        "FGI_IQCHISTORY",
        "FGI_IQCWF",
        "P_WO",
    }
)


def _cleanup_select_commas(sql: str) -> str:
    out = re.sub(r"(SELECT\s+TOP\s*\(\s*\d+\s*\))\s*,", r"\1 ", sql, flags=re.I)
    out = re.sub(r",\s*,", ", ", out)
    out = re.sub(r",\s+FROM\b", " FROM", out, flags=re.I)
    return re.sub(r"\s{2,}", " ", out).strip()


def fix_missing_modified_by_columns(sql: str) -> str:
    """剔除无 modifiedBy 列的事实表上的 modifiedBy 及误 JOIN。"""
    aliases: List[Tuple[str, str]] = []
    seen: set[Tuple[str, str]] = set()
    for m in _TABLE_ALIAS_IN_SQL.finditer(sql):
        key = (m.group("table").upper(), m.group("alias").lower())
        if key in seen:
            continue
        seen.add(key)
        if m.group("table").upper() in _TABLES_WITHOUT_MODIFIED_BY:
            aliases.append((m.group("alias"), m.group("table")))
    if not aliases:
        return sql
    out = sql
    for alias, _table in aliases:
        out = re.sub(
            rf",?\s*{re.escape(alias)}\.modifiedBy\s+AS\s+\[[^\]]+\]",
            "",
            out,
            flags=re.I,
        )
        out = re.sub(
            r"(?:LEFT|INNER|RIGHT)\s+JOIN\s+dbo\.T_User\s+(?P<tu>\w+)"
            rf"(?:\s+WITH\s*\(\s*NOLOCK\s*\))?\s+ON\s+(?P=tu)\.recId\s*=\s*"
            rf"{re.escape(alias)}\.modifiedBy\b",
            "",
            out,
            flags=re.I,
        )
        out = re.sub(
            rf",?\s*(?P<tu>\w+)\.\[?userCode\]?\s+AS\s+\[修改人\]",
            "",
            out,
            flags=re.I,
        )
    return _cleanup_select_commas(out)


def fix_p_wo_invalid_columns(sql: str) -> str:
    """P_WO 现场库常见无 moroute/partnum/modifiedBy/creatorId（文档误录或已迁移）。"""
    if not re.search(r"dbo\.P_WO\b", sql, re.I):
        return sql
    out = sql
    _wo_alias = r"pwo\d*|wo"
    for col in ("moroute", "partnum", "partNum", "modifiedBy", "creatorId"):
        out = re.sub(
            rf",?\s*(?P<alias>{_wo_alias})\.{col}\s+AS\s+\[[^\]]+\]",
            "",
            out,
            flags=re.I,
        )
    out = re.sub(
        r"(?:LEFT|INNER|RIGHT)\s+JOIN\s+dbo\.T_User\s+(?P<tu>\w+)"
        rf"(?:\s+WITH\s*\(\s*NOLOCK\s*\))?\s+ON\s+(?P=tu)\.recId\s*=\s*(?:{_wo_alias})\.(?:creatorId|modifiedBy)\b",
        "",
        out,
        flags=re.I,
    )
    out = re.sub(
        r",?\s*(?P<tu>\w+)\.\[?userCode\]?\s+AS\s+\[修改人\]",
        "",
        out,
        flags=re.I,
    )
    return _cleanup_select_commas(out)


def fix_hallucinated_column_names(sql: str) -> str:
    """LLM 常编造 businessManName / userName 等，替换为 ERP 真实列名。"""
    subs = (
        (r"\bbm\.businessManName\b", "bm.name"),
        (r"\bbm\.businessManPhone\b", "bm.telephone"),
        (r"\bbm\.businessManEmail\b", "bm.email"),
        (r"\btu\.userName\b", "tu.loginName"),
        (r"\btu\.realName\b", "tu.employeeName"),
    )
    out = sql
    for pat, repl in subs:
        out = re.sub(pat, repl, out, flags=re.I)
    return out


def fix_erp_sql(sql: str) -> str:
    s = fix_nolock_linebreaks(sql)
    s = fix_orphan_nolock_lines(s)
    s = fix_nolock_linebreaks(s)
    s = fix_pmo_string_enum_cases(s)
    s = fix_numeric_simple_case_expressions(s)
    s = fix_in_list_chinese_bit_collision(s)
    s = fix_upper_rtrim_bool_without_cast(s)
    s = fix_raw_bool_selects(s)
    s = fix_string_modified_by_join(s)
    s = fix_hallucinated_column_names(s)
    s = fix_p_wo_invalid_columns(s)
    s = fix_missing_modified_by_columns(s)
    s = fix_invalid_businessman_join(s)
    s = fix_nonexistent_sale_column(s)
    s = fix_material_tyep_id_typo(s)
    s = fix_salespartnum_or_recid(s)
    s = fix_inner_join_salesparts_layers(s)
    s = fix_sosw_plant_supplier_join(s)
    return s


_SQL_FENCE = re.compile(r"```(?:sql)?\s*(.*?)```", re.I | re.S)


def _extract_sql_text(raw: str) -> str:
    s = (raw or "").strip()
    if not s:
        return ""
    m = _SQL_FENCE.search(s)
    if m:
        return m.group(1).strip()
    return s


def coerce_erp_sql_input(sql: str = "", query_sql: str = "", **kwargs) -> str:
    """兼容 Dify 多种入参名；支持 ```sql``` 包裹。"""
    merged: dict = {}
    inputs = kwargs.get("inputs")
    if isinstance(inputs, dict):
        merged.update(inputs)
    merged.update({k: v for k, v in kwargs.items() if k != "inputs"})
    if query_sql:
        merged.setdefault("query_sql", query_sql)
    if sql:
        merged.setdefault("sql", sql)
    for key in ("sql", "query_sql", "generated_sql", "text"):
        v = merged.get(key)
        if v is not None and str(v).strip():
            return _extract_sql_text(str(v))
    return ""


def fix_erp_sql_with_meta(sql: str = "", query_sql: str = "", **kwargs) -> dict[str, str]:
    raw = coerce_erp_sql_input(sql=sql, query_sql=query_sql, **kwargs)
    if not raw:
        return {
            "fixed_sql": "",
            "sql": "",
            "query_sql": "",
            "was_changed": "false",
            "fix_error": "未收到 SQL：修复节点入参须接 LLM 的 query_sql/sql",
        }
    fixed = fix_erp_sql(raw)
    changed = fixed != raw
    return {
        "fixed_sql": fixed,
        "sql": fixed,
        "query_sql": fixed,
        "was_changed": "true" if changed else "false",
        "fix_error": "",
    }
