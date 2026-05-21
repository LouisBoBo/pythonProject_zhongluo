#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dify 知识库文档读取：从外部传入连接配置，拉取文档分段后解析出 rule_text。
配置来源：
  - 命令行：参数 > 环境变量（见 load_config）。
  - Dify 代码沙箱：支持两种形式——
    (1) main(dify_api_key=..., dify_base_url=..., dataset_id=..., document_id=...) 仅单篇；
    全库：省略 document_id，或 main(..., export_entire_dataset=True)，或 inputs 中含 export_entire_dataset / export_all_documents；
    (2) main(inputs={...}) 或 **extra 中带一段 JSON 对象 / JSON 字符串（键名与下方示例一致）。
    显式关键字优先，缺项再用 extra / 环境变量；未知键忽略。

环境变量（与 Dify 工作流「输入变量」一致）：
  DIFY_API_KEY      API Key（须为知识库 Dataset Key）
  DIFY_BASE_URL     OpenAPI 根路径，如 http://host:28080/v1
  KNOWLEDGE_ID      知识库 ID（即 dataset_id）
  DOCUMENT_ID       文档 ID。**仅导出单篇**时需要；未设置时默认**导出该知识库内全部文档**（与 --all-documents 等价）。
  EXPORT_ENTIRE_DATASET  与 --all-documents 同：显式全库。若已设置 DOCUMENT_ID 但仍要导出全库，请设为 1。

  DIFY_RULE_EXPORT_VERBOSE  设为 1/true/yes 时，打印「全文回退」说明（默认关闭）
  DIFY_RULE_EXPORT_STDERR   设为 1/true/yes 时打印进度类诊断日志（默认关闭，避免 Dify 控制台与
                            沙箱 stderr 混流导致乱码；错误行以 ❌ 开头时仍会输出）

标准输出（仅命令行 `python douqu_rules.py`）：`__main__` 中写入一行 JSON，便于管道。
  在 Dify「代码」节点中：请使用 **`result = main(inputs=...)`**（或关键字参数），返回值类型为 **dict**，
  成功为 **`{"rule_text": "<全文>", "message": "读取成功"}`**；失败为 **`{"rule_text": "", "message": "<原因>"}`**
  （平台要求 dict，不能返回 int）。

读取对象说明（与「文档提取器」关系）：
  - 默认：通过 Dataset API 读取「知识库里的一条文档」——先 GET 文档元数据，再 GET 该文档下
    已切分的 segments（分段文本），拼成与索引一致的整篇正文；不是再下载原始上传文件的二进制。
  - 全库模式（未提供 document_id，或 export_entire_dataset / --all-documents）：分页列出知识库内文档，
    对每篇拉取分段后按列表顺序拼接（篇与篇之间用双换行），不写入文档名。
  - Dify 工作流里的「文档提取器 / 知识库检索」等节点，读的是同一套知识库与分段数据，只是走
    平台内置链路；若你的目标只是拿到全文给下游，用文档提取器或本脚本二选一即可，不必叠加。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import unicodedata
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import requests


def _argparse_kwargs() -> Dict[str, Any]:
    """Python 3.9+ 关闭 parse 时直接 sys.exit，便于向 stdout 写入错误 JSON。"""
    if sys.version_info >= (3, 9):
        return {"exit_on_error": False}
    return {}


def _stdout_print_raw_utf8_line(text: str) -> None:
    """向 stdout 写入一行 UTF-8（不经由可能非 UTF-8 的 TextIO 编码层）。"""
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


_READ_OK_MESSAGE = "读取成功"


def emit_stdout_result(out: Dict[str, Any]) -> None:
    """
    命令行用：向 stdout 写入一行 UTF-8 JSON，字段与 main() 返回值一致。
    """
    try:
        _stdout_print_raw_utf8_line(json.dumps(out, ensure_ascii=False))
    except Exception:
        try:
            _stdout_print_raw_utf8_line(
                '{"rule_text":"","message":"stdout_write_failed"}'
            )
        except Exception:
            pass


def result_ok(rule_text: str) -> Dict[str, Any]:
    """Dify 代码节点：含 rule_text 与成功提示 message。"""
    return {"rule_text": rule_text, "message": _READ_OK_MESSAGE}


def result_err(message: str) -> Dict[str, Any]:
    """失败：rule_text 置空，message 说明原因。"""
    return {"rule_text": "", "message": message}


# 日志一律写 sys.stderr.buffer（UTF-8 字节），避免在已有 TextIOWrapper 上再包一层导致双解码乱码。
# 不在 stderr.buffer 上再创建 TextIOWrapper（会与原 sys.stderr 争用同一缓冲，出现截断/重复/）。
_STDERR_INIT_DONE = False


