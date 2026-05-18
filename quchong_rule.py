import re
from typing import Any


def _decode_literal_utf8_byte_escapes(s: str) -> str:
    """
    将字符串中连续的 \\xHH（字面量反斜杠 + x + 两位十六进制）按 UTF-8 解码为 Unicode。
    用于 Dify/上游把 UTF-8 字节写成 \\xe9\\xa2\\x84 这类转义时的还原。
    """

    def repl(m: re.Match[str]) -> str:
        run = m.group(0)
        pairs = re.findall(r"\\x([0-9a-fA-F]{2})", run)
        if not pairs:
            return run
        try:
            return bytes(int(h, 16) for h in pairs).decode("utf-8", errors="replace")
        except ValueError:
            return run

    return re.sub(r"(?:\\x[0-9a-fA-F]{2})+", repl, s)


def main(
    rule_text: str | None = None,
    error_rule_text: str | None = None,
    **kwargs: Any,
) -> dict[str, str]:
    """
    判断旧规则全文是否已包含新规则（去字面量 \\xHH UTF-8 转义后做子串匹配）。
    Dify 代码节点输出：result 为字符串 \"true\" 或 \"false\"。
    """
    old = (rule_text or "").strip()
    new_raw = (error_rule_text or "").strip()
    new_norm = _decode_literal_utf8_byte_escapes(new_raw)

    if not new_norm:
        return {"result": "false"}

    contained = new_norm in old
    return {"result": "true" if contained else "false"}
