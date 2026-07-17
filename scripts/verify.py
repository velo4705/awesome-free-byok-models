#!/usr/bin/env python3
"""Verify free API models are responding and measure latency.

Usage:
  python3 scripts/verify.py

Set API keys in scripts/.env (templated from .env.example) or as env vars.
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
for dotenv_path in (os.path.join(_SCRIPT_DIR, ".env"), os.path.join(os.getcwd(), ".env")):
    try:
        with open(dotenv_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ.setdefault(key.strip(), val.strip().strip("\"'"))
    except FileNotFoundError:
        pass

TIMEOUT = 30

PROVIDERS = [
    {
        "name": "AION Labs",
        "chat_url": "https://api.aionlabs.ai/v1/chat/completions",
        "model": "aion-labs/aion-3.0",
        "env_key": "AIONLABS_API_KEY",
    },
    {
        "name": "Agnes AI",
        "chat_url": "https://apihub.agnes-ai.com/v1/chat/completions",
        "model": "agnes-1.5-flash",
        "env_key": "AGNESAI_API_KEY",
    },
    {
        "name": "AnyAPI AI",
        "chat_url": "https://api.anyapi.ai/v1/chat/completions",
        "model": "liquid/lfm-2.5-1.2b-instruct:free",
        "env_key": "ANYAPI_API_KEY",
    },
    {
        "name": "Auriko",
        "chat_url": "https://api.auriko.ai/v1/chat/completions",
        "model": "glm-4.5-flash",
        "env_key": "AURIKO_API_KEY",
    },
    {
        "name": "Cerebras AI",
        "chat_url": "https://api.cerebras.ai/v1/chat/completions",
        "model": "gemma-4-31b",
        "env_key": "CEREBRAS_API_KEY",
    },
    {
        "name": "Cloudflare Workers AI",
        "chat_url": "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions",
        "model": "@cf/google/gemma-2b-it-lora",
        "env_key": "WORKERS_API_KEY",
        "requires_account_id": True,
        "account_id_key": "CLOUDFLARE_ACCOUNT_ID",
    },
    {
        "name": "Cohere AI",
        "chat_url": "https://api.cohere.com/v2/chat",
        "model": "command-r-08-2024",
        "env_key": "COHERE_API_KEY",
    },
    {
        "name": "ElectronHub",
        "chat_url": "https://api.electronhub.ai/v1/chat/completions",
        "model": "gpt-oss-120b",
        "env_key": "ELECTRON_API_KEY",
    },
    {
        "name": "FastRouter",
        "chat_url": "https://api.fastrouter.ai/api/v1/chat/completions",
        "model": "sarvam/sarvam-105b:free",
        "env_key": "FASTR_API_KEY",
    },
    {
        "name": "FreeInference",
        "chat_url": "https://freeinference.org/v1/chat/completions",
        "model": "deepseek-v4-flash",
        "env_key": "FREEINFERENCE_API_KEY",
    },
    {
        "name": "GitHub Models",
        "chat_url": "https://models.inference.ai.azure.com/chat/completions",
        "model": "gpt-4o",
        "env_key": "GITHUB_API_KEY",
    },
    {
        "name": "Google Gemini",
        "chat_url": "https://generativelanguage.googleapis.com/v1beta",
        "model": "gemini-flash-lite-latest",
        "env_key": "GOOGLE_API_KEY",
        "is_gemini": True,
    },
    {
        "name": "Groq API",
        "chat_url": "https://api.groq.com/openai/v1/chat/completions",
        "model": "llama-3.3-70b-versatile",
        "env_key": "GROQ_API_KEY",
    },
    {
        "name": "HelixMind",
        "chat_url": "https://helixmind.online/v1/chat/completions",
        "model": "gpt-oss-20b",
        "env_key": "HELIX_API_KEY",
    },
    {
        "name": "HelyxAI",
        "chat_url": "https://helyxai.space/v1/chat/completions",
        "model": "DeepSeek-V4-Flash",
        "env_key": "HELYX_API_KEY",
    },
    {
        "name": "Hugging Face Inference API",
        "chat_url": "https://router.huggingface.co/v1/chat/completions",
        "model": "google/gemma-4-26B-A4B-it",
        "env_key": "HF_API_KEY",
    },
    {
        "name": "Intern AI",
        "chat_url": "https://chat.intern-ai.org.cn/api/v1/chat/completions",
        "model": "intern-latest",
        "env_key": "INTERN_API_KEY",
    },
    {
        "name": "Kilo Code",
        "chat_url": "https://api.kilo.ai/api/gateway/chat/completions",
        "model": "kilo-auto/small",
        "env_key": "KILO_API_KEY",
    },
    {
        "name": "LLM.Kiwi",
        "chat_url": "https://api.llm.kiwi/v1/chat/completions",
        "model": "auto",
        "env_key": "KIWI_API_KEY",
    },
    {
        "name": "LLM7.IO",
        "chat_url": "https://api.llm7.io/v1/chat/completions",
        "model": "codestral-latest",
        "env_key": "LLM_API_KEY",
    },
    {
        "name": "LLMGateway",
        "chat_url": "https://api.llmgateway.io/v1/chat/completions",
        "model": "claude-haiku-4-5-free",
        "env_key": "LLMGATE_API_KEY",
    },
    {
        "name": "LiteRouter",
        "chat_url": "https://api.literouter.com/v1/chat/completions",
        "model": "deepseek-v4-flash:free",
        "env_key": "LITEROUTER_API_KEY",
    },
    {
        "name": "MNN AI",
        "chat_url": "https://api2.mnnai.ru/v1/chat/completions",
        "model": "deepseek-v3.1",
        "env_key": "MNN_API_KEY",
    },
    {
        "name": "MegaNova AI",
        "chat_url": "https://api.meganova.ai/v1/chat/completions",
        "model": "BruhzWater/Sapphira-L3.3-70b-0.1",
        "env_key": "MEGANOVA_API_KEY",
    },
    {
        "name": "Mistral AI",
        "chat_url": "https://api.mistral.ai/v1/chat/completions",
        "model": "mistral-code-agent-latest",
        "env_key": "MISTRAL_API_KEY",
    },
    {
        "name": "Mixlayer",
        "chat_url": "https://models.mixlayer.ai/v1/chat/completions",
        "model": "qwen/qwen3.5-4b-free",
        "env_key": "MIXLAYER_API_KEY",
    },
    {
        "name": "Naga AI",
        "chat_url": "https://api.naga.ac/v1/chat/completions",
        "model": "llama-4-scout-17b-16e-instruct:free",
        "env_key": "NAGA_API_KEY",
    },
    {
        "name": "Navy API",
        "chat_url": "https://api.navy/v1/chat/completions",
        "model": "deepseek-v4-flash",
        "env_key": "NAVY_API_KEY",
    },
    {
        "name": "NVIDIA NIM",
        "chat_url": "https://integrate.api.nvidia.com/v1/chat/completions",
        "model": "deepseek-ai/deepseek-v4-flash",
        "env_key": "NVIDIA_API_KEY",
    },
    {
        "name": "Ollama Cloud",
        "chat_url": "https://api.ollama.com/api/chat",
        "model": "gpt-oss:120b",
        "env_key": "OLLAMA_API_KEY",
        "is_ollama": True,
    },
    {
        "name": "OpenCode Zen",
        "chat_url": "https://opencode.ai/zen/v1/chat/completions",
        "model": "deepseek-v4-flash-free",
        "env_key": "ZEN_API_KEY",
    },
    {
        "name": "OpenRouter",
        "chat_url": "https://openrouter.ai/api/v1/chat/completions",
        "model": "nvidia/nemotron-nano-12b-v2-vl:free",
        "env_key": "OPENROUTER_API_KEY",
    },
    {
        "name": "Poixe AI",
        "chat_url": "https://api.poixe.com/v1/chat/completions",
        "model": "qwen3-235b-a22b-instruct-2507:free",
        "env_key": "POIXE_API_KEY",
    },
    {
        "name": "Poolside",
        "chat_url": "https://inference.poolside.ai/v1/chat/completions",
        "model": "poolside/laguna-m.1",
        "env_key": "POOLSIDE_API_KEY",
    },
    {
        "name": "Routeway AI",
        "chat_url": "https://api.routeway.ai/v1/chat/completions",
        "model": "laguna-xs.2:free",
        "env_key": "ROUTEWAY_API_KEY",
    },
    {
        "name": "SambaNova AI",
        "chat_url": "https://api.sambanova.ai/v1/chat/completions",
        "model": "DeepSeek-V3.1",
        "env_key": "SAMBANOVA_API_KEY",
    },
    {
        "name": "Speka AI",
        "chat_url": "https://speka.me/v1/chat/completions",
        "model": "deepseek-ai/deepseek-v4-flash",
        "env_key": "SPEKA_API_KEY",
    },
    {
        "name": "TokenReply",
        "chat_url": "https://api.tokenreply.com/v1/chat/completions",
        "model": "deepseek-v4-flash",
        "env_key": "TOKENREP_API_KEY",
    },
    {
        "name": "Void AI",
        "chat_url": "https://api.voidai.app/v1/chat/completions",
        "model": "deepseek-v4-pro",
        "env_key": "VOID_API_KEY",
    },
    {
        "name": "Yolo-Auto",
        "chat_url": "https://yolo-auto.com/v1/chat/completions",
        "model": "qwen3.6-35b-a3b",
        "env_key": "YOLO_API_KEY",
    },
    {
        "name": "Z.AI (Zhipu AI)",
        "chat_url": "https://api.z.ai/api/paas/v4/chat/completions",
        "model": "glm-4.7-flash",
        "env_key": "ZAI_API_KEY",
    },
    {
        "name": "Zylo API",
        "chat_url": "https://api.zyloai.net/v1/chat/completions",
        "model": "deepseek-v4",
        "env_key": "ZYLO_API_KEY",
    },
]


def test_provider(provider):
    api_key = os.environ.get(provider["env_key"], "")
    if not api_key:
        return "SKIPPED", 0

    url = provider["chat_url"].rstrip("/")

    if provider.get("requires_account_id"):
        account_id_key = provider.get("account_id_key", "CLOUDFLARE_ACCOUNT_ID")
        account_id = os.environ.get(account_id_key, "")
        if not account_id:
            return "SKIPPED", 0
        url = url.replace("{account_id}", account_id)

    if provider.get("is_gemini"):
        model_name = provider["model"]
        url = f"{provider['chat_url'].rstrip('/')}/models/{model_name}:generateContent?key={api_key}"
        body = json.dumps({
            "contents": [{"parts": [{"text": "Respond with OK"}]}],
            "generationConfig": {"maxOutputTokens": 10},
        }).encode()
        headers = {"Content-Type": "application/json"}
    elif provider.get("is_ollama"):
        body = json.dumps({
            "model": provider["model"],
            "messages": [{"role": "user", "content": "Respond with OK"}],
            "stream": False,
        }).encode()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
    elif provider.get("is_cohere"):
        body = json.dumps({
            "model": provider["model"],
            "message": "Respond with OK",
            "max_tokens": 10,
        }).encode()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
    else:
        body = json.dumps({
            "model": provider["model"],
            "messages": [{"role": "user", "content": "Respond with OK"}],
            "max_tokens": 10,
            "stream": False,
        }).encode()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            elapsed = round(time.time() - start, 2)
            if resp.status == 200:
                return "OK", elapsed
            return f"HTTP {resp.status}", elapsed
    except urllib.error.HTTPError as e:
        elapsed = round(time.time() - start, 2)
        return f"HTTP {e.code}", elapsed
    except Exception as e:
        elapsed = round(time.time() - start, 2)
        return "ERROR", elapsed


def main():
    passed = 0
    skipped = 0
    failed = 0

    for p in PROVIDERS:
        status, latency = test_provider(p)

        if status == "OK":
            passed += 1
            icon = "✅"
        elif status == "SKIPPED":
            skipped += 1
            icon = "⏭️"
        else:
            failed += 1
            icon = "❌"

        if status == "SKIPPED":
            print(f"  {icon} [{p['name']}] SKIPPED (set ${p['env_key']})")
        else:
            print(f"  {icon} [{p['name']}] {status} ({latency}s)")

    print(f"\n🏁 {passed} passed, {failed} failed, {skipped} skipped ({len(PROVIDERS)} total)")


if __name__ == "__main__":
    main()
