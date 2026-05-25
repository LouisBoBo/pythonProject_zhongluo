#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dify「代码」节点：将 JSON 数组逐条写入 PostgreSQL（每元素一行）。

Dify 输入变量：
  - records：JSON 数组字符串，或含 records 键的对象
  - conversation_id：Dify 会话 ID；仅当与库中上次会话不同时 TRUNCATE 再插入，同会话追加
  - 可选：table_name、column_name（默认 mes_data_records / records）

Dify 输出变量：
  - result：成功 | 失败
  - message：执行日志

数据库连接配置写死在 DB_CONFIG，不在 Dify 中传入。
"""

from __future__ import annotations

import json
import re
import sys
import traceback
from typing import Any, Dict, List, Optional

DB_CONFIG: Dict[str, Any] = {
    "host": "192.168.60.2",
    "port": 15432,
    "database": "demo",
    "user": "postgres",
    "password": "postgres",
    "connect_timeout": 10,
}

DEFAULT_TABLE = "mes_data_records"
DEFAULT_COLUMN = "records"
DEFAULT_STATE_TABLE = "mes_data_insert_state"

_RESULT_OK = "成功"
_RESULT_FAIL = "失败"
_MAX_MESSAGE_LEN = 8000

_TABLE_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)?$")
_COLUMN_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

_CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS mes_data_records (
    id BIGSERIAL PRIMARY KEY,
    records TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
)
"""

