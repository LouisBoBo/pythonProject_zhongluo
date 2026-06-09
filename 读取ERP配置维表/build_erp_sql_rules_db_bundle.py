#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
打包 Dify ERP 约束规则数据库节点（独立表 erp_sql_rules，与 mes_sql_rules 隔离）：

  python3 build_erp_sql_rules_db_bundle.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORE = ROOT / "erp_sql_rules_db.py"
READ_OUT = ROOT / "dify_erp_sql_rules_db_read.py"
WRITE_OUT = ROOT / "dify_erp_sql_rules_db_write.py"

READ_HEADER = '''# -*- coding: utf-8 -*-
# 【Dify 代码节点 · 读取 ERP SQL 约束规则 · PostgreSQL · 表 erp_sql_rules】
# 维护：改 中络项目ERP SQL约束规则提示词.md 后本地执行 seed_erp_sql_rules.py 更新 base 规则
#
# 入参：无
# 出参（string）：rule_list — 仅 learned 增量规则 → SQL LLM【规则约束】（base 约束在系统提示词，勿重复注入）

'''

WRITE_HEADER = '''# -*- coding: utf-8 -*-
# 【Dify 代码节点 · 写入 ERP SQL 学习规则 · PostgreSQL · 表 erp_sql_rules】
#
# 入参：
#   rule_text — tiqu_error_rule 节点输出的 rule_text
#   error_msg — 可选，原始报错信息（写入 source_snippet）
# 出参（均为 string）：
#   result, message, inserted_count, skipped_count

'''

READ_ENTRY = '''
def main(**kwargs):
    return read_rules_main(**kwargs)

# --- Dify 入口 ---
_out = main()
rule_list = str(_out.get("rule_list") or "")
'''

WRITE_ENTRY = '''
def main(rule_text="", error_msg="", **kwargs):
    return write_rules_main(rule_text=rule_text, error_msg=error_msg, **kwargs)

# --- Dify 入口 ---
try:
    rule_text
except NameError:
    rule_text = ""
try:
    error_msg
except NameError:
    error_msg = ""

_out = main(rule_text=rule_text, error_msg=error_msg)
result = str(_out.get("result") or "")
message = str(_out.get("message") or "")
inserted_count = str(_out.get("inserted_count") or "0")
skipped_count = str(_out.get("skipped_count") or "0")
'''


def _load_core() -> str:
    lines = CORE.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].startswith("#!"):
        lines = lines[1:]
    text = "\n".join(lines)
    idx = text.rfind('if __name__ == "__main__":')
    if idx != -1:
        text = text[:idx].rstrip() + "\n"
    return text


def main() -> None:
    core = _load_core()
    READ_OUT.write_text(READ_HEADER + core + "\n" + READ_ENTRY, encoding="utf-8")
    WRITE_OUT.write_text(WRITE_HEADER + core + "\n" + WRITE_ENTRY, encoding="utf-8")
    print(f"已生成 {READ_OUT.name}（{READ_OUT.stat().st_size} 字节）")
    print(f"已生成 {WRITE_OUT.name}（{WRITE_OUT.stat().st_size} 字节）")


if __name__ == "__main__":
    main()
