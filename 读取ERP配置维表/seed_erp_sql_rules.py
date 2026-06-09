#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化 erp_sql_rules 表，并导入基础规则（整份 md 一条 base 记录）。

  python3 seed_erp_sql_rules.py
"""

from __future__ import annotations

from erp_sql_rules_db import (
    DB_CONFIG,
    fetch_merged_rules,
    load_base_rules_from_md,
    upsert_base_rule,
)


def main() -> None:
    text = load_base_rules_from_md()
    print(
        f"目标库: {DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']} "
        f"表=erp_sql_rules"
    )
    log: list[str] = []
    upsert_base_rule(text, log)
    for line in log:
        print(line)
    merged, count = fetch_merged_rules()
    print(f"验证: 共 {count} 条规则，合并长度 {len(merged)} 字符")


if __name__ == "__main__":
    main()
