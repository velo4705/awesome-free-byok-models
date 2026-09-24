<h1 align="center">
  <a href="https://github.com/velo4705/awesome-free-byok-models">
    <img src="media/awesome-free-byok-models.svg" alt="Awesome Free BYOK Models" width="90%">
  </a>
</h1>

<p align="center">
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg" alt="Awesome">
  </a>
</p>

Text‑generation LLM API models that are currently available as free and self‑replenishing from their API providers, stress‑tested for coding and for everyday chat.

By using a **Bring Your Own Key (BYOK)** approach, you can plug your free API keys into **coding tools**, **custom projects**, or **AI-powered apps** -- no credit card required. Every model listed here is rated for coding capability, but most work just as well for general conversation.

> [!TIP]
> **Free tiers can change.** If a model hits rate limits, switch to another -- there's always a backup in this list.

> [!NOTE]
> Always verify current quotas on the provider's console before building workflows.

**Scope:** Text-generation LLM API models with a *currently available, self-replenishing free tier* -- without requiring billing information at signup, the quota resets without manual top-up, and the endpoint is accessible via a standard API call (OpenAI-compatible or provider-native). This excludes image generation models, models behind a paywall after a trial, services requiring government ID or credit card verification beyond a simple phone check, reverse-engineered access to gated models, and mainland China gateways requiring residency verification.

**Removal policy:** A model or provider is removed when (a) the free tier is paywalled or discontinued, (b) the endpoint is deprecated with no free replacement, (c) the provider adds mandatory verification what's stated in Scope, or (d) daily/monthly credits no longer replenish automatically.

**Data sources:** Quota, context size, and latency figures are drawn from provider documentation and live API verification via `scripts/verify.py`[^1]. Latency is measured from request to first token under typical network conditions and will vary. Providers are marked with a verification date showing when their free tier was last confirmed working.

**Use responsibly.** This list is for developers -- not for scraping, reselling, or bulk harvesting. Respect each provider's rate limits and terms of service.

## Contents

