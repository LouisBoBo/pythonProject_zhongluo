"""
Dify 代码节点：将 JSON 字符串解析为 object（dict/list）。

在 Dify 中配置：
- 输入：上游 LLM 整段输出 object，或变量 text / arg1（JSON 字符串）
- 输出：pcb_data（解析后的 object）

示例输入（text 字段为 JSON 字符串）：
{"text": "{\\n  \\"customer_info\\": ...}", "finish_reason": "stop", ...}
"""

from __future__ import annotations

import json
import re
from typing import Any


def _strip_code_fence(s: str) -> str:
    s = s.strip()
    if not s.startswith("```"):
        return s
    lines = s.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip()


def _extract_json_str(raw: Any) -> str:
    if raw is None:
        return ""
    if isinstance(raw, dict):
        for key in ("text", "json_str", "content", "arg1", "json"):
            v = raw.get(key)
            if v is not None and v != "":
                return _extract_json_str(v)
        if len(raw) == 1:
            return _extract_json_str(next(iter(raw.values())))
        return ""
    if isinstance(raw, (list, int, float, bool)):
        return json.dumps(raw, ensure_ascii=False)
    return str(raw).strip()


def _parse_json_text(s: str) -> Any:
    s = _strip_code_fence(s)
    if not s:
        raise ValueError("JSON 字符串为空")
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        # 兼容首尾多余说明文字，取第一个 { 或 [ 到最后一个 } 或 ]
        start_obj = s.find("{")
        start_arr = s.find("[")
        if start_obj == -1 and start_arr == -1:
            raise
        if start_arr == -1 or (start_obj != -1 and start_obj < start_arr):
            start, end_char = start_obj, "}"
        else:
            start, end_char = start_arr, "]"
        end = s.rfind(end_char)
        if end <= start:
            raise
        return json.loads(s[start : end + 1])


def main(text: Any = None, arg1: Any = None, **kwargs: Any) -> dict[str, Any]:
    """
    Dify 代码节点入口。返回 {"pcb_data": <解析结果>, "error": ""}；
    解析失败时 pcb_data 为 None，error 为错误信息。
    """
    payload = text if text is not None else arg1
    if payload is None and kwargs:
        for v in kwargs.values():
            if isinstance(v, (dict, str, list)):
                payload = v
                break

    raw_str = _extract_json_str(payload)
    if not raw_str and isinstance(payload, (dict, list)):
        return {"pcb_data": payload, "error": ""}

    try:
        pcb_data = _parse_json_text(raw_str)
    except (json.JSONDecodeError, ValueError, TypeError) as e:
        return {"pcb_data": None, "error": str(e)}

    return {"pcb_data": pcb_data, "error": ""}
