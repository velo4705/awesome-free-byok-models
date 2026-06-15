# Contributing to awesome-free-byok-models

Contributions are welcome as long as the endpoint works. This list only exists because people test things before adding them — please do the same.

## How to Contribute

1. **Test the model yourself** before opening anything.
2. **Open an Issue** if you are not sure whether a model fits.
3. **Submit a PR** once you have confirmed it works.

## Before You Submit

### 1. Make Sure It Is Actually Free

No credit card required. No trial credits that run out. No "join the waitlist." The endpoint should work every day without paying.

**Pass:** The model responds without asking for money.

**Fail:** You get `402 Payment Required`, `403 Forbidden`, or a message telling you to upgrade.

### 2. Test 3 Times in a Row

Send the same `"State the word READY."` prompt 3 times. All 3 must come back with a valid response.

**Pass:** All 3 return `"READY"` or something useful within a reasonable time.

**Fail:** Any one of them times out, returns `404`, `5xx`, or drops the connection.

A single `"READY"` could be luck. Three in a row means the endpoint is stable enough to use.

### 3. Use a Standard API Format

The model must accept OpenAI-compatible chat completion payloads or have a documented REST API.

**Pass:** Same prompt format and headers work across models from the same provider.

**Fail:** Requires a custom SDK or proprietary format just to send a message.

## How We Test Internally

We do not maintain a hardcoded list of models. Instead:

1. Fetch all model IDs from the provider's `GET /v1/models` endpoint.
2. Test every model with the same `"State the word READY."` prompt in parallel. Non-chat models (embeddings, rerankers, etc.) will fail this prompt — that is expected.
3. Split results into three buckets:
   - **Passed** — responded with valid output. Done.
   - **Failed permanently** — returned `402`, `403`, `404`, `503`, or similar. Done.
   - **Retryable** — returned `429` or a connection error. These go to the retry pass.
4. Retry the retryable group up to 5 more times with exponential backoff (1s → 2s → 4s delay). Each pass narrows the set as models start working. Any model still failing after all retries is rate-limited.
5. Re-run the whole thing after a minute to confirm at least 3 consecutive successful rounds pass for every stable model.

This catches dead endpoints, renamed models, and quota changes automatically.

## Formatting

### Top 10 Table

```
| Rank | Model Name | Host Provider | The Simple Reason to Choose It |
| :--- | :--- | :--- | :--- |
| **X** | `model-id` | **Provider** | Brief, punchy description. |
```

### Per-Provider Table

```
| Free Model | Star Rating | Best For | Speed | Opinion |
| :--- | :--- | :--- | :--- | :--- |
| `model-id` | ★★★★★ | `Code` | `Fast` | One punchy sentence. |
```

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

Every contribution helps keep this list from filling up with broken endpoints.
