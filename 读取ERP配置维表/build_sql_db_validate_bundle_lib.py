#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ERP / MES 共用：打包 Dify SQL 列校验单文件节点。"""

from __future__ import annotations

import re
from pathlib import Path

ERP_ROOT = Path(__file__).resolve().parent
CORE = ERP_ROOT / "sql_db_validate_core.py"

DIFY_ENTRY = '''

# --- Dify 入口 ---
try:
    fixed_sql
except NameError:
    fixed_sql = ""
try:
    query_sql
except NameError:
    query_sql = ""
try:
    sql
except NameError:
    sql = ""
try:
    server
except NameError:
    server = ""
try:
    port
except NameError:
    port = ""
try:
    username
except NameError:
    username = ""
try:
    password
except NameError:
    password = ""
try:
    database
except NameError:
    database = ""
try:
    db
except NameError:
    db = ""

_out = main(
    sql=sql or "",
    query_sql=query_sql or "",
    fixed_sql=fixed_sql or "",
    server=server or "",
    port=port or "",
    username=username or "",
    password=password or "",
    database=database or db or "",
    db=database or db or "",
)
fixed_sql = str(_out.get("fixed_sql") or "")
was_changed = str(_out.get("was_changed") or "false")
removed_columns = str(_out.get("removed_columns") or "[]")
tables_checked = str(_out.get("tables_checked") or "[]")
table_column_counts = str(_out.get("table_column_counts") or "{}")
validate_error = str(_out.get("validate_error") or "")
'''


def _strip_module_header(text: str) -> str:
    text = re.sub(r"^#!/.*\n", "", text)
    text = re.sub(r"^# -\*- coding:.*\n", "", text)
    text = re.sub(r'^"""[\s\S]*?"""\n+', "", text, count=1)
    text = re.sub(r"^from __future__ import annotations\n+", "", text)
    return text.lstrip()


def build_bundle(
    *,
    env_prefix: str,
    out_path: Path,
    header: str,
    after_fix_hint: str,
) -> None:
    if not CORE.is_file():
        raise SystemExit(f"未找到共用核心：{CORE}")
    body = _strip_module_header(CORE.read_text(encoding="utf-8"))
    tail = f'\nmain = make_main("{env_prefix.upper()}")\n'
    out_path.write_text(header + body + tail + DIFY_ENTRY, encoding="utf-8")
    print(f"已生成 {out_path}（{out_path.stat().st_size} 字节）")
    print(f"请复制到 Dify：放在 {after_fix_hint} 之后、text2data 之前。")
