"""
Dify 代码节点：从上游 JSON 中提取 full_rules。

在 Dify 中配置：
- 输入：整段 object/string，或变量 arg1 / json（见 main）
- 输出：仅 full_rules（string）

支持结构：
- {"arg1": [{"result": [{"full_rules": "..."}], "status": "..."}, ...]}
- {"json":  [...]}（同上）
- 直接传数组 [{"result": [...]}, ...]（常见于 Dify 把 arg1 指到数组本身）
"""

from __future__ import annotations

import json
from typing import Any


def _normalize_payload(raw: Any) -> dict[str, Any] | list[Any]:
    if raw is None:
        return {}
    if isinstance(raw, str):
        raw = raw.strip()
        if not raw:
            return {}
        return json.loads(raw)
    if isinstance(raw, (dict, list)):
        return raw
    raise TypeError("输入须为 dict、list 或可解析为 JSON 的字符串")


def _blocks_from_root(data: dict[str, Any] | list[Any]) -> list[Any]:
    """得到与旧版 json[] 同级的块列表（每项含 result）。"""
    if isinstance(data, list):
        return data
    for key in ("arg1", "json"):
        v = data.get(key)
        if isinstance(v, list):
            return v
    for v in data.values():
        if not isinstance(v, list) or not v:
            continue
        if not all(isinstance(x, dict) for x in v):
            continue
        if any(isinstance(x, dict) and "result" in x for x in v):
            return v
    return []


def extract_full_rules(data: dict[str, Any] | list[Any]) -> list[str]:
    """从 arg1[]/json[]/根数组 → result[] → full_rules 收集所有非空字符串。"""
    out: list[str] = []
    for block in _blocks_from_root(data):
        if not isinstance(block, dict):
            continue
        results = block.get("result")
        if not isinstance(results, list):
            continue
        for row in results:
            if not isinstance(row, dict):
                continue
            text = row.get("full_rules")
            if isinstance(text, str) and text.strip():
                out.append(text)
    return out


def main(arg1: Any = None, json: Any = None, **kwargs: Any) -> dict[str, Any]:
    """
    Dify 代码节点入口。

    优先使用命名参数 arg1，其次 json；若均未传则在 kwargs 中取首个 dict/str。
    """
    payload = arg1 if arg1 is not None else json
    if payload is None and kwargs:
        for v in kwargs.values():
            if isinstance(v, (dict, str, list)):
                payload = v
                break

    data = _normalize_payload(payload)
    parts = extract_full_rules(data)
    merged = "\n\n---\n\n".join(parts) if parts else ""
    return {"full_rules": merged}
