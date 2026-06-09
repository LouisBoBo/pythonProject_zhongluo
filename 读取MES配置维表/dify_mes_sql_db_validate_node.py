# -*- coding: utf-8 -*-
# 【Dify · MES SQL 列校验 · build_mes_sql_db_validate_bundle.py 自动生成】
# 位置：fix_mes_sql_nolock 之后、rookie_text2data 之前
# 依赖：pip install sqlalchemy pymssql
# 环境变量（可选）：MES_DB_SERVER / MES_DB_DATABASE / MES_DB_USER / MES_DB_PASSWORD …
#
# 入参（与 text2data 同源即可）：
#   fixed_sql ← fix 节点
#   server, port, username, password, database（或 db / db_name）
#
# 出参：
#   fixed_sql
#   was_changed, removed_columns(JSON), tables_checked(JSON), table_column_counts(JSON), validate_error

from __future__ import annotations

import json
import os
import re
import urllib.parse
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

_SQL_FENCE = re.compile(r"```(?:sql)?\s*(.*?)```", re.I | re.S)
_TABLE_ALIAS = re.compile(
    r"(?:FROM|(?:LEFT|INNER|RIGHT|FULL|CROSS)\s+JOIN)\s+"
    r"(?:(?P<schema>\w+)\.)?"
    r"\[?(?P<table>[\w_]+)\]?\s+"
    r"(?:AS\s+)?(?P<alias>\w+)"
    r"(?:\s+WITH\s*\(\s*NOLOCK\s*\))?",
    re.I,
)
_TABLE_NO_ALIAS = re.compile(
    r"(?:FROM|(?:LEFT|INNER|RIGHT|FULL|CROSS)\s+JOIN)\s+"
    r"(?:(?P<schema>\w+)\.)?"
    r"\[?(?P<table>[\w_]+)\]?\s+"
    r"WITH\s*\(\s*NOLOCK\s*\)",
    re.I,
)
_COL_REF = re.compile(r"\b(?P<alias>\w+)\.\[?(?P<col>\w+)\]?", re.I)

DEFAULT_DB_CONFIG: Dict[str, Any] = {
    "server": "",
    "port": 1433,
    "username": "",
    "password": "",
    "database": "",
    "schema": "dbo",
    "connect_timeout": 8,
    "enabled": True,
}


def _extract_sql_text(raw: str) -> str:
    s = (raw or "").strip()
    if not s:
        return ""
    m = _SQL_FENCE.search(s)
    return m.group(1).strip() if m else s


def _as_bool(v: Any, default: bool = True) -> bool:
    if v is None:
        return default
    if isinstance(v, bool):
        return v
    return str(v).strip().lower() not in ("0", "false", "no", "off", "")


def resolve_db_config(*, env_prefix: str = "ERP", **kwargs: Any) -> Dict[str, Any]:
    """优先级：入参 > 环境变量 {PREFIX}_DB_* > DEFAULT。"""
    merged: Dict[str, Any] = {}
    inputs = kwargs.get("inputs")
    if isinstance(inputs, dict):
        merged.update(inputs)
    merged.update({k: v for k, v in kwargs.items() if k != "inputs"})

    prefix = (env_prefix or "ERP").strip().upper()
    cfg: Dict[str, Any] = dict(DEFAULT_DB_CONFIG)
    env_map = {
        "server": f"{prefix}_DB_SERVER",
        "port": f"{prefix}_DB_PORT",
        "username": f"{prefix}_DB_USER",
        "password": f"{prefix}_DB_PASSWORD",
        "database": f"{prefix}_DB_DATABASE",
        "schema": f"{prefix}_DB_SCHEMA",
        "connect_timeout": f"{prefix}_DB_CONNECT_TIMEOUT",
        "enabled": f"{prefix}_SQL_DB_VALIDATE",
    }
    for key, env_key in env_map.items():
        val = os.environ.get(env_key)
        if val not in (None, ""):
            cfg[key] = val

    alias_map = {
        "server": ("server", "host", "db_host", "db_server"),
        "port": ("port", "db_port"),
        "username": ("username", "user", "db_user", "db_username"),
        "password": ("password", "db_password"),
        "database": ("database", "db", "db_name", "database_name"),
    }
    for target, keys in alias_map.items():
        for key in keys:
            val = merged.get(key)
            if val not in (None, ""):
                cfg[target] = val
                break
        if cfg.get(target) in (None, "") and cfg.get(target) != 0:
            if target in merged and merged[target] not in (None, ""):
                cfg[target] = merged[target]

    cfg["port"] = int(cfg.get("port") or 1433)
    cfg["connect_timeout"] = int(cfg.get("connect_timeout") or 8)
    cfg["schema"] = str(cfg.get("schema") or "dbo").strip() or "dbo"
    cfg["enabled"] = _as_bool(cfg.get("enabled"), True)
    return cfg


