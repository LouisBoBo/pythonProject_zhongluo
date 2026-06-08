#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一键打包全部 Dify 代码节点（改完配置后只跑这一条即可）。

  cd 读取MES配置维表
  python3 build_all.py

依次执行：选表清单 → 表结构 → 维表映射，并做 Python 语法检查。
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

STEPS: tuple[tuple[str, str], ...] = (
    ("选表清单", "build_mes_catalog_bundle.py"),
    ("表结构", "build_mes_schema_bundle.py"),
    ("维表映射", "build_dify_bundle.py"),
)

DIFY_OUT = (
    "dify_mes_table_catalog.py", 
    "dify_mes_schema_by_tables.py", 
    "dify_mes_dimension_node.py",
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
        "  1. dify_mes_table_catalog.py      → 输出表名清单\n"
        "  2. dify_mes_schema_by_tables.py   → 表结构\n"
        "  3. dify_mes_dimension_node.py     → 维表映射\n"
        "\n"
        "提示词（.md）改完直接粘 LLM SYSTEM，无需本脚本。\n"
        "详见 readme.md\n",
        flush=True,
    )


if __name__ == "__main__":
    main()
