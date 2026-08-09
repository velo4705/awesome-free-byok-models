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

By using a **Bring Your Own Key (BYOK)** approach, you can plug your free API keys into **coding tools**, **custom projects**, or **AI-powered apps** — no credit card required. Every model listed here is rated for coding capability, but most work just as well for general conversation.

> 💡 **Pro tip:** Free tiers can change. If a model hits rate limits, switch to another — there's always a backup in this list.

> 📝 **Note:** Always verify current quotas on the provider's console before building workflows.

**Scope:** Text-generation LLM API models with a *currently available, self-replenishing free tier* — no credit card required at signup, the quota resets without manual top-up, and the endpoint is accessible via a standard API call (OpenAI-compatible or provider-native). This excludes image generation models, models behind a paywall after a trial, services requiring phone/PII verification, reverse-engineered access to gated models, and Chinese mainland gateways.

**Removal policy:** A model or provider is removed when (a) the free tier is paywalled or discontinued, (b) the endpoint is deprecated with no free replacement, (c) the provider adds mandatory phone/PII verification, or (d) daily/monthly credits no longer replenish automatically.

**Data sources:** Quota, context size, and latency figures are drawn from provider documentation and live API verification via `scripts/verify.py`[^1]. Latency is measured from request to first token under typical network conditions and will vary. Providers are marked with a verification date showing when their free tier was last confirmed working.

**Use responsibly.** This list is for developers — not for scraping, reselling, or bulk harvesting. Respect each provider's rate limits and terms of service.

## Contents

