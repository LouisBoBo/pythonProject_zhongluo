#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理误伤 ERP learned 规则，并补全高频 P_MO.status 约束。

  python3 cleanup_erp_sql_learned_rules.py
"""

from __future__ import annotations

from erp_sql_rules_db import (
    DB_CONFIG,
    deactivate_learned_rules,
    fetch_learned_rules,
    fetch_merged_rules,
    insert_learned_rules,
)

_PMO_STATUS_RULE = (
    "【硬约束·245】表 P_MO 的 status 为 string 类型，禁止 CASE pmo.status WHEN 1 THEN N'外协' 等数字分支；"
    "须 CASE UPPER(RTRIM(pmo.status)) WHEN 'ORDER' THEN N'已下单' … ELSE pmo.status END。"
)


def main() -> None:
    print(
        f"目标库: {DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']} "
        f"表=erp_sql_rules"
    )
    log: list[str] = []
    deactivated = deactivate_learned_rules(
        match_regexes=[r"TBL_", r"^【硬约束·207】字段\s+(CID|CWC_ID)"],
        log=log,
    )
    for line in log:
        print(line)

    log2: list[str] = []
    inserted, skipped = insert_learned_rules(
        _PMO_STATUS_RULE,
        source_snippet="cleanup_erp_sql_learned_rules.py",
        log=log2,
    )
    for line in log2:
        print(line)
    print(f"补全 P_MO.status 规则: 新增 {inserted} 条，跳过 {skipped} 条")

    learned, learned_count = fetch_learned_rules()
    merged, total_count = fetch_merged_rules()
    print(
        f"验证: active learned {learned_count} 条（{len(learned)} 字符），"
        f"库内 active 总计 {total_count} 条（含 base）"
    )


if __name__ == "__main__":
    main()