def _configure_stderr_utf8() -> None:
    """仅尝试 reconfigure，绝不替换为新的 TextIOWrapper（易与运行时双写同一 buffer）。"""
    global _STDERR_INIT_DONE
    if _STDERR_INIT_DONE:
        return
    _STDERR_INIT_DONE = True
    stream = sys.stderr
    enc = (getattr(stream, "encoding", None) or "").lower()
    if enc in ("utf-8", "utf8"):
        return
    if hasattr(stream, "reconfigure"):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError, ValueError, TypeError):
            pass


def _safe_text_for_log(value: Any) -> str:
    """统一成合法 Unicode，避免控制台替换字与孤代理对。"""
    if value is None:
        return ""
    s = str(value)
    if s.startswith("\ufeff"):
        s = s.lstrip("\ufeff")
    try:
        s = unicodedata.normalize("NFC", s)
    except Exception:
        pass
    try:
        return s.encode("utf-8", errors="surrogateescape").decode(
            "utf-8", errors="replace"
        )
    except Exception:
        return s.encode("utf-8", errors="replace").decode("utf-8", errors="replace")


def _truthy_env(value: Optional[Any]) -> bool:
    """解析环境变量或表单里的布尔开关（1/true/yes/on）。"""
    if isinstance(value, bool):
        return value
    s = str(value or "").strip().lower()
    return s in ("1", "true", "yes", "on")


@dataclass
class DifyExportConfig:
    dify_base_url: str
    dify_api_key: str
    dataset_id: str
    document_id: str
    request_interval: float = 0.1
    export_entire_dataset: bool = False

    def normalized_base_url(self) -> str:
        return self.dify_base_url.rstrip("/")

    def headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.dify_api_key}",
            "Content-Type": "application/json",
        }


def load_config(
    argv: Optional[List[str]] = None,
) -> tuple[DifyExportConfig, Optional[str]]:
    parser = argparse.ArgumentParser(
        description="从 Dify 知识库读取文档并输出 JSON：{\"rule_text\": ...}",
        epilog="本机调试进度：export DIFY_RULE_EXPORT_STDERR=1",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        **_argparse_kwargs(),
    )
    parser.add_argument(
        "--dify-api-key",
        default=os.environ.get("DIFY_API_KEY", "").strip(),
        help="覆盖环境变量 DIFY_API_KEY",
    )
    parser.add_argument(
        "--dify-base-url",
        default=os.environ.get("DIFY_BASE_URL", "").strip(),
        help="覆盖环境变量 DIFY_BASE_URL",
    )
    parser.add_argument(
        "--dataset-id",
        default=(
            os.environ.get("KNOWLEDGE_ID", "").strip()
            or os.environ.get("DATASET_ID", "").strip()
        ),
        help="知识库 ID；默认环境变量 KNOWLEDGE_ID 或 DATASET_ID",
    )
    parser.add_argument(
        "--document-id",
        default=os.environ.get("DOCUMENT_ID", "").strip(),
        help="文档 ID；仅单篇导出需要。省略则默认导出知识库内全部文档",
    )
    parser.add_argument(
        "--all-documents",
        action="store_true",
        help="显式全库导出；与不传 document_id 时默认行为相同",
    )
    parser.add_argument(
        "--request-interval",
        type=float,
        default=float(os.environ.get("REQUEST_INTERVAL", "0.1")),
        help="分页请求间隔（秒）",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="FILE",
        help="同时将 stdout 同款 JSON 一行写入该文件（可选）",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="交互选择知识库与文档（仍从环境/参数读 API 与 Base URL）",
    )
    try:
        args = parser.parse_args(argv)
    except argparse.ArgumentError as e:
        raise ValueError(str(e)) from e

    export_all = (
        bool(args.all_documents)
        or _truthy_env(os.environ.get("EXPORT_ENTIRE_DATASET", ""))
        or not (args.document_id or "").strip()
    )
    required_rows: List[tuple[str, str]] = [
        ("DIFY_API_KEY / --dify-api-key", args.dify_api_key),
        ("DIFY_BASE_URL / --dify-base-url", args.dify_base_url),
        ("KNOWLEDGE_ID|DATASET_ID / --dataset-id", args.dataset_id),
    ]
    if not export_all:
        required_rows.append(("DOCUMENT_ID / --document-id", args.document_id))
    missing = [name for name, val in required_rows if not val]
    if missing and not args.interactive:
        extra = (
            "本脚本不会自动加载 .env，请在当前 shell 执行 export（或传入 --dify-api-key 等长参数）。"
        )
        if not export_all:
            extra += "若只导出单篇文档，请设置 DOCUMENT_ID 或 --document-id。"
        extra += "完整参数见：python douqu_rules.py --help"
        raise ValueError("缺少配置: " + ", ".join(missing) + "。" + extra)

    cfg = DifyExportConfig(
        dify_base_url=args.dify_base_url,
        dify_api_key=args.dify_api_key,
        dataset_id=args.dataset_id,
        document_id=args.document_id,
        request_interval=args.request_interval,
        export_entire_dataset=export_all,
    )
    return cfg, args.output