- [The Best API Providers](#the-best-api-providers)
- [Top Free Models](#top-free-models)
- [Provider Showcases](#provider-showcases)

## The Best API Providers

If you are signing up for free accounts to get API keys, these are the **top platforms** to look at first.

| Provider                                                   | Profile     | Why It Matters For You                                                                                                  |
| :--------------------------------------------------------- | :---------- | :---------------------------------------------------------------------------------------------------------------------- |
| **[OpenCode Zen](https://opencode.ai/docs/zen)**           | Reasoning   | 30 RPM with 500 daily requests and 1M token pool. DeepSeek-v4-flash-free handles multi-turn without losing the thread.  |
| **[Groq API](https://console.groq.com/docs/quickstart)**   | Low Latency | Sub-300ms at 14,400 RPD with 18k TPM for rapid-fire edits. Highest throughput on the list.                              |
| **[Void AI](https://docs.voidai.app/quickstart)**          | High RPM    | 100 RPM with 125K daily credits — highest RPM of any hub. 20 verified coding-relevant models across multiple providers. |

---

## Top Free Models

Ranked by **coding capability × daily volume × speed** using quantitative criteria derived from provider documentation and [`scripts/verify.py`](scripts/verify.py):

| Rank   | Model                          | Host Provider                                                 | Why It Ranks Here                                                   |
| ---    | ---                            | ---                                                           | ---                                                                 |
| **1**  | `deepseek-v4-flash-free`       | [OpenCode Zen](https://opencode.ai/docs)                      | 500 RPD, 30 RPM, 200K context, DeepSeek V4 Flash reasoning model.   |
| **2**  | `qwen/qwen3.6-27b`             | [Groq API](https://console.groq.com/docs/models)              | 256K context, sub-300ms latency, 14,400 RPD daily pool.             |
| **3**  | `openai/gpt-oss-120b`          | [Groq API](https://console.groq.com/docs/overview)            | 128K context, sub-300ms latency, 14,400 RPD, 120B params.           |
| **4**  | `gpt-5.3-codex`                | [Void AI](https://docs.voidai.app)                            | 128K context, ~1.5s latency, code-specialized model, 100 RPM.       |
| **5**  | `mimo-v2.5-free`               | [OpenCode Zen](https://opencode.ai/docs/models)               | 128K context, ~6.5s latency, vision + code, 500 RPD.                |
| **6**  | `intern-s2-preview`            | [Intern AI](https://internlm.intern-ai.org.cn/api)            | 256K context, ~1.0s latency, 90M tokens/month quota.                |
| **7**  | `models/gemini-3.5-flash-lite` | [Google Gemini](https://ai.google.dev/gemini-api/docs/models) | 1M context, ~1.5s latency, 500 RPD, general-purpose model.          |
| **8**  | `deepseek-v3.2`                | [MNN AI](https://mnnai.ru/docs)                               | 128K context, ~2.0s latency, $1/month auto-replenishing credits.    |
| **9**  | `mistral-code-agent-latest`    | [Mistral AI](https://docs.mistral.ai)                         | 128K context, sub-1s latency, agentic tool-calling, 50K TPM.        |
| **10** | `deepseek-v4-pro`              | [Void AI](https://docs.voidai.app/guides/credits)             | 128K context, ~1.6s latency, higher throughput than Flash, 100 RPM. |

---

## Provider Showcases

Filtered for coding and general chat capability across all providers.

<strong>Jump to a provider or hub:</strong>

<ul>
  <li><a href="#aion-labs">AION Labs</a></li>
  <li><a href="#agnes-ai">Agnes AI</a></li>
  <li><a href="#anyapi-ai">AnyAPI AI</a></li>
  <li><a href="#auriko">Auriko</a></li>
  <li><a href="#cerebras-ai">Cerebras AI</a></li>
  <li><a href="#cloudflare-workers-ai">Cloudflare Workers AI</a></li>
  <li><a href="#cohere-ai">Cohere AI</a></li>
  <li><a href="#electronhub">ElectronHub</a></li>
  <li><a href="#fastrouter">FastRouter</a></li>
  <li><a href="#freeinference">FreeInference</a></li>
  <li><a href="#google-gemini">Google Gemini</a></li>
  <li><a href="#gonka-broker">Gonka Broker</a></li>
  <li><a href="#groq-api">Groq API</a></li>
  <li><a href="#helixmind">HelixMind</a></li>
  <li><a href="#helyxai">HelyxAI</a></li>
  <li><a href="#hugging-face-inference-api">Hugging Face Inference API</a></li>
  <li><a href="#intern-ai">Intern AI</a></li>
  <li><a href="#kilo-code">Kilo Code</a></li>
  <li><a href="#llmkiwi">LLM.Kiwi</a></li>
  <li><a href="#llm7io">LLM7.IO</a></li>
  <li><a href="#llmgateway">LLMGateway</a></li>
  <li><a href="#literouter">LiteRouter</a></li>
  <li><a href="#mnn-ai">MNN AI</a></li>
  <li><a href="#meganova-ai">MegaNova AI</a></li>
  <li><a href="#mistral-ai">Mistral AI</a></li>
  <li><a href="#mixlayer">Mixlayer</a></li>
  <li><a href="#naga-ai">Naga AI</a></li>
  <li><a href="#navy-api">Navy API</a></li>
  <li><a href="#nvidia-nim">NVIDIA NIM</a></li>
  <li><a href="#ollama-cloud">Ollama Cloud</a></li>
  <li><a href="#opencode-zen">OpenCode Zen</a></li>
  <li><a href="#openrouter">OpenRouter</a></li>
  <li><a href="#poixe-ai">Poixe AI</a></li>
  <li><a href="#poolside">Poolside</a></li>
  <li><a href="#routeway-ai">Routeway AI</a></li>
  <li><a href="#sambanova-ai">SambaNova AI</a></li>
  <li><a href="#speka-ai">Speka AI</a></li>
  <li><a href="#tokenreply">TokenReply</a></li>
  <li><a href="#void-ai">Void AI</a></li>
  <li><a href="#yolo-auto">Yolo-Auto</a></li>
  <li><a href="#zai-zhipu-ai">Z.AI (Zhipu AI)</a></li>
  <li><a href="#zylo-api">Zylo API</a></li>
</ul>

### [AION Labs](https://www.aionlabs.ai)

AION Labs provides storytelling-optimized models through an OpenAI-compatible API. The free tier offers 20,000 tokens/day and 15 RPM with no credit card required — a solid option if you need a daily token allowance for lightweight coding and creative tasks. AION Labs currently has 5 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ⚠️             | ✅               |

🎁 **Free Tier Quota:** 15 RPM / 20,000 TPD

🔗 **Base URL:** `https://api.aionlabs.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model                       | Context | Best For   | Latency |
| :------------------------------- | ------- | ---------- | ------- |
| `aion-labs/aion-3.0`             | 128K    | `Code`     | ~2.2s   |
| `aion-labs/aion-2.5`             | 128K    | `Code`     | ~2.3s   |
| `aion-labs/aion-3.0-mini`        | 128K    | `General`  | ~2.1s   |
| `aion-labs/aion-2.0`             | 128K    | `General`  | ~2.3s   |
| `aion-labs/aion-rp-llama-3.1-8b` | 32K     | `Fallback` | ~7.3s   |

### [Agnes AI](https://www.agnes-ai.com)

Agnes AI offers flash-tier models with generous daily limits but slow inference speed. The free tier provides 1,000 requests per day at 20 RPM — enough volume for background jobs, but ~7s latency makes interactive use frustrating. No credit card required. Agnes AI currently has 4 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 20 RPM / 1,000 RPD

🔗 **Base URL:** `https://apihub.agnes-ai.com/v1`

✅ **Verified:** August 9, 2026
| Free Model            | Context | Best For   | Latency |
| :-------------------- | ------- | ---------- | ------- |
| `agnes-2.0-flash`     | 32K     | `General`  | ~6.7s   |
| `agnes-2.5-flash`     | 32K     | `Fallback` | ~6.8s   |
| `agnes-2.5-pro`       | 32K     | `General`  | ~7.2s   |
| `agnes-2.5-pro-alpha` | 32K     | `General`  | ~8.7s   |

### [AnyAPI AI](https://anyapi.ai)

AnyAPI is a unified API gateway providing access to 400+ models from OpenAI, Anthropic, Google, DeepSeek, Meta, Mistral, Cohere, and more through a single OpenAI-compatible endpoint. The free tier offers 100,000 tokens/day with access to free and basic models — no credit card required. AnyAPI currently has 6 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 100,000 tokens/day / No Credit Card

🔗 **Base URL:** `https://api.anyapi.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model                                           | Context | Best For    | Latency |
| :--------------------------------------------------- | ------- | ----------- | ------- |
| `google/gemma-4-26b-a4b-it:free`                     | 32K     | `General`   | ~6.6s   |
| `nvidia/nemotron-3-nano-30b-a3b:free`                | 128K    | `General`   | ~9.3s   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 128K    | `Reasoning` | ~8.8s   |
| `nvidia/nemotron-3-ultra-550b-a55b:free`             | 128K    | `Reasoning` | ~9.1s   |
| `nvidia/nemotron-nano-12b-v2-vl:free`                | 32K     | `Vision`    | ~8.9s   |
| `nvidia/nemotron-nano-9b-v2:free`                    | 128K    | `Fallback`  | ~9.6s   |

### [Auriko](https://www.auriko.ai)

Auriko is a unified API gateway providing access to 100+ models from top providers through a single OpenAI-compatible endpoint. The free tier offers 1,000 Platform RPM and 500 BYOK RPM with a 1M token monthly cap — but most models run on a credit system ($1 usage), not truly free. Only 3 models are genuinely free and replenishable without credits. Auriko currently has 3 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 500 RPM (BYOK) / 1,000 RPM (Platform) / 1,000,000 tokens/month (BYOK)

🔗 **Base URL:** `https://api.auriko.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model       | Context | Best For  | Latency |
| :--------------- | ------- | --------- | ------- |
| `glm-4.5-flash`  | 128K    | `General` | ~2.8s   |
| `glm-4.6v-flash` | 128K    | `General` | ~3.0s   |
| `glm-4.7-flash`  | 128K    | `General` | ~2.8s   |

### [Cerebras AI](https://cloud.cerebras.ai)

Cerebras AI is defined by its **Wafer-Scale Engine (WSE) technology**, integrating memory, compute, and interconnects onto a single silicon wafer — solving the "memory wall" that throttles inference speed. The free tier offers replenishable credits with industry-leading throughput (2,500+ tokens/second). Cerebras AI currently has 3 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ❌               |

🎁 **Free Tier Quota:** 5 RPM / 250 RPD / 30,000 TPM

🔗 **Base URL:** `https://api.cerebras.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model     | Context | Best For  | Latency |
| :------------- | ------- | --------- | ------- |
| `gpt-oss-120b` | 128K    | `General` | ~0.5s   |
| `zai-glm-4.7`  | 128K    | `Agent`   | ~0.5s   |
| `gemma-4-31b`  | 32K     | `General` | ~0.5s   |

### [Cloudflare Workers AI](https://dash.cloudflare.com)

Cloudflare Workers AI runs models on Cloudflare's global edge network using serverless GPUs. The free tier offers 10,000 requests/day shared across all models with near-zero latency from edge locations worldwide. Cloudflare Workers AI currently has 22 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 150 to 1,500 RPM / 100,000 RPD / 13,000 TPD

🔗 **Base URL:** `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions` (replace `{account_id}` with your Cloudflare account ID)

✅ **Verified:** August 9, 2026
> ⚠️ **Two API paths:** The `/chat/completions` endpoint takes standard `"messages"` (OpenAI-compatible). The legacy `/run/{model}` endpoint uses `"prompt"` instead — make sure your tool targets the right one.

| Free Model                                     | Context | Best For    | Latency |
| :--------------------------------------------- | ------- | ----------- | ------- |
| `@cf/qwen/qwen2.5-coder-32b-instruct`          | 128K    | `Code`      | ~0.7s   |
| `@cf/aisingapore/gemma-sea-lion-v4-27b-it`     | 32K     | `General`   | ~0.5s   |
| `@cf/google/gemma-2b-it-lora`                  | 8K      | `Fallback`  | ~0.5s   |
| `@cf/google/gemma-4-26b-a4b-it`                | 32K     | `General`   | ~0.5s   |
| `@cf/meta/llama-3.2-1b-instruct`               | 128K    | `Fallback`  | ~0.6s   |
| `@cf/meta/llama-3.2-3b-instruct`               | 128K    | `Fallback`  | ~0.5s   |
| `@cf/meta/llama-3.3-70b-instruct-fp8-fast`     | 128K    | `Reasoning` | ~0.9s   |
| `@cf/meta/llama-4-scout-17b-16e-instruct`      | 256K    | `General`   | ~0.6s   |
| `@cf/mistral/mistral-7b-instruct-v0.2-lora`    | 8K      | `Fallback`  | ~0.7s   |
| `@cf/mistralai/mistral-small-3.1-24b-instruct` | 32K     | `General`   | ~0.8s   |
| `@cf/nvidia/nemotron-3-120b-a12b`              | 128K    | `Reasoning` | ~0.7s   |
| `@cf/openai/gpt-oss-120b`                      | 128K    | `Code`      | ~0.7s   |
| `@cf/openai/gpt-oss-20b`                       | 128K    | `General`   | ~0.6s   |
| `@cf/qwen/qwen3-30b-a3b-fp8`                   | 256K    | `General`   | ~0.9s   |
| `@cf/zai-org/glm-4.7-flash`                    | 128K    | `Agent`     | ~0.5s   |
| `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | 128K    | `Reasoning` | ~0.7s   |
| `@cf/google/gemma-7b-it-lora`                  | 8K      | `General`   | ~1.1s   |
| `@cf/ibm-granite/granite-4.0-h-micro`          | 128K    | `General`   | ~0.9s   |
| `@cf/meta-llama/llama-2-7b-chat-hf-lora`       | 8K      | `Fallback`  | ~0.5s   |
| `@cf/meta/llama-3.1-8b-instruct-fp8`           | 128K    | `General`   | ~0.9s   |
| `@cf/meta/llama-3.2-11b-vision-instruct`       | 128K    | `Vision`    | ~0.9s   |
| `@cf/qwen/qwq-32b`                             | 128K    | `Reasoning` | ~0.8s   |

### [Cohere AI](https://dashboard.cohere.com)

Cohere focuses on enterprise-grade NLP with their Command model family — built for RAG, tool use, and coding workflows. The free API tier offers replenishable credits with daily resets, and nearly every model delivers sub-second responses. Cohere AI currently has 11 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / 1,000 API calls per month

🔗 **Base URL:** `https://api.cohere.com/v2`

✅ **Verified:** August 9, 2026
| Free Model                    | Context | Best For    | Latency |
| :---------------------------- | ------- | ----------- | ------- |
| `command-a-03-2025`           | 128K    | `Agent`     | ~0.55s  |
| `c4ai-aya-vision-32b`         | 128K    | `Vision`    | ~0.55s  |
| `command-a-plus-05-2026`      | 128K    | `Agent`     | ~0.55s  |
| `command-a-vision-07-2025`    | 128K    | `Vision`    | ~0.55s  |
| `command-r-08-2024`           | 128K    | `General`   | ~0.51s  |
| `command-r-plus-08-2024`      | 128K    | `Reasoning` | ~0.54s  |
| `command-r7b-12-2024`         | 128K    | `Code`      | ~0.5s   |
| `command-r7b-arabic-02-2025`  | 128K    | `General`   | ~0.56s  |
| `c4ai-aya-expanse-32b`        | 128K    | `General`   | ~0.82s  |
| `command-a-reasoning-08-2025` | 128K    | `Reasoning` | ~0.66s  |
| `command-a-translate-08-2025` | 128K    | `Fallback`  | ~0.55s  |

### [ElectronHub](https://electronhub.ai)

ElectronHub is a credit-based inference hub offering an enormous catalog of models from OpenAI, Google, Meta, Mistral, Cohere, DeepSeek, Qwen, Microsoft, and more through an OpenAI-compatible endpoint. The free tier provides 5 RPM with $0.25 in weekly credits — replenishes every week, but the dollar cap limits heavy usage. Best for targeted queries and efficient coding. No credit card required. ElectronHub currently has 30 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ❌               |

🎁 **Free Tier Quota:** 5 RPM / $0.25 Weekly Credits

🔗 **Base URL:** `https://api.electronhub.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model                         | Context | Best For    | Latency |
| :--------------------------------- | ------- | ----------- | ------- |
| `gemini-2.5-flash-lite`            | 1M      | `General`   | ~1.7s   |
| `gemini-3.5-flash-lite`            | 1M      | `General`   | ~2.3s   |
| `gemini-3.5-flash`                 | 1M      | `General`   | ~2.5s   |
| `devstral-latest`                  | 128K    | `Code`      | ~1.8s   |
| `codestral-latest`                 | 256K    | `Code`      | ~1.5s   |
| `gpt-4.1-nano`                     | 1M      | `Code`      | ~1.6s   |
| `gpt-4.1`                          | 1M      | `General`   | ~2.5s   |
| `gpt-4o`                           | 128K    | `General`   | ~1.8s   |
| `gpt-5`                            | 128K    | `General`   | ~2.6s   |
| `deepseek-v4-flash`                | 128K    | `Reasoning` | ~2.3s   |
| `deepseek-v4-pro`                  | 128K    | `Reasoning` | ~3.0s   |
| `deepseek-v3.2`                    | 128K    | `Reasoning` | ~3.3s   |
| `qwen3-coder-30-a3b-instruct`      | 128K    | `Code`      | ~2.2s   |
| `qwen3.6-27b`                      | 128K    | `General`   | ~2.6s   |
| `qwen3-30b-a3b`                    | 128K    | `Code`      | ~1.8s   |
| `o3`                               | 200K    | `Reasoning` | ~3.1s   |
| `o4-mini`                          | 200K    | `Reasoning` | ~3.1s   |
| `claude-sonnet-5`                  | 200K    | `General`   | ~3.8s   |
| `claude-opus-4-7`                  | 200K    | `Reasoning` | ~2.9s   |
| `mistral-small-3.2-24b-instruct`   | 128K    | `Code`      | ~1.4s   |
| `mistral-medium-2508`              | 128K    | `General`   | ~1.3s   |
| `mistral-large-latest`             | 128K    | `General`   | ~1.6s   |
| `llama-3.3-70b-instruct`           | 128K    | `General`   | ~2.3s   |
| `gpt-oss-120b`                     | 128K    | `General`   | ~5.1s   |
| `gpt-oss-20b`                      | 128K    | `Code`      | ~2.3s   |
| `nemotron-3-ultra-550b-a55b`       | 128K    | `Reasoning` | ~6.6s   |
| `phi-4`                            | 128K    | `General`   | ~1.9s   |
| `grok-4.5`                         | 128K    | `Reasoning` | ~3.4s   |
| `step-3.7-flash`                   | 128K    | `Agentic`   | ~3.3s   |
| `laguna-s-2.1`                     | 128K    | `Code`      | ~3.4s   |

### [FastRouter](https://fastrouter.ai)

FastRouter is a lightweight inference hub offering Sarvam AI models with a `:free` suffix through an OpenAI-compatible endpoint. The free tier provides 10 requests per day per model with no billing credits required — a tight cap suited for occasional queries and model evaluation. No credit card required. FastRouter currently has 1 model verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPD per model / No Billing Credits Required

🔗 **Base URL:** `https://api.fastrouter.ai/api/v1`

✅ **Verified:** August 9, 2026
| Free Model                | Context | Best For  | Latency |
| :------------------------ | ------- | --------- | ------- |
| `sarvam/sarvam-105b:free` | 128K    | `General` | ~2.79s  |

### [FreeInference](https://freeinference.org)

FreeInference is a research-backed inference hub providing access to models from GLM, MiniMax, Qwen, and DeepSeek through an OpenAI-compatible endpoint. The free tier offers $20 in daily credits with 2 concurrent requests. FreeInference currently has 5 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** $20 CPD / 2 Max Concurrent Requests

🔗 **Base URL:** `https://freeinference.org/v1`

✅ **Verified:** August 9, 2026
> ⚠️ **Non-Harvard users:** new accounts go through a manual review before they're ready to use.

| Free Model          | Context | Best For    | Latency |
| :------------------ | ------- | ----------- | ------- |
| `qwen3.6-35b`       | 256K    | `Code`      | ~1.0s   |
| `deepseek-v4-flash` | 128K    | `Reasoning` | ~4.76s  |
| `diffusiongemma`    | 32K     | `General`   | ~1.79s  |
| `minimax-m2.5`      | 1M      | `General`   | ~2.61s  |
| `minimax-m3`        | 1M      | `General`   | ~2.5s   |

### [Google Gemini](https://aistudio.google.com)

Gemini offers large context windows on paper, but the free tier's **rate limits vary by model** — Flash-lite variants enjoy ~500 RPD, while standard models can be as low as 20 RPD. Use Gemini for quick, targeted tasks and single-file edits — not marathon sessions. Google Gemini currently has 14 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 5-20 RPM / 20-500 RPD / 1M TPM / Uncapped TPD

🔗 **Base URL:** `https://generativelanguage.googleapis.com/v1beta`

✅ **Verified:** August 9, 2026
| Free Model                                               | Context | Best For    | Latency |
| :------------------------------------------------------- | ------- | ----------- | ------- |
| `models/gemini-2.5-flash`                                | 1M      | `Fallback`  | ~1.1s   |
| `models/gemini-2.5-flash-lite`                           | 1M      | `Fallback`  | ~0.9s   |
| `models/gemini-3-flash-preview`                          | 1M      | `General`   | ~1.5s   |
| `models/gemini-3.1-flash-lite`                           | 1M      | `General`   | ~0.7s   |
| `models/gemini-3.1-flash-lite-preview`                   | 1M      | `Fallback`  | ~1.0s   |
| `models/gemini-3.5-flash`                                | 1M      | `Code`      | ~1.7s   |
| `models/gemini-3.5-flash-lite`                           | 1M      | `General`   | ~1.5s   |
| `models/gemini-3.6-flash`                                | 1M      | `Code`      | ~1.8s   |
| `models/gemini-flash-latest`                             | 1M      | `Code`      | ~1.7s   |
| `models/gemini-flash-lite-latest`                        | 1M      | `General`   | ~0.9s   |
| `models/gemini-robotics-er-1.6-preview`                  | 256K    | `Reasoning` | ~2.5s   |
| `models/gemini-robotics-er-2-preview`                    | 256K    | `Reasoning` | ~2.5s   |
| `models/gemma-4-26b-a4b-it`                              | 32K     | `General`   | ~1.5s   |
| `models/gemma-4-31b-it`                                  | 32K     | `General`   | ~2.3s   |

### [Gonka Broker](https://gonkabroker.com/)

Gonka Broker is a proxy gateway routing requests to providers through a single OpenAI-compatible endpoint. The free tier offers 6 RPM with 1M tokens per month — tight for sustained use, but the sub-second latencies make it a solid fallback for quick queries. No credit card required. Gonka Broker currently has 2 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ⚠️             | ✅               |

🎁 **Free Tier Quota:** 6 RPM / ~1M tokens per month

🔗 **Base URL:** `https://proxy.gonkabroker.com/v1/`

✅ **Verified:** August 9, 2026
| Free Model                | Context | Best For    | Latency |
| :------------------------ | ------- | ----------- | ------- |
| `MiniMaxAI/MiniMax-M2.7`  | 1M      | `Reasoning` | ~0.74s  |
| `moonshotai/Kimi-K2.6`    | 128K    | `Reasoning` | ~0.62s  |

### [Groq API](https://console.groq.com)

Groq is famous for providing the **absolute lowest streaming latency** in the API market, outrunning traditional cloud providers by a massive margin. The free tier offers 30 RPM with replenishable daily credits — no credit card needed. If you want a setup where your terminal files patch instantly without the typical spinning wheel delay, this is your go-to. Groq API currently has 8 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 30 RPM / 14,400 RPD / 18,000 TPM

🔗 **Base URL:** `https://api.groq.com/openai/v1`

✅ **Verified:** August 9, 2026
| Free Model                                  | Context | Best For   | Latency |
| :------------------------------------------ | ------- | ---------- | ------- |
| `openai/gpt-oss-120b`                       | 128K    | `Code`     | ~0.4s   |
| `llama-3.3-70b-versatile`                   | 128K    | `Chat`     | ~0.2s   |
| `openai/gpt-oss-20b`                        | 128K    | `Code`     | ~0.6s   |
| `qwen/qwen3.6-27b`                          | 256K    | `Code`     | ~0.2s   |
| `allam-2-7b`                                | 128K    | `Fallback` | ~0.2s   |
| `groq/compound`                             | 128K    | `General`  | ~0.7s   |
| `groq/compound-mini`                        | 128K    | `General`  | ~0.7s   |
| `llama-3.1-8b-instant`                      | 128K    | `Code`     | ~0.2s   |

### [HelixMind](https://helixmind.online)

HelixMind is a lightweight inference hub offering a small set of free models from Meta, OpenAI, Mistral, and DeepSeek through an OpenAI-compatible endpoint. The free tier provides 3 RPM with 50 requests per day — the tightest cap on this list, strictly for occasional queries and quick tests. No credit card required. HelixMind currently has 5 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 3 RPM / 50 RPD

🔗 **Base URL:** `https://helixmind.online/v1`

✅ **Verified:** August 9, 2026
| Free Model                                | Context | Best For    | Latency |
| :---------------------------------------- | ------- | ----------- | ------- |
| `deepseek-v4-flash-0731-thinking`         | 128K    | `Reasoning` | ~2.6s   |
| `gpt-oss-20b`                             | 128K    | `Code`      | ~2.4s   |
| `llama-4-scout`                           | 256K    | `General`   | ~1.1s   |
| `mimo-v2.5`                               | 128K    | `Code`      | ~1.1s   |
| `qwen3.6-35b-a3b`                         | 128K    | `General`   | ~2.1s   |

### [HelyxAI](https://helyxai.space)

HelyxAI is a unified API gateway providing access to proprietary and open-weight models through a single OpenAI-compatible endpoint. The free tier offers 100,000 tokens/day with no credit card required — self-replenishing every 24 hours. HelyxAI currently has 12 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 100,000 TPD / 1,000,000 Monthly Tokens

🔗 **Base URL:** `https://helyxai.space/v1`

✅ **Verified:** August 9, 2026
| Free Model                 | Context | Best For    | Latency |
| :------------------------- | ------- | ----------- | ------- |
| `DeepSeek-V4-Flash`        | 128K    | `Reasoning` | ~4.83s  |
| `GLM-5.2`                  | 128K    | `General`   | ~3.85s  |
| `Kimi-K3`                  | 128K    | `Reasoning` | ~2.0s   |
| `MiniMax-M3`               | 1M      | `General`   | ~1.89s  |
| `Mistral-4`                | 128K    | `General`   | ~1.5s   |
| `Qwen3-32B`                | 128K    | `General`   | ~8.0s   |
| `gemini-3.1-flash-lite`    | 1M      | `General`   | ~4.16s  |
| `gemma-4-31B-it`           | 256K    | `General`   | ~1.27s  |
| `gpt-5.6-luna`             | 128K    | `General`   | ~2.0s   |
| `gpt-oss-120b`             | 128K    | `Code`      | ~4.0s   |
| `kairalmas-4`              | 128K    | `General`   | ~2.0s   |
| `llama-3.1-8b-instruct`    | 128K    | `General`   | ~1.5s   |

### [Hugging Face Inference API](https://huggingface.co/inference-api)

Hugging Face's free Inference API gives you access to thousands of community-hosted models with OpenAI-compatible endpoints. The free tier offers only $0.10/month in credits — barely enough for light experimentation, not sustained coding. The real strength is model diversity across thousands of community models. Hugging Face currently has 98 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** $0.10/month credits (~650K tokens)

🔗 **Base URL:** `https://router.huggingface.co/v1`

✅ **Verified:** August 9, 2026
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

Intern AI is the official API provided by Shanghai AI Laboratory, the developers behind the InternLM model family. The free tier offers 90 million tokens monthly — the most generous token quota of any provider on this list. Intern AI currently has 9 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 30 RPM / 300,000 TPM / 90,000,000 Tokens per month (3,000,000 TPD)

🔗 **Base URL:** `https://chat.intern-ai.org.cn/api/v1/`

✅ **Verified:** August 9, 2026
| Free Model               | Context | Best For    | Latency |
| :----------------------- | ------- | ----------- | ------- |
| `intern-latest`          | 256K    | `General`   | ~1.0s   |
| `intern-s1`              | 128K    | `General`   | ~1.2s   |
| `intern-s1-mini`         | 128K    | `Fallback`  | ~1.0s   |
| `intern-s1-pro`          | 128K    | `Reasoning` | ~1.5s   |
| `intern-s2-preview`      | 256K    | `Reasoning` | ~1.0s   |
| `intern-s2-preview-35b`  | 256K    | `Reasoning` | ~1.5s   |
| `intern-s2-preview-397b` | 256K    | `Reasoning` | ~10.5s  |
| `internvl-latest`        | 128K    | `Vision`    | ~1.0s   |
| `internvl3.5-241b-a28b`  | 128K    | `Vision`    | ~1.1s   |
| `internvl3.5-latest`     | 128K    | `Vision`    | ~1.0s   |

### [Kilo Code](https://app.kilo.ai)

Kilo Code is a coding-agent platform that proxies free models from OpenRouter, NVIDIA, Poolside, and others through a single API key. The free tier offers generous replenishable credits with no hard daily cap — a solid Swiss-army-knife provider that gives you access to a diverse model pool through one endpoint. Kilo Code currently has 9 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 5 RPM / 200 RPD

🔗 **Base URL:** `https://api.kilo.ai/api/gateway`

✅ **Verified:** August 9, 2026
| Free Model                                           | Context | Best For    | Latency |
| :--------------------------------------------------- | ------- | ----------- | ------- |
| `cohere/north-mini-code:free`                        | 128K    | `Code`      | ~1.5s   |
| `inclusionai/ling-3.0-tiny:free`                     | 128K    | `General`   | ~1.0s   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 128K    | `Reasoning` | ~2.5s   |
| `nvidia/nemotron-3-super-120b-a12b:free`             | 1M      | `General`   | ~0.8s   |
| `nvidia/nemotron-3-ultra-550b-a55b:free`             | 128K    | `General`   | ~1.5s   |
| `poolside/laguna-s-2.1:free`                         | 256K    | `Code`      | ~1.3s   |
| `poolside/laguna-xs-2.1:free`                        | 128K    | `Code`      | ~0.9s   |
| `stepfun/step-3.7-flash:free`                        | 128K    | `General`   | ~2.5s   |
| `tencent/hy3:free`                                   | 128K    | `General`   | ~2.2s   |

### [LLM.Kiwi](https://llm.kiwi)

LLM.Kiwi is a Cloudflare-edge inference provider offering an auto-routing endpoint that selects the best available model automatically, plus a Croatian-specific model. The free tier offers 40 requests per hour with no credit card required — sign in with GitHub or Google. LLM.Kiwi currently has 2 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ⚠️         | ❌      | ✅              | ✅               |

🎁 **Free Tier Quota:** 40 RPH / No Credit Card

🔗 **Base URL:** `https://api.llm.kiwi/v1`

✅ **Verified:** August 9, 2026
| Free Model | Context | Best For  | Latency |
| :--------- | :------ | :-------- | ------- |
| `auto`     | Varied  | `General` | ~1.0s   |
| `hrLLM`    | Varied  | `General` | ~2.4s   |

### [LLM7.IO](https://llm7.io)

LLM7.IO is a rising inference provider serving open-weight models via Llama.cpp server with OpenAI-compatible endpoints. The Turbo Tier (Free tier) offers replenishable credits with no daily hard cap — a solid option for consistent daily coding on a simple API without commitment. LLM7.IO currently has 5 models verified — all at Turbo Tier (Free tier).

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 40 RPM / 2,400 RPD / 128,000 Characters per Request / 1,000,000 TPD

🔗 **Base URL:** `https://api.llm7.io/v1`

✅ **Verified:** August 9, 2026
| Free Model                       | Context | Best For    | Latency |
| :------------------------------- | ------- | ----------- | ------- |
| `codestral-latest`               | 256K    | `Code`      | ~0.67s  |
| `gemma4:31b`                     | 32K     | `General`   | ~2.0s   |
| `gpt-oss:20b`                    | 128K    | `Code`      | ~2.0s   |
| `minimax-m2.7`                   | 128K    | `Reasoning` | ~1.8s   |
| `mistral-Nemo-Instruct-2407`     | 128K    | `General`   | ~3.1s   |

### [LLMGateway](https://llmgateway.io)

LLMGateway is a lightweight inference hub serving models from Zhipu AI and more at $0 per 1M tokens — a genuinely free per-token pricing model with no credit cap. The free tier offers 5 requests per 10 minutes with no daily token limit, making it practical for light coding and scripting tasks. No credit card required. LLMGateway currently has 1 model verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ❌               |

🎁 **Free Tier Quota:** 5 requests per 10 minutes / $0 per 1M tokens

🔗 **Base URL:** `https://api.llmgateway.io/v1`

✅ **Verified:** August 9, 2026
| Free Model              | Context | Best For  | Latency |
| :---------------------- | ------- | --------- | ------- |
| `claude-haiku-4-5-free` | 200K    | `General` | ~1.2s   |

### [LiteRouter](https://literouter.com)

LiteRouter is a lightweight inference hub offering free models from OpenAI, DeepSeek, Mistral, Meta, and more through an OpenAI-compatible endpoint with a `:free` suffix. The free tier provides uncapped daily requests with 1 concurrent request and 15,000 tokens per day — enough for light scripting and targeted queries. No credit card required. LiteRouter currently has 36 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ❌      | ✅              | ⚠️              |

🔗 **Base URL:** `https://api.literouter.com/v1`

✅ **Verified:** August 9, 2026
| Free Model                             | Context | Best For    | Latency |
| :------------------------------------- | ------- | ----------- | ------- |
| `claude-haiku-4.5-cheap:free`          | 200K    | `General`   | ~4.8s   |
| `deepseek-r1-0528:free`                | 128K    | `Reasoning` | ~4.6s   |
| `deepseek-r1:free`                     | 128K    | `Reasoning` | ~2.6s   |
| `deepseek-reasoner:free`               | 128K    | `Reasoning` | ~3.0s   |
| `deepseek-v3-0324:free`                | 128K    | `Reasoning` | ~5.0s   |
| `deepseek-v3.1-terminus:free`          | 128K    | `Reasoning` | ~2.8s   |
| `deepseek-v3.1:free`                   | 128K    | `Reasoning` | ~2.4s   |
| `deepseek-v3.2:free`                   | 128K    | `Reasoning` | ~3.4s   |
| `deepseek-v3:free`                     | 128K    | `Reasoning` | ~2.9s   |
| `deepseek-v4-flash:free`               | 128K    | `Reasoning` | ~4.0s   |
| `deepseek-v4-flash-cheap:free`         | 128K    | `Reasoning` | ~3.5s   |
| `deepseek-v4-pro:free`                 | 128K    | `Reasoning` | ~3.5s   |
| `deepseek-v4-pro-cheap:free`           | 128K    | `Reasoning` | ~3.0s   |
| `gemini-2.5-flash-lite:free`           | 1M      | `General`   | ~2.0s   |
| `gemini-2.5-flash:free`                | 1M      | `General`   | ~3.3s   |
| `gemma-3-27b-it:free`                  | 32K     | `General`   | ~3.0s   |
| `gemma-4-31b:free`                     | 32K     | `General`   | ~2.3s   |
| `gpt-4.1-mini:free`                    | 1M      | `General`   | ~2.2s   |
| `gpt-4.1-nano:free`                    | 1M      | `Code`      | ~2.5s   |
| `gpt-4o-mini:free`                     | 128K    | `General`   | ~2.0s   |
| `gpt-5-nano:free`                      | 128K    | `Code`      | ~3.1s   |
| `gpt-oss-120b:free`                    | 128K    | `General`   | ~2.0s   |
| `gpt-oss-20b:free`                     | 128K    | `Code`      | ~2.7s   |
| `grok-4.1-fast-reasoning:free`         | 128K    | `Reasoning` | ~4.2s   |
| `l3-8b-lunaris:free`                   | 8K      | `Fallback`  | ~2.1s   |
| `llama-3-8b-instruct:free`             | 8K      | `General`   | ~2.5s   |
| `llama-3.1-8b-instruct:free`           | 128K    | `General`   | ~2.5s   |
| `llama-3.3-70b-instruct-turbo:free`    | 128K    | `General`   | ~2.7s   |
| `minimax-m2.7:free`                    | 128K    | `Reasoning` | ~2.0s   |
| `ministral-3b-2512:free`               | 128K    | `Code`      | ~1.4s   |
| `mistral-large-3:free`                 | 128K    | `Reasoning` | ~3.0s   |
| `mistral-nemo-instruct-2407:free`      | 128K    | `General`   | ~1.5s   |
| `mistral-small-24b-instruct-2501:free` | 128K    | `Code`      | ~1.5s   |
| `mythomax-l2-13b:free`                 | 13K     | `General`   | ~2.0s   |
| `nemotron-3-nano:free`                 | 128K    | `General`   | ~1.5s   |
| `qwen3.5:free`                         | 1M      | `General`   | ~7.0s   |
### [MNN AI](https://mnnai.ru)

MNN AI is a credit-based inference hub offering models from OpenAI, Google, DeepSeek, Qwen, Meta, Mistral, Moonshot, Stepfun, and more through an OpenAI-compatible endpoint. The free tier provides 10 RPM with $1 in monthly credits — replenishable each month, but the dollar cap limits heavy usage. Best suited for light daily coding and targeted queries. No credit card required. MNN AI currently has 20 verified coding-relevant models.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPM / $1 Monthly Credits

🔗 **Base URL:** `https://api2.mnnai.ru/v1`

✅ **Verified:** August 9, 2026
| Free Model                         | Context | Best For    | Latency |
| :--------------------------------- | ------- | ----------- | ------- |
| `deepseek-v3.1`                    | 128K    | `Reasoning` | ~2.2s   |
| `deepseek-v3.2`                    | 128K    | `Reasoning` | ~2.0s   |
| `deepseek-v4-flash`                | 128K    | `Reasoning` | ~1.8s   |
| `gemini-3-flash-preview`           | 1M      | `General`   | ~2.0s   |
| `gemini-3.1-flash-lite`            | 1M      | `General`   | ~1.5s   |
| `gemini-3.5-flash`                 | 1M      | `Code`      | ~2.0s   |
| `gpt-4.1-mini`                     | 1M      | `General`   | ~1.5s   |
| `gpt-4.1-nano`                     | 1M      | `Code`      | ~1.0s   |
| `gpt-5-nano`                       | 128K    | `Code`      | ~1.2s   |
| `gpt-5.1`                          | 128K    | `General`   | ~1.8s   |
| `gpt-5.2`                          | 128K    | `General`   | ~2.3s   |
| `gpt-oss-120b`                     | 128K    | `General`   | ~1.8s   |
| `gpt-oss-20b`                      | 128K    | `Code`      | ~1.5s   |
| `mistral-large-latest`             | 128K    | `Reasoning` | ~2.5s   |
| `nemotron-3-nano`                  | 128K    | `Code`      | ~1.5s   |
| `o3-mini`                          | 200K    | `Reasoning` | ~2.0s   |
| `o4-mini`                          | 200K    | `Reasoning` | ~1.8s   |
| `qwen-3-coder-plus`                | 256K    | `Code`      | ~2.1s   |
| `qwen-3-235b-a22b`                 | 256K    | `Reasoning` | ~3.0s   |
| `step-3.7-flash`                   | 128K    | `Agentic`   | ~1.8s   |

### [MegaNova AI](https://meganova.ai)

MegaNova AI is a community-model inference hub offering fine-tuned variants of Llama, Mistral, and its own Manta series through an OpenAI-compatible endpoint. The free tier provides 60 RPM with 550 requests per day and 200,000 tokens per minute — generous throughput for a community model hub. No credit card required. MegaNova AI currently has 8 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 60 RPM / 550 RPD / 200,000 TPM

🔗 **Base URL:** `https://api.meganova.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model                                              | Context | Best For  | Latency |
| :------------------------------------------------------ | ------- | --------- | ------- |
| `BruhzWater/Sapphira-L3.3-70b-0.1`                      | 128K    | `General` | ~1.5s   |
| `FallenMerick/MN-Violet-Lotus-12B`                      | 32K     | `General` | ~1.3s   |
| `meganova-ai/manta-flash-1.0`                           | 128K    | `General` | ~1.1s   |
| `meganova-ai/manta-mini-1.0`                            | 128K    | `General` | ~1.3s   |
| `mistralai/Mistral-Small-3.2-24B-Instruct-2506`         | 128K    | `General` | ~1.5s   |
| `Sao10K/L3-70B-Euryale-v2.1`                            | 128K    | `General` | ~1.3s   |
| `Sao10K/L3-8B-Stheno-v3.2`                              | 128K    | `General` | ~1.0s   |
| `Steelskull/L3.3-MS-Nevoria-70b`                        | 128K    | `General` | ~1.5s   |

### [Mistral AI](https://console.mistral.ai)

Mistral AI is highly regarded for building models that punch far above their **parameter weight class**, with exceptionally clean instruction following and compact execution. The free tier offers replenishable credits with generous RPM limits. Mistral AI currently has 32 models verified (with aliases).

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** ~2–30 RPM / 50,000 TPM shared pool

🔗 **Base URL:** `https://api.mistral.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model                                          | Context | Best For    | Latency |
| :-------------------------------------------------- | ------- | ----------- | ------- |
| `mistral-code-agent-latest`                         | 128K    | `Agent`     | ~0.4s   |
| `codestral-latest` / `codestral-2508`               | 256K    | `Code`      | ~0.4s   |
| `devstral-medium-latest`                            | 128K    | `Agent`     | ~0.9s   |
| `magistral-small-latest`                            | 128K    | `General`   | ~0.5s   |
| `mistral-code-fim-latest`                           | 128K    | `Code`      | ~0.4s   |
| `mistral-code-latest`                               | 128K    | `Code`      | ~0.4s   |
| `mistral-large-latest` / `mistral-large-2512`       | 128K    | `Reasoning` | ~0.7s   |
| `mistral-medium-2604`                               | 32K     | `General`   | ~0.5s   |
| `mistral-medium-3`                                  | 32K     | `General`   | ~0.5s   |
| `mistral-medium-3.5` / `mistral-medium-3-5`         | 32K     | `General`   | ~0.5s   |
| `mistral-medium-latest` / `mistral-medium`          | 32K     | `General`   | ~0.6s   |
| `mistral-small-latest` / `mistral-small-2603`       | 32K     | `General`   | ~0.5s   |
| `devstral-latest` / `devstral-2512`                 | 128K    | `Agent`     | ~0.5s   |
| `ministral-14b-latest` / `ministral-14b-2512`       | 128K    | `General`   | ~0.4s   |
| `ministral-8b-latest` / `ministral-8b-2512`         | 128K    | `General`   | ~0.5s   |
| `ministral-3b-latest` / `ministral-3b-2512`         | 128K    | `General`   | ~0.4s   |
| `mistral-medium-2505`                               | 32K     | `Fallback`  | ~0.8s   |
| `mistral-medium-2508`                               | 32K     | `Fallback`  | ~0.8s   |
| `mistral-vibe-cli-fast`                             | 32K     | `Agent`     | ~0.5s   |
| `mistral-vibe-cli-latest`                           | 32K     | `Agent`     | ~0.5s   |
| `mistral-vibe-cli-with-tools`                       | 32K     | `Agent`     | ~1.4s   |
| `voxtral-small-latest` / `voxtral-small-2507`       | 128K    | `General`   | ~0.6s   |

### [Mixlayer](https://www.mixlayer.com)

Mixlayer is an inference platform for open-source AI models with an OpenAI-compatible API. The free tier offers `qwen/qwen3.5-4b-free` for prototyping with rate limits — no credit card required for the free model. A focused Qwen 3.5/3.6 catalog with tool calling and reasoning support. Mixlayer currently has 1 model verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / Can be rate-limited (daily usage)

🔗 **Base URL:** `https://models.mixlayer.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model             | Context | Best For  | Latency |
| :--------------------- | ------- | --------- | ------- |
| `qwen/qwen3.5-4b-free` | 256K    | `General` | ~1.0s   |

### [Naga AI](https://naga.ac)

Naga AI is a lightweight inference hub offering a small set of free models from NVIDIA and Meta through an OpenAI-compatible endpoint. The free tier provides 10 RPM with 100 requests per day — a very tight cap that limits it to occasional queries and quick debugging. No credit card required. Naga AI currently has 4 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPM / 100 RPD

🔗 **Base URL:** `https://api.naga.ac/v1`

✅ **Verified:** August 9, 2026
| Free Model                            | Context | Best For    | Latency |
| :------------------------------------ | ------- | ----------- | ------- |
| `llama-3.3-70b-instruct:free`         | 128K    | `General`   | ~1.6s   |
| `nemotron-3-super-120b-a12b:free`     | 1M      | `General`   | ~3.2s   |
| `nemotron-3-ultra-550b-a55b:free`     | 128K    | `General`   | ~2.5s   |
| `sonar:free`                          | 128K    | `General`   | ~1.5s   |

### [Navy API](https://api.navy)

Navy API is a high-volume inference hub offering an extensive catalog of models from OpenAI, DeepSeek, Grok, Google, Mistral, Cohere, Meta, Zhipu, and more through an OpenAI-compatible endpoint. The free tier provides 20 RPM with 250,000 daily tokens — enough throughput for serious coding sessions. No credit card required. Navy API currently has 30 verified coding-relevant models.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / 250,000 TPD

🔗 **Base URL:** `https://api.navy/v1`

✅ **Verified:** August 9, 2026
| Free Model                             | Context | Best For    | Latency |
| :------------------------------------- | ------- | ----------- | ------- |
| `codestral-2508`                       | 256K    | `Code`      | ~1.0s   |
| `codestral-latest`                     | 256K    | `Code`      | ~0.8s   |
| `command-a`                            | 128K    | `General`   | ~1.2s   |
| `command-a-plus`                       | 128K    | `Agent`     | ~1.5s   |
| `command-a-reasoning`                  | 128K    | `Reasoning` | ~1.8s   |
| `command-a-vision`                     | 128K    | `Vision`    | ~1.5s   |
| `deepseek-chat`                        | 128K    | `General`   | ~1.5s   |
| `deepseek-reasoner`                    | 128K    | `Reasoning` | ~2.0s   |
| `deepseek-v3.2`                        | 128K    | `Reasoning` | ~2.0s   |
| `deepseek-v4-flash`                    | 128K    | `Code`      | ~1.0s   |
| `deepseek-v4-flash-0731`               | 128K    | `Code`      | ~1.0s   |
| `deepseek-v4-pro`                      | 128K    | `Reasoning` | ~1.6s   |
| `gemini-2.5-flash`                     | 1M      | `General`   | ~1.5s   |
| `gemini-3-flash-preview`               | 1M      | `General`   | ~1.5s   |
| `gemini-3.1-flash-lite`                | 1M      | `General`   | ~0.8s   |
| `gemini-3.5-flash`                     | 1M      | `Code`      | ~1.7s   |
| `gemini-3.6-flash`                     | 1M      | `Code`      | ~1.8s   |
| `glm-5.2`                              | 128K    | `General`   | ~1.5s   |
| `gpt-4.1`                              | 1M      | `General`   | ~1.2s   |
| `gpt-4.1-mini`                         | 1M      | `Code`      | ~1.0s   |
| `gpt-4.1-nano`                         | 1M      | `Code`      | ~0.8s   |
| `gpt-5.3-codex`                        | 128K    | `Code`      | ~1.5s   |
| `gpt-5.4`                              | 128K    | `General`   | ~1.3s   |
| `gpt-5.4-mini`                         | 128K    | `General`   | ~1.2s   |
| `gpt-5.4-nano`                         | 128K    | `Code`      | ~1.0s   |
| `gpt-oss-120b`                         | 128K    | `General`   | ~0.8s   |
| `gpt-oss-20b`                          | 128K    | `Code`      | ~1.2s   |
| `grok-4.5`                             | 128K    | `General`   | ~1.5s   |
| `kimi-k2.6`                            | 128K    | `Reasoning` | ~1.0s   |
| `qwen3.6-27b`                          | 256K    | `Code`      | ~0.5s   |

### [NVIDIA NIM](https://build.nvidia.com)

NVIDIA NIM is NVIDIA's free API catalog offering 100+ models from DeepSeek, Meta, Mistral, Google, Qwen, and more through OpenAI-compatible endpoints — no credit card required. The largest free model library on the list, but 40 RPM per model caps it as a backup pool rather than a daily driver. Only models tagged as **Free Endpoint** (hosted on NVIDIA's own infrastructure) are listed below. NVIDIA NIM currently has 18 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ❌              | ✅               |

🎁 **Free Tier Quota:** 40 RPM / Uncapped TPD

🔗 **Base URL:** `https://integrate.api.nvidia.com/v1`

✅ **Verified:** August 9, 2026
> ⚠️ May require **Phone verification** to generate an API Key.

| Free Model                                      | Context | Best For    | Latency |
| :---------------------------------------------- | ------- | ----------- | ------- |
| `deepseek-ai/deepseek-v4-flash-0731`            | 128K    | `Code`      | ~1.0s   |
| `meta/llama-3.1-70b-instruct`                   | 128K    | `General`   | ~0.5s   |
| `meta/llama-3.1-8b-instruct`                    | 128K    | `Fallback`  | ~0.8s   |
| `meta/llama-3.2-11b-vision-instruct`            | 128K    | `Vision`    | ~1.0s   |
| `meta/llama-3.2-3b-instruct`                    | 8K      | `Fallback`  | ~0.5s   |
| `nvidia/llama-3.3-nemotron-super-49b-v1`        | 128K    | `General`   | ~2.1s   |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5`      | 128K    | `General`   | ~2.7s   |
| `nvidia/nemotron-3-nano-30b-a3b`                | 128K    | `General`   | ~0.3s   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | 128K    | `Reasoning` | ~0.4s   |
| `nvidia/nemotron-3-super-120b-a12b`             | 1M      | `Reasoning` | ~0.7s   |
| `nvidia/nemotron-3-ultra-550b-a55b`             | 128K    | `General`   | ~2.5s   |
| `nvidia/nemotron-nano-12b-v2-vl`                | 32K     | `Vision`    | ~1.0s   |
| `nvidia/nvidia-nemotron-nano-9b-v2`             | 128K    | `Fallback`  | ~1.5s   |
| `openai/gpt-oss-120b`                           | 128K    | `General`   | ~1.0s   |
| `openai/gpt-oss-20b`                            | 128K    | `General`   | ~2.0s   |
| `poolside/laguna-xs-2.1`                        | 128K    | `Code`      | ~1.5s   |
| `stepfun-ai/step-3.7-flash`                     | 128K    | `Agentic`   | ~0.5s   |
| `thinkingmachines/inkling`                      | 128K    | `General`   | ~2.7s   |

### [Ollama Cloud](https://ollama.com)

Ollama Cloud is a cloud-hosted inference service running Ollama behind the scenes, offering a vast model registry without the need to run locally. The free tier gives you a 5-hour session window that resets weekly — uncapped during that window but limited by the weekly refresh. Models respond cleanly and quickly, making it one of the stronger free providers for coding if you plan around the session. Ollama Cloud currently has 7 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 1 Instance / 5-Hour Session Usage / 7-day Weekly Usage

🔗 **Base URL:** `https://api.ollama.com`

✅ **Verified:** August 9, 2026
| Free Model            | Context | Best For    | Latency |
| :-------------------- | ------- | ----------- | ------- |
| `gemma4:31b`          | 32K     | `General`   | ~3.8s   |
| `gpt-oss:120b`        | 128K    | `General`   | ~1.3s   |
| `gpt-oss:20b`         | 128K    | `Reasoning` | ~1.3s   |
| `minimax-m3`          | 1M      | `General`   | ~3.9s   |
| `nemotron-3-nano:30b` | 128K    | `Reasoning` | ~2.1s   |
| `nemotron-3-super`    | 1M      | `General`   | ~2.0s   |
| `nemotron-3-ultra`    | 128K    | `General`   | ~1.5s   |

### [OpenCode Zen](https://opencode.ai/zen)

OpenCode Zen is a curated set of AI models tested and optimized for coding agents by the OpenCode team. The free tier offers 6 models at zero cost through an OpenAI-compatible API — no credit card or billing required for free models. OpenCode Zen currently has 9 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 30 RPM / 500 RPD / 1,000,000 TPD / Daily Limits

🔗 **Base URL:** `https://opencode.ai/zen/v1`

✅ **Verified:** August 9, 2026
| Free Model               | Context | Best For      | Latency |
| :----------------------- | ------- | ------------- | ------- |
| `big-pickle`             | 128K    | `Fallback`    | ~1.87s  |
| `deepseek-v4-flash-free` | 200K    | `Code`        | ~1.93s  |
| `laguna-s-2.1-free`      | 128K    | `Code`        | ~1.5s   |
| `ling-3.0-flash-free`    | 128K    | `General`     | ~2.30s  |
| `ling-3.0-tiny-free`     | 128K    | `General`     | ~1.67s  |
| `longcat-2.0-free`       | 128K    | `General`     | ~4.51s  |
| `mimo-v2.5-free`         | 128K    | `Code`        | ~2.74s  |
| `nemotron-3-ultra-free`  | 128K    | `Code Review` | ~1.94s  |
| `north-mini-code-free`   | 128K    | `Fallback`    | ~1.66s  |

### [OpenRouter](https://openrouter.ai)

OpenRouter is a unified API gateway providing access to hundreds of models from dozens of providers through a single endpoint. The free tier offers rate-limited access to community-hosted models (marked with `:free`) that changes often — no credit card required. A great backup when other providers are rate-limited. OpenRouter currently has 12 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / 50 RPD

🔗 **Base URL:** `https://openrouter.ai/api/v1`

✅ **Verified:** August 9, 2026
| Free Model                                           | Context | Best For    | Latency |
| :--------------------------------------------------- | ------- | ----------- | ------- |
| `cohere/north-mini-code:free`                        | 128K    | `Code`      | ~2.1s   |
| `google/gemma-4-26b-a4b-it:free`                     | 32K     | `General`   | ~1.3s   |
| `inclusionai/ling-3.0-tiny:free`                     | 128K    | `General`   | ~1.0s   |
| `nvidia/nemotron-3-nano-30b-a3b:free`                | 128K    | `General`   | ~0.7s   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 128K    | `Reasoning` | ~0.7s   |
| `nvidia/nemotron-3-super-120b-a12b:free`             | 1M      | `General`   | ~2.7s   |
| `nvidia/nemotron-3-ultra-550b-a55b:free`             | 128K    | `General`   | ~3.0s   |
| `nvidia/nemotron-nano-12b-v2-vl:free`                | 32K     | `Vision`    | ~1.3s   |
| `nvidia/nemotron-nano-9b-v2:free`                    | 128K    | `General`   | ~0.9s   |
| `openai/gpt-oss-20b:free`                            | 128K    | `Code`      | ~2.0s   |
| `poolside/laguna-s-2.1:free`                         | 128K    | `Code`      | ~2.0s   |
| `poolside/laguna-xs-2.1:free`                        | 128K    | `Code`      | ~1.9s   |

### [Poixe AI](https://poixe.com)

Poixe AI is a unified API gateway aggregating models from OpenAI, Anthropic, Google, xAI, ByteDance, Alibaba, Moonshot, and more through a single OpenAI-compatible endpoint. The free tier offers 10,000 requests per day with 10 million daily tokens — one of the most generous quotas on this list. Append `:free` to any model name to access the free tier; May be rate-limited depending on model. Poixe AI currently has 20 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ⚠️     | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 10,000 RPD / 10,000,000 TPD

🔗 **Base URL:** `https://api.poixe.com/v1/`

✅ **Verified:** August 9, 2026
| Free Model                                | Context | Best For    | Latency |
| :---------------------------------------- | ------- | ----------- | ------- |
| `claude-sonnet-4-5-20250929:free`         | 200K    | `Reasoning` | ~2.5s   |
| `doubao-1-5-lite-32k-250115:free`         | 32K     | `General`   | ~1.0s   |
| `doubao-1-5-pro-32k-250115:free`          | 32K     | `Reasoning` | ~2.0s   |
| `doubao-seed-1-6-250615:free`             | 128K    | `General`   | ~3.9s   |
| `doubao-seed-1-6-flash-250615:free`       | 128K    | `General`   | ~1.2s   |
| `gemini-2.5-flash-lite:free`              | 1M      | `General`   | ~1.0s   |
| `gemini-2.5-flash:free`                   | 1M      | `General`   | ~1.5s   |
| `gpt-4.1-mini:free`                       | 1M      | `General`   | ~1.0s   |
| `gpt-4.1-nano:free`                       | 1M      | `Code`      | ~0.9s   |
| `gpt-4o-mini:free`                        | 128K    | `General`   | ~0.9s   |
| `gpt-oss-20b:free`                        | 128K    | `Code`      | ~0.8s   |
| `grok-3-mini-beta:free`                   | 128K    | `Reasoning` | ~3.4s   |
| `qwen-long:free`                          | 1M      | `General`   | ~1.5s   |
| `qwen-plus:free`                          | 128K    | `General`   | ~1.3s   |
| `qwen-turbo:free`                         | 128K    | `Fallback`  | ~1.0s   |
| `qwen3-14b:free`                          | 128K    | `Reasoning` | ~1.2s   |
| `qwen3-235b-a22b:free`                    | 128K    | `General`   | ~2.0s   |
| `qwen3-8b:free`                           | 128K    | `Code`      | ~1.0s   |
| `qwen3-coder-480b-a35b-instruct:free`     | 256K    | `Code`      | ~1.2s   |
| `doubao-1-5-vision-pro-32k-250115:free`   | 32K     | `Vision`    | ~2.5s   |

### [Poolside](https://poolside.ai)

Poolside is a foundation model lab building purpose-built coding models from scratch. Their Laguna family — XS.2 (33B-A3B) and S.2 (131B-A13B) — are trained on 30T tokens exclusively for agentic software engineering with tool calling and 256K context. The models are free while in preview — the same "use it while it lasts" uncertainty as any free provider. Poolside currently has 2 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ⚠️     | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / 200 RPD / 150,000 TPM / 1,000,000 TPD

🔗 **Base URL:** `https://inference.poolside.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model               | Context | Best For | Latency |
| :----------------------- | ------- | -------- | ------- |
| `poolside/laguna-s-2.1`  | 256K    | `Code`   | ~1.3s   |
| `poolside/laguna-xs-2.1` | 128K    | `Code`   | ~0.9s   |

### [Routeway AI](https://routeway.ai)

Routeway is a unified API gateway offering free models through a `:free` model suffix — a pattern shared with OpenRouter and Kilo Code. Models are drawn from Stepfun, NVIDIA, Poolside, Meta, and others, all accessed through a single OpenAI-compatible endpoint with no credit card required. The tight 5 RPM cap makes Routeway a fallback hub rather than a daily driver. Routeway currently has 5 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ⚠️     | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 5 RPM / 200 RPD / 300,000 TPD

🔗 **Base URL:** `https://api.routeway.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model                     | Context | Best For    | Latency |
| :----------------------------- | ------- | ----------- | ------- |
| `laguna-xs.2:free`             | 128K    | `Code`      | ~0.9s   |
| `llama-3.2-3b-instruct:free`   | 8K      | `Fallback`  | ~0.7s   |
| `nemotron-3-nano-30b-a3b:free` | 128K    | `Reasoning` | ~1.0s   |
| `nemotron-nano-9b-v2:free`     | 128K    | `Code`      | ~0.8s   |
| `step-3.7-flash:free`          | 128K    | `Agentic`   | ~2.5s   |

### [SambaNova AI](https://cloud.sambanova.ai)

SambaNova AI is a **hardware-driven inference provider** utilizing proprietary Reconfigurable Dataflow Units (RDUs) rather than standard GPUs, removing the traditional hardware-decode bottleneck for incredibly high throughput. The free tier is limited to 20 requests and 200k tokens per day — tight for sustained use. SambaNova AI currently has 4 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 20 RPM / 20 RPD / 200,000 TPD

🔗 **Base URL:** `https://api.sambanova.ai/v1`

✅ **Verified:** August 9, 2026
| Free Model                    | Context | Best For  | Latency |
| :---------------------------- | ------- | --------- | ------- |
| `DeepSeek-V3.1`               | 128K    | `Agent`   | ~1.0s   |
| `gemma-4-31B-it`              | 32K     | `General` | ~1.5s   |
| `gpt-oss-120b`                | 128K    | `General` | ~0.9s   |
| `Meta-Llama-3.3-70B-Instruct` | 128K    | `General` | ~2.0s   |

### [Speka AI](https://speka.me)

Speka AI is a credit-based inference hub offering competitive per-token pricing on models from DeepSeek, NVIDIA, Meta, Mistral, and Moonshot through an OpenAI-compatible endpoint. The free tier provides 10 RPM with $1 in monthly credits — replenishes each month, but the dollar cap limits heavy usage. Best suited for light daily coding and targeted queries. No credit card required. Speka AI currently has 18 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPM / $1 Monthly Credits

🔗 **Base URL:** `https://speka.me/v1`

✅ **Verified:** August 9, 2026
| Free Model                                     | Context | Best For    | Latency |
| :--------------------------------------------- | ------- | ----------- | ------- |
| `deepseek-ai/deepseek-v4-flash`                | 128K    | `Reasoning` | ~2.3s   |
| `meta/llama-3.1-8b-instruct`                   | 128K    | `Chat`      | ~1.1s   |
| `meta/llama-3.2-11b-vision-instruct`           | 128K    | `Vision`    | ~1.2s   |
| `meta/llama-3.2-3b-instruct`                   | 8K      | `Fallback`  | ~0.7s   |
| `meta/llama-3.2-90b-vision-instruct`           | 128K    | `Vision`    | ~1.3s   |
| `minimaxai/minimax-m3`                         | 1M      | `General`   | ~3.9s   |
| `mistralai/mistral-nemotron`                   | 128K    | `General`   | ~2.5s   |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5`     | 128K    | `General`   | ~1.4s   |
| `nvidia/nemotron-3-nano-30b-a3b`               | 128K    | `General`   | ~1.5s   |
| `nvidia/nemotron-3-super-120b-a12b`            | 1M      | `General`   | ~3.0s   |
| `nvidia/nemotron-3-ultra-550b-a55b`            | 128K    | `Reasoning` | ~2.0s   |
| `nvidia/nemotron-nano-12b-v2-vl`               | 32K     | `Vision`    | ~2.0s   |
| `nvidia/nvidia-nemotron-nano-9b-v2`            | 128K    | `General`   | ~1.3s   |
| `openai/gpt-oss-120b`                          | 128K    | `General`   | ~5.1s   |
| `openai/gpt-oss-20b`                           | 128K    | `Code`      | ~1.5s   |
| `poolside/laguna-xs-2.1`                       | 128K    | `Code`      | ~1.5s   |
| `stepfun-ai/step-3.7-flash`                    | 128K    | `Agentic`   | ~1.5s   |
| `thinkingmachines/inkling`                     | 128K    | `General`   | ~2.7s   |

### [TokenReply](https://tokenreply.com)

TokenReply is a lightweight inference hub offering models from Google, DeepSeek, OpenAI, Qwen, Moonshot, Stepfun, Zhipu, and more through an OpenAI-compatible endpoint. The free tier provides 3 RPM with 40 weekly model calls — a very tight cap suited for lightweight evaluation and occasional queries, not sustained coding. Free models only. No credit card required. TokenReply currently has 5 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ⚠️     | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 3 RPM / 40 Weekly Model Calls / Free Models Only

🔗 **Base URL:** `https://api.tokenreply.com/v1`

✅ **Verified:** August 9, 2026
| Free Model                          | Context | Best For    | Latency |
| :---------------------------------- | ------- | ----------- | ------- |
| `google/gemma-4-26b-a4b-it`         | 32K     | `General`   | ~2.3s   |
| `google/gemma-4-31b-it`             | 32K     | `General`   | ~2.5s   |
| `nvidia/nemotron-3-ultra-550b-a55b` | 128K    | `General`   | ~1.3s   |
| `openai/gpt-oss-120b`               | 128K    | `General`   | ~4.3s   |
| `stepfun-ai/step-3.7-flash`         | 128K    | `Agentic`   | ~1.8s   |

### [Void AI](https://voidai.app)

Void AI is a high-RPM inference hub offering models from OpenAI, Google, DeepSeek, Qwen, Moonshot, Zhipu, and more through an OpenAI-compatible endpoint. The free tier provides 100 RPM with 125,000 daily credits — the highest RPM of any hub on this list, ideal for high-throughput coding sessions. No credit card required. Void AI currently has 20 verified coding-relevant models.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 100 RPM / 125,000 Daily Credits

🔗 **Base URL:** `https://api.voidai.app/v1`

✅ **Verified:** August 9, 2026
| Free Model                       | Context | Best For    | Latency |
| :------------------------------- | ------- | ----------- | ------- |
| `deepseek-v3.2`                  | 128K    | `Reasoning` | ~2.0s   |
| `deepseek-v4-flash`              | 128K    | `Reasoning` | ~1.5s   |
| `deepseek-v4-flash-0731`         | 128K    | `Reasoning` | ~1.5s   |
| `deepseek-v4-pro`                | 128K    | `Reasoning` | ~1.6s   |
| `gemini-3.1-pro-preview`         | 1M      | `Reasoning` | ~2.0s   |
| `gemini-3.5-flash`               | 1M      | `Code`      | ~1.7s   |
| `gemini-3.5-flash-lite`          | 1M      | `General`   | ~1.5s   |
| `gemini-3.6-flash`               | 128K    | `Code`      | ~1.5s   |
| `glm-5.2`                        | 128K    | `General`   | ~2.0s   |
| `gpt-4.1-mini`                   | 1M      | `General`   | ~1.5s   |
| `gpt-5.3-codex`                  | 128K    | `Code`      | ~1.5s   |
| `gpt-5.4`                        | 128K    | `General`   | ~1.3s   |
| `gpt-5.4-mini`                   | 128K    | `General`   | ~1.2s   |
| `gpt-5.4-nano`                   | 128K    | `Code`      | ~1.0s   |
| `gpt-oss-20b`                    | 128K    | `Code`      | ~1.5s   |
| `kimi-k2.6`                      | 128K    | `Reasoning` | ~0.8s   |
| `kimi-k2.7-code`                 | 128K    | `Code`      | ~1.5s   |
| `kimi-k3`                        | 128K    | `Reasoning` | ~1.5s   |
| `qwen3-235b-a22b-instruct`       | 256K    | `Reasoning` | ~2.5s   |
| `qwen3-coder-480b-a35b-instruct` | 256K    | `Code`      | ~3.0s   |

### [Yolo-Auto](https://yolo-auto.com)

Yolo-Auto is a bare-metal inference provider running a single Qwen3.6-35B-A3B model through an OpenAI-compatible endpoint. The free tier offers 15 requests per day for integration testing — enough to verify your tooling works before upgrading to the flat-rate unlimited plan. No credit card required. As they promised, more models are coming soon. Yolo-Auto currently has 1 model verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ⚠️              |

🎁 **Free Tier Quota:** 15 RPD

🔗 **Base URL:** `https://yolo-auto.com/v1`

✅ **Verified:** August 9, 2026
| Free Model        | Context | Best For  | Latency |
| :---------------- | ------- | --------- | ------- |
| `qwen3.6-35b-a3b` | 128K    | `General` | ~3.6s   |

### [Z.AI (Zhipu AI)](https://z.ai)

Zhipu AI is a Chinese AI company developing the GLM family of foundation models. The free tier offers two flash-variant models with a concurrency limit of 1 request at a time and unlimited daily tokens — practical for lightweight scripting and quick edits, but the single-concurrent cap makes sustained coding sessions impractical. Z.AI currently has 2 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 1 Concurrent Request / Uncapped TPD

🔗 **Base URL:** `https://api.z.ai/api/paas/v4`

✅ **Verified:** August 9, 2026
| Free Model      | Context | Best For   | Latency |
| :-------------- | ------- | ---------- | ------- |
| `glm-4.7-flash` | 128K    | `General`  | ~2.4s   |
| `glm-4.5-flash` | 128K    | `Fallback` | ~0.7s   |

### [Zylo API](https://zyloai.net)

Zylo API is a unified inference hub providing access to models from DeepSeek, NVIDIA, Mistral, MiniMax, Qwen, GLM, and Google through an OpenAI-compatible endpoint. The free tier offers 10 RPM with 7,200 requests and 200,000 tokens per day — no credit card required. Zylo API currently has 7 models verified.

| Capability | Tool Calls | Schema | Error Handling | Rate Limit Safe |
| :--------- | :--------- | :----- | :------------- | :-------------- |
| **Status** | ✅          | ✅      | ✅              | ✅               |

🎁 **Free Tier Quota:** 10 RPM / 7,200 RPD / 200,000 TPD

🔗 **Base URL:** `https://api.zyloai.net/v1`

✅ **Verified:** August 9, 2026
| Free Model                | Context | Best For    | Latency |
| :------------------------ | ------- | ----------- | ------- |
| `deepseek-v4-flash`       | 128K    | `Reasoning` | ~1.5s   |
| `glm-5.2`                 | 128K    | `General`   | ~2.0s   |
| `gpt-oss`                 | 128K    | `General`   | ~1.0s   |
| `gpt-oss-20b`             | 128K    | `Code`      | ~0.9s   |
| `minimax-m3`              | 1M      | `General`   | ~1.1s   |
| `nemotron-3-nano-30b-a3b` | 128K    | `General`   | ~1.0s   |
| `nemotron-3-ultra`        | 128K    | `General`   | ~2.1s   |

---

## Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details.

[^1]: Models are verified through live API calls to each provider's free-tier endpoint. The `scripts/verify.py` script automates this check: set the provider's API key as an environment variable and run it to confirm the model responds. Latency figures are measured from request to first token under typical network conditions and may vary. A model is removed if its provider paywalls it, deprecates it, or changes its free-tier terms. This list is updated regularly but is not a guarantee of continued availability.
