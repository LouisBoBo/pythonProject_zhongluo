#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dify「代码」节点：表结构审核（命名、字段类型、主外键、索引 + 注释/MES 标准等辅审）。

Dify 输入变量：
  - schema_data：dify_get_db_scheme 输出的 JSON 字符串（必填）
  - rules_yaml：可选，规则 YAML 全文；本地调试自动加载同目录文件

Dify 输出变量（均须在节点中声明为 String）：
  - result、message、audit_result、audit_score、audit_date、violations_json
  - 封面「合规得分」绑 audit_score；「审核日期」绑 audit_date（或读 violations_json.summary.audit_date）
"""

from __future__ import annotations

import json
import re
import traceback
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    ROOT = Path(__file__).resolve().parent
except NameError:
    ROOT = Path(".")

DEFAULT_RULES_FILE = ROOT / "mes_db_schema_audit_rules.yaml"

_RESULT_PASS = "通过"
_RESULT_FAIL = "不通过"
_SCRIPT_VERSION = "2.1.0"
_MAX_VIOLATIONS_JSON_LEN = 50_000
_MAX_MESSAGE_LEN = 2500

# Dify 出参（模块级变量）
result = "失败"
message = ""
audit_result = "不通过"
audit_score = "0"
score = "0"  # 与 audit_score 相同，供模板绑定 {{score}}
audit_date = ""
violations_json = "{}"


def _merge_inputs(
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    merged: Dict[str, Any] = {}
    allow = frozenset({"schema_data", "rules_yaml", "rules", "audit_date"})

    def _pick(data: Dict[str, Any]) -> None:
        for k, v in data.items():
            if str(k).startswith("sys."):
                continue
            if k in allow and v not in (None, ""):
                merged[k] = v

    if inputs and isinstance(inputs, dict):
        _pick(inputs)
        inner = inputs.get("inputs")
        if isinstance(inner, dict):
            _pick(inner)
    _pick(kwargs)
    inner2 = merged.get("inputs")
    if isinstance(inner2, dict):
        _pick(inner2)
    return merged


def _parse_bool(value: Any, default: bool = True) -> bool:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return value
    s = str(value).strip().lower()
    return s in ("1", "true", "yes", "y", "是", "on")


def _load_yaml_simple(text: str) -> Dict[str, Any]:
    """轻量 YAML 解析，仅支持本规则文件结构（无 PyYAML 依赖）。"""
    try:
        import yaml  # type: ignore

        return yaml.safe_load(text) or {}
    except ImportError:
        pass

    # 回退：仅解析 rules 列表中的 id/severity 等关键项 + 顶层列表
    data: Dict[str, Any] = {
        "exclude_table_patterns": [],
        "link_table_suffixes": [],
        "column_name_exceptions": [],
        "rules": [],
        "scoring": {
            "error_penalty": 10,
            "warning_penalty": 3,
            "info_penalty": 0,
            "pass_max_errors": 0,
            "max_warning_penalty": 45,
            "min_score_when_pass": 60,
        },
    }
    section = None
    current_rule: Optional[Dict[str, Any]] = None
    list_key = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.strip().startswith("#"):
            continue
        if line.startswith("meta:"):
            section = "meta"
            continue
        if line.startswith("exclude_table_patterns:"):
            section = "exclude_table_patterns"
            list_key = "exclude_table_patterns"
            continue
        if line.startswith("link_table_suffixes:"):
            section = "link_table_suffixes"
            list_key = "link_table_suffixes"
            continue
        if line.startswith("column_name_exceptions:"):
            section = "column_name_exceptions"
            list_key = "column_name_exceptions"
            continue
        if line.startswith("rules:"):
            section = "rules"
            continue
        if line.startswith("scoring:"):
            section = "scoring"
            continue

        if section in (
            "exclude_table_patterns",
            "link_table_suffixes",
            "column_name_exceptions",
        ):
            m = re.match(r'^\s+-\s+"(.*)"\s*$', line)
            if m and list_key:
                data[list_key].append(m.group(1))
            continue

        if section == "rules":
            if re.match(r"^\s+- id:", line):
                if current_rule:
                    data["rules"].append(current_rule)
                current_rule = {"id": line.split(":", 1)[1].strip()}
            elif current_rule is not None and ":" in line:
                k, v = line.strip().split(":", 1)
                k = k.strip()
                v = v.strip().strip('"')
                if v.startswith("[") and v.endswith("]"):
                    current_rule[k] = [
                        x.strip().strip('"') for x in v[1:-1].split(",") if x.strip()
                    ]
                elif v.isdigit():
                    current_rule[k] = int(v)
                elif v in ("true", "false"):
                    current_rule[k] = v == "true"
                else:
                    current_rule[k] = v
            continue

        if section == "scoring" and ":" in line:
            k, v = line.strip().split(":", 1)
            data["scoring"][k.strip()] = int(v.strip())

    if current_rule:
        data["rules"].append(current_rule)
    return data


def _load_rules(merged: Dict[str, Any]) -> Dict[str, Any]:
    raw = merged.get("rules_yaml") or merged.get("rules")
    if raw:
        text = raw if isinstance(raw, str) else json.dumps(raw)
        return _load_yaml_simple(text)
    if DEFAULT_RULES_FILE.is_file():
        return _load_yaml_simple(DEFAULT_RULES_FILE.read_text(encoding="utf-8"))
    raise FileNotFoundError("未找到规则文件 mes_db_schema_audit_rules.yaml")


_CATEGORY_KEYS = (
    "naming",
    "datatype",
    "constraint",
    "index",
    "integrity",
    "documentation",
    "mes_standard",
    "governance",
    "design",
)

_SEV_ORDER = {"error": 0, "warning": 1, "info": 2}
_CAT_ORDER = {name: i for i, name in enumerate(_CATEGORY_KEYS)}


def _sort_violations(violations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """级别 → 分类 → 规则 → 表 → 字段，保证汇总表同类连续。"""

    def _key(v: Dict[str, Any]) -> Tuple[int, int, int, str, str, str]:
        sev = _SEV_ORDER.get(str(v.get("severity") or "info"), 9)
        cat = _CAT_ORDER.get(str(v.get("category") or "design"), 99)
        col = str(v.get("column") or "").strip()
        # 表级（无字段）排在同分类字段项之前，如 TABLE_COMMENT 在 COLUMN_COMMENT 前
        col_rank = 0 if not col else 1
        return (
            sev,
            cat,
            col_rank,
            str(v.get("rule_id") or ""),
            str(v.get("table") or ""),
            col,
        )

    return sorted(violations, key=_key)


def _stats_by_category(violations: List[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    """按 category × severity 汇总，供报告模板 {naming_error} 等占位符使用。"""
    stats: Dict[str, Dict[str, int]] = {
        c: {"error": 0, "warning": 0, "info": 0, "total": 0} for c in _CATEGORY_KEYS
    }
    for v in violations:
        cat = str(v.get("category") or "design")
        if cat not in stats:
            stats[cat] = {"error": 0, "warning": 0, "info": 0, "total": 0}
        sev = str(v.get("severity") or "info")
        if sev not in ("error", "warning", "info"):
            sev = "info"
        stats[cat][sev] += 1
        stats[cat]["total"] += 1
    return stats


def _resolve_audit_date(merged: Optional[Dict[str, Any]] = None) -> str:
    raw = ""
    if merged:
        raw = str(merged.get("audit_date") or "").strip()
    if not raw:
        g = globals()
        raw = str(g.get("audit_date") or "").strip()
    if raw:
        return raw[:10]
    return date.today().isoformat()


def _build_violations_json(
    schema: Dict[str, Any],
    auditor: "SchemaAuditor",
    counts: Dict[str, int],
    audit_date_str: str,
) -> str:
    sorted_violations = _sort_violations(auditor.violations)
    by_cat = _stats_by_category(sorted_violations)
    total = counts["error"] + counts["warning"] + counts["info"]
    payload = {
        "summary": {
            "server": schema.get("server"),
            "port": schema.get("port"),
            "database": schema.get("database"),
            "schema": schema.get("schema"),
            "table_count": len(schema.get("tables") or []),
            "scan_mode": schema.get("scan_mode") or "filtered",
            "result": _RESULT_PASS if auditor.passed() else _RESULT_FAIL,
            "score": auditor.score(),
            "score_breakdown": auditor.score_breakdown(),
            "audit_date": audit_date_str,
            "error": counts["error"],
            "warning": counts["warning"],
            "info": counts["info"],
            "total": total,
            "by_category": by_cat,
        },
        "violations": sorted_violations,
    }
    text = json.dumps(payload, ensure_ascii=False)
    if len(text) > _MAX_VIOLATIONS_JSON_LEN:
        text = text[:_MAX_VIOLATIONS_JSON_LEN] + "...(violations_json 已截断)"
    return text


def _short_log(log: List[str], limit: int = 8) -> List[str]:
    return log[-limit:] if len(log) > limit else log


def _fail_output(log: List[str], audit_date_str: str = "") -> Dict[str, Any]:
    brief = _short_log(log)
    ad = audit_date_str or date.today().isoformat()
    payload = {
        "summary": {
            "result": _RESULT_FAIL,
            "score": 0,
            "audit_date": ad,
            "error": brief[-1] if brief else "",
        },
        "violations": [],
    }
    vj = json.dumps(payload, ensure_ascii=False)
    if len(vj) > _MAX_VIOLATIONS_JSON_LEN:
        vj = vj[:_MAX_VIOLATIONS_JSON_LEN]
    msg = "\n".join(brief)
    if len(msg) > _MAX_MESSAGE_LEN:
        msg = msg[:_MAX_MESSAGE_LEN] + "\n...(截断)"
    return {
        "result": "失败",
        "message": msg,
        "audit_result": _RESULT_FAIL,
        "audit_score": "0",
        "score": "0",
        "audit_date": ad,
        "violations_json": vj,
    }


def _parse_schema_data(raw: Any) -> Dict[str, Any]:
    """兼容 Dify 传入：纯 JSON 字符串、整包采集节点输出、或 dict。"""
    if raw is None or raw == "":
        raise ValueError("缺少 schema_data")
    if isinstance(raw, dict):
        if "tables" in raw:
            return raw
        if "schema_data" in raw:
            return _parse_schema_data(raw["schema_data"])
        raise ValueError("schema_data 中无 tables 字段，请绑定采集节点的 schema_data 字段")

    if isinstance(raw, str):
        s = raw.strip()
        if s.startswith("```"):
            s = re.sub(r"^```(?:json)?\s*", "", s, flags=re.I)
            s = re.sub(r"\s*```\s*$", "", s).strip()
        last_err: Optional[Exception] = None
        for _ in range(4):
            if not s or s[0] not in "{[":
                break
            try:
                obj = json.loads(s)
            except json.JSONDecodeError as e:
                last_err = e
                break
            if isinstance(obj, dict):
                if "tables" in obj:
                    return obj
                if "schema_data" in obj:
                    inner = obj["schema_data"]
                    if isinstance(inner, dict):
                        return inner
                    if isinstance(inner, str):
                        s = inner.strip()
                        continue
                raise ValueError(
                    "schema_data 不是表结构 JSON。请绑定「采集表结构.schema_data」，"
                    "不要绑定整段 message 或 result。"
                )
            break
        raise ValueError(
            f"schema_data 无法解析为 JSON: {last_err}"
            if last_err
            else "schema_data 内容不是合法 JSON 对象"
        )

    raise TypeError(f"schema_data 类型不支持: {type(raw)}")


def _match_any(name: str, patterns: List[str]) -> bool:
    for p in patterns:
        if re.search(p, name, re.IGNORECASE):
            return True
    return False


def _is_excluded(table: str, rules_cfg: Dict[str, Any]) -> bool:
    return _match_any(table, rules_cfg.get("exclude_table_patterns") or [])


def _is_link_table(table: str, rules_cfg: Dict[str, Any]) -> bool:
    suffixes = rules_cfg.get("link_table_suffixes") or []
    return any(table.upper().endswith(s.upper()) for s in suffixes)


def _table_prefix_match(table: str, prefixes: List[str]) -> bool:
    return any(table.upper().startswith(p.upper()) for p in prefixes)


def _base_type(type_str: str) -> str:
    return str(type_str or "").split()[0].upper()


def _col_by_name(columns: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {c.get("name"): c for c in columns if c.get("name")}


def _is_max_char_type(type_str: str) -> bool:
    u = str(type_str or "").upper()
    return "MAX" in u


def _index_covers_columns(index_cols: List[str], target: List[str]) -> bool:
    if not target or not index_cols:
        return False
    if len(index_cols) < len(target):
        return False
    return list(index_cols[: len(target)]) == list(target)


class SchemaAuditor:
    def __init__(
        self,
        schema: Dict[str, Any],
        rules_cfg: Dict[str, Any],
    ) -> None:
        self.schema = schema
        self.rules_cfg = rules_cfg
        self.violations: List[Dict[str, Any]] = []
        self.db_tables: Dict[str, Dict[str, Any]] = {
            t["name"]: t for t in schema.get("tables") or [] if t.get("name")
        }
        self.col_exceptions = set(rules_cfg.get("column_name_exceptions") or [])
        self.scoring = rules_cfg.get("scoring") or {}

    def _add(
        self,
        rule_id: str,
        severity: str,
        category: str,
        message: str,
        table: str = "",
        column: str = "",
    ) -> None:
        self.violations.append(
            {
                "rule_id": rule_id,
                "severity": severity,
                "category": category,
                "table": table,
                "column": column,
                "message": message,
            }
        )

    def audit_all(self) -> None:
        for table_name, table in self.db_tables.items():
            excluded = _is_excluded(table_name, self.rules_cfg)
            link = _is_link_table(table_name, self.rules_cfg)
            self._audit_table_structure(table_name, table, excluded, link)
            if not excluded:
                self._audit_fk_and_indexes(table_name, table, link)

    def _audit_table_structure(
        self,
        table_name: str,
        table: Dict[str, Any],
        excluded: bool,
        link: bool,
    ) -> None:
        columns = table.get("columns") or []
        col_map = _col_by_name(columns)
        col_names = list(col_map.keys())
        pks = table.get("primary_keys") or []
        fk_cols: Set[str] = set()
        for fk in table.get("foreign_keys") or []:
            for c in fk.get("constrained_columns") or []:
                fk_cols.add(c)

        if len(col_names) != len(columns):
            self._add(
                "DUPLICATE_COLUMN_NAME",
                "error",
                "design",
                f"表 {table_name} 存在重复字段名",
                table_name,
            )

        if not pks:
            self._add(
                "PK_REQUIRED",
                "error",
                "integrity",
                f"表 {table_name} 未定义主键",
                table_name,
            )

        if not excluded:
            if len(columns) < 2:
                self._add(
                    "MIN_COLUMN_COUNT",
                    "warning",
                    "design",
                    f"表 {table_name} 仅 {len(columns)} 个字段",
                    table_name,
                )

            if not (table.get("comment") or "").strip():
                self._add(
                    "TABLE_COMMENT_REQUIRED",
                    "warning",
                    "documentation",
                    f"表 {table_name} 缺少表级中文注释",
                    table_name,
                )

            for col in columns:
                cname = col.get("name") or ""
                if not (col.get("comment") or "").strip():
                    self._add(
                        "COLUMN_COMMENT_REQUIRED",
                        "warning",
                        "documentation",
                        f"字段 {table_name}.{cname} 缺少注释",
                        table_name,
                        cname,
                    )

                if cname and cname not in self.col_exceptions:
                    if not re.match(r"^(C[A-Z0-9_]+|[A-Z][A-Z0-9_]*)$", cname):
                        self._add(
                            "COLUMN_NAME_FORMAT",
                            "warning",
                            "naming",
                            f"字段名 {table_name}.{cname} 不符合 MES 命名习惯",
                            table_name,
                            cname,
                        )

                ctype = str(col.get("type", ""))
                base = _base_type(ctype)
                if base in ("VARCHAR", "NVARCHAR", "CHAR", "NCHAR") and "(" not in ctype:
                    self._add(
                        "VARCHAR_NEED_LENGTH",
                        "warning",
                        "datatype",
                        f"字段 {table_name}.{cname} 类型 {ctype} 未声明长度",
                        table_name,
                        cname,
                    )
                if base in ("VARCHAR", "NVARCHAR") and _is_max_char_type(ctype):
                    self._add(
                        "VARCHAR_MAX_ABUSE",
                        "warning",
                        "datatype",
                        f"字段 {table_name}.{cname} 使用 MAX 长度，建议按业务限定长度",
                        table_name,
                        cname,
                    )
                if base == "DATETIME":
                    self._add(
                        "DATETIME_LEGACY",
                        "info",
                        "datatype",
                        f"字段 {table_name}.{cname} 建议改用 DATETIME2 提升精度",
                        table_name,
                        cname,
                    )
                if base in ("FLOAT", "REAL") and (cname in pks or cname in fk_cols):
                    self._add(
                        "FLOAT_FOR_KEY",
                        "warning",
                        "datatype",
                        f"主键/外键字段 {table_name}.{cname} 不建议使用 {base}",
                        table_name,
                        cname,
                    )
                if base in ("MONEY", "SMALLMONEY"):
                    self._add(
                        "MONEY_USE_DECIMAL",
                        "info",
                        "datatype",
                        f"金额字段 {table_name}.{cname} 建议使用 DECIMAL(p,s)",
                        table_name,
                        cname,
                    )

        if len(pks) > 3:
            self._add(
                "PK_COMPOSITE_MANY",
                "info",
                "constraint",
                f"表 {table_name} 复合主键含 {len(pks)} 列，建议评估是否过宽",
                table_name,
            )

        if not re.match(r"^(TBL_[A-Z0-9_]+|VW_[A-Z0-9_]+|VM_[A-Z0-9_]+)$", table_name):
            self._add(
                "TABLE_NAME_FORMAT",
                "warning",
                "naming",
                f"表名 {table_name} 未使用 TBL_/VW_/VM_ 规范前缀",
                table_name,
            )

        if _match_any(table_name, ["TEST", "_BAK", "_TEMP", "_TMP"]):
            self._add(
                "RESERVED_TEST_NAME",
                "warning",
                "governance",
                f"表名 {table_name} 疑似测试/临时/备份对象",
                table_name,
            )

        if not link and not excluded and table_name.upper().startswith("TBL_"):
            if pks and "CID" not in pks:
                self._add(
                    "PK_PREFER_CID",
                    "info",
                    "naming",
                    f"表 {table_name} 主键为 {','.join(pks)}，非惯用 CID",
                    table_name,
                )
            elif not pks:
                pass
            elif "CID" not in col_names:
                self._add(
                    "STD_FIELD_CID",
                    "info",
                    "mes_standard",
                    f"表 {table_name} 未包含 CID 字段",
                    table_name,
                )

            self._check_std_fields(table_name, col_names, link)

    def _audit_fk_and_indexes(
        self,
        table_name: str,
        table: Dict[str, Any],
        link: bool,
    ) -> None:
        col_map = _col_by_name(table.get("columns") or [])
        pks = table.get("primary_keys") or []
        indexes = table.get("indexes") or []

        for pk_col in pks:
            col = col_map.get(pk_col)
            if col and col.get("nullable", True):
                self._add(
                    "PK_NULLABLE",
                    "error",
                    "constraint",
                    f"主键字段 {table_name}.{pk_col} 不允许为空",
                    table_name,
                    pk_col,
                )

        seen_index_keys: Set[Tuple[str, ...]] = set()
        for ix in indexes:
            ix_cols = list(ix.get("columns") or [])
            ix_name = ix.get("name") or ""
            for c in ix_cols:
                if c not in col_map:
                    self._add(
                        "INDEX_UNKNOWN_COLUMN",
                        "error",
                        "index",
                        f"索引 {ix_name} 引用不存在的字段 {table_name}.{c}",
                        table_name,
                        c,
                    )
            if ix_name and not re.match(
                r"^(PK_|FK_|IDX_|UK_|IX_)", str(ix_name), re.IGNORECASE
            ):
                self._add(
                    "INDEX_NAMING_FORMAT",
                    "warning",
                    "index",
                    f"索引 {table_name}.{ix_name} 建议以 PK_/FK_/IDX_/UK_/IX_ 命名",
                    table_name,
                )
            if ix_cols:
                key = tuple(ix_cols)
                if key in seen_index_keys:
                    self._add(
                        "INDEX_DUPLICATE_COLUMNS",
                        "warning",
                        "index",
                        f"表 {table_name} 存在列组合重复的索引: {', '.join(ix_cols)}",
                        table_name,
                    )
                else:
                    seen_index_keys.add(key)

        non_pk_indexes = [
            ix
            for ix in indexes
            if tuple(ix.get("columns") or []) != tuple(pks)
        ]
        if len(non_pk_indexes) > 10:
            self._add(
                "INDEX_TOO_MANY",
                "warning",
                "index",
                f"表 {table_name} 非主键索引达 {len(non_pk_indexes)} 个，建议合并或清理冗余",
                table_name,
            )

        for fk in table.get("foreign_keys") or []:
            fk_name = fk.get("name") or ""
            constrained = list(fk.get("constrained_columns") or [])
            referred_table = fk.get("referred_table") or ""

            if fk_name and not re.match(r"^FK_", str(fk_name), re.IGNORECASE):
                self._add(
                    "FK_NAMING_FORMAT",
                    "info",
                    "constraint",
                    f"外键 {fk_name} 建议以 FK_ 前缀命名",
                    table_name,
                )

            for c in constrained:
                if c not in col_map:
                    self._add(
                        "FK_COLUMN_MISSING",
                        "error",
                        "constraint",
                        f"外键 {fk_name} 引用本表不存在的字段 {c}",
                        table_name,
                        c,
                    )

            if (
                referred_table
                and referred_table not in self.db_tables
                and not _is_excluded(referred_table, self.rules_cfg)
            ):
                self._add(
                    "FK_REF_TABLE_NOT_SCANNED",
                    "info",
                    "constraint",
                    f"外键 {table_name}.{fk_name or '-'} 指向 {referred_table}，本次未采集该表",
                    table_name,
                )

            if constrained and not link:
                covered = any(
                    _index_covers_columns(list(ix.get("columns") or []), constrained)
                    for ix in indexes
                )
                if not covered:
                    self._add(
                        "FK_NO_INDEX",
                        "warning",
                        "index",
                        f"外键列 {table_name}({','.join(constrained)}) 缺少覆盖索引，影响关联查询性能",
                        table_name,
                        constrained[0] if constrained else "",
                    )

        col_names = list(col_map.keys())
        if pks and not link and len(col_names) > 5:
            status_cols = {"CSTATE", "CSTATUS", "CIS_ACTIVE", "CIS_DELETE", "CIS_VALID"}
            if not (set(col_names) & status_cols) and table_name.upper().startswith("TBL_"):
                self._add(
                    "STATUS_FIELD_SUGGEST",
                    "info",
                    "mes_standard",
                    f"业务表 {table_name} 建议包含状态字段（如 CSTATE）",
                    table_name,
                )

    def _check_std_fields(self, table_name: str, col_names: List[str], link: bool) -> None:
        if link:
            return
        col_set = set(col_names)
        for rule in self.rules_cfg.get("rules") or []:
            rid = rule.get("id", "")
            if not rid.startswith("STD_FIELD_"):
                continue
            prefixes = rule.get("table_prefixes")
            if prefixes and not _table_prefix_match(table_name, prefixes):
                continue
            fields = rule.get("fields")
            if fields:
                missing = [f for f in fields if f not in col_set]
                if missing and rule.get("require_all", False):
                    self._add(
                        rid,
                        rule.get("severity", "info"),
                        rule.get("category", "mes_standard"),
                        f"表 {table_name} 缺少标准字段: {', '.join(missing)}",
                        table_name,
                    )
                elif len(missing) == len(fields):
                    self._add(
                        rid,
                        rule.get("severity", "info"),
                        rule.get("category", "mes_standard"),
                        f"表 {table_name} 建议包含: {', '.join(fields)}",
                        table_name,
                    )
            elif rule.get("field") and rule.get("field") not in col_set:
                self._add(
                    rid,
                    rule.get("severity", "info"),
                    rule.get("category", "mes_standard"),
                    f"表 {table_name} 缺少字段 {rule.get('field')}",
                    table_name,
                )


    def score(self) -> int:
        err_p = int(self.scoring.get("error_penalty", 10))
        warn_p = int(self.scoring.get("warning_penalty", 3))
        max_warn = int(self.scoring.get("max_warning_penalty", 45))
        min_pass = int(self.scoring.get("min_score_when_pass", 60))
        counts = {"error": 0, "warning": 0, "info": 0}
        for v in self.violations:
            sev = v.get("severity", "info")
            counts[sev] = counts.get(sev, 0) + 1
        err_ded = counts["error"] * err_p
        warn_raw = counts["warning"] * warn_p
        warn_ded = min(warn_raw, max_warn) if max_warn > 0 else warn_raw
        penalty = err_ded + warn_ded
        raw = max(0, min(100, 100 - penalty))
        if counts["error"] <= int(self.scoring.get("pass_max_errors", 0)) and raw < min_pass:
            raw = min_pass
        return raw

    def score_breakdown(self) -> Dict[str, int]:
        err_p = int(self.scoring.get("error_penalty", 10))
        warn_p = int(self.scoring.get("warning_penalty", 3))
        max_warn = int(self.scoring.get("max_warning_penalty", 45))
        counts = {"error": 0, "warning": 0, "info": 0}
        for v in self.violations:
            counts[v.get("severity", "info")] = counts.get(v.get("severity", "info"), 0) + 1
        warn_raw = counts["warning"] * warn_p
        warn_ded = min(warn_raw, max_warn) if max_warn > 0 else warn_raw
        return {
            "error_count": counts["error"],
            "warning_count": counts["warning"],
            "error_deduction": counts["error"] * err_p,
            "warning_deduction_raw": warn_raw,
            "warning_deduction": warn_ded,
            "warning_capped": 1 if warn_raw > warn_ded else 0,
        }

    def passed(self) -> bool:
        max_err = int(self.scoring.get("pass_max_errors", 0))
        err_count = sum(1 for v in self.violations if v.get("severity") == "error")
        return err_count <= max_err

def audit_schema(
    schema_data: Any,
    rules_yaml: str = "",
    audit_date_str: str = "",
    log: Optional[List[str]] = None,
) -> Dict[str, Any]:
    if log is None:
        log = []
    merged = {"schema_data": schema_data, "rules_yaml": rules_yaml}
    ad = audit_date_str or _resolve_audit_date(merged)
    schema = _parse_schema_data(schema_data)
    rules_cfg = _load_rules(merged)
    log.append(f"开始审核，库表 {len(schema.get('tables') or [])} 张")
    auditor = SchemaAuditor(schema, rules_cfg)
    auditor.audit_all()

    counts = {"error": 0, "warning": 0, "info": 0}
    for v in auditor.violations:
        counts[v.get("severity", "info")] = counts.get(v.get("severity", "info"), 0) + 1

    log.append(
        f"审核完成：error={counts['error']} warning={counts['warning']} info={counts['info']}"
    )
    ar = _RESULT_PASS if auditor.passed() else _RESULT_FAIL
    score_val = auditor.score()
    log.append(f"合规得分={score_val} 结论={ar}")
    msg = "\n".join(log)
    if len(msg) > _MAX_MESSAGE_LEN:
        msg = msg[:_MAX_MESSAGE_LEN] + "\n...(截断)"
    vj = _build_violations_json(schema, auditor, counts, ad)
    return {
        "result": "成功",
        "message": msg,
        "audit_result": ar,
        "audit_score": str(score_val),
        "score": str(score_val),
        "audit_date": ad,
        "violations_json": vj,
    }


def main(
    inputs: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    log: List[str] = [f"=== dify_audit_db_scheme v{_SCRIPT_VERSION} ==="]
    merged: Dict[str, Any] = {}
    try:
        merged = _merge_inputs(inputs=inputs, **kwargs)
        raw_sd = merged.get("schema_data")
        log.append(f"schema_data 类型={type(raw_sd).__name__} 长度={len(str(raw_sd or ''))}")
        ad = _resolve_audit_date(merged)
        out = audit_schema(
            schema_data=raw_sd,
            rules_yaml=str(merged.get("rules_yaml") or merged.get("rules") or ""),
            audit_date_str=ad,
            log=log,
        )
        log.append("=== 执行成功 ===")
        out["message"] = "\n".join(_short_log(log, 12))
        if len(out["message"]) > _MAX_MESSAGE_LEN:
            out["message"] = out["message"][:_MAX_MESSAGE_LEN]
        out["result"] = "成功"
        return out
    except Exception as e:
        log.append(f"异常: {type(e).__name__}: {e}")
        if "JSON" in type(e).__name__ or "schema_data" in str(e):
            log.append(
                "提示: 代码入参 schema_data 应绑定「采集节点.schema_data」，"
                "类型选 String，不要绑 message/整包输出。"
            )
        else:
            log.append(traceback.format_exc().strip()[:800])
        log.append("=== 执行失败 ===")
        return _fail_output(log, _resolve_audit_date(merged))


def _collect_dify_audit_kwargs() -> Dict[str, Any]:
    import sys as _sys

    mod = _sys.modules[__name__]
    merged: Dict[str, Any] = {}
    raw_inputs = mod.__dict__.get("inputs")
    if isinstance(raw_inputs, str) and raw_inputs.strip().startswith("{"):
        try:
            raw_inputs = json.loads(raw_inputs)
        except json.JSONDecodeError:
            raw_inputs = None
    if isinstance(raw_inputs, dict):
        for k in ("schema_data", "rules_yaml", "rules", "audit_date"):
            if k in raw_inputs and raw_inputs[k] not in (None, ""):
                merged[k] = raw_inputs[k]
    for k in ("schema_data", "rules_yaml", "rules", "audit_date"):
        if k in mod.__dict__ and mod.__dict__[k] not in (None, ""):
            merged[k] = mod.__dict__[k]
    return merged


def _score_from_violations_json(vj: str) -> Optional[str]:
    try:
        summary = json.loads(vj).get("summary") or {}
        s = summary.get("score")
        if s is not None and str(s) != "":
            return str(int(s))
    except (json.JSONDecodeError, TypeError, ValueError):
        pass
    return None


def _apply_outputs(out: Dict[str, Any]) -> None:
    global result, message, audit_result, audit_score, score, audit_date, violations_json
    result = str(out.get("result", "失败"))
    message = str(out.get("message", ""))
    audit_result = str(out.get("audit_result", _RESULT_FAIL))
    audit_score = str(out.get("audit_score") or out.get("score") or "0")
    vj = str(out.get("violations_json", "{}"))
    if audit_score == "0":
        parsed = _score_from_violations_json(vj)
        if parsed is not None:
            audit_score = parsed
    score = audit_score
    audit_date = str(out.get("audit_date") or date.today().isoformat())
    if len(vj) > _MAX_VIOLATIONS_JSON_LEN:
        vj = vj[:_MAX_VIOLATIONS_JSON_LEN]
    violations_json = vj


def _dify_has_schema_input() -> bool:
    import sys as _sys

    mod = _sys.modules[__name__]
    raw = mod.__dict__.get("schema_data")
    return raw is not None and str(raw).strip() not in ("", "{}")


if __name__ == "__main__":
    import sys as _sys

    if len(_sys.argv) > 1:
        raw = _sys.argv[1]
        try:
            args = json.loads(raw)
        except json.JSONDecodeError:
            args = {"schema_data": raw}
        print(json.dumps(main(**args), ensure_ascii=False, indent=2))
        raise SystemExit(0)
elif _dify_has_schema_input():
    _apply_outputs(main(**_collect_dify_audit_kwargs()))