def log(msg: str, *, end: Optional[str] = None, flush: bool = True) -> None:
    """诊断输出：默认关闭（Dify 与 stderr 混流易乱码）；DIFY_RULE_EXPORT_STDERR=1 开启；❌ 错误始终输出。"""
    ev = os.environ.get("DIFY_RULE_EXPORT_STDERR", "").strip().lower()
    force = (
        msg.lstrip().startswith("❌")
        or msg.lstrip().startswith("✗")
        or "缺少配置" in msg
        or "失败" in msg
        or "请求失败" in msg
        or "文件保存失败" in msg
    )
    if not force and ev not in ("1", "true", "yes", "on"):
        return
    _configure_stderr_utf8()
    tail = "\n" if end is None else _safe_text_for_log(end)
    text = _safe_text_for_log(msg) + tail
    data = text.encode("utf-8", errors="replace")
    buf = getattr(sys.stderr, "buffer", None)
    if buf is not None:
        try:
            buf.write(data)
            if flush:
                buf.flush()
            return
        except (BrokenPipeError, OSError, TypeError, AttributeError, ValueError):
            pass
    try:
        print(text, end="", file=sys.stderr, flush=flush)
    except Exception:
        pass


def _pick_str(*candidates: Optional[Any]) -> str:
    """从左到右取第一个非空的字符串。"""
    for c in candidates:
        if c is None:
            continue
        s = str(c).strip()
        if s:
            return s
    return ""


def _config_from_callable_kwargs(
    *,
    dify_api_key: Optional[str] = None,
    dify_base_url: Optional[str] = None,
    dataset_id: Optional[str] = None,
    document_id: Optional[str] = None,
    knowledge_id: Optional[str] = None,
    request_interval: Optional[float] = None,
    output: Optional[str] = None,
    export_entire_dataset: Optional[Any] = None,
) -> tuple[Optional[DifyExportConfig], Optional[str]]:
    """
    供 Dify 沙箱以关键字调用 main 时使用：参数 > 环境变量。
    返回 (config, output_path)；缺必填项时 config 为 None。
    """
    api = _pick_str(dify_api_key, os.environ.get("DIFY_API_KEY"))
    base = _pick_str(dify_base_url, os.environ.get("DIFY_BASE_URL"))
    ds = _pick_str(
        dataset_id,
        knowledge_id,
        os.environ.get("KNOWLEDGE_ID"),
        os.environ.get("DATASET_ID"),
    )
    doc = _pick_str(document_id, os.environ.get("DOCUMENT_ID"))
    interval = (
        float(request_interval)
        if request_interval is not None
        else float(os.environ.get("REQUEST_INTERVAL", "0.1"))
    )
    out_path = _pick_str(output) or None

    ent = export_entire_dataset
    if ent is not None and not isinstance(ent, bool):
        ent = _truthy_env(ent)
    if ent is None:
        ent = _truthy_env(os.environ.get("EXPORT_ENTIRE_DATASET", ""))
    ent = bool(ent)
    if not doc:
        ent = True
    else:
        ent = bool(ent)

    required: List[tuple[str, str]] = [
        ("dify_api_key / DIFY_API_KEY", api),
        ("dify_base_url / DIFY_BASE_URL", base),
        ("dataset_id|knowledge_id / KNOWLEDGE_ID|DATASET_ID", ds),
    ]
    if not ent:
        required.append(("document_id / DOCUMENT_ID", doc))
    missing = [label for label, val in required if not val]
    if missing:
        log("❌ 缺少配置（关键字或环境变量）: " + ", ".join(missing))
        return None, out_path

    return (
        DifyExportConfig(
            dify_base_url=base,
            dify_api_key=api,
            dataset_id=ds,
            document_id=doc if doc else "",
            request_interval=interval,
            export_entire_dataset=ent,
        ),
        out_path,
    )


