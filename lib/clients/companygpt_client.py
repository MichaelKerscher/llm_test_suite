# lib/clients/companygpt_client.py

import os
import json
import mimetypes
import hashlib
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("COMPANYGPT_BASE_URL", "").rstrip("/")
ORG_ID = os.getenv("COMPANYGPT_ORG_ID")
API_KEY = os.getenv("COMPANYGPT_API_KEY")

DEFAULT_MODE = os.getenv("COMPANYGPT_DEFAULT_MODE", "BASIC")
INTERNAL_SYSTEM_PROMPT = os.getenv("COMPANYGPT_INTERNAL_SYSTEM_PROMPT", "true").lower() == "true"

DATA_COLLECTION_ID = os.getenv("COMPANYGPT_DATA_COLLECTION_ID")
HASH_PREFIX_LEN = int(os.getenv("COMPANYGPT_HASH_PREFIX_LEN", "12"))

GENERATOR_ASSISTANT_ID = os.getenv("COMPANYGPT_GENERATOR_ASSISTANT_ID")
JUDGE_ASSISTANT_ID = os.getenv("COMPANYGPT_JUDGE_ASSISTANT_ID")

UPLOAD_TIMEOUT = 900
CHAT_TIMEOUT = 900

if not BASE_URL or not ORG_ID or not API_KEY:
    raise EnvironmentError("CompanyGPT .env Variablen fehlen oder sind unvollständig.")
if not DATA_COLLECTION_ID:
    raise EnvironmentError("COMPANYGPT_DATA_COLLECTION_ID ist nicht gesetzt (benötigt für Media-Tests).")

HEADERS_AUTH = {"api-organization-id": ORG_ID, "api-key": API_KEY}
HEADERS_JSON = {**HEADERS_AUTH, "Content-Type": "application/json"}

_UPLOAD_CACHE: dict[str, str] = {}


def append_context_to_prompt(
    prompt: str,
    context: dict | None,
    raw_text_context: str | None = None,
) -> str:
    """
    Context injection:
    - raw_text_context (S0_raw / S0_unstructured): plain text → [KONTEXT] tag
    - context (S0 / S1 / S2): structured dict → serialized JSON → [CONTEXT_JSON] tag
    """
    if raw_text_context:
        return prompt + "\n\n[KONTEXT]\n<<<\n" + raw_text_context + "\n>>>\n"
    if not context:
        return prompt
    try:
        ctx_str = json.dumps(context, ensure_ascii=False, sort_keys=True, indent=2)
    except Exception:
        ctx_str = str(context)
    return prompt + "\n\n[CONTEXT_JSON]\n<<<\n" + ctx_str + "\n>>>\n"


