#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 erp_table_schemas.json 提取各表列名索引，供维表节点 / SQL 修复节点嵌入 Dify。"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

_ROOT = Path(__file__).resolve().parent if "__file__" in globals() else Path(".")
_SCHEMA_JSON = _ROOT / "erp_table_schemas.json"

_EMBEDDED_SCHEMA_COLUMNS: Dict[str, List[List[str]]] | None = None


def parse_table_columns(section_md: str) -> List[Tuple[str, str]]:
    """解析 schema Markdown 小节 → [(列名, 中文说明)]。"""
    out: List[Tuple[str, str]] = []
    for line in (section_md or "").splitlines():
        if not line.startswith("|") or "字段名" in line or "---" in line:
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 5:
            continue
        col, desc = parts[0], parts[4]
        if not col or not re.match(r"^[\w_]+$", col):
            continue
        label = desc if desc and desc not in ("-", "—") else col
        out.append((col, label))
    return out


def build_column_index(schemas: Dict[str, str]) -> Dict[str, List[List[str]]]:
    """TableName → [[col, label], ...]（紧凑 JSON，供 Dify 嵌入）。"""
    out: Dict[str, List[List[str]]] = {}
    for table, section in schemas.items():
        cols = parse_table_columns(section)
        if cols:
            out[table] = [[c, l] for c, l in cols]
    return out


def load_column_index_from_file(json_path: Path | None = None) -> Dict[str, List[List[str]]]:
    jp = json_path or _SCHEMA_JSON
    if not jp.is_file():
        return {}
    schemas = json.loads(jp.read_text(encoding="utf-8"))
    return build_column_index(schemas)


def set_embedded_schema_columns(data: Dict[str, List[List[str]]] | None) -> None:
    global _EMBEDDED_SCHEMA_COLUMNS
    _EMBEDDED_SCHEMA_COLUMNS = data


def get_table_columns(table_name: str) -> List[Tuple[str, str]]:
    """按表名取列清单（大小写不敏感）。"""
    key = (table_name or "").strip()
    if not key:
        return []

    index = _EMBEDDED_SCHEMA_COLUMNS
    if index is None:
        index = load_column_index_from_file()

    if key in index:
        return [(r[0], r[1]) for r in index[key]]
    upper = key.upper()
    for k, rows in index.items():
        if k.upper() == upper:
            return [(r[0], r[1]) for r in rows]
    return []


def valid_column_names(table_name: str) -> set[str]:
    cols = {c.upper() for c, _ in get_table_columns(table_name)}
    if cols:
        return cols
    # 数据字典无字段明细时，仅允许已知最小列集（避免 LLM 编造整表结构）
    if (table_name or "").upper() == "M_PURCHASEORDER":
        return {"RECID"}
    return set()
