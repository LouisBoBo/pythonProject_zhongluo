#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通用表清单相关性排序：按用户问题对精简 catalog 行打分，缩小 LLM 选表范围。"""

from __future__ import annotations

import re
from typing import Dict, List, Set, Tuple

_CJK_RUN = re.compile(r"[\u4e00-\u9fff]+")
_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+")
_TABLE_LINE = re.compile(r"^[\w_]+\s*\|")

_FGI_KW = ("制成品接收", "接收明细", "FGI", "IQC")
_MO_KW = ("制造订单", "制造单", "MOSO")
_WO_KW = ("工单", "工作单")
_PURCHASE_KW = ("采购订单", "采购明细", "采购")
_OUTPUT_KW = ("过数", "产出", "工单过数")
_REQ_KW = ("请购", "请购单")
_MRB_KW = ("MRB", "送检申请", "送检")
_BOM_KW = ("领料", "BOM领料", "BOM 领料")


def extract_query_tokens(question: str) -> List[str]:
    """从问题中提取中文 n-gram（2~6字）及英文/表名片段，无业务硬编码。"""
    q = (question or "").strip()
    if not q:
        return []
    tokens: List[str] = []
    for run in _CJK_RUN.findall(q):
        tokens.append(run)
        max_n = min(6, len(run))
        for n in range(2, max_n + 1):
            for i in range(len(run) - n + 1):
                tokens.append(run[i : i + n])
    for w in _TOKEN.findall(q):
        tokens.append(w)
        if len(w) > 2:
            tokens.append(w.lower())
    seen: Set[str] = set()
    out: List[str] = []
    for t in sorted(tokens, key=len, reverse=True):
        key = t.lower()
        if key in seen or len(key) < 2:
            continue
        seen.add(key)
        out.append(t)
    return out


def _parse_line(line: str) -> Tuple[str, str, str]:
    parts = [p.strip() for p in line.split("|", 2)]
    tname = parts[0]
    label = parts[1] if len(parts) > 1 else ""
    biz = parts[2] if len(parts) > 2 else label
    return tname, label, biz


def score_catalog_line(line: str, tokens: List[str]) -> int:
    if not _TABLE_LINE.match((line or "").strip()):
        return 0
    text = line.lower()
    score = 0
    for tok in tokens:
        t = tok.lower()
        if t in text:
            score += len(t) * 10
    return score


def _infer_related_tables(tname: str, all_names: Set[str]) -> List[str]:
    """主表选中时，补全常见明细/子表（Receipt→ReceiptItem 等）。"""
    related: List[str] = []
    upper_map = {n.upper(): n for n in all_names}
    for suffix in ("Item", "Items", "Detail", "Details"):
        cand = tname + suffix
        if cand in all_names:
            related.append(cand)
        elif cand.upper() in upper_map:
            related.append(upper_map[cand.upper()])
    return related


def _apply_intent_boosts(question: str, scored: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    """按问题意图调整分数：制造订单/工单/接收/采购等易混场景。"""
    q = question or ""
    has_detail = "明细" in q or "详情" in q
    boosted: List[Tuple[int, str]] = []

    for s, ln in scored:
        tname, label, biz = _parse_line(ln)

        if any(k in q for k in _FGI_KW):
            if tname == "FGI_ReceiptItem":
                s += 300
            elif tname == "FGI_Receipt":
                s += 180 if has_detail else 120

        if any(k in q for k in _MO_KW):
            if tname == "P_MOSO":
                s += 280
            elif tname == "P_MO":
                s += 220 if not has_detail else 120

        if any(k in q for k in _WO_KW) and "制造订单" not in q:
            if tname == "P_WO":
                s += 250
            elif tname == "P_OutPut" and any(k in q for k in _OUTPUT_KW):
                s += 200

        if any(k in q for k in _PURCHASE_KW):
            if tname == "M_PurchaseOrderItem":
                s += 280 if has_detail else 180
            elif tname == "M_PurchaseOrder":
                s += 180 if not has_detail else 100

        if any(k in q for k in _REQ_KW) and tname == "M_Requisitions":
            s += 250

        if any(k in q for k in _MRB_KW) and tname == "P_MRBRequisition":
            s += 280

        if any(k in q for k in _BOM_KW):
            if tname == "M_BOMPicklistItem" and has_detail:
                s += 260
            elif tname == "M_BOMPicklist":
                s += 200

        boosted.append((s, ln))

    boosted.sort(key=lambda x: (-x[0], x[1]))
    return boosted


def _expand_related_tables(
    picked: List[Tuple[int, str]], line_by_name: Dict[str, str]
) -> List[Tuple[int, str]]:
    """主表选中后补子表，紧跟主表之后，不抬高到清单顶部。"""
    seen: Set[str] = set()
    merged: List[Tuple[int, str]] = []

    for s, ln in picked:
        tname = _parse_line(ln)[0]
        if tname not in seen:
            merged.append((s, ln))
            seen.add(tname)
        for rel in _infer_related_tables(tname, set(line_by_name)):
            if rel not in seen:
                merged.append((max(s - 1, 1), line_by_name[rel]))
                seen.add(rel)

    return merged


def rank_catalog_lines(
    question: str,
    slim_catalog: str,
    *,
    top_n: int = 40,
    min_score: int = 10,
) -> Tuple[str, int, str]:
    """
    返回 (ranked_catalog_text, matched_count, mode)。
    mode: "ranked" | "full"（无有效 token 或未命中时退回全量精简清单）
    """
    tokens = extract_query_tokens(question)
    lines = slim_catalog.splitlines()
    header = [ln for ln in lines if not _TABLE_LINE.match(ln.strip())]
    table_lines = [ln for ln in lines if _TABLE_LINE.match(ln.strip())]
    line_by_name = {_parse_line(ln)[0]: ln for ln in table_lines}

    if not tokens or not table_lines:
        return slim_catalog.strip(), len(table_lines), "full"

    scored = [(score_catalog_line(ln, tokens), ln) for ln in table_lines]
    scored = [(s, ln) for s, ln in scored if s >= min_score]
    scored.sort(key=lambda x: (-x[0], x[1]))

    if not scored:
        return slim_catalog.strip(), 0, "full"

    scored = _apply_intent_boosts(question, scored)
    picked = scored[:top_n]
    picked = _expand_related_tables(picked, line_by_name)
    picked = picked[: top_n + 8]

    body = [ln for _, ln in picked]
    ranked = "\n".join(header + [""] + body).strip()
    return ranked, len(body), "ranked"
