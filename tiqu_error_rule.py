import re
from typing import Any

# MES 标准主数据表：一次 208 多为连错库/拼写/SQL 误写，不应写入「永久禁止」
_MES_CORE_TABLES = frozenset(
    {
        "TBL_BD_PROCESS",
        "TBL_BD_PROCESS_OUTS",
        "TBL_BD_WC",
        "TBL_BD_WC_PROCESS_LINK",
        "TBL_BD_ITEM",
        "TBL_BD_ITEM_TYPE",
        "TBL_MO",
        "TBL_SFC_WS_LOG",
        "TBL_SFC_WS_LOG_ITEM",
        "TBL_SYS_USER",
        "TBL_SYS_ROLE",
        "TBL_WMS_WAREHOUSE",
        "TBL_WMS_LOCATION",
        "TBL_EAP_DEVICE",
        "TBL_EAP_T_ALARM",
    }
)

# 文档有、现场确认未部署：208 可记为长期禁用
_KNOWN_UNDEPLOYED_TABLES = frozenset(
    {
        "TBL_EAP_ALARM",
        "TBL_EAP_AOI_DETECTIONS",
        "TBL_EAP_AOI_DETECTIONS_DTL",
        "TBL_EAP_LDI_JOB",
        "TBL_WMS_STOCKTAKING_DTL",
        "TBL_PATTERN_PLATING_PRODUCTION_RECORD",
    }
)


def _normalize_table_name(name: str) -> str:
    s = (name or "").strip()
    if "." in s:
        s = s.rsplit(".", 1)[-1]
    return s.upper()


def main(error_msg: str = None, **kwargs: Any) -> dict[str, str]:
    """
    从 SQL Server 报错信息中自动提取可固化的规则
    支持：207无效列名 / 208无效表 / 102语法错误 / 156关键字错误 / 8127聚合排序
    """
    if not error_msg:
        return {"rule_text": ""}

    rules = []
    invalid_item = None
    table_name = None

    # === 1. 提取 207 无效列名 Invalid column name 'XXX' ===
    match_207 = re.search(r"Invalid column name '([^']+)'", error_msg, re.IGNORECASE)
    if match_207:
        invalid_item = match_207.group(1)
        sql_in_err = ""
        m_sql = re.search(r"\[SQL:\s*(.+?)\]\s*\(", error_msg, re.S | re.I)
        if m_sql:
            sql_in_err = m_sql.group(1)

        if invalid_item.upper() == "CODE" and re.search(
            r"\bTBL_EAM_REPAIR\b|\ber\.CODE\b",
            sql_in_err or error_msg,
            re.I,
        ):
            rules.append(
                "【硬约束·207】表 TBL_EAM_REPAIR 严禁使用 CODE 字段，数据库不存在，必报错。"
            )
        elif invalid_item.lower() == "modifiedby" and re.search(
            r"\bFGI_IQCRESULT\b", sql_in_err or error_msg, re.I
        ):
            rules.append(
                "【提示·207】FGI_IQCResult（检验结果表）无 modifiedBy 列，"
                "删除 fiqc.modifiedBy AS [修改人]；勿 JOIN T_User ON modifiedBy。"
            )
        elif invalid_item.lower() == "partnum" and (
            re.search(r"\bP_WO\b", error_msg, re.I)
            or re.search(r"pwo\d*\.partnum", sql_in_err, re.I)
        ):
            rules.append(
                "【提示·207】P_WO 表无 partnum/partNum 列：删除所有 pwo/pwo2…partnum；"
                "制造部件编码须 JOIN dbo.E_JobMfgParts ejmp ON ejmp.recId = 主表.mfgPartId，"
                "输出 ejmp.partNum AS [制造部件编码]。"
            )
        elif invalid_item in ("partnum", "partNum") and not table_name:
            rules.append(
                f"【提示·207】字段 {invalid_item} 在 P_WO 上不存在；"
                f"勿写 pwo.partnum，改用 E_JobMfgParts.partNum 或 S_Job.partNum。"
            )
        else:
            table_match = re.search(
                r"dbo\.(\w+)|FROM d\.(\w+)|FROM (\w+)\s|JOIN (\w+)\s",
                sql_in_err or error_msg,
                re.I,
            )
            if table_match:
                table_name = next(g for g in table_match.groups() if g)
            if table_name:
                rules.append(
                    f"【硬约束·207】表 {table_name} 严禁使用 {invalid_item} 字段，数据库不存在，必报错。"
                )
            else:
                rules.append(f"【硬约束·207】字段 {invalid_item} 不存在，禁止在 SQL 中使用。")

    # === 2. 提取 208 无效表 ===
    elif "Invalid object name" in error_msg:
        match_208 = re.search(r"Invalid object name '([^']+)'", error_msg, re.IGNORECASE)
        if match_208:
            invalid_item = match_208.group(1)
            bare = _normalize_table_name(invalid_item)
            if bare in _KNOWN_UNDEPLOYED_TABLES:
                rules.append(f"【硬约束·208】表 {invalid_item} 目标库未部署，禁止使用。")
            elif bare in _MES_CORE_TABLES:
                rules.append(
                    f"【提示·208】上次 SQL 报 Invalid object name '{invalid_item}'："
                    f"请核对 MES 库连接、schema（dbo）与表名拼写；"
                    f"{bare} 为标准主数据表，修正 SQL 后仍可使用，禁止因一次 208 永久弃用。"
                )
            else:
                rules.append(
                    f"【提示·208】上次 SQL 报 Invalid object name '{invalid_item}'："
                    f"请核对 schema、表名拼写与数据库连接；"
                    f"若【参考表结构】含该表则修正 SQL 后仍可使用，勿盲目永久禁用。"
                )
        rules.append("【硬约束】表名必须与参考表结构完全一致。")

    # === 3. 提取 102 语法错误（括号 / 斜杠）===
    elif "Incorrect syntax near" in error_msg:
        match_102 = re.search(
            r"Incorrect syntax near (?:the keyword )?'([^']+)'|Incorrect syntax near \"([^\"]+)\"",
            error_msg,
            re.IGNORECASE,
        )
        if match_102:
            invalid_item = match_102.group(1) or match_102.group(2)
            token = (invalid_item or "").strip()
            if token and len(token) > 3 and token not in {"/", "（", "）"}:
                rules.append(
                    f"【硬约束·102】别名含 {token} 必须用 [] 包裹，如 AS [别名]"
                )
            else:
                rules.append(
                    "【硬约束·102】SQL 语法错误，检查别名是否用 [] 包裹、括号是否配对。"
                )
        else:
            rules.append("【硬约束·102】SQL 语法错误，检查别名是否用 [] 包裹、括号是否配对。")
        rules.append("【硬约束】中文别名含 / ( ) （ ）必须整体加 []。")

    # === 4. 156 关键字错误 ===
    elif "keyword" in error_msg:
        rules.append("【硬约束·156】与SQL关键字同名的列必须用 [] 包裹。")

    # === 5. 8127 聚合排序错误 ===
    elif "8127" in error_msg:
        rules.append("【硬约束·8127】COUNT/SUM 等单行聚合禁止加 ORDER BY。")

    return {"rule_text": "\n".join(rules)}
