"""
Dify 代码节点：xlsx Base64 → POST /v1/files/upload → **download_url 仅输出可在浏览器直接点击下载的地址**。

唯一做法（自托管）：
  1. 在部署机 `.env` 或 `docker compose exec api printenv SECRET_KEY` 取得 **SECRET_KEY**。
  2. 在 Dify 应用里建「密钥」变量，映射到本节点入参 **files_sign_secret**（与 SECRET_KEY 完全一致）。
  3. 若浏览器访问地址与 upload_base_url 的根不一致，把 **files_public_base** 设为与 **FILES_URL** 相同（无 /v1）。
  4. 上传成功后 **download_url** 形如：`http(s)://.../files/<id>/file-preview?timestamp&nonce&sign&as_attachment=true`，直接点开即可下。

若官方接口返回了已是 http(s) 的 **source_url / original_url / preview_url** 且非 /v1/files/ 预览，则直接使用该地址（少数环境）。

**upload_api_key** 仅用于上传；若未配置 files_sign_secret 且无法使用直链，本节点返回失败说明，不再返回 /v1 预览链（避免误点 401）。

入参：file、upload_base_url、upload_api_key、upload_user、upload_filename、**files_sign_secret**、files_public_base（可选）、upload_timeout。
出参：download_url、message。
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

_XLSX_MIME = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"


def _merge(inputs, kwargs: dict) -> dict:
    m: dict = {}
    if isinstance(inputs, dict):
        m.update(inputs)
        inner = inputs.get("inputs")
        if isinstance(inner, dict):
            m.update(inner)
    m.update(kwargs)
    inner2 = m.get("inputs")
    if isinstance(inner2, dict):
        m.update(inner2)
    return m


def _str(d: dict, keys: tuple[str, ...]) -> str:
    for k in keys:
        v = d.get(k)
        if v is not None and str(v).strip():
            return str(v).strip()
    return ""


def _env(keys: tuple[str, ...]) -> str:
    for k in keys:
        v = os.environ.get(k)
        if v and str(v).strip():
            return str(v).strip()
    return ""


def _api_key_for_bearer(raw_key: str) -> str:
    """去掉首尾空白及重复的 Bearer 前缀，供 Authorization 头使用。"""
    k = str(raw_key).strip()
    if k.lower().startswith("bearer "):
        k = k[7:].strip()
    return k


def _b64_decode(s: str) -> bytes:
    s = str(s).strip()
    if "base64," in s:
        s = s.split("base64,", 1)[-1].strip()
    pad = (-len(s)) % 4
    if pad:
        s += "=" * pad
    try:
        return base64.b64decode(s, validate=False)
    except Exception:
        return base64.urlsafe_b64decode(s)


def _v1_base(base: str) -> str:
    b = base.strip().rstrip("/")
    return b if b.lower().endswith("/v1") else f"{b}/v1"


def _public_base(v1: str) -> str:
    vb = v1.strip().rstrip("/")
    if vb.lower().endswith("/v1"):
        return vb[:-3].rstrip("/")
    return vb


def _ascii_filename(name: str) -> str:
    s = "".join(c if 32 <= ord(c) < 127 and c not in '\\/"|:?*' else "_" for c in name)
    return s.strip("_") or "export.xlsx"


def _multipart(user: str, filename: str, raw: bytes) -> tuple[bytes, str]:
    boundary = f"----------difyup{uuid.uuid4().hex}"
    crlf = b"\r\n"
    bnd = boundary.encode("ascii")
    fn = _ascii_filename(filename)
    head = (
        f'Content-Disposition: form-data; name="file"; filename="{fn}"\r\n'
        f"Content-Type: {_XLSX_MIME}\r\n\r\n"
    ).encode("utf-8")
    body = b"".join(
        [
            b"--" + bnd + crlf,
            b'Content-Disposition: form-data; name="user"\r\n\r\n',
            user.encode("utf-8") + crlf,
            b"--" + bnd + crlf,
            head,
            raw + crlf,
            b"--" + bnd + b"--" + crlf,
        ]
    )
    return body, f"multipart/form-data; boundary={boundary}"


def _post(url: str, headers: dict[str, str], body: bytes, ctype: str, timeout: int) -> tuple[int, dict | None, str]:
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", ctype)
    for k, v in headers.items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            txt = resp.read().decode("utf-8", errors="replace")
            try:
                return resp.getcode() or 200, json.loads(txt), ""
            except json.JSONDecodeError:
                return resp.getcode() or 200, None, txt[:800]
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")[:800]
        try:
            jo = json.loads(err)
        except json.JSONDecodeError:
            jo = None
        return e.code, jo if isinstance(jo, dict) else None, err
    except Exception as e:
        return -1, None, str(e)[:800]


def _sign_preview(fid: str, secret: str, pub: str) -> str:
    secret = str(secret).strip()
    ts = str(int(time.time()))
    nonce = os.urandom(16).hex()
    msg = f"file-preview|{fid}|{ts}|{nonce}"
    digest = hmac.new(secret.encode("utf-8"), msg.encode("utf-8"), hashlib.sha256).digest()
    sign = base64.urlsafe_b64encode(digest).decode()
    q = urllib.parse.urlencode(
        {"timestamp": ts, "nonce": nonce, "sign": sign, "as_attachment": "true"}
    )
    return f"{pub.rstrip('/')}/files/{fid}/file-preview?{q}"


def main(inputs=None, **kwargs):
    merged = _merge(inputs if isinstance(inputs, dict) else {}, kwargs)
    b64 = _str(merged, ("file", "arg1", "data", "body"))
    if not b64:
        return {"download_url": "", "message": "缺少 file 或 arg1（Base64）"}

    try:
        raw = _b64_decode(b64)
    except Exception as e:
        return {"download_url": "", "message": f"Base64 解码失败: {e}"}

    if len(raw) < 4 or raw[:2] != b"PK":
        return {"download_url": "", "message": "不是有效的 xlsx（ZIP 头应为 PK）"}

    base = _str(merged, ("upload_base_url", "file_upload_base_url", "BASE_URL", "dify_public_base")) or _env(
        ("UPLOAD_BASE_URL", "DIFY_BASE_URL")
    )
    key = _str(merged, ("upload_api_key", "api_key")) or _env(("DIFY_API_KEY", "UPLOAD_API_KEY"))
    if not base or not key:
        return {
            "download_url": "",
            "message": "缺少 upload_base_url（或 BASE_URL）与 upload_api_key（或环境变量 DIFY_API_KEY）",
        }

    user = _str(merged, ("upload_user", "user")) or "dify-export"
    filename = _str(merged, ("upload_filename",)) or "export.xlsx"
    try:
        timeout = int(merged.get("upload_timeout") or 180)
    except (TypeError, ValueError):
        timeout = 180
    timeout = max(10, min(timeout, 600))

    v1 = _v1_base(base)
    upload_url = f"{v1}/files/upload"
    body, ctype = _multipart(user, filename, raw)
    status, obj, raw_err = _post(
        upload_url,
        {"Authorization": f"Bearer {_api_key_for_bearer(key)}"},
        body,
        ctype,
        timeout,
    )
    if status not in (200, 201) or not isinstance(obj, dict):
        detail = raw_err
        if isinstance(obj, dict) and obj.get("message"):
            detail = str(obj.get("message"))
        return {"download_url": "", "message": f"上传失败 HTTP {status}: {detail}"}

    fid_raw = obj.get("id")
    fid = str(fid_raw).strip() if fid_raw is not None else ""
    http_direct = ""
    for uk in ("source_url", "original_url", "preview_url"):
        u = obj.get(uk)
        if isinstance(u, str) and u.strip().startswith(("http://", "https://")):
            u = u.strip()
            if "/v1/files/" not in u:
                http_direct = u
                break

    if http_direct:
        return {"download_url": http_direct, "message": "成功（接口返回的可直链下载地址）。"}

    if not fid:
        return {"download_url": "", "message": "上传成功但响应无 id，无法生成下载链。"}

    pub = _str(merged, ("files_public_base", "files_url")) or _public_base(v1)
    if not pub:
        return {"download_url": "", "message": "无法推导 files_public_base，请检查 upload_base_url。"}

    sec = _str(merged, ("files_sign_secret",)) or _env(
        ("DIFY_FILES_SIGN_SECRET", "FILES_SIGN_SECRET", "SECRET_KEY")
    )
    if not sec:
        return {
            "download_url": "",
            "message": (
                "要在浏览器里直接点链下载：必须在入参 **files_sign_secret** 填写与 Dify 服务端 **SECRET_KEY** "
                "完全相同的值（应用里用「密钥」变量传入）。可选 **files_public_base** 与 **FILES_URL**（无 /v1）一致。"
            ),
        }

    try:
        signed = _sign_preview(fid, sec, pub)
    except Exception as e:
        return {"download_url": "", "message": f"生成签名下载链失败: {e}"}

    if not signed:
        return {"download_url": "", "message": "生成签名下载链失败（结果为空）。"}

    return {"download_url": signed.strip(), "message": "成功：可点击 download_url 在浏览器中下载。"}


if __name__ == "__main__":
    print("在 Dify 中传入 file、upload_base_url、upload_api_key、files_sign_secret（= SECRET_KEY）后调用 main。")
