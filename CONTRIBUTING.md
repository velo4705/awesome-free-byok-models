# Contributing to awesome-free-byok-models

Thanks for your interest in helping keep this list high-quality! This repository is a curated, verified testbed for free API endpoints. Because we prioritize reliability, we have a specific process for contributions.

## How to Contribute

1. **Verify first:** Test your endpoint personally to ensure it meets our standards.
2. **Open an Issue:** If you are unsure if a model meets our quality bar, open a "Vetting Issue" first.
3. **Submit a PR:** Once confirmed, fork the repository, update the relevant table in `README.md`, and submit your PR.

## Verification Checklist

Before adding a model or provider, ensure it passes these tests:

- [ ] **Truly Free:** No credit cards, no "trial-only" credits, and no "waitlist-to-access" requirements.
- [ ] **Stability:** The endpoint must handle 5 consecutive requests without returning empty payloads (`""`) or timing out.
- [ ] **Compatibility:** Must support standard OpenAI-compatible or REST API headers.

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

* **Accuracy:** If an endpoint starts returning `429` errors or shedding payloads, please submit a PR to move it to "Experimental / Failed Testbeds."
* **Transparency:** Clearly distinguish between "Burst Compute" and "Production Grade" models.
* **Direct Links:** Always link directly to official documentation or model hubs. No redirect chains.
* **PR Scope:** Keep pull requests focused. Do not mix model additions with documentation fixes.

## Pull Request Template

When submitting, please include this in your PR description:

```markdown
## Testing Context
- **Provider:** 
- **Model ID:**
- **Stability Check:** (e.g., "Tested 10 requests, 10/10 success")
- **Free Tier Verified?** (Yes/No)

```

## Thank You!

Your contributions directly prevent the community from wasting time on broken or "bait-and-switch" API endpoints. We appreciate your rigor.
