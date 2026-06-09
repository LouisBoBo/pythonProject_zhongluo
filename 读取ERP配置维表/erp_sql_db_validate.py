#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ERP Dify SQL 列校验（复用 sql_db_validate_core，环境变量前缀 ERP）。"""

from __future__ import annotations

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

ENV_PREFIX = "ERP"
main = make_main(ENV_PREFIX)
