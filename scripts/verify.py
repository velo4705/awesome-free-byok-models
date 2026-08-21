import os
import sys
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
for env_name in (".env", ".env.txt"):
    env_path = os.path.join(SCRIPT_DIR, env_name)
    if os.path.exists(env_path):
        load_dotenv(env_path, override=True)

PROVIDER_NAME = "Provider"
BASE_URL_ENV = "BASE_URL"
API_KEY_ENV = "API_KEY"

BASE_URL_TEMPLATE = None
URL_PLACEHOLDERS = {"ACCOUNT_ID": "ACCOUNT_ID"}

MODEL_FETCH_PATH = "/v1/models"
CHAT_PATH = "/v1/chat/completions"

FREE_FILTER_MODE = "auto"
FREE_TOKEN = "free-"

MODEL_LIST = []

BLOCKED_KEYWORDS = ()
NON_CHAT_KW = ("embed", "rerank", "similarity", "transcribe", "moderation", "image", "audio", "video", "tts", "whisper")
ODIROUTER_FREE_PREFIX = "free-"
ODIROUTER_BLOCKED = (
    "image","i2i","t2i","i2v","t2v","r2v","nano-banana","midjourney","flux","seedream","seedance","seed-",
    "hailuo","pixverse","vidu","happyhorse","wan","kling","mureka","tts","speech","audio","3d","super-resolution","grok-imagine",
    "song","lyrics","voice","subjects","motion-control","lip-sync","embed","rerank","similarity",
)
OPENCODE_ZEN_EXTRA_FREE = ["big-pickle"]

def filter_model(model_id):
    return model_id.lower().startswith(FREE_TOKEN)

TEST_PROMPT = "State the word 'READY'."
MAX_TOKENS = 8
REQUEST_TIMEOUT = 30
MAX_RETRY_PASSES = 5
SUBMIT_DELAY = 2.0
RETRY_DELAY_MULTIPLIER = 1.5

GEMINI_RPM = 10
SEQUENTIAL = True
MAX_WORKERS = 4

# Fallback for TokenReply
FREE_MODELS = [
    "grok-build-0.1","grok-4.3","deepseek-ai/deepseek-v4-pro","nvidia/nemotron-3-ultra-550b-a55b",
    "deepseek-ai/deepseek-v4-flash","moonshotai/kimi-k2.6","minimaxai/minimax-m2.7","z-ai/glm-5.1",
    "google/gemma-4-31b-it","google/gemma-4-26b-a4b-it","qwen/qwen3.5-397b-a17b","stepfun-ai/step-3.5-flash",
    "openai/gpt-oss-120b","google/gemma-3n-e2b-it","google/gemma-3n-e4b-it","stepfun-ai/step-3.7-flash",
    "grok-4.20-0309-reasoning","grok-4.20-0309-non-reasoning","grok-4.20-multi-agent-0309",
]

def build_base_url():
    raw = os.getenv(BASE_URL_ENV)
    if BASE_URL_TEMPLATE is None:
        if raw and "{account_id}" in raw.lower():
            acct = os.getenv("ACCOUNT_ID")
            if acct:
                raw = raw.replace("{account_id}", acct).replace("{ACCOUNT_ID}", acct)
            else:
                pass
        return raw
    subs = {}
    for token, env_key in URL_PLACEHOLDERS.items():
        val = os.getenv(env_key)
        if not val:
            raise SystemExit(
                f"⚠️  {PROVIDER_NAME}: env var '{env_key}' is required by BASE_URL_TEMPLATE but is not set."
            )
        subs[token] = val
        subs[token.lower()] = val
        subs[token.upper()] = val
    try:
        return BASE_URL_TEMPLATE.format(**subs)
    except KeyError:
        return BASE_URL_TEMPLATE.format_map({k.lower(): v for k, v in subs.items()} | subs)

def resolve_url(base_url, path):
    if path.startswith(("http://", "https://")):
        return path
    base = base_url.rstrip("/")
    if base.endswith("/v1") and path.startswith("/v1"):
        path = path[3:]
    return f"{base}{path}"

def cprint(text):
    print(text)

def verbose_line(r):
    if r["retryable"]:
        return f"  🔄 {r['id']} {r['status']} — queued for retry"
    if r["ok"]:
        return f"  ✅ {r['id']} ({r['latency']}s) -> \"{r['content']}\""
    return f"  ❌ {r['id']} FAILED -> {r['status']}"

def is_kept_model(model_id):
    low = model_id.lower()
    if BLOCKED_KEYWORDS and any(w in low for w in BLOCKED_KEYWORDS):
        return False
    mode = FREE_FILTER_MODE
    if mode is None:
        return True
    if mode == "prefix":
        return low.startswith(FREE_TOKEN.lower())
    if mode == "contains":
        return FREE_TOKEN.lower() in low
    if mode == "custom":
        return bool(filter_model(model_id))
    if mode == "auto":
        return True
    return True

def _is_auto_free(m):
    mid = (m.get("id") or m.get("name") or m.get("slug") or "").lower()
    if "free" in mid:
        return True
    if mid == "big-pickle":
        return True
    pricing = m.get("pricing") or {}
    if isinstance(pricing, dict):
        for k in ("prompt", "input", "completion", "output", "prompt_price", "completion_price"):
            v = pricing.get(k)
            if v == 0 or v == "0" or v == "" or v == 0.0:
                return True
    tags = m.get("tags") or []
    if any("free" in str(t).lower() for t in tags):
        return True
    providers = m.get("providers") or []
    for p in providers:
        if isinstance(p, dict) and p.get("input_price") == 0 and p.get("output_price") == 0:
            return True
    return False

def _fetch_raw_models(url, key):
    headers = {"Authorization": f"Bearer {key}"} if key else {}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            lst = data if isinstance(data, list) else data.get("data") or data.get("models") or data.get("text") or []
            return [m for m in lst if isinstance(m, dict)]
    except Exception:
        pass
    return []

def fetch_models(base_url, key):
    headers = {"Authorization": f"Bearer {key}"} if key else {}
    try:
        res = requests.get(resolve_url(base_url, MODEL_FETCH_PATH), headers=headers, timeout=10)
        if res.status_code == 200:
            data = res.json()
            models_list = data if isinstance(data, list) else data.get("data", [])
            return [m["id"] for m in models_list if isinstance(m, dict) and m.get("id")]
    except Exception:
        pass
    return []

def test_model(chat_url, key, model_id):
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
        "max_tokens": MAX_TOKENS,
    }
    start = time.time()
    try:
        res = requests.post(chat_url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
        latency = round(time.time() - start, 2)
        try:
            data = res.json()
        except Exception:
            data = {}
        choices = data.get("choices", []) if isinstance(data, dict) else []
        if choices:
            content = (choices[0].get("message", {}).get("content") or "").strip().replace("\n", " ")
            return {"id": model_id, "ok": True, "latency": latency, "content": content, "retryable": False, "status": ""}
        if res.status_code == 200:
            if isinstance(data, dict) and (data.get("error") or data.get("status") == "error"):
                err = data.get("error", {}).get("message", str(data.get("error")))[:80] if isinstance(data.get("error"), dict) else str(data.get("error"))[:80]
                return {"id": model_id, "ok": False, "latency": latency, "content": "", "retryable": False, "status": f"API error: {err}"}
            return {"id": model_id, "ok": True, "latency": latency, "content": "[Empty Choice Structure]", "retryable": False, "status": ""}
        elif res.status_code in (429, 502, 503, 504):
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "retryable": True, "status": f"STATUS {res.status_code}"}
        else:
            err = ""
            if isinstance(data, dict) and isinstance(data.get("error"), dict):
                err = data.get("error", {}).get("message", "")
            snippet = (err or res.text[:80]).strip().replace("\n", " ")
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "retryable": False, "status": f"Status {res.status_code} ({snippet[:60]})"}
    except Exception as e:
        return {"id": model_id, "ok": False, "latency": round(time.time() - start, 2), "content": "", "retryable": True, "status": f"EXCEPTION {str(e)[:60]}"}

