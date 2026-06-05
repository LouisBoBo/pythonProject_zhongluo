"""
Dify 代码节点：清理 conversation.rule_list 中误伤的 208 禁用规则。

典型误伤：历史重试报 208 后写入「TBL_BD_PROCESS 不存在，禁止使用」，
导致查工艺/工序时 LLM 不敢用正确主数据表，结果为空。
"""

import re
from typing import Any

from tiqu_error_rule import _MES_CORE_TABLES, _normalize_table_name

# 旧版 tiqu_error_rule 写入的永久禁用句式
_STALE_208_BAN = re.compile(
    r"^【硬约束·208】表\s+(\S+)\s+不存在，禁止使用。?\s*$",
    re.MULTILINE,
)


def sanitize_rule_list(rule_list: str | None = None, **kwargs: Any) -> dict[str, str]:
    text = (rule_list or kwargs.get("rule_text") or "").strip()
    if not text:
        return {"rule_list": "", "removed_count": "0"}

    removed = 0
    kept_lines: list[str] = []

    for line in text.splitlines():
        m = _STALE_208_BAN.match(line.strip())
        if m:
            bare = _normalize_table_name(m.group(1))
            if bare in _MES_CORE_TABLES:
                removed += 1
                continue
        kept_lines.append(line)

    cleaned = "\n".join(kept_lines).strip()
    return {"rule_list": cleaned, "removed_count": str(removed)}


def main(rule_list: str | None = None, **kwargs: Any) -> dict[str, str]:
    return sanitize_rule_list(rule_list, **kwargs)


if __name__ == "__main__":
    sample = """【硬约束·208】表 dbo.TBL_BD_PROCESS 不存在，禁止使用。
【硬约束·208】表 dbo.TBL_BD_WC_PROCESS_LINK 不存在，禁止使用。
【硬约束·207】字段 CWC_ID 不存在，禁止在 SQL 中使用。
"""
    out = main(rule_list=sample)
    print(out)
    assert "TBL_BD_PROCESS" not in out["rule_list"]
    assert out["removed_count"] == "2"
