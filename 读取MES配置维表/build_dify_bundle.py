#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将维表映射配置嵌入 mes_dimension_rules.py，生成 Dify 代码节点单文件：

  python3 build_dify_bundle.py

维护（推荐，不用写 JSON）：
  1. 只改 mes_dimension_joins.map（表格式文本，见文件内注释）
  2. 运行 python3 build_dify_bundle.py
  3. 复制 dify_mes_dimension_node.py 到 Dify 代码节点

.map 不存在时回退读 mes_dimension_joins.json。
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from parse_dimension_map import load_dimension_config, write_json_from_map

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dify_mes_dimension_node.py"
RULES = ROOT / "mes_dimension_rules.py"
MULTIJOIN = ROOT / "mes_sql_multijoin.py"
MAP_FILE = ROOT / "mes_dimension_joins.map"
JOINS = ROOT / "mes_dimension_joins.json"


def _strip_shebang(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("#!"):
        lines = lines[1:]
    return "\n".join(lines).strip() + "\n"


def _strip_future_import(text: str) -> str:
    """拼接多模块时，__future__ 只能出现在文件最开头一次。"""
    return re.sub(
        r"^from __future__ import annotations\s*\n+",
        "",
        text,
        count=1,
        flags=re.MULTILINE,
    )


def _strip_cli_block(text: str) -> str:
    """Dify 执行时 __name__ 可能为 __main__，须去掉 argparse CLI，避免误解析 sys.argv。"""
    marker = 'if __name__ == "__main__":'
    idx = text.rfind(marker)
    if idx != -1:
        text = text[:idx].rstrip() + "\n"
    return text


HEADER = '''# -*- coding: utf-8 -*-
from __future__ import annotations
# 【Dify 代码节点专用 · 由 build_dify_bundle.py 自动生成，请勿手改】
# 维护：改 mes_dimension_joins.map → python3 build_dify_bundle.py → 本文件整段复制到 Dify
#
# 入参：user_question（必填，用户问题）
# 出参：dimension_rules, fact_table, join_tables

'''


def main() -> None:
    config = load_dimension_config(MAP_FILE, JOINS)
    if MAP_FILE.is_file():
        write_json_from_map(MAP_FILE, JOINS)
        print(f"已从 {MAP_FILE.name} 同步 → {JOINS.name}")
    rules_text = RULES.read_text(encoding="utf-8")
    # 去掉本地 shebang，避免 Dify 环境警告
    lines = rules_text.splitlines()
    if lines and lines[0].startswith("#!"):
        lines = lines[1:]
    rules_text = "\n".join(lines)

    embedded_line = f"_EMBEDDED_CONFIG = json.loads({json.dumps(json.dumps(config, ensure_ascii=False))})\n"

    marker = "_EMBEDDED_CONFIG: Optional[Dict[str, Any]] = None"
    if marker not in rules_text:
        raise SystemExit(f"未在 {RULES.name} 中找到 {marker!r}，请先更新 mes_dimension_rules.py")

    rules_text = rules_text.replace(
        marker,
        embedded_line.rstrip(),
        1,
    )
    rules_text = _strip_cli_block(rules_text)
    rules_text = _strip_future_import(rules_text)

    mj_text = ""
    if MULTIJOIN.is_file():
        mj_text = _strip_cli_block(_strip_shebang(MULTIJOIN.read_text(encoding="utf-8")))
        mj_text = _strip_future_import(mj_text)
        # 去掉模块内重复的 coding 声明
        mj_text = re.sub(r"^# -\*- coding:.*\n", "", mj_text, count=1)
        mj_text = mj_text.strip() + "\n\n"

    OUT.write_text(
        HEADER + mj_text + rules_text + "\n\n\n# --- Dify 入口 ---\n" + DIFY_ENTRY,
        encoding="utf-8",
    )
    print(f"已生成 {OUT}（{OUT.stat().st_size} 字节）")
    print("请打开该文件，全选复制到 Dify「代码」节点。")


DIFY_ENTRY = '''
def _run_dify(user_question: str = "", query_sql: str = ""):
    return main_with_sql(user_question=user_question or "", query_sql=query_sql or "")


# Dify 代码节点入参：user_question（必填）；query_sql（可选，LLM 生成 SQL 传入则自动 CASE 译码修正）
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

if __name__ == "__main__":
    main()
