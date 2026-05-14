#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dify「代码」节点：根据 SQL 文本判定应连接的数据库标识。

路由规则（摘要）：
1. 清单表名在 SQL 中全等命中（词边界，大小写不敏感；已去注释与字符串字面量）：
   - 先查 18.CIEAP 清单，再查 10.CIEAP 清单；命中即返回，整段忽略关键词规则。
2. 若两清单均无命中：启用关键词路由（全文）。
3. 仍无法归类：10.CIMOM。

返回值（Dify）：dict，仅含一个键 ``db``，值为且仅为以下三者之一：
``10.CIEAP`` | ``18.CIEAP`` | ``10.CIMOM``

命令行：``python pandan_in_db.py`` 或 ``python pandan_in_db.py 'SELECT ...'`` 时向 stdout 打印且仅打印一行该标识（无其它字符）。
"""

from __future__ import annotations

import re
import sys
from typing import Any, Dict, List, Optional, Set, Tuple

# 18.CIEAP 优先于 10.CIEAP（两清单表名互不重叠；若将来重叠，先命中 18）
TBL_18_CIEAP: Set[str] = {
    "TBL_EAP_HONGSHENG_RECORDS",
    "TBL_EAP_HONGSHENG_TM_RECORDS",
    "TBL_EAP_LWT_DETECTIONS",
    "TBL_EAP_LWT_DETECTIONS_DTL",
    "TBL_EAP_MASON_DETECTIONS",
    "TBL_EAP_MASON_DETECTIONS_DTL",
    "TBL_EAP_YUHUI_TEST_RECORDS",
    "TBL_EAP_YUHUI_TEST_RECORDS_DTL",
    "TBL_JINMING_TASK_RESULT",
    "TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD",
    "TBL_PATTERN_HAOSHUO_PRODUCTION_RECORD_DTL",
    "TBL_PATTERN_PLATING_PRODUCTION_RECORD",
}

TBL_10_CIEAP: Set[str] = {
    "TBL_EAP_ALARM",
    "TBL_EAP_AOI_DETECTIONS",
    "TBL_EAP_AOI_DETECTIONS_DTL",
    "TBL_EAP_API_RECORDS",
    "TBL_EAP_CURRENT_DATA",
    "TBL_EAP_DATA",
    "TBL_EAP_DATA_CONTENT",
    "TBL_EAP_DATA_YYYYMM",
    "TBL_EAP_DEVICE",
    "TBL_EAP_HEARTBEATS",
    "TBL_EAP_HQ_PRESS_PRODUCTION",
    "TBL_EAP_HQ_PRESS_PRODUCTION_ONSUBMIT",
    "TBL_EAP_LDI_LOG",
    "TBL_EAP_PERIOD",
    "TBL_EAP_PMS_CONTENT",
    "TBL_EAP_PMS_PROD",
    "TBL_EAP_PMS_PROD_DTL",
    "TBL_EAP_STATUS",
    "TBL_EAP_TAG",
    "TBL_EAP_WHC",
    "TBL_EAP_WHC_DTL",
    "TBL_EAP_YULIGHT_DETECTIONS_PCS",
    "TBL_EAP_YULIGHT_DETECTIONS_PNL",
}

# 无清单表名命中时：关键词（18 优先于 10）
KW_18: Tuple[str, ...] = (
    "鸿盛",
    "班通(LWT)",
    "麦逊(MASON)",
    "金铭",
    "浩硕",
    "图电",
)

KW_10: Tuple[str, ...] = (
    "EAP采集",
    "测点",
    "心跳",
    "设备状态",
    "联机设备",
    "PMS",
    "WHC",
    "玉辉点灯",
)

OUT_18 = "18.CIEAP"
OUT_10_EAP = "10.CIEAP"
OUT_10_MOM = "10.CIMOM"


def _strip_sql_comments(sql: str) -> str:
    s = re.sub(r"/\*.*?\*/", " ", sql, flags=re.DOTALL)
    s = re.sub(r"--[^\n]*", " ", s)
    return s


def _strip_string_literals(sql: str) -> str:
    """将单引号字符串替换为空格，避免字面量内出现表名导致误命中。"""
    out: List[str] = []
    i = 0
    n = len(sql)
    while i < n:
        ch = sql[i]
        if ch == "'":
            out.append(" ")
            i += 1
            while i < n:
                if sql[i] == "'":
                    if i + 1 < n and sql[i + 1] == "'":
                        i += 2
                        continue
                    i += 1
                    break
                i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def _normalize_for_table_scan(sql: str) -> str:
    return _strip_string_literals(_strip_sql_comments(sql))


def _listed_table_hit(sql_norm: str) -> Optional[str]:
    """若命中清单表名，返回 OUT_18 或 OUT_10_EAP；否则 None。"""
    for name in TBL_18_CIEAP:
        if re.search(rf"\b{re.escape(name)}\b", sql_norm, flags=re.IGNORECASE):
            return OUT_18
    for name in TBL_10_CIEAP:
        if re.search(rf"\b{re.escape(name)}\b", sql_norm, flags=re.IGNORECASE):
            return OUT_10_EAP
    return None


def _keyword_route(text: str) -> Optional[str]:
    for k in KW_18:
        if k in text:
            return OUT_18
    for k in KW_10:
        if k in text:
            return OUT_10_EAP
    return None


def route_sql_to_db(sql: str) -> str:
    if not sql or not str(sql).strip():
        return OUT_10_MOM
    raw = str(sql)
    sql_norm = _normalize_for_table_scan(raw)
    hit = _listed_table_hit(sql_norm)
    if hit is not None:
        return hit
    kw = _keyword_route(raw)
    if kw is not None:
        return kw
    return OUT_10_MOM


def _coerce_sql_arg(
    sql: Optional[str],
    inputs: Optional[Dict[str, Any]],
    kwargs: Dict[str, Any],
) -> str:
    if sql is not None and str(sql).strip():
        return str(sql)
    if kwargs:
        for key in ("sql", "query", "SQL", "statement", "sql_text"):
            v = kwargs.get(key)
            if v is not None and str(v).strip():
                return str(v)
    if inputs:
        for key in ("sql", "query", "SQL", "statement", "sql_text"):
            v = inputs.get(key)
            if v is not None and str(v).strip():
                return str(v)
        if len(inputs) == 1:
            v = next(iter(inputs.values()))
            if v is not None and str(v).strip():
                return str(v)
    return ""


def main(
    sql: Optional[str] = None,
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, str]:
    """
    Dify 代码节点入口。返回 ``{"db": "10.CIEAP"|"18.CIEAP"|"10.CIMOM"}``。
    """
    merged: Dict[str, Any] = {}
    if inputs:
        merged.update(inputs)
    merged.update(kwargs)
    text = _coerce_sql_arg(sql, inputs, merged)
    db = route_sql_to_db(text)
    return {"db": db}


def _stdout_print_raw_utf8_line(text: str) -> None:
    if not text.endswith("\n"):
        text = text + "\n"
    raw = text.encode("utf-8", errors="replace")
    buf = getattr(sys.stdout, "buffer", None)
    if buf is not None:
        buf.write(raw)
        buf.flush()
    else:
        sys.stdout.write(text)
        sys.stdout.flush()


if __name__ == "__main__":
    arg_sql = "SELECT TOP (1000) r.CP_IN_CODE AS [入库单号], r.CITEM_NO AS [料号], r.CPCS_QTY AS [总数量], r.CQUALITY_QTY AS [正品数], r.CBOX_QTY AS [箱数], r.CLOCATION_CODE AS [货位编码], w.CWAREHOUSE_NAME AS [仓库名称], i.CITEM_NAME AS [物料名称] FROM dbo.TBL_WMS_PACKAGE_IN_RECORDS r\n\nWITH (NOLOCK) LEFT JOIN dbo.TBL_BD_ITEM i\n\nWITH (NOLOCK) ON r.CITEM_NO = i.CITEM_NO LEFT JOIN dbo.TBL_WMS_WAREHOUSE w\n\nWITH (NOLOCK) ON r.CWAREHOUSE_CODE = w.CWAREHOUSE_CODE WHERE i.CITEM_NAME LIKE N'%单面沉锡板%"
    if len(sys.argv) > 1:
        arg_sql = sys.argv[1]
    elif not sys.stdin.isatty():
        arg_sql = sys.stdin.read()
    db = route_sql_to_db(arg_sql)
    _stdout_print_raw_utf8_line(db.rstrip("\n\r"))
