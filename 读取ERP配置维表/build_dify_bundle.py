#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将维表映射配置嵌入 erp_dimension_rules.py，并生成 Dify 代码节点单文件：

  python3 build_dify_bundle.py

产出：
  - dify_erp_dimension_node.py  维表规则（SQL 生成 LLM 前）
  - dify_erp_sql_fix_node.py    SQL 修复（LLM 后、text2data 前，必加）
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from parse_dimension_map import load_dimension_config, write_json_from_map

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dify_erp_dimension_node.py"
SQL_FIX_OUT = ROOT / "dify_erp_sql_fix_node.py"
RULES = ROOT / "erp_dimension_rules.py"
FIX_CORE = ROOT / "erp_sql_fix_core.py"
MAP_FILE = ROOT / "erp_dimension_joins.map"
JOINS = ROOT / "erp_dimension_joins.json"


def _strip_cli_block(text: str) -> str:
    marker = 'if __name__ == "__main__":'
    idx = text.rfind(marker)
    if idx != -1:
        text = text[:idx].rstrip() + "\n"
    return text


def _strip_main_with_sql(text: str) -> str:
    marker = "def main_with_sql("
    idx = text.find(marker)
    if idx == -1:
        return text
    return text[:idx].rstrip() + "\n"


def _strip_internal_main(text: str) -> str:
    marker = "def main(\n    fact_table:"
    idx = text.find(marker)
    if idx == -1:
        return text
    return text[:idx].rstrip() + "\n"


def _strip_module_header(text: str) -> str:
    text = re.sub(r"^#!/.*\n", "", text)
    text = re.sub(r"^# -\*- coding:.*\n", "", text)
    text = re.sub(r'^"""[\s\S]*?"""\n+', "", text, count=1)
    text = re.sub(r"^from __future__ import annotations\n+", "", text)
    return text.lstrip()


HEADER = '''# -*- coding: utf-8 -*-
# 【Dify 代码节点 · 维表规则 · build_dify_bundle.py 自动生成】
# 入参：user_question
# 出参：query_rules, fact_table, join_tables
# ⚠ 本节点只做「选表 + 生成 dimension_rules」，不修复 SQL、不执行查询
# ⚠ SQL 修复必须用独立节点 dify_erp_sql_fix_node.py（LLM 之后、text2data 之前）

from __future__ import annotations

'''

SQL_FIX_HEADER = '''# -*- coding: utf-8 -*-
# 【Dify 代码节点 · SQL 修复 · build_dify_bundle.py 自动生成】
# 位置：SQL 生成 LLM 之后、rookie_text2data 之前（重试循环内也必须经过本节点）
# 入参：query_sql（或 sql）← LLM 输出
# 出参：fixed_sql / sql / query_sql（三者同为修复后 SQL，便于不同接线习惯）
#       was_changed（true/false）、fix_error（空=成功）
# ⚠ Dify 要求入口函数必须命名为 main，并 return dict

from __future__ import annotations

'''

DIFY_ENTRY = '''

def main(user_question: str = "") -> dict:
    cfg = load_config()
    table = infer_fact_table(user_question or "", "", cfg)
    rules = build_query_rules(table, config=cfg)
    join_list = ",".join(list_join_tables(table, cfg))
    return {
        "query_rules": rules,
        "fact_table": table,
        "join_tables": join_list,
    }
'''

SQL_FIX_ENTRY = '''

def _coerce_sql(sql: str = "", query_sql: str = "", **kwargs) -> str:
    return coerce_erp_sql_input(sql=sql, query_sql=query_sql, **kwargs)


def main(**kwargs) -> dict:
    out = fix_erp_sql_with_meta(**kwargs)
    return out
'''


def _write_sql_fix_node() -> None:
    core = _strip_module_header(FIX_CORE.read_text(encoding="utf-8"))
    SQL_FIX_OUT.write_text(
        SQL_FIX_HEADER + core + SQL_FIX_ENTRY,
        encoding="utf-8",
    )
    print(f"已生成 {SQL_FIX_OUT}（{SQL_FIX_OUT.stat().st_size} 字节）")


def main() -> None:
    config = load_dimension_config(MAP_FILE, JOINS)
    if MAP_FILE.is_file():
        write_json_from_map(MAP_FILE, JOINS)
        print(f"已从 {MAP_FILE.name} 同步 → {JOINS.name}")

    rules_text = RULES.read_text(encoding="utf-8")
    rules_text = _strip_module_header(rules_text)

    embedded_line = f"_EMBEDDED_CONFIG = json.loads({json.dumps(json.dumps(config, ensure_ascii=False))})\n"
    marker = "_EMBEDDED_CONFIG: Optional[Dict[str, Any]] = None"
    if marker not in rules_text:
        raise SystemExit(f"未在 {RULES.name} 中找到 {marker!r}")

    rules_text = _strip_cli_block(rules_text)
    rules_text = _strip_main_with_sql(rules_text)
    rules_text = _strip_internal_main(rules_text)

    OUT.write_text(
        HEADER
        + rules_text
        + "\n\n"
        + embedded_line
        + "\n\n# --- Dify 入口 ---\n"
        + DIFY_ENTRY,
        encoding="utf-8",
    )
    print(f"已生成 {OUT}（{OUT.stat().st_size} 字节）")

    _write_sql_fix_node()
    print("请复制 dify_erp_sql_fix_node.py 到 LLM 与 text2data 之间的代码节点。")


if __name__ == "__main__":
    main()
