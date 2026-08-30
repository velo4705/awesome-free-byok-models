#!/usr/bin/env python3
"""
This Verifier allows to check endpoints using just an API_KEY and BASE_URL from .env, and is also configurable.
Do Fill the .env variables before proceeding to execute this script.
"""

import os
import re
import sys
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
import requests

# ======================= Configuration =======================

TEST_PROMPT = "State the word 'READY'."
MAX_TOKENS = 8
REQUEST_TIMEOUT = 30
MAX_RETRY_PASSES = 5
SUBMIT_DELAY = 2.0
RETRY_DELAY_MULTIPLIER = 1.5
SEQUENTIAL = True
MAX_WORKERS = 4

# 1 - Enable Free Filtering
# 0 - Disable Free Filtering (Deep Check)
FREE_FILTER_ENABLED = 0

# ======================= Endpoint Discovery =======================

MODEL_LIST_PATHS = [
    "/models",
    "/v1/models",
    "/v2/models",
    "/v3/models",
    "/api/models",
    "/api/v1/models",
    "/api/v2/models",
    "/api/v3/models",
    "/openai/models",
    "/openai/v1/models",
    "/text",
    "/status/models",
]

CHAT_PATHS = [
    "/chat/completions",
    "/v1/chat/completions",
    "/v2/chat/completions",
    "/v3/chat/completions",
    "/api/chat",
    "/api/v1/chat/completions",
    "/api/v2/chat/completions",
    "/api/v3/chat/completions",
    "/openai/chat/completions",
    "/openai/v1/chat/completions",
    "/completions",
    "/v1/completions",
    "/messages",
    "/generate/text/async",
]


def normalize_base(url):
    return (url or "").rstrip("/")


def resolve_endpoint(base, path):
    base = normalize_base(base)
    if path.startswith("/v1") and base.endswith("/v1"):
        path = path[3:]
    if path.startswith("/api") and base.endswith("/api"):
        path = path[4:]
    return f"{base}{path}"


def _auth_headers(key):
    if not key:
        return [{}]
    return [
        {"Authorization": f"Bearer {key}"},
        {"x-api-key": key},
        {"api-key": key},
    ]


def discover_model_list_endpoint(base, key):
    for path in MODEL_LIST_PATHS:
        url = resolve_endpoint(base, path)
        for headers in _auth_headers(key):
            try:
                r = requests.get(url, headers=headers, timeout=10)
                if r.status_code == 200:
                    return url
            except Exception:
                continue
    return None


def discover_chat_endpoint(base, key):
    for path in [""] + CHAT_PATHS:
        url = resolve_endpoint(base, path) if path else base
        for headers in _auth_headers(key):
            headers = {**headers, "Content-Type": "application/json"}
            payload = {"model": "__probe__", "messages": [{"role": "user", "content": "hi"}], "max_tokens": 1}
            try:
                r = requests.post(url, headers=headers, json=payload, timeout=10)
                if r.status_code in (200, 400, 401, 403, 422):
                    return url
            except Exception:
                continue
    return None


# ======================= Generic OpenAI-Compatible Test =======================

def test_openai_compatible(url, api_key, model_id, max_tokens=None):
    """Generic OpenAI-compatible chat test."""
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    payload = {"model": model_id, "messages": [{"role": "user", "content": TEST_PROMPT}], "max_tokens": max_tokens or MAX_TOKENS}
    start = time.time()
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
        latency = round(time.time() - start, 2)
        if r.status_code == 200:
            data = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
            choices = data.get("choices", []) if isinstance(data, dict) else []
            if choices:
                msg = choices[0].get("message") or choices[0].get("messages") or {}
                if isinstance(msg, list):
                    msg = msg[0] if msg else {}
                content = (msg.get("content") or "").strip().replace("\n", " ")
                return {"id": model_id, "ok": True, "latency": latency, "content": content, "vision": False, "retryable": False, "status": ""}
            return {"id": model_id, "ok": True, "latency": latency, "content": "[Empty Choice Structure]", "vision": False, "retryable": False, "status": ""}
        elif r.status_code in (429, 502, 503, 504):
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": True, "status": f"STATUS {r.status_code}"}
        else:
            snippet = r.text[:120].strip().replace("\n", " ")
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": False, "status": f"Status {r.status_code} ({snippet})"}
    except Exception:
        return {"id": model_id, "ok": False, "latency": round(time.time() - start, 2), "content": "", "vision": False, "retryable": True, "status": "EXCEPTION"}