_MAIN_PAYLOAD_KEYS = frozenset(
    {
        "dify_api_key",
        "dify_base_url",
        "dataset_id",
        "document_id",
        "knowledge_id",
        "request_interval",
        "output",
        "export_entire_dataset",
    }
)


def _normalize_input_key(key: str) -> str:
    return str(key).strip().lower().replace("-", "_")


def _ingest_inputs_into_payload(
    explicit: Dict[str, Optional[Any]],
    *sources: Dict[str, Any],
) -> Dict[str, Optional[Any]]:
    """
    将 Dify 传入的整段 JSON（dict 或 JSON 字符串）与显式关键字合并到同一 payload。
    仅当 explicit 中某项为 None 时才用外部对象中的同名字段覆盖。
    """
    out: Dict[str, Optional[Any]] = dict(explicit)

    def absorb(obj: Any) -> None:
        if obj is None:
            return
        if isinstance(obj, str):
            s = obj.strip()
            if s.startswith("{") and s.endswith("}"):
                try:
                    absorb(json.loads(s))
                except json.JSONDecodeError:
                    pass
            return
        if not isinstance(obj, dict):
            return
        for k, v in obj.items():
            nk = _normalize_input_key(k)
            if nk in ("export_all_documents", "all_documents"):
                nk = "export_entire_dataset"
            if nk not in _MAIN_PAYLOAD_KEYS:
                continue
            if nk == "export_entire_dataset" and v is not None and not isinstance(v, bool):
                v = _truthy_env(v)
            if nk == "request_interval" and v is not None:
                try:
                    v = float(v)
                except (TypeError, ValueError):
                    continue
            if v is None:
                continue
            if isinstance(v, str) and not v.strip():
                continue
            if out.get(nk) is None:
                out[nk] = v

    for bag in sources:
        absorb(bag)
        for v in bag.values():
            absorb(v)
    return out


def fetch_json(
    session: requests.Session,
    url: str,
    headers: Dict[str, str],
    params: Optional[Dict[str, Any]] = None,
) -> Optional[Dict[str, Any]]:
    response = None
    try:
        response = session.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        log(f"请求失败 [{url}]: {e}")
        if response is not None:
            if response.status_code == 404:
                log("  提示：请检查知识库 ID 和文档 ID 是否正确")
            elif response.status_code == 401:
                log("  提示：知识库 API 需使用 Dataset 类 API Key；app- 应用密钥会 401")
                try:
                    body = response.text[:500]
                    if body.strip():
                        log(f"  服务端返回: {body}")
                except Exception:
                    pass
            else:
                try:
                    body = response.text[:300]
                    if body.strip():
                        log(f"  服务端返回: {body}")
                except Exception:
                    pass
        return None
    except ValueError as e:
        log(f"响应不是合法 JSON [{url}]: {e}")
        if response is not None and response.text:
            log(f"  原始响应前 300 字: {response.text[:300]}")
        return None


def get_document_info(
    session: requests.Session, config: DifyExportConfig
) -> Optional[Dict[str, Any]]:
    base = config.normalized_base_url()
    url = f"{base}/datasets/{config.dataset_id}/documents/{config.document_id}"
    log("正在获取文档信息...")
    data = fetch_json(session, url, config.headers())
    if data:
        lines = [
            f"  ✓ 文档名称: {data.get('name', '未知')}",
            f"  ✓ 分段数量: {data.get('segment_count', 0)}",
            f"  ✓ 总字符数: {data.get('word_count', 0)}",
            f"  ✓ 索引状态: {data.get('indexing_status', '未知')}",
            f"  ✓ 分段模式: {data.get('doc_form', '未知')}",
        ]
        log("\n".join(lines))
    return data


def get_document_segments(
    session: requests.Session, config: DifyExportConfig
) -> List[str]:
    base = config.normalized_base_url()
    all_contents: List[str] = []
    page = 1
    limit = 100
    log("\n正在获取文档分段内容...")
    while True:
        url = f"{base}/datasets/{config.dataset_id}/documents/{config.document_id}/segments"
        params = {"page": page, "limit": limit}
        try:
            response = session.get(url, headers=config.headers(), params=params)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            log(f"  第 {page} 页请求失败: {e}")
            break
        segments = data.get("data", [])
        if not segments:
            log(f"  第 {page} 页：无数据")
            break
        page_content_count = 0
        for segment in segments:
            content = segment.get("content", "")
            if content:
                all_contents.append(content)
                page_content_count += 1
        log(f"  第 {page} 页：获取 {page_content_count} 条分段")
        pagination = data.get("pagination") or {}
        if not isinstance(pagination, dict):
            pagination = {}
        total_pages = pagination.get("total_pages")
        has_more = data.get("has_more")
        if has_more is None:
            has_more = pagination.get("has_more")
        if has_more is True:
            page += 1
            time.sleep(config.request_interval)
            continue
        if has_more is False:
            break
        try:
            tp = int(total_pages) if total_pages is not None else 0
        except (TypeError, ValueError):
            tp = 0
        # total_pages 缺失或为 0 时不能用 page>=tp 结束，否则只拿第一页（常见 limit=100）
        if tp > 0:
            if page >= tp:
                break
        elif len(segments) < limit:
            break
        page += 1
        time.sleep(config.request_interval)
    log(f"\n共获取 {len(all_contents)} 个分段")
    return all_contents


