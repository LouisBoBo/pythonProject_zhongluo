#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dify「代码」节点：从 PostgreSQL 读取 mes 数据行，拼成 JSON 字符串。

Dify 输入变量（均可选）：
  - table_name / table：表名，默认 mes_data_records
  - column_name / column：列名，默认 records
  - limit：最多读取行数（整数）

Dify 输出变量：
  - records：JSON 字符串数组，形如 ["{...}","{...}"]
    数组内每条为扁平工单 JSON 字符串（与 insert 入参、截图格式一致）
    序列化后超过 400000 字符时自动从尾部截断，保证仍为合法 JSON

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
MAX_OUTPUT_CHARS = 400_000

_TABLE_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)?$")
_COLUMN_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _merge_inputs(
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
    inner2 = merged.get("inputs")
    if isinstance(inner2, dict):
        merged.update(inner2)
    return merged


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


def _item_to_json_string(item: Any) -> str:
    """单条记录 → JSON 字符串（与 insert 入参单条格式一致）。"""
    if item is None:
        raise ValueError("记录不能为 null")
    if isinstance(item, str):
        s = item.strip()
        if not s:
            return ""
        try:
            json.loads(s)
            return s
        except json.JSONDecodeError:
            return item
    return json.dumps(item, ensure_ascii=False)


def _cell_to_record_strings(cell: Any) -> List[str]:
    """
    将库中一行 TEXT 还原为 0..n 条 JSON 字符串。

    若历史数据误存为 {"records":[...]}，会展开内层，避免输出再多包一层 records。
    """
    if cell is None:
        return []
    if not isinstance(cell, str):
        return [_item_to_json_string(cell)]

    s = cell.strip()
    if not s:
        return []

    try:
        parsed = json.loads(s)
    except json.JSONDecodeError:
        return [cell]

    if isinstance(parsed, dict) and set(parsed.keys()) == {"records"}:
        inner = parsed["records"]
        if isinstance(inner, list):
            return [_item_to_json_string(x) for x in inner]
        if inner is None:
            return []
        return [_item_to_json_string(inner)]

    return [_item_to_json_string(parsed)]


def fetch_records_items(
    log: List[str],
    *,
    table: str = DEFAULT_TABLE,
    column: str = DEFAULT_COLUMN,
    limit: Optional[int] = None,
) -> List[Any]:
    col = _validate_column(column)
    table = _validate_table(table)
    log.append(
        f"连接数据库: {DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']} "
        f"表={table} 列={col}"
    )

    conn = _connect()
    log.append("数据库连接成功")
    cur = conn.cursor()
    try:
        sql = (
            f"SELECT {_quote_ident(col)} FROM {_qualified_table_sql(table)} "
            f"ORDER BY id ASC"
        )
        params: tuple[Any, ...] = ()
        if limit is not None:
            lim = int(limit)
            if lim < 0:
                raise ValueError(f"limit 不能为负数: {limit!r}")
            sql += " LIMIT %s"
            params = (lim,)

        cur.execute(sql, params)
        rows = cur.fetchall()
        items: List[str] = []
        for row in rows:
            items.extend(_cell_to_record_strings(row[0]))
        log.append(f"查询完成: 共 {len(items)} 条（来自 {len(rows)} 行）")
        return items
    finally:
        try:
            cur.close()
        except Exception:
            pass
        conn.close()
        log.append("数据库连接已关闭")


def _parse_limit(merged: Dict[str, Any]) -> Optional[int]:
    raw = merged.get("limit")
    if raw is None or raw == "":
        return None
    if isinstance(raw, bool):
        raise ValueError("limit 须为整数")
    return int(raw)


def _truncate_single_item(item: str, max_chars: int) -> str:
    """单条过长时截断内容，使 json.dumps([item]) 不超过 max_chars。"""
    if len(json.dumps([item], ensure_ascii=False)) <= max_chars:
        return item
    lo, hi = 0, len(item)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if len(json.dumps([item[:mid]], ensure_ascii=False)) <= max_chars:
            lo = mid
        else:
            hi = mid - 1
    return item[:lo]


def _to_records_json(
    items: List[str], max_chars: int = MAX_OUTPUT_CHARS
) -> tuple[str, int, bool]:
    """序列化为 JSON 数组字符串；超长则从尾部减少条目（必要时截断单条）。返回 (json, 保留条数, 是否截断)。"""
    if not items:
        return "[]", 0, False

    kept = list(items)
    truncated = False
    while len(kept) > 1:
        out = json.dumps(kept, ensure_ascii=False)
        if len(out) <= max_chars:
            return out, len(kept), truncated
        kept.pop()
        truncated = True

    before = kept[0]
    kept[0] = _truncate_single_item(kept[0], max_chars)
    if len(kept[0]) < len(before):
        truncated = True
    return json.dumps(kept, ensure_ascii=False), 1, truncated


def main(
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, str]:
    """
    Dify 代码节点入口。返回 records（JSON 字符串数组 "[...]"）。
    """
    log: List[str] = ["=== get_mes_data_from_db 开始 ==="]
    try:
        merged = _merge_inputs(inputs=inputs, **kwargs)
        table = str(merged.get("table_name") or merged.get("table") or DEFAULT_TABLE)
        column = str(merged.get("column_name") or merged.get("column") or DEFAULT_COLUMN)
        limit = _parse_limit(merged)

        items = fetch_records_items(log, table=table, column=column, limit=limit)
        total = len(items)
        records_json, kept, truncated = _to_records_json(items)
        out_len = len(records_json)
        if truncated:
            if kept < total:
                log.append(
                    f"输出已截断: 原 {total} 条 → 保留 {kept} 条, "
                    f"长度 {out_len} 字符 (上限 {MAX_OUTPUT_CHARS})"
                )
            else:
                log.append(
                    f"输出已截断: 单条内容过长已裁切, "
                    f"长度 {out_len} 字符 (上限 {MAX_OUTPUT_CHARS})"
                )
        log.append(f"输出 JSON 长度: {out_len} 字符")
        log.append("=== 执行成功 ===")
        return {"records": records_json}
    except Exception as e:
        log.append(f"异常: {type(e).__name__}: {e}")
        log.append(traceback.format_exc().strip())
        log.append("=== 执行失败，返回空 records ===")
        # 失败时仍返回合法空数组，便于下游节点继续解析
        return {"records": _to_records_json([])[0]}  # "[]"


if __name__ == "__main__":
    out = main(limit=sys.argv[1] if len(sys.argv) > 1 else None)
    print(json.dumps(out, ensure_ascii=False, indent=2))