def _missing_db_config_keys(cfg: Dict[str, Any]) -> List[str]:
    missing: List[str] = []
    if not str(cfg.get("server") or "").strip():
        missing.append("server（或 host）")
    if not str(cfg.get("database") or "").strip():
        missing.append("database（或 db，库名）")
    if not str(cfg.get("username") or "").strip():
        missing.append("username")
    if not str(cfg.get("password") or "").strip():
        missing.append("password")
    return missing


def parse_table_aliases(sql: str) -> Dict[str, Tuple[str, str]]:
    """alias(lower) -> (schema, table_name)。覆盖 FROM/JOIN 中全部表别名。"""
    out: Dict[str, Tuple[str, str]] = {}
    text = sql or ""
    for m in _TABLE_ALIAS.finditer(text):
        schema = (m.group("schema") or "dbo").strip()
        table = (m.group("table") or "").strip()
        alias = (m.group("alias") or "").strip()
        if table and alias:
            out[alias.lower()] = (schema, table)
    for m in _TABLE_NO_ALIAS.finditer(text):
        schema = (m.group("schema") or "dbo").strip()
        table = (m.group("table") or "").strip()
        if table:
            out.setdefault(table.lower(), (schema, table))
    return out


def collect_table_specs(sql: str) -> List[Tuple[str, str]]:
    """去重 (schema, table) 列表，供批量查 INFORMATION_SCHEMA。"""
    seen: Set[Tuple[str, str]] = set()
    specs: List[Tuple[str, str]] = []
    for schema, table in parse_table_aliases(sql).values():
        key = (schema.lower(), table.upper())
        if key in seen:
            continue
        seen.add(key)
        specs.append((schema, table))
    return specs


def collect_tables(sql: str) -> List[str]:
    return [table for _schema, table in collect_table_specs(sql)]


def fetch_table_columns_mssql(
    table_specs: List[Tuple[str, str]],
    *,
    db_config: Dict[str, Any],
) -> Dict[str, Set[str]]:
    """table_upper -> set(col_upper)。一次连接批量查多表（含多 JOIN）。"""
    if not table_specs:
        return {}
    from sqlalchemy import create_engine, text

    user = urllib.parse.quote_plus(str(db_config["username"]))
    pwd = urllib.parse.quote_plus(str(db_config["password"]))
    url = f"mssql+pymssql://{user}:{pwd}@{db_config['server']}/{db_config['database']}"
    engine = create_engine(
        url,
        connect_args={
            "port": int(db_config["port"]),
            "timeout": int(db_config["connect_timeout"]),
            "login_timeout": int(db_config["connect_timeout"]),
        },
        pool_pre_ping=True,
    )
    default_schema = str(db_config.get("schema") or "dbo")

    out: Dict[str, Set[str]] = {}
    for schema, table in table_specs:
        out[table.upper()] = set()

    chunk_size = 40
    with engine.connect() as conn:
        for i in range(0, len(table_specs), chunk_size):
            chunk = table_specs[i : i + chunk_size]
            clauses: List[str] = []
            params: Dict[str, Any] = {}
            for j, (schema, table) in enumerate(chunk):
                sch_key = f"s{j}"
                tbl_key = f"t{j}"
                clauses.append(
                    f"(TABLE_SCHEMA = :{sch_key} AND TABLE_NAME = :{tbl_key})"
                )
                params[sch_key] = schema or default_schema
                params[tbl_key] = table
            q = text(
                "SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME "
                "FROM INFORMATION_SCHEMA.COLUMNS "
                f"WHERE {' OR '.join(clauses)}"
            )
            for row in conn.execute(q, params).mappings():
                out[str(row["TABLE_NAME"]).upper()].add(
                    str(row["COLUMN_NAME"]).upper()
                )
    return out


