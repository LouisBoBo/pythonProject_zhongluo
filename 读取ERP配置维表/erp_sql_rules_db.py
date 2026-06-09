#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ERP SQL 约束规则 PostgreSQL 读写（基础规则 + 学习规则，表 erp_sql_rules，与 MES 隔离）。"""

from __future__ import annotations

import re
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

DB_CONFIG: Dict[str, Any] = {
    "host": "192.168.60.2",
    "port": 15432,
    "database": "demo",
    "user": "postgres",
    "password": "postgres",
    "connect_timeout": 10,
}

DEFAULT_TABLE = "erp_sql_rules"
_RULE_TYPE_BASE = "base"
_RULE_TYPE_LEARNED = "learned"
_RESULT_OK = "成功"
_RESULT_FAIL = "失败"
_MAX_MESSAGE_LEN = 8000

_ERP_CORE_TABLES = frozenset(
    {
        "P_MO",
        "P_WO",
        "P_OUTPUT",
        "P_MOSO",
        "P_MRBREQUISITION",
        "P_MOROUTE",
        "FGI_RECEIPT",
        "FGI_RECEIPTITEM",
        "M_PURCHASEORDER",
        "M_PURCHASEORDERITEM",
        "M_REQUISITIONS",
        "M_BOMPICKLIST",
        "M_BOMPICKLISTITEM",
        "S_JOB",
        "S_CONTRACTSO",
        "S_CONTRACTITEM",
        "T_USER",
        "T_PLANTS",
        "M_MATERIALS",
        "S_CUSTOMER",
        "T_WAREHOUSE",
        "E_JOBMFGPARTS",
    }
)

_STALE_208_BAN = re.compile(
    r"^【硬约束·208】表\s+(\S+)\s+不存在，禁止使用。?\s*$",
    re.MULTILINE,
)
_STALE_102_ALIAS = re.compile(
    r"^【硬约束·102】别名含\s+(\S+)\s+必须用\s*\[\]\s*包裹",
)
_BAD_GLOBAL_207 = re.compile(
    r"^【硬约束·207】字段\s+(CID|CWC_ID|CSTATUS|CCUSTOMER_CODE|TBL_)\s",
)
_MES_TABLE_IN_ERP = re.compile(r"\bTBL_[A-Z0-9_]+\b", re.I)
_MISPARSED_102_TOKENS = frozenset(
    {
        "i",
        "p",
        "t",
        "w",
        "d",
        "mo",
        "wo",
        "pmo",
        "pwo",
        "fr",
        "sj",
        "/",
        "（",
    }
)
_ERROR_CODE_RE = re.compile(r"【(?:硬约束|提示)·(\d+)】")

_CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS erp_sql_rules (
    id BIGSERIAL PRIMARY KEY,
    rule_type TEXT NOT NULL,
    rule_text TEXT NOT NULL,
    error_code TEXT,
    source_snippet TEXT,
    priority INT NOT NULL DEFAULT 100,
    hit_count INT NOT NULL DEFAULT 0,
    state TEXT NOT NULL DEFAULT 'A',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    modified_at TIMESTAMPTZ
)
"""

_CREATE_UNIQUE_INDEX_SQL = """
CREATE UNIQUE INDEX IF NOT EXISTS ux_erp_sql_rules_learned_text
ON erp_sql_rules (rule_text)
WHERE rule_type = 'learned' AND state = 'A'
"""


def _quote_ident(part: str) -> str:
    return '"' + part.replace('"', '""') + '"'


def _qualified_table_sql(table: str = DEFAULT_TABLE) -> str:
    return _quote_ident(table.strip())


def _connect():
    try:
        import psycopg2
    except ImportError as e:
        raise ImportError(
            "未安装 psycopg2，请在 Dify 代码沙箱安装: pip install psycopg2-binary"
        ) from e

    return psycopg2.connect(
        host=str(DB_CONFIG["host"]),
        port=int(DB_CONFIG["port"]),
        dbname=str(DB_CONFIG["database"]),
        user=str(DB_CONFIG["user"]),
        password=str(DB_CONFIG["password"]),
        connect_timeout=int(DB_CONFIG["connect_timeout"]),
    )


def _mk_result(ok: bool, log: List[str], **extra: str) -> Dict[str, str]:
    msg = "\n".join(log)
    if len(msg) > _MAX_MESSAGE_LEN:
        msg = msg[: _MAX_MESSAGE_LEN - 20] + "\n...(日志已截断)"
    out: Dict[str, str] = {
        "result": _RESULT_OK if ok else _RESULT_FAIL,
        "message": msg,
    }
    for k, v in extra.items():
        out[k] = str(v if v is not None else "")
    return out


def ensure_schema(cur: Any, log: List[str]) -> None:
    cur.execute(_CREATE_TABLE_SQL)
    cur.execute(_CREATE_UNIQUE_INDEX_SQL)
    log.append(f"已确保表存在: {DEFAULT_TABLE}")


def _normalize_table_name(name: str) -> str:
    s = (name or "").strip()
    if "." in s:
        s = s.rsplit(".", 1)[-1]
    return s.upper()


def should_skip_learned_rule(rule_text: str) -> bool:
    """误伤核心 ERP 表、MES 表名混入、泛化 102/207 规则不入库。"""
    text = (rule_text or "").strip()
    if not text:
        return True
    if _MES_TABLE_IN_ERP.search(text):
        return True
    for line in text.splitlines():
        stripped = line.strip()
        m208 = _STALE_208_BAN.match(stripped)
        if m208 and _normalize_table_name(m208.group(1)) in _ERP_CORE_TABLES:
            return True
        m102 = _STALE_102_ALIAS.match(stripped)
        if m102:
            token = (m102.group(1) or "").strip().strip("'\"")
            if len(token) <= 3 or token.lower() in _MISPARSED_102_TOKENS:
                return True
        if _BAD_GLOBAL_207.match(stripped):
            return True
    return False


def extract_error_code(rule_text: str) -> str:
    m = _ERROR_CODE_RE.search(rule_text or "")
    return m.group(1) if m else ""


def _split_rule_blocks(text: str) -> List[str]:
    blocks: List[str] = []
    buf: List[str] = []
    for line in (text or "").splitlines():
        if not line.strip():
            if buf:
                blocks.append("\n".join(buf).strip())
                buf = []
            continue
        buf.append(line.rstrip())
    if buf:
        blocks.append("\n".join(buf).strip())
    return [b for b in blocks if b]


_BOILERPLATE_LINES = frozenset(
    {
        "【硬约束】所有字段必须来自参考表结构，禁止臆造字段。",
        "【自检规则】SQL 生成后必须逐列校验：字段/表必须在参考结构中存在。",
        "【硬约束】禁止在 ERP SQL 中使用 MES 表名/字段（TBL_*、CID、CWC_ID 等）。",
    }
)
_RULE_LINE_RE = re.compile(r"^【(?:硬约束|提示)[^】]*】.*$")


def format_learned_rules_for_prompt(rule_texts: Sequence[str]) -> str:
    """合并 learned 规则：去重 boilerplate，每条硬约束只保留一行。"""
    seen_rules: Set[str] = set()
    rule_lines: List[str] = []
    for block in rule_texts:
        for line in (block or "").splitlines():
            stripped = line.strip()
            if not stripped or stripped in _BOILERPLATE_LINES:
                continue
            if _RULE_LINE_RE.match(stripped):
                if stripped not in seen_rules:
                    seen_rules.add(stripped)
                    rule_lines.append(stripped)
    if not rule_lines:
        return ""
    tail = list(_BOILERPLATE_LINES)
    return "\n".join(rule_lines + tail)


def fetch_learned_rules(log: Optional[List[str]] = None) -> Tuple[str, int]:
    """仅读取 learned 规则（base 由系统提示词/约束 md 提供，避免重复占 token）。"""
    qtable = _qualified_table_sql()
    sql = f"""
        SELECT rule_text
        FROM {qtable}
        WHERE rule_type = %s AND state = 'A'
        ORDER BY priority, id
    """
    conn = _connect()
    try:
        cur = conn.cursor()
        cur.execute(sql, (_RULE_TYPE_LEARNED,))
        rows = cur.fetchall()
        cur.close()
    finally:
        conn.close()

    parts: List[str] = []
    for (rule_text,) in rows:
        text = (rule_text or "").strip()
        if text:
            parts.append(text)
    merged = format_learned_rules_for_prompt(parts)
    if log is not None:
        log.append(
            f"读取 learned 规则 {len(parts)} 条，压缩后 {len(merged)} 字符"
        )
    return merged, len(parts)


def fetch_merged_rules(log: Optional[List[str]] = None) -> Tuple[str, int]:
    """兼容本地脚本：base + learned 全量（含分隔符）。"""
    qtable = _qualified_table_sql()
    sql = f"""
        SELECT rule_type, rule_text
        FROM {qtable}
        WHERE state = 'A'
        ORDER BY CASE rule_type WHEN 'base' THEN 0 ELSE 1 END, priority, id
    """
    conn = _connect()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
    finally:
        conn.close()

    parts: List[str] = []
    for _rule_type, rule_text in rows:
        text = (rule_text or "").strip()
        if text:
            parts.append(text)
    merged = "\n\n".join(parts)
    if log is not None:
        log.append(f"读取规则 {len(rows)} 条，合并后 {len(merged)} 字符")
    return merged, len(rows)


def deactivate_learned_rules(
    match_substrings: Optional[List[str]] = None,
    match_regexes: Optional[List[str]] = None,
    log: Optional[List[str]] = None,
) -> int:
    """软删除匹配的 learned 规则，返回停用条数。"""
    qtable = _qualified_table_sql()
    conn = _connect()
    deactivated = 0
    try:
        cur = conn.cursor()
        ensure_schema(cur, log or [])
        cur.execute(
            f"SELECT id, rule_text FROM {qtable} WHERE rule_type = %s AND state = 'A'",
            (_RULE_TYPE_LEARNED,),
        )
        rows = cur.fetchall()
        regexes = [re.compile(p) for p in (match_regexes or [])]
        for rule_id, rule_text in rows:
            text = rule_text or ""
            hit = False
            for sub in match_substrings or []:
                if sub and sub in text:
                    hit = True
                    break
            if not hit:
                for rx in regexes:
                    if rx.search(text):
                        hit = True
                        break
            if not hit and should_skip_learned_rule(text):
                hit = True
            if hit:
                cur.execute(
                    f"UPDATE {qtable} SET state = 'D', modified_at = NOW() WHERE id = %s",
                    (rule_id,),
                )
                deactivated += 1
                if log is not None:
                    log.append(f"停用 learned #{rule_id}: {text[:72]}...")
        conn.commit()
        cur.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    if log is not None:
        log.append(f"共停用 learned 规则 {deactivated} 条")
    return deactivated


def upsert_base_rule(rule_text: str, log: Optional[List[str]] = None) -> None:
    text = (rule_text or "").strip()
    if not text:
        raise ValueError("基础规则内容为空")
    qtable = _qualified_table_sql()
    conn = _connect()
    try:
        cur = conn.cursor()
        ensure_schema(cur, log or [])
        cur.execute(
            f"UPDATE {qtable} SET state = 'D', modified_at = NOW() "
            f"WHERE rule_type = %s AND state = 'A'",
            (_RULE_TYPE_BASE,),
        )
        cur.execute(
            f"""
            INSERT INTO {qtable}
                (rule_type, rule_text, error_code, priority, state)
            VALUES (%s, %s, %s, %s, 'A')
            """,
            (_RULE_TYPE_BASE, text, "", 0),
        )
        conn.commit()
        if log is not None:
            log.append(f"已写入基础规则 1 条（{len(text)} 字符）")
        cur.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def insert_learned_rules(
    rule_text: str,
    source_snippet: str = "",
    log: Optional[List[str]] = None,
) -> Tuple[int, int]:
    """返回 (inserted_count, skipped_count)。"""
    qtable = _qualified_table_sql()
    inserted = 0
    skipped = 0
    blocks = _split_rule_blocks(rule_text)
    if not blocks and (rule_text or "").strip():
        blocks = [(rule_text or "").strip()]

    conn = _connect()
    try:
        cur = conn.cursor()
        ensure_schema(cur, log or [])
        for block in blocks:
            if should_skip_learned_rule(block):
                skipped += 1
                if log is not None:
                    log.append(f"跳过误伤规则: {block[:80]}...")
                continue
            err_code = extract_error_code(block)
            cur.execute(
                f"""
                SELECT 1 FROM {qtable}
                WHERE rule_type = %s AND state = 'A' AND rule_text = %s
                LIMIT 1
                """,
                (_RULE_TYPE_LEARNED, block),
            )
            if cur.fetchone():
                skipped += 1
                continue
            cur.execute(
                f"""
                INSERT INTO {qtable}
                    (rule_type, rule_text, error_code, source_snippet, priority, state)
                VALUES (%s, %s, %s, %s, %s, 'A')
                """,
                (
                    _RULE_TYPE_LEARNED,
                    block,
                    err_code,
                    (source_snippet or "")[:500],
                    100,
                ),
            )
            inserted += 1
        conn.commit()
        cur.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    if log is not None:
        log.append(f"学习规则写入: 新增 {inserted} 条，跳过 {skipped} 条")
    return inserted, skipped


def read_rules_main(**kwargs: Any) -> Dict[str, str]:
    try:
        merged, _count = fetch_learned_rules()
        return {"rule_list": str(merged or "")}
    except Exception:
        return {"rule_list": ""}


def write_rules_main(
    rule_text: str = "",
    error_msg: str = "",
    **kwargs: Any,
) -> Dict[str, str]:
    log: List[str] = ["=== erp_sql_rules_db_write 开始 ==="]
    raw = (rule_text or kwargs.get("new_rule") or kwargs.get("rule_text") or "").strip()
    source = (error_msg or kwargs.get("error_message") or "")[:500]
    if not raw:
        log.append("rule_text 为空，无需写入")
        return _mk_result(True, log, inserted_count="0", skipped_count="0")
    try:
        inserted, skipped = insert_learned_rules(raw, source_snippet=source, log=log)
        log.append("=== 执行成功 ===")
        return _mk_result(
            True,
            log,
            inserted_count=str(inserted),
            skipped_count=str(skipped),
        )
    except Exception as e:
        log.append(f"异常: {type(e).__name__}: {e}")
        log.append(traceback.format_exc().strip())
        log.append("=== 执行失败 ===")
        return _mk_result(False, log, inserted_count="0", skipped_count="0")


def load_base_rules_from_md(md_path: Optional[Path] = None) -> str:
    root = Path(__file__).resolve().parent
    path = Path(md_path) if md_path else root.parent / "中络项目ERP SQL约束规则提示词.md"
    if not path.is_file():
        raise FileNotFoundError(f"未找到: {path}")
    return path.read_text(encoding="utf-8")
