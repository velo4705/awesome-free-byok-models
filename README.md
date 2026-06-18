# Awesome Free BYOK Models [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

> **Last Verified: June 18, 2026** - All models tested live across 19 providers.

A curated list of the **best high-performance**, **free-tier AI models** you can use to **supercharge your coding setup** without paying for expensive monthly subscriptions or getting locked out by trial credit expiry.

By using a **Bring Your Own Key (BYOK)** approach, you can plug your free API keys directly into coding tools like **VS Code extensions, terminal assistants, or code editors**, or use them in your **coding projects**. It doesn't even require a **credit card** for the best models!

> **Pro tip:** Free tiers rotate often. If a model hits rate limits, switch to another — there's always a backup in this list.
> **Always verify** current quotas on the provider's console before building workflows.

## Contents

- [The Best 3 API Providers](#the-best-3-api-providers)
- [The Top 10 Recommended Free Models](#the-top-10-recommended-free-models)
- [The Deep-Dive: Individual Provider Showcases](#the-deep-dive-individual-provider-showcases)
  - [AION Labs Models](#aion-labs-models)
  - [Auriko Models](#auriko-models)
  - [Cerebras AI Models](#cerebras-ai-models)
  - [Cloudflare Workers AI Models](#cloudflare-workers-ai-models)
  - [Cohere AI Models](#cohere-ai-models)
  - [GitHub Models](#github-models)
  - [Google Gemini Models](#google-gemini-models)
  - [Groq API Models](#groq-api-models)
  - [Hugging Face Inference API Models](#hugging-face-inference-api-models)
  - [Kilo Code Models](#kilo-code-models)
  - [LLM7.IO Models](#llm7io-models)
  - [Mistral AI Models](#mistral-ai-models)
  - [Mixlayer Models](#mixlayer-models)
  - [MorphLLM Models](#morphllm-models)
  - [Ollama Cloud Models](#ollama-cloud-models)
  - [OpenCode Zen Models](#opencode-zen-models)
  - [OpenRouter Models](#openrouter-models)
  - [Pollinations AI Models](#pollinations-ai-models)
  - [SambaNova AI Models](#sambanova-ai-models)

## The Best 3 API Providers

If you are signing up for free accounts to get API keys, these are the **three best platforms** to look at first.

| Provider          | The Simple Vibe     | Why It Matters For You                                                                                                                                              |
| :---------------- | :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ollama Cloud**  | Uncapped & Reliable | Time-based compute allocation with no daily request cap — the only provider where you can code all day without counting requests. Home to the #1 ranked free model. |
| **Google Gemini** | Infinite Battery    | 1,500 free requests per day on flash-lite with a massive context window. Lighter on reasoning but unstoppable for continuous background tasks.                      |
| **LLM7.IO**       | Generous Credits    | 5M TPD and 128 RPM with replenishable credits — no hard daily ceiling. Hosts the #3 ranked model.                                                                   |

---


## The Top 10 Recommended Free Models

The absolute best free models available right now, ranked by how well they handle **daily coding tasks** and **projects that require a working model**. This does **NOT** include vision models — all models here are text-only.

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
| **10** | `codestral-latest`             | **LLM7.IO**         | Exceptional multi-language completion engine with 128 RPM and 5M TPD — far more generous quota than Mistral's shared pool. Best kept for single-file, line-by-line edits.                                                                                                     |

---


## The Deep-Dive: Individual Provider Showcases

These tables break down notable free models from each provider's ecosystem, **capped at ★★★☆☆ or above for providers and ★★★★☆ or above for hubs**. Ratings are based on how well they handle real-world development demands — typing speed, instruction following, and large projects — evaluated against each provider's quota, rate limits, and context windows.


### [AION Labs](https://www.aionlabs.ai) Models

AION Labs provides storytelling-optimized models through an OpenAI-compatible API. The free tier offers 20,000 tokens/day and 15 RPM with no credit card required — a solid option if you need a daily token allowance for lightweight coding and creative tasks. AION Labs currently has 2 models verified.

**Free Tier Quota:** 15 RPM / 500 RPD / 5,000,000 TPD

**Base URL:** `https://api.aionlabs.ai/v1`

| Free Model                       | Star Rating | Best For    | Speed     | Opinion                                                                                      |
| :------------------------------- | :---------- | :---------- | :-------- | :------------------------------------------------------------------------------------------- |
| `aion-labs/aion-2.5`             | ★★★★★       | `Code`      | `Fast`    | Clean, direct output with no preamble. The top pick on AION Labs.                            |
| `aion-labs/aion-rp-llama-3.1-8b` | ★★★★☆       | `Fallback`  | `Blazing` | Fastest AION model. Handles lightweight tasks instantly, but 8B cap limits depth.            |


### [Auriko](https://www.auriko.ai) Models

Auriko is a unified API gateway providing access to 100+ models from top providers (OpenAI, Anthropic, DeepSeek, Google, xAI, Moonshot, and more) through a single OpenAI-compatible endpoint. The free tier offers 1,000 Platform RPM and 500 BYOK RPM with a 1M token monthly cap and zero inference markup — no credit card required. Access to every model on the platform at provider cost. Auriko currently has 166 models verified — 29 are ★★★★☆ or above.

**Free Tier Quota:** 500 RPM (BYOK) / 1,000 RPM (Platform) / 1,000,000 tokens/month (BYOK)

**Base URL:** `https://api.auriko.ai/v1`

| Free Model                                     | Star Rating | Best For    | Speed      | Opinion                                                                                                     |
| :--------------------------------------------- | :---------- | :---------- | :--------- | :---------------------------------------------------------------------------------------------------------- |
| `o3-2025-04-16`                                | ★★★★★       | `Reasoning` | `Moderate` | Top-tier reasoning — handles multi-file architecture without preamble. The strongest coding pick on Auriko. |
| `claude-opus-4-8`                              | ★★★★★       | `Code`      | `Blazing`  | Latest Claude Opus. Deep reasoning and code generation with zero preamble.                                  |
| `claude-opus-4-7`                              | ★★★★★       | `Code`      | `Blazing`  | Fastest Claude Opus variant. Deep reasoning and code generation with zero preamble.                         |
| `claude-opus-4-6`                              | ★★★★★       | `Code`      | `Blazing`  | Slightly older Opus but still elite — handles complex architecture with zero preamble.                      |
| `deepseek-v3.2`                                | ★★★★★       | `Reasoning` | `Fast`     | Elite reasoning workhorse trusted across every provider. Clean output for multi-file analysis.              |
| `deepseek-v3.1`                                | ★★★★★       | `Reasoning` | `Fast`     | The best provider for V3.1 — 5,000 RPD and 5M TPD with zero quota stress. Elite reasoning at blazing speed. |
| `qwen-3-coder-480b-a35b-instruct`              | ★★★★★       | `Code`      | `Moderate` | Purpose-built 480B code model — tackles the hardest debugging sessions.                                     |
| `qwen-3-coder-30b-a3b-instruct`                | ★★★★★       | `Code`      | `Fast`     | Focused 30B coder from Qwen — efficient and responsive for everyday coding.                                 |
| `qwen-3-235b-a22b-instruct-2507-fp8`           | ★★★★★       | `General`   | `Fast`     | 235B at FP8 precision. Elite reasoning without the full-weight latency.                                     |
| `qwen-2.5-72b-instruct`                        | ★★★★★       | `General`   | `Fast`     | Proven workhorse trusted across every setup. Reliable and consistent.                                       |
| `gpt-5-2025-08-07`                             | ★★★★★       | `General`   | `Fast`     | GPT-5 flagship — handles every coding task with zero preamble. Elite intelligence without friction.         |
| `hermes-3-llama-3.1-405b`                      | ★★★★★       | `Reasoning` | `Moderate` | 405B of raw Llama capability. Feels unfair for a free tier.                                                 |
| `claude-sonnet-4-20250514`                     | ★★★★☆       | `General`   | `Fast`     | Latest Sonnet — balances speed and depth well. Clean, direct responses.                                     |
| `deepseek-v4-flash`                            | ★★★★☆       | `Reasoning` | `Fast`     | Latest DeepSeek flash variant — strong reasoning depth with clean inference.                                |
| `o4-mini-2025-04-16`                           | ★★★★☆       | `Reasoning` | `Fast`     | Latest reasoning model from OpenAI — compact but capable. Handles logic-heavy tasks cleanly.                |
| `gpt-4.1-2025-04-14`                           | ★★★★☆       | `Code`      | `Blazing`  | Blazing fast with strong general coding capability. A solid daily driver.                                   |
| `gpt-5.2-2025-12-11`                           | ★★★★☆       | `General`   | `Fast`     | Latest GPT-5 point release. Fast and reliable across every coding task.                                     |
| `gpt-5-chat-latest`                            | ★★★★☆       | `Chat`      | `Fast`     | Chat-optimized GPT-5 variant. Handles conversational coding naturally and cleanly.                          |
| `gpt-5.4-2026-03-05`                           | ★★★★☆       | `General`   | `Fast`     | Latest GPT generation. Strong general intelligence with clean output.                                       |
| `claude-sonnet-4-6`                            | ★★★★☆       | `Code`      | `Fast`     | Latest Sonnet 4.6 — handles creative coding with Anthropic's clear response style.                          |
| `gpt-5.4-mini-2026-03-17`                      | ★★★★☆       | `General`   | `Fast`     | Compact GPT-5.4 — handles lightweight tasks efficiently.                                                    |
| `gpt-5.4-nano-2026-03-17`                      | ★★★★☆       | `General`   | `Blazing`  | The nano tier — syntax checks and quick edits return almost instantly.                                      |
| `groq-4.20-0309-non-reasoning`                 | ★★★★☆       | `Agent`     | `Blazing`  | xAI's fastest — clean output for rapid-fire coding loops where speed is everything.                         |
| `phi-4`                                        | ★★★★☆       | `Code`      | `Blazing`  | Microsoft's compact powerhouse. Surprising coding depth for its size.                                       |
| `gemma-4-31b-it-turbo`                         | ★★★★☆       | `General`   | `Fast`     | Turbocharged Gemma 4. Fast responses with clean, structured output.                                         |
| `seed-2.0-code`                                | ★★★★☆       | `Code`      | `Fast`     | Coding-specialized from Seed. Handles multi-file refactors without rambling.                                |
| `gpt-4o-mini-2024-07-18`                       | ★★★★☆       | `Code`      | `Fast`     | OpenAI's compact classic. Reliable daily coding with broad language support.                                |
| `claude-haiku-4-5-20251001`                    | ★★★★☆       | `General`   | `Blazing`  | Fast and focused. Handles daily coding without fanfare.                                                     |
| `llama-3.3-70b-instruct-fp8`                   | ★★★★☆       | `General`   | `Fast`     | Strong instruction following with edge-friendly speed. Clean and dependable.                                |


### [Cerebras AI](https://cloud.cerebras.ai) Models

Cerebras AI is defined by its **Wafer-Scale Engine (WSE) technology**, integrating memory, compute, and interconnects onto a single silicon wafer — solving the "memory wall" that throttles inference speed. The free tier offers replenishable credits with industry-leading throughput (2,500+ tokens/second). Cerebras AI currently has 2 models verified.

**Free Tier Quota:** 5 RPM / 250 RPD / 30,000 TPM

**Base URL:** `https://api.cerebras.ai/v1`

| Free Model     | Star Rating | Best For  | Speed     | Opinion                                                                                                        |
| :------------- | :---------- | :-------- | :-------- | :------------------------------------------------------------------------------------------------------------- |
| `gpt-oss-120b` | ★★★★☆       | `General` | `Blazing` | The same 117B MoE flagship that dominates on Groq. Sub-second responses on Cerebras' wafer-scale architecture. |
| `zai-glm-4.7`  | ★★★★☆       | `Agent`   | `Blazing` | 131K context window optimized for rapid agentic coding. Efficient at blazing speeds.                           |


### [Cloudflare Workers AI](https://dash.cloudflare.com) Models

Cloudflare Workers AI runs models on Cloudflare's global edge network using serverless GPUs. The free tier offers 10,000 requests/day shared across all models with near-zero latency from edge locations worldwide. Cloudflare Workers AI currently has 25 models verified — the top 20 are listed below.

**Free Tier Quota:** 150 to 1,500 RPM / 100,000 RPD / 13,000 TPD

**Base URL:** `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions` (replace `{account_id}` with your Cloudflare account ID)

> ⚠️ **Two API paths:** The `/chat/completions` endpoint takes standard `"messages"` (OpenAI-compatible). The legacy `/run/{model}` endpoint uses `"prompt"` instead — make sure your tool targets the right one.

| Free Model                                     | Star Rating | Best For    | Speed      | Opinion                                                                                                         |
| :--------------------------------------------- | :---------- | :---------- | :--------- | :-------------------------------------------------------------------------------------------------------------- |
| `@cf/qwen/qwen2.5-coder-32b-instruct`          | ★★★★★       | `Code`      | `Fast`     | The only dedicated code model on Cloudflare's edge network — responds instantly with clean, no-preamble output. |
| `@cf/meta/llama-3.3-70b-instruct-fp8-fast`     | ★★★★☆       | `Reasoning` | `Fast`     | Strong instruction-following at edge speed with good depth.                                                     |
| `@cf/openai/gpt-oss-120b`                      | ★★★★☆       | `Code`      | `Fast`     | The 120B headroom shows on hard problems — smaller models tap out, this keeps digging.                          |
| `@cf/qwen/qwen3-30b-a3b-fp8`                   | ★★★★☆       | `General`   | `Fast`     | Feels like a full-size model despite the tiny active footprint.                                                 |
| `@cf/google/gemma-4-26b-a4b-it`                | ★★★★☆       | `General`   | `Fast`     | Clean, thoughtful responses that don't waste your time.                                                         |
| `@cf/zai-org/glm-4.7-flash`                    | ★★★★☆       | `Agent`     | `Fast`     | Snappy under heavy use — coding calls return before you notice the lag.                                         |
| `@cf/meta/llama-4-scout-17b-16e-instruct`      | ★★★★☆       | `General`   | `Fast`     | Direct answers without the overhead of a full-parameter model.                                                  |
| `@cf/moonshotai/kimi-k2.7-code`                | ★★★★☆       | `Reasoning` | `Moderate` | The one that actually reads your whole codebase for project-wide refactors.                                     |
| `@cf/nvidia/nemotron-3-120b-a12b`              | ★★★★☆       | `Reasoning` | `Moderate` | Keeps reasoning until it hits something useful — depth over speed.                                              |
| `@cf/aisingapore/gemma-sea-lion-v4-27b-it`     | ★★★★☆       | `General`   | `Fast`     | Punchy multilingual model with surprising competence for its size.                                              |
| `@cf/meta/llama-3.2-3b-instruct`               | ★★★★☆       | `Fallback`  | `Blazing`  | Syntax checks finish before you finish typing — the instant-sanity-check model.                                 |
| `@cf/openai/gpt-oss-20b`                       | ★★★★☆       | `General`   | `Fast`     | The guilt-free daily driver that handles most tasks without complaint.                                          |
| `@cf/meta/llama-3.2-1b-instruct`               | ★★★★☆       | `Fallback`  | `Blazing`  | The tiniest model that still passes verification — use it when every resource counts.                           |
| `@cf/mistralai/mistral-small-3.1-24b-instruct` | ★★★☆☆       | `General`   | `Slow`     | Feels sluggish for tight coding loops — fine for conversation, frustrating for quick edits.                     |
| `@cf/meta/llama-3.1-8b-instruct-fp8`           | ★★★☆☆       | `General`   | `Moderate` | Gets the job done but wraps answers in unnecessary preamble.                                                    |
| `@cf/qwen/qwq-32b`                             | ★★★☆☆       | `Reasoning` | `Moderate` | Good at logic puzzles, but chain-of-thought preamble makes you wait.                                            |
| `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | ★★★☆☆       | `Reasoning` | `Slow`     | Useful for debugging with visible reasoning, annoying when speed matters.                                       |
| `@cf/meta/llama-3.2-11b-vision-instruct`       | ★★★☆☆       | `Vision`    | `Moderate` | Multimodal but verbose — overkill for text-only coding.                                                         |
| `@cf/ibm-granite/granite-4.0-h-micro`          | ★★★☆☆       | `General`   | `Slow`     | You'll trim its output constantly — only worth it if you need IBM Granite.                                      |
| `@cf/google/gemma-7b-it-lora`                  | ★★★☆☆       | `General`   | `Moderate` | Feels dated next to Gemma v4 — more verbose, less polished.                                                     |


### [Cohere AI](https://dashboard.cohere.com) Models

Cohere focuses on enterprise-grade NLP with their Command model family — built for RAG, tool use, and coding workflows. The free API tier offers replenishable credits with daily resets, and nearly every model delivers sub-second responses. Cohere AI currently has 10 models verified.

**Free Tier Quota:** 20 RPM / 1,000 API calls per month

**Base URL:** `https://api.cohere.com/v2`

| Free Model                    | Star Rating | Best For    | Speed      | Opinion                                                                                                      |
| :---------------------------- | :---------- | :---------- | :--------- | :----------------------------------------------------------------------------------------------------------- |
| `command-a-03-2025`           | ★★★★★       | `Agent`     | `Blazing`  | Cohere's flagship. Blazing fast with clean, direct command execution — ideal for agentic tool-use pipelines. |
| `command-r-plus-08-2024`      | ★★★★☆       | `Reasoning` | `Moderate` | High-capability reasoning engine. Reliable for complex multi-step logic and architectural analysis.          |
| `command-r-08-2024`           | ★★★★☆       | `General`   | `Fast`     | Fast general-purpose workhorse. Handles scripting, terminal commands, and single-file edits.                 |
| `c4ai-aya-vision-32b`         | ★★★★☆       | `Vision`    | `Moderate` | 32B vision-language model. Handles both code and visual context for UI-to-code workflows.                    |
| `command-a-vision-07-2025`    | ★★★★☆       | `Vision`    | `Fast`     | Vision variant of Command A. Process screenshots and diagrams alongside code.                                |
| `command-r7b-12-2024`         | ★★★★☆       | `Code`      | `Fast`     | Compact 7B for rapid-fire completions with minimal overhead.                                                 |
| `command-r7b-arabic-02-2025`  | ★★★★☆       | `General`   | `Fast`     | Arabic-optimized 7B variant. Clean responses for Arabic technical documentation.                             |
| `command-a-translate-08-2025` | ★★★☆☆       | `Fallback`  | `Fast`     | Translation-optimized model. Works for code but limited general coding utility.                              |
| `command-a-reasoning-08-2025` | ★★★☆☆       | `Reasoning` | `Moderate` | Reasoning-focused variant. Minimal outputs suit internal chain-of-thought.                                   |
| `c4ai-aya-expanse-32b`        | ★★★☆☆       | `General`   | `Moderate` | 32B multilingual model that over-answers — adds noise in prompt chains.                                      |


### [GitHub Models](https://github.com/marketplace/models)

GitHub Models provides free API access to models from OpenAI, Meta, Mistral, and others using your existing GitHub account — no new signup needed. Free tier quotas are modest (request-based limits), making it best for prototyping and personal projects. GitHub Models currently has 3 models verified.

**Free Tier Quota:** 10 to 15 RPM / 50 to 150 RPD

**Base URL:** `https://models.inference.ai.azure.com`

| Free Model                     | Star Rating | Best For    | Speed      | Opinion                                                                                                                           |
| :----------------------------- | :---------- | :---------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| `Meta-Llama-3.1-405B-Instruct` | ★★★★★       | `Reasoning` | `Moderate` | The best model on GitHub Models. 405B of deep reasoning at zero cost — add system prompt "no markdown" for clean agentic output.  |
| `gpt-4o`                       | ★★★★☆       | `General`   | `Moderate` | Full OpenAI flagship. Adds markdown by default, but a simple system prompt fixes it — strong all-around for chat and coding.      |
| `gpt-4o-mini`                  | ★★★★☆       | `General`   | `Fast`     | Compact, fast, and clean. Reliable fallback when your bigger model quota runs low for the day.                                    |


### [Google Gemini](https://aistudio.google.com) Models

Gemini offers large context windows on paper, but the free tier's **rate limits vary by model** — Flash-lite variants enjoy ~500 RPD, while standard models can be as low as 20 RPD. Use Gemini for quick, targeted tasks and single-file edits — not marathon sessions. Google Gemini currently has 8 models verified.

**Free Tier Quota:** 15–30 RPM / 1,500 RPD / 1M TPM / Uncapped TPD

**Base URL:** `https://generativelanguage.googleapis.com/v1beta`

| Free Model                                               | Star Rating | Best For    | Speed      | Opinion                                                                                               |
| :------------------------------------------------------- | :---------- | :---------- | :--------- | :---------------------------------------------------------------------------------------------------- |
| `models/gemini-3.1-flash-lite`                           | ★★★★★       | `General`   | `Blazing`  | Lightning-fast, no-fuss outputs. Handles daily coding comfortably with ~500 RPD.                      |
| `models/gemma-4-31b-it`                                  | ★★★★☆       | `General`   | `Fast`     | Highly responsive and incredibly smart. Occasionally overthinks simple instructions.                  |
| `models/gemma-4-26b-a4b-it`                              | ★★★★☆       | `General`   | `Moderate` | Compact Gemma with solid reasoning depth. Clean, structured outputs.                                  |
| `models/gemini-3.5-flash` / `models/gemini-flash-latest` | ★★★☆☆       | `Code`      | `Fast`     | Improved reasoning over prior flash variants. ~20 RPD prevents sustained agentic use.                 |
| `models/gemini-3.1-flash-lite-preview`                   | ★★★☆☆       | `Fallback`  | `Blazing`  | Preview of the BEST model. Nearly identical speed and quality, but experimental.                      |
| `models/gemini-3-flash-preview`                          | ★★★☆☆       | `Reasoning` | `Fast`     | Outstanding intelligence. Deep reasoning with large contexts, but tight ~20 RPD limits.               |
| `models/gemini-2.5-flash`                                | ★★★☆☆       | `Fallback`  | `Fast`     | Solid backup for standard context sizes. Newer Gemini 3 leaves it behind on complex logic.            |
| `models/gemini-flash-lite-latest`                        | ★★★☆☆       | `General`   | `Blazing`  | **LIGHT SCRIPTING ONLY.** Incredibly fast bare-bones lite variant. Lacks depth for multi-file work.   |



### [Groq API](https://console.groq.com) Models

Groq is famous for providing the **absolute lowest streaming latency** in the API market, outrunning traditional cloud providers by a massive margin. The free tier offers 30 RPM with replenishable daily credits — no credit card needed. If you want a setup where your terminal files patch instantly without the typical spinning wheel delay, this is your go-to. Groq API currently has 8 models verified.

**Free Tier Quota:** 30 RPM / 14,400 RPD / 18,000 TPM

**Base URL:** `https://api.groq.com/openai/v1`

| Free Model                                  | Star Rating | Best For   | Speed      | Opinion                                                                                                                               |
| :------------------------------------------ | :---------- | :--------- | :--------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| `openai/gpt-oss-120b`                       | ★★★★★       | `Code`     | `Blazing`  | The undisputed champion. Rarely gets confused by tricky code logic, never hits rate-limit walls.                                      |
| `qwen/qwen3-32b`                            | ★★★★☆       | `Code`     | `Moderate` | Phenomenal for complex code blocks. Briefly thinks out loud before responding.                                                        |
| `llama-3.3-70b-versatile`                   | ★★★★☆       | `Chat`     | `Fast`     | Dependable for developer conversations and brainstorming.                                                                             |
| `openai/gpt-oss-20b`                        | ★★★★☆       | `Code`     | `Blazing`  | Same coding DNA as the 120b. Lightning-fast for standard tasks.                                                                       |
| `qwen/qwen3.6-27b`                          | ★★★★☆       | `Code`     | `Blazing`  | Fast 27B Qwen 3.6. Brief `<think>` preamble but clean output and blazing speed.                                                       |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ★★★☆☆       | `Chat`     | `Fast`     | Handles medium tasks. Overthinks simple prompts.                                                                                      |
| `groq/compound`                             | ★★★☆☆       | `General`  | `Fast`     | Great for single-turn terminal questions. Lacks depth for multi-file projects.                                                        |
| `llama-3.1-8b-instant`                      | ★★★☆☆       | `Code`     | `Blazing`  | Fun for tiny, rapid-fire edits — tends to cut off on long scripts.                                                                    |



### [Hugging Face Inference API](https://huggingface.co/inference-api) Models

Hugging Face's free Inference API gives you access to thousands of community-hosted models with OpenAI-compatible endpoints. The free tier offers $0.10/month in credits — enough for light experimentation, not sustained coding. The real strength is model diversity: 19 ★★★★★ models ranging from 3B to 1T parameters. Hugging Face currently has approximately 80 models verified — 27 are ★★★★☆ or above.

**Free Tier Quota:** $0.10/month credits (~650K tokens)

**Base URL:** `https://router.huggingface.co/v1`

| Free Model                                           | Star Rating | Best For    | Speed      | Opinion                                                                                            |
| :--------------------------------------------------- | :---------- | :---------- | :--------- | :------------------------------------------------------------------------------------------------- |
| `Qwen/Qwen3-Coder-Next`                              | ★★★★★       | `Code`      | `Blazing`  | Generation, completion, debugging — no preamble noise. The strongest coding model on Hugging Face. |
| `Qwen/Qwen3-Coder-480B-A35B-Instruct`                | ★★★★★       | `Code`      | `Moderate` | Tackles the hardest debugging and architecture problems. The largest purpose-built code model.     |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct`                  | ★★★★★       | `Code`      | `Fast`     | Deep, structured reasoning at 30B quality on a 3B budget.                                          |
| `google/gemma-4-31B-it`                              | ★★★★★       | `General`   | `Fast`     | Gemma 4 at full 31B. Cleaner and smarter than the 26B. Follows instructions on the first try.      |
| `Qwen/Qwen2.5-Coder-32B-Instruct`                    | ★★★★★       | `Code`      | `Fast`     | Purpose-built 32B coder with focused output. Drops code without preamble.                          |
| `EssentialAI/rnj-1-instruct`                         | ★★★★★       | `General`   | `Blazing`  | Responds before you finish typing. Uncanny speed for an 8B-class model.                            |
| `meta-llama/Llama-3.3-70B-Instruct`                  | ★★★★★       | `General`   | `Fast`     | Follows complex instructions precisely on the first try.                                           |
| `meta-llama/Llama-3.1-70B-Instruct`                  | ★★★★★       | `General`   | `Fast`     | The workhorse that keeps delivering under heavy use.                                               |
| `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`     | ★★★★★       | `Reasoning` | `Moderate` | Clean, precise output on every turn — feels too big to be free.                                    |
| `deepseek-ai/DeepSeek-V3.2`                          | ★★★★★       | `Reasoning` | `Fast`     | Multi-file architecture work where it never loses the thread.                                      |
| `deepseek-ai/DeepSeek-V3.1`                          | ★★★★★       | `Reasoning` | `Fast`     | Solid alternative to Auriko for V3.1 — 1,000 RPD with the same elite quality.                      |
| `deepcogito/cogito-671b-v2.1`                        | ★★★★★       | `Reasoning` | `Slow`     | An unfair advantage. The sheer reasoning depth is shocking.                                        |
| `google/gemma-4-26B-A4B-it`                          | ★★★★★       | `General`   | `Fast`     | Responds faster than its size suggests with clean, direct output.                                  |
| `Qwen/Qwen2.5-72B-Instruct`                          | ★★★★★       | `Fallback`  | `Fast`     | A reliable fallback that handles most coding tasks competently.                                    |
| `Qwen/Qwen3-235B-A22B-Instruct-2507`                 | ★★★★★       | `Code`      | `Fast`     | 235B capacity with snappy response times — immense power without the wait.                         |
| `CohereLabs/c4ai-command-a-03-2025`                  | ★★★★★       | `Agent`     | `Fast`     | Reliable tool-calling workflows that follow structured instructions.                               |
| `inclusionAI/Ling-2.6-1T`                            | ★★★★★       | `Reasoning` | `Slow`     | A trillion-parameter model for free — immense knowledge and reasoning.                             |
| `swiss-ai/Apertus-70B-Instruct-2509`                 | ★★★★★       | `General`   | `Moderate` | Llama-class reasoning quality without the attitude. Solid and dependable.                          |
| `deepseek-ai/DeepSeek-R1`                            | ★★★★★       | `Reasoning` | `Moderate` | Walks through reasoning step by step without cluttering the output.                                |
| `openai/gpt-oss-120b`                                | ★★★★☆       | `General`   | `Fast`     | Proven across every provider — reliable as ever with clean output.                                 |
| `MiniMaxAI/MiniMax-M3`                               | ★★★★☆       | `General`   | `Blazing`  | The fastest responder on Hugging Face alongside GPT-OSS. Clean and efficient.                      |
| `zai-org/GLM-4.7`                                    | ★★★★☆       | `General`   | `Fast`     | Optimized for throughput — hammer it all day and it keeps responding.                              |
| `Qwen/Qwen3.6-35B-A3B`                               | ★★★★☆       | `Code`      | `Fast`     | The most efficient model on the list. Modern Qwen quality for rapid iteration.                     |
| `moonshotai/Kimi-K2.5`                               | ★★★★☆       | `Reasoning` | `Moderate` | Deep reasoning with chain-of-thought. Strong for logic-heavy debugging.                            |
| `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`  | ★★★★☆       | `General`   | `Fast`     | Llama 4's strongest instruct variant. Clean and dependable for daily coding.                       |
| `pearl-ai/Gemma-4-31B-it-pearl`                      | ★★★★☆       | `General`   | `Fast`     | Fine-tuned Gemma 4 variant. Slightly different flavor with the same clean base quality.            |
| `Qwen/Qwen2.5-Coder-7B-Instruct`                     | ★★★★☆       | `Code`      | `Blazing`  | Compact 7B coder for rapid-fire completions. Small enough to hammer all day.                       |


### [Kilo Code](https://app.kilo.ai) Models

Kilo Code is a coding-agent platform that proxies free models from OpenRouter, NVIDIA, Poolside, and others through a single API key. The free tier offers generous replenishable credits with no hard daily cap — a solid Swiss-army-knife provider that gives you access to a diverse model pool (nano to 550B) through one endpoint. Kilo Code currently has 8 models verified.

**Free Tier Quota:** 5 RPM / 200 RPD

**Base URL:** `https://api.kilo.ai/api/gateway`

| Free Model                                            | Star Rating  | Best For     | Speed       | Opinion                                                                           |
| :---------------------------------------------------- | :----------- | :----------- | :---------- | :-------------------------------------------------------------------------------- |
| `openrouter/owl-alpha`                                | ★★★★★        | `Agent`      | `Fast`      | Zero preamble, straight answers. The safest pick on Kilo Code.                    |
| `nex-agi/nex-n2-pro:free`                             | ★★★★★        | `Agent`      | `Fast`      | Responds immediately without wasting tokens on filler.                            |
| `kilo-auto/small`                                     | ★★★★★        | `General`    | `Fast`      | Kilo's own routing picks the right model — the no-brainer choice.                 |
| `poolside/laguna-xs.2:free`                           | ★★★★☆        | `Code`       | `Blazing`   | Built for inline edits — stays out of your way and finishes before you blink.     |
| `poolside/laguna-m.1:free`                            | ★★★★☆        | `Code`       | `Blazing`   | More headroom than XS for trickier edits. Still fast and focused.                 |
| `stepfun/step-3.7-flash:free`                         | ★★★★☆        | `General`    | `Fast`      | Dependable and drama-free. Perfect for everyday edits.                            |
| `kilo-auto/free`                                      | ★★★★☆        | `Fallback`   | `Moderate`  | Kilo's fallback router — always lands on something functional.                    |
| `openrouter/free`                                     | ★★★★☆        | `Fallback`   | `Moderate`  | Routes through OpenRouter's free pool — a good backup when others are tapped.     |



### [LLM7.IO](https://llm7.io) Models

LLM7.IO is a rising inference provider serving open-weight models via Llama.cpp server with OpenAI-compatible endpoints. The free tier offers replenishable credits with no daily hard cap — a solid option if you want to test heavyweight models (up to 235B) on a simple API without commitment. LLM7.IO currently has 4 models verified.

**Free Tier Quota:** 128 RPM / ~7,200 RPD / 5M TPD (Free Token Users Only)

**Base URL:** `https://api.llm7.io/v1`

| Free Model             | Star Rating | Best For  | Speed      | Opinion                                                                                        |
| :--------------------- | :---------- | :-------- | :--------- | :--------------------------------------------------------------------------------------------- |
| `qwen3-235b`           | ★★★★★       | `Code`    | `Fast`     | Handles multi-file architecture cleanly with zero preamble. Remarkably fluid for a 235B model. |
| `codestral-latest`     | ★★★★☆       | `Code`    | `Fast`     | Strongest coding option here after Qwen. Adds a brief preamble but completions are solid.      |
| `mistral-small-3.2`    | ★★★☆☆       | `General` | `Moderate` | Adequate for chat and scripting, but the verbose preamble kills the flow.                      |
| `devstral-small-2:24b` | ★★★☆☆       | `Agent`   | `Moderate` | Same preamble problem as the Mistral family. Capable under the chatter.                        |


### [Mistral AI](https://console.mistral.ai) Models

Mistral AI is highly regarded for building models that punch far above their **parameter weight class**, with exceptionally clean instruction following and compact execution. The free tier offers replenishable credits with generous RPM limits. Mistral AI currently has 42 models verified (with aliases) — 24 are ★★★☆☆ or above.

**Free Tier Quota:** ~2–30 RPM / 50,000 TPM shared pool

**Base URL:** `https://api.mistral.ai/v1`

| Free Model                                           | Star Rating | Best For    | Speed      | Opinion                                                                                                            |
| :--------------------------------------------------- | :---------- | :---------- | :--------- | :------------------------------------------------------------------------------------------------                  |
| `mistral-code-agent-latest`                          | ★★★★★       | `Agent`     | `Fast`     | **BEST FOR AGENTS.** Purpose-built for autonomous agents with native tool use.                                     |
| `codestral-latest` / `codestral-2508`                | ★★★★☆       | `Code`      | `Fast`     | **CODE COMPLETION ONLY.** Built for programmers. Flies through auto-completions and inline edits.                  |
| `mistral-large-latest` / `mistral-large-2512`        | ★★★★☆       | `Reasoning` | `Fast`     | Strong multi-lingual reasoning but lacks code-specific architecture. The 50k TPM shared pool limits sustained use. |
| `mistral-code-latest`                                | ★★★★☆       | `Code`      | `Fast`     | **CODE COMPLETION ONLY.** Fast, precise completions across dozens of languages.                                    |
| `mistral-code-fim-latest`                            | ★★★★☆       | `Code`      | `Fast`     | **CODE COMPLETION ONLY.** Fill-in-Middle specialist for smart inline insertion.                                    |
| `mistral-medium-3.5` / `mistral-medium-3-5`          | ★★★★☆       | `General`   | `Fast`     | Exceptional price-to-performance. Highly responsive for structural software layouts.                               |
| `mistral-medium-3`                                   | ★★★★☆       | `General`   | `Fast`     | Trusted, stable Medium line. Clean boilerplate code without empty chatter.                                         |
| `mistral-medium-2604`                                | ★★★★☆       | `General`   | `Fast`     | Responsive Medium iteration with predictable execution and strong structural debugging.                            |
| `devstral-medium-latest`                             | ★★★★☆       | `Agent`     | `Moderate` | **AGENT ROUTING ONLY.** Streamlined Medium optimized for automated developer task loops.                           |
| `mistral-medium-latest` / `mistral-medium`           | ★★★★☆       | `General`   | `Fast`     | The classic production model. Dependable for everyday scripting.                                                   |
| `mistral-small-latest` / `mistral-small-2603`        | ★★★★☆       | `General`   | `Blazing`  | Incredible lightweight architecture. Punchy, direct tone with surprising depth.                                    |
| `magistral-small-latest` / `magistral-small-2509`    | ★★★★☆       | `General`   | `Fast`     | New Mistral line. Clean responses with solid depth. A pleasant surprise.                                           |
| `magistral-medium-latest` / `magistral-medium-2509`  | ★★★★☆       | `Reasoning` | `Fast`     | Medium-tier Magistral. Strong reasoning with clean, structured output.                                             |
| `devstral-latest` / `devstral-2512`                  | ★★★☆☆       | `Agent`     | `Moderate` | **AGENT ROUTING ONLY.** Tailored for programmatic tool use.                                                        |
| `ministral-14b-latest` / `ministral-14b-2512`        | ★★★☆☆       | `General`   | `Fast`     | Nimble, edge-focused model. Remarkably capable for its tight memory footprint.                                     |
| `ministral-8b-latest` / `ministral-8b-2512`          | ★★★☆☆       | `General`   | `Fast`     | 8B ministral. Nimble and responsive for lightweight coding tasks.                                                  |
| `mistral-medium-2505`                                | ★★★☆☆       | `Fallback`  | `Slow`     | Early Medium build. Tends to use full-sentence prefix framing.                                                     |
| `mistral-medium-2508`                                | ★★★☆☆       | `Fallback`  | `Moderate` | Older Medium point-release. Clean output but lacks the 3.x optimization pass.                                      |
| `mistral-small-2506`                                 | ★★★☆☆       | `Fallback`  | `Moderate` | Earlier Small snapshot. Trails 2603 on speed.                                                                      |
| `mistral-tiny-latest` / `mistral-tiny-2407`          | ★★★☆☆       | `Fallback`  | `Blazing`  | Fastest Mistral model. Perfect for syntax checks and terminal one-liners.                                          |
| `mistral-vibe-cli-fast`                              | ★★★☆☆       | `Agent`     | `Blazing`  | **TERMINAL HELPER.** Blistering single-turn replies for terminal flags.                                            |
| `mistral-vibe-cli-latest`                            | ★★★☆☆       | `Agent`     | `Moderate` | **TERMINAL HELPER.** Favors explicit sentence explanations when breaking down commands.                            |
| `mistral-vibe-cli-with-tools`                        | ★★★☆☆       | `Agent`     | `Fast`     | **TERMINAL HELPER.** Returns raw executable bash tokens with zero conversational prefix.                           |
| `open-mistral-nemo` / `open-mistral-nemo-2407`       | ★★★☆☆       | `Fallback`  | `Fast`     | Fast and flexible for low-complexity text filtering.                                                               |


### [Mixlayer](https://www.mixlayer.com) Models

Mixlayer is an inference platform for open-source AI models with an OpenAI-compatible API. The free tier offers `qwen/qwen3.5-4b-free` for prototyping with rate limits — no credit card required for the free model. A focused Qwen 3.5/3.6 catalog with tool calling and reasoning support. Mixlayer currently has 1 model verified.

**Free Tier Quota:** 20 RPM / Can be rate-limited (daily usage)

**Base URL:** `https://models.mixlayer.ai/v1`

| Free Model             | Star Rating | Best For  | Speed     | Opinion                                                                                                                              |
| :--------------------- | :---------- | :-------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `qwen/qwen3.5-4b-free` | ★★★★★       | `General` | `Blazing` | The only free model on Mixlayer — handles prototyping and lightweight tasks at blazing speed. Clean, direct output with no preamble. |


### [MorphLLM](https://morphllm.com) Models

MorphLLM hosts a diverse catalog of open-weight models (Qwen, DeepSeek, MiniMax, Morph) optimized for competitive inference speeds. The free tier offers replenishable credits — useful when you need massive model scale (up to 397B) without requiring a credit card. MorphLLM currently has 9 models verified.

**Free Tier Quota:** 5 RPM / 50,000 Input TPM / 20,000 Output TPM

**Base URL:** `https://api.morphllm.com/v1`

| Free Model             | Star Rating | Best For    | Speed      | Opinion                                                                                                 |
| :--------------------- | :---------- | :---------- | :--------- | :------------------------------------------------------------------------------------------------------ |
| `morph-v3-large`       | ★★★★★       | `Agent`     | `Blazing`  | The fastest clean responder. Delivers direct output with zero preamble — ideal for tight agentic loops. |
| `morph-qwen36-27b`     | ★★★★☆       | `General`   | `Fast`     | Fast 27B Qwen variant with clean response. Solid everyday coding companion.                             |
| `morph-dsv4flash`      | ★★★★☆       | `Code`      | `Fast`     | DeepSeek-based flash model. Lightweight and responsive for rapid code completions.                      |
| `morph-qwen35-397b`    | ★★★★☆       | `Reasoning` | `Fast`     | 397B parameter model — remarkably fast for its scale. Massive reasoning without paying for a cluster.   |
| `morph-minimax27-230b` | ★★★☆☆       | `Reasoning` | `Moderate` | Large 230B model with a `<think>` preamble. Helps complex logic but wastes cycles on simple requests.   |
| `morph-minimax3-428b`  | ★★★☆☆       | `Fallback`  | `Moderate` | Massive 428B free model. Empty on READY but responds to real prompts. Inconsistent but huge free scale. |
| `morph-v3-fast`        | ★★★☆☆       | `Fallback`  | `Fast`     | Fast but echoes the instruction back instead of executing.                                              |
| `morph-compactor`      | ★★★☆☆       | `Fallback`  | `Moderate` | Same instruction-echoing pattern as v3-fast.                                                            |
| `morph-warp-grep-v2.1` | ★★★☆☆       | `General`   | `Slow`     | Slower with a search-focused architecture. Better for log analysis.                                     |


### [Ollama Cloud](https://ollama.com) Models

Ollama Cloud is a cloud-hosted inference service running Ollama behind the scenes, offering a vast model registry without the need to run locally. The free tier provides replenishable credits with generous rate limits — most models respond cleanly and quickly, making it one of the strongest free providers for coding. Ollama Cloud currently has 21 models verified — 20 are ★★★☆☆ or above.

**Free Tier Quota:** 1 Instance / 5-Hour Session Usage / 7-day Weekly Usage

**Base URL:** `https://api.ollama.com`

| Free Model               | Star Rating | Best For    | Speed      | Opinion                                                                                                    |
| :----------------------- | :---------- | :---------- | :--------- | :--------------------------------------------------------------------------------------------------------- |
| `qwen3-coder-next`       | ★★★★★       | `Code`      | `Blazing`  | Zero preamble, instant answers. Reads terminal logs to fix its own bugs. Uncapped usage.                   |
| `qwen3-coder:480b`       | ★★★★★       | `Code`      | `Moderate` | 480B of pure coding muscle. Makes the toughest debugging sessions feel like a chat with a senior engineer. |
| `devstral-2:123b`        | ★★★★★       | `Agent`     | `Fast`     | Purpose-built for agent pipelines — structured tool-use without drift or hallucination.                    |
| `gemma4:31b`             | ★★★★★       | `General`   | `Fast`     | Google's latest 31B. Clean, responsive, and punches above its weight class.                                |
| `gpt-oss:120b`           | ★★★★★       | `General`   | `Blazing`  | Consistent as gravity. Same quality across every provider, same clean output.                              |
| `nemotron-3-nano:30b`    | ★★★★★       | `Reasoning` | `Fast`     | Fast, direct, and efficient. Answers without chain-of-thought fluff.                                       |
| `rnj-1:8b`               | ★★★★★       | `General`   | `Blazing`  | Don't let the 8B fool you — responds faster than most with surprising depth.                               |
| `devstral-small-2:24b`   | ★★★★★       | `Code`      | `Fast`     | Lean and responsive for everyday coding. Does 90% of what the 123B does.                                   |
| `gemma3:12b`             | ★★★★★       | `General`   | `Fast`     | Google's compact powerhouse. Follows complex instructions without rambling.                                |
| `gemma3:27b`             | ★★★★★       | `General`   | `Fast`     | Everything the 12B does well with more breathing room. The sweet spot.                                     |
| `gemma3:4b`              | ★★★★★       | `General`   | `Blazing`  | Blink-and-you-miss-it speed. Perfect for syntax checks.                                                    |
| `minimax-m2.5`           | ★★★★★       | `General`   | `Fast`     | Consistent output that doesn't make you second-guess.                                                      |
| `minimax-m3`             | ★★★★★       | `General`   | `Fast`     | The most polished MiniMax yet. Clean, dependable for whatever your day throws at it.                       |
| `glm-4.7`                | ★★★★★       | `Reasoning` | `Moderate` | Takes a beat longer but the extra thought shows. Thorough answers when correctness beats speed.            |
| `gpt-oss:20b`            | ★★★★☆       | `Reasoning` | `Fast`     | Smaller GPT-OSS variant. Solid reasoning at a fraction of the 120B latency.                                |
| `nemotron-3-ultra`       | ★★★★☆       | `Reasoning` | `Blazing`  | 550B of raw power at blazing speed. Impressive when you can reach past the preamble.                       |
| `ministral-3:14b`        | ★★★☆☆       | `General`   | `Fast`     | Nimble Mistral ministral. Compact but responsive for lightweight coding tasks.                             |
| `ministral-3:8b`         | ★★★☆☆       | `General`   | `Fast`     | 8B ministral variant. Reliable for quick edits and syntax checks.                                          |
| `minimax-m2.1`           | ★★★☆☆       | `General`   | `Slow`     | Earlier MiniMax release. Empty clean output but noticeably slower than m2.5.                               |
| `nemotron-3-super`       | ★★★☆☆       | `Reasoning` | `Slow`     | Deep reasoning with significant latency. Capable but you'll wait for every answer.                         |


### [OpenCode Zen](https://opencode.ai/zen) Models

OpenCode Zen is a curated set of AI models tested and optimized for coding agents by the OpenCode team. The free tier offers 5 models at zero cost through an OpenAI-compatible API — no credit card required for free models (requires adding billing details for API key).

**Free Tier Quota:** 30 RPM / 500 RPD / 1,000,000 TPD

**Base URL:** `https://opencode.ai/zen/v1`

| Free Model                    | Star Rating | Best For      | Speed      | Opinion                                                                                                                                                |
| :---------------------------- | :---------- | :------------ | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deepseek-v4-flash-free`      | ★★★★★       | `Code`        | `Fast`     | The strongest model on OpenCode Zen for coding. Handles multi-turn context tracking smoothly with rapid generation speeds.                             |
| `nemotron-3-ultra-free`       | ★★★★★       | `Code Review` | `Fast`     | Exceptional for code review and syntax linting — pedantic and precise when catching edge cases. Slightly clumsy at generating large template blocks.   |
| `big-pickle`                  | ★★★★☆       | `Fallback`    | `Fast`     | A strong, versatile fallback with rotating capabilities. Handles standard single-file scripting reliably.                                              |
| `mimo-v2.5-free`              | ★★★★☆       | `Code`        | `Moderate` | Lightweight model best kept for small tasks where brief patches matter more than deep logic.                                                           |
| `north-mini-code-free`        | ★★★★☆       | `Fallback`    | `Blazing`  | Micro-scale utility model suited for inline autocomplete or basic regex conversions.                                                                   |


### [OpenRouter](https://openrouter.ai) Models

OpenRouter is a unified API gateway providing access to hundreds of models from dozens of providers through a single endpoint. The free tier offers rate-limited access to community-hosted models (marked with `:free`) that changes often in a specific time period — no credit card required. A great backup when other providers are rate-limited. OpenRouter currently has 15 models verified — 11 are ★★★★☆ or above.

**Free Tier Quota:** 20 RPM / 50 RPD

**Base URL:** `https://openrouter.ai/api/v1`

| Free Model                                             | Star Rating   | Best For      | Speed        | Opinion                                                                                     |
| :----------------------------------------------------- | :------------ | :------------ | :----------- | :------------------------------------------------------------------------------------------ |
| `openai/gpt-oss-120b:free`                             | ★★★★★         | `General`     | `Blazing`    | The same reliable gpt-oss every provider carries. The safest five-star bet on OpenRouter.   |
| `google/gemma-4-31b-it:free`                           | ★★★★★         | `General`     | `Fast`       | Extra headroom over the 26B without sacrificing speed.                                      |
| `nex-agi/nex-n2-pro:free`                              | ★★★★★         | `General`     | `Fast`       | Genuine dark horse. Strength that catches you off guard.                                    |
| `openai/gpt-oss-20b:free`                              | ★★★★★         | `Code`        | `Fast`       | Same reliable output as the 120B but lighter. The everyday driver.                          |
| `nvidia/nemotron-nano-12b-v2-vl:free`                  | ★★★★★         | `Vision`      | `Fast`       | Does text and vision in one call without the bloat.                                         |
| `liquid/lfm-2.5-1.2b-instruct:free`                    | ★★★★★         | `General`     | `Blazing`    | The smallest model that actually answers usefully. Insane response times.                   |
| `google/gemma-4-26b-a4b-it:free`                       | ★★★★☆         | `General`     | `Fast`       | Same clean Gemma 4 quality in a smaller package. Slightly less headroom than the 31B.       |
| `poolside/laguna-m.1:free`                             | ★★★★☆         | `Code`        | `Fast`       | Built by devs for devs. Inline completions that feel like they read your mind.              |
| `poolside/laguna-xs.2:free`                            | ★★★★☆         | `Code`        | `Blazing`    | Snappier than M.1, slightly less depth. Perfect for fast suggestions.                       |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`   | ★★★★☆         | `Reasoning`   | `Moderate`   | Shows its work step by step. Useful for verification, noisy for quick answers.              |
| `nvidia/nemotron-nano-9b-v2:free`                      | ★★★★☆         | `Fallback`    | `Fast`       | Reliable fallback that punches above its 9B weight.                                         |


### [Pollinations AI](https://pollinations.ai) Models

Pollinations AI is a free, no-signup inference provider serving a wide variety of models — from OpenAI and Grok to Qwen, Perplexity, and niche music/safety models. No API key needed, no account required — the only truly zero-friction provider on this list. Pollinations AI currently has 38 models verified — 25 are ★★★☆☆ or above.

**Free Tier Quota:** 60 RPM / Unlimited RPD For Secret Keys; 8 RPM / 11,500 RPD For Publishable Keys

**Base URL:** `https://gen.pollinations.ai/v1` (OpenAI-compatible)

| Free Model            | Star Rating | Best For    | Speed      | Opinion                                                                       |
| :-------------------- | :---------- | :---------- | :--------- | :---------------------------------------------------------------------------- |
| `qwen-coder`          | ★★★★★       | `Code`      | `Fast`     | Focused code output without the fluff.                                        |
| `openai`              | ★★★★★       | `General`   | `Fast`     | Predictable. Drop it into any workflow and get clean answers.                 |
| `openai-large`        | ★★★★★       | `Reasoning` | `Fast`     | Extra headroom when the reasoning gets thorny.                                |
| `gpt-5.4-mini`        | ★★★★★       | `General`   | `Blazing`  | Snappy to the point of feeling instant.                                       |
| `gemma`               | ★★★★★       | `General`   | `Fast`     | Punches above its weight class. Follows complex instructions with precision.  |
| `grok`                | ★★★★★       | `Chat`      | `Fast`     | Surprisingly polished at code. Switches between chat and coding effortlessly. |
| `grok-4-20-reasoning` | ★★★★★       | `General`   | `Fast`     | Tighter than base Grok. Fewer surprises, more consistency.                    |
| `perplexity`          | ★★★★★       | `General`   | `Moderate` | Research-backed answers to coding questions.                                  |
| `nova-fast`           | ★★★★★       | `Code`      | `Blazing`  | For rapid-fire coding loops where waiting isn't an option.                    |
| `llama`               | ★★★★★       | `General`   | `Fast`     | The workhorse. No-nonsense output, zero chatter.                              |
| `qwen-vision`         | ★★★★★       | `Vision`    | `Fast`     | Clean multimodal responses. Screenshots and code mix without the rambling.    |
| `qwen-vision-pro`     | ★★★★★       | `Vision`    | `Fast`     | Polished vision experience. Sharper answers for text and images.              |
| `openai-fast`         | ★★★★☆       | `General`   | `Blazing`  | Built for speed. Quick tasks handled instantly.                               |
| `gpt-5.4`             | ★★★★☆       | `General`   | `Fast`     | Reliable daily coding, though outputs sometimes need a second try.            |
| `kimi-code`           | ★★★★☆       | `Code`      | `Fast`     | Strong on code — use it for programming-specific work.                        |
| `minimax-m2.7`        | ★★★★☆       | `General`   | `Fast`     | Solid and frictionless for everyday tasks.                                    |
| `step-3.5-flash`      | ★★★★☆       | `General`   | `Fast`     | Keeps pace with daily edits and scripts.                                      |
| `qwen-large`          | ★★★★☆       | `General`   | `Moderate` | More parameters, more context. Slightly less direct but more headroom.        |
| `step-flash`          | ★★★★☆       | `Fallback`  | `Fast`     | Dependable fallback — keeps quality up when main model hits limits.           |
| `nova`                | ★★★★☆       | `Agent`     | `Fast`     | Clean output for agent pipelines. Straightforward coding without noise.       |
| `mistral`             | ★★★★☆       | `General`   | `Fast`     | Clean Mistral responses without the full API quota drain.                     |
| `mistral-large`       | ★★★★☆       | `General`   | `Fast`     | Strong Mistral flagship. Crisp output with strong instruction following.      |
| `grok-large`          | ★★★★☆       | `General`   | `Fast`     | Extra Grok headroom for heavier reasoning tasks.                              |
| `perplexity-fast`     | ★★★☆☆       | `General`   | `Blazing`  | Research-backed answers at the speed of light.                                |
| `midijourney-large`   | ★★★☆☆       | `General`   | `Fast`     | Clean empty responses for frictionless automation.                            |


### [SambaNova AI](https://cloud.sambanova.ai) Models

SambaNova AI is a **hardware-driven inference provider** utilizing proprietary Reconfigurable Dataflow Units (RDUs) rather than standard GPUs, removing the traditional hardware-decode bottleneck for incredibly high throughput. The free tier is limited to 20 requests and 200k tokens per day — tight for sustained use. Preview models (DeepSeek-V3.2, Gemma-4-31B-it) require a one-time $5 signup credit that does not replenish. SambaNova AI currently has 5 models verified.

**Free Tier Quota:** 20 RPM / 20 RPD / 200,000 TPD

**Base URL:** `https://api.sambanova.ai/v1`

| Free Model                    | Star Rating | Best For    | Speed      | Opinion                                                                                                                                          |
| :---------------------------- | :---------- | :---------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| `DeepSeek-V3.1`               | ★★★★★       | `Agent`     | `Blazing`  | Production-grade flagship with elite reasoning at blazing speeds. The 20 RPD cap limits sustained use — better quota on Auriko or Hugging Face.  |
| `DeepSeek-V3.2`               | ★★★★☆       | `Reasoning` | `Blazing`  | **Preview** — Blazing fast on RDUs but requires $5 signup credit that does not replenish. Use while it lasts.                                    |
| `Meta-Llama-3.3-70B-Instruct` | ★★★★☆       | `General`   | `Fast`     | The traditional benchmark engine. Interprets dense, multi-variable project constraints with high structural reliability.                         |
| `gemma-4-31B-it`              | ★★★☆☆       | `General`   | `Blazing`  | **Preview** — Google's newest runs fast but dies with the $5 credit. Stops working once the bonus is drained.                                    |
| `gpt-oss-120b`                | ★★★☆☆       | `Fallback`  | `Moderate` | The same 117B MoE flagship that dominates on Groq. Available on SambaNova but with noticeably higher latency (~3.5s).                            |

---

## Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details.