def merge_segments(segments: List[str], separator: str = "\n\n") -> str:
    if not segments:
        return ""
    return separator.join(segments)


def extract_rule_text(raw: str) -> str:
    """
    从拼接后的正文解析 rule_text。
    支持：整段为 {"rule_text": "..."}；或为 [{...,"rule_text":...}, ...]；
    或各分段分别为含 rule_text 的 JSON（合并后再解析一次）。
    """
    text = raw.strip()
    if not text:
        return ""

    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        return ""

    if isinstance(obj, dict) and "rule_text" in obj:
        v = obj["rule_text"]
        return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)

    if isinstance(obj, list):
        parts: List[str] = []
        for item in obj:
            if isinstance(item, dict) and "rule_text" in item:
                v = item["rule_text"]
                parts.append(v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))
        if parts:
            return "\n\n".join(parts)

    return ""


def extract_rule_text_from_segments(segments: List[str]) -> str:
    """
    优先从 JSON 结构中提取 rule_text（整段或分段、或数组元素）。
    若无 JSON 或不含 rule_text 键（例如 Markdown / 纯文本入库），则返回分段拼接后的全文。
    """
    merged = merge_segments(segments)
    merged_stripped = merged.strip()
    if not merged_stripped:
        return ""

    out = extract_rule_text(merged)
    if out:
        return out
    pieces: List[str] = []
    for seg in segments:
        seg = seg.strip()
        if not seg:
            continue
        try:
            obj = json.loads(seg)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and "rule_text" in obj:
            v = obj["rule_text"]
            pieces.append(v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, dict) and "rule_text" in item:
                    v = item["rule_text"]
                    pieces.append(
                        v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
                    )
    if pieces:
        return "\n\n".join(pieces)
    if merged_stripped:
        if os.environ.get("DIFY_RULE_EXPORT_VERBOSE", "").strip().lower() in (
            "1",
            "true",
            "yes",
        ):
            log(
                "ℹ 未解析到 JSON 字段 rule_text，已使用分段拼接全文作为 rule_text（Markdown/纯文本等）"
            )
    return merged_stripped


def export_to_file(content: str, filename: str) -> None:
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"\n✓ 已写入文件: {filename}（{len(content)} 字符）")
    except OSError as e:
        log(f"\n✗ 文件保存失败: {e}")


def list_all_datasets(session: requests.Session, config: DifyExportConfig) -> Optional[List[Dict]]:
    base = config.normalized_base_url()
    url = f"{base}/datasets"
    log("\n正在获取知识库列表...")
    data = fetch_json(session, url, config.headers())
    if not data:
        return None
    datasets = data.get("data", [])
    log(f"\n共找到 {len(datasets)} 个知识库:")
    for ds in datasets:
        log(f"  - ID: {ds.get('id')}, 名称: {ds.get('name')}")
    return datasets


def list_documents_in_dataset(
    session: requests.Session, config: DifyExportConfig, dataset_id: str
) -> Optional[List[Dict[str, Any]]]:
    base = config.normalized_base_url()
    url = f"{base}/datasets/{dataset_id}/documents"
    log(f"\n正在分页获取知识库 {dataset_id} 中的文档列表...")
    all_docs: List[Dict[str, Any]] = []
    page = 1
    limit = 100
    while True:
        data = fetch_json(
            session, url, config.headers(), params={"page": page, "limit": limit}
        )
        if data is None:
            return None if not all_docs else all_docs
        docs = data.get("data") or []
        if not docs:
            break
        all_docs.extend(docs)
        has_more = data.get("has_more")
        pag = data.get("pagination")
        if isinstance(pag, dict) and has_more is None:
            has_more = pag.get("has_more")
        total = data.get("total")
        if isinstance(pag, dict) and total is None:
            total = pag.get("total")
        if total is not None:
            try:
                if len(all_docs) >= int(total):
                    break
            except (TypeError, ValueError):
                pass
        if has_more is True:
            page += 1
            time.sleep(config.request_interval)
            continue
        if has_more is False:
            break
        if len(docs) < limit:
            break
        page += 1
        time.sleep(config.request_interval)
    log(f"\n共找到 {len(all_docs)} 个文档")
    for doc in all_docs:
        log(
            f"  - ID: {doc.get('id')}, 名称: {doc.get('name')}, 状态: {doc.get('indexing_status')}"
        )
    return all_docs


