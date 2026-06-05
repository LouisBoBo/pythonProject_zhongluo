from __future__ import annotations

"""
Dify 代码节点：将嵌套 records 转为单层 JSON 字符串（供下游展示/消费）。

入参（不变）：
  {"records": "[\"{\\\"模块代码\\\":\\\"...\\\", ...}\", \"{\\\"用户组ID\\\":...}\", ...]"}

即 records 为字符串 → json.loads 得到字符串数组 → 每条再 json.loads 得到对象。

输出（与贴图一致）：
  {"records": "[{\"最后修改日期\":\"...\",\"修改人\":\"...\", ...}, ...]"}

即 records 为字符串 → json.loads 一次即得到对象数组。

同时输出 markdown 表格（可选展示）。
"""

import json

_SKIP_KEYS = {"-"}

_PREFERRED_COLUMNS = (
    "最后修改日期",
    "修改人",
    "版本",
    "用户组名称",
    "用户组代码",
    "用户名称",
    "用户账号",
    "用户代码",
    "模块代码",
    "模块简称名",
    "模块简称名称",
    "是否禁用",
    "是否默认",
    "修改时间",
    "名称名称",
    "类型",
    "用户组ID",
    "组代码",
    "组名称",
    "是否激活",
)


def _merge_inputs(records, kwargs: dict) -> dict:
    merged: dict = {}
    raw = records
    if isinstance(raw, str):
        s = raw.strip()
        if s.startswith("{"):
            try:
                raw = json.loads(s)
            except json.JSONDecodeError:
                pass
    if isinstance(raw, dict):
        merged.update(raw)
        if "records" not in merged and len(raw) == 1:
            only_val = next(iter(raw.values()))
            if isinstance(only_val, (str, list)):
                merged["records"] = only_val
    merged.update(kwargs)
    return merged


def _parse_json_value(val):
    if isinstance(val, str):
        s = val.strip()
        if not s:
            return None
        parsed = json.loads(s)
        if isinstance(parsed, str):
            return json.loads(parsed.strip())
        return parsed
    return val


def _parse_records(raw) -> list[dict]:
    """解析入参：支持双层嵌套（元素为 JSON 字符串）及已是对象数组的情况。"""
    if raw is None:
        return []

    parsed = _parse_json_value(raw) if isinstance(raw, str) else raw
    if isinstance(parsed, dict) and "records" in parsed:
        parsed = parsed["records"]
    if parsed is None:
        return []
    if isinstance(parsed, dict):
        return [_clean_record(parsed)]
    if not isinstance(parsed, list):
        raise ValueError(f"records 须为 JSON 数组，当前为 {type(parsed).__name__}")

    out: list[dict] = []
    for i, item in enumerate(parsed):
        if item is None:
            continue
        if isinstance(item, str):
            s = item.strip()
            if not s:
                continue
            try:
                item = json.loads(s)
            except json.JSONDecodeError as e:
                raise ValueError(f"records[{i}] 不是合法 JSON 对象: {e}") from e
        if isinstance(item, dict):
            out.append(_clean_record(item))
    return out


def _clean_record(rec: dict) -> dict:
    return {k: v for k, v in rec.items() if k not in _SKIP_KEYS}


def _order_record(rec: dict) -> dict:
    ordered: dict = {}
    seen: set[str] = set()
    for name in _PREFERRED_COLUMNS:
        if name in rec:
            ordered[name] = rec[name]
            seen.add(name)
    for k, v in rec.items():
        if k not in seen:
            ordered[k] = v
    return ordered


def records_to_flat_json(records: list[dict]) -> str:
    """输出贴图格式：records 为单层 JSON 对象数组字符串。"""
    normalized = [_order_record(rec) for rec in records]
    return json.dumps(normalized, ensure_ascii=False)


