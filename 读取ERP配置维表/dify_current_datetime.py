# -*- coding: utf-8 -*-
# Dify「代码」节点：输出北京时间 current_datetime，供 SQL 生成 LLM 提示词使用。
#
# 不要用内置「获取当前时间」工具（返回 UTC，会差 8 小时）。
#
# 入参：无（可选 timestamp ← sys.timestamp）
# 出参：current_datetime，如 2026-06-05 10:45:09

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

_TZ_CN = timezone(timedelta(hours=8))


def main(timestamp: Optional[float] = None, **kwargs: Any) -> Dict[str, str]:
    ts = timestamp
    if ts is None:
        for key in ("timestamp", "sys_timestamp", "time"):
            v = kwargs.get(key)
            if v is not None and str(v).strip() != "":
                try:
                    ts = float(v)
                    break
                except (TypeError, ValueError):
                    pass

    if ts is not None:
        dt = datetime.fromtimestamp(float(ts), tz=_TZ_CN)
    else:
        dt = datetime.now(_TZ_CN)

    return {"current_datetime": dt.strftime("%Y-%m-%d %H:%M:%S")}


# --- Dify 入口（无需入参）---
try:
    timestamp
except NameError:
    timestamp = None

_out = main(timestamp=timestamp)
current_datetime = _out["current_datetime"]