def run_gemini_provider(base_url, key):
    cprint(f"\n{'='*80}")
    cprint(f"🔬 Testing {PROVIDER_NAME} (GEMINI) models")
    cprint(f"{'='*80}")

    if not key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV}) set.")
        return {"passed": [], "failed": 0, "total": 0}

    base = base_url.rstrip("/")
    base_delay = 60.0 / GEMINI_RPM

    try:
        if MODEL_LIST:
            model_names = list(MODEL_LIST)
            cprint(f"📋 Using explicit MODEL_LIST ({len(model_names)} models) for {PROVIDER_NAME} (GEMINI).")
        else:
            res = requests.get(f"{base}/models?key={key}", timeout=10)
            if res.status_code != 200:
                cprint(f"⚠️  {PROVIDER_NAME} (GEMINI) model listing failed: Status {res.status_code} ({res.text[:80].strip()})")
                return {"passed": [], "failed": 0, "total": 0}
            g_models = res.json().get("models", [])
            model_names = [
                gm.get("name") for gm in g_models
                if "generateContent" in gm.get("supportedGenerationMethods", [])
            ]
            cprint(f"🔗 Queued {len(model_names)} chat models from {PROVIDER_NAME} (GEMINI) ({len(g_models)} total).")

        kept = [m for m in model_names if is_kept_model(m)]
        if len(kept) != len(model_names):
            cprint(f"🔎 Filtered to {len(kept)} models after FREE_FILTER/BLOCKED filter.")

        def test_gemini(m_name):
            url = f"{base}/{m_name}:generateContent?key={key}"
            payload = {"contents": [{"parts": [{"text": TEST_PROMPT}]}]}
            start = time.time()
            try:
                r = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=REQUEST_TIMEOUT)
                lat = round(time.time() - start, 2)
                if r.status_code == 200:
                    try:
                        reply = (r.json()["candidates"][0]["content"]["parts"][0].get("text") or "").strip().replace("\n", " ")
                    except Exception:
                        reply = ""
                    return {"id": m_name, "ok": True, "latency": lat, "content": reply, "retryable": False, "status": ""}
                elif r.status_code in (429, 502, 503, 504):
                    return {"id": m_name, "ok": False, "latency": lat, "content": "", "retryable": True, "status": f"STATUS {r.status_code}"}
                else:
                    return {"id": m_name, "ok": False, "latency": lat, "content": "", "retryable": False, "status": f"Status {r.status_code} ({r.text[:60].strip()})"}
            except Exception as e:
                return {"id": m_name, "ok": False, "latency": round(time.time() - start, 2), "content": "", "retryable": True, "status": f"EXCEPTION {str(e)[:60]}"}

        passed = {}
        failed = {}
        retry_queue = kept[:]

        for retry_pass in range(MAX_RETRY_PASSES + 1):
            if not retry_queue:
                break
            delay = base_delay * (RETRY_DELAY_MULTIPLIER ** retry_pass)
            if retry_pass > 0:
                cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
            next_retry = []
            if SEQUENTIAL:
                for m_name in retry_queue:
                    r = test_gemini(m_name)
                    if r["retryable"]:
                        next_retry.append(r["id"])
                        failed.pop(r["id"], None)
                    elif r["ok"]:
                        passed[r["id"]] = r
                        failed.pop(r["id"], None)
                    else:
                        failed[r["id"]] = r
                        passed.pop(r["id"], None)
                    cprint(verbose_line(r))
                    time.sleep(delay)
            else:
                futures = []
                with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                    for m_name in retry_queue:
                        futures.append(executor.submit(test_gemini, m_name))
                        time.sleep(delay)
                    for future in as_completed(futures):
                        r = future.result()
                        if r["retryable"]:
                            next_retry.append(r["id"])
                            failed.pop(r["id"], None)
                        elif r["ok"]:
                            passed[r["id"]] = r
                            failed.pop(r["id"], None)
                        else:
                            failed[r["id"]] = r
                            passed.pop(r["id"], None)
                        cprint(verbose_line(r))
            retry_queue = next_retry

        if retry_queue:
            cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after {MAX_RETRY_PASSES} retry passes.")
        cprint(f"🏁 {PROVIDER_NAME} (GEMINI): {len(passed)} passed, {len(failed)} failed")
        return {"passed": list(passed.values()), "failed": len(failed), "total": len(kept)}
    except Exception as e:
        cprint(f"⚠️  {PROVIDER_NAME} (GEMINI) encountered an error: {str(e)[:80]}")
        return {"passed": [], "failed": 0, "total": 0}

def _fetch_openai_models(url, key):
    headers = {"Authorization": f"Bearer {key}"} if key else {}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            lst = data if isinstance(data, list) else data.get("data") or data.get("models") or data.get("text") or []
            ids = []
            for m in lst:
                if isinstance(m, dict):
                    mid = m.get("id") or m.get("name") or m.get("slug") or m.get("model")
                    if mid:
                        ids.append(mid)
            if not ids and isinstance(data, dict) and (data.get("id") or data.get("name")):
                mid = data.get("id") or data.get("name")
                if mid:
                    ids.append(mid)
            return ids
    except Exception:
        pass
    return []

def _test_openai_chat(chat_url, key, model_id):
    return test_model(chat_url, key, model_id)

