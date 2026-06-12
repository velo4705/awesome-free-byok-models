# Awesome Free BYOK Models 🚀

> ⏰ **Last Verified: June 12, 2026** - All Models are Verified from their API Providers.

A curated list of the **best high-performance**, **free-tier AI models** you can use to **supercharge your coding setup** without paying for expensive monthly subscriptions.

By using a **Bring Your Own Key (BYOK)** approach, you can plug your free API keys directly into coding tools like **VS Code extensions, terminal assistants, or code editors**. It doesn't even require a **credit card** for the best models!

> 💡 **Pro tip:** Free tiers rotate often. If a model hits rate limits, switch to another — there's always a backup in this list. 
> **Always verify** current quotas on the provider's console before building workflows.

## 📋 Contents

- [🏢 The Best 3 API Providers](#the-best-3-api-providers)
- [🏆 The Top 10 Recommended Free Models](#the-top-10-recommended-free-models)
- [📂 Individual Provider Showcases](#the-deep-dive-individual-provider-showcases)
  - [⚡ Groq](#groq-api-models)
  - [🌐 Google Gemini](#google-gemini-models)
  - [🍊 Mistral AI](#mistral-ai-models)
  - [🌀 SambaNova AI](#sambanova-ai-models)
  - [🧠 Cerebras AI](#cerebras-ai-models)
- [CONTRIBUTING](#contributing)
- [LICENSE](#license)

---

## 🏢 The Best 3 API Providers

If you are signing up for free accounts to get API keys, these are the **three best platforms** to look at first.

| Provider | The Simple Vibe | Why It Matters For You |
| :--- | :--- | :--- |
| **Groq** | Speedy Accurate | Code prints out on your screen instantly. If you hate waiting for an AI to finish typing, this is your go-to. |
| **SambaNova** | Hardware Speed | Proprietary RDU architecture removes traditional GPU bottlenecks, delivering incredibly high throughput for massive models. |
| **Mistral AI** | Clean & Efficient | Builds models that punch above their weight class with exceptionally clean instruction following and compact, efficient execution profiles. |

---

## 🏆 The Top 10 Recommended Free Models

The absolute best free models available right now, ranked by how well they handle **daily coding tasks**. This does **NOT** include vision models — all models here are for text completions.

| Rank | Model Name | Host Provider | The Simple Reason to Choose It |
| :--- | :--- | :--- | :--- |
| **1** 🏆 | `openai/gpt-oss-120b` | **Groq** | **For All Tasks.** The undisputed champion. Writes incredibly clean code, never hits rate-limit walls, and responds almost instantly. |
| **2** 🥈 | `DeepSeek-V3.1` | **SambaNova** | **For Agentic Pipelines.** A massive hybrid mixture model on SambaNova's RDU architecture — blazing-fast inference with elite reasoning, optimized as a background planner for multi-step agent actions. |
| **3** 🥉 | `qwen/qwen3-32b` | **Groq** | **For Code.** Phenomenal code generation that dumps into your editor at lightning speed. The `<think>` preamble is a minor trade-off for its coding depth. |
| **4** | `DeepSeek-V3.2` | **SambaNova** | **For Deep Reasoning.** The pinnacle of hardware-optimized reasoning on SambaNova's infrastructure — near-instant token speeds with elite multi-file architectural analysis. |
| **5** | `mistral-code-agent-latest` | **Mistral AI** | **For Agentic Coding.** Purpose-built for autonomous agents with native tool use, structured JSON outputs, and multi-step coding workflows. |
| **6** | `models/gemini-3.1-flash-lite` | **Google Gemini** | **For Quick Tasks.** Lightning-fast with ~500 RPD free tier — the only Gemini model with enough quota for sustained agentic triaging. |
| **7** | `mistral-large-2512` | **Mistral AI** | **For Instruction Following.** Top-tier multilingual reasoning with strict adherence to complex system prompts and massive file contexts. |
| **8** | `gpt-oss-120b` | **Cerebras** | **For Speed.** The same 117B MoE champion running on Cerebras' wafer-scale engine — sub-second responses for rapid-fire coding loops. |
| **9** | `zai-glm-4.7` | **Cerebras** | **For Large Context.** 131K context window optimized for long-horizon agentic coding — handles massive project contexts at blazing Cerebras speeds. |
| **10** | `codestral-latest` | **Mistral AI** | **For Code Completions.** Built from the ground up for programming — flies through auto-completions and single-file inline edits across dozens of languages. |

---

## 📂 The Deep-Dive: Individual Provider Showcases

These tables break down the notable free models available within each provider's ecosystem. Ratings are based on how well they handle **real-world development** demands like typing speed, following instructions, and not getting confused by **large projects**.

### ⚡ [Groq API](https://console.groq.com) Models
Groq is famous for providing the **absolute lowest streaming latency** in the API market, outrunning traditional cloud providers by a massive margin. If you want a setup where your terminal files patch instantly without the typical spinning wheel delay, you want a model from this list.

| Free Model | Star Rating | The honest opinion on how it handles your work |
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

---

### 🌐 [Google Gemini](https://aistudio.google.com) Models
Gemini offers large context windows on paper, but the free tier's **rate limits vary by model** — Flash-lite variants enjoy ~500 RPD, while standard models can be as low as 20 RPD. Use Gemini for quick, targeted tasks and single-file edits — not marathon sessions.

| Free Model | Star Rating | The honest opinion on how it handles your work |
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

---

### 🍊 [Mistral AI](https://console.mistral.ai) Models
Mistral AI is highly regarded in the **open-weights and developer communities** for building models that punch far above their **parameter weight class**. They emphasize exceptionally clean instruction following, compact sizing, and highly efficient execution profiles.

| Free Model | Star Rating | The honest opinion on how it handles your work |
| :--- | :--- | :--- |
| `mistral-large-latest` / `mistral-large-2512` | ⭐⭐⭐⭐⭐ | **BEST.** Mistral's absolute crown jewel flagship engine. Top-tier multi-lingual reasoning, deep system architecture capabilities, and flawless focus across massive files. |
| `codestral-latest` / `codestral-2508` | ⭐⭐⭐⭐☆ | **CODE COMPLETION ONLY.** Built from the ground up for programmers. Flies through auto-completions and single-file inline edits across dozens of languages. |
| `mistral-code-latest` | ⭐⭐⭐⭐☆ | **CODE COMPLETION ONLY.** Dedicated code generation engine. Fast, precise completions across dozens of programming languages for inline editing workflows. |
| `mistral-code-fim-latest` | ⭐⭐⭐⭐☆ | **CODE COMPLETION ONLY.** Fill-in-Middle specialist. Designed for smart inline insertion within existing code blocks and contextual completions. |
| `mistral-code-agent-latest` | ⭐⭐⭐⭐⭐ | **BEST FOR AGENTS.** Purpose-built for autonomous agents with native tool use, structured JSON outputs, and multi-step coding workflows. |
| `mistral-medium-3.5` / `mistral-medium-3-5` | ⭐⭐⭐⭐☆ | Exceptional balance of price-to-performance. Highly responsive reasoning loops for structural software layouts, just missing 5 stars due to niche edge-case gaps. |
| `mistral-medium-3` | ⭐⭐⭐⭐☆ | Trusted, incredibly stable version of the Medium line. Keeps a rigid handle on instructions and delivers clean boilerplate code without empty chatter. |
| `mistral-medium-2604` | ⭐⭐⭐⭐☆ | A responsive iteration within the Medium family. Predictable execution flow and excellent at breaking down tricky structural bugs. |
| `devstral-medium-latest` / `devstral-medium-2507` | ⭐⭐⭐⭐☆ | **AGENT ROUTING ONLY.** Specialized, highly streamlined Medium variation optimized specifically to function inside automated developer continuous task loops. |
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
| `magistral-small-latest` | ⭐⭐⭐☆☆ | Experimental variant block. Good for stylistic parsing tests, but consistency slips behind official production branches on strict syntax rules. |
| `magistral-small-2509` | ⭐⭐⭐☆☆ | Experimental Magistral variant. Responsive for basic queries but less consistent than official production branches on strict formatting. |
| `magistral-medium-latest` | ⭐⭐⭐☆☆ | Experimental Magistral medium. Handles expanded reasoning tasks but can drift slightly on strict syntax enforcement. |
| `magistral-medium-2509` | ⭐⭐⭐☆☆ | Experimental Magistral snapshot. Capable for general-purpose queries but lacks the polish of official Medium releases. |
| `ministral-8b-latest` / `ministral-8b-2512` | ⭐⭐⭐☆☆ | **LIGHT SCRIPTING.** Fast option for minor string manipulations and terminal setup queries. Frequently leans into text descriptions over pure raw code. |
| `voxtral-small-latest` / `voxtral-small-2507` | ⭐⭐☆☆☆ | **AUDIO LOGIC ONLY.** Pinned voice-to-text layer model optimized for speech translation. Entirely unsuited for parsing complex software files. |
| `ministral-3b-latest` / `ministral-3b-2512` | ⭐⭐☆☆☆ | **LIGHT SCRIPTING.** Micro footprint that initializes instantly. Good for spelling transformations but completely loses coherence on deep runtime errors. |
| `mistral-tiny-latest` / `mistral-tiny-2407` | ⭐⭐☆☆☆ | Legacy tiny build block. Decent processing speed for simple text replacement, but struggles heavily under modern coding paradigms. |
| `voxtral-mini-latest` / `voxtral-mini-2507` | ⭐⭐☆☆☆ | **AUDIO LOGIC ONLY.** Highly specialized micro audio engine that tends to truncate standard text outputs early because it anticipates audio streaming input. |

---

### 🌀 [SambaNova AI](https://cloud.sambanova.ai) Models
SambaNova AI is a **hardware-driven inference provider** utilizing proprietary Reconfigurable Dataflow Units (RDUs) rather than standard GPUs. By running open-weight frameworks natively on dataflow architectures, they remove the **traditional hardware-decode bottleneck**. This setup provides incredibly high tokens-per-second throughput and low multi-turn response times, making it a natural choice for rapid, agentic continuous-task pipelines. The free tier offers generous rate limits suitable for sustained agentic use.

| Free Model | Star Rating | The honest opinion on how it handles your work |
| :--- | :--- | :--- |
| `DeepSeek-V3.2` | ⭐⭐⭐⭐⭐ | **BEST.** The absolute pinnacle of hardware-optimized reasoning. Running on fine-grained sparse attention mechanisms, it hits near immediate end-to-end token execution speeds and effortlessly untangles high-level architectural errors or logic puzzles. |
| `DeepSeek-V3.1` | ⭐⭐⭐⭐⭐ | **BEST.** An incredibly fast, massive hybrid mixture model. Running in non-thinking mode over SambaNova's RDU pipelines, it functions as a premium, highly responsive background planner for code-routing and multi-step agent actions. |
| `Meta-Llama-3.3-70B-Instruct` | ⭐⭐⭐⭐☆ | The traditional benchmark engine. It interprets dense, multi-variable project constraints with high structural reliability, only trailing the newer architectures slightly on processing heavy visual context. |
| `gemma-4-31B-it` | ⭐⭐⭐⭐☆ | Google's newest instruction-tuned model block. Strikes a masterclass balance between low parameter footprint and high-level structural syntax mastery, blazing through system boilerplates. |
| `gpt-oss-120b` | ⭐⭐⭐☆☆ | The same 117B MoE flagship that dominates on Groq. Available on SambaNova but with noticeably higher latency (~3.5s) compared to its sub-second performance on Groq. |

---

### 🧠 [Cerebras AI](https://cloud.cerebras.ai) Models
Cerebras AI is defined by its **Wafer-Scale Engine (WSE) technology**, which integrates memory, compute, and interconnects onto a single, massive silicon wafer rather than relying on clusters of traditional GPUs. This architecture fundamentally solves the **"memory wall"** that throttles inference speed, allowing it to deliver industry-leading token throughput (often 2,500+ tokens/second).

| Free Model | Star Rating | The honest opinion on how it handles your work |
| :--- | :--- | :--- |
| `gpt-oss-120b` | ⭐⭐⭐⭐☆ | **For All Tasks.** The same 117B MoE flagship that dominates on Groq. Delivers sub-second responses on Cerebras' wafer-scale architecture with solid reliability across standard developer workflows. |
| `zai-glm-4.7` | ⭐⭐⭐⭐☆ | A 131K context window model optimized for rapid agentic coding. Handles modular code snippets efficiently at blazing speeds — ideal for large-context agent loops and multi-file reasoning tasks. |

---

## CONTRIBUTING

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details.

## LICENSE

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

This project is released under the [CC0-1.0](LICENSE.md) license.