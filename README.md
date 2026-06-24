# Awesome Free BYOK Models [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

> ⏰ **Last Verified: June 24, 2026** - All models tested live across 38 providers.

Text‑generation APIs that are permanently free and self‑replenishing, stress‑tested for coding tools and versatile enough for everyday chat.

By using a **Bring Your Own Key (BYOK)** approach, you can plug your free API keys into **coding tools**, **custom projects**, or **AI-powered apps** — no credit card required. Every model listed here is rated for coding capability, but most work just as well for general conversation.

> 💡 **Pro tip:** Free tiers rotate often. If a model hits rate limits, switch to another — there's always a backup in this list.
> **Always verify** current quotas on the provider's console before building workflows.

## Contents

- [The Best API Providers](#the-best-api-providers)
- [Top Free Models](#top-free-models)
- [Provider Showcases](#provider-showcases)

## The Best API Providers

If you are signing up for free accounts to get API keys, these are the **top platforms** to look at first.

| Provider          | The Simple Vibe     | Why It Matters For You                                                                                                                                                      |
| :---------------- | :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ollama Cloud**  | Uncapped & Reliable | Time-based compute allocation with no daily request cap — the only provider where you can code or chat all day without counting requests. Home to the #1 ranked free model. |
| **Google Gemini** | Infinite Battery    | 1,500 free requests per day on flash-lite with a massive context window. Lighter on reasoning but unstoppable for continuous background tasks.                              |
| **LLM7.IO**       | Heavy Lifter        | 128 RPM with 5M daily tokens and replenishable credits — hosts the #3 ranked model. No hard daily cap, ideal for sustained coding and general-purpose use.                  |

---

## Top Free Models

The absolute best free models available right now, ranked by how well they handle **daily coding tasks** and **projects that require a working model**. While this leaderboard ranks models for coding, every provider in the full list below also works great for general chat and creative tasks. This does **NOT** include vision models — all models here are text-only.

| Rank   | Model                          | Host Provider       | The Simple Reason to Choose It                                                                                                                                                                                                                                                |
| :----- | :----------------------------- | :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1**  | `qwen3-coder-next`             | **Ollama Cloud**    | Scores over 70% on SWE-bench Verified. Native 256K context with sandbox reinforcement learning — if it writes broken code, it reads your terminal logs and fixes its own bugs. Uncapped usage via time-based compute allocation. The best overall assistant for daily coding. |
| **2**  | `models/gemini-3.1-flash-lite` | **Google Gemini**   | 1,500 free daily requests with a massive context window. Lighter on deep reasoning, but unstoppable for background triaging, test iterations, and log file analysis all day. The infinite workhorse.                                                                          |
| **3**  | `qwen3-235b`                   | **LLM7.IO**         | Native support for 119 programming languages at 128 RPM with a 5M daily token pool. Elite reasoning depth for cross-language refactoring.                                                                                                                                     |
| **4**  | `qwen-coder`                   | **Pollinations AI** | Stays focused on code without rambling. You can hammer it all day with 60 RPM and unlimited requests — it answers directly every time.                                                                                                                                        |
| **5**  | `deepseek-v4-flash-free`       | **OpenCode Zen**    | The strongest model on OpenCode Zen for coding with 30 RPM, 500 RPD, and 1M TPD — a quota profile that outlasts everything below this rank. Handles multi-turn context tracking smoothly at rapid generation speeds.                                                          |
| **6**  | `mistral-code-agent-latest`    | **Mistral AI**      | Purpose-built for multi-step agent actions with reliable tool-calling and structured JSON outputs. Mistral's 50k TPM shared pool limits it to single-file scope in practice.                                                                                                  |
| **7**  | `openai/gpt-oss-120b`          | **Groq API**        | Elite algorithmic reasoning, but Groq's 18k TPM cap is a trap — one multi-file prompt triggers a 429. Use it sparingly for targeted debugging of the hardest bugs.                                                                                                            |
| **8**  | `qwen/qwen3-32b`               | **Groq API**        | Dumps clean code into your IDE at blazing speed. Same 18k TPM handcuffs as rank 7 — ideal for short snippets, unusable for sustained sessions.                                                                                                                                |
| **9**  | `DeepSeek-V3.1`                | **SambaNova AI**    | The 671B flagship — unmatched structural planning and algorithm generation, but crippled by 20 RPD and 200k TPD caps. A single comprehensive prompt drains your entire 24-hour token allowance on your first call.                                                            |
| **10** | `codestral-latest`             | **LLM7.IO**         | Strongest Mistral-based coding model with 128 RPM and a 5M daily token pool. Fast, clean completions — solid backup when Qwen is busy.                                                                                                                                        |

---

## Provider Showcases

These tables break down notable free models from each provider's ecosystem, **capped at ★★★☆☆ or above for providers and ★★★★☆ or above for hubs**. Ratings are based on how well they handle real-world development demands — typing speed, instruction following, and large projects — evaluated against each provider's quota, rate limits, and context windows.

<strong>Jump to a provider or hub:</strong>

<ul>
  <li><a href="#aion-labs">AION Labs</a></li>
  <li><a href="#agnes-ai">Agnes AI</a></li>
  <li><a href="#anyapi-ai">AnyAPI AI</a></li>
  <li><a href="#api-airforce">API Airforce</a></li>
  <li><a href="#auriko">Auriko</a></li>
  <li><a href="#blazeapi">BlazeAPI</a></li>
  <li><a href="#cerebras-ai">Cerebras AI</a></li>
  <li><a href="#cloudflare-workers-ai">Cloudflare Workers AI</a></li>
  <li><a href="#cohere-ai">Cohere AI</a></li>
  <li><a href="#electronhub">ElectronHub</a></li>
  <li><a href="#fastrouter">FastRouter</a></li>
  <li><a href="#github-models">GitHub Models</a></li>
  <li><a href="#google-gemini">Google Gemini</a></li>
  <li><a href="#groq-api">Groq API</a></li>
  <li><a href="#helixmind">HelixMind</a></li>
  <li><a href="#hugging-face-inference-api">Hugging Face Inference API</a></li>
  <li><a href="#kilo-code">Kilo Code</a></li>
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
  <li><a href="#paxsenix">PaxSenix</a></li>
  <li><a href="#pollinations-ai">Pollinations AI</a></li>
  <li><a href="#poolside">Poolside</a></li>
  <li><a href="#routeway-ai">Routeway AI</a></li>
  <li><a href="#sambanova-ai">SambaNova AI</a></li>
  <li><a href="#tokenreply">TokenReply</a></li>
  <li><a href="#void-ai">Void AI</a></li>
  <li><a href="#zai-zhipu-ai">Z.AI (Zhipu AI)</a></li>
</ul>

### [AION Labs](https://www.aionlabs.ai)

AION Labs provides storytelling-optimized models through an OpenAI-compatible API. The free tier offers 20,000 tokens/day and 15 RPM with no credit card required — a solid option if you need a daily token allowance for lightweight coding and creative tasks. AION Labs currently has 2 models verified.

🎁 **Free Tier Quota:** 15 RPM / 500 RPD / 5,000,000 TPD

🔗 **Base URL:** `https://api.aionlabs.ai/v1`

| Free Model                       | Star Rating | Best For   | Speed     | Opinion                                                                           |
| :------------------------------- | :---------- | :--------- | :-------- | :-------------------------------------------------------------------------------- |
| `aion-labs/aion-2.5`             | ★★★★★       | `Code`     | `Fast`    | Clean, direct output with no preamble. The top pick on AION Labs.                 |
| `aion-labs/aion-rp-llama-3.1-8b` | ★★★★☆       | `Fallback` | `Blazing` | Fastest AION model. Handles lightweight tasks instantly, but 8B cap limits depth. |

### [Agnes AI](https://www.agnes.ai)

Agnes AI offers flash-tier models with generous daily limits but slow inference speed. The free tier provides 1,000 requests per day at 20 RPM — enough volume for background jobs, but ~7s latency makes interactive use frustrating. No credit card required. Agnes AI currently has 2 models verified.

🎁 **Free Tier Quota:** 20 RPM / 1,000 RPD

🔗 **Base URL:** `https://api.agnes.ai/v1`

| Free Model        | Star Rating | Best For   | Speed  | Opinion                                                                                          |
| :---------------- | :---------- | :--------- | :----- | :----------------------------------------------------------------------------------------------- |
| `agnes-1.5-flash` | ★★★☆☆       | `Fallback` | `Slow` | Older flash model — works but well behind current frontier models in both speed and quality.     |
| `agnes-2.0-flash` | ★★★☆☆       | `General`  | `Slow` | Latest flash variant with decent reasoning. The 7s latency is the main bottleneck for daily use. |

### [AnyAPI AI](https://anyapi.ai)

AnyAPI is a unified API gateway providing access to 400+ models from OpenAI, Anthropic, Google, DeepSeek, Meta, Mistral, Cohere, and more through a single OpenAI-compatible endpoint. The free tier offers 100,000 tokens/day with access to free and basic models — no credit card required. AnyAPI currently has 10 models verified — 8 are ★★★★☆ or above.

🎁 **Free Tier Quota:** 100,000 tokens/day / No Credit Card

🔗 **Base URL:** `https://api.anyapi.ai/v1`

| Free Model                                           | Star Rating | Best For    | Speed      | Opinion                                                                                 |
| :--------------------------------------------------- | :---------- | :---------- | :--------- | :-------------------------------------------------------------------------------------- |
| `nvidia/nemotron-nano-12b-v2-vl:free`                | ★★★★★       | `Vision`    | `Fast`     | Handles text and vision in one call. Strong general coding with multimodal flexibility. |
| `poolside/laguna-m.1:free`                           | ★★★★★       | `Code`      | `Fast`     | Same elite 225B Poolside coding flagship. Clean output with zero preamble noise.        |
| `google/gemma-4-26b-a4b-it:free`                     | ★★★★☆       | `General`   | `Fast`     | Google's compact 26B Gemma. Clean, structured output for daily coding.                  |
| `nvidia/nemotron-3-nano-30b-a3b:free`                | ★★★★☆       | `General`   | `Fast`     | Efficient 30B MoE — clean responses with no preamble.                                   |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ★★★★☆       | `Reasoning` | `Moderate` | Shows step-by-step reasoning. Useful for verification, verbose for quick answers.       |
| `nvidia/nemotron-nano-9b-v2:free`                    | ★★★★☆       | `Fallback`  | `Fast`     | Reliable NVIDIA nano. Punches above its 9B weight for quick edits.                      |
| `openrouter/fusion`                                  | ★★★★☆       | `General`   | `Moderate` | OpenRouter's multi-model fusion — aggregates outputs for balanced responses.            |
| `poolside/laguna-xs.2:free`                          | ★★★★☆       | `Code`      | `Blazing`  | Poolside's 33B coder. Sub-second responses for inline completions.                      |

### [API Airforce](https://www.apiairforce.com)

API Airforce is a lightweight inference provider with a single model offering — a free DeepSeek V3.2 variant. The free tier gives you 1,000 requests per day at 1 RPM, suitable for occasional queries and quick debugging. No identity verification required. API Airforce currently has 1 model verified.

🎁 **Free Tier Quota:** 1 RPM / 1,000 RPD

🔗 **Base URL:** `https://api.apiairforce.com/v1`

| Free Model           | Star Rating | Best For   | Speed      | Opinion                                                                                                      |
| :------------------- | :---------- | :--------- | :--------- | :----------------------------------------------------------------------------------------------------------- |
| `deepseek-v3.2-free` | ★★★☆☆       | `Fallback` | `Moderate` | DeepSeek V3.2 at no cost — strong reasoning but 1 RPM limits it to occasional queries, not sustained coding. |

### [Auriko](https://www.auriko.ai)

Auriko is a unified API gateway providing access to 100+ models from top providers (OpenAI, Anthropic, DeepSeek, Google, xAI, Moonshot, and more) through a single OpenAI-compatible endpoint. The free tier offers 1,000 Platform RPM and 500 BYOK RPM with a 1M token monthly cap and zero inference markup — no credit card required. Access to every model on the platform at provider cost. Auriko currently has 166 models verified — 45 are ★★★★☆ or above.

🎁 **Free Tier Quota:** 500 RPM (BYOK) / 1,000 RPM (Platform) / 1,000,000 tokens/month (BYOK)

🔗 **Base URL:** `https://api.auriko.ai/v1`

| Free Model                           | Star Rating | Best For    | Speed      | Opinion                                                                                                     |
| :----------------------------------- | :---------- | :---------- | :--------- | :---------------------------------------------------------------------------------------------------------- |
| `claude-opus-4-1-20250805`           | ★★★★★       | `Code`      | `Blazing`  | Earlier Opus 4.1 — established baseline for the Opus 4 series. Still elite for daily coding.                |
| `claude-opus-4-5-20251101`           | ★★★★★       | `Code`      | `Blazing`  | Polished mid-cycle Opus — strong reasoning with clean, structured code output.                              |
| `claude-opus-4-6`                    | ★★★★★       | `Code`      | `Blazing`  | Slightly older Opus but still elite — handles complex architecture with zero preamble.                      |
| `claude-opus-4-7`                    | ★★★★★       | `Code`      | `Blazing`  | Fastest Claude Opus variant. Deep reasoning and code generation with zero preamble.                         |
| `claude-opus-4-8`                    | ★★★★★       | `Code`      | `Blazing`  | Latest Claude Opus. Deep reasoning and code generation with zero preamble.                                  |
| `deepseek-r1-0528`                   | ★★★★★       | `Reasoning` | `Moderate` | Elite reasoning model — walks through complex problems step by step. Clean chain-of-thought output.         |
| `deepseek-v3.1-terminus`             | ★★★★★       | `Reasoning` | `Fast`     | Specialized V3.1 variant — refined reasoning output for complex multi-step analysis.                        |
| `deepseek-v3.1`                      | ★★★★★       | `Reasoning` | `Fast`     | The best provider for V3.1 — 5,000 RPD and 5M TPD with zero quota stress. Elite reasoning at blazing speed. |
| `deepseek-v3.2-exp`                  | ★★★★★       | `Reasoning` | `Fast`     | Experimental variant of V3.2 — bleeding-edge reasoning with deeper chain-of-thought.                        |
| `deepseek-v3.2`                      | ★★★★★       | `Reasoning` | `Fast`     | Elite reasoning workhorse trusted across every provider. Clean output for multi-file analysis.              |
| `deepseek-v4-pro`                    | ★★★★★       | `Reasoning` | `Fast`     | Pro variant of DeepSeek V4 — extra headroom for the hardest multi-file problems.                            |
| `glm-5.1`                            | ★★★★★       | `Code`      | `Fast`     | GLM's strongest coding model. Clean structured output for multi-file agentic work.                          |
| `gpt-5-2025-08-07`                   | ★★★★★       | `General`   | `Fast`     | GPT-5 flagship — handles every coding task with zero preamble. Elite intelligence without friction.         |
| `gpt-5.5-2026-04-23`                 | ★★★★★       | `General`   | `Fast`     | Latest GPT generation. Best general intelligence on Auriko with zero preamble.                              |
| `gpt-oss-120b-turbo`                 | ★★★★★       | `General`   | `Blazing`  | Turbo variant of OSS 120B — extra throughput for rapid-fire agentic loops.                                  |
| `gpt-oss-120b`                       | ★★★★★       | `General`   | `Blazing`  | Reliable 120B general model — clean output across every coding task at blazing speed.                       |
| `grok-4.20-0309-reasoning`           | ★★★★★       | `Reasoning` | `Fast`     | xAI's reasoning variant — strong chain-of-thought for complex multi-step debugging.                         |
| `hermes-3-llama-3.1-405b`            | ★★★★★       | `Reasoning` | `Moderate` | 405B of raw Llama capability. Feels unfair for a free tier.                                                 |
| `minimax-m3`                         | ★★★★★       | `General`   | `Blazing`  | 80.5% SWE-bench Verified with 1M context. Frontier-class coding at blazing speed.                           |
| `nex-n2-pro`                         | ★★★★★       | `Code`      | `Fast`     | Strong coder with deep reasoning. Proven across daily agentic workflows.                                    |
| `o3-2025-04-16`                      | ★★★★★       | `Reasoning` | `Moderate` | Top-tier reasoning — handles multi-file architecture without preamble. The strongest coding pick on Auriko. |
| `qwen-2.5-72b-instruct`              | ★★★★★       | `General`   | `Fast`     | Proven workhorse trusted across every setup. Reliable and consistent.                                       |
| `qwen-3-235b-a22b-instruct-2507-fp8` | ★★★★★       | `General`   | `Fast`     | 235B at FP8 precision. Elite reasoning without the full-weight latency.                                     |
| `qwen-3-coder-30b-a3b-instruct`      | ★★★★★       | `Code`      | `Fast`     | Focused 30B coder from Qwen — efficient and responsive for everyday coding.                                 |
| `qwen-3-coder-480b-a35b-instruct`    | ★★★★★       | `Code`      | `Moderate` | Purpose-built 480B code model — tackles the hardest debugging sessions.                                     |
| `qwen-3.5-397b-a17b`                 | ★★★★★       | `Reasoning` | `Moderate` | 397B MoE (17B active) — immense capacity for the most complex multi-file prompts.                           |
| `qwen-3.7-max`                       | ★★★★★       | `General`   | `Fast`     | Latest Qwen max generation — elite general intelligence with clean, reliable output.                        |
| `claude-haiku-4-5-20251001`          | ★★★★☆       | `General`   | `Blazing`  | Fast and focused. Handles daily coding without fanfare.                                                     |
| `claude-sonnet-4-6`                  | ★★★★☆       | `Code`      | `Fast`     | Latest Sonnet 4.6 — handles creative coding with Anthropic's clear response style.                          |
| `deepseek-v4-flash`                  | ★★★★☆       | `Reasoning` | `Fast`     | Latest DeepSeek flash variant — strong reasoning depth with clean inference.                                |
| `gemini-3.1-flash-lite`              | ★★★★☆       | `General`   | `Blazing`  | Google's fastest flash variant. Uncapped daily usage through Auriko's quota pool.                           |
| `gemma-4-31b-it-turbo`               | ★★★★☆       | `General`   | `Fast`     | Turbocharged Gemma 4. Fast responses with clean, structured output.                                         |
| `gpt-4.1-2025-04-14`                 | ★★★★☆       | `Code`      | `Blazing`  | Blazing fast with strong general coding capability. A solid daily driver.                                   |
| `gpt-4o-mini-2024-07-18`             | ★★★★☆       | `Code`      | `Fast`     | OpenAI's compact classic. Reliable daily coding with broad language support.                                |
| `gpt-5-chat-latest`                  | ★★★★☆       | `Chat`      | `Fast`     | Chat-optimized GPT-5 variant. Handles conversational coding naturally and cleanly.                          |
| `gpt-5.2-2025-12-11`                 | ★★★★☆       | `General`   | `Fast`     | Latest GPT-5 point release. Fast and reliable across every coding task.                                     |
| `gpt-5.4-2026-03-05`                 | ★★★★☆       | `General`   | `Fast`     | Latest GPT generation. Strong general intelligence with clean output.                                       |
| `gpt-5.4-mini-2026-03-17`            | ★★★★☆       | `General`   | `Fast`     | Compact GPT-5.4 — handles lightweight tasks efficiently.                                                    |
| `gpt-5.4-nano-2026-03-17`            | ★★★★☆       | `General`   | `Blazing`  | The nano tier — syntax checks and quick edits return almost instantly.                                      |
| `grok-4.20-0309-non-reasoning`       | ★★★★☆       | `Agent`     | `Blazing`  | xAI's fastest — clean output for rapid-fire coding loops where speed is everything.                         |
| `llama-3.3-70b-instruct-fp8`         | ★★★★☆       | `General`   | `Fast`     | Strong instruction following with edge-friendly speed. Clean and dependable.                                |
| `o4-mini-2025-04-16`                 | ★★★★☆       | `Reasoning` | `Fast`     | Latest reasoning model from OpenAI — compact but capable. Handles logic-heavy tasks cleanly.                |
| `phi-4`                              | ★★★★☆       | `Code`      | `Blazing`  | Microsoft's compact powerhouse. Surprising coding depth for its size.                                       |
| `qwen-3.6-35b-a3b`                   | ★★★★☆       | `Code`      | `Blazing`  | Latest Qwen 3.6 — efficient MoE architecture with strong reasoning density per token.                       |
| `seed-2.0-code`                      | ★★★★☆       | `Code`      | `Fast`     | Coding-specialized from Seed. Handles multi-file refactors without rambling.                                |

### [BlazeAPI](https://blazeai.boxu.dev)

BlazeAPI is a lightweight inference hub serving models from Moonshot and Z.AI through an OpenAI-compatible endpoint. The free tier provides 20 RPM with 1,000 requests per day — a solid quota for daily coding and occasional heavy queries. No credit card required. BlazeAPI currently has 2 models verified — both at ★★★★☆ or above.

🎁 **Free Tier Quota:** 20 RPM / 1,000 RPD

🔗 **Base URL:** `https://blazeai.boxu.dev/api`

| Free Model             | Star Rating | Best For    | Speed  | Opinion                                                                                |
| :--------------------- | :---------- | :---------- | :----- | :------------------------------------------------------------------------------------- |
| `moonshotai/kimi-k2.6` | ★★★★☆       | `Reasoning` | `Fast` | 1T multimodal MoE with strong long-horizon reasoning. Solid daily driver at 1,000 RPD. |
| `z-ai/glm-5.1`         | ★★★★☆       | `General`   | `Fast` | GLM 5.1 — clean output with solid reasoning for everyday coding tasks.                 |

### [Cerebras AI](https://cloud.cerebras.ai)

Cerebras AI is defined by its **Wafer-Scale Engine (WSE) technology**, integrating memory, compute, and interconnects onto a single silicon wafer — solving the "memory wall" that throttles inference speed. The free tier offers replenishable credits with industry-leading throughput (2,500+ tokens/second). Cerebras AI currently has 2 models verified.

🎁 **Free Tier Quota:** 5 RPM / 250 RPD / 30,000 TPM

🔗 **Base URL:** `https://api.cerebras.ai/v1`

| Free Model     | Star Rating | Best For  | Speed     | Opinion                                                                                                        |
| :------------- | :---------- | :-------- | :-------- | :------------------------------------------------------------------------------------------------------------- |
| `gpt-oss-120b` | ★★★★☆       | `General` | `Blazing` | The same 117B MoE flagship that dominates on Groq. Sub-second responses on Cerebras' wafer-scale architecture. |
| `zai-glm-4.7`  | ★★★★☆       | `Agent`   | `Blazing` | 131K context window optimized for rapid agentic coding. Efficient at blazing speeds.                           |

### [Cloudflare Workers AI](https://dash.cloudflare.com)

Cloudflare Workers AI runs models on Cloudflare's global edge network using serverless GPUs. The free tier offers 10,000 requests/day shared across all models with near-zero latency from edge locations worldwide. Cloudflare Workers AI currently has 27 models verified — 22 are ★★★☆☆ or above.

🎁 **Free Tier Quota:** 150 to 1,500 RPM / 100,000 RPD / 13,000 TPD

🔗 **Base URL:** `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions` (replace `{account_id}` with your Cloudflare account ID)

> ⚠️ **Two API paths:** The `/chat/completions` endpoint takes standard `"messages"` (OpenAI-compatible). The legacy `/run/{model}` endpoint uses `"prompt"` instead — make sure your tool targets the right one.

| Free Model                                     | Star Rating | Best For    | Speed      | Opinion                                                                                                         |
| :--------------------------------------------- | :---------- | :---------- | :--------- | :-------------------------------------------------------------------------------------------------------------- |
| `@cf/qwen/qwen2.5-coder-32b-instruct`          | ★★★★★       | `Code`      | `Fast`     | The only dedicated code model on Cloudflare's edge network — responds instantly with clean, no-preamble output. |
| `@cf/aisingapore/gemma-sea-lion-v4-27b-it`     | ★★★★☆       | `General`   | `Fast`     | Punchy multilingual model with surprising competence for its size.                                              |
| `@cf/google/gemma-4-26b-a4b-it`                | ★★★★☆       | `General`   | `Fast`     | Clean, thoughtful responses that don't waste your time.                                                         |
| `@cf/meta/llama-3.2-1b-instruct`               | ★★★★☆       | `Fallback`  | `Blazing`  | The tiniest model that still passes verification — use it when every resource counts.                           |
| `@cf/meta/llama-3.2-3b-instruct`               | ★★★★☆       | `Fallback`  | `Blazing`  | Syntax checks finish before you finish typing — the instant-sanity-check model.                                 |
| `@cf/meta/llama-3.3-70b-instruct-fp8-fast`     | ★★★★☆       | `Reasoning` | `Fast`     | Strong instruction-following at edge speed with good depth.                                                     |
| `@cf/meta/llama-4-scout-17b-16e-instruct`      | ★★★★☆       | `General`   | `Fast`     | Direct answers without the overhead of a full-parameter model.                                                  |
| `@cf/moonshotai/kimi-k2.6`                     | ★★★★☆       | `Reasoning` | `Fast`     | 1T multimodal MoE for long-horizon coding and agentic tool use with edge speed.                                 |
| `@cf/moonshotai/kimi-k2.7-code`                | ★★★★☆       | `Reasoning` | `Moderate` | The one that actually reads your whole codebase for project-wide refactors.                                     |
| `@cf/nvidia/nemotron-3-120b-a12b`              | ★★★★☆       | `Reasoning` | `Moderate` | Keeps reasoning until it hits something useful — depth over speed.                                              |
| `@cf/openai/gpt-oss-120b`                      | ★★★★☆       | `Code`      | `Fast`     | The 120B headroom shows on hard problems — smaller models tap out, this keeps digging.                          |
| `@cf/openai/gpt-oss-20b`                       | ★★★★☆       | `General`   | `Fast`     | The guilt-free daily driver that handles most tasks without complaint.                                          |
| `@cf/qwen/qwen3-30b-a3b-fp8`                   | ★★★★☆       | `General`   | `Fast`     | Feels like a full-size model despite the tiny active footprint.                                                 |
| `@cf/zai-org/glm-4.7-flash`                    | ★★★★☆       | `Agent`     | `Fast`     | Snappy under heavy use — coding calls return before you notice the lag.                                         |
| `@cf/zai-org/glm-5.2`                          | ★★★★☆       | `General`   | `Fast`     | Latest GLM release — refined generation over 5.1 with consistent, clean edge responses.                         |
| `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | ★★★☆☆       | `Reasoning` | `Slow`     | Useful for debugging with visible reasoning, annoying when speed matters.                                       |
| `@cf/google/gemma-7b-it-lora`                  | ★★★☆☆       | `General`   | `Moderate` | Feels dated next to Gemma v4 — more verbose, less polished.                                                     |
| `@cf/ibm-granite/granite-4.0-h-micro`          | ★★★☆☆       | `General`   | `Slow`     | You'll trim its output constantly — only worth it if you need IBM Granite.                                      |
| `@cf/meta/llama-3.1-8b-instruct-fp8`           | ★★★☆☆       | `General`   | `Moderate` | Gets the job done but wraps answers in unnecessary preamble.                                                    |
| `@cf/meta/llama-3.2-11b-vision-instruct`       | ★★★☆☆       | `Vision`    | `Moderate` | Multimodal but verbose — overkill for text-only coding.                                                         |
| `@cf/mistralai/mistral-small-3.1-24b-instruct` | ★★★☆☆       | `General`   | `Slow`     | Feels sluggish for tight coding loops — fine for conversation, frustrating for quick edits.                     |
| `@cf/qwen/qwq-32b`                             | ★★★☆☆       | `Reasoning` | `Moderate` | Good at logic puzzles, but chain-of-thought preamble makes you wait.                                            |

### [Cohere AI](https://dashboard.cohere.com)

Cohere focuses on enterprise-grade NLP with their Command model family — built for RAG, tool use, and coding workflows. The free API tier offers replenishable credits with daily resets, and nearly every model delivers sub-second responses. Cohere AI currently has 10 models verified.

🎁 **Free Tier Quota:** 20 RPM / 1,000 API calls per month

🔗 **Base URL:** `https://api.cohere.com/v2`

| Free Model                    | Star Rating | Best For    | Speed      | Opinion                                                                                                      |
| :---------------------------- | :---------- | :---------- | :--------- | :----------------------------------------------------------------------------------------------------------- |
| `command-a-03-2025`           | ★★★★★       | `Agent`     | `Blazing`  | Cohere's flagship. Blazing fast with clean, direct command execution — ideal for agentic tool-use pipelines. |
| `c4ai-aya-vision-32b`         | ★★★★☆       | `Vision`    | `Moderate` | 32B vision-language model. Handles both code and visual context for UI-to-code workflows.                    |
| `command-a-vision-07-2025`    | ★★★★☆       | `Vision`    | `Fast`     | Vision variant of Command A. Process screenshots and diagrams alongside code.                                |
| `command-r-08-2024`           | ★★★★☆       | `General`   | `Fast`     | Fast general-purpose workhorse. Handles scripting, terminal commands, and single-file edits.                 |
| `command-r-plus-08-2024`      | ★★★★☆       | `Reasoning` | `Moderate` | High-capability reasoning engine. Reliable for complex multi-step logic and architectural analysis.          |
| `command-r7b-12-2024`         | ★★★★☆       | `Code`      | `Fast`     | Compact 7B for rapid-fire completions with minimal overhead.                                                 |
| `command-r7b-arabic-02-2025`  | ★★★★☆       | `General`   | `Fast`     | Arabic-optimized 7B variant. Clean responses for Arabic technical documentation.                             |
| `c4ai-aya-expanse-32b`        | ★★★☆☆       | `General`   | `Moderate` | 32B multilingual model that over-answers — adds noise in prompt chains.                                      |
| `command-a-reasoning-08-2025` | ★★★☆☆       | `Reasoning` | `Moderate` | Reasoning-focused variant. Minimal outputs suit internal chain-of-thought.                                   |
| `command-a-translate-08-2025` | ★★★☆☆       | `Fallback`  | `Fast`     | Translation-optimized model. Works for code but limited general coding utility.                              |

### [ElectronHub](https://electronhub.ai)

ElectronHub is a credit-based inference hub offering an enormous catalog of models from OpenAI, Google, Meta, Mistral, Cohere, DeepSeek, Qwen, Microsoft, and more through an OpenAI-compatible endpoint. The free tier provides 5 RPM with $0.25 in weekly credits — replenishes every week, but the dollar cap limits heavy usage. Best for targeted queries and efficient coding. No credit card required. ElectronHub currently has roughly 55 verified coding-relevant models — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 5 RPM / $0.25 Weekly Credits

🔗 **Base URL:** `https://api.electronhub.ai/v1`

| Free Model                           | Star Rating | Best For    | Speed      | Opinion                                                                                         |
| :----------------------------------- | :---------- | :---------- | :--------- | :---------------------------------------------------------------------------------------------- |
| `gpt-oss-120b`                       | ★★★★★       | `General`   | `Blazing`  | The same reliable 120B flagship. Sub-second responses stretch your $0.25 weekly credit further. |
| `mistral-large-3-675b-instruct-2512` | ★★★★★       | `General`   | `Blazing`  | Mistral's 675B monster — elite reasoning at sub-second speed. Best model on ElectronHub.        |
| `nemotron-3-ultra-550b-a55b`         | ★★★★★       | `General`   | `Moderate` | NVIDIA's 550B flagship. Raw horsepower for the hardest prompts when credits allow.              |
| `codestral-latest`                   | ★★★★☆       | `Code`      | `Blazing`  | Mistral's coding specialist. Fast completions with strong multi-file awareness.                 |
| `gemini-2.5-flash`                   | ★★★★☆       | `General`   | `Fast`     | Google's reliable flash model. Steady throughput for background coding tasks.                   |
| `gpt-4.1`                            | ★★★★☆       | `General`   | `Fast`     | Reliable workhorse — handles daily coding with consistent, efficient output.                    |
| `gpt-4o`                             | ★★★★☆       | `General`   | `Fast`     | Proven workhorse. Efficient token usage helps stretch your weekly credit budget.                |
| `gpt-5.1-codex-mini`                 | ★★★★☆       | `Code`      | `Fast`     | Purpose-built codex variant. Clean code generation with efficient token consumption.            |
| `gpt-oss-20b`                        | ★★★★☆       | `Code`      | `Blazing`  | Same reliable DNA as the 120B, lighter and faster. Best value for the weekly credit cap.        |
| `llama-3.3-70b-instruct`             | ★★★★☆       | `General`   | `Blazing`  | Meta's benchmark engine. Fast and reliable for daily coding within the weekly budget.           |
| `mistral-large-latest`               | ★★★★☆       | `General`   | `Fast`     | Mistral's 123B flagship. Strong reasoning with clean instruction following.                     |
| `o3-mini`                            | ★★★★☆       | `Reasoning` | `Moderate` | OpenAI's reasoning specialist. Strong chain-of-thought for complex debugging sessions.          |
| `phi-4`                              | ★★★★☆       | `General`   | `Blazing`  | Microsoft's compact 14B — punches above its weight. Efficient and responsive for quick tasks.   |
| `qwen-2.5-coder-32b-instruct`        | ★★★★☆       | `Code`      | `Blazing`  | Qwen's coding specialist. Strong code generation at sub-second speed with efficient token use.  |
| `step-3.5-flash`                     | ★★★★☆       | `Agentic`   | `Blazing`  | Agentic powerhouse — 74.4% SWE-bench. Tiny 11B active params deliver shocking value.            |

### [FastRouter](https://fastrouter.ai)

FastRouter is a lightweight inference hub offering Sarvam AI models with a `:free` suffix through an OpenAI-compatible endpoint. The free tier provides 10 requests per day per model with no billing credits required — a tight cap suited for occasional queries and model evaluation. No credit card required. FastRouter currently has 2 models verified — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 10 RPD per model / No Billing Credits Required

🔗 **Base URL:** `https://api.fastrouter.ai/api/v1`

| Free Model                | Star Rating | Best For  | Speed     | Opinion                                                                                        |
| :------------------------ | :---------- | :-------- | :-------- | :--------------------------------------------------------------------------------------------- |
| `sarvam/sarvam-105b:free` | ★★★★☆       | `General` | `Fast`    | Sarvam's 105B flagship — strong multilingual reasoning with solid general coding capability.   |
| `sarvam/sarvam-30b:free`  | ★★★★☆       | `General` | `Blazing` | Compact 30B variant. Faster responses for lighter tasks, the 105B is better for complex logic. |

### [GitHub Models](https://github.com/marketplace/models)

GitHub Models provides free API access to models from OpenAI, Meta, Mistral, and others using your existing GitHub account — no new signup needed. Free tier quotas are modest (request-based limits), making it best for prototyping and personal projects. GitHub Models currently has 3 models verified.

🎁 **Free Tier Quota:** 10 to 15 RPM / 50 to 150 RPD

🔗 **Base URL:** `https://models.inference.ai.azure.com`

| Free Model                     | Star Rating | Best For    | Speed      | Opinion                                                                                                                          |
| :----------------------------- | :---------- | :---------- | :--------- | :------------------------------------------------------------------------------------------------------------------------------- |
| `Meta-Llama-3.1-405B-Instruct` | ★★★★★       | `Reasoning` | `Moderate` | The best model on GitHub Models. 405B of deep reasoning at zero cost — add system prompt "no markdown" for clean agentic output. |
| `gpt-4o-mini`                  | ★★★★☆       | `General`   | `Fast`     | Compact, fast, and clean. Reliable fallback when your bigger model quota runs low for the day.                                   |
| `gpt-4o`                       | ★★★★☆       | `General`   | `Moderate` | Full OpenAI flagship. Adds markdown by default, but a simple system prompt fixes it — strong all-around for chat and coding.     |

### [Google Gemini](https://aistudio.google.com)

Gemini offers large context windows on paper, but the free tier's **rate limits vary by model** — Flash-lite variants enjoy ~500 RPD, while standard models can be as low as 20 RPD. Use Gemini for quick, targeted tasks and single-file edits — not marathon sessions. Google Gemini currently has 8 models verified.

🎁 **Free Tier Quota:** 15–30 RPM / 1,500 RPD / 1M TPM / Uncapped TPD

🔗 **Base URL:** `https://generativelanguage.googleapis.com/v1beta`

| Free Model                                               | Star Rating | Best For    | Speed     | Opinion                                                                                             |
| :------------------------------------------------------- | :---------- | :---------- | :-------- | :-------------------------------------------------------------------------------------------------- |
| `models/gemini-3.1-flash-lite`                           | ★★★★★       | `General`   | `Blazing` | Lightning-fast, no-fuss outputs. Handles daily coding comfortably with ~500 RPD.                    |
| `models/gemma-4-31b-it`                                  | ★★★★☆       | `General`   | `Fast`    | Highly responsive and incredibly smart. Occasionally overthinks simple instructions.                |
| `models/gemini-2.5-flash-lite`                           | ★★★☆☆       | `Fallback`  | `Blazing` | Fast bare-bones lite variant. Useful as a lightweight backup for simple tasks.                      |
| `models/gemini-2.5-flash`                                | ★★★☆☆       | `Fallback`  | `Fast`    | Solid backup for standard context sizes. Newer Gemini 3 leaves it behind on complex logic.          |
| `models/gemini-3-flash-preview`                          | ★★★☆☆       | `Reasoning` | `Fast`    | Outstanding intelligence. Deep reasoning with large contexts, but tight ~20 RPD limits.             |
| `models/gemini-3.1-flash-lite-preview`                   | ★★★☆☆       | `Fallback`  | `Blazing` | Preview of the BEST model. Nearly identical speed and quality, but experimental.                    |
| `models/gemini-3.5-flash` / `models/gemini-flash-latest` | ★★★☆☆       | `Code`      | `Fast`    | Improved reasoning over prior flash variants. ~20 RPD prevents sustained agentic use.               |
| `models/gemini-flash-lite-latest`                        | ★★★☆☆       | `General`   | `Blazing` | **LIGHT SCRIPTING ONLY.** Incredibly fast bare-bones lite variant. Lacks depth for multi-file work. |

### [Groq API](https://console.groq.com)

Groq is famous for providing the **absolute lowest streaming latency** in the API market, outrunning traditional cloud providers by a massive margin. The free tier offers 30 RPM with replenishable daily credits — no credit card needed. If you want a setup where your terminal files patch instantly without the typical spinning wheel delay, this is your go-to. Groq API currently has 8 models verified.

🎁 **Free Tier Quota:** 30 RPM / 14,400 RPD / 18,000 TPM

🔗 **Base URL:** `https://api.groq.com/openai/v1`

| Free Model                                  | Star Rating | Best For  | Speed      | Opinion                                                                                          |
| :------------------------------------------ | :---------- | :-------- | :--------- | :----------------------------------------------------------------------------------------------- |
| `openai/gpt-oss-120b`                       | ★★★★★       | `Code`    | `Blazing`  | The undisputed champion. Rarely gets confused by tricky code logic, never hits rate-limit walls. |
| `llama-3.3-70b-versatile`                   | ★★★★☆       | `Chat`    | `Fast`     | Dependable for developer conversations and brainstorming.                                        |
| `openai/gpt-oss-20b`                        | ★★★★☆       | `Code`    | `Blazing`  | Same coding DNA as the 120b. Lightning-fast for standard tasks.                                  |
| `qwen/qwen3-32b`                            | ★★★★☆       | `Code`    | `Moderate` | Phenomenal for complex code blocks. Briefly thinks out loud before responding.                   |
| `qwen/qwen3.6-27b`                          | ★★★★☆       | `Code`    | `Blazing`  | Fast 27B Qwen 3.6. Brief `<think>` preamble but clean output and blazing speed.                  |
| `groq/compound`                             | ★★★☆☆       | `General` | `Fast`     | Great for single-turn terminal questions. Lacks depth for multi-file projects.                   |
| `llama-3.1-8b-instant`                      | ★★★☆☆       | `Code`    | `Blazing`  | Fun for tiny, rapid-fire edits — tends to cut off on long scripts.                               |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ★★★☆☆       | `Chat`    | `Fast`     | Handles medium tasks. Overthinks simple prompts.                                                 |

### [HelixMind](https://helixmind.online)

HelixMind is a lightweight inference hub offering a small set of free models from Meta, OpenAI, Mistral, and DeepSeek through an OpenAI-compatible endpoint. The free tier provides 3 RPM with 50 requests per day — the tightest cap on this list, strictly for occasional queries and quick tests. No credit card required. HelixMind currently has 5 models verified — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 3 RPM / 50 RPD

🔗 **Base URL:** `https://helixmind.online/v1`

| Free Model             | Star Rating | Best For    | Speed     | Opinion                                                                                            |
| :--------------------- | :---------- | :---------- | :-------- | :------------------------------------------------------------------------------------------------- |
| `deepseek-v3.2`        | ★★★★☆       | `Reasoning` | `Fast`    | 73.1% SWE-bench. The best model on HelixMind — make each of your 50 daily requests count.          |
| `gpt-oss-20b`          | ★★★★☆       | `Code`      | `Fast`    | Reliable light flagship. Best value for the restrictive 50 RPD — efficient token usage.            |
| `llama-4-maverick`     | ★★★★☆       | `General`   | `Blazing` | Meta's 17B MoE. Fast and responsive for quick edits within the tight daily limit.                  |
| `llama-4-scout`        | ★★★★☆       | `General`   | `Fast`    | Meta's scout variant. Solid fallback when Maverick is rate-limited.                                |
| `mistral-large-latest` | ★★★★☆       | `General`   | `Slow`    | Mistral's 123B flagship with strong reasoning, but 27s latency makes it impractical for daily use. |

### [Hugging Face Inference API](https://huggingface.co/inference-api)

Hugging Face's free Inference API gives you access to thousands of community-hosted models with OpenAI-compatible endpoints. The free tier offers $0.10/month in credits — enough for light experimentation, not sustained coding. The real strength is model diversity: 19 ★★★★★ models ranging from 3B to 1T parameters. Hugging Face currently has approximately 80 models verified — 27 are ★★★★☆ or above.

🎁 **Free Tier Quota:** $0.10/month credits (~650K tokens)

🔗 **Base URL:** `https://router.huggingface.co/v1`

| Free Model                                          | Star Rating | Best For    | Speed      | Opinion                                                                                            |
| :-------------------------------------------------- | :---------- | :---------- | :--------- | :------------------------------------------------------------------------------------------------- |
| `CohereLabs/c4ai-command-a-03-2025`                 | ★★★★★       | `Agent`     | `Fast`     | Reliable tool-calling workflows that follow structured instructions.                               |
| `deepcogito/cogito-671b-v2.1`                       | ★★★★★       | `Reasoning` | `Slow`     | An unfair advantage. The sheer reasoning depth is shocking.                                        |
| `deepseek-ai/DeepSeek-R1`                           | ★★★★★       | `Reasoning` | `Moderate` | Walks through reasoning step by step without cluttering the output.                                |
| `deepseek-ai/DeepSeek-V3.1`                         | ★★★★★       | `Reasoning` | `Fast`     | Solid alternative to Auriko for V3.1 — 1,000 RPD with the same elite quality.                      |
| `deepseek-ai/DeepSeek-V3.2`                         | ★★★★★       | `Reasoning` | `Fast`     | Multi-file architecture work where it never loses the thread.                                      |
| `EssentialAI/rnj-1-instruct`                        | ★★★★★       | `General`   | `Blazing`  | Responds before you finish typing. Uncanny speed for an 8B-class model.                            |
| `google/gemma-4-26B-A4B-it`                         | ★★★★★       | `General`   | `Fast`     | Responds faster than its size suggests with clean, direct output.                                  |
| `google/gemma-4-31B-it`                             | ★★★★★       | `General`   | `Fast`     | Gemma 4 at full 31B. Cleaner and smarter than the 26B. Follows instructions on the first try.      |
| `inclusionAI/Ling-2.6-1T`                           | ★★★★★       | `Reasoning` | `Slow`     | A trillion-parameter model for free — immense knowledge and reasoning.                             |
| `meta-llama/Llama-3.1-70B-Instruct`                 | ★★★★★       | `General`   | `Fast`     | The workhorse that keeps delivering under heavy use.                                               |
| `meta-llama/Llama-3.3-70B-Instruct`                 | ★★★★★       | `General`   | `Fast`     | Follows complex instructions precisely on the first try.                                           |
| `MiniMaxAI/MiniMax-M3`                              | ★★★★★       | `General`   | `Blazing`  | MiniMax M3 — 80.5% SWE-bench Verified with 1M context. Frontier-class coding at blazing speed.     |
| `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`    | ★★★★★       | `Reasoning` | `Moderate` | Clean, precise output on every turn — feels too big to be free.                                    |
| `Qwen/Qwen2.5-72B-Instruct`                         | ★★★★★       | `Fallback`  | `Fast`     | A reliable fallback that handles most coding tasks competently.                                    |
| `Qwen/Qwen2.5-Coder-32B-Instruct`                   | ★★★★★       | `Code`      | `Fast`     | Purpose-built 32B coder with focused output. Drops code without preamble.                          |
| `Qwen/Qwen3-235B-A22B-Instruct-2507`                | ★★★★★       | `Code`      | `Fast`     | 235B capacity with snappy response times — immense power without the wait.                         |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct`                 | ★★★★★       | `Code`      | `Fast`     | Deep, structured reasoning at 30B quality on a 3B budget.                                          |
| `Qwen/Qwen3-Coder-480B-A35B-Instruct`               | ★★★★★       | `Code`      | `Moderate` | Tackles the hardest debugging and architecture problems. The largest purpose-built code model.     |
| `Qwen/Qwen3-Coder-Next`                             | ★★★★★       | `Code`      | `Blazing`  | Generation, completion, debugging — no preamble noise. The strongest coding model on Hugging Face. |
| `swiss-ai/Apertus-70B-Instruct-2509`                | ★★★★★       | `General`   | `Moderate` | Llama-class reasoning quality without the attitude. Solid and dependable.                          |
| `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | ★★★★☆       | `General`   | `Fast`     | Llama 4's strongest instruct variant. Clean and dependable for daily coding.                       |
| `moonshotai/Kimi-K2.5`                              | ★★★★☆       | `Reasoning` | `Moderate` | Deep reasoning with chain-of-thought. Strong for logic-heavy debugging.                            |
| `openai/gpt-oss-120b`                               | ★★★★☆       | `General`   | `Fast`     | Proven across every provider — reliable as ever with clean output.                                 |
| `pearl-ai/Gemma-4-31B-it-pearl`                     | ★★★★☆       | `General`   | `Fast`     | Fine-tuned Gemma 4 variant. Slightly different flavor with the same clean base quality.            |
| `Qwen/Qwen2.5-Coder-7B-Instruct`                    | ★★★★☆       | `Code`      | `Blazing`  | Compact 7B coder for rapid-fire completions. Small enough to hammer all day.                       |
| `Qwen/Qwen3.6-35B-A3B`                              | ★★★★☆       | `Code`      | `Fast`     | The most efficient model on the list. Modern Qwen quality for rapid iteration.                     |
| `zai-org/GLM-4.7`                                   | ★★★★☆       | `General`   | `Fast`     | Optimized for throughput — hammer it all day and it keeps responding.                              |

### [Kilo Code](https://app.kilo.ai)

Kilo Code is a coding-agent platform that proxies free models from OpenRouter, NVIDIA, Poolside, and others through a single API key. The free tier offers generous replenishable credits with no hard daily cap — a solid Swiss-army-knife provider that gives you access to a diverse model pool through one endpoint. Kilo Code currently has 11 models verified.

🎁 **Free Tier Quota:** 5 RPM / 200 RPD

🔗 **Base URL:** `https://api.kilo.ai/api/gateway`

| Free Model                                           | Star Rating | Best For    | Speed      | Opinion                                                                           |
| :--------------------------------------------------- | :---------- | :---------- | :--------- | :-------------------------------------------------------------------------------- |
| `kilo-auto/small`                                    | ★★★★★       | `General`   | `Fast`     | Kilo's own routing picks the right model — the no-brainer choice.                 |
| `nvidia/nemotron-3-ultra-550b-a55b:free`             | ★★★★★       | `General`   | `Moderate` | The 550B nemotron flagship — raw horsepower for the hardest prompts on Kilo Code. |
| `openrouter/owl-alpha`                               | ★★★★★       | `Agent`     | `Fast`     | Zero preamble, straight answers. The safest pick on Kilo Code.                    |
| `cohere/north-mini-code:free`                        | ★★★★☆       | `Code`      | `Blazing`  | Efficient coding model from Cohere. Lightweight enough for rapid iteration loops. |
| `kilo-auto/free`                                     | ★★★★☆       | `Fallback`  | `Moderate` | Kilo's fallback router — always lands on something functional.                    |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ★★★★☆       | `Reasoning` | `Moderate` | Shows its work step by step. Useful for verification, noisy for quick answers.    |
| `nvidia/nemotron-3-super-120b-a12b:free`             | ★★★★☆       | `General`   | `Fast`     | Strong 120B mid-range with 1M context. Steps in when the 30Bs need more headroom. |
| `openrouter/free`                                    | ★★★★☆       | `Fallback`  | `Moderate` | Routes through OpenRouter's free pool — a good backup when others are tapped.     |
| `poolside/laguna-m.1:free`                           | ★★★★☆       | `Code`      | `Blazing`  | More headroom than XS for trickier edits. Still fast and focused.                 |
| `poolside/laguna-xs.2:free`                          | ★★★★☆       | `Code`      | `Blazing`  | Built for inline edits — stays out of your way and finishes before you blink.     |
| `stepfun/step-3.7-flash:free`                        | ★★★★☆       | `General`   | `Fast`     | Dependable and drama-free. Perfect for everyday edits.                            |

### [LLM7.IO](https://llm7.io)

LLM7.IO is a rising inference provider serving open-weight models via Llama.cpp server with OpenAI-compatible endpoints. The free tier offers replenishable credits with no daily hard cap — a solid option if you want to test heavyweight models (up to 235B) on a simple API without commitment. LLM7.IO currently has 3 models verified.

🎁 **Free Tier Quota:** 128 RPM / ~7,200 RPD / 5M TPD (Free Token Users Only)

🔗 **Base URL:** `https://api.llm7.io/v1`

| Free Model          | Star Rating | Best For  | Speed      | Opinion                                                                                        |
| :------------------ | :---------- | :-------- | :--------- | :--------------------------------------------------------------------------------------------- |
| `qwen3-235b`        | ★★★★★       | `Code`    | `Fast`     | Handles multi-file architecture cleanly with zero preamble. Remarkably fluid for a 235B model. |
| `codestral-latest`  | ★★★★☆       | `Code`    | `Fast`     | Strongest coding option here after Qwen. Adds a brief preamble but completions are solid.      |
| `mistral-small-3.2` | ★★★☆☆       | `General` | `Moderate` | Adequate for chat and scripting, but the verbose preamble kills the flow.                      |

### [LLMGateway](https://llmgateway.io)

LLMGateway is a lightweight inference hub serving models from Zhipu AI and more through its gateway at $0 per 1M tokens — a genuinely free per-token pricing model with no credit cap. The free tier offers 5 requests per 10 minutes with no daily token limit, making it practical for light coding and scripting tasks. No credit card required. LLMGateway currently has 2 models verified — both at ★★★★☆ or above.

🎁 **Free Tier Quota:** 5 requests per 10 minutes / $0 per 1M tokens

🔗 **Base URL:** `https://api.llmgateway.io/v1`

| Free Model       | Star Rating | Best For   | Speed     | Opinion                                                                                            |
| :--------------- | :---------- | :--------- | :-------- | :------------------------------------------------------------------------------------------------- |
| `glm-4.5-flash`  | ★★★★☆       | `Fallback` | `Fast`    | Older flash variant. Handles basic scripting and text tasks with direct output — no wasted tokens. |
| `glm-4.6v-flash` | ★★★★☆       | `General`  | `Blazing` | Newer flash variant with vision support. Fast, clean responses with no token-wasting preamble.     |

### [LiteRouter](https://literouter.com)

LiteRouter is a lightweight inference hub offering free models from OpenAI, DeepSeek, Mistral, Meta, and more through an OpenAI-compatible endpoint with a `:free` suffix. The free tier provides uncapped daily requests with 1 concurrent request and 15,000 tokens per day — enough for light scripting and targeted queries. No credit card required. LiteRouter currently has 3 models verified — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 1 Concurrent Request / 15,000 TPD / Uncapped RPD

🔗 **Base URL:** `https://api.literouter.com/v1`

| Free Model           | Star Rating | Best For    | Speed      | Opinion                                                                                       |
| :------------------- | :---------- | :---------- | :--------- | :-------------------------------------------------------------------------------------------- |
| `gpt-oss-120b:free`  | ★★★★★       | `General`   | `Fast`     | The same reliable 120B flagship. Make each of your 15k daily tokens count with efficient use. |
| `deepseek-v3.2:free` | ★★★★☆       | `Reasoning` | `Moderate` | 73.1% SWE-bench. Strong reasoning for complex debugging within the tight token budget.        |
| `gpt-oss-20b:free`   | ★★★★☆       | `Code`      | `Blazing`  | Reliable light flagship. Best value for the 15k TPD cap — efficient token usage per response. |

### [MNN AI](https://mnnai.ru)

MNN AI is a credit-based inference hub offering models from OpenAI, Google, DeepSeek, Qwen, Meta, Mistral, Moonshot, Stepfun, and more through an OpenAI-compatible endpoint. The free tier provides 10 RPM with $1 in monthly credits — replenishable each month, but the dollar cap limits heavy usage. Best suited for light daily coding and targeted queries. No credit card required. MNN AI currently has roughly 25 verified coding-relevant models — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 10 RPM / $1 Monthly Credits

🔗 **Base URL:** `https://api2.mnnai.ru/v1`

| Free Model           | Star Rating | Best For    | Speed      | Opinion                                                                                      |
| :------------------- | :---------- | :---------- | :--------- | :------------------------------------------------------------------------------------------- |
| `deepseek-v4-flash`  | ★★★★★       | `Reasoning` | `Blazing`  | Elite flash variant with 79.0% SWE-bench. Blazing speed for the hardest reasoning prompts.   |
| `gpt-5.2`            | ★★★★★       | `General`   | `Fast`     | Proven GPT generation model. Clean, direct output with no preamble noise.                    |
| `gpt-5.3-chat`       | ★★★★★       | `General`   | `Fast`     | Latest GPT chat variant with polished output. Top pick on MNN for daily coding tasks.        |
| `gpt-oss-120b`       | ★★★★★       | `General`   | `Blazing`  | The same reliable 120B flagship. Sub-second responses that stretch your $1 credit further.   |
| `qwen-3-235b-a22b`   | ★★★★★       | `General`   | `Fast`     | 235B Qwen3 flagship — deep multi-file reasoning at competitive speed.                        |
| `qwen-3.5-397b-a17b` | ★★★★★       | `General`   | `Moderate` | 397B MoE flagship — 76.4% SWE-bench. Immense capacity for complex multi-file architecture.   |
| `gemini-3.5-flash`   | ★★★★☆       | `General`   | `Fast`     | Google's latest flash variant — capable reasoning at efficient token cost.                   |
| `gemma-4-31b-it`     | ★★★★☆       | `General`   | `Fast`     | Google's 31B dense model. Strong generalist for daily coding without overhead.               |
| `gpt-4.1`            | ★★★★☆       | `General`   | `Fast`     | Reliable workhorse — handles daily coding with consistent, structured output.                |
| `gpt-4o`             | ★★★★☆       | `General`   | `Fast`     | Proven workhorse. Efficient token usage helps stretch the $1 monthly credit cap.             |
| `gpt-oss-20b`        | ★★★★☆       | `Code`      | `Blazing`  | Same reliable DNA as the 120B, lighter and faster. Best value for the monthly credit budget. |
| `kimi-k2.5`          | ★★★★☆       | `Reasoning` | `Fast`     | Moonshot's strong reasoning model. Solid for complex multi-step analysis.                    |
| `llama-4-maverick`   | ★★★★☆       | `General`   | `Blazing`  | Meta's latest 17B MoE. Responsive and reliable for lightweight coding tasks.                 |
| `qwen-3-coder-plus`  | ★★★★☆       | `Code`      | `Fast`     | Qwen's coding-specialized variant. Clean code output with strong instruction following.      |
| `step-3.5-flash`     | ★★★★☆       | `Agentic`   | `Blazing`  | Agentic powerhouse — 74.4% SWE-bench. Tiny 11B active params punch far above weight.         |

### [MegaNova AI](https://meganova.ai)

MegaNova AI is a community-model inference hub offering fine-tuned variants of Llama, Mistral, and its own Manta series through an OpenAI-compatible endpoint. The free tier provides 60 RPM with 550 requests per day and 200,000 tokens per minute — generous throughput for a community model hub. No credit card required. MegaNova AI currently has 6 models verified — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 60 RPM / 550 RPD / 200,000 TPM

🔗 **Base URL:** `https://api.meganova.ai/v1`

| Free Model                                      | Star Rating | Best For  | Speed     | Opinion                                                                                           |
| :---------------------------------------------- | :---------- | :-------- | :-------- | :------------------------------------------------------------------------------------------------ |
| `BruhzWater/Sapphira-L3.3-70b-0.1`              | ★★★★☆       | `General` | `Fast`    | Llama 3.3 70B fine-tune — strong reasoning depth with polished instruction following.             |
| `meganova-ai/manta-flash-1.0`                   | ★★★★☆       | `General` | `Blazing` | MegaNova's own flash variant — fast, clean responses with solid general coding capability.        |
| `meganova-ai/manta-mini-1.0`                    | ★★★★☆       | `General` | `Blazing` | Compact Manta variant. Efficient for lightweight tasks and quick edits at blazing speed.          |
| `mistralai/Mistral-Small-3.2-24B-Instruct-2506` | ★★★★☆       | `General` | `Fast`    | Official Mistral 24B — clean instruction following at a strong quality-to-speed ratio.            |
| `Sao10K/L3-70B-Euryale-v2.1`                    | ★★★★☆       | `General` | `Fast`    | Community Llama 3 70B fine-tune. Solid general-purpose coding with consistent output.             |
| `Steelskull/L3.3-MS-Nevoria-70b`                | ★★★★☆       | `General` | `Fast`    | Another 70B community fine-tune. Reliable output for daily coding with good structural awareness. |

### [Mistral AI](https://console.mistral.ai)

Mistral AI is highly regarded for building models that punch far above their **parameter weight class**, with exceptionally clean instruction following and compact execution. The free tier offers replenishable credits with generous RPM limits. Mistral AI currently has 42 models verified (with aliases) — 24 are ★★★☆☆ or above.

🎁 **Free Tier Quota:** ~2–30 RPM / 50,000 TPM shared pool

🔗 **Base URL:** `https://api.mistral.ai/v1`

| Free Model                                          | Star Rating | Best For    | Speed      | Opinion                                                                                                            |
| :-------------------------------------------------- | :---------- | :---------- | :--------- | :----------------------------------------------------------------------------------------------------------------- |
| `mistral-code-agent-latest`                         | ★★★★★       | `Agent`     | `Fast`     | **BEST FOR AGENTS.** Purpose-built for autonomous agents with native tool use.                                     |
| `codestral-latest` / `codestral-2508`               | ★★★★☆       | `Code`      | `Fast`     | **CODE COMPLETION ONLY.** Built for programmers. Flies through auto-completions and inline edits.                  |
| `devstral-medium-latest`                            | ★★★★☆       | `Agent`     | `Moderate` | **AGENT ROUTING ONLY.** Streamlined Medium optimized for automated developer task loops.                           |
| `magistral-medium-latest` / `magistral-medium-2509` | ★★★★☆       | `Reasoning` | `Fast`     | Medium-tier Magistral. Strong reasoning with clean, structured output.                                             |
| `magistral-small-latest` / `magistral-small-2509`   | ★★★★☆       | `General`   | `Fast`     | New Mistral line. Clean responses with solid depth. A pleasant surprise.                                           |
| `mistral-code-fim-latest`                           | ★★★★☆       | `Code`      | `Fast`     | **CODE COMPLETION ONLY.** Fill-in-Middle specialist for smart inline insertion.                                    |
| `mistral-code-latest`                               | ★★★★☆       | `Code`      | `Fast`     | **CODE COMPLETION ONLY.** Fast, precise completions across dozens of languages.                                    |
| `mistral-large-latest` / `mistral-large-2512`       | ★★★★☆       | `Reasoning` | `Fast`     | Strong multi-lingual reasoning but lacks code-specific architecture. The 50k TPM shared pool limits sustained use. |
| `mistral-medium-2604`                               | ★★★★☆       | `General`   | `Fast`     | Responsive Medium iteration with predictable execution and strong structural debugging.                            |
| `mistral-medium-3.5` / `mistral-medium-3-5`         | ★★★★☆       | `General`   | `Fast`     | Exceptional price-to-performance. Highly responsive for structural software layouts.                               |
| `mistral-medium-3`                                  | ★★★★☆       | `General`   | `Fast`     | Trusted, stable Medium line. Clean boilerplate code without empty chatter.                                         |
| `mistral-medium-latest` / `mistral-medium`          | ★★★★☆       | `General`   | `Fast`     | The classic production model. Dependable for everyday scripting.                                                   |
| `mistral-small-latest` / `mistral-small-2603`       | ★★★★☆       | `General`   | `Blazing`  | Incredible lightweight architecture. Punchy, direct tone with surprising depth.                                    |
| `devstral-latest` / `devstral-2512`                 | ★★★☆☆       | `Agent`     | `Moderate` | **AGENT ROUTING ONLY.** Tailored for programmatic tool use.                                                        |
| `ministral-14b-latest` / `ministral-14b-2512`       | ★★★☆☆       | `General`   | `Fast`     | Nimble, edge-focused model. Remarkably capable for its tight memory footprint.                                     |
| `ministral-8b-latest` / `ministral-8b-2512`         | ★★★☆☆       | `General`   | `Fast`     | 8B ministral. Nimble and responsive for lightweight coding tasks.                                                  |
| `mistral-medium-2505`                               | ★★★☆☆       | `Fallback`  | `Slow`     | Early Medium build. Tends to use full-sentence prefix framing.                                                     |
| `mistral-medium-2508`                               | ★★★☆☆       | `Fallback`  | `Moderate` | Older Medium point-release. Clean output but lacks the 3.x optimization pass.                                      |
| `mistral-small-2506`                                | ★★★☆☆       | `Fallback`  | `Moderate` | Earlier Small snapshot. Trails 2603 on speed.                                                                      |
| `mistral-tiny-latest` / `mistral-tiny-2407`         | ★★★☆☆       | `Fallback`  | `Blazing`  | Fastest Mistral model. Perfect for syntax checks and terminal one-liners.                                          |
| `mistral-vibe-cli-fast`                             | ★★★☆☆       | `Agent`     | `Blazing`  | **TERMINAL HELPER.** Blistering single-turn replies for terminal flags.                                            |
| `mistral-vibe-cli-latest`                           | ★★★☆☆       | `Agent`     | `Moderate` | **TERMINAL HELPER.** Favors explicit sentence explanations when breaking down commands.                            |
| `mistral-vibe-cli-with-tools`                       | ★★★☆☆       | `Agent`     | `Fast`     | **TERMINAL HELPER.** Returns raw executable bash tokens with zero conversational prefix.                           |
| `open-mistral-nemo` / `open-mistral-nemo-2407`      | ★★★☆☆       | `Fallback`  | `Fast`     | Fast and flexible for low-complexity text filtering.                                                               |

### [Mixlayer](https://www.mixlayer.com)

Mixlayer is an inference platform for open-source AI models with an OpenAI-compatible API. The free tier offers `qwen/qwen3.5-4b-free` for prototyping with rate limits — no credit card required for the free model. A focused Qwen 3.5/3.6 catalog with tool calling and reasoning support. Mixlayer currently has 1 model verified.

🎁 **Free Tier Quota:** 20 RPM / Can be rate-limited (daily usage)

🔗 **Base URL:** `https://models.mixlayer.ai/v1`

| Free Model             | Star Rating | Best For  | Speed     | Opinion                                                                                                                              |
| :--------------------- | :---------- | :-------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `qwen/qwen3.5-4b-free` | ★★★★★       | `General` | `Blazing` | The only free model on Mixlayer — handles prototyping and lightweight tasks at blazing speed. Clean, direct output with no preamble. |

### [Naga AI](https://naga.ac)

Naga AI is a lightweight inference hub offering a small set of free models from NVIDIA and Meta through an OpenAI-compatible endpoint. The free tier provides 10 RPM with 100 requests per day — a very tight cap that limits it to occasional queries and quick debugging. No credit card required. Naga AI currently has 3 models verified — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 10 RPM / 100 RPD

🔗 **Base URL:** `https://api.naga.ac/v1`

| Free Model                            | Star Rating | Best For  | Speed     | Opinion                                                                                      |
| :------------------------------------ | :---------- | :-------- | :-------- | :------------------------------------------------------------------------------------------- |
| `llama-3.3-70b-instruct:free`         | ★★★★☆       | `General` | `Fast`    | The traditional benchmark engine. Reliable, well-rounded output for daily coding.            |
| `llama-4-scout-17b-16e-instruct:free` | ★★★★☆       | `General` | `Blazing` | Meta's latest 17B MoE scout — fast and responsive, but the 100 RPD cap limits sustained use. |
| `nemotron-3-super-120b-a12b:free`     | ★★★★☆       | `General` | `Fast`    | Strong 120B mid-range from NVIDIA. Steps in when smaller models need more headroom.          |

### [Navy API](https://api.navy)

Navy API is a high-volume inference hub offering an extensive catalog of models from OpenAI, DeepSeek, Grok, Google, Mistral, Cohere, Meta, and more through an OpenAI-compatible endpoint. The free tier provides 20 RPM with 250,000 daily tokens — enough throughput for serious coding sessions. No credit card required. Navy API currently has roughly 60 verified coding-relevant models — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 20 RPM / 250,000 TPD

🔗 **Base URL:** `https://api.navy/v1`

| Free Model             | Star Rating | Best For    | Speed      | Opinion                                                                                          |
| :--------------------- | :---------- | :---------- | :--------- | :----------------------------------------------------------------------------------------------- |
| `deepseek-v4-flash`    | ★★★★★       | `Reasoning` | `Blazing`  | Elite flash variant with 79.0% SWE-bench. Blazing speed with no daily cap on Navy.               |
| `deepseek-v4-pro`      | ★★★★★       | `Reasoning` | `Fast`     | Pro variant of V4 — 80.6% SWE-bench. Extra headroom over Flash for the hardest prompts.          |
| `gpt-5.2`              | ★★★★★       | `General`   | `Fast`     | Proven GPT generation model. Reliable output without preamble noise.                             |
| `gpt-5.3-chat-latest`  | ★★★★★       | `General`   | `Fast`     | Latest GPT chat variant. Strong all-rounder for both coding and conversation.                    |
| `gpt-5.4`              | ★★★★★       | `General`   | `Fast`     | Latest GPT flagship — frontier reasoning with clean, direct output. Top-tier daily driver.       |
| `gpt-oss-120b`         | ★★★★★       | `General`   | `Blazing`  | The same reliable 120B flagship. Clean output across every coding task at sub-second speed.      |
| `grok-4.20-reasoning`  | ★★★★★       | `Reasoning` | `Moderate` | xAI's strongest reasoning model. Deep chain-of-thought for the hardest logic problems.           |
| `qwen3.5-397b-a17b`    | ★★★★★       | `General`   | `Moderate` | 397B MoE flagship — 76.4% SWE-bench. Immense capacity for complex multi-file architecture.       |
| `codestral-latest`     | ★★★★☆       | `Code`      | `Blazing`  | Mistral's coding specialist — fast completions with strong multi-file awareness.                 |
| `command-a-plus`       | ★★★★☆       | `General`   | `Fast`     | Cohere's flagship — clean instruction following with solid coding chops.                         |
| `deepseek-v3.2`        | ★★★★☆       | `Reasoning` | `Fast`     | 73.1% SWE-bench. Refined V3 release with clean reasoning and strong coding capability.           |
| `gemma-4-31b-it`       | ★★★★☆       | `General`   | `Fast`     | Google's 31B dense model. Strong generalist for daily coding without the overhead.               |
| `gpt-4.1`              | ★★★★☆       | `General`   | `Fast`     | Reliable workhorse — handles daily coding with consistent, structured output.                    |
| `gpt-5.4-nano`         | ★★★★☆       | `Code`      | `Blazing`  | Lightning-fast GPT variant. Ideal for quick edits and inline completions.                        |
| `gpt-oss-20b`          | ★★★★☆       | `Code`      | `Blazing`  | Same reliable DNA as the 120B in a lighter package. Lightning-fast responses for everyday tasks. |
| `kimi-k2.6`            | ★★★★☆       | `Reasoning` | `Fast`     | 1T multimodal MoE from Moonshot. Strong long-horizon reasoning for complex projects.             |
| `mistral-large-latest` | ★★★★☆       | `General`   | `Fast`     | Mistral's 123B flagship — strong reasoning with exceptionally clean instruction following.       |

### [NVIDIA NIM](https://build.nvidia.com)

NVIDIA NIM is NVIDIA's free API catalog offering 100+ models from DeepSeek, Meta, Mistral, Google, Qwen, and more through OpenAI-compatible endpoints — no credit card required. The largest free model library on the list, but 40 RPM per model caps it as a backup pool rather than a daily driver. Only models tagged as **Free Endpoint** (hosted on NVIDIA's own infrastructure) are listed below. NVIDIA NIM currently has 56 models verified — 27 are ★★★★☆ or above.

🎁 **Free Tier Quota:** 40 RPM / Uncapped TPD

🔗 **Base URL:** `https://integrate.api.nvidia.com/v1`

> ⚠️ May require **Phone verification** to generate an API Key.

| Free Model                                      | Star Rating | Best For    | Speed      | Opinion                                                                                                    |
| :---------------------------------------------- | :---------- | :---------- | :--------- | :--------------------------------------------------------------------------------------------------------- |
| `deepseek-ai/deepseek-v4-flash`                 | ★★★★★       | `Code`      | `Blazing`  | Elite 284B MoE reasoning at blazing speed. The strongest coding model on NVIDIA NIM.                       |
| `deepseek-ai/deepseek-v4-pro`                   | ★★★★★       | `Reasoning` | `Fast`     | Pro variant of V4 with extra headroom for the hardest multi-file problems.                                 |
| `minimaxai/minimax-m3`                          | ★★★★★       | `General`   | `Blazing`  | Latest MiniMax flagship — 80.5% SWE-bench Verified with 1M context. Frontier-class coding at blazing speed |
| `mistralai/mistral-large-3-675b-instruct-2512`  | ★★★★★       | `General`   | `Fast`     | Mistral's 675B flagship — state-of-the-art general purpose with strong agentic capability.                 |
| `openai/gpt-oss-120b`                           | ★★★★★       | `General`   | `Blazing`  | The same 120B reliable flagship. Clean output across every coding task.                                    |
| `qwen/qwen3.5-397b-a17b`                        | ★★★★★       | `Reasoning` | `Moderate` | 397B MoE (17B active) — immense capacity for the hardest prompts at free-tier scale.                       |
| `z-ai/glm-5.1`                                  | ★★★★★       | `Code`      | `Slow`     | GLM's 2026 flagship. Strong agentic coding with structured output — worth the wait.                        |
| `abacusai/dracarys-llama-3.1-70b-instruct`      | ★★★★☆       | `Code`      | `Fast`     | Coding-specialized fine-tune of Llama 3.1 70B. Focused output for agentic workflows.                       |
| `bytedance/seed-oss-36b-instruct`               | ★★★★☆       | `General`   | `Fast`     | ByteDance's open-weight 36B — clean instruction following with solid coding capability.                    |
| `meta/llama-3.1-70b-instruct`                   | ★★★★☆       | `General`   | `Fast`     | The proven workhorse. Reliable across every coding task.                                                   |
| `meta/llama-3.3-70b-instruct`                   | ★★★★☆       | `General`   | `Fast`     | Strong instruction following — complex prompts executed precisely on the first try.                        |
| `meta/llama-4-maverick-17b-128e-instruct`       | ★★★★☆       | `General`   | `Fast`     | Latest Llama 4. Clean, dependable output for daily coding.                                                 |
| `minimaxai/minimax-m2.7`                        | ★★★★☆       | `General`   | `Fast`     | Proven 230B MoE with strong coding and reasoning. A solid mid-range daily driver.                          |
| `mistralai/mistral-medium-3.5-128b`             | ★★★★☆       | `General`   | `Fast`     | Reliable mid-range workhorse for everyday coding tasks and scripting.                                      |
| `mistralai/mistral-nemotron`                    | ★★★★☆       | `General`   | `Fast`     | Mistral × Nemotron collab — balanced reasoning and speed for general use.                                  |
| `mistralai/mistral-small-4-119b-2603`           | ★★★★☆       | `Code`      | `Fast`     | Hybrid MoE unifying instruct, reasoning, and coding with 256K context.                                     |
| `moonshotai/kimi-k2.6`                          | ★★★★☆       | `Reasoning` | `Fast`     | 1T multimodal MoE for long-horizon coding and agentic tool use.                                            |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5`      | ★★★★☆       | `General`   | `Fast`     | Updated v1.5 with cleaner output. Solid mid-range daily driver.                                            |
| `nvidia/llama-3.3-nemotron-super-49b-v1`        | ★★★★☆       | `General`   | `Fast`     | 49B Nemotron with clean, direct responses. Solid for daily coding without overhead.                        |
| `nvidia/nemotron-3-nano-30b-a3b`                | ★★★★☆       | `General`   | `Fast`     | 30B MoE (3B active) — efficient and responsive for lightweight daily tasks.                                |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ★★★★☆       | `Reasoning` | `Moderate` | Reasoning-focused variant of the 30B nano. Shows thorough chain-of-thought.                                |
| `nvidia/nemotron-3-super-120b-a12b`             | ★★★★☆       | `Reasoning` | `Fast`     | Strong 120B mid-range with 1M context. Steps in when smaller models need headroom.                         |
| `openai/gpt-oss-20b`                            | ★★★★☆       | `General`   | `Blazing`  | Same reliable DNA as the 120B in a lighter package. Lightning-fast responses.                              |
| `qwen/qwen3-next-80b-a3b-instruct`              | ★★★★☆       | `Code`      | `Fast`     | Next-gen Qwen 3 — 80B MoE (3B active). Efficient and responsive for coding.                                |
| `qwen/qwen3.5-122b-a10b`                        | ★★★★☆       | `Code`      | `Fast`     | 122B MoE with Qwen's elite coding quality. Strong reasoning at efficient active param count.               |
| `stepfun-ai/step-3.5-flash`                     | ★★★★☆       | `Agentic`   | `Blazing`  | Agentic powerhouse at 11B active params. Strong reasoning for daily coding.                                |
| `stepfun-ai/step-3.7-flash`                     | ★★★★☆       | `Agentic`   | `Blazing`  | Latest Step flash variant. Improved agentic coding with fast response times.                               |

### [Ollama Cloud](https://ollama.com)

Ollama Cloud is a cloud-hosted inference service running Ollama behind the scenes, offering a vast model registry without the need to run locally. The free tier provides replenishable credits with generous rate limits — most models respond cleanly and quickly, making it one of the strongest free providers for coding. Ollama Cloud currently has 21 models verified — 20 are ★★★☆☆ or above.

🎁 **Free Tier Quota:** 1 Instance / 5-Hour Session Usage / 7-day Weekly Usage

🔗 **Base URL:** `https://api.ollama.com`

| Free Model             | Star Rating | Best For    | Speed      | Opinion                                                                                                    |
| :--------------------- | :---------- | :---------- | :--------- | :--------------------------------------------------------------------------------------------------------- |
| `devstral-2:123b`      | ★★★★★       | `Agent`     | `Fast`     | Purpose-built for agent pipelines — structured tool-use without drift or hallucination.                    |
| `devstral-small-2:24b` | ★★★★★       | `Code`      | `Fast`     | Lean and responsive for everyday coding. Does 90% of what the 123B does.                                   |
| `gemma3:12b`           | ★★★★★       | `General`   | `Fast`     | Google's compact powerhouse. Follows complex instructions without rambling.                                |
| `gemma3:27b`           | ★★★★★       | `General`   | `Fast`     | Everything the 12B does well with more breathing room. The sweet spot.                                     |
| `gemma3:4b`            | ★★★★★       | `General`   | `Blazing`  | Blink-and-you-miss-it speed. Perfect for syntax checks.                                                    |
| `gemma4:31b`           | ★★★★★       | `General`   | `Fast`     | Google's latest 31B. Clean, responsive, and punches above its weight class.                                |
| `glm-4.7`              | ★★★★★       | `Reasoning` | `Moderate` | Takes a beat longer but the extra thought shows. Thorough answers when correctness beats speed.            |
| `gpt-oss:120b`         | ★★★★★       | `General`   | `Blazing`  | Consistent as gravity. Same quality across every provider, same clean output.                              |
| `minimax-m2.5`         | ★★★★★       | `General`   | `Fast`     | Consistent output that doesn't make you second-guess.                                                      |
| `minimax-m3`           | ★★★★★       | `General`   | `Fast`     | The most polished MiniMax yet. Clean, dependable for whatever your day throws at it.                       |
| `nemotron-3-nano:30b`  | ★★★★★       | `Reasoning` | `Fast`     | Fast, direct, and efficient. Answers without chain-of-thought fluff.                                       |
| `qwen3-coder-next`     | ★★★★★       | `Code`      | `Blazing`  | Zero preamble, instant answers. Reads terminal logs to fix its own bugs. Uncapped usage.                   |
| `qwen3-coder:480b`     | ★★★★★       | `Code`      | `Moderate` | 480B of pure coding muscle. Makes the toughest debugging sessions feel like a chat with a senior engineer. |
| `rnj-1:8b`             | ★★★★★       | `General`   | `Blazing`  | Don't let the 8B fool you — responds faster than most with surprising depth.                               |
| `gpt-oss:20b`          | ★★★★☆       | `Reasoning` | `Fast`     | Smaller GPT-OSS variant. Solid reasoning at a fraction of the 120B latency.                                |
| `nemotron-3-ultra`     | ★★★★☆       | `Reasoning` | `Blazing`  | 550B of raw power at blazing speed. Impressive when you can reach past the preamble.                       |
| `minimax-m2.1`         | ★★★☆☆       | `General`   | `Slow`     | Earlier MiniMax release. Empty clean output but noticeably slower than m2.5.                               |
| `ministral-3:14b`      | ★★★☆☆       | `General`   | `Fast`     | Nimble Mistral ministral. Compact but responsive for lightweight coding tasks.                             |
| `ministral-3:8b`       | ★★★☆☆       | `General`   | `Fast`     | 8B ministral variant. Reliable for quick edits and syntax checks.                                          |
| `nemotron-3-super`     | ★★★☆☆       | `Reasoning` | `Slow`     | Deep reasoning with significant latency. Capable but you'll wait for every answer.                         |

### [OpenCode Zen](https://opencode.ai/zen)

OpenCode Zen is a curated set of AI models tested and optimized for coding agents by the OpenCode team. The free tier offers 5 models at zero cost through an OpenAI-compatible API — no credit card or billing required for free models.

🎁 **Free Tier Quota:** 30 RPM / 500 RPD / 1,000,000 TPD / Daily Limits

🔗 **Base URL:** `https://opencode.ai/zen/v1`

| Free Model               | Star Rating | Best For      | Speed      | Opinion                                                                                                                                              |
| :----------------------- | :---------- | :------------ | :--------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deepseek-v4-flash-free` | ★★★★★       | `Code`        | `Fast`     | The strongest model on OpenCode Zen for coding. Handles multi-turn context tracking smoothly with rapid generation speeds.                           |
| `nemotron-3-ultra-free`  | ★★★★★       | `Code Review` | `Fast`     | Exceptional for code review and syntax linting — pedantic and precise when catching edge cases. Slightly clumsy at generating large template blocks. |
| `big-pickle`             | ★★★★☆       | `Fallback`    | `Fast`     | A strong, versatile fallback with rotating capabilities. Handles standard single-file scripting reliably.                                            |
| `mimo-v2.5-free`         | ★★★★☆       | `Code`        | `Moderate` | Lightweight model best kept for small tasks where brief patches matter more than deep logic.                                                         |
| `north-mini-code-free`   | ★★★★☆       | `Fallback`    | `Blazing`  | Micro-scale utility model suited for inline autocomplete or basic regex conversions.                                                                 |

### [OpenRouter](https://openrouter.ai)

OpenRouter is a unified API gateway providing access to hundreds of models from dozens of providers through a single endpoint. The free tier offers rate-limited access to community-hosted models (marked with `:free`) that changes often — no credit card required. A great backup when other providers are rate-limited. OpenRouter currently has 13 models verified — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 20 RPM / 50 RPD

🔗 **Base URL:** `https://openrouter.ai/api/v1`

| Free Model                                           | Star Rating | Best For    | Speed      | Opinion                                                                                   |
| :--------------------------------------------------- | :---------- | :---------- | :--------- | :---------------------------------------------------------------------------------------- |
| `google/gemma-4-31b-it:free`                         | ★★★★★       | `General`   | `Fast`     | Extra headroom over the 26B without sacrificing speed.                                    |
| `liquid/lfm-2.5-1.2b-instruct:free`                  | ★★★★★       | `General`   | `Blazing`  | The smallest model that actually answers usefully. Insane response times.                 |
| `nvidia/nemotron-nano-12b-v2-vl:free`                | ★★★★★       | `Vision`    | `Fast`     | Does text and vision in one call without the bloat.                                       |
| `openai/gpt-oss-120b:free`                           | ★★★★★       | `General`   | `Blazing`  | The same reliable gpt-oss every provider carries. The safest five-star bet on OpenRouter. |
| `openai/gpt-oss-20b:free`                            | ★★★★★       | `Code`      | `Fast`     | Same reliable output as the 120B but lighter. The everyday driver.                        |
| `cohere/north-mini-code:free`                        | ★★★★☆       | `Code`      | `Blazing`  | Efficient coding model from Cohere. Lightweight enough for rapid iteration loops.         |
| `liquid/lfm-2.5-1.2b-thinking:free`                  | ★★★★☆       | `Reasoning` | `Moderate` | Tiny 1.2B that thinks aloud. Good for logic, verbose for quick code edits.                |
| `nvidia/nemotron-3-nano-30b-a3b:free`                | ★★★★☆       | `General`   | `Fast`     | Efficient 30B MoE — clean responses with no preamble for lightweight daily tasks.         |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ★★★★☆       | `Reasoning` | `Moderate` | Shows its work step by step. Useful for verification, noisy for quick answers.            |
| `nvidia/nemotron-3-super-120b-a12b:free`             | ★★★★☆       | `General`   | `Fast`     | Strong 120B mid-range. Steps in when the 30Bs need more headroom.                         |
| `nvidia/nemotron-nano-9b-v2:free`                    | ★★★★☆       | `Fallback`  | `Fast`     | Reliable fallback that punches above its 9B weight.                                       |
| `poolside/laguna-m.1:free`                           | ★★★★☆       | `Code`      | `Fast`     | Built by devs for devs. Inline completions that feel like they read your mind.            |
| `poolside/laguna-xs.2:free`                          | ★★★★☆       | `Code`      | `Blazing`  | Snappier than M.1, slightly less depth. Perfect for fast suggestions.                     |

### [Routeway AI](https://routeway.ai)

Routeway is a unified API gateway offering free models through a `:free` model suffix — a pattern shared with OpenRouter and Kilo Code. Models are drawn from Stepfun, NVIDIA, Poolside, Meta, and others, all accessed through a single OpenAI-compatible endpoint with no credit card required. The tight 5 RPM cap makes Routeway a fallback hub rather than a daily driver. Routeway currently has 7 models verified — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 5 RPM / 200 RPD / 300,000 TPD

🔗 **Base URL:** `https://api.routeway.ai/v1`

| Free Model                     | Star Rating | Best For    | Speed      | Opinion                                                                           |
| :----------------------------- | :---------- | :---------- | :--------- | :-------------------------------------------------------------------------------- |
| `deepseek-v4-flash:free`       | ★★★★★       | `Reasoning` | `Blazing`  | Elite 284B MoE reasoning at blazing speed. The strongest model on Routeway.       |
| `poolside/laguna-m.1:free`     | ★★★★★       | `Code`      | `Fast`     | Same elite Poolside 225B coding model — best pick on Routeway. Fast and focused.  |
| `laguna-xs.2:free`             | ★★★★☆       | `Code`      | `Blazing`  | Poolside's 33B coder. Sub-second response time for inline completions.            |
| `llama-3.3-70b-instruct:free`  | ★★★★☆       | `General`   | `Fast`     | The 70B workhorse. Complex instruction following without drama.                   |
| `nemotron-3-nano-30b-a3b:free` | ★★★★☆       | `General`   | `Fast`     | NVIDIA's efficient 30B MoE — clean responses with no preamble.                    |
| `nemotron-nano-9b-v2:free`     | ★★★★☆       | `Fallback`  | `Fast`     | Reliable NVIDIA nano — punches above its 9B weight for quick edits.               |
| `step-3.5-flash:free`          | ★★★★☆       | `Agentic`   | `Moderate` | Stepfun's 11B active-param agentic powerhouse. Proven quality at 74.4% SWE-bench. |

### [PaxSenix](https://api.paxsenix.org)

PaxSenix is a high-volume inference hub offering an enormous catalog of models from OpenAI, Anthropic, Google, DeepSeek, Meta, Mistral, xAI, and more through an OpenAI-compatible endpoint. The free tier provides 1,000 requests per day with 500,000 daily tokens — among the most generous quotas on this list, ideal for sustained coding sessions. No credit card required. PaxSenix currently has roughly 50 verified coding-relevant models — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 1,000 RPD / 500,000 TPD

🔗 **Base URL:** `https://api.paxsenix.org/v1`

| Free Model          | Star Rating | Best For    | Speed      | Opinion                                                                                             |
| :------------------ | :---------- | :---------- | :--------- | :-------------------------------------------------------------------------------------------------- |
| `claude-sonnet-4-6` | ★★★★★       | `Code`      | `Blazing`  | Latest Claude Sonnet — frontier reasoning at blazing speed. The top pick on PaxSenix for coding.    |
| `deepseek-v4-flash` | ★★★★★       | `Reasoning` | `Blazing`  | Elite flash variant with 79.0% SWE-bench. Blazing speed at 1,000 RPD — unmatched throughput.        |
| `deepseek-v4-pro`   | ★★★★★       | `Reasoning` | `Fast`     | Pro variant of V4 — 80.6% SWE-bench. Extra headroom over Flash for the hardest prompts.             |
| `gemini-3-pro`      | ★★★★★       | `General`   | `Moderate` | Google's pro-tier flagship. Deep reasoning with a massive context window for big projects.          |
| `gpt-5.4`           | ★★★★★       | `General`   | `Fast`     | Flagship GPT with polished output. Elite general coding at 1k daily requests — best quota in class. |
| `gpt-5.5`           | ★★★★★       | `General`   | `Blazing`  | Latest GPT release — frontier reasoning with clean, direct output at sub-second speed.              |
| `gpt-oss-120b`      | ★★★★★       | `General`   | `Blazing`  | The same reliable 120B flagship. Sub-second responses that stretch your daily budget further.       |
| `codestral-latest`  | ★★★★☆       | `Code`      | `Blazing`  | Mistral's coding specialist — fast completions with strong multi-file awareness.                    |
| `deepseek-r1`       | ★★★★☆       | `Reasoning` | `Moderate` | Reasoning specialist with visible chain-of-thought. Excellent for math and logic-heavy debugging.   |
| `deepseek-v3.2`     | ★★★★☆       | `Reasoning` | `Fast`     | 73.1% SWE-bench. Refined V3 release — reliable reasoning for complex coding tasks.                  |
| `gemini-2.5-flash`  | ★★★★☆       | `General`   | `Fast`     | Google's reliable flash model. Steady throughput for background coding tasks at 1k RPD.             |
| `gemma-4-31b`       | ★★★★☆       | `General`   | `Fast`     | Google's 31B dense model. Strong generalist for daily coding without the overhead.                  |
| `gpt-4.1`           | ★★★★☆       | `General`   | `Fast`     | Reliable workhorse — handles daily coding with consistent, structured output.                       |
| `llama-3.3-70b`     | ★★★★☆       | `General`   | `Blazing`  | Meta's 70B workhorse. Fast and reliable for daily coding with strong instruction following.         |
| `step-3.5-flash`    | ★★★★☆       | `Agentic`   | `Blazing`  | Agentic powerhouse — 74.4% SWE-bench. Tiny 11B active params deliver shocking strength.             |

### [Pollinations AI](https://pollinations.ai)

Pollinations AI is a free, no-signup inference provider serving a wide variety of models — from OpenAI and Grok to Qwen, Perplexity, and niche music/safety models. No API key needed, no account required — the only truly zero-friction provider on this list. Pollinations AI currently has 38 models verified — 25 are ★★★☆☆ or above.

🎁 **Free Tier Quota:** 60 RPM / Unlimited RPD For Secret Keys; 8 RPM / 11,500 RPD For Publishable Keys

🔗 **Base URL:** `https://gen.pollinations.ai/v1` (OpenAI-compatible)

| Free Model            | Star Rating | Best For    | Speed      | Opinion                                                                       |
| :-------------------- | :---------- | :---------- | :--------- | :---------------------------------------------------------------------------- |
| `gemma`               | ★★★★★       | `General`   | `Fast`     | Punches above its weight class. Follows complex instructions with precision.  |
| `gpt-5.4-mini`        | ★★★★★       | `General`   | `Blazing`  | Snappy to the point of feeling instant.                                       |
| `grok-4-20-reasoning` | ★★★★★       | `General`   | `Fast`     | Tighter than base Grok. Fewer surprises, more consistency.                    |
| `grok`                | ★★★★★       | `Chat`      | `Fast`     | Surprisingly polished at code. Switches between chat and coding effortlessly. |
| `llama`               | ★★★★★       | `General`   | `Fast`     | The workhorse. No-nonsense output, zero chatter.                              |
| `nova-fast`           | ★★★★★       | `Code`      | `Blazing`  | For rapid-fire coding loops where waiting isn't an option.                    |
| `openai-large`        | ★★★★★       | `Reasoning` | `Fast`     | Extra headroom when the reasoning gets thorny.                                |
| `openai`              | ★★★★★       | `General`   | `Fast`     | Predictable. Drop it into any workflow and get clean answers.                 |
| `perplexity`          | ★★★★★       | `General`   | `Moderate` | Research-backed answers to coding questions.                                  |
| `qwen-coder`          | ★★★★★       | `Code`      | `Fast`     | Focused code output without the fluff.                                        |
| `qwen-vision-pro`     | ★★★★★       | `Vision`    | `Fast`     | Polished vision experience. Sharper answers for text and images.              |
| `qwen-vision`         | ★★★★★       | `Vision`    | `Fast`     | Clean multimodal responses. Screenshots and code mix without the rambling.    |
| `gpt-5.4`             | ★★★★☆       | `General`   | `Fast`     | Reliable daily coding, though outputs sometimes need a second try.            |
| `grok-large`          | ★★★★☆       | `General`   | `Fast`     | Extra Grok headroom for heavier reasoning tasks.                              |
| `kimi-code`           | ★★★★☆       | `Code`      | `Fast`     | Strong on code — use it for programming-specific work.                        |
| `minimax-m2.7`        | ★★★★☆       | `General`   | `Fast`     | Solid and frictionless for everyday tasks.                                    |
| `mistral-large`       | ★★★★☆       | `General`   | `Fast`     | Strong Mistral flagship. Crisp output with strong instruction following.      |
| `mistral`             | ★★★★☆       | `General`   | `Fast`     | Clean Mistral responses without the full API quota drain.                     |
| `nova`                | ★★★★☆       | `Agent`     | `Fast`     | Clean output for agent pipelines. Straightforward coding without noise.       |
| `openai-fast`         | ★★★★☆       | `General`   | `Blazing`  | Built for speed. Quick tasks handled instantly.                               |
| `qwen-large`          | ★★★★☆       | `General`   | `Moderate` | More parameters, more context. Slightly less direct but more headroom.        |
| `step-3.5-flash`      | ★★★★☆       | `General`   | `Fast`     | Keeps pace with daily edits and scripts.                                      |
| `step-flash`          | ★★★★☆       | `Fallback`  | `Fast`     | Dependable fallback — keeps quality up when main model hits limits.           |
| `midijourney-large`   | ★★★☆☆       | `General`   | `Fast`     | Clean empty responses for frictionless automation.                            |
| `perplexity-fast`     | ★★★☆☆       | `General`   | `Blazing`  | Research-backed answers at the speed of light.                                |

### [Poolside](https://poolside.ai)

Poolside is a foundation model lab building purpose-built coding models from scratch. Their Laguna series — M.1 (225B-A23B MoE) and XS.2 (33B-A3B MoE) — are trained on 30T tokens exclusively for agentic software engineering with tool calling and 256K context. Both models are free while in preview — the same "use it while it lasts" uncertainty as any free provider. Poolside currently has 2 models verified.

🎁 **Free Tier Quota:** 20 RPM / 200 RPD / 150,000 TPM / 1,000,000 TPD

🔗 **Base URL:** `https://inference.poolside.ai/v1`

| Free Model             | Star Rating | Best For | Speed     | Opinion                                                                                                      |
| :--------------------- | :---------- | :------- | :-------- | :----------------------------------------------------------------------------------------------------------- |
| `poolside/laguna-m.1`  | ★★★★★       | `Code`   | `Fast`    | Purpose-built 225B MoE for agentic coding. Strong SWE-bench scores with tool calling — elite coding quality. |
| `poolside/laguna-xs.2` | ★★★★☆       | `Code`   | `Blazing` | Open-weight 33B (Apache 2.0). Impressive depth for its size at 0.55s response time.                          |

### [SambaNova AI](https://cloud.sambanova.ai)

SambaNova AI is a **hardware-driven inference provider** utilizing proprietary Reconfigurable Dataflow Units (RDUs) rather than standard GPUs, removing the traditional hardware-decode bottleneck for incredibly high throughput. The free tier is limited to 20 requests and 200k tokens per day — tight for sustained use. Preview models (DeepSeek-V3.2, Gemma-4-31B-it) require a one-time $5 signup credit that does not replenish. SambaNova AI currently has 5 models verified.

🎁 **Free Tier Quota:** 20 RPM / 20 RPD / 200,000 TPD

🔗 **Base URL:** `https://api.sambanova.ai/v1`

| Free Model                    | Star Rating | Best For    | Speed      | Opinion                                                                                                                                         |
| :---------------------------- | :---------- | :---------- | :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| `DeepSeek-V3.1`               | ★★★★★       | `Agent`     | `Blazing`  | Production-grade flagship with elite reasoning at blazing speeds. The 20 RPD cap limits sustained use — better quota on Auriko or Hugging Face. |
| `DeepSeek-V3.2`               | ★★★★☆       | `Reasoning` | `Blazing`  | **Preview** — Blazing fast on RDUs but requires $5 signup credit that does not replenish. Use while it lasts.                                   |
| `Meta-Llama-3.3-70B-Instruct` | ★★★★☆       | `General`   | `Fast`     | The traditional benchmark engine. Interprets dense, multi-variable project constraints with high structural reliability.                        |
| `gemma-4-31B-it`              | ★★★☆☆       | `General`   | `Blazing`  | **Preview** — Google's newest runs fast but dies with the $5 credit. Stops working once the bonus is drained.                                   |
| `gpt-oss-120b`                | ★★★☆☆       | `Fallback`  | `Moderate` | The same 117B MoE flagship that dominates on Groq. Available on SambaNova but with noticeably higher latency (~3.5s).                           |

### [TokenReply](https://tokenreply.com)

TokenReply is a lightweight inference hub offering models from Google, DeepSeek, OpenAI, Qwen, Moonshot, Stepfun, and more through an OpenAI-compatible endpoint. The free tier provides 3 RPM with 40 weekly model calls — a very tight cap suited for lightweight evaluation and occasional queries, not sustained coding. Free models only. No credit card required. TokenReply currently has 7 models verified — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 3 RPM / 40 Weekly Model Calls / Free Models Only

🔗 **Base URL:** `https://api.tokenreply.com/v1`

| Free Model                    | Star Rating | Best For    | Speed      | Opinion                                                                                               |
| :---------------------------- | :---------- | :---------- | :--------- | :---------------------------------------------------------------------------------------------------- |
| `deepseek-ai/deepseek-v4-pro` | ★★★★★       | `Reasoning` | `Fast`     | Pro variant of V4 — 80.6% SWE-bench. Make each of your 40 weekly calls count with top-tier reasoning. |
| `openai/gpt-oss-120b`         | ★★★★★       | `General`   | `Moderate` | The same reliable 120B flagship. Best value for the tight weekly cap — efficient and dependable.      |
| `qwen/qwen3.5-397b-a17b`      | ★★★★★       | `General`   | `Moderate` | 397B MoE flagship — 76.4% SWE-bench. Immense capacity for your most critical prompts.                 |
| `google/gemma-4-31b-it`       | ★★★★☆       | `General`   | `Fast`     | Google's 31B dense model. Strong generalist for daily coding without overhead.                        |
| `moonshotai/kimi-k2.6`        | ★★★★☆       | `Reasoning` | `Blazing`  | 1T multimodal MoE with strong long-horizon reasoning. Solid pick for complex analysis.                |
| `stepfun-ai/step-3.5-flash`   | ★★★★☆       | `Agentic`   | `Blazing`  | Agentic powerhouse — 74.4% SWE-bench. Tiny 11B active params punch far above their weight.            |
| `stepfun-ai/step-3.7-flash`   | ★★★★☆       | `Agentic`   | `Blazing`  | Latest Stepfun flash — refined agentic reasoning with blazing speed.                                  |

### [Void AI](https://voidai.app)

Void AI is a high-RPM inference hub offering models from OpenAI, Google, DeepSeek, Qwen, Moonshot, Zhipu, and more through an OpenAI-compatible endpoint. The free tier provides 100 RPM with 125,000 daily credits — the highest RPM of any hub on this list, ideal for high-throughput coding sessions. No credit card required. Void AI currently has roughly 30 verified coding-relevant models — all at ★★★★☆ or above.

🎁 **Free Tier Quota:** 100 RPM / 125,000 Daily Credits

🔗 **Base URL:** `https://api.voidai.app/v1`

| Free Model                       | Star Rating | Best For    | Speed      | Opinion                                                                                          |
| :------------------------------- | :---------- | :---------- | :--------- | :----------------------------------------------------------------------------------------------- |
| `deepseek-v4-flash`              | ★★★★★       | `Reasoning` | `Blazing`  | Elite flash variant with 79.0% SWE-bench. Blazing speed paired with Void's 100 RPM is unmatched. |
| `gpt-5.3-chat-latest`            | ★★★★★       | `General`   | `Fast`     | Latest GPT chat variant. Strong all-rounder for coding and conversation alike.                   |
| `gpt-5.4`                        | ★★★★★       | `General`   | `Fast`     | Flagship GPT with polished output. Elite general coding at 100 RPM — the best quota in class.    |
| `gpt-5.5`                        | ★★★★★       | `General`   | `Fast`     | Latest GPT release — frontier reasoning at high speed. Top pick on Void AI for daily coding.     |
| `gpt-oss-120b`                   | ★★★★★       | `General`   | `Blazing`  | The same reliable 120B flagship. Sub-second responses at 100 RPM make this a daily driver.       |
| `qwen3-235b-a22b-instruct`       | ★★★★★       | `General`   | `Fast`     | 235B Qwen3 flagship — native 119-language support with deep multi-file reasoning.                |
| `qwen3-coder-480b-a35b-instruct` | ★★★★★       | `Code`      | `Moderate` | Massive 480B coder with 35B active params. Elite architecture-level reasoning for big projects.  |
| `deepseek-v3.2`                  | ★★★★☆       | `Reasoning` | `Fast`     | 73.1% SWE-bench. Refined V3 release — reliable reasoning for complex coding tasks.               |
| `gemini-3.1-flash-lite`          | ★★★★☆       | `General`   | `Fast`     | Google's efficient flash-lite. Steady throughput for background tasks at 100 RPM.                |
| `gpt-4o`                         | ★★★★☆       | `General`   | `Fast`     | Proven workhorse. Handles daily coding with consistent, structured output.                       |
| `gpt-5-codex`                    | ★★★★☆       | `Code`      | `Blazing`  | GPT codex variant — purpose-built for code generation at blazing speed.                          |
| `gpt-5.3-codex`                  | ★★★★☆       | `Code`      | `Fast`     | Latest codex variant. Clean, direct code output with strong multi-file awareness.                |
| `gpt-oss-20b`                    | ★★★★☆       | `Code`      | `Blazing`  | Same reliable DNA as the 120B, lighter and faster. Perfect for rapid iteration loops.            |
| `kimi-k2.6`                      | ★★★★☆       | `Reasoning` | `Fast`     | 1T multimodal MoE. Strong long-horizon reasoning for complex multi-step analysis.                |
| `umbra`                          | ★★★★☆       | `General`   | `Blazing`  | Mystery model with sub-second responses. Surprisingly capable for its speed — a solid wildcard.  |

### [Z.AI (Zhipu AI)](https://z.ai)

Zhipu AI is a Chinese AI company developing the GLM family of foundation models. The free tier offers two flash-variant models with a concurrency limit of 1 request at a time and unlimited daily tokens — practical for lightweight scripting and quick edits, but the single-concurrent cap makes sustained coding sessions impractical. Z.AI currently has 2 models verified.

🎁 **Free Tier Quota:** 1 Concurrent Request / Uncapped TPD

🔗 **Base URL:** `https://api.z.ai/api/paas/v4`

| Free Model      | Star Rating | Best For   | Speed     | Opinion                                                                      |
| :-------------- | :---------- | :--------- | :-------- | :--------------------------------------------------------------------------- |
| `glm-4.7-flash` | ★★★★☆       | `General`  | `Blazing` | Newer and noticeably sharper than 4.5-flash. Strong for a flash variant.     |
| `glm-4.5-flash` | ★★★☆☆       | `Fallback` | `Blazing` | Older flash variant. Handles basic tasks but shows its age on complex logic. |

---

## Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details.