def run_export_entire_dataset(
    config: DifyExportConfig,
    *,
    output_file: Optional[str] = None,
) -> Dict[str, Any]:
    """遍历知识库内全部已索引文档，拼接各篇分段正文（篇间双换行，不插入文档名）。"""

    def fail(msg: str) -> Dict[str, Any]:
        log(f"\n❌ {msg}")
        return result_err(msg)

    try:
        log("=" * 60)
        log("Dify 知识库（全部文档）→ rule_text")
        log("=" * 60)
        log(f"\nAPI: {config.normalized_base_url()}")
        log(f"知识库: {config.dataset_id}")

        with requests.Session() as session:
            docs = list_documents_in_dataset(session, config, config.dataset_id)
            if docs is None:
                return fail("获取文档列表失败，请检查 API Key、知识库 ID 与网络")
            if not docs:
                return fail("知识库中没有文档")

            parts: List[str] = []
            for doc in docs:
                doc_id = doc.get("id")
                if not doc_id:
                    continue
                # 列表接口各版本字段不一致：可能缺 indexing_status、segment_count 恒为 0。
                # 仅明确跳过失败态，其余一律尝试拉 segments（与单篇导出「非 completed 仍拉取」一致）。
                status = str(
                    doc.get("indexing_status")
                    or doc.get("display_status")
                    or doc.get("status")
                    or ""
                ).strip().lower()
                if status == "error":
                    log(f"  跳过（索引失败）: id={doc_id}")
                    continue

                doc_cfg = DifyExportConfig(
                    dify_base_url=config.dify_base_url,
                    dify_api_key=config.dify_api_key,
                    dataset_id=config.dataset_id,
                    document_id=str(doc_id),
                    request_interval=config.request_interval,
                    export_entire_dataset=False,
                )
                segments = get_document_segments(session, doc_cfg)
                if not segments:
                    log(f"  跳过（分段接口为空）: id={doc_id}")
                    continue
                rule_text = extract_rule_text_from_segments(segments)
                if not rule_text.strip():
                    continue
                parts.append(rule_text.strip())
                time.sleep(config.request_interval)

            merged = "\n\n".join(parts)
            if not merged.strip():
                return fail(
                    "没有可用的文档内容：可能仍在索引进度中、分段接口为空，或列表字段与当前 Dify 版本不一致。"
                    "请设置 DIFY_RULE_EXPORT_STDERR=1 后重试以查看每篇文档的处理日志。"
                )

            if output_file:
                line = json.dumps({"rule_text": merged}, ensure_ascii=False)
                export_to_file(line, output_file)
            return result_ok(merged)
    except Exception as e:
        err = f"{type(e).__name__}: {e}"
        log(f"❌ 未捕获异常: {err}")
        return result_err(err)


def run_export(
    config: DifyExportConfig,
    *,
    output_file: Optional[str] = None,
) -> Dict[str, Any]:
    """返回 dict 供 Dify 代码节点；命令行由 __main__ 再写 stdout。"""
    if config.export_entire_dataset:
        return run_export_entire_dataset(config, output_file=output_file)

    def fail(msg: str) -> Dict[str, Any]:
        log(f"\n❌ {msg}")
        return result_err(msg)

    try:
        log("=" * 60)
        log("Dify 知识库 → rule_text")
        log("=" * 60)
        log(f"\nAPI: {config.normalized_base_url()}")
        log(f"知识库: {config.dataset_id}")
        log(f"文档: {config.document_id}")

        with requests.Session() as session:
            doc_info = get_document_info(session, config)
            if not doc_info:
                return fail("获取文档信息失败，请检查 API Key、知识库 ID、文档 ID 与网络")

            indexing_status = doc_info.get("indexing_status", "")
            if indexing_status != "completed":
                log(f"\n⚠ 索引状态: {indexing_status}，内容可能不完整")
            if doc_info.get("segment_count", 0) == 0:
                return fail("该文档没有分段（segment_count 为 0）")

            segments = get_document_segments(session, config)
            if not segments:
                return fail("未获取到任何分段内容")

            rule_text = extract_rule_text_from_segments(segments)
            if not rule_text:
                return fail("分段内容为空，无法组成 rule_text")

            line = json.dumps({"rule_text": rule_text}, ensure_ascii=False)
            if output_file:
                export_to_file(line, output_file)
            return result_ok(rule_text)
    except Exception as e:
        err = f"{type(e).__name__}: {e}"
        log(f"❌ 未捕获异常: {err}")
        return result_err(err)


