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

from erp_schema_columns import load_column_index_from_file
from parse_dimension_map import load_dimension_config, write_json_from_map

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dify_erp_dimension_node.py"
SQL_FIX_OUT = ROOT / "dify_erp_sql_fix_node.py"
RULES = ROOT / "erp_dimension_rules.py"
SCHEMA_COLS = ROOT / "erp_schema_columns.py"
MULTIJOIN = ROOT / "erp_sql_multijoin.py"
FIX_CORE = ROOT / "erp_sql_fix_core.py"
MAP_FILE = ROOT / "erp_dimension_joins.map"
JOINS = ROOT / "erp_dimension_joins.json"


def _strip_shebang(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("#!"):
        lines = lines[1:]
    return "\n".join(lines).strip() + "\n"


def _strip_future_import(text: str) -> str:
    return re.sub(
        r"^from __future__ import annotations\s*\n+",
        "",
        text,
        count=1,
        flags=re.MULTILINE,
    )


def _strip_cli_block(text: str) -> str:
    marker = 'if __name__ == "__main__":'
    idx = text.rfind(marker)
    if idx != -1:
        text = text[:idx].rstrip() + "\n"
    return text


def _strip_module_header(text: str) -> str:
    text = re.sub(r"^#!/.*\n", "", text)
    text = re.sub(r"^# -\*- coding:.*\n", "", text)
    text = re.sub(r'^"""[\s\S]*?"""\n+', "", text, count=1)
    text = re.sub(r"^from __future__ import annotations\n+", "", text)
    return text.lstrip()


def _strip_inlined_imports(text: str) -> str:
    """Dify 单文件已内联合并，不能再 import 同目录 module。"""
    for pat in (
        r"^from erp_schema_columns import .+\n",
        r"^from erp_sql_multijoin import .+\n",
        r"^from erp_sql_fix_core import .+\n",
    ):
        text = re.sub(pat, "", text, flags=re.MULTILINE)
    return text


def _assert_no_local_imports(path: Path) -> None:
    bad = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if re.match(r"^from erp_\w+ import ", line):
            bad.append(f"  L{i}: {line}")
    if bad:
        raise SystemExit(f"{path.name} 仍含本地 module import（Dify 会报错）：\n" + "\n".join(bad))


def _embed_schema_columns(text: str, column_index: dict) -> str:
    marker = "_EMBEDDED_SCHEMA_COLUMNS: Dict[str, List[List[str]]] | None = None"
    if marker not in text:
        raise SystemExit(f"未在 erp_schema_columns.py 中找到 {marker!r}")
    embedded = (
        f"_EMBEDDED_SCHEMA_COLUMNS = json.loads({json.dumps(json.dumps(column_index, ensure_ascii=False))})\n"
    )
    return text.replace(marker, embedded.rstrip(), 1)


HEADER = '''# -*- coding: utf-8 -*-
from __future__ import annotations
# 【Dify 代码节点专用 · 由 build_dify_bundle.py 自动生成，请勿手改】
# 维护：改 erp_dimension_joins.map → python3 build_dify_bundle.py → 本文件整段复制到 Dify
#
# 入参：user_question（必填，用户问题）
# 出参：dimension_rules, fact_table, join_tables

import json

'''

SQL_FIX_HEADER = '''# -*- coding: utf-8 -*-
# 【Dify 代码节点 · SQL 修复 · build_dify_bundle.py 自动生成】
# 位置：SQL 生成 LLM 之后、rookie_text2data 之前（重试循环内也必须经过本节点）
# 入参：query_sql（或 sql）← LLM 输出；user_question（可选）
# 出参：fixed_sql / sql / query_sql（三者同为修复后 SQL，便于不同接线习惯）
#       was_changed（true/false）、fix_error（空=成功）
# 含 erp_dimension_rules（嵌入 .map 配置）→ fix 末尾自动 CASE 枚举译码兜底
# ⚠ Dify 沙箱要求入口函数必须命名为 main（见文件末尾 def main）

from __future__ import annotations

import json

'''

DIFY_ENTRY = '''
def _run_dify(user_question: str = "", query_sql: str = ""):
    return main_with_sql(user_question=user_question or "", query_sql=query_sql or "")


try:
    user_question
except NameError:
    user_question = ""
try:
    query_sql
except NameError:
    query_sql = ""

_out = _run_dify(user_question=user_question, query_sql=query_sql)
dimension_rules = _out["query_rules"]
query_rules = dimension_rules
fact_table = _out["fact_table"]
_join_list = _out["join_tables"]
join_tables = _join_list if isinstance(_join_list, str) else ",".join(_join_list)
query_sql_fixed = _out.get("query_sql_fixed") or ""
'''

SQL_FIX_ENTRY = '''

def main(
    sql: str = "",
    query_sql: str = "",
    user_question: str = "",
    **kwargs,
) -> dict:
    """Dify 入口函数（必须命名为 main）。"""
    return fix_erp_sql_with_meta(
        sql=sql,
        query_sql=query_sql,
        user_question=user_question,
        **kwargs,
    )


# --- Dify 入口（入参 sql/query_sql ← LLM；user_question ← {{#sys.query#}}）---
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

_out = main(
    sql=sql or "",
    query_sql=query_sql or "",
    user_question=user_question or "",
)
fixed_sql = str(_out.get("fixed_sql") or "")
sql = str(_out.get("sql") or fixed_sql)
query_sql = str(_out.get("query_sql") or fixed_sql)
was_changed = str(_out.get("was_changed") or "false")
fix_error = str(_out.get("fix_error") or "")
'''


def _schema_columns_bundle(column_index: dict) -> str:
    text = _strip_module_header(SCHEMA_COLS.read_text(encoding="utf-8"))
    text = _embed_schema_columns(text, column_index)
    return _strip_future_import(text).strip() + "\n\n"


def _rules_bundle(config: dict) -> str:
    rules_text = RULES.read_text(encoding="utf-8")
    lines = rules_text.splitlines()
    if lines and lines[0].startswith("#!"):
        lines = lines[1:]
    rules_text = "\n".join(lines)
    embedded_line = (
        f"_EMBEDDED_CONFIG = json.loads({json.dumps(json.dumps(config, ensure_ascii=False))})\n"
    )
    marker = "_EMBEDDED_CONFIG: Optional[Dict[str, Any]] = None"
    if marker not in rules_text:
        raise SystemExit(f"未在 {RULES.name} 中找到 {marker!r}")
    rules_text = rules_text.replace(marker, embedded_line.rstrip(), 1)
    rules_text = _strip_cli_block(rules_text)
    rules_text = _strip_future_import(rules_text)
    rules_text = _strip_inlined_imports(rules_text)
    return rules_text.strip() + "\n\n"


def _write_sql_fix_node(column_index: dict, config: dict) -> None:
    core = _strip_inlined_imports(_strip_module_header(FIX_CORE.read_text(encoding="utf-8")))
    mj_text = ""
    if MULTIJOIN.is_file():
        mj_text = _strip_cli_block(_strip_shebang(MULTIJOIN.read_text(encoding="utf-8")))
        mj_text = _strip_future_import(mj_text)
        mj_text = re.sub(r"^# -\*- coding:.*\n", "", mj_text, count=1)
        mj_text = mj_text.strip() + "\n\n"
    SQL_FIX_OUT.write_text(
        SQL_FIX_HEADER
        + _schema_columns_bundle(column_index)
        + _rules_bundle(config)
        + mj_text
        + core
        + SQL_FIX_ENTRY,
        encoding="utf-8",
    )
    print(f"已生成 {SQL_FIX_OUT}（{SQL_FIX_OUT.stat().st_size} 字节）")


def main() -> None:
    config = load_dimension_config(MAP_FILE, JOINS)
    if MAP_FILE.is_file():
        write_json_from_map(MAP_FILE, JOINS)
        print(f"已从 {MAP_FILE.name} 同步 → {JOINS.name}")

    column_index = load_column_index_from_file()
    if not column_index:
        raise SystemExit("erp_table_schemas.json 缺失或为空，无法嵌入列索引")
    print(f"已加载 schema 列索引：{len(column_index)} 张表")

    rules_text = _rules_bundle(config)

    mj_text = ""
    if MULTIJOIN.is_file():
        mj_text = _strip_cli_block(_strip_shebang(MULTIJOIN.read_text(encoding="utf-8")))
        mj_text = _strip_future_import(mj_text)
        mj_text = re.sub(r"^# -\*- coding:.*\n", "", mj_text, count=1)
        mj_text = mj_text.strip() + "\n\n"

    OUT.write_text(
        HEADER
        + _schema_columns_bundle(column_index)
        + mj_text
        + rules_text
        + "\n\n\n# --- Dify 入口 ---\n"
        + DIFY_ENTRY,
        encoding="utf-8",
    )
    print(f"已生成 {OUT}（{OUT.stat().st_size} 字节）")
    _assert_no_local_imports(OUT)

    _write_sql_fix_node(column_index, config)
    _assert_no_local_imports(SQL_FIX_OUT)
    print("请复制 dify_erp_dimension_node.py 到维表节点；dify_erp_sql_fix_node.py 到 LLM 与 text2data 之间。")


if __name__ == "__main__":
    main()