# ======================= Special Provider Detection =======================

def is_gemini_base(base):
    return "generativelanguage.googleapis.com" in base


def is_cloudflare_base(base):
    return "cloudflare.com" in base


def is_cohere_base(base):
    return "cohere.com" in base


def is_ollama_base(base):
    return "ollama.com" in base


def is_zai_base(base):
    return "z.ai" in base or "zai" in base


def is_huggingface_base(base):
    return "huggingface.co" in base


def is_routeway_base(base):
    return "routeway" in base

def is_anyapi_base(base):
    return "anyapi" in base


def is_poixe_base(base):
    return "poixe" in base


def is_auriko_base(base):
    return "auriko" in base


def is_helyx_base(base):
    return "helyx" in base

def is_zylo_base(base):
    return "zylo" in base

def is_electronhub_base(base):
    return "electronhub" in base

def is_voidai_base(base):
    return "voidai" in base

def is_navy_base(base):
    return "navy" in base or "api.navy" in base

def is_freeai_base(base):
    return "free.ai" in base

# ======================= Gemini =======================

def fetch_gemini_models(base_url, api_key):
    url = f"{base_url.rstrip('/')}/models?key={api_key}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return []
        data = r.json()
        return [m.get("name") for m in data.get("models", []) if "generateContent" in m.get("supportedGenerationMethods", [])]
    except Exception:
        return []