def interactive_mode(
    config: DifyExportConfig,
    *,
    output_file: Optional[str],
    export_entire_dataset: bool = False,
) -> Dict[str, Any]:
    if not config.dify_api_key:
        log("❌ 请先设置 DIFY_API_KEY")
        return result_err("请先设置 DIFY_API_KEY")
    log("=" * 60)
    log("交互模式")
    log("=" * 60)

    with requests.Session() as session:
        datasets = list_all_datasets(session, config)
        if not datasets:
            return result_err("未找到任何知识库")
        log("\n请输入知识库 ID（回车使用当前 KNOWLEDGE_ID / DATASET_ID）:")
        ds = input("> ").strip() or config.dataset_id
        if not ds:
            log("❌ 未指定知识库 ID")
            return result_err("未指定知识库 ID")
        if export_entire_dataset:
            cfg = DifyExportConfig(
                dify_base_url=config.dify_base_url,
                dify_api_key=config.dify_api_key,
                dataset_id=ds,
                document_id="",
                request_interval=config.request_interval,
                export_entire_dataset=True,
            )
            return run_export(cfg, output_file=output_file)

        documents = list_documents_in_dataset(session, config, ds)
        if documents is None:
            return result_err("获取文档列表失败")
        if not documents:
            return result_err("该知识库中没有文档")
        log("\n请输入文档 ID（回车使用当前 DOCUMENT_ID）:")
        doc = input("> ").strip() or config.document_id
        if not doc:
            log("❌ 未指定文档 ID")
            return result_err("未指定文档 ID")

        cfg = DifyExportConfig(
            dify_base_url=config.dify_base_url,
            dify_api_key=config.dify_api_key,
            dataset_id=ds,
            document_id=doc,
            request_interval=config.request_interval,
            export_entire_dataset=False,
        )
        return run_export(cfg, output_file=output_file)


