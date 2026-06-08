#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""输出 MES 精简表名清单，供 Dify「分析业务表」LLM 选表（替代知识库检索）。"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, Optional

_EMBEDDED_CATALOG_SLIM: Optional[str] = None
_EMBEDDED_CATALOG_FULL_CHAR_COUNT: Optional[str] = None

_TABLE_HEADER_RE = re.compile(r"^#### \d+ .+?\(TBL_\w+\)", re.MULTILINE)
_TABLE_SECTION_RE = re.compile(
    r"^#### \d+ (.+?) \((TBL_\w+)\)\s*$",
    re.MULTILINE,
)
_BIZ_MEANING_RE = re.compile(r"- \*\*业务含义\*\*：(.+)")


def load_catalog_text(catalog_path: Optional[Path] = None) -> str:
    root = Path(__file__).resolve().parent
    if catalog_path is None:
        catalog_path = root.parent / "中络项目MES 系统表名清单V1.2.md"
    path = Path(catalog_path)
    if not path.is_file():
        raise FileNotFoundError(f"未找到表名清单：{path}")
    return path.read_text(encoding="utf-8")


def _get_catalog() -> str:
    return load_catalog_text()


def count_tables(catalog_text: str) -> int:
    return len(_TABLE_HEADER_RE.findall(catalog_text))


def slim_catalog_text(catalog_text: str) -> str:
    """选表用精简清单：每表一行「表名 | 中文名 | 业务含义」，去掉关联关系与章节说明。"""
    lines: list[str] = [
        "# MES 表清单（精简·选表用，仅表名+业务含义）",
        "# 格式：TBL_XXX | 中文表名 | 业务含义",
        "",
    ]
    matches = list(_TABLE_SECTION_RE.finditer(catalog_text))
    seen: set[str] = set()
    for i, m in enumerate(matches):
        label = (m.group(1) or "").strip()
        tname = (m.group(2) or "").strip()
        if tname in seen:
            continue
        seen.add(tname)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(catalog_text)
        block = catalog_text[start:end]
        biz_m = _BIZ_MEANING_RE.search(block)
        biz = (biz_m.group(1).strip() if biz_m else label).replace("\n", " ")
        lines.append(f"{tname} | {label} | {biz}")
    return "\n".join(lines).strip()


def count_slim_tables(slim_text: str) -> int:
    return sum(1 for line in slim_text.splitlines() if line.startswith("TBL_"))


def _get_catalog_slim() -> str:
    global _EMBEDDED_CATALOG_SLIM
    if _EMBEDDED_CATALOG_SLIM is not None:
        return _EMBEDDED_CATALOG_SLIM
    return slim_catalog_text(_get_catalog())


def main(**kwargs: Any) -> Dict[str, str]:
    slim = _get_catalog_slim()
    n = count_slim_tables(slim)
    if _EMBEDDED_CATALOG_FULL_CHAR_COUNT is not None:
        full_chars = _EMBEDDED_CATALOG_FULL_CHAR_COUNT
    else:
        full = load_catalog_text()
        if n == 0:
            n = count_tables(full)
        full_chars = str(len(full))
    return {
        "table_catalog": str(slim),
        "table_count": str(n),
        "char_count": str(len(slim)),
        "char_count_full": str(full_chars),
    }
