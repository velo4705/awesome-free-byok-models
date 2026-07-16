# Contributing to awesome-free-byok-models

We welcome contributions to this list. It only exists because people test things before adding them — please do the same.

## How to Contribute

1. **Test the provider yourself** — check that endpoints work and models respond before opening anything.
2. **Open an Issue** if you are not sure whether a provider or model fits.
3. **Submit a PR** once you have confirmed it works.

## Before You Submit

### 1. Make Sure It Is Actually Free

The provider must be genuinely free and stay that way without paying. That means:
- No paywalls
- No trial credits that run out with no free tier underneath
- No one-time credits
- No "Join the waitlist" walls

**Pass:** The model responds without asking for money.

**Fail:** You get `402 Payment Required`, `403 Forbidden`, or a message telling you to upgrade.

### 2. Test 3 Times in a Row

Send `"State the word READY."` to a model 3 times across the provider's catalog. This catches hidden hard limits that require an upgrade. At least one model must pass for the provider to be listed.

**Pass:** One or more models return `READY` 3 times, or something useful within a reasonable time.

**Fail:** Every model times out, returns `404`, `5xx`, or drops the connection.

A single `"READY"` could be luck. Three in a row means the endpoint is stable enough.

### 3. No Reverse-Engineered Access

The provider must not rely on reverse engineering or unauthorized scraping of third-party APIs. Proxy and gateway services that route through official channels are fine — the line is drawn at open admission of reverse engineering.

**Pass:** The provider runs their own inference stack, has an official partnership or reseller agreement, or builds their own models.

**Fail:** The provider openly states their endpoints rely on "reverse engineering" or "public web scraping" of third-party APIs without authorization.

### 4. Use a Standard API Format

The model must accept OpenAI-compatible chat completion payloads or have a documented REST API.

**Pass:** Same prompt format and headers work across models from the same provider.

**Fail:** Requires a custom SDK or proprietary format just to send a message.

## How We Test Internally

We don't use a hardcoded model list. Instead:

0. Grab an API key from the provider and figure out their endpoint format.

1. Fetch all model IDs from the provider's `GET /v1/models` endpoint.
2. Hit every model with `"State the word READY."` in parallel. Non-chat models (embeddings, rerankers, etc.) will fail — that is expected.
3. Split results into three buckets:
   - **Passed** — responded with valid output or an empty string (`""`). Still working. Done.
   - **Failed permanently** — returned `402`, `403`, `404`, `503`, or similar. Done.
   - **Retryable** — returned `429` or a connection error. These go to the retry pass.
4. Retry the retryable group up to 3 more times with exponential backoff (1s → 2s → 4s delay). Any model still failing after all retries is rate-limited.
5. Re-run after a minute to confirm at least 3 consecutive rounds pass for every stable model.

This catches dead endpoints, renamed models, and quota changes automatically.

If a model is rate-limited, wait a day or two for its quota to refill. If it still fails, drop it until it passes again.

## Formatting

### Top 10 Table

```
| Rank | Model Name | Host Provider | The Simple Reason to Choose It |
| :--- | :--- | :--- | :--- |
| **X** | `model-id` | **Provider** | Brief, punchy description. |
```

### Per-Provider Table

```
| Free Model | Context | Best For | Latency |
| :--------- | :------ | :------- | :------ |
| `model-id` | 128K    | `Code`   | `Fast`  |
```

For the Context column, note the model's input/output context window.

## Quality Standards

- If an endpoint starts returning `429` errors, submit a PR to remove it or note its degraded status.
- Be clear about the difference between burst compute and production-grade models.
- Link directly to official docs. No redirect chains.
- Keep PRs focused. Do not mix model additions with documentation fixes.

## Pull Request Template

Include this in your PR description:

```
## Testing Context
- **Provider:**
- **Model ID:**
- **Stability Check:** (e.g., "3/3 requests returned READY")
```

## Thank You

Every contribution helps keep this list freshly updated.