def _main_impl(
    argv: Optional[List[str]] = None,
    *,
    inputs: Optional[Any] = None,
    dify_api_key: Optional[str] = None,
    dify_base_url: Optional[str] = None,
    dataset_id: Optional[str] = None,
    document_id: Optional[str] = None,
    knowledge_id: Optional[str] = None,
    request_interval: Optional[float] = None,
    output: Optional[str] = None,
    export_entire_dataset: Optional[Any] = None,
    interactive: bool = False,
    **extra: Any,
) -> Dict[str, Any]:
    """命令行无关键字且无 inputs/extra 时走 argparse；否则合并 inputs、extra 与显式参数。"""
    merge_sources: List[Dict[str, Any]] = []
    if extra:
        merge_sources.append(dict(extra))
    if inputs is not None:
        merge_sources.append({"inputs": inputs})

    payload = _ingest_inputs_into_payload(
        {
            "dify_api_key": dify_api_key,
            "dify_base_url": dify_base_url,
            "dataset_id": dataset_id,
            "document_id": document_id,
            "knowledge_id": knowledge_id,
            "request_interval": request_interval,
            "output": output,
            "export_entire_dataset": export_entire_dataset,
        },
        *merge_sources,
    )

    argv = sys.argv[1:] if argv is None else list(argv)
    pre_parser = argparse.ArgumentParser(add_help=False, **_argparse_kwargs())
    pre_parser.add_argument("--interactive", action="store_true")
    pre_parser.add_argument("--all-documents", action="store_true")
    pre_args, _ = pre_parser.parse_known_args(argv)

    if interactive:
        api = _pick_str(payload["dify_api_key"], os.environ.get("DIFY_API_KEY"))
        base = _pick_str(payload["dify_base_url"], os.environ.get("DIFY_BASE_URL"))
        if not api or not base:
            log("❌ 交互模式需要 dify_api_key 与 dify_base_url（inputs、关键字或环境变量）")
            return result_err(
                "交互模式需要 dify_api_key 与 dify_base_url（inputs、关键字或环境变量）"
            )
        interval = (
            float(payload["request_interval"])
            if payload["request_interval"] is not None
            else float(os.environ.get("REQUEST_INTERVAL", "0.1"))
        )
        doc_pick = _pick_str(payload["document_id"], os.environ.get("DOCUMENT_ID"))
        ent_raw = payload.get("export_entire_dataset")
        if not doc_pick:
            ent_flag = True
        elif isinstance(ent_raw, bool):
            ent_flag = ent_raw
        elif ent_raw is not None:
            ent_flag = _truthy_env(ent_raw)
        else:
            ent_flag = _truthy_env(os.environ.get("EXPORT_ENTIRE_DATASET", ""))
        cfg = DifyExportConfig(
            dify_base_url=base,
            dify_api_key=api,
            dataset_id=_pick_str(
                payload["dataset_id"],
                payload["knowledge_id"],
                os.environ.get("KNOWLEDGE_ID"),
                os.environ.get("DATASET_ID"),
            ),
            document_id=doc_pick,
            request_interval=interval,
            export_entire_dataset=bool(ent_flag),
        )
        return interactive_mode(
            cfg,
            output_file=_pick_str(payload["output"]) or None,
            export_entire_dataset=cfg.export_entire_dataset,
        )

    kw_passed = any(
        payload[k] is not None
        for k in (
            "dify_api_key",
            "dify_base_url",
            "dataset_id",
            "document_id",
            "knowledge_id",
            "output",
            "request_interval",
            "export_entire_dataset",
        )
    )
    if kw_passed:
        cfg, out_path = _config_from_callable_kwargs(
            dify_api_key=payload["dify_api_key"],
            dify_base_url=payload["dify_base_url"],
            dataset_id=payload["dataset_id"],
            document_id=payload["document_id"],
            knowledge_id=payload["knowledge_id"],
            request_interval=payload["request_interval"],
            output=payload["output"],
            export_entire_dataset=payload.get("export_entire_dataset"),
        )
        if cfg is None:
            return result_err(
                "缺少必要配置：dify_api_key、dify_base_url、dataset_id（或 KNOWLEDGE_ID 等）。"
                "未传 document_id 时默认全库导出；仅导出单篇时请传 document_id。"
            )
        return run_export(cfg, output_file=out_path)

    if pre_args.interactive:
        parser = argparse.ArgumentParser(
            parents=[pre_parser], add_help=True, **_argparse_kwargs()
        )
        parser.add_argument("--dify-api-key", default=os.environ.get("DIFY_API_KEY", "").strip())
        parser.add_argument("--dify-base-url", default=os.environ.get("DIFY_BASE_URL", "").strip())
        parser.add_argument(
            "--dataset-id",
            default=os.environ.get("KNOWLEDGE_ID", "").strip()
            or os.environ.get("DATASET_ID", "").strip(),
        )
        parser.add_argument("--document-id", default=os.environ.get("DOCUMENT_ID", "").strip())
        parser.add_argument(
            "--all-documents",
            action="store_true",
            help="交互选库后导出该库全部已索引文档（无需再输入文档 ID）",
        )
        parser.add_argument("--request-interval", type=float, default=0.1)
        parser.add_argument("-o", "--output", default=None)
        try:
            args = parser.parse_args(argv)
        except argparse.ArgumentError as e:
            return result_err(str(e))
        if not args.dify_api_key or not args.dify_base_url:
            return result_err("交互模式需要 DIFY_API_KEY 与 DIFY_BASE_URL（环境或参数）")
        export_all = (
            bool(args.all_documents)
            or _truthy_env(os.environ.get("EXPORT_ENTIRE_DATASET", ""))
            or not (args.document_id or "").strip()
        )
        config = DifyExportConfig(
            dify_base_url=args.dify_base_url,
            dify_api_key=args.dify_api_key,
            dataset_id=args.dataset_id or "",
            document_id=args.document_id or "",
            request_interval=args.request_interval,
            export_entire_dataset=export_all,
        )
        return interactive_mode(
            config,
            output_file=args.output,
            export_entire_dataset=config.export_entire_dataset,
        )

    try:
        config, output_file = load_config(argv)
        return run_export(config, output_file=output_file)
    except ValueError as e:
        return result_err(str(e))


def main(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    """对外入口：返回 dict 供 Dify；未捕获异常也转为 dict。"""
    try:
        return _main_impl(*args, **kwargs)
    except ValueError as e:
        return result_err(str(e))
    except SystemExit:
        raise
    except BaseException as e:
        err = f"{type(e).__name__}: {e}"
        log(f"❌ {err}")
        return result_err(err)


if __name__ == "__main__":
    _out = main()
    emit_stdout_result(_out)
    raise SystemExit(1 if not (_out.get("rule_text") or "").strip() else 0)
