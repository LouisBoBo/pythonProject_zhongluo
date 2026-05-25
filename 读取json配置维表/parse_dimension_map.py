#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
解析 mes_dimension_joins.map（表格式文本）→ 与 mes_dimension_joins.json 相同结构的 dict。

维护人员只改 .map 文件，不必手写 JSON。
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

DEFAULT_MAP = Path(__file__).resolve().parent / "mes_dimension_joins.map"
DEFAULT_JSON = Path(__file__).resolve().parent / "mes_dimension_joins.json"


def _split_pipe(line: str) -> List[str]:
    return [p.strip() for p in line.split("|")]


def _parse_kv(line: str) -> Optional[Tuple[str, str]]:
    if "=" not in line:
        return None
    key, _, val = line.partition("=")
    return key.strip(), val.strip()


def parse_dimension_map(text: str) -> Dict[str, Any]:
    config: Dict[str, Any] = {
        "version": 1,
        "description": "由 mes_dimension_joins.map 解析生成",
        "default_fact_alias": "l",
        "tables": {},
        "global_forbidden": [],
    }

    current_table: Optional[str] = None
    current_mapping: Optional[Dict[str, Any]] = None
    section: Optional[str] = None  # global | table | mapping

    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("[") and line.endswith("]"):
            inner = line[1:-1].strip()
            if inner == "全局":
                section = "global"
                current_table = None
                current_mapping = None
                continue
            if inner.startswith("表 "):
                section = "table"
                tname = inner[2:].strip().upper()
                config["tables"][tname] = {
                    "fact_alias": config["default_fact_alias"],
                    "label": tname,
                    "default_for_keywords": [],
                    "mappings": [],
                    "display_columns": [],
                }
                current_table = tname
                current_mapping = None
                continue
            if inner.startswith("映射 "):
                if not current_table:
                    raise ValueError(f"映射块 [{inner}] 之前缺少 [表 ...]")
                section = "mapping"
                mid = inner[3:].strip()
                current_mapping = {
                    "id": mid,
                    "fact_columns": [],
                    "joins": [],
                    "select": [],
                    "forbidden": [],
                }
                config["tables"][current_table]["mappings"].append(current_mapping)
                continue
            raise ValueError(f"未知区块: {line}")

        kv = _parse_kv(line)
        if not kv:
            continue
        key, val = kv

        if section == "global":
            if key == "默认别名":
                config["default_fact_alias"] = val
            elif key == "禁止":
                config["global_forbidden"].append(val)
            continue

        if section == "table" and current_table:
            tbl = config["tables"][current_table]
            if key == "标签":
                tbl["label"] = val
            elif key == "关键词":
                tbl["default_for_keywords"] = [x.strip() for x in val.split(",") if x.strip()]
            elif key == "别名":
                tbl["fact_alias"] = val
            continue

        if key == "展示列" and current_table:
            parts = _split_pipe(val)
            if len(parts) != 2:
                raise ValueError(f"展示列格式错误（需 表达式|中文名）: {line}")
            config["tables"][current_table].setdefault("display_columns", []).append(
                {"expr": parts[0], "as": parts[1]}
            )
            continue

        if section == "mapping" and current_mapping is not None:
            if key == "字段":
                current_mapping["fact_columns"] = [
                    x.strip() for x in val.split(",") if x.strip()
                ]
            elif key == "类型":
                if val == "账号":
                    current_mapping["match_type"] = "account"
                elif val == "枚举":
                    current_mapping["match_type"] = "enum"
            elif key == "可选" and val in ("是", "true", "True", "1", "yes"):
                current_mapping["optional"] = True
            elif key == "说明":
                current_mapping["notes"] = val
            elif key == "关联":
                parts = _split_pipe(val)
                if len(parts) < 3:
                    raise ValueError(f"关联行格式错误（需 别名|维表|ON）: {line}")
                join: Dict[str, Any] = {
                    "alias": parts[0],
                    "table": parts[1],
                    "on": parts[2],
                }
                for extra in parts[3:]:
                    ek, _, ev = extra.partition("=")
                    if ek.strip() == "依赖":
                        join["depends_on"] = ev.strip()
                current_mapping["joins"].append(join)
            elif key == "列":
                parts = _split_pipe(val)
                if len(parts) != 2:
                    raise ValueError(f"列行格式错误（需 表达式|中文名）: {line}")
                current_mapping["select"].append({"expr": parts[0], "as": parts[1]})
            elif key == "禁止":
                current_mapping["forbidden"].append(val)
            continue

    if not config["tables"]:
        raise ValueError("未解析到任何 [表 ...] 块")
    return config


def load_dimension_config(
    map_path: Optional[Path] = None,
    json_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """优先读 .map；不存在则回退 .json。"""
    mp = Path(map_path) if map_path else DEFAULT_MAP
    jp = Path(json_path) if json_path else DEFAULT_JSON
    if mp.is_file():
        return parse_dimension_map(mp.read_text(encoding="utf-8"))
    if jp.is_file():
        return json.loads(jp.read_text(encoding="utf-8"))
    raise FileNotFoundError(f"未找到 {mp.name} 或 {jp.name}")


def write_json_from_map(
    map_path: Optional[Path] = None,
    json_path: Optional[Path] = None,
) -> Path:
    mp = Path(map_path) if map_path else DEFAULT_MAP
    jp = Path(json_path) if json_path else DEFAULT_JSON
    cfg = load_dimension_config(mp)
    jp.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return jp


if __name__ == "__main__":
    cfg = load_dimension_config()
    write_json_from_map()
    print(f"已从 {DEFAULT_MAP.name} 同步 → {DEFAULT_JSON.name}")
    print("表:", ", ".join(cfg["tables"].keys()))
