#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一键打包全部 ERP Dify 代码节点（改完配置后只跑这一条即可）。

  cd 读取ERP配置维表
  python3 build_all.py

依次执行：选表清单 → 表结构 → 维表映射，并做 Python 语法检查。
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

STEPS: tuple[tuple[str, str], ...] = (
    ("选表清单", "build_erp_catalog_bundle.py"),
    ("表结构", "build_erp_schema_bundle.py"),
    ("维表映射", "build_dify_bundle.py"),
    ("约束规则节点", "build_erp_sql_rules_db_bundle.py"),
    ("SQL列校验节点", "build_erp_sql_db_validate_bundle.py"),
)

DIFY_OUT = (
    "dify_erp_table_catalog.py",
    "dify_erp_schema_by_tables.py",
    "dify_erp_dimension_node.py",
    "dify_erp_sql_fix_node.py",
    "dify_erp_sql_rules_db_read.py",
    "dify_erp_sql_rules_db_write.py",
    "dify_erp_sql_db_validate_node.py",
)


def _run_step(label: str, script: str) -> None:
    path = ROOT / script
    if not path.is_file():
        raise SystemExit(f"未找到脚本：{path}")
    print(f"\n{'=' * 60}\n▶ {label}  ({script})\n{'=' * 60}", flush=True)
    rc = subprocess.run([sys.executable, str(path)], cwd=str(ROOT)).returncode
    if rc != 0:
        raise SystemExit(f"失败：{script}（exit {rc}）")


def _verify_syntax() -> None:
    print(f"\n{'=' * 60}\n▶ 语法检查\n{'=' * 60}")
    for name in DIFY_OUT:
        path = ROOT / name
        if not path.is_file():
            raise SystemExit(f"未生成：{path}")
        rc = subprocess.run(
            [sys.executable, "-m", "py_compile", str(path)],
            cwd=str(ROOT),
        ).returncode
        if rc != 0:
            raise SystemExit(f"语法错误：{name}")
        print(f"  ✓ {name}")


def main() -> None:
    for label, script in STEPS:
        _run_step(label, script)
    _verify_syntax()
    print(
        "\n"
        "全部完成。请将以下文件全文复制到 Dify 对应代码节点并【发布】workflow：\n"
        "  1. dify_erp_table_catalog.py      → 输出表名清单\n"
        "  2. dify_erp_schema_by_tables.py   → 表结构\n"
        "  3. dify_erp_dimension_node.py     → 维表映射\n"
        "  4. dify_erp_sql_fix_node.py       → SQL 修复（LLM 与 text2data 之间，必加）\n"
        "  5. dify_erp_sql_rules_db_read.py  → 读取 SQL 约束规则（表 erp_sql_rules）\n"
        "  6. dify_erp_sql_rules_db_write.py → 写入 SQL 学习规则\n"
        "  7. dify_erp_sql_db_validate_node.py → SQL 列校验（fix 与 text2data 之间，可选）\n"
        "\n"
        "另 1 个代码节点很少改，不用每次 build：\n"
        "  8. dify_current_datetime.py       → 当前时间\n"
        "\n"
        "base 规则入库（改 中络项目ERP SQL约束规则提示词.md 后）：python3 seed_erp_sql_rules.py\n"
        "\n"
        "提示词（.md）改完直接粘 LLM SYSTEM，无需本脚本。\n"
        "详见 readme.md\n",
        flush=True,
    )


if __name__ == "__main__":
    main()
