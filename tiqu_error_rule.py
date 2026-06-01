import re
from typing import Any


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
        
        # 尝试提取表名（从 SQL 中定位）
        table_match = re.search(r"FROM d\.(\w+)|FROM (\w+)\s|JOIN (\w+)\s", error_msg)
        if table_match:
            table_name = next(g for g in table_match.groups() if g)

        # 生成规则
        if table_name:
            rules.append(f"【硬约束·207】表 {table_name} 严禁使用 {invalid_item} 字段，数据库不存在，必报错。")
        else:
            rules.append(f"【硬约束·207】字段 {invalid_item} 不存在，禁止在 SQL 中使用。")
        

    # === 2. 提取 208 无效表 ===
    elif "Invalid object name" in error_msg:
        match_208 = re.search(r"Invalid object name '([^']+)'", error_msg, re.IGNORECASE)
        if match_208:
            invalid_item = match_208.group(1)
            rules.append(f"【硬约束·208】表 {invalid_item} 不存在，禁止使用。")
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
            rules.append(f"【硬约束·102】别名含 {invalid_item} 必须用 [] 包裹，如 AS [别名]")
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
