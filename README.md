# Awesome Free BYOK Models 🚀

[![License](https://img.shields.io/badge/license-CC0--1.0-white)](LICENSE.md)
[![API Provider Count](https://img.shields.io/badge/providers-18-8A2BE2)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

> ⏰ **Last Verified: June 14, 2026** - All Models are Verified from their API Providers.

A curated list of the **best high-performance**, **free-tier AI models** you can use to **supercharge your coding setup** without paying for expensive monthly subscriptions nor being "woke up" from a Trial Credit Expiry.

By using a **Bring Your Own Key (BYOK)** approach, you can plug your free API keys directly into coding tools like **VS Code extensions, terminal assistants, or code editors**, or use it in your **Coding Projects**. It doesn't even require a **credit card** for the best models!

> 💡 **Pro tip:** Free tiers rotate often. If a model hits rate limits, switch to another — there's always a backup in this list. 
> **Always verify** current quotas on the provider's console before building workflows.

## 📋 Contents

- [🏢 The Best 3 API Providers](#the-best-3-api-providers)
- [🏆 The Top 10 Recommended Free Models](#the-top-10-recommended-free-models)
- [📂 Individual Provider Showcases](#the-deep-dive-individual-provider-showcases)
  - [✅ AION Labs](#aion-labs-models)
  - [⚡ Auriko](#auriko-models)
  - [🧠 Cerebras AI](#cerebras-ai-models)
  - [☁️ Cloudflare Workers AI](#cloudflare-workers-ai-models)
  - [🟢 Cohere AI](#cohere-ai-models)
  - [🐙 GitHub Models](#github-models-models)
  - [🌐 Google Gemini](#google-gemini-models)
  - [⚡ Groq](#groq-api-models)
  - [🤗 Hugging Face Inference API](#hugging-face-inference-api-models)
  - [🏎️ Kilo Code](#kilo-code-models)
  - [🪐 LLM7.IO](#llm7io-models)
  - [🍊 Mistral AI](#mistral-ai-models)
  - [🎭 Mixlayer](#mixlayer-models)
  - [🔮 MorphLLM](#morphllm-models)
  - [🦙 Ollama Cloud](#ollama-cloud-models)
  - [🌐 OpenRouter](#openrouter-models)
  - [🎨 Pollinations AI](#pollinations-ai-models)
  - [🌀 SambaNova AI](#sambanova-ai-models)
- [CONTRIBUTING](#contributing)
- [LICENSE](#license)

<a id="the-best-3-api-providers"></a>
## 🏢 The Best 3 API Providers

If you are signing up for free accounts to get API keys, these are the **three best platforms** to look at first.

| Provider | The Simple Vibe | Why It Matters For You |
| :--- | :--- | :--- |
| **Groq** | Speedy Accurate | Code prints out on your screen instantly. If you hate waiting for an AI to finish typing, this is your go-to. |
| **SambaNova** | Hardware Speed | Proprietary RDU architecture removes traditional GPU bottlenecks, delivering incredibly high throughput for massive models. |
| **Mistral AI** | Clean & Efficient | Builds models that punch above their weight class with exceptionally clean instruction following and compact, efficient execution profiles. |

---

<a id="the-top-10-recommended-free-models"></a>
## 🏆 The Top 10 Recommended Free Models

The absolute best free models available right now, ranked by how well they handle **daily coding tasks** and **projects that require a working model**. This does **NOT** include vision models — all models here are only for text-out models.

| Rank | Model Name | Host Provider | Free Tier Quota | The Simple Reason to Choose It |
| :--- | :--- | :--- | :--- | :--- |
| **1** 🏆 | `openai/gpt-oss-120b` | **Groq** | 14,400 RPD / 18,000 TPM | **For All Tasks.** The undisputed champion. Writes incredibly clean code, never hits rate-limit walls, and responds almost instantly. |
| **2** 🥈 | `DeepSeek-V3.1` | **SambaNova** | 20 RPM + credits | **For Agentic Pipelines.** A massive hybrid mixture model on SambaNova's RDU architecture — blazing-fast inference with elite reasoning, optimized as a background planner for multi-step agent actions. |
| **3** 🥉 | `qwen/qwen3-32b` | **Groq** | 14,400 RPD / 18,000 TPM | **For Code.** Phenomenal code generation that dumps into your editor at lightning speed. The `<think>` preamble is a minor trade-off for its coding depth. |
| **4** | `DeepSeek-V3.2` | **SambaNova** | 20 RPM + credits | **For Deep Reasoning.** The pinnacle of hardware-optimized reasoning on SambaNova's infrastructure — near-instant token speeds with elite multi-file architectural analysis. |
| **5** | `mistral-code-agent-latest` | **Mistral AI** | 30 RPM + daily credits | **For Agentic Coding.** Purpose-built for autonomous agents with native tool use, structured JSON outputs, and multi-step coding workflows. |
| **6** | `models/gemini-3.1-flash-lite` | **Google Gemini** | 15 RPM / 500 RPD | **For Quick Tasks.** Lightning-fast with ~500 RPD free tier — the only Gemini model with enough quota for sustained agentic triaging. |
| **7** | `mistral-large-2512` | **Mistral AI** | 30 RPM + daily credits | **For Instruction Following.** Top-tier multilingual reasoning with strict adherence to complex system prompts and massive file contexts. |
| **8** | `gpt-oss-120b` | **Cerebras** | 5 RPM + credits | **For Speed.** The same 117B MoE champion running on Cerebras' wafer-scale engine — sub-second responses for rapid-fire coding loops. |
| **9** | `zai-glm-4.7` | **Cerebras** | 5 RPM + credits | **For Large Context.** 131K context window optimized for long-horizon agentic coding — handles massive project contexts at blazing Cerebras speeds. |
| **10** | `codestral-latest` | **Mistral AI** | 30 RPM + daily credits | **For Code Completions.** Built from the ground up for programming — flies through auto-completions and single-file inline edits across dozens of languages. |

---

<a id="the-deep-dive-individual-provider-showcases"></a>
## 📂 The Deep-Dive: Individual Provider Showcases

These tables break down the notable free models available **(Capped at 20 Best Free Models)** within each provider's ecosystem. Ratings are based on how well they handle **real-world development** demands like typing speed, following instructions, and not getting confused by **large projects**, all by a point of view to the Provider's Quota, Rate Limits, and Context Windows.

<a id="aion-labs-models"></a>
### ✅ [AION Labs](https://www.aionlabs.ai) Models (5)
AION Labs provides storytelling-optimized models through an OpenAI-compatible API. The free tier offers 20,000 tokens/day and 15 RPM with no credit card required — a solid option if you need a daily token allowance for lightweight coding and creative tasks.

**Base URL:** `https://api.aionlabs.ai/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `aion-labs/aion-2.5` | ⭐⭐⭐⭐⭐ | **BEST.** Handles general tasks with clean, direct output and no thinking preamble. Feels surprisingly smooth for a storytelling-optimized model — the best pick on AION Labs. |
| `aion-labs/aion-2.0` | ⭐⭐⭐⭐☆ | Delivers the same clean output as 2.5 but with slightly more latency between turns. Still a reliable option for everyday use without preamble noise. |
| `aion-labs/aion-rp-llama-3.1-8b` | ⭐⭐⭐⭐☆ | Responds faster than any other AION model. Handles lightweight tasks instantly, but the 8B cap limits depth on complex coding or multi-file reasoning. |
| `aion-labs/aion-1.0-mini` | ⭐⭐⭐☆☆ | Coding/reasoning specialist (distilled DeepSeek-R1) but wraps every response in a `<think>` preamble. Sunset June 20, 2026 — replaced by the cleaner aion-2.0. |
| `aion-labs/aion-1.0` | ⭐⭐⭐☆☆ | Thinking preamble adds friction to every interaction. Sunset June 20, 2026 — reach for aion-2.0 instead for the same quality without the chatter. |

<a id="auriko-models"></a>
### ⚡ [Auriko](https://www.auriko.ai) Models (166)
Auriko is a unified API gateway providing access to 100+ models from top providers (OpenAI, Anthropic, DeepSeek, Google, xAI, Moonshot, and more) through a single OpenAI-compatible endpoint. The free tier offers 1,000 Platform RPM and 10,000 BYOK requests/month with zero inference markup — no credit card required. Access to every model on the platform at provider cost.

At the time of testing, Auriko AI has **166 Models**... so we made the Top 20 of Auriko's Best Models.

**Base URL:** `https://api.auriko.ai/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `o3-2025-04-16` | ⭐⭐⭐⭐⭐ | **BEST.** Top-tier reasoning model — handles multi-file architecture and complex debugging with zero preamble. The strongest coding pick on Auriko for the hardest problems. |
| `claude-opus-4-7` | ⭐⭐⭐⭐⭐ | The fastest Claude Opus variant — handles deep reasoning and code generation with Anthropic's signature precision. No preamble, just direct answers. |
| `deepseek-v3.2` | ⭐⭐⭐⭐⭐ | Elite reasoning workhorse trusted across every provider. Delivers clean output for multi-file analysis and agentic planning without extra chatter. |
| `gpt-5-2025-08-07` | ⭐⭐⭐⭐⭐ | OpenAI's GPT-5 flagship — handles every coding task with zero preamble. Elite intelligence without any friction. |
| `gpt-4.1-2025-04-14` | ⭐⭐⭐⭐⭐ | Blazing fast with strong general coding capability. A top-tier daily driver that responds instantly with clean output. |
| `claude-sonnet-4-20250514` | ⭐⭐⭐⭐☆ | Latest Sonnet — balances speed and depth well. Handles complex instructions reliably with clean response. |
| `deepseek-v4-flash` | ⭐⭐⭐⭐☆ | Latest DeepSeek flash variant — strong reasoning depth with fast inference. |
| `o4-mini-2025-04-16` | ⭐⭐⭐⭐☆ | Latest reasoning model from OpenAI — compact but capable. Handles logic-heavy tasks cleanly. |
| `qwen-3-coder-480b-a35b-instruct` | ⭐⭐⭐⭐☆ | Purpose-built 480B code model — tackles the hardest debugging sessions. The dedicated coder on Auriko. |
| `gpt-5.2-2025-12-11` | ⭐⭐⭐⭐☆ | Latest GPT-5 point release. Fast and reliable across every task. |
| `gpt-5-chat-latest` | ⭐⭐⭐⭐☆ | The chat-optimized GPT-5 variant. Handles conversational coding naturally. |
| `gpt-5.4-2026-03-05` | ⭐⭐⭐⭐☆ | Latest GPT generation. Strong general intelligence with clean, direct output. |
| `claude-sonnet-4-6` | ⭐⭐⭐⭐☆ | Latest Sonnet 4.6 — handles creative coding and complex prompts with Anthropic's clear response style. |
| `gpt-5.3-chat-latest` | ⭐⭐⭐⭐☆ | Latest chat-optimized GPT. Clean responses for everyday coding. |
| `gpt-5.1-chat-latest` | ⭐⭐⭐⭐☆ | Handles general tasks with zero preamble. Reliable daily driver. |
| `gpt-5.4-mini-2026-03-17` | ⭐⭐⭐⭐☆ | Compact GPT-5.4 — handles lightweight tasks efficiently without sacrificing response quality. |
| `gpt-5-mini-2025-08-07` | ⭐⭐⭐⭐☆ | GPT-5 compact variant with clean output. Great for high-volume simple tasks where cost matters. |
| `gpt-5.4-nano-2026-03-17` | ⭐⭐⭐⭐☆ | The nano tier — blazing fast. Handles syntax checks and quick edits almost instantly. |
| `groq-4.20-0309-non-reasoning` | ⭐⭐⭐⭐☆ | xAI's fastest — clean, direct output for rapid-fire coding loops where speed is everything. |
| `o3-mini-2025-01-31` | ⭐⭐⭐☆☆ | Older reasoning model — still capable with clean output, but trails newer o3/o4 variants on complex architecture analysis. |


<a id="cerebras-ai-models"></a>
### 🧠 [Cerebras AI](https://cloud.cerebras.ai) Models (2)
Cerebras AI is defined by its **Wafer-Scale Engine (WSE) technology**, integrating memory, compute, and interconnects onto a single silicon wafer — solving the "memory wall" that throttles inference speed. The free tier offers replenishable credits with industry-leading throughput (2,500+ tokens/second).

**Base URL:** `https://api.cerebras.ai/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `gpt-oss-120b` | ⭐⭐⭐⭐☆ | **For All Tasks.** The same 117B MoE flagship that dominates on Groq. Delivers sub-second responses on Cerebras' wafer-scale architecture with solid reliability across standard developer workflows. |
| `zai-glm-4.7` | ⭐⭐⭐⭐☆ | A 131K context window model optimized for rapid agentic coding. Handles modular code snippets efficiently at blazing speeds — ideal for large-context agent loops and multi-file reasoning tasks. |


<a id="cloudflare-workers-ai-models"></a>
### ☁️ [Cloudflare Workers AI](https://dash.cloudflare.com) Models (25)
Cloudflare Workers AI runs models on Cloudflare's global edge network using serverless GPUs. The free tier offers 10,000 requests/day shared across all models with near-zero latency from edge locations worldwide.

At the time of testing, Cloudflare Workers AI has **25 Models**... so we made the Top 20 of Cloudflare Workers' Best Models.

**Base URL:** `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions` (replace `{account_id}` with your Cloudflare account ID)

> ⚠️ **Two API paths:** The `/chat/completions` endpoint takes standard `"messages"` (OpenAI-compatible). The legacy `/run/{model}` endpoint uses `"prompt"` instead — make sure your tool targets the right one.

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `@cf/qwen/qwen2.5-coder-32b-instruct` | ⭐⭐⭐⭐⭐ | **BEST.** Handles generation, completion, and debugging without preamble noise. Sits on Cloudflare's edge network so it responds instantly — the only dedicated code model here, so start with this. |
| `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | ⭐⭐⭐⭐☆ | **REASONING ONLY** Handles complex logic at edge speed. You can rely on it for instruction-heavy prompts where you need real depth without waiting. |
| `@cf/openai/gpt-oss-120b` | ⭐⭐⭐⭐☆ | Handles tough debugging and architectural questions with massive parameter headroom. You can rely on it for the hardest problems where smaller models hit their ceiling. |
| `@cf/qwen/qwen3-30b-a3b-fp8` | ⭐⭐⭐⭐☆ | Feels like a full-size model despite the tiny active footprint — responses come fast without sacrificing substance. Good for everyday coding where you want both speed and depth. |
| `@cf/google/gemma-4-26b-a4b-it` | ⭐⭐⭐⭐☆ | Delivers clean, thoughtful responses that feel fresh from Google's latest research. You can rely on it when response quality matters more than raw speed. |
| `@cf/zai-org/glm-4.7-flash` | ⭐⭐⭐⭐☆ | Handles rapid-fire coding calls without noticeable lag. Feels snappy even under heavy use — ideal when every millisecond counts in your workflow. |
| `@cf/meta/llama-4-scout-17b-16e-instruct` | ⭐⭐⭐⭐☆ | Produces clean, direct answers without excess chatter. You can rely on it for straightforward coding help where you want quality without the overhead of a full-parameter model. |
| `@cf/moonshotai/kimi-k2.7-code` | ⭐⭐⭐⭐☆ | **LONG CONTEXT ONLY** Handles long-file analysis and project-wide refactors that smaller contexts can't fit. Feels like having a model that actually reads your whole codebase. |
| `@cf/nvidia/nemotron-3-120b-a12b` | ⭐⭐⭐⭐☆ | Handles complex reasoning that demands extra depth. You can rely on it when you need a model that keeps digging rather than giving up early. |
| `@cf/aisingapore/gemma-sea-lion-v4-27b-it` | ⭐⭐⭐⭐☆ | Handles multilingual and coding tasks with surprising competence for its size — feels like a bigger model than it is. |
| `@cf/meta/llama-3.2-3b-instruct` | ⭐⭐⭐⭐☆ | **SPEED ONLY** Handles syntax checks and inline completions before you finish typing. Feels instant for those quick sanity-check moments. |
| `@cf/openai/gpt-oss-20b` | ⭐⭐⭐⭐☆ | Handles daily coding tasks dependably without burning through quota. Feels like a practical workhorse you can reach for without guilt. |
| `@cf/meta/llama-3.2-1b-instruct` | ⭐⭐⭐⭐☆ | You can rely on it for trivial classification or absolute minimum compute tasks. It's the smallest model that still passes verification — use it when you want to save every resource. |
| `@cf/mistralai/mistral-small-3.1-24b-instruct` | ⭐⭐⭐☆☆ | Feels sluggish for tight coding loops — capable in conversation but you'll notice the lag during quick edits. |
| `@cf/meta/llama-3.1-8b-instruct-fp8` | ⭐⭐⭐☆☆ | Gets the job done but adds unnecessary preamble around answers. You'll find yourself trimming its responses more than you'd like. |
| `@cf/qwen/qwq-32b` | ⭐⭐⭐☆☆ | Handles logic puzzles well with chain-of-thought, but you have to sit through the thinking preamble before reaching the answer. Feels like waiting for a slow thinker. |
| `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | ⭐⭐⭐☆☆ | **REASONING ONLY** Its <think> blocks are useful when you want to peek at its reasoning, but frustrating when you just want the answer fast without the internal monologue. |
| `@cf/meta/llama-3.2-11b-vision-instruct` | ⭐⭐⭐☆☆ | **VISION ONLY** Handles multimodal tasks competently, but it's verbose and overkill if you only need text code help. You'll need a Model Agreement before you can use it. |
| `@cf/ibm-granite/granite-4.0-h-micro` | ⭐⭐⭐☆☆ | Handles basic tasks but struggles to be concise — you'll find yourself trimming its output often. Only worth exploring if you're specifically evaluating IBM Granite. |
| `@cf/google/gemma-7b-it-lora` | ⭐⭐⭐☆☆ | Handles tasks competently but feels dated next to the Gemma v4 entries. You'll notice it's more verbose and less polished in practice. |


<a id="cohere-ai-models"></a>
### 🟢 [Cohere AI](https://dashboard.cohere.com) Models (11)
Cohere focuses on enterprise-grade NLP with their Command model family — built for RAG, tool use, and coding workflows. The free API tier offers replenishable credits with daily resets, and nearly every model delivers sub-second responses.

**Base URL:** `https://api.cohere.com/v2`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `command-a-03-2025` | ⭐⭐⭐⭐⭐ | **BEST.** Cohere's flagship model. Blazing fast with clean, direct command execution — ideal for agentic tool-use pipelines and structured outputs. |
| `command-r-plus-08-2024` | ⭐⭐⭐⭐☆ | High-capability reasoning engine. Reliable for complex multi-step logic and architectural analysis with strong output quality. |
| `command-r-08-2024` | ⭐⭐⭐⭐☆ | Fast general-purpose workhorse. Handles scripting, terminal commands, and single-file edits with consistent formatting. |
| `c4ai-aya-vision-32b` | ⭐⭐⭐⭐☆ | 32B vision-language model. Handles both code and visual context — useful for UI-to-code workflows. |
| `command-a-vision-07-2025` | ⭐⭐⭐⭐☆ | Vision variant of Command A. Process screenshots and diagrams alongside code without switching contexts. |
| `command-r7b-12-2024` | ⭐⭐⭐⭐☆ | Compact 7B that is great for rapid-fire completions with minimal overhead and consistent output. |
| `command-r7b-arabic-02-2025` | ⭐⭐⭐⭐☆ | Arabic-optimized 7B variant. Clean responses for Arabic technical documentation and bilingual codebases. |
| `command-a-translate-08-2025` | ⭐⭐⭐☆☆ | Translation-optimized model. Works for code but specialized for multilingual text, limiting general coding utility. |
| `command-a-reasoning-08-2025` | ⭐⭐⭐☆☆ | Reasoning-focused variant. Minimal outputs suit internal chain-of-thought, but lack of direct answers hurts in agentic use. |
| `c4ai-aya-expanse-32b` | ⭐⭐⭐☆☆ | 32B multilingual model that over-answers — "READY. Is there anything else I can" adds noise in prompt chains. |
| `command-a-plus-05-2026` | ⭐⭐☆☆☆ | Plus-tier variant with empty responses. Unreliable output makes it risky for agentic pipelines despite the speed. |


<a id="github-models-models"></a>
### 🐙 [GitHub Models](https://github.com/marketplace/models) Models (4)
GitHub Models provides free API access to models from OpenAI, Meta, Mistral, and others using your existing GitHub account — no new signup needed. Free tier quotas are modest (request-based limits), making it best for prototyping and personal projects.

**Base URL:** `https://models.inference.ai.azure.com`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `gpt-4o-mini` | ⭐⭐⭐⭐☆ | **BEST.** OpenAI's compact flagship. Clean responses and broad language support — the safest pick on GitHub Models for everyday coding. |
| `Meta-Llama-3.1-405B-Instruct` | ⭐⭐⭐⭐☆ | A 405B giant with clean output. Exceptional reasoning depth for system design and architectural analysis at zero cost. |
| `gpt-4o` | ⭐⭐⭐☆☆ | Full OpenAI flagship but adds unnecessary markdown to simple outputs. Excellent intelligence, but verbosity clutters agent pipelines. |
| `Meta-Llama-3.1-8B-Instruct` | ⭐⭐⭐☆☆ | Fast 8B model but verbose for its size class, which is Decent for bash command lookups and syntax checks. |


<a id="google-gemini-models"></a>
### 🌐 [Google Gemini](https://aistudio.google.com) Models (11)
Gemini offers large context windows on paper, but the free tier's **rate limits vary by model** — Flash-lite variants enjoy ~500 RPD, while standard models can be as low as 20 RPD. Use Gemini for quick, targeted tasks and single-file edits — not marathon sessions.

**Base URL:** `https://generativelanguage.googleapis.com/v1beta`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `models/gemini-3.1-flash-lite` | ⭐⭐⭐⭐⭐ | **BEST.** The new baseline. Lightning-fast with responsive, no-fuss outputs. Handles daily coding, terminal commands, and single-file edits comfortably thanks to ~500 RPD on the free tier. |
| `models/gemma-4-31b-it` | ⭐⭐⭐⭐☆ | A highly responsive and incredibly smart model. The only catch is that it occasionally "overthinks" simple instructions—instead of just giving you the direct answer, it might type out its internal rule-checking steps first. |
| `models/gemma-4-26b-a4b-it` | ⭐⭐⭐⭐☆ | A compact Gemma variant with solid reasoning depth. Slightly slower to respond than its 31b sibling, but delivers clean, structured outputs for general development tasks. |
| `models/gemini-3.5-flash` / `models/gemini-flash-latest` | ⭐⭐⭐☆☆ | Next-generation flash model with improved reasoning over prior flash variants. Fast responses and strong coding capability, but standard flash rate limits (~20 RPD) prevent sustained agentic use. |
| `models/gemini-3.1-flash-lite-preview` | ⭐⭐⭐☆☆ | A preview snapshot of the BEST model. Nearly identical speed and quality, but being experimental means its behavior can shift when Google updates it behind the scenes, making it unreliable for consistent agentic use despite ~500 RPD. |
| `models/gemini-3-flash-preview` | ⭐⭐⭐☆☆ | Outstanding intelligence for a preview model. It handles deep reasoning and large contexts beautifully, but because it is an experimental playground model with tight rate limits (as low as 20 RPD), it's impractical for sustained agentic use. |
| `models/gemini-2.5-flash` | ⭐⭐⭐☆☆ | A solid, reliable backup option that handles standard context sizes perfectly. It only slips to 3 stars because the newer Gemini 3 series leaves it in the dust when it comes to tracking complex coding logic. |
| `models/gemini-flash-lite-latest` | ⭐⭐⭐☆☆ | **LIGHT SCRIPTING ONLY.** An incredibly fast, bare-bones lite variant. Perfect for rapid terminal lookups and quick syntax checks, but lacks the depth for multi-file project work. |
| `models/gemini-2.5-flash-lite` | ⭐⭐☆☆☆ | **LIGHT SCRIPTING ONLY.** It is incredibly fast and lightweight for basic tasks, but its older reasoning core means it gets confused easily if you paste in a long list of complex terminal errors. |
| `models/gemini-robotics-er-1.6-preview` | ⭐⭐☆☆☆ | A fascinating experimental model built for physical task automation and robotics logic. While it technically works for text, using it for daily coding is a waste of time since it isn't optimized for programming syntax. |


<a id="groq-api-models"></a>
### ⚡ [Groq API](https://console.groq.com) Models (12)
Groq is famous for providing the **absolute lowest streaming latency** in the API market, outrunning traditional cloud providers by a massive margin. The free tier offers 30 RPM with replenishable daily credits — no credit card needed. If you want a setup where your terminal files patch instantly without the typical spinning wheel delay, this is your go-to.

**Base URL:** `https://api.groq.com/openai/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `openai/gpt-oss-120b` | ⭐⭐⭐⭐⭐ | **BEST.** This is the undisputed champion of the list. It feels completely seamless to use because it rarely gets confused by tricky code logic, never hits frustrating rate-limit walls, and types so fast you barely have time to read along. |
| `qwen/qwen3-32b` | ⭐⭐⭐⭐☆ | **CODE COMPLETION ONLY.** A phenomenal option if you are writing complex code blocks. The only catch is that it insists on "thinking out loud" for a brief moment before it types, which can feel slightly laggy if you just want a quick answer. |
| `llama-3.3-70b-versatile` | ⭐⭐⭐⭐☆ | **GENERAL CHAT ONLY.** Incredibly dependable for standard developer conversations and brainstorming. It is a stubborn rule-follower that does exactly what you ask, though it lacks that extra specialized edge for high-level programming loops. |
| `openai/gpt-oss-20b` | ⭐⭐⭐⭐☆ | **SOLID COMPANION.** A highly capable, mid-sized model that shares the same excellent coding DNA as its 120b big brother. It lacks the massive reasoning depth needed for highly complex systems programming, but it is lightning-fast for standard tasks. |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ⭐⭐⭐☆☆ | **TEXT ONLY.** It handles medium-sized tasks well enough, but it has a habit of overthinking simple prompts. It tends to get overly wordy and chatty when a direct, simple response would have been much better. |
| `groq/compound` | ⭐⭐⭐☆☆ | Great for a quick, single-turn question when you are stuck in the terminal, but it simply doesn't have the memory or the brainpower to track a project that involves multiple files. |
| `llama-3.1-8b-instant` | ⭐⭐⭐☆☆ | Fun to use for tiny, rapid-fire edits because it responds like a lightning bolt. However, if you ask it to write a long script, it often gets tired toward the end and cuts off final characters or punctuation. |
| `groq/compound-mini` | ⭐⭐☆☆☆ | **TERMINAL QUICK PICKS.** A stripped-down version of the standard compound model. It is incredibly lightweight and fast, but it is purely meant for single-sentence syntax checks or basic bash command lookups. |
| `openai/gpt-oss-safeguard-20b` | ⭐⭐☆☆☆ | **OVERLY CAUTIOUS.** While it has the core architecture to be a good developer assistant, its built-in safety filters make it incredibly paranoid. It will frequently refuse to generate standard code blocks if it suspects a security risk. |
| `allam-2-7b` | ⭐⭐☆☆☆ | **TRANSLATION ONLY.** Fantastic if you are doing specific language translation work, but it is completely out of its depth here. Try to use it for coding, and it will quickly lose track of what you are building. |
| `meta-llama/llama-prompt-guard-2-86m` | ⭐☆☆☆☆ | **SECURITY MONITORING ONLY (LARGE).** Do not let the "Llama" name fool you—this is a behind-the-scenes injection detection tool, not a coding buddy. Asking it a standard question will just get you back a random decimal string. |
| `meta-llama/llama-prompt-guard-2-22m` | ⭐☆☆☆☆ | **SECURITY MONITORING ONLY (MINI).** Even smaller than the 86m version, this model exists purely to analyze inputs for malicious prompt attacks instantly. It cannot converse, write logic, or follow standard user instructions. |


<a id="hugging-face-inference-api-models"></a>
### 🤗 [Hugging Face Inference API](https://huggingface.co/inference-api) Models (~80)
Hugging Face's free Inference API gives you access to thousands of community-hosted models with OpenAI-compatible endpoints. The free tier offers replenishable credits with daily resets. With models ranging from 3B to 1T parameters, this is the most diverse single provider on the list.

At the time of testing, Hugging Face has **approximately 80 Models**... so we made the Top 20 of Hugging Face's Best Models.

**Base URL:** `https://router.huggingface.co/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `Qwen/Qwen3-Coder-Next` | ⭐⭐⭐⭐⭐ | **BEST.** Handles generation, completion, and debugging without preamble noise. Rarely gets confused by tricky code logic and delivers clean output every time — the strongest coding model on Hugging Face. |
| `Qwen/Qwen3-Coder-480B-A35B-Instruct` | ⭐⭐⭐⭐⭐ | Tackles the hardest debugging and architecture problems with ease. The largest purpose-built code model available — use it when nothing else can handle the complexity. |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct` | ⭐⭐⭐⭐⭐ | Feels like running a 30B model on a 3B budget. You get deep, structured reasoning without the latency penalty — ideal for iterative coding sessions. |
| `meta-llama/Llama-3.3-70B-Instruct` | ⭐⭐⭐⭐⭐ | Follows complex instructions precisely on the first try. You barely have to re-prompt — it just gets what you want and responds cleanly. |
| `meta-llama/Llama-3.1-70B-Instruct` | ⭐⭐⭐⭐⭐ | You can rely on it for any task without second-guessing the output. The workhorse that keeps delivering even under heavy use. |
| `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4` | ⭐⭐⭐⭐⭐ | Feels like talking to a model that's far too big to be free. Clean, precise output on every turn — NVIDIA knocked it out of the park. |
| `deepseek-ai/DeepSeek-V3.2` | ⭐⭐⭐⭐⭐ | Handles multi-file architecture tasks without losing track of context. One of the smartest models available — you trust it with the hard stuff. |
| `deepseek-ai/DeepSeek-V3.1` | ⭐⭐⭐⭐⭐ | Slightly faster than V3.2 with the same elite reasoning depth — you barely wait for answers even on complex planning workflows. |
| `deepcogito/cogito-671b-v2.1` | ⭐⭐⭐⭐⭐ | Feels like having an unfair advantage. The sheer depth of its reasoning is shocking — use it when you need the absolute best answer. |
| `google/gemma-4-26B-A4B-it` | ⭐⭐⭐⭐⭐ | Responds faster than its size suggests with surprisingly clean, direct output. Google's sparse architecture shines in everyday use. |
| `Qwen/Qwen2.5-72B-Instruct` | ⭐⭐⭐⭐⭐ | A reliable fallback that handles most coding tasks competently. Broad capability without the massive overhead — never lets you down. |
| `Qwen/Qwen3-235B-A22B-Instruct-2507` | ⭐⭐⭐⭐⭐ | Feels like having 235B parameters at your fingertips but only paying for 22B. Immense capacity with snappy response times. |
| `CohereLabs/c4ai-command-a-03-2025` | ⭐⭐⭐⭐⭐ | You can rely on it for tool-calling workflows because it follows structured instructions without deviating. Enterprise-grade reliability in a free API. |
| `inclusionAI/Ling-2.6-1T` | ⭐⭐⭐⭐⭐ | Feels like you're cheating the system. A trillion-parameter model for free — use it when you need the broadest possible knowledge and reasoning. |
| `swiss-ai/Apertus-70B-Instruct-2509` | ⭐⭐⭐⭐⭐ | Delivers Llama-class reasoning quality without any of the attitude. Solid and dependable for any general-purpose task. |
| `deepseek-ai/DeepSeek-R1` | ⭐⭐⭐⭐⭐ | Walks through its reasoning step by step without cluttering the output. You can follow its logic and trust its conclusions. |
| `openai/gpt-oss-120b` | ⭐⭐⭐⭐☆ | Proven across every provider — reliable as ever with clean output. You know exactly what you're getting every single time. |
| `MiniMaxAI/MiniMax-M3` | ⭐⭐⭐⭐☆ | The fastest responder on Hugging Face alongside GPT-OSS. You get answers before you finish typing — clean and efficient. |
| `zai-org/GLM-4.7` | ⭐⭐⭐⭐☆ | Handles high-volume work without slowing down. Optimized for throughput — you can hammer it all day and it keeps responding. |
| `Qwen/Qwen3.6-35B-A3B` | ⭐⭐⭐⭐☆ | Feels like the most efficient model on the list. You get modern Qwen quality — perfect for rapid iteration. |


<a id="kilo-code-models"></a>
### 🏎️ [Kilo Code](https://app.kilo.ai) Models (12)
Kilo Code is a coding-agent platform that proxies free models from OpenRouter, NVIDIA, Poolside, and others through a single API key. The free tier offers generous replenishable credits with no hard daily cap — a solid Swiss-army-knife provider that gives you access to a diverse model pool (nano to 550B) through one endpoint.

**Base URL:** `https://api.kilo.ai/api/gateway`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `openrouter/owl-alpha` | ⭐⭐⭐⭐⭐ | **BEST.** Handles general reasoning without any preamble noise. You get direct, clean answers every time without having to wade through thinking blocks — the safest pick on Kilo Code. |
| `nex-agi/nex-n2-pro:free` | ⭐⭐⭐⭐⭐ | Fast and direct with no extra chatter — you can drop it into an agent pipeline and it'll respond immediately without wasting tokens on preamble or filler. |
| `kilo-auto/small` | ⭐⭐⭐⭐⭐ | Kilo's own auto-routed small model, biased for clean output. When you don't know what to pick, it reliably gives you clean answers without any fuss. |
| `poolside/laguna-xs.2:free` | ⭐⭐⭐⭐☆ | Purpose-built for software development — it handles code edits quickly and stays out of your way. Great for rapid inline completions where you don't want extra chatter. |
| `poolside/laguna-m.1:free` | ⭐⭐⭐⭐☆ | A step up in capacity — when the XS variant isn't quite enough for tricky code edits, this one gives you the headroom without slowing you down. |
| `stepfun/step-3.7-flash:free` | ⭐⭐⭐⭐☆ | A solid general-purpose pick — it handles everyday coding tasks without surprises. You can trust it to just work when you need a quick edit or refactor. |
| `kilo-auto/free` | ⭐⭐⭐⭐☆ | Kilo's default auto-routed model — when you're not sure which model to reach for, this one gives you clean output without needing to think about it. |
| `openrouter/free` | ⭐⭐⭐⭐☆ | OpenRouter's free routing routes through a wide model pool — quality varies but usually lands on something that works. A decent fallback when other models are exhausted. |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | ⭐⭐⭐☆☆ | A 550B monster — raw power is there, but you'll spend as much time scrolling past preamble as reading the actual answer. The constant prefix noise makes it frustrating for agentic use. |
| `nvidia/nemotron-3-super-120b-a12b:free` | ⭐⭐⭐☆☆ | 120B under the hood, but you'll fight through a long preamble every time you use it. The constant verbal overhead makes it impractical for agentic use despite the reasoning depth. |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ⭐⭐⭐☆☆ | Designed for reasoning tasks, not general coding — you'll get chain-of-thought analysis when you just wanted a simple answer. Limited utility unless you're specifically debugging logic. |
| `nvidia/nemotron-3.5-content-safety:free` | ⭐⭐☆☆☆ | **SAFETY MONITOR ONLY.** Not a coding assistant at all — asking it for code will just give you safety scores. Only useful as a filter for agent outputs. |


<a id="llm7io-models"></a>
### 🪐 [LLM7.IO](https://llm7.io) Models (4)
LLM7.IO is a rising inference provider serving open-weight models via Llama.cpp server with OpenAI-compatible endpoints. The free tier offers replenishable credits with no daily hard cap — a solid option if you want to test heavyweight models (up to 235B) on a simple API without commitment.

**Base URL:** `https://api.llm7.io/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `qwen3-235b` | ⭐⭐⭐⭐⭐ | **BEST.** Handles deep reasoning and complex coding without any preamble noise. You can throw multi-file architecture problems at it and it responds with clean, direct output every time — feels remarkably fluid for a 235B model. |
| `codestral-latest` | ⭐⭐⭐⭐☆ | **CODE COMPLETION ONLY.** Handles code generation smoothly for inline completions and file edits. You can rely on it as the strongest coding option here after Qwen, though it adds a brief preamble before each response. |
| `mistral-small-3.2` | ⭐⭐⭐☆☆ | Handles general chat and scripting adequately, but the verbose preamble makes it feel sluggish when you just want a quick answer. You can rely on it as a fallback when the top models are exhausted. |
| `devstral-small-2:24b` | ⭐⭐⭐☆☆ | Feels similar to the other Mistral models — the verbose preamble adds friction to every interaction. Handles straightforward tasks well enough, but trails the cleaner options on this list. |


<a id="mistral-ai-models"></a>
### 🍊 [Mistral AI](https://console.mistral.ai) Models (42)
Mistral AI is highly regarded for building models that punch far above their **parameter weight class**, with exceptionally clean instruction following and compact execution. The free tier offers replenishable credits with generous RPM limits. 

At the time of testing, Mistral has **42 Models** (with Aliases)... So we made the Top 20 of the Best Mistral AI Models (again, with Aliases).

**Base URL:** `https://api.mistral.ai/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `mistral-large-latest` / `mistral-large-2512` | ⭐⭐⭐⭐⭐ | **BEST.** Mistral's absolute crown jewel flagship engine. Top-tier multi-lingual reasoning, deep system architecture capabilities, and flawless focus across massive files. |
| `codestral-latest` / `codestral-2508` | ⭐⭐⭐⭐☆ | **CODE COMPLETION ONLY.** Built from the ground up for programmers. Flies through auto-completions and single-file inline edits across dozens of languages. |
| `mistral-code-latest` | ⭐⭐⭐⭐☆ | **CODE COMPLETION ONLY.** Dedicated code generation engine. Fast, precise completions across dozens of programming languages for inline editing workflows. |
| `mistral-code-fim-latest` | ⭐⭐⭐⭐☆ | **CODE COMPLETION ONLY.** Fill-in-Middle specialist. Designed for smart inline insertion within existing code blocks and contextual completions. |
| `mistral-code-agent-latest` | ⭐⭐⭐⭐⭐ | **BEST FOR AGENTS.** Purpose-built for autonomous agents with native tool use, structured JSON outputs, and multi-step coding workflows. |
| `mistral-medium-3.5` / `mistral-medium-3-5` | ⭐⭐⭐⭐☆ | Exceptional balance of price-to-performance. Highly responsive reasoning loops for structural software layouts, just missing 5 stars due to niche edge-case gaps. |
| `mistral-medium-3` | ⭐⭐⭐⭐☆ | Trusted, incredibly stable version of the Medium line. Keeps a rigid handle on instructions and delivers clean boilerplate code without empty chatter. |
| `mistral-medium-2604` | ⭐⭐⭐⭐☆ | A responsive iteration within the Medium family. Predictable execution flow and excellent at breaking down tricky structural bugs. |
| `devstral-medium-latest` | ⭐⭐⭐⭐☆ | **AGENT ROUTING ONLY.** Specialized, highly streamlined Medium variation optimized specifically to function inside automated developer continuous task loops. |
| `mistral-medium-latest` / `mistral-medium` | ⭐⭐⭐⭐☆ | The classic production model. Very dependable for everyday scripting queries and general developer workflows. |
| `mistral-small-latest` / `mistral-small-2603` | ⭐⭐⭐⭐☆ | Incredible lightweight architecture. Handles multi-turn logic with surprising depth and a punchy, direct tone that fits background execution perfectly. |
| `mistral-medium-2508` | ⭐⭐⭐☆☆ | Older point-release of the Medium framework. Outputs direct string text cleanly, though it lacks the optimization pass of the 3.x series. |
| `mistral-medium-2505` | ⭐⭐⭐☆☆ | Early build snapshot of Medium. Tends to use full-sentence prefix framing and has slightly slower throughput. |
| `mistral-small-2506` | ⭐⭐⭐☆☆ | An earlier snapshot of the Small ecosystem. Keeps syntax errors to a minimum but trails behind `2603` on processing velocity. |
| `devstral-latest` / `devstral-2512` | ⭐⭐⭐☆☆ | **AGENT ROUTING ONLY.** Tailored strictly for programmatic tool use and structured JSON schemas rather than standard conversational chat. |
| `ministral-14b-latest` / `ministral-14b-2512` | ⭐⭐⭐☆☆ | Nimble, edge-focused model. Remarkably capable of handling direct coding questions for its tight memory footprint. |
| `open-mistral-nemo` / `open-mistral-nemo-2407` | ⭐⭐⭐☆☆ | Classic community workhorse. Fast and flexible for low-complexity text filtering, but struggles on deep algorithmic logic. |
| `mistral-vibe-cli-fast` | ⭐⭐⭐☆☆ | **TERMINAL HELPER.** Built to fire off blistering, immediate single-turn replies for terminal flags or shell configuration checks. |
| `mistral-vibe-cli-latest` | ⭐⭐⭐☆☆ | **TERMINAL HELPER.** Standard CLI automation snapshot that favors explicit sentence explanations when breaking down commands. |
| `mistral-vibe-cli-with-tools` | ⭐⭐⭐☆☆ | **TERMINAL HELPER.** Version optimized to drop conversational prefixes entirely and focus strictly on returning raw executable bash tokens. |

<a id="mixlayer-models"></a>
### 🎭 [Mixlayer](https://www.mixlayer.com) Models (1)
Mixlayer is an inference platform for open-source AI models with an OpenAI-compatible API. The free tier offers `qwen/qwen3.5-4b-free` for prototyping with rate limits — no credit card required for the free model. A focused Qwen 3.5/3.6 catalog with tool calling and reasoning support.

**Base URL:** `https://models.mixlayer.ai/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `qwen/qwen3.5-4b-free` | ⭐⭐⭐⭐⭐ | **BEST.** The only free model on Mixlayer — handles prototyping and lightweight tasks at blazing speed. Clean, direct output with no preamble. Rate-limited but perfect for daily coding without spending a cent. |


<a id="morphllm-models"></a>
### 🔮 [MorphLLM](https://morphllm.com) Models (9)
MorphLLM hosts a diverse catalog of open-weight models (Qwen, DeepSeek, MiniMax, Morph) optimized for competitive inference speeds. The free tier offers replenishable credits — useful when you need massive model scale (up to 397B) without requiring a credit card.

**Base URL:** `https://api.morphllm.com/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `morph-v3-large` | ⭐⭐⭐⭐⭐ | **BEST.** The fastest clean responder. Delivers direct output with zero preamble — ideal for tight agentic loops. |
| `morph-qwen36-27b` | ⭐⭐⭐⭐☆ | Fast 27B Qwen variant with clean response. Solid everyday coding companion with good multilingual support. |
| `morph-dsv4flash` | ⭐⭐⭐⭐☆ | DeepSeek-based flash model. Lightweight and responsive for rapid code completions. |
| `morph-qwen35-397b` | ⭐⭐⭐⭐☆ | A 397B parameter model — remarkably fast for its scale. Use it when you need massive reasoning without paying for a cluster. |
| `morph-minimax27-230b` | ⭐⭐⭐☆☆ | Large 230B model with a `<think>` preamble. The reasoning layer helps complex logic but wastes cycles on simple requests. |
| `morph-v3-fast` | ⭐⭐⭐☆☆ | Fast but echoes the instruction back instead of executing — adds unnecessary tokens in pipeline contexts. |
| `morph-compactor` | ⭐⭐⭐☆☆ | Same instruction-echoing pattern as v3-fast. Useful for prompt confirmation, wasteful otherwise. |
| `morph-warp-grep-v2.1` | ⭐⭐⭐☆☆ | Slower with a search-focused architecture. Better suited for log analysis and grep-style lookups than general coding. |
| `auto` | ⭐⭐☆☆☆ | Slowest and echoes instructions back. Too sluggish for real-time coding — use the other MorphLLM models instead. |


<a id="ollama-cloud-models"></a>
### 🦙 [Ollama Cloud](https://ollama.com) Models (26)
Ollama Cloud is a cloud-hosted inference service running Ollama behind the scenes, offering a vast model registry without the need to run locally. The free tier provides replenishable credits with generous rate limits — most models respond cleanly and quickly, making it one of the strongest free providers for coding.

At the time of testing, Ollama Cloud has **26 Models**... so we made the Top 20 of Ollama Cloud's best Models.

**Base URL:** `https://api.ollama.com`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `qwen3-coder-next` | ⭐⭐⭐⭐⭐ | **BEST.** Handles every coding task directly and instantly. You can rely on it as the first thing you reach for on Ollama Cloud because it responds cleanly with no preamble or chatter. |
| `qwen3-coder:480b` | ⭐⭐⭐⭐⭐ | Handles the toughest debugging sessions without breaking a sweat. Feels like having a senior engineer review your architecture when you're stuck on hard problems. |
| `cogito-2.1:671b` | ⭐⭐⭐⭐⭐ | Handles deep reasoning problems that smaller models give up on. You can rely on it for the hardest architectural questions because its raw capacity rarely hits a wall. |
| `devstral-2:123b` | ⭐⭐⭐⭐⭐ | Handles agentic tool-use pipelines smoothly. You can rely on it for automated workflows because it was purpose-built for developer routing from the ground up. |
| `gpt-oss:120b` | ⭐⭐⭐⭐⭐ | Handles every coding task the same reliable way across every provider. Feels familiar and trustworthy because the quality never wavers. |
| `nemotron-3-nano:30b` | ⭐⭐⭐⭐⭐ | Handles reasoning tasks quickly without wasting tokens. Feels efficient and direct — you can rely on it for fast turnarounds on structured problems. |
| `rnj-1:8b` | ⭐⭐⭐⭐⭐ | Handles rapid-fire completions with surprising quality for its size. Feels punchy and responsive — you can rely on it for quick edits without any slowdown. |
| `devstral-small-2:24b` | ⭐⭐⭐⭐⭐ | Handles everyday coding without the overhead of larger models. Feels lean and responsive — you can rely on it for daily work when you don't need the full 123B. |
| `gemma3:12b` | ⭐⭐⭐⭐⭐ | Handles instruction-heavy prompts with clean, direct answers. Feels surprisingly capable for its size — you can rely on it to follow complex instructions precisely. |
| `gemma3:27b` | ⭐⭐⭐⭐⭐ | Handles the same clean instruction following as the 12B with more room for complex tasks. Feels like a natural upgrade when you need extra capacity without sacrificing quality. |
| `gemma3:4b` | ⭐⭐⭐⭐⭐ | Handles ultra-light tasks with barely any latency. You can rely on it for syntax checks and simple scripts where speed matters more than depth. |
| `qwen3-vl:235b-instruct` | ⭐⭐⭐⭐⭐ | Handles multimodal inputs without rambling preamble. Feels clean and focused when you mix screenshots with code — you get answers, not commentary. |
| `qwen3-next:80b` | ⭐⭐⭐⭐⭐ | Handles the middle ground between coder specialization and general chat naturally. Feels versatile — you can rely on it when you're not sure which Qwen to pick. |
| `minimax-m2.5` | ⭐⭐⭐⭐⭐ | Handles responses with better consistency than earlier versions. Feels like a refined tool — you can rely on it for dependable output every time. |
| `minimax-m3` | ⭐⭐⭐⭐⭐ | Handles everything the M2 line does with the latest polish. Feels like the most mature MiniMax option — you can rely on it for dependable daily coding. |
| `glm-4.7` | ⭐⭐⭐⭐⭐ | Handles complex tasks reliably, even if it takes a moment longer. You can rely on it for thorough answers when getting it right matters more than speed. |
| `minimax-m2` | ⭐⭐⭐⭐⭐ | Handles basic coding tasks cleanly, though newer versions have pulled ahead. Still feels dependable for straightforward work where you don't need the latest improvements. |
| `gpt-oss:20b` | ⭐⭐⭐⭐☆ | **SOLID COMPANION.** Handles daily coding without burning through your quota. Feels like a practical daily driver — you can rely on it for solid results without the parameter overhead of bigger models. |
| `minimax-m2.1` | ⭐⭐⭐⭐☆ | Handles tasks functionally, but newer versions feel noticeably cleaner. You can rely on it in a pinch, though you'll have a smoother experience with M2.5 or M3. |
| `ministral-3:14b` | ⭐⭐⭐⭐☆ | Handles agent pipeline tasks with minimal output noise. Feels clean and direct — you can rely on it for automated workflows without cleaning up extra chatter. |


<a id="openrouter-models"></a>
### 🌐 [OpenRouter](https://openrouter.ai) Models (15)
OpenRouter is a unified API gateway providing access to hundreds of models from dozens of providers through a single endpoint. The free tier offers rate-limited access to community-hosted models (marked with `:free`) — no credit card required. A great backup when other providers are rate-limited.

**Base URL:** `https://openrouter.ai/api/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `openai/gpt-oss-120b:free` | ⭐⭐⭐⭐⭐ | **BEST.** Handles every coding task reliably the same way across every provider. Feels familiar and trustworthy because the quality never wavers — still the strongest coding option on OpenRouter. |

| `google/gemma-4-31b-it:free` | ⭐⭐⭐⭐⭐ | Handles deeper reasoning problems with the extra parameter headroom. Feels like a natural upgrade from the 26B when you need to think through harder problems. |
| `nex-agi/nex-n2-pro:free` | ⭐⭐⭐⭐⭐ | Handles general coding tasks with surprising strength. Feels like a dark horse — you can rely on it when you need a fresh perspective on a problem. |
| `openai/gpt-oss-20b:free` | ⭐⭐⭐⭐⭐ | Handles everyday coding tasks without wasting compute. Feels like the practical sibling of the 120B — you can rely on it for quick, solid results. |
| `nvidia/nemotron-nano-12b-v2-vl:free` | ⭐⭐⭐⭐⭐ | Handles both text and vision inputs in a small, responsive package. Feels surprisingly capable for its size — great when you need multimodal without the overhead. |
| `liquid/lfm-2.5-1.2b-instruct:free` | ⭐⭐⭐⭐⭐ | Handles trivial tasks instantly with minimal latency. Feels like the smallest model that actually works — you can rely on it when you just need a quick answer. |
| `poolside/laguna-m.1:free` | ⭐⭐⭐⭐☆ | **CODE COMPLETION ONLY.** Handles code completions with purpose-built precision. Feels purpose-built for software development — you can rely on it for inline completions that fit your context. |
| `poolside/laguna-xs.2:free` | ⭐⭐⭐⭐☆ | Handles inline completions with blazing speed. Feels compact and efficient — you can rely on it when you need fast suggestions without distraction. |
| `nvidia/nemotron-3-nano-30b-a3b:free` | ⭐⭐⭐⭐☆ | Handles reasoning tasks efficiently by activating only what it needs. Feels fast and responsive — you can rely on it for efficient thinking without the full parameter tax. |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ⭐⭐⭐⭐☆ | Handles chain-of-thought tasks with structured reasoning. Feels specialized for step-by-step thinking — you can rely on it when you need the model to show its work. |
| `nvidia/nemotron-nano-9b-v2:free` | ⭐⭐⭐⭐☆ | Handles fallback duties reliably when other models are unavailable. Feels lightweight and dependable — you can rely on it to keep you unblocked. |
| `liquid/lfm-2.5-1.2b-thinking:free` | ⭐⭐⭐☆☆ | Handles thinking tasks but adds noisy preamble. Feels cluttered compared to the instruct version — better to rely on the cleaner alternative for straightforward work. |
| `nvidia/nemotron-3-super-120b-a12b:free` | ⭐⭐⭐☆☆ | Handles large-scale queries but adds verbose preamble that gets in the way. Feels impractical for agents — the parameter count doesn't help when the output is cluttered. |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | ⭐⭐⭐☆☆ | Raw 550B power is there, but you'll spend as much time scrolling past preamble as reading the actual answer. The constant prefix noise makes it frustrating for agentic use despite the massive parameter count. |
| `nvidia/nemotron-3.5-content-safety:free` | ⭐⭐☆☆☆ | **SAFETY MONITOR ONLY.** Handles content safety classification with a single purpose. You can rely on it for filtering agent outputs, but don't expect coding capability — use it for safety checks only. |


<a id="pollinations-ai-models"></a>
### 🎨 [Pollinations AI](https://pollinations.ai) Models (38)
Pollinations AI is a free, no-signup inference provider serving a wide variety of models — from OpenAI and Grok to Qwen, Perplexity, and niche music/safety models. No API key needed, no account required — the only truly zero-friction provider on this list.

At the time of testing, Pollinations AI has **38 Models**... so we made the Top 20 of Pollinations AI's Best Models.

**Base URL:** `https://gen.pollinations.ai/v1` (OpenAI-compatible)

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `qwen-coder` | ⭐⭐⭐⭐⭐ | **BEST.** Handles every coding task with focused, direct output. You can rely on it as the obvious first pick on Pollinations — it just works and stays out of your way. |
| `openai` | ⭐⭐⭐⭐⭐ | Handles everyday coding without surprises. Feels reliable and direct — you can drop it into any workflow and get clean answers back. |
| `openai-large` | ⭐⭐⭐⭐⭐ | Handles complex reasoning with extra headroom. Feels capable when you need to think through a hard problem — you can rely on it for the tough stuff. |
| `gpt-5.4-mini` | ⭐⭐⭐⭐⭐ | Handles tasks at blazing speed with zero preamble. Feels snappy and efficient — you can rely on it for fast turnarounds without any fluff. |
| `gemma` | ⭐⭐⭐⭐⭐ | Handles instruction-heavy prompts with surprising precision. Feels punchier than its size suggests — you can rely on it to follow complex instructions cleanly. |
| `grok` | ⭐⭐⭐⭐⭐ | Handles code tasks with unexpected polish. Feels natural when you switch between chat and coding — you can rely on it even though coding isn't its main pitch. |
| `grok-4.3` | ⭐⭐⭐⭐⭐ | Handles the same tasks as base Grok with slightly better consistency. Feels like a refined version — you can rely on it for the same clean output. |
| `perplexity` | ⭐⭐⭐⭐⭐ | Handles research-heavy coding with factual grounding. Feels trustworthy when accuracy matters — you can rely on it to back up its answers. |
| `nova-fast` | ⭐⭐⭐⭐⭐ | Handles rapid-fire coding loops without lag. Feels like the name promises — fast — you can rely on it when speed is the priority. |
| `llama` | ⭐⭐⭐⭐⭐ | Handles general coding without extra chatter. Feels like a classic workhorse — you can rely on it for clean, no-nonsense output every time. |
| `qwen-vision` | ⭐⭐⭐⭐⭐ | Handles multimodal inputs while keeping responses clean. Feels seamless when you mix screenshots with code — you can rely on it not to ramble. |
| `qwen-vision-pro` | ⭐⭐⭐⭐⭐ | Handles the same vision tasks with more polish. Feels like a step up from the base vision model — you can rely on it for sharper multimodal answers. |
| `openai-fast` | ⭐⭐⭐⭐☆ | Handles quick tasks with minimal latency. Feels purpose-built for speed, though you'll notice it trades some depth on very complex reasoning. |
| `gpt-5.5` | ⭐⭐⭐⭐☆ | Handles most coding tasks reliably. Feels slightly less consistent than 5.4 Mini — you can rely on it but may need to refresh outputs occasionally. |
| `kimi-k2.7-code` | ⭐⭐⭐⭐☆ | Handles programming-specific tasks with solid competence. Feels specialized — you can rely on it for code-focused work rather than general chat. |
| `minimax-m3` | ⭐⭐⭐⭐☆ | Handles everyday coding without friction. Feels like a solid general pick — you can rely on it when you don't need anything exotic. |
| `step-3.5-flash` | ⭐⭐⭐⭐☆ | Handles routine coding tasks quickly and efficiently. Feels fast enough for daily use — you can rely on it for straightforward edits and scripts. |
| `qwen-large` | ⭐⭐⭐⭐☆ | Handles bigger contexts with more parameter headroom. Feels capable but slightly less direct than base Qwen — you can rely on it when you need extra capacity. |
| `step-flash` | ⭐⭐⭐⭐☆ | Handles fallback duties without noticeable quality loss. Feels dependable when your primary model is tapped out — you can rely on it as a backup. |
| `nova` | ⭐⭐⭐⭐☆ | Handles agentic pipelines with minimal output noise. Feels clean enough for automated use — you can rely on it for straightforward coding tasks. |


<a id="sambanova-ai-models"></a>
### 🌀 [SambaNova AI](https://cloud.sambanova.ai) Models (5)
SambaNova AI is a **hardware-driven inference provider** utilizing proprietary Reconfigurable Dataflow Units (RDUs) rather than standard GPUs, removing the traditional hardware-decode bottleneck for incredibly high throughput. The free tier offers generous replenishable credits with rate limits suitable for sustained agentic use.

**Base URL:** `https://api.sambanova.ai/v1`

| Free Model | Star Rating | How that Model handles your work |
| :--- | :--- | :--- |
| `DeepSeek-V3.2` | ⭐⭐⭐⭐⭐ | **BEST.** The absolute pinnacle of hardware-optimized reasoning. Running on fine-grained sparse attention mechanisms, it hits near immediate end-to-end token execution speeds and effortlessly untangles high-level architectural errors or logic puzzles. |
| `DeepSeek-V3.1` | ⭐⭐⭐⭐⭐ | **BEST.** An incredibly fast, massive hybrid mixture model. Running in non-thinking mode over SambaNova's RDU pipelines, it functions as a premium, highly responsive background planner for code-routing and multi-step agent actions. |
| `Meta-Llama-3.3-70B-Instruct` | ⭐⭐⭐⭐☆ | The traditional benchmark engine. It interprets dense, multi-variable project constraints with high structural reliability, only trailing the newer architectures slightly on processing heavy visual context. |
| `gemma-4-31B-it` | ⭐⭐⭐⭐☆ | Google's newest instruction-tuned model block. Strikes a masterclass balance between low parameter footprint and high-level structural syntax mastery, blazing through system boilerplates. |
| `gpt-oss-120b` | ⭐⭐⭐☆☆ | The same 117B MoE flagship that dominates on Groq. Available on SambaNova but with noticeably higher latency (~3.5s) compared to its sub-second performance on Groq. |

---

<a id="contributing"></a>
## CONTRIBUTING

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details.

<a id="license"></a>
## LICENSE

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

This project is released under the [CC0-1.0](LICENSE.md) license.