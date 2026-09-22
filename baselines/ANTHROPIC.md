# Anthropic / Claude Baseline

_Last researched: 2026-09-22_

## Current routing summary

| Model | Baseline role | Strong suits | Main weaknesses / cautions |
|---|---|---|---|
| Claude Fable 5.1 | Frontier knowledge/coding/research | Deep difficult coding, long-running research, low-level reasoning, professional knowledge work | Very expensive; safeguard fallback complicates comparisons; some users report partial completion/laziness |
| Claude Opus 5.5 | New high-end daily frontier candidate | Agentic coding and knowledge work near/above Fable-class at materially lower price; faster/clearer than Opus 5 | Released today: independent/user evidence is immature; honeymoon bias likely |
| Claude Sonnet 5 | Mid/high-tier agentic workhorse | Thorough large-codebase work, multimodal, cheaper per token than Opus/Fable | Very high token consumption at higher effort; cost per completed task can erase per-token savings |
| Claude Mythos 5.1 | Restricted high-risk research tier | Same underlying intelligence as Fable 5.1 with safeguards tuned for trusted cyber/life-science use | Not a normal general-routing option; trusted-access restrictions |

## Claude Fable 5.1

### Independent benchmark signal

Artificial Analysis's September 1 evaluation put Fable 5.1 at the top of the then-current Intelligence Index. Under the newer v4.3 rebasing, Fable 5.1 and GPT-6 Astra are tied at **53**.

Fable 5.1 also showed exceptionally strong Terminal-Bench, SciCode, and knowledge-work performance.

Important caveat: Artificial Analysis evaluated Fable 5.1 with Anthropic's production fallback system. Safety-flagged requests were sometimes routed to Opus-family models, accounting for a small share of output tokens. This makes "Fable 5.1" partly a production-system result rather than a pure isolated-base-model result.

Sources:

- https://artificialanalysis.ai/articles/claude-fable-5-1
- https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3

### Provider signal

Anthropic markets Fable 5.1 as its most capable generally available model for coding and knowledge work.

Pricing:

- $10/M input
- $50/M output
- heavily discounted cache reads

Source:

- https://www.anthropic.com/claude/fable

### Human-review signal

Positive forum themes:

- especially strong on low-level programming such as Rust/C/C++/assembly;
- excellent on difficult debugging and deep repository analysis;
- stronger than aggregate charts can convey for some expert workflows.

Negative themes:

- premium price is difficult to justify when cheaper models/harness routing can do most of the work;
- some users preferred Fable 5 over 5.1 because 5.1 appeared more willing to stop early, create follow-up issues, or ask obvious questions;
- heavy use can be prohibitively expensive.

Representative threads:

- https://www.reddit.com/r/ClaudeAI/comments/1w4k4pz/claude_fable_51/
- https://www.reddit.com/r/ClaudeAI/comments/1w4za9d/fable_51_vs_claude_code_model_routing/

### Baseline prior

Use when **deep judgment or correctness dominates cost**: difficult architecture, low-level code, deep review, research, and high-stakes knowledge work.

Do not use as the default implementer solely because it tops a benchmark.

---

## Claude Opus 5.5

### Current evidence status

Released **2026-09-22**, so this is a provisional baseline.

Reuters reports Anthropic positions Opus 5.5 near Fable 5.1 on most tasks at substantially lower operating cost than Opus 5.

Reported API pricing:

- $4/M input
- $20/M output

Anthropic says it is faster, clearer, uses fewer tokens per task, and leads its reported agentic-coding / real-world knowledge-work evaluations.

Sources:

- https://www.reuters.com/business/anthropic-unveils-claude-opus-55-2026-09-22/
- https://www.reddit.com/r/Anthropic/comments/1wnecjb/introducing_claude_opus_55_the_first_model_in_our/

### Human-review signal

Day-one impressions are positive but extremely low confidence.

Early reports emphasize:

- much faster than Opus 5;
- clearer/plain-language output;
- strong UI bug finding and practical coding;
- better apparent subscription mileage.

Cautions:

- it still produces bugs;
- some users notice residual over-verification/delegation behavior;
- all first-day enthusiasm should be treated as honeymoon evidence.

Representative threads:

- https://www.reddit.com/r/ClaudeAI/comments/1wnil7n/opus_55_in_claude_code_is_crazy_fast_especially/
- https://www.reddit.com/r/Anthropic/comments/1wnl3k8/opus_55_first_impressions/
- https://www.reddit.com/r/ClaudeAI/comments/1wnl999/claudemd_for_opus_55_based_on_anthropics_official/

### Baseline prior

**High-priority model to test personally.**

If the launch claims hold up, Opus 5.5 may become a more rational daily high-end Claude choice than Fable 5.1 because its performance is close while its economics are much better.

Confidence: **low until several weeks of external use data accumulate.**

---

## Claude Sonnet 5

### Independent benchmark signal

Current Artificial Analysis v4.3:

- Sonnet 5 Max: Intelligence Index **38**
- ~1M context
- around 75–80 t/s
- very high total output-token use on the evaluation

Sources:

- https://artificialanalysis.ai/models/claude-sonnet-5
- https://artificialanalysis.ai/models/releases/claude-sonnet-5

### Human-review signal

This is one of the clearest examples where "cheaper per token" and "cheaper per task" can diverge.

Positive reports:

- unusually thorough;
- explores multiple possibilities before committing;
- valuable for complex architecture in large codebases;
- some users prefer the extra checking because late architecture mistakes are expensive.

Negative reports:

- repeatedly described as a "token monster";
- reports of 3–5x token use versus Sonnet 4.6 on similar work;
- some teams report it slower and more expensive per completed task than Opus 4.8;
- additional thinking does not always translate into better output.

Representative threads:

- https://www.reddit.com/r/ClaudeAI/comments/1ukoszu/sonnet_5_is_a_token_monster/
- https://www.reddit.com/r/ClaudeCode/comments/1uzyuwr/anyone_else_think_sonnet_5_is_a_joke/

### Baseline prior

Good candidate for **thorough architecture/review and complex bounded engineering**, but monitor task-level cost rather than token price.

Use max effort selectively.

---

## Claude Mythos 5.1

Anthropic states Fable 5.1 and Mythos 5.1 are the same underlying model with different safeguards. Fable is generally available; Mythos is for trusted-access programs in cybersecurity and life sciences.

Source:

- https://www.anthropic.com/claude-fable-and-mythos-5-1

### Baseline prior

Do not treat Mythos as an ordinary model-routing alternative.

Document it when evaluating authorized high-risk scientific/security workflows where its access tier is actually available.
