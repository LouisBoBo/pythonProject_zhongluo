#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理误伤 learned 规则，并补全 TBL_EAM_REPAIR.CODE 现场约束。

  python3 cleanup_mes_sql_learned_rules.py
"""

from __future__ import annotations

from mes_sql_rules_db import (
    DB_CONFIG,
    deactivate_learned_rules,
    fetch_learned_rules,
    fetch_merged_rules,
    insert_learned_rules,
)

_EAM_REPAIR_CODE_RULE = (
    "【硬约束·207】表 TBL_EAM_REPAIR 严禁使用 CODE 字段，数据库不存在，必报错。"
)


def main() -> None:
    print(
        f"目标库: {DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']} "
        f"表=mes_sql_rules"
    )
    log: list[str] = []
    deactivated = deactivate_learned_rules(log=log)
    for line in log:
        print(line)

    log2: list[str] = []
    inserted, skipped = insert_learned_rules(
        _EAM_REPAIR_CODE_RULE,
        source_snippet="cleanup_mes_sql_learned_rules.py",
        log=log2,
    )
    for line in log2:
        print(line)
    print(f"补全 CODE 规则: 新增 {inserted} 条，跳过 {skipped} 条")

    learned, learned_count = fetch_learned_rules()
    merged, total_count = fetch_merged_rules()
    print(
        f"验证: active learned {learned_count} 条（{len(learned)} 字符），"
        f"库内 active 总计 {total_count} 条（含 base）"
    )


if __name__ == "__main__":
    main()
