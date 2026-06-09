#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 fix_mes_sql_nolock + mes_dimension_rules（含映射配置）+ mes_sql_multijoin
打包为 Dify 单文件 SQL 修复节点：

  python3 build_mes_sql_fix_bundle.py

维护：改 mes_dimension_joins.map → build_dify_bundle.py 或本脚本 →
复制 dify_mes_sql_fix_node.py 到 Dify fix 节点（替换原 fix_mes_sql_nolock.py 单文件）。
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from build_dify_bundle import (
    MAP_FILE,
    JOINS,
    _strip_cli_block,
    _strip_future_import,
    _strip_shebang,
)
from parse_dimension_map import load_dimension_config, write_json_from_map

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dify_mes_sql_fix_node.py"
RULES = ROOT / "mes_dimension_rules.py"
FIX = ROOT / "fix_mes_sql_nolock.py"
MULTIJOIN = ROOT / "mes_sql_multijoin.py"

HEADER = """# -*- coding: utf-8 -*-
from __future__ import annotations
# 【Dify 代码节点专用 · 由 build_mes_sql_fix_bundle.py 自动生成，请勿手改】
# 维护：改 mes_dimension_joins.map → python3 build_mes_sql_fix_bundle.py → 本文件整段复制到 Dify
#
# 位置：SQL 生成 LLM 之后、db_validate / text2data 之前
# 入参：sql 或 query_sql；user_question（可选，多表 TOP 修正用）
# 出参：fixed_sql, sql

"""

DIFY_ENTRY = """
# --- Dify 入口 ---
try:
    sql
except NameError:
    sql = ""
try:
    query_sql
except NameError:
    query_sql = ""
try:
    user_question
except NameError:
    user_question = ""

_out = main(sql=sql or query_sql, user_question=user_question)
fixed_sql = _out["fixed_sql"]
sql = fixed_sql
"""


def _embed_config(rules_text: str, config: dict) -> str:
    embedded_line = (
        f"_EMBEDDED_CONFIG = json.loads({json.dumps(json.dumps(config, ensure_ascii=False))})\n"
    )
    marker = "_EMBEDDED_CONFIG: Optional[Dict[str, Any]] = None"
    if marker not in rules_text:
        raise SystemExit(f"未在 {RULES.name} 中找到 {marker!r}")
    return rules_text.replace(marker, embedded_line.rstrip(), 1)


def main() -> None:
    config = load_dimension_config(MAP_FILE, JOINS)
    if MAP_FILE.is_file():
        write_json_from_map(MAP_FILE, JOINS)
        print(f"已从 {MAP_FILE.name} 同步 → {JOINS.name}")

    rules_text = RULES.read_text(encoding="utf-8")
    lines = rules_text.splitlines()
    if lines and lines[0].startswith("#!"):
        lines = lines[1:]
    rules_text = "\n".join(lines)
    rules_text = _embed_config(rules_text, config)
    rules_text = _strip_cli_block(rules_text)
    rules_text = _strip_future_import(rules_text)

    mj_text = ""
    if MULTIJOIN.is_file():
        mj_text = _strip_cli_block(_strip_shebang(MULTIJOIN.read_text(encoding="utf-8")))
        mj_text = _strip_future_import(mj_text)
        mj_text = re.sub(r"^# -\*- coding:.*\n", "", mj_text, count=1)
        mj_text = mj_text.strip() + "\n\n"

    fix_text = FIX.read_text(encoding="utf-8")
    fix_text = _strip_shebang(fix_text)
    fix_text = _strip_future_import(fix_text)
    fix_text = re.sub(r"^# -\*- coding:.*\n", "", fix_text, count=1)
    # 去掉 fix 文件末尾重复的 Dify 入口（由本脚本统一追加）
    marker = "# --- Dify 入口"
    idx = fix_text.find(marker)
    if idx != -1:
        fix_text = fix_text[:idx].rstrip() + "\n"

    OUT.write_text(
        HEADER + rules_text + "\n\n" + mj_text + fix_text + DIFY_ENTRY,
        encoding="utf-8",
    )
    print(f"已生成 {OUT}（{OUT.stat().st_size} 字节）")
    print("请打开该文件，全选复制到 Dify「SQL 修复」代码节点并【发布】workflow。")


if __name__ == "__main__":
    main()