def test_gemini_model(base_url, api_key, model_name):
    url = f"{base_url.rstrip('/')}/{model_name}:generateContent?key={api_key}"
    payload = {"contents": [{"parts": [{"text": TEST_PROMPT}]}]}
    start = time.time()
    try:
        r = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=REQUEST_TIMEOUT)
        latency = round(time.time() - start, 2)
        if r.status_code == 200:
            try:
                reply = (r.json()["candidates"][0]["content"]["parts"][0].get("text") or "").strip().replace("\n", " ")
            except Exception:
                reply = ""
            return {"id": model_name, "ok": True, "latency": latency, "content": reply, "vision": False, "retryable": False, "status": ""}
        elif r.status_code in (429, 502, 503, 504):
            return {"id": model_name, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": True, "status": f"STATUS {r.status_code}"}
        else:
            snippet = r.text[:120].strip().replace("\n", " ")
            return {"id": model_name, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": False, "status": f"Status {r.status_code} ({snippet})"}
    except Exception:
        return {"id": model_name, "ok": False, "latency": round(time.time() - start, 2), "content": "", "vision": False, "retryable": True, "status": "EXCEPTION"}


# ======================= Cloudflare Workers AI =======================

def fetch_cloudflare_models(account_id, api_key):
    models_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/models/search"
    try:
        r = requests.get(models_url, headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        if r.status_code == 200:
            raw = r.json().get("result", [])
            task_filtered = [m.get("name") for m in raw if m.get("task", {}).get("name") == "Text Generation"]
            if task_filtered:
                return task_filtered
            return [m.get("name") or m.get("id") for m in raw]
        return []
    except Exception:
        return []


def test_cloudflare_model(account_id, api_key, model_id):
    chat_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": model_id, "messages": [{"role": "user", "content": TEST_PROMPT}], "max_tokens": 16, "temperature": 0.0}
    start = time.time()
    try:
        r = requests.post(chat_url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
        latency = round(time.time() - start, 2)
        if r.status_code == 200:
            result = r.json().get("result", {})
            choices = result.get("choices", [])
            if choices:
                content = (choices[0].get("message", {}).get("content") or "").strip().replace("\n", " ")
            else:
                content = result.get("response", "")
            return {"id": model_id, "ok": True, "latency": latency, "content": content, "vision": False, "retryable": False, "status": ""}
        elif r.status_code in (429, 502, 503, 504):
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": True, "status": f"STATUS {r.status_code}"}
        else:
            snippet = r.text[:120].strip().replace("\n", " ")
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": False, "status": f"Status {r.status_code} ({snippet})"}
    except Exception:
        return {"id": model_id, "ok": False, "latency": round(time.time() - start, 2), "content": "", "vision": False, "retryable": True, "status": "EXCEPTION"}


# ======================= Cohere =======================

def fetch_cohere_models(api_key):
    url = "https://api.cohere.com/v1/models"
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        if r.status_code == 200:
            data = r.json()
            models = data if isinstance(data, list) else data.get("models", [])
            return [m.get("name") or m.get("id") for m in models if m.get("name") or m.get("id")]
        return []
    except Exception:
        return []


def test_cohere_model(api_key, model_id):
    url = "https://api.cohere.com/v2/chat"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": model_id, "messages": [{"role": "user", "content": TEST_PROMPT}], "max_tokens": 16, "temperature": 0.0}
    start = time.time()
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
        latency = round(time.time() - start, 2)
        if r.status_code == 200:
            body = r.json()
            blocks = body.get("message", {}).get("content", [])
            if blocks:
                content = blocks[0].get("text", "").strip().replace("\n", " ")
            else:
                content = (body.get("text") or "").strip().replace("\n", " ")
            return {"id": model_id, "ok": True, "latency": latency, "content": content, "vision": False, "retryable": False, "status": ""}
        elif r.status_code in (429, 502, 503, 504):
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": True, "status": f"STATUS {r.status_code}"}
        else:
            snippet = r.text[:120].strip().replace("\n", " ")
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": False, "status": f"Status {r.status_code} ({snippet})"}
    except Exception:
        return {"id": model_id, "ok": False, "latency": round(time.time() - start, 2), "content": "", "vision": False, "retryable": True, "status": "EXCEPTION"}


# ======================= Ollama Cloud =======================

def fetch_ollama_models(api_key):
    url = "https://api.ollama.com/v1/models"
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return [m.get("id") for m in data.get("data", []) if m.get("id")]
        return []
    except Exception:
        return []


def test_ollama_model(api_key, model_id):
    url = "https://api.ollama.com/api/chat"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": model_id, "messages": [{"role": "user", "content": TEST_PROMPT}], "stream": False}
    start = time.time()
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
        latency = round(time.time() - start, 2)
        if r.status_code == 200:
            body = r.json()
            reply = (body.get("message", {}).get("content") or "").strip().replace("\n", " ")
            return {"id": model_id, "ok": True, "latency": latency, "content": reply, "vision": False, "retryable": False, "status": ""}
        elif r.status_code in (429, 502, 503, 504):
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": True, "status": f"STATUS {r.status_code}"}
        else:
            snippet = r.text[:120].strip().replace("\n", " ")
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "vision": False, "retryable": False, "status": f"Status {r.status_code} ({snippet})"}
    except Exception:
        return {"id": model_id, "ok": False, "latency": round(time.time() - start, 2), "content": "", "vision": False, "retryable": True, "status": "EXCEPTION"}


# ======================= Model Fetching (OpenAI-Compatible) =======================

def fetch_openai_models(url, api_key):
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        if r.status_code == 200:
            data = r.json()
            models = data if isinstance(data, list) else data.get("data", [])
            return [m.get("id") for m in models if m.get("id")]
        return []
    except Exception:
        return []


# ======================= Fetch Functions =======================

def fetch_zai_models(api_key):
    ids = fetch_openai_models("https://api.z.ai/api/paas/v4/models", api_key)
    for m in ["glm-4.5-flash", "glm-4.7-flash"]:
        if m not in ids:
            ids.append(m)
    return ids


def fetch_huggingface_models(api_key):
    return fetch_openai_models("https://router.huggingface.co/v1/models", api_key)


def fetch_routeway_models(api_key):
    return fetch_openai_models("https://api.routeway.ai/v1/models", api_key)


def fetch_anyapi_models(api_key):
    return fetch_openai_models("https://api.anyapi.ai/v1/models", api_key)


def fetch_poixe_models(api_key):
    url = "https://api.poixe.com/v1/models"
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        if r.status_code == 200:
            data = r.json()
            models = data if isinstance(data, list) else data.get("data", [])
            return [f"{m['id']}:free" for m in models if isinstance(m, dict) and m.get("id") and not any(w in m['id'].lower() for w in NON_TEXT_KW)]
        return []
    except Exception:
        return []


def fetch_auriko_models(api_key):
    url = "https://api.auriko.ai/v1/models"
    blocked_prefixes = ("gemma-",)
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        if r.status_code == 200:
            data = r.json()
            models = data if isinstance(data, list) else data.get("data", [])
            free_models = []
            for m in models:
                if not isinstance(m, dict) or not m.get("id"):
                    continue
                mid = m["id"]
                if any(mid.startswith(p) for p in blocked_prefixes):
                    continue
                if any(w in mid.lower() for w in NON_TEXT_KW):
                    continue
                providers = m.get("providers", [])
                for p in providers:
                    if p.get("input_price") == 0 and p.get("output_price") == 0:
                        free_models.append(mid)
                        break
            return free_models
        return []
    except Exception:
        return []


def fetch_helyx_models():
    url = "https://helyxai.space/models-list"
    try:
        r = requests.get(url, timeout=10)
        raw = r.content.decode("utf-8", errors="replace")
        slugs = [s.strip("'\"") for s in re.findall(r'slug=([^\"&]+)', raw)]
        return list(dict.fromkeys(s for s in slugs if s))
    except Exception:
        return []


def fetch_zylo_models(api_key):
    url = "https://api.zyloai.net/v1/models"
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        if r.status_code == 200:
            data = r.json()
            models_list = data.get("text", [])
            basic = []
            for m in models_list:
                if not isinstance(m, dict) or not m.get("id"):
                    continue
                if m.get("min_plan") != "BASIC":
                    continue
                mid = m["id"]
                if any(w in mid.lower() for w in NON_TEXT_KW):
                    continue
                basic.append(mid)
            return basic
        return []
    except Exception:
        return []

def fetch_freeai_models(api_key):
    return ["qwen7b", "qwen3-8b", "qwen-vl", "qwen25-vl"]

# ======================= Filtering Logic =======================

NON_TEXT_KW = (
    "embed", "rerank", "similarity", "transcribe", "moderation",
    "audio", "tts", "whisper", "speech", "music", "song", "lyrics",
    "image", "i2i", "t2i", "i2v", "t2v", "video", "3d",
    "lyria", "voice", "sound", "melody", "instrument",
    "flux", "seedance", "seedream", "veo", "kling", "leonardo",
    "sora", "pika", "pollo", "runway", "bulbul", "saaras",
    "vidu", "wanx", "dreamina",
)

VISION_KW = ("vision", "vl", "multimodal", "ocr")

FREE_MARKERS = (":free", "-free", "_free", "[free]", "free-")


def is_vision_model(mid):
    low = mid.lower()
    return any(w in low for w in VISION_KW)


def is_non_text_model(mid):
    low = mid.lower()
    return any(w in low for w in NON_TEXT_KW)


def is_free_by_marker(mid):
    low = mid.lower()
    return any(marker in low for marker in FREE_MARKERS) or "free" in low


def is_free_by_pricing(m):
    pricing = m.get("pricing") or {}

    if isinstance(pricing, dict):
        for k in ("prompt", "input", "completion", "output", "prompt_price", "completion_price"):
            v = pricing.get(k)
            if v == 0 or v == "0" or v == "" or v == 0.0:
                return True

    if isinstance(pricing, list):
        for p in pricing:
            if isinstance(p, dict):
                for k in ("input_price", "output_price", "prompt_price", "completion_price"):
                    v = p.get(k)
                    if v == 0 or v == "0" or v == "" or v == 0.0:
                        return True

    providers = m.get("providers") or []
    for p in providers:
        if isinstance(p, dict) and p.get("input_price") == 0 and p.get("output_price") == 0:
            return True

    return False


def is_free_by_tags(m):
    tags = m.get("tags") or []
    return any("free" in str(t).lower() for t in tags)


def is_free_by_plan(m):
    plan = (m.get("min_plan") or m.get("plan") or "").upper()
    return plan in ("FREE", "BASIC", "STARTER", "HOBBY")


def is_free_model(m):
    if isinstance(m, str):
        return is_free_by_marker(m)

    mid = (m.get("id") or m.get("name") or m.get("slug") or "").lower()
    if is_free_by_marker(mid):
        return True
    if is_free_by_pricing(m):
        return True
    if is_free_by_tags(m):
        return True
    if is_free_by_plan(m):
        return True
    return False


def is_eligible_model(m):
    if isinstance(m, str):
        mid = m
        meta = {}
    else:
        mid = (m.get("id") or m.get("name") or m.get("slug") or m.get("model") or "")
        meta = m

    if not mid:
        return False

    if is_non_text_model(mid):
        return False

    if not FREE_FILTER_ENABLED:
        return True

    return is_free_model(meta if meta else mid)


def get_eligible_models(raw_models):
    eligible = []
    if FREE_FILTER_ENABLED:
        for m in raw_models:
            if is_eligible_model(m):
                mid = m if isinstance(m, str) else (m.get("id") or m.get("name") or m.get("slug") or m.get("model"))
                if mid:
                    eligible.append({"id": mid, "meta": m if not isinstance(m, str) else {}})
    if not eligible:
        for m in raw_models:
            mid = m if isinstance(m, str) else (m.get("id") or m.get("name") or m.get("slug") or m.get("model"))
            if not mid:
                continue
            if is_non_text_model(mid):
                continue
            eligible.append({"id": mid, "meta": m if not isinstance(m, str) else {}})
    return eligible


# ======================= Model Fetching (Generic) =======================

def fetch_models_generic(models_url, key):
    for headers in _auth_headers(key):
        try:
            r = requests.get(models_url, headers=headers, timeout=10)
            if r.status_code == 200:
                data = r.json()
                if isinstance(data, list):
                    return data
                if isinstance(data, dict):
                    for k in ("data", "models", "text"):
                        if k in data:
                            return data[k]
                    if "id" in data or "name" in data:
                        return [data]
        except Exception:
            continue
    return []


# ======================= Report =======================

def write_report(path, summary):
    passed = summary["passed"]
    total = summary["total"]
    lines = []
    lines.append("=" * 80)
    lines.append("VERIFIED MODELS — Provider")
    lines.append("=" * 80)
    if not passed:
        lines.append("(no models verified)")
    else:
        idx_w = len(str(len(passed)))
        model_w = max(len(r["id"]) for r in passed)
        lines.append(f"{'#':<{idx_w}}  {'MODEL':<{model_w}}  {'LATENCY':<9}  RESPONSE")
        lines.append("-" * 80)
        for i, r in enumerate(passed, 1):
            resp = r["content"].replace("\n", " ")
            if len(resp) > 60:
                resp = resp[:57] + "..."
            tag = " [vision]" if r.get("vision") else ""
            lines.append(f"{i:<{idx_w}}  {r['id']:<{model_w}}  {str(r['latency']) + 's':<9}  {resp}{tag}")
        lines.append("-" * 80)
    lines.append(f"Verified: {len(passed)} / {total}")
    text = "\n".join(lines) + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return text


# ======================= Main =======================

def run():
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    for env_name in (".env", ".env.txt"):
        env_path = os.path.join(SCRIPT_DIR, env_name)
        if os.path.exists(env_path):
            load_dotenv(env_path, override=True)
            break

    base_url = os.getenv("BASE_URL", "").strip()
    api_key = os.getenv("API_KEY", "").strip()

    if not base_url:
        print("⚠️  No BASE_URL found in .env. Add BASE_URL=... and API_KEY=...")
        return

    base_url = normalize_base(base_url)

    # ================= Gemini =================
    if is_gemini_base(base_url):
        model_ids = fetch_gemini_models(base_url, api_key)
        eligible = [{"id": mid, "meta": {}} for mid in model_ids]
        test_fn = lambda mid: test_gemini_model(base_url, api_key, mid)

    # ================= Cloudflare Workers AI =================
    elif is_cloudflare_base(base_url):
        account_id = os.getenv("ACCOUNT_ID", "").strip()
        if not account_id:
            print("⚠️  No ACCOUNT_ID found in .env. Add ACCOUNT_ID=... for Cloudflare Workers AI.")
            return
        model_ids = fetch_cloudflare_models(account_id, api_key)
        eligible = [{"id": mid, "meta": {}} for mid in model_ids]
        test_fn = lambda mid: test_cloudflare_model(account_id, api_key, mid)

    # ================= Cohere =================
    elif is_cohere_base(base_url):
        model_ids = fetch_cohere_models(api_key)
        eligible = [{"id": mid, "meta": {}} for mid in model_ids]
        test_fn = lambda mid: test_cohere_model(api_key, mid)

    # ================= Ollama Cloud =================
    elif is_ollama_base(base_url):
        model_ids = fetch_ollama_models(api_key)
        eligible = [{"id": mid, "meta": {}} for mid in model_ids]
        test_fn = lambda mid: test_ollama_model(api_key, mid)

    # ================= Z.AI =================
    elif is_zai_base(base_url):
        model_ids = fetch_zai_models(api_key)
        eligible = [{"id": mid, "meta": {}} for mid in model_ids]
        test_fn = lambda mid: test_openai_compatible("https://api.z.ai/api/paas/v4/chat/completions", api_key, mid)

    # ================= Hugging Face =================
    elif is_huggingface_base(base_url):
        model_ids = fetch_huggingface_models(api_key)
        filtered = [m for m in model_ids if not any(w in m.lower() for w in ("embed", "rerank", "similarity"))]
        eligible = [{"id": mid, "meta": {}} for mid in filtered]
        test_fn = lambda mid: test_openai_compatible("https://router.huggingface.co/v1/chat/completions", api_key, mid)

    # ================= Routeway =================
    elif is_routeway_base(base_url):
        model_ids = fetch_routeway_models(api_key)
        filtered = [m for m in model_ids if ":free" in m.lower() and not any(w in m.lower() for w in ("embed", "rerank", "similarity"))]
        eligible = [{"id": mid, "meta": {}} for mid in filtered]
        test_fn = lambda mid: test_openai_compatible("https://api.routeway.ai/v1/chat/completions", api_key, mid, 8)

    # ================= AnyAPI AI =================
    elif is_anyapi_base(base_url):
        model_ids = fetch_anyapi_models(api_key)
        filtered = [m for m in model_ids if ":free" in m.lower() and not any(w in m.lower() for w in ("embed", "rerank", "similarity"))]
        eligible = [{"id": mid, "meta": {}} for mid in filtered]
        test_fn = lambda mid: test_openai_compatible("https://api.anyapi.ai/v1/chat/completions", api_key, mid)

    # ================= Poixe AI =================
    elif is_poixe_base(base_url):
        model_ids = fetch_poixe_models(api_key)
        eligible = [{"id": mid, "meta": {}} for mid in model_ids]
        test_fn = lambda mid: test_openai_compatible("https://api.poixe.com/v1/chat/completions", api_key, mid)

    # ================= Auriko =================
    elif is_auriko_base(base_url):
        model_ids = fetch_auriko_models(api_key)
        eligible = [{"id": mid, "meta": {}} for mid in model_ids]
        test_fn = lambda mid: test_openai_compatible("https://api.auriko.ai/v1/chat/completions", api_key, mid)

    # ================= Helyx =================
    elif is_helyx_base(base_url):
        model_ids = fetch_helyx_models()
        eligible = [{"id": mid, "meta": {}} for mid in model_ids]
        test_fn = lambda mid: test_openai_compatible("https://helyxai.space/v1/chat/completions", api_key, mid)

    # ================= Zylo AI =================
    elif is_zylo_base(base_url):
        model_ids = fetch_zylo_models(api_key)
        eligible = [{"id": mid, "meta": {}} for mid in model_ids]
        test_fn = lambda mid: test_openai_compatible("https://api.zyloai.net/v1/chat/completions", api_key, mid)

    # ================= ElectronHub =================
    elif is_electronhub_base(base_url):
        model_ids = fetch_openai_models("https://api.electronhub.ai/v1/models", api_key)
        filtered = [m for m in model_ids if not any(w in m.lower() for w in ("embed", "rerank", "similarity", "whisper", "tts", "asr", "image", "audio", "video"))]
        eligible = [{"id": mid, "meta": {}} for mid in filtered]
        test_fn = lambda mid: test_openai_compatible("https://api.electronhub.ai/v1/chat/completions", api_key, mid)
        current_delay = 12.0   # 5 RPM

    # ================= Void AI =================
    elif is_voidai_base(base_url):
        eligible = [{"id": mid, "meta": {}} for mid in fetch_openai_models("https://api.voidai.app/v1/models", api_key) if not any(w in mid.lower() for w in NON_TEXT_KW)]
        test_fn = lambda mid: test_openai_compatible("https://api.voidai.app/v1/chat/completions", api_key, mid)

    # ================= Navy API =================
    elif is_navy_base(base_url):
        eligible = [{"id": mid, "meta": {}} for mid in fetch_openai_models("https://api.navy/v1/models", api_key) if not any(w in mid.lower() for w in NON_TEXT_KW)]
        test_fn = lambda mid: test_openai_compatible("https://api.navy/v1/chat/completions", api_key, mid)

    # ================= Free.ai =================
    elif is_freeai_base(base_url):
        eligible = [{"id": mid, "meta": {}} for mid in fetch_freeai_models(api_key)]
        test_fn = lambda mid: test_openai_compatible("https://api.free.ai/v1/chat/completions", api_key, mid)

    # ================= Generic OpenAI-compatible =================
    else:
        models_url = discover_model_list_endpoint(base_url, api_key)
        if not models_url:
            print(f"❌ Could not find model list endpoint for {base_url}")
            return

        raw_models = fetch_models_generic(models_url, api_key)
        if not raw_models:
            print(f"⚠️  No models found at {models_url}")
            return

        eligible = get_eligible_models(raw_models)

        chat_url = discover_chat_endpoint(base_url, api_key)
        if not chat_url:
            print(f"❌ Could not find chat endpoint for {base_url}")
            return

        test_fn = lambda mid: test_openai_compatible(chat_url, api_key, mid)

    if not eligible:
        print("⚠️  No eligible models found.")
        return

    print()
    print("=" * 80)
    print("🔬 Testing Provider models")
    print("=" * 80)
    print(f"🔗 Queued {len(eligible)} free models out of {len(eligible)} total.")
    print()

    passed = []
    failed = 0
    retry_queue = eligible[:]

    for retry_pass in range(MAX_RETRY_PASSES + 1):
        if not retry_queue:
            break
        delay = SUBMIT_DELAY * (RETRY_DELAY_MULTIPLIER ** retry_pass)
        if retry_pass > 0:
            print(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
        next_retry = []
        for item in retry_queue:
            mid = item["id"]
            r = test_fn(mid)
            if r["retryable"]:
                next_retry.append(item)
            elif r["ok"]:
                passed.append(r)
            else:
                failed += 1
            if r["retryable"]:
                print(f"  🔄 {mid} {r['status']} — queued for retry")
            elif r["ok"]:
                print(f"  ✅ {mid} ({r['latency']}s) -> \"{r['content']}\"")
            else:
                print(f"  ❌ {mid} FAILED -> {r['status']}")
            time.sleep(delay)
        retry_queue = next_retry

    print()
    print(f"🏁 {len(passed)} passed, {failed} failed")

    summary = {"passed": passed, "failed": failed, "total": len(eligible), "provider": base_url}
    date_tag = datetime.now().strftime("%Y-%m-%d")
    out = os.path.join(SCRIPT_DIR, f"verified_models_{date_tag}.txt")
    report = write_report(out, summary)
    print()
    print(report)
    print(f"💾 Verified-models report written to '{out}'.")


if __name__ == "__main__":
    run()