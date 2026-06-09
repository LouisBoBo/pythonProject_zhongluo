#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从《中络项目ERP 系统数据库表结构V1.0.md》生成表结构索引，并打包为 Dify 代码节点：

  python3 build_erp_schema_bundle.py

维护：
  1. 改表结构 .md
  2. 运行本脚本
  3. 复制 dify_erp_schema_by_tables.py 到 Dify 代码节点
"""

from __future__ import annotations

import json
from pathlib import Path

from erp_schema_by_tables import parse_schema_markdown

ROOT = Path(__file__).resolve().parent
MD_FILE = ROOT.parent / "中络项目ERP 系统数据库表结构V1.0.md"
JSON_FILE = ROOT / "erp_table_schemas.json"
OUT = ROOT / "dify_erp_schema_by_tables.py"

HEADER = '''# -*- coding: utf-8 -*-
# 【Dify 代码节点专用 · 由 build_erp_schema_bundle.py 自动生成，请勿手改】
# 维护：改 中络项目ERP 系统数据库表结构V1.0.md → python3 build_erp_schema_bundle.py → 复制到 Dify
#
# 作用：按选表结果直接拼【参考表结构】，替代「每张表循环知识库检索」，毫秒级完成。
#
# 入参（任选其一，推荐 tables_json）：
#   tables — 上游表名数组
#   tables_json — 选表 LLM JSON 字符串（按 score 取 Top max_tables，默认 8）
#   table_names — 逗号/空格分隔表名
#   fact_table / join_tables — 来自维表节点时优先用（最小 schema 集，推荐 workflow 维表在 schema 前）
#   max_tables — 最多拼接表数（默认 8）
# 出参：
#   context, table_count, found_tables, missing_tables

'''

DIFY_ENTRY = '''
# --- Dify 入口 ---
try:
    tables
except NameError:
    tables = None
try:
    tables_json
except NameError:
    tables_json = ""
try:
    table_names
except NameError:
    table_names = ""
try:
    fact_table
except NameError:
    fact_table = ""
try:
    join_tables
except NameError:
    join_tables = ""
try:
    max_tables
except NameError:
    max_tables = 8

_out = main(
    tables=tables,
    tables_json=tables_json,
    table_names=table_names,
    fact_table=fact_table or "",
    join_tables=join_tables,
    max_tables=max_tables,
)
context = str(_out.get("context") or "")
table_count = str(_out.get("table_count") or "0")
found_tables = str(_out.get("found_tables") or "")
missing_tables = str(_out.get("missing_tables") or "")
'''


def main() -> None:
    if not MD_FILE.is_file():
        raise SystemExit(f"未找到：{MD_FILE}")

    md_text = MD_FILE.read_text(encoding="utf-8")
    index = parse_schema_markdown(md_text)
    JSON_FILE.write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"已生成 {JSON_FILE.name}（{len(index)} 张表，{JSON_FILE.stat().st_size} 字节）")

    core = (ROOT / "erp_schema_by_tables.py").read_text(encoding="utf-8")
    lines = core.splitlines()
    if lines and lines[0].startswith("#!"):
        lines = lines[1:]
    core = "\n".join(lines)

    embedded = f'_EMBEDDED_SCHEMAS = json.loads({json.dumps(json.dumps(index, ensure_ascii=False))})\n'
    marker = "_EMBEDDED_SCHEMAS: Optional[Dict[str, str]] = None"
    if marker not in core:
        raise SystemExit(f"未在 erp_schema_by_tables.py 中找到 {marker!r}")

    core = core.replace(marker, embedded.rstrip(), 1)

    OUT.write_text(HEADER + core + "\n\n" + DIFY_ENTRY, encoding="utf-8")
    print(f"已生成 {OUT.name}（{OUT.stat().st_size} 字节）")
    print("请复制 dify_erp_schema_by_tables.py 全文到 Dify「代码」节点。")


if __name__ == "__main__":
    main()
