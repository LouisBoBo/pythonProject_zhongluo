#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MES Dify SQL 列校验（复用 ERP 侧 sql_db_validate_core，环境变量前缀 MES）。"""

from __future__ import annotations

import sys
from pathlib import Path

# 本地开发：引用 sibling 目录中的共用核心
_CORE_DIR = Path(__file__).resolve().parent.parent / "读取ERP配置维表"
if str(_CORE_DIR) not in sys.path:
    sys.path.insert(0, str(_CORE_DIR))

from sql_db_validate_core import (
    collect_table_specs,
    collect_tables,
    fetch_table_columns_mssql,
    make_main,
    parse_table_aliases,
    resolve_db_config,
    validate_sql_against_db,
    validate_sql_columns,
)

ENV_PREFIX = "MES"
main = make_main(ENV_PREFIX)
