# Contributing to awesome-free-byok-models

We welcome contributions to this list. It only exists because people test things before adding them — please do the same.

## Before You Submit A Pull Request

### 1. Make Sure It Is Actually Free

The provider must be genuinely free and stay that way without paying. That means:
- No paywalls.
- No trial credits that run out with no free tier underneath.
- No one-time credits.
- No "Join the waitlist" walls.
- No gated services that requires to join a server/group by force, just to enable core functionality (the free model access).

It must also have an option to obtain an API Key (which is necessary for BYOK-supported providers).

**Pass:** The model responds without asking for money.

**Fail:** You get `402 Payment Required`, `403 Forbidden`, or a message telling you to upgrade.

### 2. Test using the Verifier

Use the [Verifier](scripts/verify.py). For most providers you just set `API_KEY` and `BASE_URL`. It is recommended to download this script and run it locally.

1. Get the provider's API key and Base URL.
2. Copy `scripts/.env.example` to your `.env` file and fill in `API_KEY` and `BASE_URL` (add `ACCOUNT_ID` too if your URL has `{account_id}`, like Cloudflare).
3. Install dependencies required for the Verifier: `pip install requests python-dotenv`.
4. Run `python verify.py` — it detects the provider from your `BASE_URL`, tests every model, and retries rate-limits.
5. Open `verified_models_YYYY-MM-DD.txt` — that's your proof. Paste it all into the PR.

If it finds more than 40 models, keep 40 for the README. Drop uncensored / roleplay / safety / guard models first, and double-check the rest are actually free in your dashboard.

### 3. No Reverse-Engineered Access

The provider must not rely on reverse engineering or unauthorized scraping of third-party APIs. Proxy and gateway services that route through official channels are fine — the line is drawn at open admission of reverse engineering.

**Pass:** The provider runs their own inference stack, has an official partnership or reseller agreement, or builds their own models.

**Fail:** The provider openly states their endpoints rely on "reverse engineering" or "public web scraping" of third-party APIs without authorization.

### 4. Use a Standard API Format

The model must accept OpenAI-compatible chat completion payloads or have a documented REST API.

**Pass:** Same prompt format and headers work across models from the same provider.

**Fail:** Requires a custom SDK or proprietary format just to send a message.

## Formatting

### Top 10 Table

```
| Rank  | Model Name | Host Provider | The Simple Reason to Choose It  |
| :---- | :--------- | :------------ | :------------------------------ |
| **X** | `model-id` | **Provider**  | Brief, punchy description.      |
```

### Per-Provider Table

```
| Free Model | Context | Best For | Latency |
| :--------- | :------ | :------- | :------ |
| `model-id` | 128K    | `Code`   | <time>  |
```

For the Context column, note the model's input/output context window. Latencies are recorded from the log file itself.

## Pull Request Template

The PR should have a title that states "Add [PROVIDER_NAME]". Anything else is closed without review.

Below here is a template to fill out exactly as shown below.

```

<-- Explain why this provider is worth adding -->

<-- Provider link (website) -->

Free Tier Quota:

Base URL:

<-- Log file contents -->

```

## Thank You

Every contribution helps keep the list freshly updated.