def _split_top_level(text: str, sep: str = ",") -> List[str]:
    parts: List[str] = []
    depth = 0
    start = 0
    for i, ch in enumerate(text):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == sep and depth == 0:
            parts.append(text[start:i].strip())
            start = i + 1
    tail = text[start:].strip()
    if tail:
        parts.append(tail)
    return parts


def _refs_in_expr(expr: str) -> List[Tuple[str, str]]:
    return [(m.group("alias").lower(), m.group("col")) for m in _COL_REF.finditer(expr or "")]


def _invalid_refs_in_expr(
    expr: str,
    alias_map: Dict[str, Tuple[str, str]],
    table_cols: Dict[str, Set[str]],
) -> List[str]:
    bad: List[str] = []
    for alias, col in _refs_in_expr(expr):
        tbl = alias_map.get(alias)
        if not tbl:
            continue
        cols = table_cols.get(tbl[1].upper())
        if cols is None:
            continue
        if not cols or col.upper() not in cols:
            bad.append(f"{alias}.{col}")
    return bad


def _cleanup_select_commas(sql: str) -> str:
    out = re.sub(r"SELECT\s*,", "SELECT ", sql, flags=re.I)
    out = re.sub(r"(SELECT\s+TOP\s*\(\s*\d+\s*\))\s*,", r"\1 ", out, flags=re.I)
    out = re.sub(r",\s*,", ", ", out)
    out = re.sub(r",\s+FROM\b", " FROM", out, flags=re.I)
    return re.sub(r"\s{2,}", " ", out).strip()


def _fix_select_list(
    sql: str,
    alias_map: Dict[str, Tuple[str, str]],
    table_cols: Dict[str, Set[str]],
    removed: List[str],
) -> str:
    m = re.search(
        r"^\s*(SELECT\s+(?:TOP\s*\(\s*\d+\s*\)\s+)?)(.*?)\s+FROM\b",
        sql,
        re.I | re.S,
    )
    if not m:
        return sql
    prefix = m.group(1)
    suffix = sql[m.end(2) :]
    items = _split_top_level(m.group(2))
    kept: List[str] = []
    for item in items:
        bad = _invalid_refs_in_expr(item, alias_map, table_cols)
        if bad:
            removed.extend(bad)
            continue
        kept.append(item)
    if not kept:
        return sql
    new_select = ", ".join(kept)
    return _cleanup_select_commas(prefix + new_select + suffix)


def _fix_joins(
    sql: str,
    alias_map: Dict[str, Tuple[str, str]],
    table_cols: Dict[str, Set[str]],
    removed: List[str],
) -> str:
    join_pat = re.compile(
        r"(?P<join>(?:LEFT|INNER|RIGHT|FULL)\s+JOIN\s+"
        r"(?:\w+\.)?\w+\s+\w+(?:\s+WITH\s*\(\s*NOLOCK\s*\))?\s+ON\s+"
        r"(?:(?!LEFT\s+JOIN|INNER\s+JOIN|RIGHT\s+JOIN|FULL\s+JOIN|WHERE\b|ORDER\s+BY\b|GROUP\s+BY\b).)+)",
        re.I | re.S,
    )

    def _repl(jm: re.Match[str]) -> str:
        block = jm.group("join")
        on_m = re.search(r"\bON\s+(.*)", block, re.I | re.S)
        on_expr = on_m.group(1).strip() if on_m else block
        bad = _invalid_refs_in_expr(on_expr, alias_map, table_cols)
        if bad:
            removed.extend(bad)
            return ""
        return block

    return re.sub(join_pat, _repl, sql)


