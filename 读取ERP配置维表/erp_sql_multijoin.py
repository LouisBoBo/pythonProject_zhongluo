#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多表主从明细查询：TOP (1000) 放置与排序策略（ERP 版）。

Dify 约束：最终结果**必须** `SELECT TOP (1000)`，超过 1000 行会导致出参 token 超限报错。
因此**禁止**省略 TOP。

主表 + 明细 JOIN 时，TOP 限制的是 JOIN 后总行数（最多 1000 行）。
须用 ORDER BY 主表时间 DESC + 明细序号 ASC，使这 1000 行优先覆盖「最新单据 + 有序明细行」。
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

_PARENT_CHILD_TABLES: Tuple[Tuple[str, str], ...] = (
    ("FGI_Receipt", "FGI_ReceiptItem"),
    ("M_PurchaseOrder", "M_PurchaseOrderItem"),
    ("M_BOMPicklist", "M_BOMPicklistItem"),
    ("S_ContractSO", "S_ContractItem"),
    ("M_Requisitions", "M_RequisitionsItem"),
    ("P_MO", "P_MOItem"),
)

_CHILD_SUFFIX_RE = re.compile(
    r"\b(?:FGI_|M_|S_|P_|T_|E_|EQ_)[\w_]*(?:Item|Items|Detail|Details)\b",
    re.I,
)

_EACH_DETAIL_KW = (
    "每一笔", "每一条", "每一项", "每个", "全部", "所有", "各项目",
    "明细行", "行项目", "明细项",
)

_DIFY_TOP_LIMIT = 1000


def _question_has_child_detail_intent(question: str) -> bool:
    q = (question or "").strip()
    if not q:
        return False
    if any(k in q for k in _EACH_DETAIL_KW):
        return True
    if "明细" in q and any(k in q for k in ("列表", "行", "项", "详情")):
        return True
    return False


def detect_multijoin_mode(user_question: str = "") -> str:
    """返回 multijoin 或 single_table（均须遵守 Dify TOP 1000 上限）。"""
    if _question_has_child_detail_intent(user_question):
        return "multijoin"
    return "single_table"


def sql_has_parent_child_join(sql: str) -> bool:
    s = (sql or "").upper()
    if not s.strip():
        return False
    for parent, child in _PARENT_CHILD_TABLES:
        if parent.upper() in s and child.upper() in s:
            return True
    if _CHILD_SUFFIX_RE.search(s) and re.search(r"\bJOIN\b", s, re.I):
        return True
    return False


def build_multijoin_query_hints(
    user_question: str = "",
    fact_table: str = "",
    config: Optional[Dict[str, Any]] = None,
) -> str:
    """注入 SQL LLM 的多表 TOP 策略块（由维表节点随 question 输出）。"""
    _ = config
    if detect_multijoin_mode(user_question) != "multijoin":
        return ""

    lines: List[str] = [
        "【多表主从明细 · TOP (1000) 策略（Dify 硬约束）】",
        f"- **必须保留**最外层 `SELECT TOP ({_DIFY_TOP_LIMIT})`：Dify 出参超过 {_DIFY_TOP_LIMIT} 行会 token 超限报错，**禁止省略 TOP**。",
        "- 本问题含主表 + 明细/子表 JOIN（1:N）：TOP 限制 **JOIN 后最多 1000 行**，无法在 Dify 内返回更多。",
        "- **必须** `ORDER BY` 主表主时间列 **DESC**（如 createDate/sendDate）+ 主表 **recId DESC** + 明细 **recId ASC** 或行号列 ASC。",
        "- 制成品接收明细：主表 `FGI_Receipt`，明细 `FGI_ReceiptItem`，JOIN `fr.recId = fri.fgiReceiptId`。",
        "- 采购订单明细：主表 `M_PurchaseOrder`，明细 `M_PurchaseOrderItem`。",
        "- 若用户问「全部/每一项」：在【相关表】说明「Dify 单次最多返回 1000 行，已按时间优先截断」。",
    ]
    return "\n".join(lines)


def fix_multijoin_top(sql: str, user_question: str = "") -> str:
    """
    Dify 兜底：主从 JOIN 的明细列表若缺少 TOP，补上 TOP (1000)。
    **不**再移除 TOP（与 Dify token 上限一致）。
    """
    s = (sql or "").strip()
    if not s:
        return s
    if not sql_has_parent_child_join(s):
        return s

    if re.match(r"^\s*SELECT\s+TOP\s*\(\s*\d+\s*\)", s, re.I):
        return s

    upper = s.upper()
    if re.search(r"\bSELECT\s+COUNT\s*\(", upper) and "GROUP BY" not in upper:
        return s

    return re.sub(
        r"^\s*SELECT\s+",
        f"SELECT TOP ({_DIFY_TOP_LIMIT}) ",
        s,
        count=1,
        flags=re.I,
    )