- [Recommended API Providers](#recommended-api-providers)
- [Replenishable Providers](#replenishable-providers)
- [Non-Replenishable Providers](#non-replenishable-providers)

## Recommended API Providers

Providers offering the strongest verified free tiers across different trade-offs, tabulated based on quota, context, and latency -- measured via [`scripts/verify.py`](scripts/verify.py):

| Provider                                                           | Profile            | Why It Matters For You                                                                    |
| :----------------------------------------------------------------- | :----------------- | :---------------------------------------------------------------------------------------- |
| **[Groq API](https://console.groq.com/docs/quickstart)**           | Low Latency        | 14,400 RPD / 18,000 TPM at sub-300ms latency; 131K-context models.                        |
| **[Void AI](https://docs.voidai.app/quickstart)**                  | High RPM           | 100 RPM / 125,000 daily credits; 400K-context code model.                                 |
| **[Intern AI](https://internlm.intern-ai.org.cn/api)**             | High Volume        | 90M tokens/month (3M TPD) / 300,000 TPM; 256K-context model at ~1.0s.                     |
| **[Google Gemini](https://ai.google.dev/gemini-api/docs/models)**  | Long Context       | Uncapped TPD / 1M TPM; 1M-context model at ~1.5s, up to 500 RPD.                          |
| **[xKiro AI](https://docs.xkiro.com)**                             | Code Speed         | 5M TPD / free models only; dedicated code model at ~0.57s latency.                        |

---

## Replenishable Providers

Providers that replenish their free tier on a fixed cycle -- daily, weekly, or monthly quotas of credits or tokens.

Filtered for coding and general chat capability across 37 Replenishable providers.

<strong>Jump to a provider or hub:</strong>

<ul>
  <li><a href="#aion-labs">AION Labs</a></li>
  <li><a href="#anyapi-ai">AnyAPI AI</a></li>
  <li><a href="#cloudflare-workers-ai">Cloudflare Workers AI</a></li>
  <li><a href="#cohere-ai">Cohere AI</a></li>
  <li><a href="#electronhub">ElectronHub</a></li>
  <li><a href="#evolvex">EvolveX</a></li>
  <li><a href="#freeai">Free.ai</a></li>
  <li><a href="#freeinference">FreeInference</a></li>
  <li><a href="#google-gemini">Google Gemini</a></li>
  <li><a href="#gonka-broker">Gonka Broker</a></li>
  <li><a href="#groq-api">Groq API</a></li>
  <li><a href="#helixmind">HelixMind</a></li>
  <li><a href="#hugging-face-inference-api">Hugging Face Inference API</a></li>
  <li><a href="#intern-ai">Intern AI</a></li>
  <li><a href="#kilo-gateway">Kilo Gateway</a></li>
  <li><a href="#literouter">LiteRouter</a></li>
  <li><a href="#llmkiwi">LLM.Kiwi</a></li>
  <li><a href="#llm7io">LLM7.IO</a></li>
  <li><a href="#meganova-ai">MegaNova AI</a></li>
  <li><a href="#mistral-ai">Mistral AI</a></li>
  <li><a href="#mixlayer">Mixlayer</a></li>
  <li><a href="#naga-ai">Naga AI</a></li>
  <li><a href="#nvidia-nim">NVIDIA NIM</a></li>
  <li><a href="#ollama-cloud">Ollama Cloud</a></li>
  <li><a href="#orcarouter">Orcarouter</a></li>
  <li><a href="#poixe-ai">Poixe AI</a></li>
  <li><a href="#pooled-ai">Pooled AI</a></li>
  <li><a href="#poolside">Poolside</a></li>
  <li><a href="#routeway-ai">Routeway AI</a></li>
  <li><a href="#sea-lion">SEA-LION</a></li>
  <li><a href="#tokenreply">TokenReply</a></li>
  <li><a href="#void-ai">Void AI</a></li>
  <li><a href="#xkiro-ai">xKiro AI</a></li>
  <li><a href="#yolo-auto">Yolo-Auto</a></li>
  <li><a href="#zhipu-ai">Zhipu AI</a></li>
  <li><a href="#zydit-ai">Zydit AI</a></li>
  <li><a href="#zylo-api">Zylo API</a></li>
</ul>

### [AION Labs](https://www.aionlabs.ai)

AION Labs provides storytelling-optimized models through an OpenAI-compatible API. The free tier offers 20,000 tokens/day and 15 RPM -- a solid option if you need a daily token allowance for lightweight coding and creative tasks. AION Labs currently has 5 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ⚠️             | ✅               |

🎁 **Free Tier Quota:** 15 RPM / 20,000 TPD

🔗 **Base URL:** `https://api.aionlabs.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                       | Context | Best For   | Latency |
| :------------------------------- | ------- | ---------- | ------- |
| `aion-labs/aion-2.0`             | 128K    | `General`  | ~1.4s   |
| `aion-labs/aion-3.0`             | 128K    | `Code`     | ~1.6s   |
| `aion-labs/aion-3.0-mini`        | 128K    | `General`  | ~1.5s   |
| `aion-labs/aion-3.5`             | 128K    | `Code`     | ~1.4s   |
| `aion-labs/aion-3.5-mini`        | 128K    | `General`  | ~1.5s   |

### [AnyAPI AI](https://anyapi.ai)

AnyAPI is a unified API gateway providing access to 400+ models from OpenAI, Anthropic, Google, DeepSeek, Meta, Mistral, Cohere, and more through a single OpenAI-compatible endpoint. The free tier offers 100,000 tokens/day with access to free and basic models. AnyAPI currently has 4 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 100,000 tokens/day / No Credit Card

🔗 **Base URL:** `https://api.anyapi.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                                           | Context | Best For    | Latency |
| :--------------------------------------------------- | ------- | ----------- | ------- |
| `dots-studio/dots-3-note-preview:free`               | 32K     | `General`   | ~1.6s   |
| `google/gemma-4-26b-a4b-it:free`                     | 32K     | `General`   | ~1.5s   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 128K    | `Reasoning` | ~8.8s   |
| `nvidia/nemotron-3-ultra-550b-a55b:free`             | 128K    | `Reasoning` | ~9.1s   |

### [Cloudflare Workers AI](https://dash.cloudflare.com)

Cloudflare Workers AI runs models on Cloudflare's global edge network using serverless GPUs. The free tier offers 10,000 requests/day shared across all models with near-zero latency from edge locations worldwide. Cloudflare Workers AI currently has 23 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 150 to 1,500 RPM / 100,000 RPD / 13,000 TPD

🔗 **Base URL:** `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1` (replace `{account_id}` with your Cloudflare account ID)

✅ **Verified:** September 24, 2026

> [!IMPORTANT]
> **Two API paths:** The `/chat/completions` endpoint takes standard `"messages"` (OpenAI-compatible). The legacy `/run/{model}` endpoint uses `"prompt"` instead -- make sure your tool targets the right one.

| Free Model                                     | Context | Best For    | Latency |
| :--------------------------------------------- | ------- | ----------- | ------- |
| `@cf/qwen/qwen2.5-coder-32b-instruct`          | 32K     | `Code`      | ~0.7s   |
| `@cf/aisingapore/gemma-sea-lion-v4-27b-it`     | 128K    | `General`   | ~0.5s   |
| `@cf/google/gemma-2b-it-lora`                  | 8K      | `Fallback`  | ~0.5s   |
| `@cf/google/gemma-4-26b-a4b-it`                | 256K    | `General`   | ~0.5s   |
| `@cf/meta/llama-3.2-1b-instruct`               | 60K     | `Fallback`  | ~0.6s   |
| `@cf/meta/llama-3.2-3b-instruct`               | 80K     | `Fallback`  | ~0.5s   |
| `@cf/meta/llama-3.3-70b-instruct-fp8-fast`     | 24K     | `Reasoning` | ~0.9s   |
| `@cf/meta/llama-4-scout-17b-16e-instruct`      | 131K    | `General`   | ~0.6s   |
| `@cf/mistral/mistral-7b-instruct-v0.2-lora`    | 15K     | `Fallback`  | ~0.7s   |
| `@cf/mistralai/mistral-small-3.1-24b-instruct` | 128K    | `General`   | ~0.8s   |
| `@cf/nvidia/nemotron-3-120b-a12b`              | 256K    | `Reasoning` | ~0.7s   |
| `@cf/openai/gpt-oss-120b`                      | 128K    | `Code`      | ~0.7s   |
| `@cf/openai/gpt-oss-20b`                       | 128K    | `General`   | ~0.6s   |
| `@cf/qwen/qwen3-30b-a3b-fp8`                   | 32K     | `General`   | ~0.9s   |
| `@cf/qwen/qwen3.8-27b`                         | 262K    | `General`   | ~0.7s   |
| `@cf/zai-org/glm-4.7-flash`                    | 131K    | `Agent`     | ~0.5s   |
| `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | 80K     | `Reasoning` | ~0.7s   |
| `@cf/google/gemma-7b-it-lora`                  | 3K      | `General`   | ~1.1s   |
| `@cf/ibm-granite/granite-4.0-h-micro`          | 131K    | `General`   | ~0.9s   |
| `@cf/meta-llama/llama-2-7b-chat-hf-lora`       | 8K      | `Fallback`  | ~0.5s   |
| `@cf/meta/llama-3.1-8b-instruct-fp8`           | 32K     | `General`   | ~0.9s   |
| `@cf/meta/llama-3.2-11b-vision-instruct`       | 128K    | `Vision`    | ~0.9s   |
| `@cf/qwen/qwq-32b`                             | 24K     | `Reasoning` | ~0.8s   |

### [Cohere AI](https://dashboard.cohere.com)

Cohere focuses on enterprise-grade NLP with their Command model family -- built for RAG, tool use, and coding workflows. The free API tier offers replenishable credits with daily resets, and nearly every model delivers sub-second responses. Cohere AI currently has 11 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / 1,000 API calls per month

🔗 **Base URL:** `https://api.cohere.com/v2`

✅ **Verified:** September 24, 2026
| Free Model                    | Context | Best For    | Latency |
| :---------------------------- | ------- | ----------- | ------- |
| `command-a-03-2025`           | 256K    | `Agent`     | ~0.55s  |
| `c4ai-aya-vision-32b`         | 16K     | `Vision`    | ~0.55s  |
| `command-a-plus-05-2026`      | 128K    | `Agent`     | ~0.55s  |
| `command-a-vision-07-2025`    | 128K    | `Vision`    | ~0.55s  |
| `command-r-08-2024`           | 128K    | `General`   | ~0.51s  |
| `command-r-plus-08-2024`      | 128K    | `Reasoning` | ~0.54s  |
| `command-r7b-12-2024`         | 128K    | `Code`      | ~0.5s   |
| `command-r7b-arabic-02-2025`  | 128K    | `General`   | ~0.56s  |
| `c4ai-aya-expanse-32b`        | 128K    | `General`   | ~0.82s  |
| `command-a-reasoning-08-2025` | 256K    | `Reasoning` | ~0.66s  |
| `command-a-translate-08-2025` | 8K      | `Fallback`  | ~0.55s  |

### [ElectronHub](https://electronhub.ai)

ElectronHub is a credit-based inference hub offering an enormous catalog of models from OpenAI, Google, Meta, Mistral, Cohere, DeepSeek, Qwen, Microsoft, and more through an OpenAI-compatible endpoint. The free tier provides 5 RPM with $0.25 in weekly credits -- replenishes every week, but the dollar cap limits heavy usage. Best for targeted queries and efficient coding. ElectronHub currently has 40 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ❌               |

🎁 **Free Tier Quota:** 5 RPM / $0.25 Weekly Credits

🔗 **Base URL:** `https://api.electronhub.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                         | Context | Best For    | Latency |
| :--------------------------------- | ------- | ----------- | ------- |
| `codestral-latest`                 | 256K    | `Code`      | ~1.1s   |
| `codestral-2508`                   | 256K    | `Code`      | ~1.92s  |
| `command-nightly`                  | 128K    | `General`   | ~0.95s  |
| `deepseek-v4-flash`                | 1M      | `Reasoning` | ~3.15s  |
| `deepseek-v4-flash-thinking`       | 1M      | `Reasoning` | ~2.43s  |
| `devstral-medium-latest`           | 262K    | `Code`      | ~5.71s  |
| `gemini-2.5-flash-lite`            | 1M      | `General`   | ~3.05s  |
| `gemini-2.5-flash`                 | 1M      | `General`   | ~3.25s  |
| `gemini-3.5-flash-lite`            | 1M      | `General`   | ~4.17s  |
| `glm-4.7-flash`                    | 128K    | `General`   | ~3.04s  |
| `gpt-3.5-turbo`                    | 4K      | `General`   | ~3.07s  |
| `gpt-4.1-nano`                     | 1M      | `Code`      | ~1.92s  |
| `gpt-4.1-mini`                     | 1M      | `General`   | ~1.2s   |
| `gpt-4.1`                          | 1M      | `General`   | ~1.2s   |
| `gpt-4o-mini`                      | 128K    | `General`   | ~1.62s  |
| `gpt-4o`                           | 128K    | `General`   | ~1.2s   |
| `gpt-5-mini`                       | 400K    | `General`   | ~2.63s  |
| `gpt-5-nano`                       | 400K    | `General`   | ~2.64s  |
| `gpt-5.4-mini`                     | 400K    | `General`   | ~1.82s  |
| `gpt-5.6-luna`                     | 400K    | `General`   | ~2.43s  |
| `gpt-oss-120b`                     | 128K    | `Reasoning` | ~2.84s  |
| `laguna-s-2.1`                     | 262K    | `Code`      | ~3.39s  |
| `ling-3.0-flash-fin`               | 128K    | `General`   | ~1.92s  |
| `llama-3-70b`                      | 128K    | `General`   | ~1.51s  |
| `llama-4-scout-17b-16e-instruct`   | 128K    | `General`   | ~1.41s  |
| `magistral-medium-latest`          | 262K    | `Reasoning` | ~5.59s  |
| `minimax-m2.7`                     | 200K    | `General`   | ~2.84s  |
| `minimax-m3`                       | 1M      | `General`   | ~1.41s  |
| `ministral-14b-2512`               | 262K    | `General`   | ~1.61s  |
| `ministral-3b-2512`                | 131K    | `Code`      | ~1.18s  |
| `mistral-code-latest`              | 256K    | `Code`      | ~1.1s   |
| `mistral-small-3.2-24b-instruct`   | 128K    | `Code`      | ~1.18s  |
| `north-mini-code-1-0`              | 131K    | `Code`      | ~1.41s  |
| `o3-mini`                          | 200K    | `Reasoning` | ~4.02s  |
| `o4-mini`                          | 200K    | `Reasoning` | ~2.02s  |
| `phi-4`                            | 16K     | `General`   | ~1.1s   |
| `qwen-2.5-coder-32b-instruct`      | 33K     | `Code`      | ~0.8s   |
| `qwen-2.5-coder-7b-instruct`       | 32K     | `Code`      | ~0.69s  |
| `qwen3-coder-30-a3b-instruct`      | 262K    | `Code`      | ~1.2s   |
| `qwen3.8-flash`                    | 1M      | `General`   | ~4.77s  |

### [EvolveX](https://evolvex.gg)

EvolveX is a lightweight inference hub offering models from Google, Meta, MiniMax, NVIDIA, Poolside, OpenAI, and Moonshot through an OpenAI-compatible endpoint. The free tier provides 5 RPM with unspecified RPD -- generous for light coding and general tasks with a diverse model pool. EvolveX currently has 14 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 5 RPM / Unspecified RPD

🔗 **Base URL:** `https://api.evolvex.gg/v1`

✅ **Verified:** September 24, 2026
| Free Model                                      | Context | Best For      | Latency |
| :---------------------------------------------- | ------- | ------------- | ------- |
| `google/diffusiongemma-26b-a4b-it`              | 262K    | `General`     | ~2.56s  |
| `meta/llama-3.2-11b-vision-instruct`            | 128K    | `Vision`      | ~1.06s  |
| `meta/muse-glimmer-30b`                         | 131K    | `General`     | ~5.36s  |
| `nvidia/ising-calibration-1.5-31b`              | 32K     | `General`     | ~1.3s   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | 1M      | `Reasoning`   | ~5.99s  |
| `nvidia/nemotron-3-super-120b-a12b`             | 1M      | `General`     | ~2.21s  |
| `nvidia/nemotron-3-ultra-550b-a55b`             | 1M      | `General`     | ~14.78s |
| `nvidia/nemotron-3.5-lightning-30b-a3b`         | 262K    | `General`     | ~13.55s |
| `nvidia/riva-translate-4b-instruct-v1.1`        | 32K     | `Translation` | ~1.3s   |
| `nvidia/riva-translate-4b-instruct-v2`          | 32K     | `Translation` | ~1.3s   |
| `openai/gpt-oss-20b`                            | 131K    | `Code`        | ~2.3s   |
| `openai/gpt-5-2`                                | 400K    | `General`     | ~10.07s |
| `poolside/laguna-xs-2.1`                        | 128K    | `Code`        | ~5.23s  |
| `z-ai/glm-5.3-flash`                            | 128K    | `General`     | ~1.3s   |

### [Free.ai](https://free.ai)

Free.ai is a lightweight inference service offering self-hosted models via an OpenAI-compatible API. The free tier provides 10 RPM with 30,000 TPD and 1,000 requests per month for currently available self-hosted models. Free.ai currently has 4 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPM / 30,000 TPD / 1,000 Requests per month / Currently available self-hosted models only

🔗 **Base URL:** `https://api.free.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model   | Context | Best For  | Latency |
| :----------- | ------- | --------- | ------- |
| `qwen-vl`    | 32K     | `Vision`  | ~2.31s  |
| `qwen25-vl`  | 32K     | `Vision`  | ~1.67s  |
| `qwen3-8b`   | 128K    | `General` | ~1.37s  |
| `qwen7b`     | 32K     | `General` | ~2.65s  |

### [FreeInference](https://freeinference.org)

FreeInference is a research-backed inference hub providing access to models from GLM, MiniMax, Qwen, and DeepSeek through an OpenAI-compatible endpoint. The free tier offers $20 in daily credits with 2 concurrent requests. FreeInference currently has 3 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** $20 CPD / 2 Max Concurrent Requests

🔗 **Base URL:** `https://freeinference.org/v1`

✅ **Verified:** September 24, 2026

> [!IMPORTANT]
> **Non-Harvard users:** New accounts go through a manual review before they're ready to use.

| Free Model          | Context | Best For    | Latency |
| :------------------ | ------- | ----------- | ------- |
| `deepseek-v4-flash` | 1M      | `Reasoning` | ~1.31s  |
| `diffusiongemma`    | 262K    | `General`   | ~2.05s  |
| `qwen3.6-35b`       | 262K    | `Code`      | ~1.12s  |

### [Google Gemini](https://aistudio.google.com)

Gemini offers large context windows on paper, but the free tier's **rate limits vary by model** -- Flash-lite variants enjoy ~500 RPD, while standard models can be as low as 20 RPD. Use Gemini for quick, targeted tasks and single-file edits -- not marathon sessions. Google Gemini currently has 12 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 5-20 RPM / 20-500 RPD / 1M TPM / Uncapped TPD

🔗 **Base URL:** `https://generativelanguage.googleapis.com/v1beta`

✅ **Verified:** September 24, 2026
| Free Model                                               | Context | Best For    | Latency |
| :------------------------------------------------------- | ------- | ----------- | ------- |
| `models/gemini-2.5-flash`                                | 1M      | `Fallback`  | ~1.1s   |
| `models/gemini-2.5-flash-lite`                           | 1M      | `Fallback`  | ~0.9s   |
| `models/gemini-3-flash-preview`                          | 1M      | `General`   | ~1.5s   |
| `models/gemini-3.1-flash-lite`                           | 1M      | `General`   | ~0.7s   |
| `models/gemini-3.1-flash-lite-preview`                   | 1M      | `Fallback`  | ~1.0s   |
| `models/gemini-3.5-flash`                                | 1M      | `Code`      | ~1.7s   |
| `models/gemini-3.5-flash-lite`                           | 1M      | `General`   | ~1.5s   |
| `models/gemini-3.5-transcribe`                           | 1M      | `General`   | ~1.5s   |
| `models/gemini-3.6-flash`                                | 1M      | `Code`      | ~1.5s   |
| `models/gemini-flash-lite-latest`                        | 1M      | `General`   | ~0.9s   |
| `models/gemini-robotics-er-2-preview`                    | 256K    | `Reasoning` | ~2.5s   |
| `models/gemma-4-26b-a4b-it`                              | 32K     | `General`   | ~1.5s   |

### [Gonka Broker](https://gonkabroker.com/)

Gonka Broker is a proxy gateway routing requests to providers through a single OpenAI-compatible endpoint. The free tier offers 6 RPM with 1M tokens per month -- tight for sustained use, but the sub-second latencies make it a solid fallback for quick queries. Gonka Broker currently has 3 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ⚠️             | ✅               |

🎁 **Free Tier Quota:** 6 RPM / ~1M tokens per month

🔗 **Base URL:** `https://proxy.gonkabroker.com/v1/`

✅ **Verified:** September 24, 2026

> [!IMPORTANT]
> Requires **Phone Verification** to access free monthly tokens.

| Free Model                           | Context | Best For    | Latency |
| :----------------------------------- | ------- | ----------- | ------- |
| `deepseek-ai/DeepSeek-V4-Flash-0731` | 400K    | `Reasoning` | ~0.7s   |
| `MiniMaxAI/MiniMax-M2.7`             | 200K    | `Reasoning` | ~0.74s  |
| `zai-org/GLM-5.3-Flash`              | 128K    | `General`   | ~1.3s   |

### [Groq API](https://console.groq.com)

Groq provides low-latency inference. The free tier offers 30 RPM with replenishable daily credits -- enough for most use cases. Verification measures sub-300ms latency. Groq API currently has 4 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 30 RPM / 14,400 RPD / 18,000 TPM

🔗 **Base URL:** `https://api.groq.com/openai/v1`

✅ **Verified:** September 24, 2026
| Free Model                                  | Context | Best For   | Latency |
| :------------------------------------------ | ------- | ---------- | ------- |
| `allam-2-7b`                                | 131K    | `Fallback` | ~0.2s   |
| `openai/gpt-oss-120b`                       | 131K    | `Code`     | ~0.4s   |
| `openai/gpt-oss-20b`                        | 131K    | `Code`     | ~0.6s   |
| `qwen/qwen3.8-27b`                          | 131K    | `Code`     | ~0.3s   |

### [HelixMind](https://helixmind.online)

HelixMind is a lightweight inference hub offering a small set of free models from Meta, OpenAI, Mistral, and DeepSeek through an OpenAI-compatible endpoint. The free tier provides 3 RPM with 50 requests per day -- the tightest cap on this list, strictly for occasional queries and quick tests. HelixMind currently has 5 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 3 RPM / 50 RPD

🔗 **Base URL:** `https://helixmind.online/v1`

✅ **Verified:** September 24, 2026
| Free Model                        | Context | Best For    | Latency |
| :-------------------------------- | ------- | ----------- | ------- |
| `deepseek-v4-flash-0731-thinking` | 128K    | `Reasoning` | ~2.86s  |
| `gpt-oss-20b`                     | 128K    | `Code`      | ~2.4s   |
| `llama-4-scout`                   | 328K    | `General`   | ~1.1s   |
| `mimo-v2.5`                       | 1M      | `Code`      | ~1.1s   |
| `qwen3.6-35b-a3b`                 | 262K    | `General`   | ~2.1s   |

### [Hugging Face Inference API](https://huggingface.co/inference-api)

Hugging Face's free Inference API gives you access to thousands of community-hosted models with OpenAI-compatible endpoints. The free tier offers only $0.10/month in credits -- barely enough for light experimentation, not sustained coding. The real strength is model diversity across thousands of community models. Hugging Face currently has 98 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** $0.10/month credits (~650K tokens)

🔗 **Base URL:** `https://router.huggingface.co/v1`

✅ **Verified:** September 24, 2026
| Free Model                                          | Context | Best For    | Latency |
| :-------------------------------------------------- | ------- | ----------- | ------- |
| `deepcogito/cogito-671b-v2.1`                       | 128K    | `Reasoning` | ~0.7s   |
| `deepseek-ai/DeepSeek-R1`                           | 128K    | `Reasoning` | ~1.9s   |
| `deepseek-ai/DeepSeek-V3.1`                         | 128K    | `Reasoning` | ~1.8s   |
| `deepseek-ai/DeepSeek-V3.2`                         | 128K    | `Reasoning` | ~1.1s   |
| `deepseek-ai/DeepSeek-V4-Flash`                     | 128K    | `Reasoning` | ~1.2s   |
| `deepseek-ai/DeepSeek-V4-Pro`                       | 128K    | `Reasoning` | ~0.9s   |
| `meta-llama/Llama-3.3-70B-Instruct`                 | 128K    | `General`   | ~0.6s   |
| `moonshotai/Kimi-K2.7-Code`                         | 128K    | `Code`      | ~0.7s   |
| `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`    | 128K    | `Reasoning` | ~0.7s   |
| `Qwen/Qwen3-235B-A22B-Instruct-2507`                | 256K    | `Code`      | ~0.5s   |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct`                 | 256K    | `Code`      | ~0.8s   |
| `Qwen/Qwen3-Coder-480B-A35B-Instruct`               | 256K    | `Code`      | ~2.1s   |
| `Qwen/Qwen3-Coder-Next`                             | 256K    | `Code`      | ~0.8s   |
| `zai-org/GLM-5.2`                                   | 128K    | `General`   | ~0.8s   |
| `google/gemma-4-26B-A4B-it`                         | 32K     | `General`   | ~0.6s   |
| `google/gemma-4-31B-it`                             | 32K     | `General`   | ~0.5s   |
| `inclusionAI/Ling-2.6-1T`                           | 128K    | `Reasoning` | ~1.2s   |
| `meta-llama/Llama-3.1-70B-Instruct`                 | 128K    | `General`   | ~0.7s   |
| `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 256K    | `General`   | ~0.7s   |
| `meta-llama/Llama-4-Scout-17B-16E-Instruct`         | 256K    | `General`   | ~0.6s   |
| `microsoft/phi-4`                                   | 128K    | `Code`      | ~0.7s   |
| `MiniMaxAI/MiniMax-M3`                              | 1M      | `General`   | ~1.5s   |
| `moonshotai/Kimi-K2.5`                              | 128K    | `Reasoning` | ~0.7s   |
| `openai/gpt-oss-120b`                               | 128K    | `General`   | ~0.6s   |
| `pearl-ai/Gemma-4-31B-it-pearl`                     | 32K     | `General`   | ~2.4s   |
| `Qwen/Qwen2.5-Coder-32B-Instruct`                   | 128K    | `Code`      | ~0.7s   |
| `Qwen/Qwen2.5-VL-72B-Instruct`                      | 128K    | `Vision`    | ~0.9s   |
| `Qwen/Qwen3-235B-A22B`                              | 256K    | `Reasoning` | ~1.0s   |
| `Qwen/Qwen3-VL-30B-A3B-Instruct`                    | 128K    | `Vision`    | ~1.0s   |
| `Qwen/Qwen3.6-27B`                                  | 256K    | `General`   | ~1.0s   |
| `Qwen/Qwen3.6-35B-A3B`                              | 256K    | `Code`      | ~0.6s   |
| `zai-org/GLM-4.7`                                   | 128K    | `General`   | ~4.7s   |
| `tencent/Hy3`                                       | 128K    | `General`   | ~0.7s   |

### [Intern AI](https://internlm.intern-ai.org.cn)

Intern AI is the official API from Shanghai AI Laboratory for the InternLM model family. The free tier offers 90 million tokens per month. Intern AI currently has 11 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 30 RPM / 300,000 TPM / 90,000,000 Tokens per month (3,000,000 TPD)

🔗 **Base URL:** `https://chat.intern-ai.org.cn/api/v1/`

✅ **Verified:** September 24, 2026
| Free Model               | Context | Best For    | Latency |
| :----------------------- | ------- | ----------- | ------- |
| `intern-latest`          | 256K    | `General`   | ~1.0s   |
| `intern-s1`              | 32K     | `General`   | ~1.2s   |
| `intern-s1-mini`         | 32K     | `Fallback`  | ~1.0s   |
| `intern-s1-pro`          | 256K    | `Reasoning` | ~1.5s   |
| `intern-s2`              | 256K    | `Reasoning` | ~1.0s   |
| `intern-s2-preview`      | 256K    | `Reasoning` | ~1.0s   |
| `intern-s2-preview-35b`  | 256K    | `Reasoning` | ~1.5s   |
| `intern-s2-preview-397b` | 256K    | `Reasoning` | ~10.5s  |
| `internvl-latest`        | 128K    | `Vision`    | ~1.0s   |
| `internvl3.5-241b-a28b`  | 32K     | `Vision`    | ~1.1s   |
| `internvl3.5-latest`     | 32K     | `Vision`    | ~1.0s   |

### [Kilo Gateway](https://app.kilo.ai)

Kilo Gateway is a coding-agent platform that proxies free models from OpenRouter, NVIDIA, Poolside, and others through a single API key. The free tier offers generous replenishable credits with no hard daily cap -- a solid Swiss-army-knife provider that gives you access to a diverse model pool through one endpoint. Kilo Gateway currently has 14 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 5 RPM / 200 RPD

🔗 **Base URL:** `https://api.kilo.ai/api/gateway`

✅ **Verified:** September 24, 2026
| Free Model                                           | Context | Best For    | Latency |
| :--------------------------------------------------- | ------- | ----------- | ------- |
| `cohere/north-mini-code:free`                        | 128K    | `Code`      | ~1.5s   |
| `dots-studio/dots-3-note-preview:free`               | 32K     | `General`   | ~1.6s   |
| `inclusionai/ling-3.0-flash-fin:free`                | 262K    | `General`   | ~1.5s   |
| `inclusionai/ling-3.0-flash-sante:free`              | 262K    | `General`   | ~1.5s   |
| `inclusionai/ling-3.0-flash-vl:free`                 | 262K    | `Vision`    | ~1.5s   |
| `liquid/lfm-2.5-2.6b:free`                           | 65K     | `General`   | ~1.6s   |
| `nex-agi/nex-n2.5-mini:free`                         | 32K     | `General`   | ~1.5s   |
| `nex-agi/nex-n2.5-pro:free`                          | 32K     | `General`   | ~1.5s   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 128K    | `Reasoning` | ~2.5s   |
| `nvidia/nemotron-3-super-120b-a12b:free`             | 262K    | `General`   | ~0.8s   |
| `nvidia/nemotron-3-ultra-550b-a55b:free`             | 1M      | `General`   | ~14.78s |
| `poolside/laguna-s-2.1:free`                         | 262K    | `Code`      | ~1.3s   |
| `poolside/laguna-xs-2.1:free`                        | 128K    | `Code`      | ~1.9s   |
| `stepfun/step-3.7-flash:free`                        | 128K    | `General`   | ~2.5s   |

### [LiteRouter](https://literouter.com)

LiteRouter is a lightweight inference hub offering free models from OpenAI, DeepSeek, Mistral, Meta, and more through an OpenAI-compatible endpoint with a `:free` suffix. The free tier provides uncapped daily requests with 1 concurrent request and 15,000 tokens per day -- enough for light scripting and targeted queries. LiteRouter currently has 27 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ❌      | ✅              | ⚠️              |

🎁 **Free Tier Quota:** Unlimited Requests (for some Free models) / 1 concurrent request / 7s Cooldown

🔗 **Base URL:** `https://api.literouter.com/v1`

✅ **Verified:** September 24, 2026
| Free Model                               | Context | Best For    | Latency |
| :--------------------------------------- | ------- | ----------- | ------- |
| `deepseek-v3-0324:free`                  | 128K    | `Reasoning` | ~2.0s   |
| `deepseek-v3.1-terminus:free`            | 128K    | `Reasoning` | ~2.0s   |
| `deepseek-v3.1:free`                     | 128K    | `Reasoning` | ~2.0s   |
| `deepseek-v3.2:free`                     | 128K    | `Reasoning` | ~1.77s  |
| `deepseek-v3:free`                       | 128K    | `Reasoning` | ~2.0s   |
| `deepseek-v4-flash:free`                 | 1M      | `Reasoning` | ~2.63s  |
| `gemini-2.5-flash-lite:free`             | 1M      | `General`   | ~4.07s  |
| `gemini-2.5-flash:free`                  | 1M      | `General`   | ~4.54s  |
| `gemma-3-27b-it:free`                    | 32K     | `General`   | ~1.81s  |
| `gemma-4-31b:free`                       | 32K     | `General`   | ~1.8s   |
| `gemma-4-31b-it:free`                    | 32K     | `General`   | ~1.7s   |
| `glm-5.1:free`                           | 128K    | `General`   | ~5.87s  |
| `glm-5.2-cheap:free`                     | 128K    | `General`   | ~5.87s  |
| `glm-5.2:free`                           | 128K    | `General`   | ~5.87s  |
| `glm-5.3-cheap:free`                     | 128K    | `General`   | ~5.87s  |
| `glm-5.3-flash:free`                     | 128K    | `General`   | ~5.87s  |
| `glm-5:free`                             | 128K    | `General`   | ~5.87s  |
| `llama-3-8b-instruct:free`               | 128K    | `General`   | ~3.29s  |
| `llama-3.3-70b-instruct-turbo:free`      | 128K    | `General`   | ~2.18s  |
| `minimax-m2.7:free`                      | 200K    | `General`   | ~6.78s  |
| `ministral-3b-2512:free`                 | 128K    | `General`   | ~3.21s  |
| `mistral-large-2512:free`                | 128K    | `General`   | ~3.21s  |
| `mistral-large-3:free`                   | 128K    | `General`   | ~3.21s  |
| `mistral-medium-2508:free`               | 128K    | `General`   | ~3.21s  |
| `mistral-small-2603:free`                | 128K    | `General`   | ~3.21s  |
| `qwen3.6-27b:free`                       | 128K    | `General`   | ~5.36s  |
| `qwen3.8-27b:free`                       | 128K    | `General`   | ~5.36s  |

### [LLM.Kiwi](https://llm.kiwi)

LLM.Kiwi is a Cloudflare-edge inference provider offering an auto-routing endpoint that selects the best available model automatically, plus a Croatian-specific model. The free tier offers 40 requests per hour. LLM.Kiwi currently has 2 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ⚠️         | ❌      | ✅              | ✅               |

🎁 **Free Tier Quota:** 40 RPH / No Credit Card

🔗 **Base URL:** `https://api.llm.kiwi/v1`

✅ **Verified:** September 24, 2026
| Free Model | Context | Best For  | Latency |
| :--------- | :------ | :-------- | ------- |
| `auto`     | Varies  | `General` | ~1.0s   |
| `hrLLM`    | Varies  | `General` | ~2.4s   |

### [LLM7.IO](https://llm7.io)

LLM7.IO is a rising inference provider serving open-weight models via Llama.cpp server with OpenAI-compatible endpoints. The Turbo Tier (Free tier) offers replenishable credits with no daily hard cap -- a solid option for consistent daily coding on a simple API without commitment. LLM7.IO currently has 4 models verified -- all at Turbo Tier (Free tier).

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 40 RPM / 2,400 RPD / 128,000 Characters per Request / 1,000,000 TPD

🔗 **Base URL:** `https://api.llm7.io/v1`

✅ **Verified:** September 24, 2026
| Free Model                            | Context | Best For    | Latency |
| :------------------------------------ | ------- | ----------- | ------- |
| `GLM-5.3-Flash`                       | 128K    | `General`   | ~1.5s   |
| `codestral-latest`                    | 32K     | `Code`      | ~1.0s   |
| `minimax-m2.7`                        | 180K    | `Reasoning` | ~1.8s   |
| `mistral-Nemo-Instruct-2407`          | 128K    | `General`   | ~3.1s   |

### [MegaNova AI](https://meganova.ai)

MegaNova AI is a community-model inference hub offering fine-tuned variants of Llama, Mistral, and its own Manta series through an OpenAI-compatible endpoint. The free tier provides 60 RPM with 550 requests per day and 200,000 tokens per minute -- generous throughput for a community model hub. MegaNova AI currently has 8 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 60 RPM / 550 RPD / 200,000 TPM

🔗 **Base URL:** `https://api.meganova.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                                              | Context | Best For  | Latency |
| :------------------------------------------------------ | ------- | --------- | ------- |
| `BruhzWater/Sapphira-L3.3-70b-0.1`                      | 65K     | `General` | ~1.5s   |
| `FallenMerick/MN-Violet-Lotus-12B`                      | 8K      | `General` | ~1.3s   |
| `Sao10K/L3-70B-Euryale-v2.1`                            | 8K      | `General` | ~1.3s   |
| `Sao10K/L3-8B-Stheno-v3.2`                              | 8K      | `General` | ~1.0s   |
| `Steelskull/L3.3-MS-Nevoria-70b`                        | 65K     | `General` | ~1.5s   |
| `meganova-ai/manta-flash-1.0`                           | 16K     | `General` | ~1.1s   |
| `meganova-ai/manta-mini-1.0`                            | 8K      | `General` | ~1.3s   |
| `mistralai/Mistral-Small-3.2-24B-Instruct-2506`         | 8K      | `General` | ~1.5s   |

### [Mistral AI](https://console.mistral.ai)

Mistral AI provides models with a focus on instruction following and tool use. The free tier offers replenishable credits with per-model rate limits. Mistral AI currently has 12 models verified (with aliases).

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** ~2-30 RPM / 50,000 TPM shared pool

🔗 **Base URL:** `https://api.mistral.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                                          | Context | Best For    | Latency |
| :-------------------------------------------------- | ------- | ----------- | ------- |
| `codestral-latest` / `codestral-2508`               | 256K    | `Code`      | ~0.4s   |
| `ministral-14b-latest` / `ministral-14b-2512`       | 128K    | `General`   | ~0.4s   |
| `ministral-8b-latest` / `ministral-8b-2512`         | 128K    | `General`   | ~0.5s   |
| `ministral-3b-latest` / `ministral-3b-2512`         | 128K    | `General`   | ~0.4s   |
| `mistral-code-fim-latest`                           | 128K    | `Code`      | ~0.4s   |
| `mistral-code-latest`                               | 128K    | `Code`      | ~0.4s   |
| `voxtral-small-latest` / `voxtral-small-2507`       | 128K    | `General`   | ~0.6s   |

### [Mixlayer](https://www.mixlayer.com)

Mixlayer is an inference platform for open-source AI models with an OpenAI-compatible API. The free tier offers `qwen/qwen3.5-4b-free` for prototyping with rate limits. A focused Qwen 3.5/3.6 catalog with tool calling and reasoning support. Mixlayer currently has 1 model verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / Can be rate-limited (daily usage)

🔗 **Base URL:** `https://models.mixlayer.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model             | Context | Best For  | Latency |
| :--------------------- | ------- | --------- | ------- |
| `qwen/qwen3.5-4b-free` | 131K    | `General` | ~1.0s   |

### [Naga AI](https://naga.ac)

Naga AI is a lightweight inference hub offering a small set of free models from NVIDIA and Meta through an OpenAI-compatible endpoint. The free tier provides 10 RPM with 100 requests per day -- a very tight cap that limits it to occasional queries and quick debugging. Naga AI currently has 10 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPM / 100 RPD

🔗 **Base URL:** `https://api.naga.ac/v1`

✅ **Verified:** September 24, 2026
| Free Model                           | Context | Best For  | Latency |
| :----------------------------------- | ------- | --------- | ------- |
| `dots-3-note-preview:free`           | 32K     | `General` | ~1.6s   |
| `lfm-2.5-2.6b:free`                  | 65K     | `General` | ~1.6s   |
| `ling-3.0-flash-fin:free`            | 262K    | `General` | ~1.5s   |
| `ling-3.0-flash-sante:free`          | 262K    | `General` | ~1.5s   |
| `ling-3.0-flash-vl:free`             | 262K    | `Vision`  | ~1.5s   |
| `nemotron-3-super-120b-a12b:free`    | 262K    | `General` | ~0.8s   |
| `nemotron-3-ultra-550b-a55b:free`    | 1M      | `General` | ~14.78s |
| `nex-n2.5-mini:free`                 | 32K     | `General` | ~1.5s   |
| `nex-n2.5-pro:free`                  | 32K     | `General` | ~1.5s   |
| `sonar:free`                         | 128K    | `General` | ~1.63s  |

<!-- The Free tier for Navy API has been temporarily disabled. Will be re-added back to the list when it goes up. -->

### [NVIDIA NIM](https://build.nvidia.com)

NVIDIA NIM is NVIDIA's free API catalog offering 100+ models from DeepSeek, Meta, Mistral, Google, Qwen, and more through OpenAI-compatible endpoints. The largest free model library on the list, but 40 RPM per model caps it as a backup pool rather than a daily driver. Only models tagged as **Free Endpoint** (hosted on NVIDIA's own infrastructure) are listed below. NVIDIA NIM currently has 10 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ❌              | ✅               |

🎁 **Free Tier Quota:** 40 RPM / Uncapped TPD

🔗 **Base URL:** `https://integrate.api.nvidia.com/v1`

✅ **Verified:** September 24, 2026

> [!IMPORTANT]
> May require **Phone verification** to generate an API Key.

| Free Model                                      | Context | Best For      | Latency |
| :---------------------------------------------- | ------- | ------------- | ------- |
| `meta/llama-3.2-11b-vision-instruct`            | 128K    | `Vision`      | ~1.0s   |
| `mistralai/mistral-nemotron`                    | 128K    | `General`     | ~2.0s   |
| `nvidia/ising-calibration-1.5-31b`              | 32K     | `General`     | ~1.3s   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | 1M      | `Reasoning`   | ~0.4s   |
| `nvidia/nemotron-3-super-120b-a12b`             | 1M      | `Reasoning`   | ~0.7s   |
| `nvidia/nemotron-3-ultra-550b-a55b`             | 1M      | `General`     | ~14.78s |
| `nvidia/riva-translate-4b-instruct-v1.1`        | 32K     | `Translation` | ~1.3s   |
| `nvidia/riva-translate-4b-instruct-v2`          | 32K     | `Translation` | ~1.3s   |
| `openai/gpt-oss-20b`                            | 131K    | `General`     | ~2.0s   |
| `poolside/laguna-xs-2.1`                        | 128K    | `Code`        | ~0.9s   |

### [Ollama Cloud](https://ollama.com)

Ollama Cloud is a cloud-hosted inference service running Ollama behind the scenes, offering a vast model registry without the need to run locally. The free tier gives you a 5-hour session window that resets weekly -- uncapped during that window but limited by the weekly refresh. Models respond cleanly and quickly, making it one of the stronger free providers for coding if you plan around the session. Ollama Cloud currently has 6 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 1 Instance / 5-Hour Session Usage / 7-day Weekly Usage

🔗 **Base URL:** `https://api.ollama.com`

✅ **Verified:** September 24, 2026
| Free Model            | Context | Best For    | Latency |
| :-------------------- | ------- | ----------- | ------- |
| `gemma4:31b`          | 256K    | `General`   | ~3.8s   |
| `gpt-oss:120b`        | 128K    | `General`   | ~1.3s   |
| `gpt-oss:20b`         | 128K    | `Reasoning` | ~1.3s   |
| `nemotron-3-nano:30b` | 1M      | `Reasoning` | ~2.1s   |
| `nemotron-3-super`    | 256K    | `General`   | ~2.0s   |
| `nemotron-3-ultra`    | 256K    | `General`   | ~1.5s   |

### [Orcarouter](https://orcarouter.ai)

Orcarouter is an API gateway offering free models via an OpenAI-compatible API. The free tier has unspecified rate limits (they exist, but are not mentioned) for free models, which means that it can be suited for light coding and general conversations. Orcarouter currently has 4 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** Unspecified rate limits / Free models only

🔗 **Base URL:** `https://api.orcarouter.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                          | Context | Best For  | Latency |
| :---------------------------------- | ------- | --------- | ------- |
| `deepseek/deepseek-v4-flash-free`   | 1M      | `General` | ~1.38s  |
| `orcarouter/free`                   | Varies  | `General` | ~1.31s  |
| `z-ai/glm-5.3-flash-free`           | 128K    | `General` | ~2.07s  |
| `tencent/hy3-free`                  | 32K     | `General` | ~3.49s  |

### [Poixe AI](https://poixe.com)

Poixe AI is a unified API gateway aggregating models from OpenAI, Anthropic, Google, xAI, ByteDance, Alibaba, Moonshot, and more through a single OpenAI-compatible endpoint. The free tier offers 10,000 requests per day with 10 million daily tokens. Append `:free` to any model name to access the free tier; may be rate-limited depending on model. Poixe AI currently has 29 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ⚠️     | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 10,000 RPD / 10,000,000 TPD

🔗 **Base URL:** `https://api.poixe.com/v1`

✅ **Verified:** September 24, 2026
| Free Model                                | Context | Best For    | Latency |
| :---------------------------------------- | ------- | ----------- | ------- |
| `deepseek-chat:free`                      | 128K    | `General`   | ~1.5s   |
| `gemini-2.5-flash-lite:free`              | 1M      | `General`   | ~1.5s   |
| `gemini-2.5-flash:free`                   | 1M      | `General`   | ~1.5s   |
| `gpt-3.5-turbo:free`                      | 16K     | `General`   | ~1.5s   |
| `gpt-4.1-mini-2025-04-14:free`            | 1M      | `Code`      | ~1.6s   |
| `gpt-4.1-mini:free`                       | 1M      | `Code`      | ~1.6s   |
| `gpt-4.1-nano-2025-04-14:free`            | 1M      | `Code`      | ~0.9s   |
| `gpt-4.1-nano:free`                       | 1M      | `Code`      | ~1.6s   |
| `gpt-4o-2024-08-06:free`                  | 128K    | `General`   | ~1.5s   |
| `gpt-4o-mini-2024-07-18:free`             | 128K    | `General`   | ~0.9s   |
| `gpt-4o-mini:free`                        | 128K    | `General`   | ~0.9s   |
| `gpt-5-mini:free`                         | 400K    | `General`   | ~1.6s   |
| `gpt-5-nano-2025-08-07:free`              | 400K    | `General`   | ~1.6s   |
| `gpt-oss-120b:free`                       | 131K    | `General`   | ~1.3s   |
| `gpt-oss-20b:free`                        | 131K    | `Code`      | ~0.8s   |
| `grok-3-mini-beta:free`                   | 131K    | `Reasoning` | ~3.4s   |
| `grok-3-mini:free`                        | 131K    | `Reasoning` | ~3.4s   |
| `o3-mini-2025-01-31:free`                 | 200K    | `Reasoning` | ~4.0s   |
| `qwen-long-2025-01-25:free`               | 1M      | `General`   | ~1.5s   |
| `qwen-long-latest:free`                   | 1M      | `General`   | ~1.5s   |
| `qwen-plus-2025-04-28:free`               | 128K    | `General`   | ~1.3s   |
| `qwen-plus-latest:free`                   | 128K    | `General`   | ~1.3s   |
| `qwen-plus:free`                          | 128K    | `General`   | ~1.3s   |
| `qwen-turbo:free`                         | 1M      | `General`   | ~1.5s   |
| `qwen3-14b:free`                          | 128K    | `General`   | ~1.5s   |
| `qwen3-235b-a22b:free`                    | 262K    | `General`   | ~1.6s   |
| `qwen3-32b:free`                          | 128K    | `General`   | ~1.5s   |
| `qwen3-8b:free`                           | 128K    | `General`   | ~1.4s   |
| `qwen3-coder-480b-a35b-instruct:free`     | 256K    | `Code`      | ~1.2s   |

### [Pooled AI](https://ai.pooled.dev)

Pooled AI is a lightweight inference hub offering official MiniMax models through an OpenAI-compatible endpoint. The free tier provides 1M TPD with access to MiniMax M2.5, M2.7, and M3 official variants -- solid for general tasks and reasoning with generous daily tokens. Pooled AI currently has 3 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 1M TPD / MiniMax models only

🔗 **Base URL:** `https://ai.pooled.dev/v1`

✅ **Verified:** September 24, 2026
| Free Model                | Context | Best For    | Latency |
| :------------------------ | ------- | ----------- | ------- |
| `MiniMax-M2.5-Official`   | 200K    | `General`   | ~2.58s  |
| `MiniMax-M2.7-Official`   | 200K    | `General`   | ~2.37s  |
| `MiniMax-M3-Official`     | 1M      | `General`   | ~1.55s  |

### [Poolside](https://poolside.ai)

Poolside is a foundation model lab building purpose-built coding models from scratch. Laguna S and XS models are trained on 30T tokens exclusively for agentic software engineering with tool calling and 256K context. The models are free while in preview -- the same "use it while it lasts" uncertainty as any free provider. Poolside currently has 2 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ⚠️     | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / 200 RPD / 150,000 TPM / 1,000,000 TPD

🔗 **Base URL:** `https://inference.poolside.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model               | Context | Best For | Latency |
| :----------------------- | ------- | -------- | ------- |
| `poolside/laguna-s-2.1`  | 256K    | `Code`   | ~1.3s   |
| `poolside/laguna-xs-2.1` | 128K    | `Code`   | ~0.9s   |

### [Routeway AI](https://routeway.ai)

Routeway is a unified API gateway offering free models through a `:free` model suffix -- a pattern shared with OpenRouter and Kilo Code. Models are drawn from Stepfun, NVIDIA, Poolside, Meta, and others, all accessed through a single OpenAI-compatible endpoint. The tight 5 RPM cap makes Routeway a fallback hub rather than a daily driver. Routeway currently has 7 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ⚠️     | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 5 RPM / 200 RPD / 300,000 TPD

🔗 **Base URL:** `https://api.routeway.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                          | Context | Best For    | Latency |
| :---------------------------------- | ------- | ----------- | ------- |
| `gemma-4-26b-a4b-it-chimerax:free`  | 32K     | `General`   | ~1.5s   |
| `gemma-4-26b-a4b-it-darksoul:free`  | 32K     | `General`   | ~1.5s   |
| `gemma-4-26b-a4b-it-luminous:free`  | 32K     | `General`   | ~1.5s   |
| `gemma-4-26b-a4b-it-meromero:free`  | 32K     | `General`   | ~1.5s   |
| `gemma-4-26b-a4b-it-moonlight:free` | 32K     | `General`   | ~1.5s   |
| `gemma-4-26b-a4b-it-musica:free`    | 32K     | `General`   | ~1.5s   |
| `muse-glimmer-30b:free`             | 131K    | `General`   | ~2.96s  |

### [SEA-LION](https://playground.sea-lion.ai)

SEA-LION is a family of Southeast Asian language models by AI Singapore, offering open models via an OpenAI-compatible API. The free tier provides 10 RPM. SEA-LION currently has 5 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPM

🔗 **Base URL:** `https://api.sea-lion.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                                     | Context | Best For  | Latency |
| :--------------------------------------------- | ------- | --------- | ------- |
| `aisingapore/Gemma-SEA-LION-v4-27B-IT`         | 131K    | `General` | ~1.64s  |
| `aisingapore/Llama-SEA-LION-v3-70B-IT`         | 128K    | `General` | ~1.55s  |
| `aisingapore/Qwen-SEA-LION-v4-32B-IT`          | 128K    | `General` | ~1.69s  |
| `aisingapore/Qwen-SEA-LION-v4.5-27B-IT`        | 128K    | `General` | ~1.68s  |
| `aisingapore/Nemotron-SEA-LION-v4.8-120B-A12B` | 1M      | `General` | ~1.63s  |

### [TokenReply](https://tokenreply.com)

TokenReply is a lightweight inference hub offering models from Google, DeepSeek, OpenAI, Qwen, Moonshot, Stepfun, Zhipu, and more through an OpenAI-compatible endpoint. The free tier provides 3 RPM for its free models, but given its latencies, it's more of a tight cap suited for general conversations and light coding. TokenReply currently has 36 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ⚠️     | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 3 RPM / Free Models Only

🔗 **Base URL:** `https://api.tokenreply.com/v1`

✅ **Verified:** September 24, 2026
| Free Model                                   | Context | Best For    | Latency |
| :------------------------------------------- | ------- | ----------- | ------- |
| `dots-3-note-preview`                        | 32K     | `General`   | ~1.63s  |
| `gemini-3.7-flash-default-free`              | 1M      | `General`   | ~2.73s  |
| `google/diffusiongemma-26b-a4b-it`           | 32K     | `General`   | ~2.04s  |
| `google/gemma-4-26b-a4b-it`                  | 32K     | `General`   | ~2.07s  |
| `grok-4.20-0309-non-reasoning`               | 131K    | `General`   | ~11.25s |
| `grok-4.20-0309-reasoning`                   | 256K    | `Reasoning` | ~18.52s |
| `grok-4.20-fast`                             | 256K    | `General`   | ~7.9s   |
| `grok-4.20-multi-agent-0309`                 | 256K    | `General`   | ~19.09s |
| `grok-4.20-multi-agent-high`                 | 256K    | `General`   | ~13.82s |
| `grok-4.20-multi-agent-low`                  | 256K    | `General`   | ~16.57s |
| `grok-4.20-multi-agent-medium`               | 256K    | `General`   | ~7.95s  |
| `grok-4.20-multi-agent-xhigh`                | 256K    | `General`   | ~21.83s |
| `grok-4.3`                                   | 256K    | `General`   | ~9.01s  |
| `grok-4.3-high`                              | 256K    | `General`   | ~6.39s  |
| `grok-4.3-low`                               | 256K    | `General`   | ~9.05s  |
| `grok-4.3-medium`                            | 256K    | `General`   | ~7.61s  |
| `grok-build-0.1`                             | 131K    | `General`   | ~17.92s |
| `laguna-s-2.1`                               | 256K    | `Code`      | ~1.85s  |
| `laguna-xs-2.1`                              | 128K    | `Code`      | ~1.17s  |
| `lfm-2.5-2.6b`                               | 32K     | `General`   | ~1.2s   |
| `ling-3.0-flash-fin-free`                    | 262K    | `General`   | ~1.78s  |
| `meta/llama-3.2-11b-vision-instruct`         | 128K    | `Vision`    | ~9.09s  |
| `meta/muse-glimmer-30b`                      | 131K    | `General`   | ~4.27s  |
| `nemotron-3-nano-omni-30b-a3b-reasoning`     | 1M      | `Reasoning` | ~2.09s  |
| `nemotron-3-ultra-free`                      | 1M      | `General`   | ~24.91s |
| `nemotron-3-ultra-thinking-free`             | 1M      | `Reasoning` | ~22.03s |
| `nemotron-3.5-lightning-30b-a3b`             | 262K    | `General`   | ~1.75s  |
| `nemotron-3.5-lightning-free`                | 262K    | `General`   | ~4.0s   |
| `nemotron-3.5-lightning-thinking-free`       | 262K    | `Reasoning` | ~2.56s  |
| `north-mini-code`                            | 128K    | `Code`      | ~0.93s  |
| `nvidia/ising-calibration-1.5-31b`           | 32K     | `General`   | ~8.09s  |
| `nvidia/nemotron-3-nano-30b-a3b`             | 1M      | `General`   | ~0.96s  |
| `nvidia/nemotron-3-super-120b-a12b`          | 1M      | `Reasoning` | ~1.07s  |
| `nvidia/nemotron-3-ultra-550b-a55b`          | 1M      | `General`   | ~14.78s |
| `openai/gpt-oss-120b`                        | 128K    | `General`   | ~1.7s   |
| `openai/gpt-oss-20b`                         | 128K    | `Code`      | ~0.98s  |

### [Void AI](https://voidai.app)

Void AI is an inference hub offering models from OpenAI, Google, DeepSeek, Qwen, Moonshot, Zhipu, and more through an OpenAI-compatible endpoint. The free tier provides 100 RPM with 125,000 daily credits -- Sustained for light coding. Void AI currently has 35 verified coding-relevant models.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 100 RPM / 125,000 Daily Credits

🔗 **Base URL:** `https://api.voidai.app/v1`

✅ **Verified:** September 24, 2026
| Free Model                       | Context | Best For    | Latency |
| :------------------------------- | ------- | ----------- | ------- |
| `deepseek-v3.2`                  | 128K    | `Reasoning` | ~2.0s   |
| `deepseek-v4-flash`              | 128K    | `Reasoning` | ~1.5s   |
| `deepseek-v4-flash-0731`         | 128K    | `Reasoning` | ~1.5s   |
| `deepseek-v4-pro`                | 128K    | `Reasoning` | ~1.6s   |
| `deepseek-v4-pro-0813`           | 128K    | `Reasoning` | ~1.6s   |
| `gemini-2.5-flash`               | 1M      | `General`   | ~1.5s   |
| `gemini-2.5-pro`                 | 1M      | `General`   | ~1.5s   |
| `gemini-3-flash-preview`         | 1M      | `General`   | ~1.5s   |
| `gemini-3.1-flash-lite`          | 1M      | `General`   | ~0.7s   |
| `gemini-3.1-pro-preview`         | 1M      | `Reasoning` | ~1.5s   |
| `gemini-3.5-flash-lite`          | 1M      | `General`   | ~1.5s   |
| `gemini-3.5-flash`               | 1M      | `Code`      | ~1.7s   |
| `gemini-3.6-flash`               | 1M      | `Code`      | ~1.8s   |
| `gemini-3.7-flash`               | 1M      | `General`   | ~1.7s   |
| `gemini-3.8-flash`               | 1M      | `General`   | ~1.8s   |
| `glm-5.2`                        | 128K    | `General`   | ~2.0s   |
| `glm-5.3`                        | 128K    | `General`   | ~2.0s   |
| `glm-5.3-flash`                  | 128K    | `General`   | ~1.5s   |
| `gpt-4.1`                        | 1M      | `General`   | ~1.7s   |
| `gpt-4.1-mini`                   | 1M      | `General`   | ~1.7s   |
| `gpt-4o`                         | 128K    | `General`   | ~1.7s   |
| `gpt-4o-mini`                    | 128K    | `General`   | ~1.7s   |
| `gpt-5.1`                        | 400K    | `General`   | ~1.7s   |
| `gpt-5.2`                        | 400K    | `General`   | ~1.7s   |
| `gpt-5.3-codex`                  | 400K    | `Code`      | ~1.7s   |
| `gpt-5.4`                        | 400K    | `General`   | ~1.7s   |
| `gpt-5.4-mini`                   | 400K    | `General`   | ~1.7s   |
| `gpt-oss-120b`                   | 131K    | `General`   | ~1.7s   |
| `gpt-oss-20b`                    | 131K    | `Code`      | ~1.5s   |
| `kimi-k2.6`                      | 128K    | `Reasoning` | ~0.8s   |
| `kimi-k2.7-code`                 | 128K    | `Code`      | ~1.5s   |
| `kimi-k3`                        | 128K    | `Reasoning` | ~1.5s   |
| `qwen3-235b-a22b-instruct`       | 256K    | `Reasoning` | ~1.7s   |
| `qwen3-coder-480b-a35b-instruct` | 256K    | `Code`      | ~3.0s   |
| `qwen3.8-2.4t-a95b`              | 262K    | `Reasoning` | ~1.7s   |

### [xKiro AI](https://xkiro.com)

xKiro AI is an API gateway offering free models from DeepSeek, Qwen, Mistral, MiniMax and more via an OpenAI-compatible API. The free tier offers 5M TPD for free models. xKiro AI currently has 37 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 5M TPD / Free models only

🔗 **Base URL:** `https://api.xkiro.com/v1`

✅ **Verified:** September 24, 2026
| Free Model                              | Context | Best For    | Latency   |
| :-------------------------------------- | ------- | ----------- | --------- |
| `mistralai/codestral-2508`              | 256K    | `Code`      | ~0.64s    |
| `mistralai/devstral-medium`             | 128K    | `Code`      | ~0.57s    |
| `mistralai/ministral-14b`               | 128K    | `General`   | ~0.69s    |
| `mistralai/ministral-3b`                | 128K    | `General`   | ~0.59s    |
| `mistralai/ministral-8b`                | 128K    | `General`   | ~0.66s    |
| `mistralai/mistral-large-2512`          | 262K    | `Reasoning` | ~0.72s    |
| `mistralai/mistral-medium-3.5`          | 32K     | `General`   | ~0.67s    |
| `mistralai/mistral-small-2603`          | 32K     | `General`   | ~1.69s    |
| `minimax/minimax-m2:free`               | 200K    | `General`   | ~1.14s    |
| `minimax/minimax-m2.1:free`             | 200K    | `General`   | ~1.54s    |
| `minimax/minimax-m2.1-highspeed:free`   | 200K    | `General`   | ~1.83s    |
| `minimax/minimax-m2.5:free`             | 200K    | `General`   | ~1.57s    |
| `minimax/minimax-m2.5-highspeed:free`   | 200K    | `General`   | ~2.05s    |
| `minimax/minimax-m2.7:free`             | 200K    | `General`   | ~1.1s     |
| `minimax/minimax-m2.7-highspeed:free`   | 200K    | `General`   | ~10.77s   |
| `minimax/minimax-m3:free`               | 200K    | `General`   | ~1.06s    |
| `qwen/qwen-plus-2025-07-28:free`        | 128K    | `General`   | ~3.04s    |
| `qwen/qwen3-omni-flash:free`            | 128K    | `Vision`    | ~2.63s    |
| `qwen/qwen3-coder-plus:free`            | 131K    | `Code`      | ~2.79s    |
| `qwen/qwen3-vl-plus:free`               | 128K    | `Vision`    | ~2.99s    |
| `qwen/qwen3-max:free`                   | 262K    | `General`   | ~6.7s     |
| `qwen/qwen3.5-397b-a17b:free`           | 128K    | `General`   | ~3.33s    |
| `qwen/qwen3.5-flash:free`               | 128K    | `General`   | ~3.03s    |
| `qwen/qwen3.5-omni-flash:free`          | 128K    | `Vision`    | ~2.45s    |
| `qwen/qwen3.5-omni-plus:free`           | 128K    | `Vision`    | ~2.83s    |
| `qwen/qwen3.5-plus:free`                | 256K    | `Reasoning` | ~2.89s    |
| `qwen/qwen3.6-27b:free`                 | 128K    | `General`   | ~3.17s    |
| `qwen/qwen3.6-35b-a3b:free`             | 262K    | `General`   | ~2.74s    |
| `qwen/qwen3.6-max-preview:free`         | 256K    | `General`   | ~3.18s    |
| `qwen/qwen3.6-plus:free`                | 256K    | `General`   | ~2.75s    |
| `qwen/qwen3.7-flash:free`               | 1M      | `General`   | ~2.71s    |
| `qwen/qwen3.7-max:free`                 | 262K    | `General`   | ~2.91s    |
| `qwen/qwen3.7-plus:free`                | 256K    | `General`   | ~2.92s    |
| `qwen/qwen3.8-max:free`                 | 262K    | `General`   | ~2.98s    |
| `qwen/qwen3.8-omni-flash:free`          | 128K    | `Vision`    | ~4.74s    |
| `sensenova/sensenova-6.7-flash-lite`    | 128K    | `General`   | ~1.02s    |
| `sensenova/sensenova-6.8-flash-lite`    | 128K    | `General`   | ~3.08s    |

### [Yolo-Auto](https://yolo-auto.com)

Yolo-Auto is a bare-metal inference provider running a single Qwen model through an OpenAI-compatible endpoint. The free tier offers 15 requests per day for integration testing -- enough to verify your tooling works before upgrading to the flat-rate unlimited plan. As they promised, more models are coming soon. Yolo-Auto currently has 2 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 15 RPD

🔗 **Base URL:** `https://yolo-auto.com/v1`

✅ **Verified:** September 24, 2026
| Free Model      | Context | Best For  | Latency |
| :-------------- | ------- | --------- | ------- |
| `qwen3.8-27b`   | 128K    | `General` | ~4.69s  |
| `qwen3.8-flash` | 1M      | `General` | ~3.16s  |

### [Zhipu AI](https://z.ai)

Zhipu AI is a Chinese AI company developing the GLM family of foundation models. The free tier offers two flash-variant models with a concurrency limit of 1 request at a time and unlimited daily tokens -- practical for lightweight scripting and quick edits, but the single-concurrent cap makes sustained coding sessions impractical. Zhipu AI currently has 2 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 1 Concurrent Request / Uncapped TPD

🔗 **Base URL:** `https://api.z.ai/api/paas/v4`

✅ **Verified:** September 24, 2026
| Free Model      | Context | Best For   | Latency |
| :-------------- | ------- | ---------- | ------- |
| `glm-4.7-flash` | 128K    | `General`  | ~2.4s   |
| `glm-4.5-flash` | 128K    | `Fallback` | ~0.7s   |

### [Zydit AI](https://zydit.in)

Zydit AI is an API gateway offering free models via an OpenAI-compatible API. The free tier provides unlimited requests at 10 RPM for free models (v3 endpoints). Zydit AI currently has 7 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** Unlimited Requests / 10 RPM / Free models only (For v3 endpoints)

🔗 **Base URL:** `https://api.zydit.in/v3`

✅ **Verified:** September 24, 2026
| Free Model                           | Context | Best For    | Latency |
| :----------------------------------- | ------- | ----------- | ------- |
| `big-pickle`                         | 200K    | `General`   | ~12.23s |
| `deepseek-r1:latest`                 | 128K    | `Reasoning` | ~9.92s  |
| `dolphin3:latest`                    | 128K    | `General`   | ~13.21s |
| `gemma4-31b-it-pro`                  | 32K     | `General`   | ~5.3s   |
| `mimo-v2.5`                          | 1M      | `General`   | ~7.72s  |
| `muse-spark-1.3`                     | 1M      | `General`   | ~15.18s |
| `nemotron-3-ultra-max`               | 262K    | `General`   | ~9.61s  |

### [Zylo API](https://zyloai.net)

Zylo API is a unified inference hub providing access to models from DeepSeek, NVIDIA, Mistral, MiniMax, Qwen, GLM, and Google through an OpenAI-compatible endpoint. The free tier offers 10 RPM with 7,200 requests and 200,000 tokens per day -- which is sustained for light coding or general use cases. Zylo API currently has 6 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPM / 7,200 RPD / 200,000 TPD

🔗 **Base URL:** `https://api.zyloai.net/v1`

✅ **Verified:** September 24, 2026
| Free Model                | Context | Best For  | Latency |
| :------------------------ | ------- | --------- | ------- |
| `gpt-oss-20b`             | 131K    | `Code`    | ~0.9s   |
| `gemma-4`                 | 32K     | `General` | ~1.7s   |
| `laguna-xs-2.1`           | 128K    | `Code`    | ~1.9s   |
| `muse-glimmer-30b`        | 131K    | `General` | ~1.3s   |
| `nemotron-3.5-lightning`  | 262K    | `General` | ~1.6s   |
| `nemotron-3-ultra`        | 1M      | `General` | ~1.1s   |

---

## Non-Replenishable Providers

Providers with no replenishing cycle -- use their free models as much as you want; the cost never rises above **$0**.

Filtered for coding and general chat capability across 9 Non-Replenishable providers.

<strong>Jump to a provider or hub:</strong>

<ul>
  <li><a href="#agnes-ai">Agnes AI</a></li>
  <li><a href="#auriko">Auriko</a></li>
  <li><a href="#bazaarlink">BazaarLink</a></li>
  <li><a href="#fastrouter">FastRouter</a></li>
  <li><a href="#odirouter">Odirouter</a></li>
  <li><a href="#openrouter">OpenRouter</a></li>
  <li><a href="#requesty">Requesty</a></li>
  <li><a href="#tokeness">Tokeness</a></li>
  <li><a href="#vsllm">VSLLM</a></li>
</ul>

### [Agnes AI](https://www.agnes-ai.com)

Agnes AI offers flash-tier and pro-tier models with generous daily limits and responsive sub-2s latencies. The free tier provides 1,000 requests per day at 20 RPM -- enough volume for background jobs and light interactive coding. Agnes AI currently has 3 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 20 RPM / 1,000 RPD

🔗 **Base URL:** `https://apihub.agnes-ai.com/v1`

✅ **Verified:** September 24, 2026
| Free Model            | Context | Best For    | Latency |
| :-------------------- | ------- | ----------- | ------- |
| `agnes-2.0-flash`     | 512K    | `General`   | ~0.65s  |
| `agnes-2.5-flash`     | 512K    | `Fallback`  | ~0.7s   |
| `agnes-3.0-flash`     | 512K    | `General`   | ~0.69s  |

### [Auriko](https://www.auriko.ai)

Auriko is a unified API gateway providing access to 100+ models from top providers through a single OpenAI-compatible endpoint. The free tier offers 1,000 Platform RPM and 500 BYOK RPM with a 1M token monthly cap -- but most models run on a credit system ($1 usage), not truly free. Only 3 models are genuinely free and replenishable without credits. Auriko currently has 3 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 500 RPM (BYOK) / 1,000 RPM (Platform) / 1,000,000 tokens/month (BYOK) / Has Permanently Free models

🔗 **Base URL:** `https://api.auriko.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model       | Context | Best For  | Latency |
| :--------------- | ------- | --------- | ------- |
| `glm-4.5-flash`  | 200K    | `General` | ~2.8s   |
| `glm-4.6v-flash` | 128K    | `General` | ~3.0s   |
| `glm-4.7-flash`  | 200K    | `General` | ~2.8s   |

### [BazaarLink](https://bazaarlink.ai)

BazaarLink is a lightweight inference gateway offering free models via an OpenAI-compatible API using a `:free` suffix. The free tier provides 10 RPM with 50 requests per day. BazaarLink currently has 3 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPM / 50 RPD / Free Models only

🔗 **Base URL:** `https://api.bazaarlink.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                                 | Context | Best For    | Latency |
| :----------------------------------------- | ------- | ----------- | ------- |
| `auto:free`                                | Varies  | `General`   | ~2.56s  |
| `deepseek/deepseek-v4-flash-0731free:free` | 128K    | `Reasoning` | ~2.0s   |
| `qwen/qwen3.7-flash:free`                  | 1M      | `General`   | ~3.23s  |

### [FastRouter](https://fastrouter.ai)

FastRouter is a lightweight inference hub offering models with a `:free` suffix through an OpenAI-compatible endpoint. The free tier provides 10 requests per day per model with no billing credits required -- a tight cap suited for occasional queries and model evaluation. FastRouter currently has 6 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPD per model / No Billing Credits Required

🔗 **Base URL:** `https://api.fastrouter.ai/api/v1`

✅ **Verified:** September 24, 2026
| Free Model                         | Context | Best For  | Latency |
| :--------------------------------- | ------- | --------- | ------- |
| `google/gemma4-26b:free`           | 256K    | `General` | ~0.97s  |
| `nvidia/nemotron-3-nano-30b:free`  | 1M      | `General` | ~1.02s  |
| `nvidia/nemotron-3-super:free`     | 256K    | `General` | ~2.79s  |
| `openai/gpt-oss-120b:free`         | 131K    | `General` | ~0.92s  |
| `openai/gpt-oss-20b:free`          | 131K    | `Code`    | ~1.06s  |
| `sarvam/sarvam-105b:free`          | 128K    | `General` | ~1.34s  |

### [Odirouter](https://odirouter.ai)

Odirouter is an API router in Russia, providing a pool of free-tier models from Anthropic, Google, Qwen, MiniMax, and OpenAI through an OpenAI-compatible endpoint. Models are exposed with a `free-` prefix -- which provides about 100 Requests/day. Odirouter currently has 12 models verified.

| Capability | Tool Calls | Schema | Error Handling  | Rate Limit Safe |
| :--------- | :--------- | :----- | :-------------- | :-------------- |
| **Status** | ✅          | ✅      | ⚠️              | ⚠️              |

🎁 **Free Tier Quota:** 5 RPM / 50 RPD / Free Models Only / 2 Parallel Multimodal Queries

🔗 **Base URL:** `https://api.odirouter.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                       | Context | Best For    | Latency |
| :------------------------------- | ------- | ----------- | ------- |
| `free-claude-haiku-4-5-20251001` | 200K    | `Code`      | ~2.46s  |
| `free-claude-haiku-4.5`          | 200K    | `Code`      | ~2.21s  |
| `free-gemini-2.5-flash`          | 1M      | `General`   | ~1.8s   |
| `free-gemini-2.5-pro`            | 1M      | `Reasoning` | ~4.4s   |
| `free-gemini-3-flash-preview`    | 1M      | `General`   | ~12.54s |
| `free-gemini-3.1-flash-lite`     | 1M      | `General`   | ~6.83s  |
| `free-gpt-5.4-mini`              | 400K    | `General`   | ~1.71s  |
| `free-minimax-m2.5`              | 200K    | `Reasoning` | ~1.71s  |
| `free-minimax-m2.7`              | 200K    | `Reasoning` | ~4.0s   |
| `free-qwen3.5-flash`             | 128K    | `General`   | ~2.59s  |
| `free-qwen3.5-plus`              | 256K    | `Reasoning` | ~2.07s  |
| `free-vclaude-haiku-4.5`         | 200K    | `Code`      | ~7.6s   |

### [OpenRouter](https://openrouter.ai)

OpenRouter is a unified API gateway providing access to hundreds of models from dozens of providers through a single endpoint. The free tier offers rate-limited access to community-hosted models (marked with `:free`) that changes often. A great backup when other providers are rate-limited. OpenRouter currently has 15 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / 50 RPD

🔗 **Base URL:** `https://openrouter.ai/api/v1`

✅ **Verified:** September 24, 2026
| Free Model                                           | Context | Best For    | Latency |
| :--------------------------------------------------- | ------- | ----------- | ------- |
| `cohere/north-mini-code:free`                        | 128K    | `Code`      | ~2.1s   |
| `dots-studio/dots-3-note-preview:free`               | 32K     | `General`   | ~1.7s   |
| `google/gemma-4-26b-a4b-it:free`                     | 32K     | `General`   | ~1.5s   |
| `google/gemma-4-31b-it:free`                         | 32K     | `General`   | ~1.5s   |
| `inclusionai/ling-3.0-flash-fin:free`                | 262K    | `General`   | ~1.5s   |
| `inclusionai/ling-3.0-flash-sante:free`              | 262K    | `General`   | ~1.5s   |
| `inclusionai/ling-3.0-flash-vl:free`                 | 262K    | `Vision`    | ~1.5s   |
| `liquid/lfm-2.5-2.6b:free`                           | 65K     | `General`   | ~1.6s   |
| `nex-agi/nex-n2.5-mini:free`                         | 32K     | `General`   | ~1.5s   |
| `nex-agi/nex-n2.5-pro:free`                          | 32K     | `General`   | ~1.5s   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 1M      | `Reasoning` | ~0.7s   |
| `nvidia/nemotron-3-super-120b-a12b:free`             | 1M      | `General`   | ~2.7s   |
| `nvidia/nemotron-3-ultra-550b-a55b:free`             | 1M      | `General`   | ~14.78s |
| `poolside/laguna-s-2.1:free`                         | 262K    | `Code`      | ~1.3s   |
| `poolside/laguna-xs-2.1:free`                        | 128K    | `Code`      | ~1.9s   |

### [Requesty](https://requesty.ai)

Requesty is an API router providing access to free models via an OpenAI-compatible API. The free tier offers 200 RPD for free models. Requesty currently has 5 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 200 RPD / Free Models only

🔗 **Base URL:** `https://router.requesty.ai/v1`

✅ **Verified:** September 24, 2026
| Free Model                                      | Context | Best For    | Latency |
| :---------------------------------------------- | ------- | ----------- | ------- |
| `google/gemma-4-31b-it`                         | 32K     | `General`   | ~1.84s  |
| `mistral/leanstral-1-5`                         | 128K    | `Code`      | ~0.99s  |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | 1M      | `Reasoning` | ~2.3s   |
| `nvidia/nemotron-3-super-120b-a12b`             | 1M      | `General`   | ~1.21s  |
| `nvidia/nemotron-3-ultra-550b-a55b`             | 1M      | `General`   | ~1.12s  |

### [Tokeness](https://tokeness.ai)

Tokeness is an auto-routing inference gateway serving a single free auto model via an OpenAI-compatible endpoint. Because it auto-routes, context windows vary per request. Tokeness currently has 1 model verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ⚠️              |

🎁 **Free Tier Quota:** Unspecified Rate Limits / Free models only

🔗 **Base URL:** `https://n.tokeness.dev/v1`

✅ **Verified:** September 24, 2026
| Free Model      | Context | Best For  | Latency |
| :-------------- | :------ | :-------- | ------- |
| `tokeness/free` | Varies  | `General` | ~5.94s  |

### [VSLLM](https://vsllm.cc)

VSLLM is a Chinese-based API gateway offering free GLM models via an OpenAI-compatible endpoint. The free tier provides access to free-tagged models only. VSLLM currently has 2 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** Unspecified Rate Limits / Free Models only

🔗 **Base URL:** `https://vsllm.cc/v1`

✅ **Verified:** September 24, 2026
| Free Model            | Context | Best For  | Latency |
| :-------------------- | :------ | :-------- | :------ |
| `glm-4.6v-flash-free` | 128K    | `Vision`  | ~2.33s  |
| `glm-4.7-flash-free`  | 200K    | `General` | ~1.5s   |

---

## Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details.

[^1]: Models are verified through live API calls. `scripts/verify.py` discovers free models via the provider's `/v1/models` endpoint (or provider-specific listing), tests every discovered free model once with the prompt `State the word 'READY'.` (retries on 429/5xx with backoff), and records latency to first token. To reproduce: copy `scripts/.env.example` to `scripts/.env`, set `API_KEY` and `BASE_URL` (plus `ACCOUNT_ID` for Cloudflare), and run `python scripts/verify.py` -- it writes `scripts/verified_models_YYYY-MM-DD.txt`. A model is removed if its free tier is paywalled, deprecated, or stops replenishing.

