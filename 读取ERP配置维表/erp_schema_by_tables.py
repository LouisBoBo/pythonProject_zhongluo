#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按表名从 ERP 表结构文档提取小节，供 Dify 直接拼 context（替代循环知识库检索）。"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

_TABLE_HEADER_RE = re.compile(
    r"^#### \d+ (.+?) \(\s*([\w_]+)\s*\)\s*$",
    re.MULTILINE,
)
_SECTION_SPLIT_RE = re.compile(
    r"(?=^#### \d+ .+? \(\s*[\w_]+\s*\)\s*$)",
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
        table_name = m.group(2).strip()
        sections[table_name] = part.strip()
    return sections


def load_schema_index(
    md_path: Optional[Union[str, Path]] = None,
    json_path: Optional[Union[str, Path]] = None,
) -> Dict[str, str]:
    root = Path(__file__).resolve().parent
    if json_path is None:
        json_path = root / "erp_table_schemas.json"
    jp = Path(json_path)
    if jp.is_file():
        return json.loads(jp.read_text(encoding="utf-8"))

    if md_path is None:
        md_path = root.parent / "中络项目ERP 系统数据库表结构V1.0.md"
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
        # ERP 文档部分表用「-关联关系：」无加粗
        idx = text.find("-关联关系")
    if idx == -1:
        return text
    trimmed = text[:idx].rstrip()
    if not trimmed.endswith("---"):
        trimmed += "\n\n---"
    return trimmed


def _score_llm_tables(raw: Any) -> List[Tuple[str, int]]:
    """从选表 LLM JSON 提取 (表名, score)，按 score 降序。"""
    if not isinstance(raw, dict):
        return []
    tables = raw.get("tables") or raw.get("table_names") or []
    if not isinstance(tables, list):
        return []
    scored: List[Tuple[str, int]] = []
    for item in tables:
        if isinstance(item, str):
            name = item.strip()
            if name:
                scored.append((name, 0))
        elif isinstance(item, dict):
            name = (item.get("table_name") or item.get("name") or "").strip()
            if not name:
                continue
            try:
                score = int(item.get("score") or 0)
            except (TypeError, ValueError):
                score = 0
            scored.append((name, score))
    scored.sort(key=lambda x: (-x[1], x[0]))
    return scored


def resolve_schema_tables(
    *,
    tables: Any = None,
    tables_json: str = "",
    table_names: str = "",
    fact_table: str = "",
    join_tables: Any = None,
    max_tables: int = 8,
) -> List[str]:
    """
    拼 schema 的最小表集合：
    1. 若提供 fact_table/join_tables → 优先维表推导集合；
    2. 否则 LLM 选表 JSON 按 score 取 Top-N；
    3. max_tables 限制 token（默认 8）。
    """
    cap = max(1, int(max_tables or 8))
    ordered: List[str] = []
    seen: set[str] = set()

    def _add(name: str) -> None:
        key = name.strip()
        if not key:
            return
        norm = key.upper()
        if norm in seen:
            return
        seen.add(norm)
        ordered.append(key)

    ft = (fact_table or "").strip()
    joins = _normalize_table_names(join_tables)
    if ft or joins:
        if ft:
            _add(ft)
        for t in joins:
            _add(t)
        return ordered[:cap]

    raw = tables if tables not in (None, "", []) else None
    if raw is None:
        raw = tables_json or table_names or ""
    if isinstance(raw, str) and _looks_like_json_payload(raw):
        try:
            parsed = json.loads(_extract_json_text(raw))
        except json.JSONDecodeError:
            parsed = raw
    else:
        parsed = raw

    scored = _score_llm_tables(parsed) if isinstance(parsed, dict) else []
    if scored:
        for name, _ in scored:
            _add(name)
            if len(ordered) >= cap:
                break
        return ordered

    for name in _normalize_table_names(parsed):
        _add(name)
        if len(ordered) >= cap:
            break
    return ordered


def build_context_for_tables(
    table_names: Any,
    *,
    config: Optional[Dict[str, str]] = None,
    separator: str = "\n\n---\n\n",
    slim_schema: bool = True,
    fact_table: str = "",
    join_tables: Any = None,
    max_tables: int = 8,
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
    upper_index = {k.upper(): v for k, v in index.items()}
    if (fact_table or "").strip() or join_tables:
        requested = resolve_schema_tables(
            fact_table=fact_table,
            join_tables=join_tables,
            max_tables=max_tables,
        )
    elif isinstance(table_names, list):
        requested = resolve_schema_tables(tables=table_names, max_tables=max_tables)
    elif isinstance(table_names, str) and _looks_like_json_payload(table_names):
        requested = resolve_schema_tables(tables_json=table_names, max_tables=max_tables)
    else:
        requested = resolve_schema_tables(
            table_names=str(table_names or ""),
            max_tables=max_tables,
        )
    if not requested:
        requested = _normalize_table_names(table_names)

    seen: set[str] = set()
    ordered: List[str] = []
    for name in requested:
        key = name.strip()
        norm = key.upper()
        if norm in seen:
            continue
        seen.add(norm)
        ordered.append(key)

    parts: List[str] = []
    found: List[str] = []
    missing: List[str] = []

    for name in ordered:
        section = index.get(name) or upper_index.get(name.upper())
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
    fact_table: str = "",
    join_tables: Any = None,
    max_tables: int = 8,
    **kwargs: Any,
) -> Dict[str, Any]:
    raw = tables if tables not in (None, "", []) else None
    if raw is None:
        raw = tables_json or table_names or kwargs.get("tables") or ""
    ft = (fact_table or kwargs.get("fact_table") or "").strip()
    jt = join_tables if join_tables not in (None, "", []) else kwargs.get("join_tables")
    try:
        cap = int(max_tables or kwargs.get("max_tables") or 8)
    except (TypeError, ValueError):
        cap = 8
    return build_context_for_tables(
        raw,
        fact_table=ft,
        join_tables=jt,
        max_tables=cap,
    )
