#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量导入/更新有效 ERP learned 规则（不含误伤项）。

  python3 seed_erp_sql_learned_rules.py
"""

from __future__ import annotations

from erp_sql_rules_db import DB_CONFIG, fetch_learned_rules, insert_learned_rules

_LEARNED_RULES_TEXT = """
【硬约束·245】表 P_MO 的 status 为 string 类型，禁止 CASE pmo.status WHEN 1 THEN N'外协' 等数字分支；须 CASE UPPER(RTRIM(pmo.status)) WHEN 'ORDER' THEN N'已下单' … ELSE pmo.status END。

【硬约束·245】表 P_MO 的 synchro/dev 为 string 存 '0'/'1' 等，禁止 CASE pmo.synchro WHEN 0 THEN … 数字分支。

【硬约束·207】表 P_WO 禁止无文档依据写 pwo.partnum / pwo.partNum；制造部件编码须经 P_MORoute JOIN E_JobMfgParts 输出 ejmp.partNum。

【硬约束·207】表 P_WO 禁止写 wo.moroute / pwo.moroute；工艺路线须 JOIN P_MORoute。

【硬约束·245】modifiedBy 为字符串用户名时，禁止 JOIN T_User ON tu.recId = 事实表.modifiedBy；须 事实表.modifiedBy AS [修改人]。

【硬约束·208】ERP SQL 禁止出现 MES 表名 TBL_*（如 TBL_MO、TBL_SFC_WS_LOG）。

【硬约束·102】中文别名含 /、(、)、（、）、空格、- 时，必须 AS [全文]，禁止 AS 审核/驳回人 等裸别名。

【硬约束】所有字段必须来自参考表结构，禁止臆造字段。
【自检规则】SQL 生成后必须逐列校验：字段/表必须在参考结构中存在。
【硬约束】禁止在 ERP SQL 中使用 MES 表名/字段（TBL_*、CID、CWC_ID 等）。
"""


def main() -> None:
    print(
        f"目标库: {DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']} "
        f"表=erp_sql_rules"
    )
    log: list[str] = []
    inserted, skipped = insert_learned_rules(
        _LEARNED_RULES_TEXT.strip(),
        source_snippet="seed_erp_sql_learned_rules.py",
        log=log,
    )
    for line in log:
        print(line)
    merged, count = fetch_learned_rules()
    print(f"完成: 本次新增 {inserted} 条，跳过 {skipped} 条")
    print(f"验证: learned 共 {count} 条，合并长度 {len(merged)} 字符")


if __name__ == "__main__":
    main()
