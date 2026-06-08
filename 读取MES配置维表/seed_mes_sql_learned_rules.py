#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量导入/更新有效 learned 规则（不含误伤项）。

  python3 seed_mes_sql_learned_rules.py
"""

from __future__ import annotations

from mes_sql_rules_db import DB_CONFIG, fetch_learned_rules, insert_learned_rules

# 仅保留字段级、可复用的 learned；泛化 102/全局 CSTATUS/CWC_ID 等勿写入
_LEARNED_RULES_TEXT = """
【硬约束·207】字段 CDISP_NAME 不存在，禁止在 SQL 中使用。

【硬约束·207】字段 CWO_LOT 不存在，禁止在 SQL 中使用。

【硬约束·207】字段 BOAR_TYPE 不存在，禁止在 SQL 中使用。

【硬约束·207】字段 CCLINK 不存在，禁止在 SQL 中使用。

【硬约束·207】字段 CISPONNECT 不存在，禁止在 SQL 中使用。

【硬约束·207】字段 CCCHECK_REMARK 不存在，禁止在 SQL 中使用。

【硬约束·207】字段 预测数量 不存在，禁止在 SQL 中使用。
【硬约束】所有字段必须来自参考表结构，禁止臆造字段。
【自检规则】SQL 生成后必须逐列校验：字段/表必须在参考结构中存在。

【硬约束·207】字段 APPLY_DATE 不存在，禁止在 SQL 中使用。
【硬约束】所有字段必须来自参考表结构，禁止臆造字段。
【自检规则】SQL 生成后必须逐列校验：字段/表必须在参考结构中存在。

【硬约束·207】字段 CREATE_DATE 不存在，禁止在 SQL 中使用。
【硬约束】所有字段必须来自参考表结构，禁止臆造字段。
【自检规则】SQL 生成后必须逐列校验：字段/表必须在参考结构中存在。

【硬约束·207】字段 CCREATE_DATE 不存在，禁止在 SQL 中使用。
【硬约束】所有字段必须来自参考表结构，禁止臆造字段。
【自检规则】SQL 生成后必须逐列校验：字段/表必须在参考结构中存在。

【硬约束·207】表 TBL_EAM_REPAIR 严禁使用 CODE 字段，数据库不存在，必报错。
"""


def main() -> None:
    print(
        f"目标库: {DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']} "
        f"表=mes_sql_rules"
    )
    log: list[str] = []
    inserted, skipped = insert_learned_rules(
        _LEARNED_RULES_TEXT.strip(),
        source_snippet="seed_mes_sql_learned_rules.py",
        log=log,
    )
    for line in log:
        print(line)
    merged, count = fetch_learned_rules()
    print(f"完成: 本次新增 {inserted} 条，跳过 {skipped} 条")
    print(f"验证: learned 共 {count} 条，合并长度 {len(merged)} 字符")


if __name__ == "__main__":
    main()