def _format_cell(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "是" if value else "否"
    if isinstance(value, (dict, list)):
        text = json.dumps(value, ensure_ascii=False)
    else:
        text = str(value)
    return text.replace("|", "\\|").replace("\n", " ").replace("\r", "")


def _infer_columns(records: list[dict]) -> list[str]:
    seen: set[str] = set()
    cols: list[str] = []
    for name in _PREFERRED_COLUMNS:
        if any(name in rec for rec in records):
            cols.append(name)
            seen.add(name)
    for rec in records:
        for k in rec:
            if k in seen:
                continue
            seen.add(k)
            cols.append(k)
    return cols


def _schema_title(sample: dict) -> str:
    if "模块代码" in sample:
        return "模块/报表配置"
    if "用户组ID" in sample or "用户组名称" in sample:
        return "用户组成员"
    keys = list(sample.keys())
    return " / ".join(keys[:3]) if keys else "数据"


def _group_by_schema(records: list[dict]) -> list[tuple[str, list[str], list[dict]]]:
    buckets: dict[tuple[str, ...], list[dict]] = {}
    for rec in records:
        keys = tuple(rec.keys())
        buckets.setdefault(keys, []).append(rec)

    groups: list[tuple[str, list[str], list[dict]]] = []
    for keys, items in buckets.items():
        title = _schema_title(items[0])
        groups.append((title, list(keys), items))
    groups.sort(key=lambda x: (-len(x[2]), x[0]))
    return groups


def _table_markdown(records: list[dict], columns: list[str], max_rows: int) -> str:
    if not records:
        return "（无数据）"
    if not columns:
        return "（无有效列）"

    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    shown = records if max_rows <= 0 else records[:max_rows]
    for rec in shown:
        row = [_format_cell(rec.get(c)) for c in columns]
        lines.append("| " + " | ".join(row) + " |")

    if max_rows > 0 and len(records) > max_rows:
        lines.append("")
        lines.append(f"*共 {len(records)} 条，以下仅展示前 {max_rows} 条*")
    return "\n".join(lines)


def records_to_markdown(
    records: list[dict],
    *,
    max_rows: int = 500,
    split_by_schema: bool = True,
) -> str:
    if not records:
        return "（无数据）"

    parts: list[str] = []
    schemas = {tuple(rec.keys()) for rec in records}

    if split_by_schema and len(schemas) > 1:
        for title, columns, group in _group_by_schema(records):
            parts.append(f"### {title}（{len(group)} 条）\n")
            parts.append(_table_markdown(group, columns, max_rows))
            parts.append("")
    else:
        columns = _infer_columns(records)
        parts.append(_table_markdown(records, columns, max_rows))

    return "\n".join(parts).strip()


def main(records=None, **kwargs) -> dict:
    merged = _merge_inputs(records, kwargs)
    raw = merged.get("records", records)

    try:
        max_rows = int(merged.get("max_rows", 500))
    except (TypeError, ValueError):
        max_rows = 500

    split_raw = merged.get("split_by_schema", True)
    if isinstance(split_raw, str):
        split_by_schema = split_raw.strip().lower() not in ("0", "false", "no", "off")
    else:
        split_by_schema = bool(split_raw) if split_raw is not None else True

    try:
        parsed = _parse_records(raw)
        flat_records = records_to_flat_json(parsed)
        markdown = records_to_markdown(
            parsed,
            max_rows=max_rows,
            split_by_schema=split_by_schema,
        )
    except (json.JSONDecodeError, ValueError) as e:
        return {
            "records": "",
            "markdown": "",
            "error": str(e),
            "row_count": "0",
        }

    return {
        "records": flat_records,
        "markdown": markdown,
        "error": "",
        "row_count": str(len(parsed)),
    }


if __name__ == "__main__":
    demo_in = {
        "records": json.dumps(
            [
                json.dumps(
                    {
                        "-": True,
                        "最后修改日期": "2026-06-04 08:24:35",
                        "修改人": "余保",
                        "版本": 0,
                        "用户组名称": "成品工程师",
                        "用户组代码": "1034",
                        "用户名称": "段艳",
                        "用户账号": "005017",
                        "用户代码": "005017",
                    },
                    ensure_ascii=False,
                ),
                json.dumps(
                    {
                        "-": True,
                        "最后修改日期": "2026-06-02 16:05:39",
                        "修改人": "冯沌",
                        "版本": 0,
                        "用户组名称": "生产经理",
                        "用户组代码": "1047",
                        "用户名称": "何少华",
                        "用户账号": "005018",
                        "用户代码": "005018",
                    },
                    ensure_ascii=False,
                ),
            ],
            ensure_ascii=False,
        )
    }
    result = main(**demo_in)
    print("=== 输出 records（贴图格式）===")
    print(json.dumps({"records": result["records"]}, ensure_ascii=False, indent=2))
    print("\n=== 解析验证（loads 一次即对象数组）===")
    print(json.loads(result["records"])[0])
