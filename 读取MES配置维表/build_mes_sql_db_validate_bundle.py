#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 Dify SQL 列校验节点：dify_mes_sql_db_validate_node.py"""

from __future__ import annotations

import sys
from pathlib import Path

ERP_ROOT = Path(__file__).resolve().parent.parent / "读取ERP配置维表"
if str(ERP_ROOT) not in sys.path:
    sys.path.insert(0, str(ERP_ROOT))

from build_sql_db_validate_bundle_lib import build_bundle

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dify_mes_sql_db_validate_node.py"

HEADER = '''# -*- coding: utf-8 -*-
# 【Dify · MES SQL 列校验 · build_mes_sql_db_validate_bundle.py 自动生成】
# 位置：fix_mes_sql_nolock 之后、rookie_text2data 之前
# 依赖：pip install sqlalchemy pymssql
# 环境变量（可选）：MES_DB_SERVER / MES_DB_DATABASE / MES_DB_USER / MES_DB_PASSWORD …
#
# 入参（与 text2data 同源即可）：
#   fixed_sql ← fix 节点
#   server, port, username, password, database（或 db / db_name）
#
# 出参：
#   fixed_sql
#   was_changed, removed_columns(JSON), tables_checked(JSON), table_column_counts(JSON), validate_error

from __future__ import annotations

'''


def main() -> None:
    build_bundle(
        env_prefix="MES",
        out_path=OUT,
        header=HEADER,
        after_fix_hint="fix_mes_sql_nolock",
    )


if __name__ == "__main__":
    main()