def _fix_order_by(
    sql: str,
    alias_map: Dict[str, Tuple[str, str]],
    table_cols: Dict[str, Set[str]],
    removed: List[str],
) -> str:
    m = re.search(r"\bORDER\s+BY\s+(.*?)(?:$|\s+OFFSET\b)", sql, re.I | re.S)
    if not m:
        return sql
    head = sql[: m.start(1)]
    tail = sql[m.end(1) :]
    items = _split_top_level(m.group(1))
    kept: List[str] = []
    for item in items:
        bad = _invalid_refs_in_expr(item, alias_map, table_cols)
        if bad:
            removed.extend(bad)
            continue
        kept.append(item)
    if not kept:
        return re.sub(r"\s+ORDER\s+BY\s+.*?(?=$|\s+OFFSET\b)", "", sql, flags=re.I | re.S).strip()
    return head + ", ".join(kept) + tail


def _fix_where(
    sql: str,
    alias_map: Dict[str, Tuple[str, str]],
    table_cols: Dict[str, Set[str]],
    removed: List[str],
) -> str:
    m = re.search(
        r"\bWHERE\s+(.*?)(?=\bORDER\s+BY\b|\bGROUP\s+BY\b|\bHAVING\b|$)",
        sql,
        re.I | re.S,
    )
    if not m:
        return sql
    where_body = m.group(1).strip()
    tokens = re.split(r"(\s+(?:AND|OR)\s+)", where_body, flags=re.I)
    kept: List[str] = []
    for tok in tokens:
        if re.fullmatch(r"\s+(?:AND|OR)\s+", tok, flags=re.I):
            if kept and not re.fullmatch(r"\s+(?:AND|OR)\s+", kept[-1], flags=re.I):
                kept.append(tok)
            continue
        bad = _invalid_refs_in_expr(tok, alias_map, table_cols)
        if bad:
            removed.extend(bad)
            if kept and re.fullmatch(r"\s+(?:AND|OR)\s+", kept[-1], flags=re.I):
                kept.pop()
            continue
        kept.append(tok)
    new_where = "".join(kept).strip()
    if not new_where:
        return (sql[: m.start()] + sql[m.end() :]).strip()
    return sql[: m.start(1)] + new_where + sql[m.end(1) :]


def validate_sql_columns(
    sql: str,
    table_cols: Dict[str, Set[str]],
) -> Tuple[str, List[str]]:
    if not (sql or "").strip() or not table_cols:
        return sql, []
    alias_map = parse_table_aliases(sql)
    removed: List[str] = []
    out = sql
    out = _fix_select_list(out, alias_map, table_cols, removed)
    out = _fix_joins(out, alias_map, table_cols, removed)
    out = _fix_where(out, alias_map, table_cols, removed)
    out = _fix_order_by(out, alias_map, table_cols, removed)
    out = _cleanup_select_commas(out)
    seen: Set[str] = set()
    uniq = []
    for r in removed:
        key = r.lower()
        if key not in seen:
            seen.add(key)
            uniq.append(r)
    return out, uniq


