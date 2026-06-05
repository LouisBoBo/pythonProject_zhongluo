# -*- coding: utf-8 -*-
"""
Dify 代码节点：清洗问题分类器 LLM 输出，强制二选一「查询」或「追问」。

入参：
  - raw_text: 分类器 LLM 节点的原始输出

出参：
  - intent: 「查询」或「追问」
"""


def main(raw_text: str) -> dict:
    text = (raw_text or "").strip()
    if not text:
        return {"intent": "追问"}

    first_line = text.splitlines()[0].strip()
    if first_line in ("查询", "追问"):
        return {"intent": first_line}
    if first_line.startswith("查询"):
        return {"intent": "查询"}
    if first_line.startswith("追问"):
        return {"intent": "追问"}

    idx_query = text.find("查询")
    idx_follow = text.find("追问")
    if idx_query >= 0 and (idx_follow < 0 or idx_query <= idx_follow):
        return {"intent": "查询"}
    if idx_follow >= 0:
        return {"intent": "追问"}

    return {"intent": "追问"}
