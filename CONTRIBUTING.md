# Contributing to awesome-free-byok-models

Thanks for your interest in helping keep this list high-quality! This repository is a curated, verified testbed for free API endpoints. Because we prioritize reliability, we have a specific process for contributions.

## How to Contribute

1. **Verify first:** Test your endpoint personally to ensure it meets our standards.
2. **Open an Issue:** If you are unsure if a model meets our quality bar, open a "Vetting Issue" first.
3. **Submit a PR:** Once confirmed, fork the repository, update the relevant table in `README.md`, and submit your PR.

## Verification Checklist

Before adding a model or provider, ensure it passes all three checks below. To make the process easier, we recommend writing a small script that **discovers models from the provider's registry API** and tests them all in one pass — this is what we do internally. 

We recommend storing your API key in a **`.env` file** to keep it out of version control.

### ✅ 1. Truly Free — Not paywalled or trial-gated
No credit cards, no "trial-only" credits, and no "waitlist-to-access" when signing up. 

It should also be **Replenishable** (Resets every day/week/month) and doesn't offer "one-time free offers".

**Pass:** Model responds without asking for payment.
**Fail:** Returns `402 Payment Required`, `403 Forbidden`, or requires upgrading to use.

### ✅ 2. Stability — 3 consecutive requests must succeed
Send the **same `"State the word READY."` prompt 3 times in a row**. All 3 must return valid responses.

**Pass:** All 3 runs return `"READY"` or equivalent valid output within reasonable time.  
**Fail:** Any request times out, returns `404`, `5xx`, or drops the connection.

> ⚡ A single request could be luck. 3 in a row proves the endpoint is stable enough for real use.

### 🔍 How we verify internally
We don't maintain a hardcoded model list. Instead, our test suite:
1. **Fetches all model IDs** from the provider's `GET /v1/models` registry.
2. **Tests every model** with the same `"State the word READY."` prompt in parallel. Non-Chat models (embeddings, rerankers, etc.) will likely fail from this prompt.
3. **Results split into three groups:**
   - ✅ **Passed** — responded with valid output. Ignored in retries.
   - ❌ **Failed permanently** — returned `402`, `403`, `404`, `503` or similar. Ignored in retries.
   - 🔄 **Retryable** — returned `429` or connection exception. These move to the retry pass.
4. **Retries** only the 🔄 group up to **3 extra passes** with exponential backoff (1s → 2s → 4s delay). Each pass narrows the set as models start working. Any model still failing after all retries is flagged as rate-limited.
5. **Re-run the full process** after waiting a minute to confirm at least 3 consecutive successful rounds pass for all stable models.

This catches dead endpoints, renamed models, and quota changes automatically. You can replicate this approach with any language that supports HTTP requests.

### ✅ 3. Compatibility — Standard API format
The model must accept standard OpenAI-compatible chat completion payloads or provide a documented REST API.

**Pass:** Same prompt format and headers work across models within the provider.  
**Fail:** Requires custom SDKs, proprietary formats, or non-standard auth to function.

## Formatting Guidelines

### Adding to the Recommended Models Table
Use this exact table format to maintain consistency:

```markdown
| Rank | Model Name | Host Provider | The Simple Reason to Choose It |
| :--- | :--- | :--- | :--- |
| **X** | `model-id` | **Provider** | Brief, punchy description of utility. |

```

### Adding to the Model Performance Table

Use this exact table format for detailed model ratings for a specific category-type model:

```markdown
| Free Model | Star Rating | The honest opinion on how it handles your work |
| :--- | :--- | :--- |
| `model-id` | ⭐⭐⭐⭐⭐ | **TITLE.** Detailed honest opinion on performance/reliability. |

```

## Contribution Quality Standards

* **Accuracy:** If an endpoint starts returning `429` errors or shedding payloads, please submit a PR to remove it or note its degraded status.
* **Transparency:** Clearly distinguish between "Burst Compute" and "Production Grade" models.
* **Direct Links:** Always link directly to official documentation or model hubs. No redirect chains.
* **PR Scope:** Keep pull requests focused. Do not mix model additions with documentation fixes.

## Pull Request Template

When submitting, please include this in your PR description:

```markdown
## Testing Context
- **Provider:** 
- **Model ID:**
- **Stability Check:** (e.g., "3/3 requests returned READY")

```

## Thank You!

Your contributions directly prevent the community from wasting time on broken or "bait-and-switch" API endpoints. We appreciate your rigor.
