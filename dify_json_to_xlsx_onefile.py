from __future__ import annotations

"""
Dify 单文件：JSON → xlsx（Base64），替代「JSON→Markdown→工具→XLSX」整条链。

- 零第三方依赖（标准库生成 OOXML）
- 报表数据：列宽、首行冻结、自动筛选；可选「维度取值参考」表
- 入口：main(inputs=..., **kwargs) → {"file","error","metadata"}

整段粘贴到 Dify 代码节点即可，无需其它 .py 文件。
"""

import base64
import json
import re
import zipfile
from io import BytesIO
from xml.sax.saxutils import escape as _xml_escape_attr  # noqa: SLF001

# OOXML 命名空间 URI（仅用于 Content_Types 等常量拼接）
_CT = "http://schemas.openxmlformats.org/package/2006/content-types"
_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def _normalize_str_list(value):
    if value is None:
        return []
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
            if isinstance(parsed, list):
                return [str(x).strip() for x in parsed if str(x).strip()]
        except json.JSONDecodeError:
            pass
        return [s.strip() for s in value.split(",") if s.strip()]
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    return []


def _infer_columns(records):
    keys = []
    seen = set()
    for rec in records:
        if not isinstance(rec, dict):
            continue
        for k in rec:
            if k not in seen:
                seen.add(k)
                keys.append(k)
    return keys


def _coerce_to_record_list(raw):
    if raw is None:
        return None, "缺少数据：请在 inputs 中传入 json_data 或 arg1"
    if isinstance(raw, list):
        return raw, None
    if isinstance(raw, dict):
        return [raw], None
    if isinstance(raw, str):
        s = raw.strip()
        if not s:
            return [], None
        try:
            parsed = json.loads(s)
        except json.JSONDecodeError as e:
            return None, f"JSON 解析失败: {e}"
        if isinstance(parsed, str):
            try:
                parsed = json.loads(parsed.strip())
            except json.JSONDecodeError as e:
                return None, f"二次 JSON 解析失败: {e}"
        if isinstance(parsed, dict):
            return [parsed], None
        if isinstance(parsed, list):
            return parsed, None
        return None, f"解析结果须为 JSON 数组或对象，当前为: {type(parsed).__name__}"
    return None, f"不支持的数据类型: {type(raw).__name__}"


def _resolve_json_payload(inputs):
    for key in ("json_data", "arg1", "data", "body"):
        if key not in inputs:
            continue
        val = inputs[key]
        if val is None:
            continue
        if isinstance(val, str) and not val.strip():
            continue
        return val, key
    return None, None


def _xlsx_bytes_to_dify_file_str(raw: bytes) -> str:
    if not raw:
        return ""
    return base64.standard_b64encode(raw).decode("ascii")


def _order_columns(metric_columns, filter_dimensions, dimensions_first):
    if not dimensions_first or not filter_dimensions:
        return list(metric_columns)
    seen = set()
    ordered = []
    for c in filter_dimensions:
        if c in metric_columns and c not in seen:
            ordered.append(c)
            seen.add(c)
    for c in metric_columns:
        if c not in seen:
            ordered.append(c)
            seen.add(c)
    return ordered


def _col_letters_1_based(n: int) -> str:
    """Excel 列号（1-based）→ 'A'、'Z'、'AA'。"""
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def _cell_ref(col_0: int, row_1: int) -> str:
    return f"{_col_letters_1_based(col_0 + 1)}{row_1}"


def _infer_col_widths_for_rows(
    rows: list[list],
    *,
    min_w: float = 10.43,
    max_w: float = 54.0,
    pad: float = 2.5,
) -> list[float] | None:
    """
    按单元格文本估算 Excel 列宽（字符量级；CJK 按约双倍计），写入 OOXML <cols> 避免表头挤在一起。
    """
    if not rows:
        return None
    ncols = len(rows[0])
    scores = [0.0] * ncols
    for row in rows:
        if not isinstance(row, (list, tuple)) or len(row) != ncols:
            continue
        for ci, val in enumerate(row):
            s = "" if val is None else str(val)
            disp = sum(2.0 if ord(c) > 127 else 1.0 for c in s)
            scores[ci] = max(scores[ci], disp)
    out: list[float] = []
    for s in scores:
        w = min(max_w, max(min_w, s * 0.95 + pad))
        out.append(round(w, 2))
    return out


def _cols_xml_fragment(col_widths: list[float]) -> str:
    parts = ["<cols>"]
    for i, w in enumerate(col_widths, start=1):
        parts.append(f'<col min="{i}" max="{i}" width="{w}" customWidth="1"/>')
    parts.append("</cols>")
    return "".join(parts)