def run_cohere_provider(base_url, key):
    cprint(f"\n{'='*80}")
    cprint(f"🔬 Testing {PROVIDER_NAME} (COHERE) models")
    cprint(f"{'='*80}")
    eff_key = key or os.getenv("COHERE_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or COHERE_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    base_delay = 60.0 / 10
    model_ids = _fetch_openai_models("https://api.cohere.com/v1/models", eff_key)
    filtered = [m for m in model_ids if not any(w in m.lower() for w in ("embed", "rerank", "transcribe"))]
    filtered = [m for m in filtered if is_kept_model(m)]
    if MODEL_LIST:
        filtered = [m for m in MODEL_LIST if is_kept_model(m)]
        cprint(f"📋 Using explicit MODEL_LIST ({len(filtered)} models) for {PROVIDER_NAME} (COHERE).")
    else:
        cprint(f"🔗 Queued {len(filtered)} models from {PROVIDER_NAME} (COHERE).")

    def test_cohere(mid):
        headers = {"Authorization": f"Bearer {eff_key}", "Content-Type": "application/json"}
        payload = {"model": mid, "messages": [{"role": "user", "content": TEST_PROMPT}], "max_tokens": 16, "temperature": 0.0}
        start = time.time()
        try:
            res = requests.post("https://api.cohere.com/v2/chat", headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
            lat = round(time.time() - start, 2)
            if res.status_code == 200:
                body = res.json()
                msg = body.get("message", {})
                blocks = msg.get("content", [])
                if blocks:
                    reply = blocks[0].get("text", "").strip().replace("\n", " ")
                else:
                    reply = (body.get("text") or "").strip().replace("\n", " ")
                return {"id": mid, "ok": True, "latency": lat, "content": reply, "retryable": False, "status": ""}
            elif res.status_code in (429, 502, 503, 504):
                return {"id": mid, "ok": False, "latency": lat, "content": "", "retryable": True, "status": f"STATUS {res.status_code}"}
            else:
                return {"id": mid, "ok": False, "latency": lat, "content": "", "retryable": False, "status": f"Status {res.status_code} ({res.text[:60].strip()})"}
        except Exception as e:
            return {"id": mid, "ok": False, "latency": round(time.time() - start, 2), "content": "", "retryable": True, "status": f"EXCEPTION {str(e)[:60]}"}

    passed, failed, retry_queue = {}, {}, filtered[:]
    for retry_pass in range(MAX_RETRY_PASSES + 1):
        if not retry_queue:
            break
        delay = base_delay * (RETRY_DELAY_MULTIPLIER ** retry_pass)
        if retry_pass > 0:
            cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
        nxt = []
        if SEQUENTIAL:
            for mid in retry_queue:
                r = test_cohere(mid)
                if r["retryable"]:
                    nxt.append(r["id"]); failed.pop(r["id"], None)
                elif r["ok"]:
                    passed[r["id"]] = r; failed.pop(r["id"], None)
                else:
                    failed[r["id"]] = r; passed.pop(r["id"], None)
                cprint(verbose_line(r)); time.sleep(delay)
        else:
            futs = []
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
                for mid in retry_queue:
                    futs.append(ex.submit(test_cohere, mid)); time.sleep(delay)
                for f in as_completed(futs):
                    r = f.result()
                    if r["retryable"]:
                        nxt.append(r["id"]); failed.pop(r["id"], None)
                    elif r["ok"]:
                        passed[r["id"]] = r; failed.pop(r["id"], None)
                    else:
                        failed[r["id"]] = r; passed.pop(r["id"], None)
                    cprint(verbose_line(r))
        retry_queue = nxt
    if retry_queue:
        cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after {MAX_RETRY_PASSES} retry passes.")
    cprint(f"🏁 {PROVIDER_NAME} (COHERE): {len(passed)} passed, {len(failed)} failed")
    return {"passed": list(passed.values()), "failed": len(failed), "total": len(filtered)}

def run_workers_provider(base_url, key):
    cprint(f"\n{'='*80}")
    cprint(f"🔬 Testing {PROVIDER_NAME} (CLOUDFLARE WORKERS AI) models")
    cprint(f"{'='*80}")
    eff_key = key or os.getenv("WORKERS_API_KEY") or os.getenv("CLOUDFLARE_API_KEY")
    account_id = os.getenv("ACCOUNT_ID")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or WORKERS_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    if not account_id:
        import re
        m = re.search(r"/accounts/([^/]+)/", base_url or "")
        if m:
            account_id = m.group(1)
    if not account_id:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No ACCOUNT_ID in env or BASE_URL.")
        return {"passed": [], "failed": 0, "total": 0}
    base_v1 = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1"
    chat_url = f"{base_v1}/chat/completions"
    models_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/models/search"
    base_delay = 60.0 / 30
    try:
        res = requests.get(models_url, headers={"Authorization": f"Bearer {eff_key}"}, timeout=10)
        if res.status_code == 200:
            data = res.json()
            raw = data.get("result", [])
            model_ids = [m.get("name") or m.get("id") for m in raw if isinstance(m, dict)]
            task_filtered = [m.get("name") for m in raw if isinstance(m, dict) and m.get("name") and m.get("task", {}).get("name") == "Text Generation"]
            if task_filtered:
                model_ids = task_filtered
        else:
            cprint(f"⚠️  CLOUDFLARE model listing failed: Status {res.status_code}, falling back to known models.")
            model_ids = ["@cf/meta/llama-3.1-8b-instruct","@cf/meta/llama-3.1-70b-instruct","@cf/meta/llama-3.2-3b-instruct","@cf/meta/llama-3.2-11b-vision-instruct","@cf/mistral/mistral-7b-instruct-v0.1","@hf/thebloke/deepseek-coder-6.7b-instruct-awq"]
    except Exception:
        cprint("⚠️  CLOUDFLARE model listing failed, falling back to known models.")
        model_ids = ["@cf/meta/llama-3.1-8b-instruct","@cf/meta/llama-3.1-70b-instruct","@cf/meta/llama-3.2-3b-instruct","@cf/meta/llama-3.2-11b-vision-instruct","@cf/mistral/mistral-7b-instruct-v0.1"]
    if MODEL_LIST:
        model_ids = list(MODEL_LIST)
        cprint(f"📋 Using explicit MODEL_LIST ({len(model_ids)} models) for {PROVIDER_NAME} (WORKERS).")
    filtered = [m for m in model_ids if m and not any(w in m.lower() for w in ("embed", "rerank")) and is_kept_model(m)]
    cprint(f"🔗 Queued {len(filtered)} models from {PROVIDER_NAME} (CLOUDFLARE WORKERS AI).")

    def test_worker(mid):
        headers = {"Authorization": f"Bearer {eff_key}", "Content-Type": "application/json"}
        payload = {"model": mid, "messages": [{"role": "user", "content": TEST_PROMPT}], "max_tokens": 16, "temperature": 0.0}
        start = time.time()
        try:
            res = requests.post(chat_url, headers=headers, json=payload, timeout=10)
            lat = round(time.time() - start, 2)
            if res.status_code == 200:
                body = res.json()
                result = body.get("result", {})
                choices = result.get("choices", body.get("choices", []))
                if choices:
                    msg = choices[0].get("message", {})
                    reply = (msg.get("content") or "").strip().replace("\n", " ")
                    return {"id": mid, "ok": True, "latency": lat, "content": reply, "retryable": False, "status": ""}
                response_val = result.get("response", "")
                if response_val:
                    reply = str(response_val).strip().replace("\n", " ")
                    return {"id": mid, "ok": True, "latency": lat, "content": reply, "retryable": False, "status": ""}
                return {"id": mid, "ok": True, "latency": lat, "content": "[Empty Choice Structure]", "retryable": False, "status": ""}
            elif res.status_code in (429, 502, 503, 504):
                return {"id": mid, "ok": False, "latency": lat, "content": "", "retryable": True, "status": f"STATUS {res.status_code}"}
            else:
                return {"id": mid, "ok": False, "latency": lat, "content": "", "retryable": False, "status": f"Status {res.status_code} ({res.text[:60].strip()})"}
        except Exception as e:
            return {"id": mid, "ok": False, "latency": round(time.time() - start, 2), "content": "", "retryable": True, "status": f"EXCEPTION {str(e)[:60]}"}

    passed, failed, retry_queue = {}, {}, filtered[:]
    for retry_pass in range(MAX_RETRY_PASSES + 1):
        if not retry_queue:
            break
        delay = base_delay * (RETRY_DELAY_MULTIPLIER ** retry_pass)
        if retry_pass > 0:
            cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
        nxt = []
        if SEQUENTIAL:
            for mid in retry_queue:
                r = test_worker(mid)
                if r["retryable"]:
                    nxt.append(r["id"]); failed.pop(r["id"], None)
                elif r["ok"]:
                    passed[r["id"]] = r; failed.pop(r["id"], None)
                else:
                    failed[r["id"]] = r; passed.pop(r["id"], None)
                cprint(verbose_line(r)); time.sleep(delay)
        else:
            futs = []
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
                for mid in retry_queue:
                    futs.append(ex.submit(test_worker, mid)); time.sleep(delay)
                for f in as_completed(futs):
                    r = f.result()
                    if r["retryable"]:
                        nxt.append(r["id"]); failed.pop(r["id"], None)
                    elif r["ok"]:
                        passed[r["id"]] = r; failed.pop(r["id"], None)
                    else:
                        failed[r["id"]] = r; passed.pop(r["id"], None)
                    cprint(verbose_line(r))
        retry_queue = nxt
    if retry_queue:
        cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after {MAX_RETRY_PASSES} retry passes.")
    cprint(f"🏁 {PROVIDER_NAME} (WORKERS): {len(passed)} passed, {len(failed)} failed")
    return {"passed": list(passed.values()), "failed": len(failed), "total": len(filtered)}

def run_ollama_provider(base_url, key):
    cprint(f"\n{'='*80}")
    cprint(f"🔬 Testing {PROVIDER_NAME} (OLLAMA CLOUD) models")
    cprint(f"{'='*80}")
    eff_key = key or os.getenv("OLLAMA_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or OLLAMA_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    base_delay = 60.0 / 30
    try:
        res = requests.get("https://api.ollama.com/v1/models", headers={"Authorization": f"Bearer {eff_key}"}, timeout=10)
        if res.status_code == 200:
            data = res.json()
            model_ids = [m.get("id") for m in data.get("data", []) if m.get("id")]
        else:
            cprint(f"⚠️  OLLAMA model listing failed: Status {res.status_code}")
            return {"passed": [], "failed": 0, "total": 0}
    except Exception as e:
        cprint(f"⚠️  OLLAMA model listing failed: {str(e)[:60]}")
        return {"passed": [], "failed": 0, "total": 0}
    if MODEL_LIST:
        model_ids = list(MODEL_LIST)
        cprint(f"📋 Using explicit MODEL_LIST ({len(model_ids)} models) for {PROVIDER_NAME} (OLLAMA).")
    filtered = [m for m in model_ids if not any(w in m.lower() for w in ("embed", "rerank", "similarity")) and is_kept_model(m)]
    cprint(f"🔗 Queued {len(filtered)} models from {PROVIDER_NAME} (OLLAMA CLOUD).")

    def test_ollama(mid):
        headers = {"Authorization": f"Bearer {eff_key}", "Content-Type": "application/json"}
        payload = {"model": mid, "messages": [{"role": "user", "content": TEST_PROMPT}], "stream": False}
        start = time.time()
        try:
            res = requests.post("https://api.ollama.com/api/chat", headers=headers, json=payload, timeout=10)
            lat = round(time.time() - start, 2)
            if res.status_code == 200:
                body = res.json()
                reply = (body.get("message", {}).get("content") or "").strip().replace("\n", " ")
                return {"id": mid, "ok": True, "latency": lat, "content": reply, "retryable": False, "status": ""}
            elif res.status_code in (429, 502, 503, 504):
                return {"id": mid, "ok": False, "latency": lat, "content": "", "retryable": True, "status": f"STATUS {res.status_code}"}
            else:
                return {"id": mid, "ok": False, "latency": lat, "content": "", "retryable": False, "status": f"Status {res.status_code} ({res.text[:60].strip()})"}
        except Exception as e:
            return {"id": mid, "ok": False, "latency": round(time.time() - start, 2), "content": "", "retryable": True, "status": f"EXCEPTION {str(e)[:60]}"}

    passed, failed, retry_queue = {}, {}, filtered[:]
    for retry_pass in range(MAX_RETRY_PASSES + 1):
        if not retry_queue:
            break
        delay = base_delay * (RETRY_DELAY_MULTIPLIER ** retry_pass)
        if retry_pass > 0:
            cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
        nxt = []
        if SEQUENTIAL:
            for mid in retry_queue:
                r = test_ollama(mid)
                if r["retryable"]:
                    nxt.append(r["id"]); failed.pop(r["id"], None)
                elif r["ok"]:
                    passed[r["id"]] = r; failed.pop(r["id"], None)
                else:
                    failed[r["id"]] = r; passed.pop(r["id"], None)
                cprint(verbose_line(r)); time.sleep(delay)
        else:
            futs = []
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
                for mid in retry_queue:
                    futs.append(ex.submit(test_ollama, mid)); time.sleep(delay)
                for f in as_completed(futs):
                    r = f.result()
                    if r["retryable"]:
                        nxt.append(r["id"]); failed.pop(r["id"], None)
                    elif r["ok"]:
                        passed[r["id"]] = r; failed.pop(r["id"], None)
                    else:
                        failed[r["id"]] = r; passed.pop(r["id"], None)
                    cprint(verbose_line(r))
        retry_queue = nxt
    if retry_queue:
        cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after {MAX_RETRY_PASSES} retry passes.")
    cprint(f"🏁 {PROVIDER_NAME} (OLLAMA): {len(passed)} passed, {len(failed)} failed")
    return {"passed": list(passed.values()), "failed": len(failed), "total": len(filtered)}

def run_huggingface_provider(base_url, key):
    cprint(f"\n{'='*80}")
    cprint(f"🔬 Testing {PROVIDER_NAME} (HUGGING FACE) models")
    cprint(f"{'='*80}")
    eff_key = key or os.getenv("HF_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or HF_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    base_delay = 60.0 / 30
    model_ids = _fetch_openai_models("https://router.huggingface.co/v1/models", eff_key)
    filtered = [m for m in model_ids if not any(w in m.lower() for w in ("embed", "rerank", "similarity")) and is_kept_model(m)]
    if MODEL_LIST:
        filtered = list(MODEL_LIST)
        cprint(f"📋 Using explicit MODEL_LIST ({len(filtered)} models) for {PROVIDER_NAME} (HF).")
    else:
        cprint(f"🔗 Queued {len(filtered)} models from {PROVIDER_NAME} (HUGGING FACE).")
    chat_url = "https://router.huggingface.co/v1/chat/completions"
    passed, failed, retry_queue = {}, {}, filtered[:]
    for retry_pass in range(5 + 1):
        if not retry_queue:
            break
        delay = base_delay * (1.5 ** retry_pass)
        if retry_pass > 0:
            cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
        nxt = []
        for mid in retry_queue:
            r = _test_openai_chat("HUGGING FACE", chat_url, eff_key, mid)
            if r["retryable"]:
                nxt.append(r["id"]); failed.pop(r["id"], None)
            elif r["ok"]:
                passed[r["id"]] = r; failed.pop(r["id"], None)
            else:
                failed[r["id"]] = r; passed.pop(r["id"], None)
            cprint(verbose_line(r)); time.sleep(delay)
        retry_queue = nxt
    if retry_queue:
        cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after 5 retry passes.")
    cprint(f"🏁 {PROVIDER_NAME} (HUGGING FACE): {len(passed)} passed, {len(failed)} failed")
    return {"passed": list(passed.values()), "failed": len(failed), "total": len(filtered)}

def _test_openai_chat(tag, chat_url, key, model_id):
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {"model": model_id, "messages": [{"role": "user", "content": TEST_PROMPT}], "max_tokens": MAX_TOKENS}
    start = time.time()
    try:
        res = requests.post(chat_url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
        lat = round(time.time() - start, 2)
        try:
            data = res.json()
        except Exception:
            data = {}
        choices = data.get("choices", []) if isinstance(data, dict) else []
        if choices:
            msg = choices[0].get("message", {}) or {}
            reply = (msg.get("content") or "").strip().replace("\n", " ")
            return {"id": model_id, "ok": True, "latency": lat, "content": reply, "retryable": False, "status": ""}
        if res.status_code == 200:
            if data.get("error") or data.get("status") == "error":
                err = data.get("error", {}).get("message", str(data.get("error")))[:80] if isinstance(data.get("error"), dict) else str(data.get("error"))[:80]
                return {"id": model_id, "ok": False, "latency": lat, "content": "", "retryable": False, "status": f"API error: {err}"}
            return {"id": model_id, "ok": True, "latency": lat, "content": "[Empty Choice Structure]", "retryable": False, "status": ""}
        elif res.status_code in (429, 502, 503, 504):
            return {"id": model_id, "ok": False, "latency": lat, "content": "", "retryable": True, "status": f"STATUS {res.status_code}"}
        else:
            err = data.get("error", {}).get("message", "") if isinstance(data, dict) and isinstance(data.get("error"), dict) else ""
            snippet = (err or res.text[:80]).strip().replace("\n", " ")
            return {"id": model_id, "ok": False, "latency": lat, "content": "", "retryable": False, "status": f"Status {res.status_code} ({snippet[:60]})"}
    except Exception as e:
        return {"id": model_id, "ok": False, "latency": round(time.time() - start, 2), "content": "", "retryable": True, "status": f"EXCEPTION {str(e)[:60]}"}

def run_openrouter_provider(base_url, key):
    cprint(f"\n{'='*80}")
    cprint(f"🔬 Testing {PROVIDER_NAME} (OPENROUTER) models")
    cprint(f"{'='*80}")
    eff_key = key or os.getenv("OPENROUTER_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or OPENROUTER_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    base_delay = 60.0 / 20
    model_ids = _fetch_openai_models("https://openrouter.ai/api/v1/models", eff_key)
    filtered = [m for m in model_ids if ":free" in m.lower() and is_kept_model(m)]
    if MODEL_LIST:
        filtered = [m for m in MODEL_LIST if ":free" in m.lower() and is_kept_model(m)]
        cprint(f"📋 Using explicit MODEL_LIST ({len(filtered)} models) for {PROVIDER_NAME} (OPENROUTER).")
    else:
        cprint(f"🔗 Queued {len(filtered)} free models from {PROVIDER_NAME} (OPENROUTER) ({len(model_ids)} total).")
    chat_url = "https://openrouter.ai/api/v1/chat/completions"
    passed, failed, retry_queue = {}, {}, filtered[:]
    for retry_pass in range(5 + 1):
        if not retry_queue:
            break
        delay = base_delay * (1.5 ** retry_pass)
        if retry_pass > 0:
            cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
        nxt = []
        for mid in retry_queue:
            r = _test_openai_chat("OPENROUTER", chat_url, eff_key, mid)
            if r["retryable"]:
                nxt.append(r["id"]); failed.pop(r["id"], None)
            elif r["ok"]:
                passed[r["id"]] = r; failed.pop(r["id"], None)
            else:
                failed[r["id"]] = r; passed.pop(r["id"], None)
            cprint(verbose_line(r)); time.sleep(delay)
        retry_queue = nxt
    if retry_queue:
        cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after 5 retry passes.")
    cprint(f"🏁 {PROVIDER_NAME} (OPENROUTER): {len(passed)} passed, {len(failed)} failed")
    return {"passed": list(passed.values()), "failed": len(failed), "total": len(filtered)}

def test_routeway_model(key, model_id, chat_url):
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {"model": model_id, "messages": [{"role": "user", "content": TEST_PROMPT}], "max_tokens": 8}
    start = time.time()
    try:
        res = requests.post(chat_url, headers=headers, json=payload, timeout=10)
        latency = round(time.time() - start, 2)
        if res.status_code == 200:
            data = res.json()
            choices = data.get("choices", [])
            if choices:
                msg = choices[0].get("message") or choices[0].get("messages") or {}
                if isinstance(msg, list):
                    msg = msg[0] if msg else {}
                content = (msg.get("content") or "").strip().replace("\n", " ")
                return {"id": model_id, "ok": True, "latency": latency, "content": content, "retryable": False, "status": ""}
            return {"id": model_id, "ok": True, "latency": latency, "content": "[Empty Choice Structure]", "retryable": False, "status": ""}
        elif res.status_code in (429, 502, 503, 504):
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "retryable": True, "status": f"STATUS {res.status_code}"}
        else:
            return {"id": model_id, "ok": False, "latency": latency, "content": "", "retryable": False, "status": f"Status {res.status_code} ({res.text[:60].strip()})"}
    except Exception as e:
        return {"id": model_id, "ok": False, "latency": round(time.time() - start, 2), "content": "", "retryable": True, "status": f"EXCEPTION {str(e)[:60]}"}

def run_routeway_provider(base_url, key):
    cprint(f"\n{'='*80}")
    cprint(f"🔬 Testing {PROVIDER_NAME} (ROUTEWAY) models")
    cprint(f"{'='*80}")
    eff_key = key or os.getenv("ROUTEWAY_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or ROUTEWAY_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    chat_url = resolve_url(base_url, CHAT_PATH) if base_url else "https://api.routeway.ai/v1/chat/completions"
    reg_url = resolve_url(base_url, MODEL_FETCH_PATH) if base_url and "routeway" in base_url.lower() else "https://api.routeway.ai/v1/models"
    model_ids = _fetch_openai_models(reg_url, eff_key)
    if MODEL_LIST:
        model_ids = list(MODEL_LIST)
        cprint(f"📋 Using explicit MODEL_LIST ({len(model_ids)} models) for {PROVIDER_NAME} (ROUTEWAY).")
    filtered = [m for m in model_ids if ":free" in m.lower() and not any(w in m.lower() for w in ("embed", "rerank", "similarity")) and is_kept_model(m)]
    cprint(f"🔗 Queued {len(filtered)} free models from {PROVIDER_NAME} (ROUTEWAY) ({len(model_ids)} total).")
    base_delay = 60.0 / 30
    passed, failed, retry_queue = {}, {}, filtered[:]
    for retry_pass in range(MAX_RETRY_PASSES + 1):
        if not retry_queue:
            break
        delay = base_delay * (RETRY_DELAY_MULTIPLIER ** retry_pass)
        if retry_pass > 0:
            cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
        nxt = []
        for mid in retry_queue:
            r = test_routeway_model(eff_key, mid, chat_url)
            if r["retryable"]:
                nxt.append(r["id"]); failed.pop(r["id"], None)
            elif r["ok"]:
                passed[r["id"]] = r; failed.pop(r["id"], None)
            else:
                failed[r["id"]] = r; passed.pop(r["id"], None)
            cprint(verbose_line(r)); time.sleep(delay)
        retry_queue = nxt
    if retry_queue:
        cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after {MAX_RETRY_PASSES} retry passes.")
    cprint(f"🏁 {PROVIDER_NAME} (ROUTEWAY): {len(passed)} passed, {len(failed)} failed")
    return {"passed": list(passed.values()), "failed": len(failed), "total": len(filtered)}

def run_tokenreply_provider(base_url, key):
    cprint(f"\n{'='*80}")
    cprint(f"🔬 Testing {PROVIDER_NAME} (TOKENREPLY) models")
    cprint(f"{'='*80}")
    eff_key = key or os.getenv("TOKENREP_API_KEY") or os.getenv("TOKENREPLY_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or TOKENREP_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    base_delay = 60.0 / 5
    chat_url = "https://api.tokenreply.com/v1/chat/completions"
    if base_url and "tokenreply" in base_url.lower():
        chat_url = resolve_url(base_url, CHAT_PATH)
    known = set(FREE_MODELS)
    if MODEL_LIST:
        model_ids = list(MODEL_LIST)
        cprint(f"📋 Using explicit MODEL_LIST ({len(model_ids)} models) for {PROVIDER_NAME} (TOKENREPLY).")
    else:
        api_ids = _fetch_openai_models("https://api.tokenreply.com/v1/models", eff_key)
        model_ids = list(known)
        for mid in api_ids:
            base = mid.replace(":free", "").replace("-free", "")
            for known_mid in known:
                if base == known_mid or base in known_mid or known_mid in base:
                    if mid not in model_ids:
                        model_ids.append(mid)
                        break
        cprint(f"🔗 Queued {len(model_ids)} models from {PROVIDER_NAME} (TOKENREPLY) ({len(api_ids)} api total, {len(known)} known).")
    filtered = [m for m in model_ids if is_kept_model(m)]
    passed, failed, retry_queue = {}, {}, filtered[:]
    for retry_pass in range(MAX_RETRY_PASSES + 1):
        if not retry_queue:
            break
        delay = base_delay * (RETRY_DELAY_MULTIPLIER ** retry_pass)
        if retry_pass > 0:
            cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
        nxt = []
        for mid in retry_queue:
            r = _test_openai_chat("TOKENREPLY", chat_url, eff_key, mid)
            if r["retryable"]:
                nxt.append(r["id"]); failed.pop(r["id"], None)
            elif r["ok"]:
                passed[r["id"]] = r; failed.pop(r["id"], None)
            else:
                failed[r["id"]] = r; passed.pop(r["id"], None)
            cprint(verbose_line(r)); time.sleep(delay)
        retry_queue = nxt
    if retry_queue:
        cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after {MAX_RETRY_PASSES} retry passes.")
    cprint(f"🏁 {PROVIDER_NAME} (TOKENREPLY): {len(passed)} passed, {len(failed)} failed")
    return {"passed": list(passed.values()), "failed": len(failed), "total": len(filtered)}

def _run_test_loop(tag, chat_url, key, model_ids, base_delay):
    if MODEL_LIST:
        model_ids = [m for m in MODEL_LIST if is_kept_model(m)]
        cprint(f"📋 Using explicit MODEL_LIST ({len(model_ids)} models) for {PROVIDER_NAME} ({tag}).")
    filtered = [m for m in model_ids if is_kept_model(m)]
    cprint(f"🔗 Queued {len(filtered)} models from {PROVIDER_NAME} ({tag}).")
    passed, failed, retry_queue = {}, {}, filtered[:]
    for retry_pass in range(MAX_RETRY_PASSES + 1):
        if not retry_queue:
            break
        delay = base_delay * (RETRY_DELAY_MULTIPLIER ** retry_pass)
        if retry_pass > 0:
            cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")
        nxt = []
        if SEQUENTIAL:
            for mid in retry_queue:
                r = _test_openai_chat(tag, chat_url, key, mid)
                if r["retryable"]:
                    nxt.append(r["id"]); failed.pop(r["id"], None)
                elif r["ok"]:
                    passed[r["id"]] = r; failed.pop(r["id"], None)
                else:
                    failed[r["id"]] = r; passed.pop(r["id"], None)
                cprint(verbose_line(r)); time.sleep(delay)
        else:
            futs = []
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
                for mid in retry_queue:
                    futs.append(ex.submit(_test_openai_chat, tag, chat_url, key, mid)); time.sleep(delay)
                for f in as_completed(futs):
                    r = f.result()
                    if r["retryable"]:
                        nxt.append(r["id"]); failed.pop(r["id"], None)
                    elif r["ok"]:
                        passed[r["id"]] = r; failed.pop(r["id"], None)
                    else:
                        failed[r["id"]] = r; passed.pop(r["id"], None)
                    cprint(verbose_line(r))
        retry_queue = nxt
    if retry_queue:
        cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after {MAX_RETRY_PASSES} retry passes.")
    cprint(f"🏁 {PROVIDER_NAME} ({tag}): {len(passed)} passed, {len(failed)} failed")
    return {"passed": list(passed.values()), "failed": len(failed), "total": len(filtered)}

def run_fastrouter_provider(base_url, key):
    eff_key = key or os.getenv("FASTR_API_KEY") or os.getenv("FASTROUTER_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or FASTR_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    chat_url = resolve_url(base_url, CHAT_PATH) if base_url and "fastrouter" in base_url.lower() else "https://api.fastrouter.ai/api/v1/chat/completions"
    reg_url = resolve_url(base_url, MODEL_FETCH_PATH) if base_url and "fastrouter" in base_url.lower() else "https://api.fastrouter.ai/api/v1/models"
    headers = {"Authorization": f"Bearer {eff_key}"}
    model_ids = []
    try:
        res = requests.get(reg_url, headers=headers, timeout=10)
        if res.status_code == 200:
            data = res.json()
            models = data if isinstance(data, list) else data.get("data", [])
            text_models = []
            for m in models:
                if not isinstance(m, dict):
                    continue
                mid = m.get("id")
                if not mid or not m.get("is_active", True):
                    continue
                if any(w in mid.lower() for w in NON_CHAT_KW):
                    continue
                arch = m.get("architecture", {})
                mod = (arch.get("modality") or "").lower()
                if mod and "text" not in mod and "->" in mod:
                    continue
                if m.get("pricing", {}).get("prompt") == "":
                    continue
                text_models.append(mid)
            model_ids = [f"{m}:free" for m in text_models]
            if not is_kept_model(":free"):
                model_ids = text_models
        else:
            cprint(f"⚠️  FASTROUTER model listing failed: Status {res.status_code}")
    except Exception as e:
        cprint(f"⚠️  FASTROUTER model listing failed: {str(e)[:60]}")
    return _run_test_loop("FASTROUTER", chat_url, eff_key, model_ids, 60.0 / 30)

def run_poixe_provider(base_url, key):
    eff_key = key or os.getenv("POIXE_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or POIXE_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    chat_url = resolve_url(base_url, CHAT_PATH) if base_url and "poixe" in base_url.lower() else "https://api.poixe.com/v1/chat/completions"
    reg_url = resolve_url(base_url, MODEL_FETCH_PATH) if base_url and "poixe" in base_url.lower() else "https://api.poixe.com/v1/models"
    model_ids = []
    try:
        res = requests.get(reg_url, headers={"Authorization": f"Bearer {eff_key}"}, timeout=10)
        if res.status_code == 200:
            data = res.json()
            models = data if isinstance(data, list) else data.get("data", [])
            model_ids = [f"{m['id']}:free" for m in models if isinstance(m, dict) and m.get("id") and not any(w in m['id'].lower() for w in NON_CHAT_KW)]
        else:
            cprint(f"⚠️  POIXE model listing failed: Status {res.status_code}")
    except Exception as e:
        cprint(f"⚠️  POIXE model listing failed: {str(e)[:60]}")
    return _run_test_loop("POIXE", chat_url, eff_key, model_ids, 60.0 / 40)

def run_auriko_provider(base_url, key):
    eff_key = key or os.getenv("AURIKO_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or AURIKO_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    chat_url = resolve_url(base_url, CHAT_PATH) if base_url and "auriko" in base_url.lower() else "https://api.auriko.ai/v1/chat/completions"
    reg_url = resolve_url(base_url, MODEL_FETCH_PATH) if base_url and "auriko" in base_url.lower() else "https://api.auriko.ai/v1/models"
    blocked_prefixes = ("gemma-",)
    model_ids = []
    try:
        res = requests.get(reg_url, headers={"Authorization": f"Bearer {eff_key}"}, timeout=10)
        if res.status_code == 200:
            data = res.json()
            models = data if isinstance(data, list) else data.get("data", [])
            free_models = []
            for m in models:
                if not isinstance(m, dict) or not m.get("id"):
                    continue
                mid = m["id"]
                if any(mid.startswith(p) for p in blocked_prefixes):
                    continue
                if any(w in mid.lower() for w in NON_CHAT_KW):
                    continue
                providers = m.get("providers", [])
                for p in providers:
                    if p.get("input_price") == 0 and p.get("output_price") == 0:
                        free_models.append(mid)
                        break
            model_ids = free_models
        else:
            cprint(f"⚠️  AURIKO model listing failed: Status {res.status_code}")
    except Exception as e:
        cprint(f"⚠️  AURIKO model listing failed: {str(e)[:60]}")
    return _run_test_loop("AURIKO", chat_url, eff_key, model_ids, 60.0 / 30)

def run_meganova_provider(base_url, key):
    eff_key = key or os.getenv("MEGANOVA_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or MEGANOVA_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    chat_url = resolve_url(base_url, CHAT_PATH) if base_url and "meganova" in base_url.lower() else "https://api.meganova.ai/v1/chat/completions"
    reg_url = resolve_url(base_url, MODEL_FETCH_PATH) if base_url and "meganova" in base_url.lower() else "https://api.meganova.ai/v1/models"
    model_ids = []
    try:
        res = requests.get(reg_url, headers={"Authorization": f"Bearer {eff_key}"}, timeout=10)
        if res.status_code == 200:
            data = res.json()
            models = data if isinstance(data, list) else data.get("data", [])
            for m in models:
                if not isinstance(m, dict) or not m.get("id"):
                    continue
                if "free" not in m.get("tags", []):
                    continue
                if any(w in m["id"].lower() for w in NON_CHAT_KW):
                    continue
                model_ids.append(m["id"])
        else:
            cprint(f"⚠️  MEGANOVA model listing failed: Status {res.status_code}")
    except Exception as e:
        cprint(f"⚠️  MEGANOVA model listing failed: {str(e)[:60]}")
    return _run_test_loop("MEGANOVA", chat_url, eff_key, model_ids, 60.0 / 20)

def run_helyx_provider(base_url, key):
    eff_key = key or os.getenv("HELYX_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or HELYX_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    import re
    chat_url = "https://helyxai.space/v1/chat/completions"
    if base_url and "helyx" in base_url.lower():
        chat_url = resolve_url(base_url, CHAT_PATH)
    models_url = "https://helyxai.space/models-list"
    model_ids = []
    try:
        res = requests.get(models_url, timeout=10)
        raw = res.content.decode("utf-8", errors="replace")
        slugs = [s.strip("'\"") for s in re.findall(r'slug=([^\"&]+)', raw)]
        model_ids = list(dict.fromkeys(s for s in slugs if s))
    except Exception as e:
        cprint(f"⚠️  HELYX model scraping failed: {str(e)[:60]}")
    return _run_test_loop("HELYX", chat_url, eff_key, model_ids, 60.0 / 30)

def run_zylo_provider(base_url, key):
    eff_key = key or os.getenv("ZYLO_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or ZYLO_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    chat_url = resolve_url(base_url, CHAT_PATH) if base_url and "zylo" in base_url.lower() else "https://api.zyloai.net/v1/chat/completions"
    reg_url = resolve_url(base_url, MODEL_FETCH_PATH) if base_url and "zylo" in base_url.lower() else "https://api.zyloai.net/v1/models"
    model_ids = []
    try:
        res = requests.get(reg_url, headers={"Authorization": f"Bearer {eff_key}"}, timeout=10)
        if res.status_code == 200:
            data = res.json()
            models_list = data.get("text", [])
            basic = []
            for m in models_list:
                if not isinstance(m, dict) or not m.get("id"):
                    continue
                if m.get("min_plan") != "BASIC":
                    continue
                mid = m["id"]
                if any(w in mid.lower() for w in NON_CHAT_KW):
                    continue
                basic.append(mid)
            cprint(f"🔗 Queued {len(basic)} basic-plan models from {PROVIDER_NAME} (ZYLO AI).")
            model_ids = basic
        else:
            cprint(f"⚠️  ZYLO AI model listing failed: Status {res.status_code}")
    except Exception as e:
        cprint(f"⚠️  ZYLO AI model listing failed: {str(e)[:60]}")
    return _run_test_loop("ZYLO AI", chat_url, eff_key, model_ids, 60.0 / 10)

def run_zai_provider(base_url, key):
    eff_key = key or os.getenv("ZAI_API_KEY") or os.getenv("Z_AI_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or ZAI_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    chat_url = "https://api.z.ai/api/paas/v4/chat/completions"
    reg_url = resolve_url(base_url, MODEL_FETCH_PATH) if base_url and ("z.ai" in base_url.lower() or "zai" in base_url.lower()) else "https://api.z.ai/v1/models"
    raw_ids = _fetch_openai_models(reg_url, eff_key)
    model_ids = list(raw_ids)
    for m in ["glm-4.5-flash", "glm-4.7-flash"]:
        if m not in model_ids:
            model_ids.append(m)
    if MODEL_LIST:
        model_ids = [m for m in MODEL_LIST if is_kept_model(m)]
        cprint(f"📋 Using explicit MODEL_LIST ({len(model_ids)} models) for {PROVIDER_NAME} (Z.AI).")
    else:
        model_ids = [m for m in model_ids if is_kept_model(m)]
    return _run_test_loop("Z.AI", chat_url, eff_key, model_ids, 60.0 / 30)

def run_odirouter_provider(base_url, key):
    eff_key = key or os.getenv("ODIROUTER_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or ODIROUTER_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    if MODEL_LIST:
        model_ids = [m for m in MODEL_LIST if m.lower().startswith(ODIROUTER_FREE_PREFIX) and not any(w in m.lower() for w in ODIROUTER_BLOCKED) and is_kept_model(m)]
        cprint(f"📋 Using explicit MODEL_LIST ({len(model_ids)} models) for {PROVIDER_NAME} (ODIROUTER, free filter).")
    else:
        raw_ids = _fetch_openai_models(resolve_url(base_url, MODEL_FETCH_PATH), eff_key)
        if not raw_ids:
            raw_ids = _fetch_openai_models(f"{base_url.rstrip('/')}/models", eff_key)
        model_ids = [m for m in raw_ids if m.lower().startswith(ODIROUTER_FREE_PREFIX) and not any(w in m.lower() for w in ODIROUTER_BLOCKED) and is_kept_model(m)]
        cprint(f"🔗 Queued {len(model_ids)} free models from {PROVIDER_NAME} (ODIROUTER) ({len(raw_ids)} total).")
    chat_url = resolve_url(base_url, CHAT_PATH)
    return _run_test_loop("ODIROUTER", chat_url, eff_key, model_ids, 60.0 / 30)

def run_opencode_provider(base_url, key):
    eff_key = key or os.getenv("OPENCODE_API_KEY") or os.getenv("ZEN_API_KEY") or os.getenv("OPENCODE_ZEN_API_KEY")
    if not eff_key:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: No API key ({API_KEY_ENV} or OPENCODE_API_KEY).")
        return {"passed": [], "failed": 0, "total": 0}
    if MODEL_LIST:
        raw_ids = list(MODEL_LIST)
        cprint(f"📋 Using explicit MODEL_LIST ({len(raw_ids)} models) for {PROVIDER_NAME} (OPENCODE ZEN).")
    else:
        raw_ids = _fetch_openai_models(resolve_url(base_url, MODEL_FETCH_PATH), eff_key)
        if not raw_ids:
            raw_ids = _fetch_openai_models(f"{base_url.rstrip('/')}/models", eff_key)
        cprint(f"🔗 Fetched {len(raw_ids)} models from {PROVIDER_NAME} (OPENCODE ZEN).")
    if FREE_FILTER_MODE in (None, "auto"):
        free_ids = []
        for mid in raw_ids:
            low = mid.lower()
            if "free" in low or mid in OPENCODE_ZEN_EXTRA_FREE:
                if not any(w in low for w in ODIROUTER_BLOCKED) and is_kept_model(mid):
                    free_ids.append(mid)
        for extra in OPENCODE_ZEN_EXTRA_FREE:
            if extra in raw_ids and extra not in free_ids and is_kept_model(extra):
                free_ids.append(extra)
        model_ids = free_ids
    else:
        model_ids = [m for m in raw_ids if is_kept_model(m)]
    chat_url = resolve_url(base_url, CHAT_PATH)
    return _run_test_loop("OPENCODE ZEN", chat_url, eff_key, model_ids, 60.0 / 30)

def run():
    base_url = build_base_url()
    key = os.getenv(API_KEY_ENV)
    low = (base_url or "").lower()
    if "generativelanguage.googleapis.com" in low:
        return run_gemini_provider(base_url, key)
    if "cohere.com" in low:
        return run_cohere_provider(base_url, key)
    if "cloudflare.com" in low:
        return run_workers_provider(base_url, key)
    if "ollama.com" in low:
        return run_ollama_provider(base_url, key)
    if "huggingface.co" in low:
        return run_huggingface_provider(base_url, key)
    if "openrouter.ai" in low:
        return run_openrouter_provider(base_url, key)
    if "routeway" in low:
        return run_routeway_provider(base_url, key)
    if "tokenreply" in low:
        return run_tokenreply_provider(base_url, key)
    if "fastrouter" in low:
        return run_fastrouter_provider(base_url, key)
    if "poixe" in low:
        return run_poixe_provider(base_url, key)
    if "auriko" in low:
        return run_auriko_provider(base_url, key)
    if "meganova" in low:
        return run_meganova_provider(base_url, key)
    if "helyx" in low:
        return run_helyx_provider(base_url, key)
    if "zylo" in low:
        return run_zylo_provider(base_url, key)
    if "odirouter" in low:
        return run_odirouter_provider(base_url, key)
    if "opencode" in low or "zen" in low:
        return run_opencode_provider(base_url, key)
    if "z.ai" in low or "zai" in low:
        return run_zai_provider(base_url, key)

    cprint(f"\n{'='*80}")
    cprint(f"🔬 Testing {PROVIDER_NAME} models")
    cprint(f"{'='*80}")
    if not base_url:
        cprint(f"⚠️  Skipping {PROVIDER_NAME}: base URL not resolvable (set {BASE_URL_ENV} or BASE_URL_TEMPLATE + its placeholders).")
        return {"passed": [], "failed": 0, "total": 0}
    if not key:
        cprint(f"⚠️  No API key ({API_KEY_ENV}) — attempting keyless requests.")

    if MODEL_LIST:
        model_ids = list(MODEL_LIST)
        cprint(f"📋 Using explicit MODEL_LIST ({len(model_ids)} models) for {PROVIDER_NAME}.")
        kept = [m for m in model_ids if is_kept_model(m)]
        cprint(f"🔗 Queued {len(kept)} models from {PROVIDER_NAME} ({len(model_ids)} total listed).")
    else:
        if FREE_FILTER_MODE == "auto":
            raw = _fetch_raw_models(resolve_url(base_url, MODEL_FETCH_PATH), key)
            if not raw:
                model_ids = fetch_models(base_url, key)
                if not model_ids:
                    cprint(f"⚠️  {PROVIDER_NAME}: No models discovered (and MODEL_LIST is empty).")
                    return {"passed": [], "failed": 0, "total": 0}
                kept = [m for m in model_ids if is_kept_model(m)]
                cprint(f"🔗 Queued {len(kept)} models from {PROVIDER_NAME} ({len(model_ids)} total listed).")
            else:
                raw_filtered = [m for m in raw if not any(w in (m.get("id") or m.get("name") or m.get("slug") or "").lower() for w in BLOCKED_KEYWORDS)]
                free_candidates = [m for m in raw_filtered if _is_auto_free(m)]
                for m in raw_filtered:
                    mid = (m.get("id") or m.get("name") or "")
                    if mid in OPENCODE_ZEN_EXTRA_FREE and m not in free_candidates:
                        free_candidates.append(m)
                if 0 < len(free_candidates) < len(raw_filtered):
                    kept = [(m.get("id") or m.get("name") or m.get("slug")) for m in free_candidates]
                    cprint(f"🔗 Queued {len(kept)} free models from {PROVIDER_NAME} (AUTO) ({len(raw_filtered)} total).")
                else:
                    kept = [(m.get("id") or m.get("name") or m.get("slug")) for m in raw_filtered]
                    cprint(f"🔗 Queued {len(kept)} models from {PROVIDER_NAME} ({len(raw_filtered)} total, auto kept all).")
        else:
            model_ids = fetch_models(base_url, key)
            if not model_ids:
                cprint(f"⚠️  {PROVIDER_NAME}: No models discovered (and MODEL_LIST is empty).")
                return {"passed": [], "failed": 0, "total": 0}
            kept = [m for m in model_ids if is_kept_model(m)]
            cprint(f"🔗 Queued {len(kept)} models from {PROVIDER_NAME} ({len(model_ids)} total listed).")

    chat_url = resolve_url(base_url, CHAT_PATH)
    passed = {}
    failed = {}
    retry_queue = kept[:]

    for retry_pass in range(MAX_RETRY_PASSES + 1):
        if not retry_queue:
            break

        delay = SUBMIT_DELAY * (RETRY_DELAY_MULTIPLIER ** retry_pass)
        if retry_pass > 0:
            cprint(f"  🔄 Retry pass {retry_pass}: {len(retry_queue)} models (delay={delay:.1f}s)...")

        next_retry = []
        for mid in retry_queue:
            r = test_model(chat_url, key, mid)
            if r["retryable"]:
                next_retry.append(mid)
                failed.pop(mid, None)
            elif r["ok"]:
                passed[mid] = r
                failed.pop(mid, None)
            else:
                failed[mid] = r
                passed.pop(mid, None)
            cprint(verbose_line(r))
            time.sleep(delay)

        retry_queue = next_retry

    if retry_queue:
        cprint(f"  ⚠️  {len(retry_queue)} models still rate-limited after {MAX_RETRY_PASSES} retry passes.")

    cprint(f"🏁 {PROVIDER_NAME}: {len(passed)} passed, {len(failed)} failed")
    return {"passed": list(passed.values()), "failed": len(failed), "total": len(kept)}

def _terminal_table(summary):
    passed = summary["passed"]
    total = summary["total"]
    lines = []
    lines.append("=" * 80)
    lines.append(f"VERIFIED MODELS — {PROVIDER_NAME}")
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
            lines.append(f"{i:<{idx_w}}  {r['id']:<{model_w}}  {str(r['latency']) + 's':<9}  {resp}")
        lines.append("-" * 80)
    lines.append(f"Verified: {len(passed)} / {total}")
    for ln in lines:
        cprint(ln)

def write_report(path, summary):
    passed = summary["passed"]
    total = summary["total"]
    lines = []
    lines.append("=" * 80)
    lines.append(f"VERIFIED MODELS — {PROVIDER_NAME}")
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
            lines.append(f"{i:<{idx_w}}  {r['id']:<{model_w}}  {str(r['latency']) + 's':<9}  {resp}")
        lines.append("-" * 80)
    lines.append(f"Verified: {len(passed)} / {total}")
    text = "\n".join(lines) + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return text

if __name__ == "__main__":
    date_tag = datetime.now().strftime("%Y-%m-%d")
    out = os.path.join(SCRIPT_DIR, f"verified_models_{date_tag}.txt")
    summary = run()
    report = write_report(out, summary)
    print()
    print(report)
    print(f"💾 Verified-models report written to '{out}'.")