def _dify_out(
    fixed_sql: str,
    *,
    was_changed: bool = False,
    removed_columns: Optional[List[str]] = None,
    tables_checked: Optional[List[str]] = None,
    table_column_counts: Optional[Dict[str, int]] = None,
    validate_error: str = "",
) -> Dict[str, str]:
    return {
        "fixed_sql": fixed_sql,
        "was_changed": "true" if was_changed else "false",
        "removed_columns": json.dumps(removed_columns or [], ensure_ascii=False),
        "tables_checked": json.dumps(tables_checked or [], ensure_ascii=False),
        "table_column_counts": json.dumps(
            table_column_counts or {}, ensure_ascii=False
        ),
        "validate_error": validate_error,
    }


def validate_sql_against_db(
    sql: str = "",
    query_sql: str = "",
    *,
    env_prefix: str = "ERP",
    db_config: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, str]:
    cfg = resolve_db_config(env_prefix=env_prefix, **(db_config or {}), **kwargs)
    raw = _extract_sql_text(query_sql or sql or str(kwargs.get("fixed_sql") or ""))
    if not raw:
        return _dify_out("", validate_error="未收到 SQL")
    if not cfg.get("enabled"):
        return _dify_out(raw)
    missing = _missing_db_config_keys(cfg)
    if missing:
        return _dify_out(
            raw,
            validate_error="未配置数据库连接，缺少：" + "、".join(missing),
        )
    table_specs = collect_table_specs(raw)
    tables = [t for _s, t in table_specs]
    if not table_specs:
        return _dify_out(raw, validate_error="SQL 中未解析到 FROM/JOIN 表名")
    try:
        table_cols = fetch_table_columns_mssql(table_specs, db_config=cfg)
    except Exception as exc:
        return _dify_out(
            raw,
            tables_checked=tables,
            validate_error=f"数据库连接/查询失败：{exc}",
        )
    col_counts = {t: len(table_cols.get(t.upper(), set())) for t in tables}
    fixed, removed = validate_sql_columns(raw, table_cols)
    return _dify_out(
        fixed,
        was_changed=fixed != raw,
        removed_columns=removed,
        tables_checked=tables,
        table_column_counts=col_counts,
    )


def make_main(env_prefix: str) -> Callable[..., Dict[str, str]]:
    prefix = (env_prefix or "ERP").strip().upper()

    def main(
        sql: str = "",
        query_sql: str = "",
        fixed_sql: str = "",
        server: str = "",
        port: str = "",
        username: str = "",
        password: str = "",
        database: str = "",
        **kwargs: Any,
    ) -> Dict[str, str]:
        merged = dict(kwargs)
        merged.update(
            {
                k: v
                for k, v in {
                    "sql": sql,
                    "query_sql": query_sql,
                    "fixed_sql": fixed_sql,
                    "server": server,
                    "port": port,
                    "username": username,
                    "password": password,
                    "database": database,
                }.items()
                if v not in (None, "")
            }
        )
        src = fixed_sql or query_sql or sql
        return validate_sql_against_db(src, env_prefix=prefix, **merged)

    return main

main = make_main("MES")


# --- Dify 入口 ---
try:
    fixed_sql
except NameError:
    fixed_sql = ""
try:
    query_sql
except NameError:
    query_sql = ""
try:
    sql
except NameError:
    sql = ""
try:
    server
except NameError:
    server = ""
try:
    port
except NameError:
    port = ""
try:
    username
except NameError:
    username = ""
try:
    password
except NameError:
    password = ""
try:
    database
except NameError:
    database = ""
try:
    db
except NameError:
    db = ""

_out = main(
    sql=sql or "",
    query_sql=query_sql or "",
    fixed_sql=fixed_sql or "",
    server=server or "",
    port=port or "",
    username=username or "",
    password=password or "",
    database=database or db or "",
    db=database or db or "",
)
fixed_sql = str(_out.get("fixed_sql") or "")
was_changed = str(_out.get("was_changed") or "false")
removed_columns = str(_out.get("removed_columns") or "[]")
tables_checked = str(_out.get("tables_checked") or "[]")
table_column_counts = str(_out.get("table_column_counts") or "{}")
validate_error = str(_out.get("validate_error") or "")