def _xml_cell_text(value) -> str:
    if value is None:
        return ""
    s = str(value)
    s = "".join(c for c in s if ord(c) >= 32 or c in "\t\n\r")
    return _xml_escape_attr(s, {"\n": "&#10;", "\r": "&#13;", "\t": "&#9;"})


def _worksheet_xml(
    rows: list[list],
    *,
    auto_filter_ref: str | None,
    freeze_top_row: bool,
    col_widths: list[float] | None = None,
) -> str:
    """rows: 矩形（每行列数一致）；单元格一律 inlineStr，避免大整数精度问题。"""
    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        f'<worksheet xmlns="{_MAIN}" xmlns:r="{_R}">',
    ]
    if freeze_top_row:
        parts.append(
            "<sheetViews>"
            '<sheetView workbookViewId="0">'
            '<pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/>'
            "</sheetView>"
            "</sheetViews>"
        )
    if rows:
        ncols = len(rows[0])
        nrows = len(rows)
        parts.append(
            f'<dimension ref="A1:{_cell_ref(ncols - 1, nrows)}"/>'
        )
        if col_widths is not None and len(col_widths) == ncols:
            parts.append(_cols_xml_fragment(col_widths))
    parts.append("<sheetData>")
    for ri, row in enumerate(rows, start=1):
        parts.append(f'<row r="{ri}">')
        for ci, val in enumerate(row):
            ref = _cell_ref(ci, ri)
            tx = _xml_cell_text(val)
            parts.append(
                f'<c r="{ref}" t="inlineStr"><is><t xml:space="preserve">{tx}</t></is></c>'
            )
        parts.append("</row>")
    parts.append("</sheetData>")
    if auto_filter_ref:
        parts.append(f'<autoFilter ref="{auto_filter_ref}"/>')
    parts.append("</worksheet>")
    return "".join(parts)


def _safe_sheet_name(name: str, default: str = "Sheet") -> str:
    name = re.sub(r'[\[\]\\/*?:]', "_", name).strip() or default
    return name[:31]


_STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="1"><font><sz val="11"/><color theme="1"/><name val="Calibri"/><family val="2"/></font></fonts>
  <fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>
  <borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
  <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
  <cellXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/></cellXfs>
  <cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>"""


def _build_xlsx_bytes(
    *,
    sheet_data_name: str,
    data_rows: list[list],
    data_autofilter: bool,
    auto_column_width: bool = True,
) -> bytes:
    sheet_data_name = _safe_sheet_name(sheet_data_name, "报表数据")

    ncols = len(data_rows[0]) if data_rows else 1
    nrows = len(data_rows)
    af_ref = None
    if data_autofilter and nrows >= 1 and ncols >= 1:
        af_ref = f"A1:{_cell_ref(ncols - 1, nrows)}"

    data_w = _infer_col_widths_for_rows(data_rows) if auto_column_width else None
    ws_data = _worksheet_xml(
        data_rows,
        auto_filter_ref=af_ref,
        freeze_top_row=bool(data_rows),
        col_widths=data_w,
    )

    esc_data = _xml_escape_attr(sheet_data_name)
    wb_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="{_MAIN}" xmlns:r="{_R}">
  <workbookPr/>
  <sheets>
    <sheet name="{esc_data}" sheetId="1" r:id="rId1"/>
  </sheets>
</workbook>"""

    wb_rels = f"""<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="{_REL}">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

    root_rels = f"""<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="{_REL}">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""

    content_types = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="{_CT}">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>"""

    buf = BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", root_rels)
        zf.writestr("xl/workbook.xml", wb_xml)
        zf.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        zf.writestr("xl/styles.xml", _STYLES_XML)
        zf.writestr("xl/worksheets/sheet1.xml", ws_data)
    buf.seek(0)
    return buf.getvalue()


def _merge_inputs(inputs: dict | str | None, kwargs: dict) -> dict:
    """合并 Dify / 工作流传入的 inputs 与关键字参数。"""
    merged: dict = {}
    raw = inputs
    if isinstance(raw, str):
        s = raw.strip()
        if s.startswith("{"):
            try:
                raw = json.loads(s)
            except json.JSONDecodeError:
                raw = None
    if isinstance(raw, dict):
        merged.update(raw)
        inner = raw.get("inputs")
        if isinstance(inner, dict):
            merged.update(inner)
    merged.update(kwargs)
    inner2 = merged.get("inputs")
    if isinstance(inner2, dict):
        merged.update(inner2)
    return merged


def _boolish(val, default: bool = False) -> bool:
    if val is None:
        return default
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val)
    s = str(val).strip().lower()
    if not s:
        return default
    return s in ("1", "true", "yes", "y", "on")


def _unique_values_for_dimension(records: list, col: str, max_values: int) -> list:
    out: list = []
    seen: set[str] = set()
    for rec in records:
        if not isinstance(rec, dict):
            continue
        v = rec.get(col)
        key = "" if v is None else str(v)
        if key in seen:
            continue
        seen.add(key)
        out.append(v if v is not None else "")
        if len(out) >= max_values:
            break
    return out


def _aux_dimension_rows(dimensions: list[str], records: list, max_per_dim: int) -> list[list]:
    pairs: list[tuple[str, list]] = []
    for d in dimensions:
        pairs.append((d, _unique_values_for_dimension(records, d, max_per_dim)))
    if not pairs:
        return []
    max_len = max(len(vals) for _, vals in pairs)
    rows: list[list] = [[p[0] for p in pairs]]
    for i in range(max_len):
        row = []
        for _, vals in pairs:
            row.append(vals[i] if i < len(vals) else "")
        rows.append(row)
    return rows


def _build_xlsx_with_optional_aux(
    *,
    sheet_data_name: str,
    data_rows: list[list],
    data_autofilter: bool,
    aux_name: str | None,
    aux_rows: list[list] | None,
    auto_column_width: bool = True,
) -> bytes:
    if not aux_rows:
        return _build_xlsx_bytes(
            sheet_data_name=sheet_data_name,
            data_rows=data_rows,
            data_autofilter=data_autofilter,
            auto_column_width=auto_column_width,
        )

    sheet_data_name = _safe_sheet_name(sheet_data_name, "报表数据")
    aux_sheet = _safe_sheet_name(aux_name or "维度取值参考", "维度取值参考")
    if sheet_data_name == aux_sheet:
        aux_sheet = (aux_sheet[:28] + "_2")[:31]

    ncols = len(data_rows[0]) if data_rows else 1
    nrows = len(data_rows)
    af_ref = None
    if data_autofilter and nrows >= 1 and ncols >= 1:
        af_ref = f"A1:{_cell_ref(ncols - 1, nrows)}"

    data_w = _infer_col_widths_for_rows(data_rows) if auto_column_width else None
    aux_w = _infer_col_widths_for_rows(aux_rows) if auto_column_width else None
    ws_data = _worksheet_xml(
        data_rows,
        auto_filter_ref=af_ref,
        freeze_top_row=bool(data_rows),
        col_widths=data_w,
    )
    ws_aux = _worksheet_xml(
        aux_rows, auto_filter_ref=None, freeze_top_row=bool(aux_rows), col_widths=aux_w
    )

    esc_data = _safe_sheet_name(sheet_data_name, "报表数据")
    esc_aux = _safe_sheet_name(aux_sheet, "维度取值参考")
    ed = _xml_escape_attr(esc_data)
    ea = _xml_escape_attr(esc_aux)

    wb_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="{_MAIN}" xmlns:r="{_R}">
  <workbookPr/>
  <sheets>
    <sheet name="{ed}" sheetId="1" r:id="rId1"/>
    <sheet name="{ea}" sheetId="2" r:id="rId2"/>
  </sheets>
</workbook>"""

    wb_rels = f"""<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="{_REL}">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

    root_rels = f"""<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="{_REL}">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""

    content_types = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="{_CT}">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>"""

    buf = BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", root_rels)
        zf.writestr("xl/workbook.xml", wb_xml)
        zf.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        zf.writestr("xl/styles.xml", _STYLES_XML)
        zf.writestr("xl/worksheets/sheet1.xml", ws_data)
        zf.writestr("xl/worksheets/sheet2.xml", ws_aux)
    buf.seek(0)
    return buf.getvalue()


def main(inputs=None, **kwargs):
    """
    Dify 代码节点入口：JSON 记录列表 → 数据表 xlsx。

    输入（与 json_to_table 一致，支持 json_data / arg1 / data / body）：
      - json_data / arg1: JSON 数组或对象，或 JSON 字符串
      - metric_columns: 要输出的指标列名列表；留空则全部列
      - filter_dimensions: 维度列（须在 metric_columns 中）；留空则与指标列相同
      - dimensions_first: 是否把 filter_dimensions 中的列排在表头前面（默认 true）
      - sheet_name: 数据工作表名称（默认「报表数据」）
      - report_title: 仅写入 metadata，不出现在 xlsx 中
      - include_unique_values: 是否增加「维度取值参考」表（默认 false）
      - unique_values_max: 每个维度最多列出的不同取值条数（默认 5000）
      - auto_column_width: 是否按内容估算列宽（默认 true），减轻表头挤在一起

    输出（建议在 Dify 中声明为字符串）：
      - file: xlsx 的 Base64
      - error: 失败原因；成功为空字符串
      - metadata: JSON 字符串（列信息、行数、实际选用的指标与维度等）
    """
    merged = _merge_inputs(inputs, kwargs)

    raw_payload, used_key = _resolve_json_payload(merged)
    json_data, parse_err = _coerce_to_record_list(raw_payload)
    if parse_err:
        return {"file": "", "error": parse_err, "metadata": ""}

    acw = _boolish(merged.get("auto_column_width", True), True)

    empty_data = [
        ["（无数据）请在流程中传入非空的 json_data 或 arg1（JSON 数组）。"],
    ]
    empty_ret = {
        "file": _xlsx_bytes_to_dify_file_str(
            _build_xlsx_bytes(
                sheet_data_name="报表数据",
                data_rows=empty_data,
                data_autofilter=False,
                auto_column_width=acw,
            )
        ),
        "error": "",
        "metadata": json.dumps(
            {
                "payload_key": used_key or "",
                "row_count": 0,
                "all_columns": [],
                "metric_columns": [],
                "filter_dimensions": [],
                "ordered_columns": [],
            },
            ensure_ascii=False,
        ),
    }

    if not json_data:
        return empty_ret

    all_cols = _infer_columns(json_data)
    col_set = set(all_cols)
    metric_columns = _normalize_str_list(merged.get("metric_columns"))
    if not metric_columns:
        metric_columns = list(all_cols)

    metric_columns = [c for c in metric_columns if c in col_set]
    if not metric_columns:
        return {
            "file": "",
            "error": "未找到与数据列交集的指标列（metric_columns），请检查列名或留空以使用全部列。",
            "metadata": "",
        }

    filter_dimensions = _normalize_str_list(merged.get("filter_dimensions"))
    if not filter_dimensions:
        filter_dimensions = list(metric_columns)

    filter_dimensions = [c for c in filter_dimensions if c in col_set]
    filter_dimensions = [c for c in filter_dimensions if c in metric_columns]
    if not filter_dimensions:
        filter_dimensions = list(metric_columns)

    dimensions_first = _boolish(merged.get("dimensions_first", True), True)
    ordered_metrics = _order_columns(metric_columns, filter_dimensions, dimensions_first)

    sheet_name = (merged.get("sheet_name") or "报表数据").strip()[:31] or "报表数据"
    report_title = (merged.get("report_title") or "指标与维度报表模板").strip()

    include_uv = _boolish(merged.get("include_unique_values"), False)
    try:
        uv_max = int(merged.get("unique_values_max") or 5000)
    except (TypeError, ValueError):
        uv_max = 5000
    uv_max = max(1, min(uv_max, 20000))

    aux_rows = None
    aux_sheet_name = None
    if include_uv and filter_dimensions:
        aux_rows = _aux_dimension_rows(filter_dimensions, json_data, uv_max)
        aux_sheet_name = (merged.get("aux_sheet_name") or "维度取值参考").strip()[:31] or "维度取值参考"

    data_rows: list[list] = [list(ordered_metrics)]
    for rec in json_data:
        row = rec if isinstance(rec, dict) else {}
        data_rows.append([row.get(k) for k in ordered_metrics])

    raw = _build_xlsx_with_optional_aux(
        sheet_data_name=sheet_name,
        data_rows=data_rows,
        data_autofilter=True,
        aux_name=aux_sheet_name,
        aux_rows=aux_rows,
        auto_column_width=acw,
    )

    meta_obj = {
        "payload_key": used_key or "",
        "row_count": len(json_data),
        "all_columns": all_cols,
        "metric_columns": metric_columns,
        "filter_dimensions": filter_dimensions,
        "ordered_columns": ordered_metrics,
        "sheet_name": sheet_name,
        "report_title": report_title,
        "include_unique_values": bool(aux_rows),
        "unique_values_max": uv_max if include_uv else 0,
        "auto_column_width": acw,
    }
    return {
        "file": _xlsx_bytes_to_dify_file_str(raw),
        "error": "",
        "metadata": json.dumps(meta_obj, ensure_ascii=False),
    }


if __name__ == "__main__":
    demo = [
        {"地区": "华东", "产品": "A", "销售额": 100, "利润": 10},
        {"地区": "华北", "产品": "B", "销售额": 200, "利润": 20},
    ]
    r = main(
        inputs={
            "json_data": demo,
            "metric_columns": ["地区", "产品", "销售额", "利润"],
            "filter_dimensions": ["地区", "产品"],
            "include_unique_values": True,
        }
    )
    print("error:", r.get("error"))
    print("metadata:", r.get("metadata"))
    print("file len:", len(r.get("file") or ""))
