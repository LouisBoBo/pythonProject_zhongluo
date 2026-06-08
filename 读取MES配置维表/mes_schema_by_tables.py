#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按表名从 MES 表结构文档提取小节，供 Dify 直接拼 context（替代循环知识库检索）。"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

_TABLE_HEADER_RE = re.compile(
    r"^#### \d+ (.+?) \( (TBL_\w+) \)\s*$",
    re.MULTILINE,
)
_SECTION_SPLIT_RE = re.compile(
    r"(?=^#### \d+ .+? \( TBL_\w+ \)\s*$)",
    re.MULTILINE,
)

_EMBEDDED_SCHEMAS: Optional[Dict[str, str]] = None


def parse_schema_markdown(md_text: str) -> Dict[str, str]:
    """从《系统数据库表结构》Markdown 解析 table_name -> 完整小节文本。"""
    sections: Dict[str, str] = {}
    for part in _SECTION_SPLIT_RE.split(md_text):
        m = _TABLE_HEADER_RE.search(part)
        if not m:
            continue
        table_name = m.group(2)
        sections[table_name] = part.strip()
    return sections


def load_schema_index(
    md_path: Optional[Union[str, Path]] = None,
    json_path: Optional[Union[str, Path]] = None,
) -> Dict[str, str]:
    root = Path(__file__).resolve().parent
    if json_path is None:
        json_path = root / "mes_table_schemas.json"
    jp = Path(json_path)
    if jp.is_file():
        return json.loads(jp.read_text(encoding="utf-8"))

    if md_path is None:
        md_path = root.parent / "中络项目MES 系统数据库表结构V1.2.md"
    mp = Path(md_path)
    if not mp.is_file():
        raise FileNotFoundError(f"未找到表结构文档：{mp}")
    return parse_schema_markdown(mp.read_text(encoding="utf-8"))


def _get_index(config: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    global _EMBEDDED_SCHEMAS
    if config is not None:
        return config
    if _EMBEDDED_SCHEMAS is not None:
        return _EMBEDDED_SCHEMAS
    return load_schema_index()


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)


def _extract_json_text(text: str) -> str:
    """从 LLM 输出中提取 JSON：去 Markdown 围栏、截取首尾配对的 {} 或 []。"""
    s = (text or "").strip()
    if not s:
        return s
    m = _JSON_FENCE_RE.search(s)
    if m:
        return m.group(1).strip()
    for opener, closer in (("{", "}"), ("[", "]")):
        start = s.find(opener)
        if start == -1:
            continue
        depth = 0
        for i in range(start, len(s)):
            ch = s[i]
            if ch == opener:
                depth += 1
            elif ch == closer:
                depth -= 1
                if depth == 0:
                    return s[start : i + 1]
    return s


def _looks_like_json_payload(s: str) -> bool:
    t = s.strip()
    return (
        t.startswith("{")
        or t.startswith("[")
        or "```" in t
        or '"tables"' in t
        or "'tables'" in t
    )


def _normalize_table_names(raw: Any) -> List[str]:
    """支持：JSON 选表结果、表名数组、逗号分隔字符串。"""
    if raw is None:
        return []

    if isinstance(raw, str):
        s = raw.strip()
        if not s:
            return []
        if _looks_like_json_payload(s):
            try:
                raw = json.loads(_extract_json_text(s))
            except json.JSONDecodeError:
                return []
        else:
            return [t.strip() for t in re.split(r"[,，\s]+", s) if t.strip()]

    if isinstance(raw, dict):
        tables = raw.get("tables") or raw.get("table_names") or []
        if isinstance(tables, list):
            return _normalize_table_names(tables)
        if isinstance(tables, str):
            return _normalize_table_names(tables)

    if isinstance(raw, list):
        out: List[str] = []
        for item in raw:
            if isinstance(item, str):
                name = item.strip()
                if name:
                    out.append(name)
            elif isinstance(item, dict):
                name = (item.get("table_name") or item.get("name") or "").strip()
                if name:
                    out.append(name)
        return out

    return []


_RELATIONS_MARKER = "- **关联关系**"
_DB_LINE_RE = re.compile(r"^- \*\*所属数据库\*\*.*$", re.MULTILINE)


def slim_schema_section(
    section: str,
    *,
    drop_relations: bool = True,
    drop_db_line: bool = False,
) -> str:
    """压缩表结构小节：JOIN 已在维表映射规则中，关联关系块占 token 且易误导。"""
    text = (section or "").strip()
    if not text:
        return text
    if drop_db_line:
        text = _DB_LINE_RE.sub("", text).strip()
    if not drop_relations:
        return text
    idx = text.find(_RELATIONS_MARKER)
    if idx == -1:
        return text
    trimmed = text[:idx].rstrip()
    if not trimmed.endswith("---"):
        trimmed += "\n\n---"
    return trimmed


def build_context_for_tables(
    table_names: Any,
    *,
    config: Optional[Dict[str, str]] = None,
    separator: str = "\n\n---\n\n",
    slim_schema: bool = True,
) -> Dict[str, Any]:
    """
    按表名列表拼接【参考表结构】context。

    返回（均为 string，供 Dify 代码节点出参）：
      context: 拼接后的 Markdown 小节
      table_count: 成功命中的表数
      found_tables: 命中的表名（有序、去重）
      missing_tables: 未命中的表名
    """
    index = _get_index(config)
    requested = _normalize_table_names(table_names)

    seen: set[str] = set()
    ordered: List[str] = []
    for name in requested:
        key = name.upper()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(key)

    parts: List[str] = []
    found: List[str] = []
    missing: List[str] = []

    for name in ordered:
        section = index.get(name) or index.get(name.upper())
        if section:
            if slim_schema:
                section = slim_schema_section(section)
            parts.append(section)
            found.append(name)
        else:
            missing.append(name)

    return {
        "context": str(separator.join(parts)),
        "table_count": str(len(found)),
        "found_tables": ",".join(found),
        "missing_tables": ",".join(missing),
    }


def main(
    tables: Any = None,
    tables_json: str = "",
    table_names: str = "",
    **kwargs: Any,
) -> Dict[str, Any]:
    # 优先级：tables（上游数组）> tables_json（JSON 字符串）> table_names
    raw = tables if tables not in (None, "", []) else None
    if raw is None:
        raw = tables_json or table_names or kwargs.get("tables") or ""
    return build_context_for_tables(raw)
