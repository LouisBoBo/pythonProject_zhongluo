#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dify 代码节点：向知识库按文本新建一篇文档（create-by-text）。

入参（仅 4 个，与画布变量名一致）：
- dataset_id：知识库 ID
- dify_base_url：API 根，须含 /v1
- dify_api_key：Dataset API Key
- add_rule：文档正文（约束规则等）

文档名称每次自动生成：「追加约束」+ 时间戳 + 短随机串，避免与已有文档同名
被平台当作重复/更新而覆盖内容（仅一条「追加约束」行不断被替换）。

出参（仅 1 个，字符串）：
- success：成功为字符串 "true"，否则为 "false"（HTTP 非 2xx 或请求异常、参数不全）；不等待索引完成。

可选：将上述键放在 arg1（dict）中传入；与命名参数同时存在时，命名参数优先。
"""

from __future__ import annotations

import argparse
import os
import sys
import time
import uuid
from typing import Any, Dict, Optional

import requests

DEFAULT_DOC_NAME = "追加约束"


def _unique_append_doc_name() -> str:
    """知识库内同名易触发重复索引/覆盖；每次追加使用唯一名称。"""
    ts = time.strftime("%Y%m%d_%H%M%S")
    return f"{DEFAULT_DOC_NAME}_{ts}_{uuid.uuid4().hex[:8]}"


def _norm_base_url(url: str) -> str:
    return (url or "").strip().rstrip("/")


def _headers(api_key: str) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }


def _coerce_str(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, str):
        return v.strip()
    return str(v).strip()


def create_document_by_text(
    *,
    base_url: str,
    api_key: str,
    dataset_id: str,
    name: str,
    text: str,
    indexing_technique: str = "high_quality",
    doc_form: str = "text_model",
    doc_language: str = "Chinese",
    timeout: int = 120,
) -> Dict[str, Any]:
    root = _norm_base_url(base_url)
    url = f"{root}/datasets/{dataset_id}/document/create-by-text"
    payload: Dict[str, Any] = {
        "name": name,
        "text": text,
        "indexing_technique": indexing_technique,
        "doc_form": doc_form,
        "doc_language": doc_language,
    }
    r = requests.post(
        url, headers=_headers(api_key), json=payload, timeout=timeout
    )
    r.raise_for_status()
    return r.json()


def _merge_inputs(
    arg1: Any,
    dataset_id: str | None,
    dify_base_url: str | None,
    dify_api_key: str | None,
    add_rule: str | None,
    kwargs: dict[str, Any],
) -> dict[str, Any]:
    m: dict[str, Any] = {}
    keys = ("dataset_id", "dify_base_url", "dify_api_key", "add_rule")
    if isinstance(arg1, dict):
        for k in keys:
            if k in arg1:
                m[k] = arg1[k]
    for k in keys:
        if k in kwargs:
            m[k] = kwargs[k]
    if dataset_id is not None:
        m["dataset_id"] = dataset_id
    if dify_base_url is not None:
        m["dify_base_url"] = dify_base_url
    if dify_api_key is not None:
        m["dify_api_key"] = dify_api_key
    if add_rule is not None:
        m["add_rule"] = add_rule
    return m


def main(
    arg1: Any = None,
    dataset_id: str | None = None,
    dify_base_url: str | None = None,
    dify_api_key: str | None = None,
    add_rule: str | None = None,
    **kwargs: Any,
) -> dict[str, str]:
    m = _merge_inputs(arg1, dataset_id, dify_base_url, dify_api_key, add_rule, kwargs)

    ds = _coerce_str(m.get("dataset_id"))
    base = _coerce_str(m.get("dify_base_url"))
    key = _coerce_str(m.get("dify_api_key"))
    text = _coerce_str(m.get("add_rule"))

    if not (base and key and ds and text):
        return {"success": "false"}

    try:
        create_document_by_text(
            base_url=base,
            api_key=key,
            dataset_id=ds,
            name=_unique_append_doc_name(),
            text=text,
        )
        return {"success": "true"}
    except requests.exceptions.RequestException:
        return {"success": "false"}


def list_documents(
    *,
    base_url: str,
    api_key: str,
    dataset_id: str,
    page: int = 1,
    limit: int = 50,
    timeout: int = 60,
) -> Dict[str, Any]:
    """本机 --list 用，非 Dify 出参。"""
    root = _norm_base_url(base_url)
    url = f"{root}/datasets/{dataset_id}/documents"
    r = requests.get(
        url,
        headers=_headers(api_key),
        params={"page": page, "limit": limit},
        timeout=timeout,
    )
    r.raise_for_status()
    return r.json()


def _cli_env_dataset_id() -> str:
    return _coerce_str(
        os.environ.get("DIFY_DATASET_ID")
        or os.environ.get("KNOWLEDGE_ID")
        or os.environ.get("DATASET_ID")
    )


def run_cli_smoke() -> int:
    base = _coerce_str(os.environ.get("DIFY_BASE_URL"))
    key = _coerce_str(
        os.environ.get("DIFY_API_KEY")
        or os.environ.get("DIFY_DATASET_API_KEY")
    )
    ds = _cli_env_dataset_id()
    ts = time.strftime("%Y%m%d_%H%M%S")
    r = main(
        dataset_id=ds,
        dify_base_url=base,
        dify_api_key=key,
        add_rule=f"# CLI smoke\n{ts}\n",
    )
    print(r)
    return 0 if r.get("success") == "true" else 1


def run_cli_list() -> int:
    base = _coerce_str(os.environ.get("DIFY_BASE_URL"))
    key = _coerce_str(
        os.environ.get("DIFY_API_KEY")
        or os.environ.get("DIFY_DATASET_API_KEY")
    )
    ds = _cli_env_dataset_id()
    if not (base and key and ds):
        print(
            "请设置 DIFY_BASE_URL、DIFY_API_KEY（或 DIFY_DATASET_API_KEY）、"
            "KNOWLEDGE_ID（或 DIFY_DATASET_ID）"
        )
        return 2
    try:
        data = list_documents(base_url=base, api_key=key, dataset_id=ds)
        docs = data.get("data", [])
        print(f"共 {len(docs)} 条（当前页）")
        for d in docs:
            print(
                f"  - {d.get('name')} | id={d.get('id')} | {d.get('indexing_status')}"
            )
        return 0
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return 1


def _cli_main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="知识库追加文档（Dify 代码节点）本机辅助命令")
    p.add_argument("--smoke", action="store_true", help="用环境变量调用 main()")
    p.add_argument("--list", action="store_true", help="列出知识库文档")
    args = p.parse_args(argv)
    if args.list:
        return run_cli_list()
    if args.smoke:
        return run_cli_smoke()
    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(_cli_main())