_CREATE_STATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS mes_data_insert_state (
    table_name TEXT PRIMARY KEY,
    conversation_id TEXT NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
)
"""


def _strip_code_fence(s: str) -> str:
    s = s.strip()
    if not s.startswith("```"):
        return s
    lines = s.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip()


def _merge_inputs(
    records: Any = None,
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    merged: Dict[str, Any] = {}
    if inputs and isinstance(inputs, dict):
        merged.update(inputs)
        inner = inputs.get("inputs")
        if isinstance(inner, dict):
            merged.update(inner)
    merged.update(kwargs)
    if records is not None:
        merged["records"] = records
    inner2 = merged.get("inputs")
    if isinstance(inner2, dict):
        merged.update(inner2)
    return merged


def _parse_json_value(raw: Any) -> Any:
    if isinstance(raw, str):
        s = _strip_code_fence(raw)
        if not s:
            return None
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            start_obj = s.find("{")
            start_arr = s.find("[")
            if start_obj == -1 and start_arr == -1:
                raise
            if start_arr == -1 or (start_obj != -1 and start_obj < start_arr):
                start, end_char = start_obj, "}"
            else:
                start, end_char = start_arr, "]"
            end = s.rfind(end_char)
            if end <= start:
                raise
            return json.loads(s[start : end + 1])
    return raw


def _extract_raw_records(merged: Dict[str, Any]) -> Any:
    raw: Any = None
    for key in ("records", "records_json", "json_str", "text", "arg1", "content", "payload"):
        v = merged.get(key)
        if v is not None and v != "":
            raw = v
            break
    if raw is None and len(merged) == 1:
        only_key = next(iter(merged.keys()))
        if only_key not in (
            "table_name",
            "table",
            "column_name",
            "column",
            "ensure_table",
            "conversation_id",
            "inputs",
        ):
            raw = next(iter(merged.values()))
    return raw


def _item_to_row_string(item: Any, index: int) -> str:
    if item is None:
        raise ValueError(f"records[{index}] 不能为 null")
    if isinstance(item, str):
        return item
    return json.dumps(item, ensure_ascii=False)


def _parse_records_items(merged: Dict[str, Any], log: List[str]) -> List[str]:
    raw = _extract_raw_records(merged)
    if raw is None:
        log.append("未找到 records 入参")
        return []

    log.append(f"records 入参类型: {type(raw).__name__}")

    try:
        parsed = _parse_json_value(raw) if isinstance(raw, str) else raw
    except json.JSONDecodeError as e:
        preview = str(raw)[:200].replace("\n", " ")
        raise ValueError(f"records JSON 解析失败: {e}；内容前200字: {preview}") from e

    if isinstance(parsed, dict) and "records" in parsed:
        log.append("已从对象中提取 records 数组")
        parsed = parsed["records"]

    if parsed is None:
        log.append("解析结果为空")
        return []

    if not isinstance(parsed, list):
        raise ValueError(f"records 必须是 JSON 数组，当前为 {type(parsed).__name__}")

    items = [_item_to_row_string(item, i) for i, item in enumerate(parsed)]
    if items:
        sizes = [len(s.encode("utf-8")) for s in items]
        log.append(
            f"解析完成: 共 {len(items)} 条；单条字节 min={min(sizes)} max={max(sizes)} total={sum(sizes)}"
        )
    else:
        log.append("解析完成: 数组为空，共 0 条")
    return items


def _format_db_target(table: str, column: str) -> str:
    return (
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']} "
        f"(PostgreSQL) 表={table} 列={column}"
    )


def _mk_result(ok: bool, log: List[str]) -> Dict[str, str]:
    msg = "\n".join(log)
    if len(msg) > _MAX_MESSAGE_LEN:
        msg = msg[: _MAX_MESSAGE_LEN - 20] + "\n...(日志已截断)"
    return {
        "result": _RESULT_OK if ok else _RESULT_FAIL,
        "message": msg,
    }


def _validate_table(table: str) -> str:
    t = table.strip()
    if not t or not _TABLE_NAME_RE.match(t):
        raise ValueError(f"非法表名: {table!r}")
    return t


def _validate_column(column: str) -> str:
    c = column.strip()
    if not c or not _COLUMN_NAME_RE.match(c):
        raise ValueError(f"非法列名: {column!r}")
    return c


def _quote_ident(part: str) -> str:
    return '"' + part.replace('"', '""') + '"'


def _qualified_table_sql(table: str) -> str:
    parts = _validate_table(table).split(".")
    return ".".join(_quote_ident(p) for p in parts)


def _connect():
    try:
        import psycopg2
    except ImportError as e:
        raise ImportError(
            "未安装 psycopg2，请在 Dify 代码沙箱安装: pip install psycopg2-binary"
        ) from e

    return psycopg2.connect(
        host=str(DB_CONFIG["host"]),
        port=int(DB_CONFIG["port"]),
        dbname=str(DB_CONFIG["database"]),
        user=str(DB_CONFIG["user"]),
        password=str(DB_CONFIG["password"]),
        connect_timeout=int(DB_CONFIG["connect_timeout"]),
    )


def _normalize_conversation_id(raw: Any) -> str:
    if raw is None or raw == "":
        raise ValueError("缺少必填参数 conversation_id（Dify 会话 ID）")
    cid = str(raw).strip()
    if not cid:
        raise ValueError("conversation_id 不能为空")
    return cid


def _ensure_state_table(cur: Any, log: List[str]) -> None:
    cur.execute(_CREATE_STATE_TABLE_SQL)
    log.append(f"已确保会话状态表存在: {DEFAULT_STATE_TABLE}")


def _get_stored_conversation_id(cur: Any, table: str) -> Optional[str]:
    qstate = _qualified_table_sql(DEFAULT_STATE_TABLE)
    cur.execute(
        f"SELECT conversation_id FROM {qstate} WHERE table_name = %s",
        (table,),
    )
    row = cur.fetchone()
    return str(row[0]) if row and row[0] is not None else None


def _upsert_conversation_id(cur: Any, table: str, conversation_id: str) -> None:
    qstate = _qualified_table_sql(DEFAULT_STATE_TABLE)
    cur.execute(
        f"""
        INSERT INTO {qstate} (table_name, conversation_id, updated_at)
        VALUES (%s, %s, NOW())
        ON CONFLICT (table_name) DO UPDATE
        SET conversation_id = EXCLUDED.conversation_id,
            updated_at = NOW()
        """,
        (table, conversation_id),
    )


def _parse_bool(raw: Any, default: bool = True) -> bool:
    if raw is None or raw == "":
        return default
    if isinstance(raw, bool):
        return raw
    if isinstance(raw, (int, float)):
        return bool(raw)
    s = str(raw).strip().lower()
    if s in ("1", "true", "yes", "y", "on", "是"):
        return True
    if s in ("0", "false", "no", "n", "off", "否"):
        return False
    raise ValueError(f"无法解析布尔值: {raw!r}")


def _clear_table_before_insert(
    cur: Any,
    log: List[str],
    *,
    table: str,
    restart_identity: bool = True,
) -> int:
    qtable = _qualified_table_sql(table)
    cur.execute(f"SELECT COUNT(*) FROM {qtable}")
    row = cur.fetchone()
    before = int(row[0]) if row else 0
    log.append(f"插入前清表: 当前 {before} 行")

    sql = f"TRUNCATE TABLE {qtable}"
    if restart_identity:
        sql += " RESTART IDENTITY"
    log.append(f"执行 SQL: {sql}")
    cur.execute(sql)
    log.append(f"已清空表 {table}，删除 {before} 行")
    return before


def insert_records_items(
    items: List[str],
    log: List[str],
    *,
    conversation_id: str,
    table: str = DEFAULT_TABLE,
    column: str = DEFAULT_COLUMN,
    ensure_table: bool = True,
    restart_identity: bool = True,
) -> int:
    if not items:
        return 0

    col = _validate_column(column)
    table = _validate_table(table)
    conversation_id = _normalize_conversation_id(conversation_id)
    log.append(f"会话 ID: {conversation_id}")
    log.append(f"开始连接数据库: {_format_db_target(table, col)}")
    conn = _connect()
    log.append("数据库连接成功")
    cur = conn.cursor()
    try:
        if ensure_table and table.split(".")[-1].lower() == DEFAULT_TABLE:
            cur.execute(_CREATE_TABLE_SQL)
            log.append(f"已确保表存在: {DEFAULT_TABLE}")
        _ensure_state_table(cur, log)
        stored_cid = _get_stored_conversation_id(cur, table)
        if stored_cid is None:
            log.append("首次写入该表，将清表后插入")
            should_clear = True
        elif stored_cid != conversation_id:
            log.append(
                f"会话已变更: {stored_cid!r} -> {conversation_id!r}，将清表后插入"
            )
            should_clear = True
        else:
            log.append(f"会话未变更 ({conversation_id})，跳过清表，追加插入")
            should_clear = False
        if should_clear:
            _clear_table_before_insert(
                cur, log, table=table, restart_identity=restart_identity
            )
            _upsert_conversation_id(cur, table, conversation_id)
            log.append(f"已更新会话状态: table={table} conversation_id={conversation_id}")
        sql = (
            f"INSERT INTO {_qualified_table_sql(table)} "
            f"({_quote_ident(col)}) VALUES (%s)"
        )
        total = len(items)
        for i, row in enumerate(items):
            try:
                cur.execute(sql, (row,))
            except Exception as e:
                row_bytes = len(row.encode("utf-8"))
                log.append(
                    f"第 {i + 1}/{total} 条插入失败: {type(e).__name__}: {e}；"
                    f"该行字节={row_bytes}"
                )
                raise
            if total <= 20 or (i + 1) % 50 == 0 or i + 1 == total:
                log.append(f"已插入 {i + 1}/{total} 条")
        conn.commit()
        log.append(f"事务提交成功，共写入 {len(items)} 条")
        return len(items)
    except Exception:
        try:
            conn.rollback()
            log.append("事务已回滚")
        except Exception:
            pass
        raise
    finally:
        try:
            cur.close()
        except Exception:
            pass
        conn.close()
        log.append("数据库连接已关闭")


def main(
    records: Any = None,
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, str]:
    """Dify 代码节点入口。返回 result、message。"""
    log: List[str] = ["=== insert_mes_data_todb 开始 ==="]
    try:
        merged = _merge_inputs(records=records, inputs=inputs, **kwargs)
        items = _parse_records_items(merged, log)
        if not items:
            log.append("失败: 无有效数据可插入")
            return _mk_result(False, log)

        table = str(merged.get("table_name") or merged.get("table") or DEFAULT_TABLE)
        column = str(merged.get("column_name") or merged.get("column") or DEFAULT_COLUMN)
        ensure_table = _parse_bool(merged.get("ensure_table"), default=True)
        restart_identity = _parse_bool(merged.get("restart_identity"), default=True)
        conversation_id = _normalize_conversation_id(
            merged.get("conversation_id") or merged.get("conversationId")
        )

        insert_records_items(
            items,
            log,
            conversation_id=conversation_id,
            table=table,
            column=column,
            ensure_table=ensure_table,
            restart_identity=restart_identity,
        )
        log.append("=== 执行成功 ===")
        return _mk_result(True, log)
    except Exception as e:
        log.append(f"异常: {type(e).__name__}: {e}")
        log.append(traceback.format_exc().strip())
        log.append("=== 执行失败 ===")
        return _mk_result(False, log)


if __name__ == "__main__":
    sample = (
        sys.argv[1]
        if len(sys.argv) > 1
        else '{"records":["{\\"k\\":1}","{\\"k\\":2}"]}'
    )
    print(
        json.dumps(
            main(records=sample, conversation_id="local-test-conversation"),
            ensure_ascii=False,
            indent=2,
        )
    )
