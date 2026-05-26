#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dify 代码节点：读取数据库表结构（PostgreSQL / SQL Server）。

入参：server, port, username, password, database, audit_table_names
      db_type  可选 postgresql | mssql（用户名 postgres 或端口 5432/15432 时自动识别 PG）

Dify 依赖：pip install sqlalchemy psycopg2-binary   # PostgreSQL
          pip install sqlalchemy pymssql            # SQL Server
"""

from __future__ import annotations

import json
import re
import sys
import traceback
import urllib.parse
from typing import Any, Dict, List, Optional, Tuple

result = "失败"
message = ""
schema_data = "{}"
table_count = 0
schema_text = ""

DEFAULT = {
    "server": "192.168.49.10",
    "port": 1433,
    "username": "sa",
    "password": "",
    "database": "CIMOM_TEST",
    "schema": "",
    "db_type": "",
    "connect_timeout": 10,
    "include_comments": True,
    "include_foreign_keys": True,
    "include_indexes": True,
    "include_schema_text": False,
    "max_tables": 0,
    "allow_full_scan": False,
}

MAX_MSG, MAX_DATA, MAX_TEXT = 3000, 70000, 20000
SCRIPT_VERSION = "2.1.0"  # 日志含此版本号，用于确认 Dify 已粘贴最新代码


def _parse_tables(raw: Any) -> List[str]:
    if raw is None:
        return []
    parts = raw if isinstance(raw, list) else re.split(r"[,，;\s]+", str(raw).strip())
    return [str(p).strip() for p in parts if str(p).strip() and "/" not in str(p)]


def _as_bool(v: Any, default: bool) -> bool:
    if v is None:
        return default
    if isinstance(v, bool):
        return v
    return str(v).strip().lower() not in ("0", "false", "no")


def _detect_db_type(raw: Dict[str, Any]) -> str:
    explicit = str(raw.get("db_type") or raw.get("db_engine") or "").strip().lower()
    if explicit in ("postgresql", "postgres", "pg"):
        return "postgresql"
    if explicit in ("mssql", "sqlserver", "sql_server", "sql"):
        return "mssql"
    user = str(raw.get("username") or raw.get("user") or "").lower()
    if user in ("postgres", "postgresql") or user.startswith("pg"):
        return "postgresql"
    port = int(raw.get("port") or 0)
    if port in (5432, 15432):
        return "postgresql"
    return "mssql"


def _resolve_config(inputs: Optional[Dict[str, Any]] = None, **kw: Any) -> Dict[str, Any]:
    raw: Dict[str, Any] = {**DEFAULT}
    g = globals()
    for key in (
        "server", "host", "port", "username", "user", "password",
        "database", "db", "schema", "db_type", "db_engine",
        "audit_table_names", "audit_tables", "table_names",
        "connect_timeout", "include_comments", "include_foreign_keys",
        "include_indexes", "include_schema_text", "max_tables", "allow_full_scan",
    ):
        if key in g and g[key] not in (None, ""):
            raw[key] = g[key]
    if isinstance(inputs, dict):
        raw.update({k: v for k, v in inputs.items() if v not in (None, "")})
    raw.update({k: v for k, v in kw.items() if v not in (None, "")})

    tables = _parse_tables(raw.get("audit_table_names") or raw.get("audit_tables"))
    if not tables:
        tn = raw.get("table_names")
        if tn and "/" not in str(tn):
            tables = _parse_tables(tn)

    db_type = _detect_db_type(raw)
    schema = str(raw.get("schema") or "").strip()
    if not schema:
        schema = "public" if db_type == "postgresql" else "dbo"
    elif schema == "dbo" and db_type == "postgresql":
        schema = "public"

    return {
        "db_type": db_type,
        "server": str(raw.get("server") or raw.get("host") or DEFAULT["server"]).strip(),
        "port": int(raw.get("port") or (5432 if db_type == "postgresql" else 1433)),
        "username": str(raw.get("username") or raw.get("user") or "").strip(),
        "password": str(raw.get("password") or "").strip(),
        "database": str(raw.get("database") or raw.get("db") or "").strip(),
        "schema": schema,
        "tables": tables,
        "audit_table_names": raw.get("audit_table_names"),
        "connect_timeout": int(raw.get("connect_timeout") or 10),
        "include_comments": _as_bool(raw.get("include_comments"), True),
        "include_foreign_keys": _as_bool(raw.get("include_foreign_keys"), True),
        "include_indexes": _as_bool(raw.get("include_indexes"), True),
        "include_schema_text": _as_bool(raw.get("include_schema_text"), False),
        "max_tables": int(raw.get("max_tables") or 0),
        "allow_full_scan": _as_bool(raw.get("allow_full_scan"), False),
    }


def _create_engine(cfg: Dict[str, Any]):
    from sqlalchemy import create_engine

    user = urllib.parse.quote_plus(cfg["username"])
    pwd = urllib.parse.quote_plus(cfg["password"])
    t = int(cfg["connect_timeout"])
    if cfg["db_type"] == "postgresql":
        url = (
            f"postgresql+psycopg2://{user}:{pwd}@"
            f"{cfg['server']}:{cfg['port']}/{cfg['database']}"
        )
        return create_engine(url, connect_args={"connect_timeout": t}, pool_pre_ping=True)
    url = f"mssql+pymssql://{user}:{pwd}@{cfg['server']}/{cfg['database']}"
    return create_engine(
        url,
        connect_args={"port": cfg["port"], "timeout": t, "login_timeout": t},
        pool_pre_ping=True,
    )


def _sql_in(prefix: str, names: List[str]) -> Tuple[str, Dict[str, Any]]:
    ph = ", ".join(f":{prefix}{i}" for i in range(len(names)))
    return ph, {f"{prefix}{i}": n for i, n in enumerate(names)}


def _pg_type(row: Any) -> str:
    dt = row["data_type"] or ""
    if row.get("character_maximum_length"):
        return f"{dt}({row['character_maximum_length']})"
    if row.get("numeric_precision") is not None:
        scale = row.get("numeric_scale") or 0
        return f"{dt}({row['numeric_precision']},{scale})"
    return dt


def _mssql_type(row: Any) -> str:
    dt = (row["data_type"] or "").upper()
    ml = int(row["max_length"] or 0)
    prec, scale = int(row["precision"] or 0), int(row["scale"] or 0)
    if dt in ("VARCHAR", "NVARCHAR", "CHAR", "NCHAR"):
        if ml == -1:
            return f"{dt}(MAX)"
        ln = ml // 2 if dt.startswith("N") and ml > 0 else ml
        return f"{dt}({ln})"
    if dt in ("DECIMAL", "NUMERIC"):
        return f"{dt}({prec},{scale})"
    return dt


def _empty_tables(schema: str, names: List[str]) -> Dict[str, Dict[str, Any]]:
    return {
        n: {
            "name": n,
            "schema": schema,
            "comment": "",
            "columns": [],
            "primary_keys": [],
            "foreign_keys": [],
            "indexes": [],
        }
        for n in names
    }


def _finalize(state: Dict[str, Dict[str, Any]], order: List[str]) -> List[Dict[str, Any]]:
    out = []
    for name in order:
        if name not in state:
            continue
        item = state[name]
        item["column_count"] = len(item["columns"])
        out.append(item)
    return out


def _list_tables_pg(engine, schema: str, limit: int) -> List[str]:
    from sqlalchemy import text

    sql = text(
        """
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = :schema AND table_type = 'BASE TABLE'
        ORDER BY table_name
        """
    )
    names: List[str] = []
    with engine.connect() as conn:
        for row in conn.execute(sql, {"schema": schema}).mappings():
            names.append(row["table_name"])
            if limit > 0 and len(names) >= limit:
                break
    return names


def _list_tables_mssql(engine, schema: str, limit: int) -> List[str]:
    from sqlalchemy import text

    sql = text(
        """
        SELECT t.name AS table_name FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = :schema ORDER BY t.name
        """
    )
    names: List[str] = []
    with engine.connect() as conn:
        for row in conn.execute(sql, {"schema": schema}).mappings():
            names.append(row["table_name"])
            if limit > 0 and len(names) >= limit:
                break
    return names


def _tables_exist_pg(engine, schema: str, names: List[str]) -> List[str]:
    from sqlalchemy import text

    in_sql, p = _sql_in("t", names)
    sql = text(
        f"""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = :schema AND table_type = 'BASE TABLE'
          AND table_name IN ({in_sql})
        """
    )
    with engine.connect() as conn:
        found = {
            r["table_name"]
            for r in conn.execute(sql, {"schema": schema, **p}).mappings()
        }
    return [n for n in names if n in found]


def _tables_exist_mssql(engine, schema: str, names: List[str]) -> List[str]:
    from sqlalchemy import text

    in_sql, p = _sql_in("t", names)
    sql = text(
        f"""
        SELECT t.name AS table_name FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = :schema AND t.name IN ({in_sql})
        """
    )
    with engine.connect() as conn:
        found = {
            r["table_name"]
            for r in conn.execute(sql, {"schema": schema, **p}).mappings()
        }
    return [n for n in names if n in found]


def _fetch_pg(
    engine,
    schema: str,
    table_names: List[str],
    *,
    with_comments: bool,
    with_fks: bool,
    with_indexes: bool,
) -> List[Dict[str, Any]]:
    from sqlalchemy import text

    if not table_names:
        return []
    in_sql, in_p = _sql_in("t", table_names)
    params: Dict[str, Any] = {"schema": schema, **in_p}
    state = _empty_tables(schema, table_names)

    with engine.connect() as conn:
        col_sql = text(
            f"""
            SELECT table_name, column_name, data_type,
                   character_maximum_length, numeric_precision, numeric_scale,
                   is_nullable, column_default
            FROM information_schema.columns
            WHERE table_schema = :schema AND table_name IN ({in_sql})
            ORDER BY table_name, ordinal_position
            """
        )
        for row in conn.execute(col_sql, params).mappings():
            t = row["table_name"]
            if t in state:
                state[t]["columns"].append(
                    {
                        "name": row["column_name"],
                        "type": _pg_type(row),
                        "nullable": row["is_nullable"] == "YES",
                        "default": row["column_default"],
                        "comment": "",
                    }
                )

        pk_sql = text(
            f"""
            SELECT tc.table_name, kcu.column_name, kcu.ordinal_position
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
              ON tc.constraint_schema = kcu.constraint_schema
             AND tc.constraint_name = kcu.constraint_name
            WHERE tc.constraint_type = 'PRIMARY KEY'
              AND tc.table_schema = :schema AND tc.table_name IN ({in_sql})
            ORDER BY tc.table_name, kcu.ordinal_position
            """
        )
        for row in conn.execute(pk_sql, params).mappings():
            state[row["table_name"]]["primary_keys"].append(row["column_name"])

        if with_fks:
            fk_sql = text(
                f"""
                SELECT tc.table_name, tc.constraint_name AS fk_name,
                       kcu.column_name AS parent_column,
                       ccu.table_schema AS referred_schema,
                       ccu.table_name AS referred_table,
                       ccu.column_name AS referred_column
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                  ON tc.constraint_schema = kcu.constraint_schema
                 AND tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage ccu
                  ON tc.constraint_schema = ccu.constraint_schema
                 AND tc.constraint_name = ccu.constraint_name
                WHERE tc.constraint_type = 'FOREIGN KEY'
                  AND tc.table_schema = :schema AND tc.table_name IN ({in_sql})
                ORDER BY tc.table_name, tc.constraint_name, kcu.ordinal_position
                """
            )
            acc: Dict[str, Dict[str, Any]] = {}
            for row in conn.execute(fk_sql, params).mappings():
                key = f"{row['table_name']}::{row['fk_name']}"
                if key not in acc:
                    acc[key] = {
                        "name": row["fk_name"],
                        "table": row["table_name"],
                        "constrained_columns": [],
                        "referred_schema": row["referred_schema"],
                        "referred_table": row["referred_table"],
                        "referred_columns": [],
                    }
                acc[key]["constrained_columns"].append(row["parent_column"])
                acc[key]["referred_columns"].append(row["referred_column"])
            for fk in acc.values():
                tn = fk.pop("table")
                cc, rc = fk["constrained_columns"], fk["referred_columns"]
                ref = fk["referred_table"]
                if fk["referred_schema"]:
                    ref = f"{fk['referred_schema']}.{ref}"
                pairs = ",".join(f"{a}={b}" for a, b in zip(cc, rc))
                fk["relation"] = f"{fk['name']}: {pairs} -> {ref}"
                state[tn]["foreign_keys"].append(fk)

        if with_indexes:
            ix_sql = text(
                f"""
                SELECT tablename AS table_name, indexname AS index_name, indexdef
                FROM pg_indexes
                WHERE schemaname = :schema AND tablename IN ({in_sql})
                ORDER BY tablename, indexname
                """
            )
            for row in conn.execute(ix_sql, params).mappings():
                t = row["table_name"]
                if t in state:
                    state[t]["indexes"].append(
                        {
                            "name": row["index_name"],
                            "columns": [],
                            "unique": "UNIQUE" in (row["indexdef"] or "").upper(),
                            "type": row["indexdef"] or "",
                        }
                    )

        if with_comments:
            cmt_sql = text(
                f"""
                SELECT c.relname AS table_name, a.attname AS column_name,
                       col_description(a.attrelid, a.attnum) AS comment
                FROM pg_class c
                JOIN pg_namespace n ON n.oid = c.relnamespace
                JOIN pg_attribute a ON a.attrelid = c.oid
                WHERE n.nspname = :schema AND c.relkind = 'r'
                  AND a.attnum > 0 AND NOT a.attisdropped
                  AND c.relname IN ({in_sql})
                """
            )
            for row in conn.execute(cmt_sql, params).mappings():
                t, col, cmt = row["table_name"], row["column_name"], row["comment"]
                if not cmt or t not in state:
                    continue
                for col_obj in state[t]["columns"]:
                    if col_obj["name"] == col:
                        col_obj["comment"] = str(cmt).strip()
                        break
            tbl_cmt = text(
                f"""
                SELECT c.relname AS table_name,
                       obj_description(c.oid) AS comment
                FROM pg_class c
                JOIN pg_namespace n ON n.oid = c.relnamespace
                WHERE n.nspname = :schema AND c.relkind = 'r'
                  AND c.relname IN ({in_sql})
                """
            )
            for row in conn.execute(tbl_cmt, params).mappings():
                if row["comment"] and row["table_name"] in state:
                    state[row["table_name"]]["comment"] = str(row["comment"]).strip()

    return _finalize(state, table_names)


def _fetch_mssql(
    engine,
    schema: str,
    table_names: List[str],
    *,
    with_comments: bool,
    with_fks: bool,
    with_indexes: bool,
) -> List[Dict[str, Any]]:
    from sqlalchemy import text

    if not table_names:
        return []
    in_sql, in_p = _sql_in("t", table_names)
    params: Dict[str, Any] = {"schema": schema, **in_p}
    state = _empty_tables(schema, table_names)
    cmt_sel = ", CAST(ep.value AS NVARCHAR(4000)) AS comment" if with_comments else ", NULL AS comment"
    cmt_join = (
        """
        LEFT JOIN sys.extended_properties ep
            ON ep.major_id = c.object_id AND ep.minor_id = c.column_id
           AND ep.name = N'MS_Description'
        """
        if with_comments
        else ""
    )

    with engine.connect() as conn:
        col_sql = text(
            f"""
            SELECT t.name AS table_name, c.name AS column_name,
                   TYPE_NAME(c.user_type_id) AS data_type,
                   c.max_length, c.precision, c.scale,
                   c.is_nullable, OBJECT_DEFINITION(c.default_object_id) AS column_default
                   {cmt_sel}
            FROM sys.columns c
            INNER JOIN sys.tables t ON c.object_id = t.object_id
            INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
            {cmt_join}
            WHERE s.name = :schema AND t.name IN ({in_sql})
            ORDER BY t.name, c.column_id
            """
        )
        for row in conn.execute(col_sql, params).mappings():
            t = row["table_name"]
            if t in state:
                state[t]["columns"].append(
                    {
                        "name": row["column_name"],
                        "type": _mssql_type(row),
                        "nullable": bool(row["is_nullable"]),
                        "default": row["column_default"],
                        "comment": (row.get("comment") or "").strip(),
                    }
                )

        pk_sql = text(
            f"""
            SELECT t.name AS table_name, c.name AS column_name
            FROM sys.indexes i
            INNER JOIN sys.index_columns ic
                ON i.object_id = ic.object_id AND i.index_id = ic.index_id
            INNER JOIN sys.columns c
                ON ic.object_id = c.object_id AND ic.column_id = c.column_id
            INNER JOIN sys.tables t ON i.object_id = t.object_id
            INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE i.is_primary_key = 1 AND s.name = :schema AND t.name IN ({in_sql})
            ORDER BY t.name, ic.key_ordinal
            """
        )
        for row in conn.execute(pk_sql, params).mappings():
            state[row["table_name"]]["primary_keys"].append(row["column_name"])

        if with_fks:
            fk_sql = text(
                f"""
                SELECT t.name AS table_name, fk.name AS fk_name,
                       pc.name AS parent_column, rs.name AS referred_schema,
                       rt.name AS referred_table, rc.name AS referred_column
                FROM sys.foreign_keys fk
                INNER JOIN sys.foreign_key_columns fkc ON fk.object_id = fkc.constraint_object_id
                INNER JOIN sys.tables pt ON fkc.parent_object_id = pt.object_id
                INNER JOIN sys.schemas ps ON pt.schema_id = ps.schema_id
                INNER JOIN sys.columns pc
                    ON fkc.parent_object_id = pc.object_id AND fkc.parent_column_id = pc.column_id
                INNER JOIN sys.tables rt ON fkc.referenced_object_id = rt.object_id
                INNER JOIN sys.schemas rs ON rt.schema_id = rs.schema_id
                INNER JOIN sys.columns rc
                    ON fkc.referenced_object_id = rc.object_id AND fkc.referenced_column_id = rc.column_id
                INNER JOIN sys.tables t ON pt.object_id = t.object_id
                INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
                WHERE ps.name = :schema AND t.name IN ({in_sql})
                ORDER BY t.name, fk.name, fkc.constraint_column_id
                """
            )
            acc: Dict[str, Dict[str, Any]] = {}
            for row in conn.execute(fk_sql, params).mappings():
                key = f"{row['table_name']}::{row['fk_name']}"
                if key not in acc:
                    acc[key] = {
                        "name": row["fk_name"],
                        "table": row["table_name"],
                        "constrained_columns": [],
                        "referred_schema": row["referred_schema"],
                        "referred_table": row["referred_table"],
                        "referred_columns": [],
                    }
                acc[key]["constrained_columns"].append(row["parent_column"])
                acc[key]["referred_columns"].append(row["referred_column"])
            for fk in acc.values():
                tn = fk.pop("table")
                cc, rc = fk["constrained_columns"], fk["referred_columns"]
                ref = fk["referred_table"]
                if fk["referred_schema"]:
                    ref = f"{fk['referred_schema']}.{ref}"
                pairs = ",".join(f"{a}={b}" for a, b in zip(cc, rc))
                fk["relation"] = f"{fk['name']}: {pairs} -> {ref}"
                state[tn]["foreign_keys"].append(fk)

        if with_indexes:
            ix_sql = text(
                f"""
                SELECT t.name AS table_name, i.name AS index_name, i.is_unique, i.type_desc,
                       c.name AS column_name, ic.is_included_column
                FROM sys.indexes i
                INNER JOIN sys.index_columns ic
                    ON i.object_id = ic.object_id AND i.index_id = ic.index_id
                INNER JOIN sys.columns c
                    ON ic.object_id = c.object_id AND ic.column_id = c.column_id
                INNER JOIN sys.tables t ON i.object_id = t.object_id
                INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
                WHERE i.type > 0 AND s.name = :schema AND t.name IN ({in_sql})
                ORDER BY t.name, i.name, ic.key_ordinal
                """
            )
            ix_acc: Dict[str, Dict[str, Any]] = {}
            for row in conn.execute(ix_sql, params).mappings():
                if row["is_included_column"]:
                    continue
                key = f"{row['table_name']}::{row['index_name']}"
                if key not in ix_acc:
                    ix_acc[key] = {
                        "name": row["index_name"],
                        "table": row["table_name"],
                        "columns": [],
                        "unique": bool(row["is_unique"]),
                        "type": row["type_desc"] or "",
                    }
                ix_acc[key]["columns"].append(row["column_name"])
            for ix in ix_acc.values():
                tn = ix.pop("table")
                state[tn]["indexes"].append(ix)

    return _finalize(state, table_names)


def _markdown(payload: Dict[str, Any]) -> str:
    lines = [f"# {payload.get('database')}", f"表数量: {payload.get('table_count', 0)}", ""]
    for t in payload.get("tables") or []:
        lines.append(f"## {t['name']}")
        lines.append("| 字段 | 类型 | 可空 | 说明 |")
        lines.append("|---|---|---|---|")
        for c in t.get("columns") or []:
            lines.append(
                f"| {c['name']} | {c['type']} | "
                f"{'是' if c.get('nullable') else '否'} | {c.get('comment') or ''} |"
            )
        if t.get("primary_keys"):
            lines.append(f"主键: {', '.join(t['primary_keys'])}")
        lines.append("")
    text = "\n".join(lines)
    return text[:MAX_TEXT] + ("\n...(截断)" if len(text) > MAX_TEXT else "")


def _pack(
    ok: bool,
    log: List[str],
    payload: Optional[Dict[str, Any]] = None,
    *,
    schema_text_out: str = "",
) -> Dict[str, Any]:
    msg = "\n".join(log)
    if len(msg) > MAX_MSG:
        msg = msg[:MAX_MSG] + "\n...(截断)"
    data = "{}"
    if ok and payload:
        data = json.dumps(payload, ensure_ascii=False)
        if len(data) > MAX_DATA:
            data = data[:MAX_DATA] + ',"_truncated":true}'
    return {
        "result": "成功" if ok else "失败",
        "message": msg,
        "schema_data": data,
        "table_count": (payload or {}).get("table_count", 0),
        "schema_text": schema_text_out,
    }


def main(inputs: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
    log = [f"=== 采集表结构 v{SCRIPT_VERSION} ==="]
    cfg: Dict[str, Any] = {}
    try:
        cfg = _resolve_config(inputs, **kwargs)
        log.append(
            f"type={cfg['db_type']} db={cfg['database']} schema={cfg['schema']} "
            f"tables={cfg['tables']!r}"
        )
        log.append(
            f"连接参数: {cfg['server']}:{cfg['port']} user={cfg['username']} "
            f"password={'已设置' if cfg['password'] else '未设置(请在Dify绑定password)'}"
        )

        names = cfg["tables"]
        if not names and not cfg["allow_full_scan"]:
            log.append("错误: 请绑定 audit_table_names。")
            return _pack(False, log)

        from sqlalchemy import text

        log.append(f"连接: {cfg['server']}:{cfg['port']}")
        engine = _create_engine(cfg)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        log.append("连接成功")

        schema = cfg["schema"]
        is_pg = cfg["db_type"] == "postgresql"
        if not names:
            names = (_list_tables_pg if is_pg else _list_tables_mssql)(
                engine, schema, cfg["max_tables"]
            )
            log.append(f"全库: {len(names)} 张表")
        else:
            exist = (_tables_exist_pg if is_pg else _tables_exist_mssql)(
                engine, schema, names
            )
            missing = sorted(set(names) - set(exist))
            if missing:
                log.append(f"警告: 不存在 {', '.join(missing)}")
            names = exist[: cfg["max_tables"]] if cfg["max_tables"] > 0 else exist

        if not names:
            engine.dispose()
            log.append("错误: 无有效表")
            return _pack(False, log)

        fetch = _fetch_pg if is_pg else _fetch_mssql
        tables = fetch(
            engine,
            schema,
            names,
            with_comments=cfg["include_comments"],
            with_fks=cfg["include_foreign_keys"],
            with_indexes=cfg["include_indexes"],
        )
        engine.dispose()
        log.append(f"读取 {len(tables)} 张表")
        log.append("=== 成功 ===")

        payload = {
            "db_type": cfg["db_type"],
            "server": cfg["server"],
            "port": cfg["port"],
            "database": cfg["database"],
            "schema": schema,
            "table_count": len(tables),
            "scan_mode": "filtered" if cfg["tables"] else "full",
            "tables": tables,
        }
        st = _markdown(payload) if cfg["include_schema_text"] else ""
        return _pack(True, log, payload, schema_text_out=st)
    except ImportError as e:
        log.append(f"缺少依赖: {e}")
        need = "psycopg2-binary" if cfg.get("db_type") == "postgresql" else "pymssql"
        log.append(f"请在 Dify 沙箱安装: pip install sqlalchemy {need}")
        return _pack(False, log)
    except Exception as e:
        log.append(f"异常: {type(e).__name__}: {e}")
        err = str(e).lower()
        if "18456" in err or "登录失败" in err or "login failed" in err:
            log.append(
                "提示: 已连上 SQL Server，但用户 sa 登录失败(18456)。"
                " 请核对 Dify 开始节点 password 是否与 SSMS 完全一致"
                "（注意首尾空格、是否复制错环境密码）。"
                " 若 SSMS 能登而 Dify 不能，可能是 SQL Server 禁止该来源 IP 使用 sa。"
            )
        elif "adaptive server" in err and cfg.get("db_type") == "postgresql":
            log.append(
                "提示: Adaptive Server + postgresql 类型 = 曾用 SQL Server 驱动连 PG，"
                " 请安装 psycopg2-binary 或检查 db_type。"
            )
        elif "unable to connect" in err or "20009" in err or "could not connect" in err:
            if cfg.get("db_type") == "mssql":
                log.append(
                    "提示: SQL Server 20009 在库正常时，常见原因是 Dify 里仍是旧脚本"
                    "（连接串 host,port 写错）。请确认日志首行含 "
                    f"v{SCRIPT_VERSION}；若无则是旧代码未替换。"
                )
            else:
                log.append(
                    f"提示: 无法连接 {cfg.get('server')}:{cfg.get('port')}。"
                    " 确认依赖与 CODE_EXECUTION_NETWORK_ENABLED=true。"
                )
        else:
            log.append(traceback.format_exc().strip()[:1200])
        return _pack(False, log)


def _apply_outputs(out: Dict[str, Any]) -> None:
    global result, message, schema_data, table_count, schema_text
    result = out["result"]
    message = out["message"]
    schema_data = out["schema_data"]
    table_count = int(out["table_count"])
    schema_text = out["schema_text"]


def _dify_has_inputs() -> bool:
    g = globals()
    return any(g.get(k) not in (None, "") for k in ("server", "database", "password", "audit_table_names"))


if __name__ == "__main__":
    cli: Dict[str, Any] = {}
    if len(sys.argv) > 1:
        try:
            cli = json.loads(sys.argv[1])
        except json.JSONDecodeError:
            cli = {"audit_table_names": sys.argv[1]}
    print(json.dumps(main(**cli), ensure_ascii=False, indent=2))
elif _dify_has_inputs():
    _apply_outputs(main())