def _sha256_hex(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _make_upload_filename(original_name: str, sha256_hex: str) -> str:
    prefix = sha256_hex[:max(1, HASH_PREFIX_LEN)]
    safe_name = original_name.replace("\\", "_").replace("/", "_")
    return f"{prefix}_{safe_name}"


def _wait_until_media_visible(model_id: str, unique_title: str, max_wait_seconds: int = 15) -> None:
    delays = [2, 4, 8]
    start = time.time()
    probe_prompt = "Antworte nur mit: OK"
    for d in delays:
        try:
            out = _chat_no_stream(
                model_id=model_id, prompt=probe_prompt, temperature=0.0,
                selected_mode=DEFAULT_MODE, selected_files=[unique_title],
                selected_data_collections=[DATA_COLLECTION_ID],
            )
            if out and "keine" not in out.lower() and "sichtbar" not in out.lower():
                return
        except Exception:
            pass
        if time.time() - start + d > max_wait_seconds:
            return
        time.sleep(d)


def _upload_media(media_path: str, data_collection_id: str) -> str:
    if not media_path:
        raise ValueError("media_path fehlt.")
    p = Path(media_path)
    if not p.is_file():
        raise FileNotFoundError(f"Datei nicht gefunden: {p}")
    abs_path = str(p.resolve())
    if abs_path in _UPLOAD_CACHE:
        return _UPLOAD_CACHE[abs_path]
    digest = _sha256_hex(p)
    upload_filename = _make_upload_filename(p.name, digest)
    mime, _ = mimetypes.guess_type(abs_path)
    if not mime:
        mime = "application/octet-stream"
    url = f"{BASE_URL}/api/v1/public/uploadMedia"
    params = {"dataCollectionId": data_collection_id, "replace": "false"}
    with p.open("rb") as f:
        files = {"media": (upload_filename, f, mime)}
        r = requests.post(url, headers=HEADERS_AUTH, params=params, files=files, timeout=UPLOAD_TIMEOUT)
    if r.status_code == 409:
        unique_title = f"{data_collection_id}_{upload_filename}"
        _UPLOAD_CACHE[abs_path] = unique_title
        return unique_title
    if r.status_code >= 400:
        raise RuntimeError(f"uploadMedia failed: {r.status_code} {r.text}")
    data = r.json()
    file_obj = data[0] if isinstance(data, list) and data else (data if isinstance(data, dict) else {})
    api_unique = file_obj.get("uniqueTitle")
    unique_title = api_unique or f"{data_collection_id}_{upload_filename}"
    _UPLOAD_CACHE[abs_path] = unique_title
    return unique_title


def _chat_no_stream(
    model_id: str,
    prompt: str,
    temperature: float = 0.2,
    selected_mode: str = "BASIC",
    selected_files: list[str] | None = None,
    selected_data_collections: list[str] | None = None,
    assistant_id: str | None = None,
    internal_system_prompt_override: bool | None = None,
) -> str:
    url = f"{BASE_URL}/api/v1/public/chatNoStream"
    use_internal = INTERNAL_SYSTEM_PROMPT if internal_system_prompt_override is None else internal_system_prompt_override
    params = {"internalSystemPrompt": "true" if use_internal else "false"}
    payload = {
        "model": {"id": model_id},
        "messages": [{"role": "user", "content": prompt, "references": [], "sources": []}],
        "roleId": "",
        "temperature": temperature,
        "selectedMode": selected_mode,
        "selectedFiles": selected_files or [],
        "selectedDataCollections": selected_data_collections or [],
    }
    if assistant_id:
        payload["selectedAssistantId"] = assistant_id
    response = requests.post(url, headers=HEADERS_JSON, params=params, data=json.dumps(payload), timeout=CHAT_TIMEOUT)
    response.raise_for_status()
    return response.json().get("content", "")


def generate(
    input_type: str,
    prompt: str,
    model: str,
    image_path: str = None,
    audio_path: str = None,
    video_path: str = None,
    context: dict = None,
    raw_text_context: str | None = None,
    temperature: float = 0.2,
    selected_mode: str | None = None,
    internal_system_prompt: bool | None = None,
) -> str:
    try:
        prompt_with_context = append_context_to_prompt(prompt, context, raw_text_context)
        mode = selected_mode or DEFAULT_MODE

        if input_type == "text":
            return _chat_no_stream(
                model_id=model, prompt=prompt_with_context, temperature=temperature,
                selected_mode=mode, selected_files=[], selected_data_collections=[],
                assistant_id=GENERATOR_ASSISTANT_ID,
                internal_system_prompt_override=internal_system_prompt,
            )

        if input_type == "image":
            if not image_path:
                return "[CompanyGPT] image_path fehlt."
            unique_title = _upload_media(image_path, DATA_COLLECTION_ID)
            _wait_until_media_visible(model, unique_title)
            return _chat_no_stream(
                model_id=model, prompt=prompt_with_context, temperature=temperature,
                selected_mode=mode, selected_files=[unique_title],
                selected_data_collections=[DATA_COLLECTION_ID],
                assistant_id=GENERATOR_ASSISTANT_ID,
                internal_system_prompt_override=internal_system_prompt,
            )

        if input_type == "audio":
            if not audio_path:
                return "[CompanyGPT] audio_path fehlt."
            unique_title = _upload_media(audio_path, DATA_COLLECTION_ID)
            _wait_until_media_visible(model, unique_title)
            return _chat_no_stream(
                model_id=model, prompt=prompt_with_context, temperature=temperature,
                selected_mode=mode, selected_files=[unique_title],
                selected_data_collections=[DATA_COLLECTION_ID],
                assistant_id=GENERATOR_ASSISTANT_ID,
                internal_system_prompt_override=internal_system_prompt,
            )

        return f"[CompanyGPT] Input-Typ '{input_type}' in Step 06 nicht unterstützt."

    except Exception as e:
        return f"[CompanyGPT ERROR] {e}"


def _strip_code_fences(text: str) -> str:
    if not isinstance(text, str):
        return text
    s = text.strip()
    if not s.startswith("```"):
        return s
    lines = s.splitlines()
    if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].strip() == "```":
        return "\n".join(lines[1:-1]).strip()
    first_nl = s.find("\n")
    last_fence = s.rfind("```")
    if first_nl != -1 and last_fence != -1 and last_fence > first_nl:
        return s[first_nl:last_fence].strip()
    return s


def judge(
    prompt: str,
    model: str,
    temperature: float = 0.1,
    selected_mode: str | None = None,
    internal_system_prompt: bool | None = None,
) -> str:
    try:
        mode = selected_mode or DEFAULT_MODE
        raw = _chat_no_stream(
            model_id=model, prompt=prompt, temperature=temperature,
            selected_mode=mode, selected_files=[], selected_data_collections=[],
            assistant_id=JUDGE_ASSISTANT_ID,
            internal_system_prompt_override=internal_system_prompt,
        )
        return _strip_code_fences(raw)
    except Exception as e:
        return f"[CompanyGPT JUDGE ERROR] {e}"