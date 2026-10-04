# Google / Gemini Baseline

_Last researched: 2026-10-04_

For the latest release delta, see [2026-10-04 model release update](../research/models/2026-10-04-new-model-release-update.md).

## Current routing summary

| Model | Public-prior role | Strong suits | Main cautions | Confidence |
|---|---|---|---|---|
| **Gemini 4 Argon** | Restricted frontier watchlist | long-horizon coding, automation, multimodal professional work, cyber, low hallucination tendency | restricted rollout; little genuine user evidence | Low |
| **Gemini 3.8 Flash** | Generally available fast worker | high throughput, multimodal work, inexpensive coding/execution | below frontier broad intelligence; instruction/harness complaints | High |

## Gemini 4 Argon

Announced September 30.

### Availability

Argon is **not yet broadly available**.

Google initially rolled it out to trusted cyber defenders and selected testers through Fairwind and says broader release will begin with paid API customers and Google AI Ultra subscribers.

This severely limits community evidence.

Official source:

- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/

### Provider position

Google targets:

- long-horizon coding;
- enterprise knowledge work including legal/finance;
- autonomous cybersecurity defense;
- multimodal professional tasks.

Launch specifications include:

- 1M context;
- extended long output via continuation;
- text/image/video/speech input;
- introductory $2/M input, $10/M output;
- 95% cached-input discount;
- later standard pricing $4/M input, $20/M output.

Google reports DeepSWE 77.9%, AutomationBench 51.3%, LVBench 91.7%, and CWE-bench v1 68%. These are provider claims.

### Independent benchmark signal

Artificial Analysis reports Argon High at approximately **53** on its broad Intelligence Index, in the Astra-class range.

Important characteristics:

- very strong automation;
- solid terminal performance;
- roughly 62k output tokens/task versus ~27k for Astra Max in the cited evaluation;
- launch cost efficiency is heavily price-driven;
- unusually low hallucination rate among leading models, but lower factual answer accuracy than Astra.

Interpretation:

> Argon may be more willing to abstain rather than confidently guess.

That could be valuable for research/review, but it is not the same thing as knowing more.

### Community consensus

There is no mature quality consensus yet.

The strongest repeated user reaction is simply:

> **"Why can't we access it?"**

Users criticize the restricted Fairwind/Ultra rollout and are skeptical of launch benchmarks until normal developers can test it.

Limited first-impression discussion is mixed: impressive demos, but some users see agent/coding behavior closer to GPT-6.1 Sol/Sonnet 5.5 than a runaway new leader.

### Routing prior

**Watchlist only.**

Do not make Argon a default until real access and real-user evidence exist.

When accessible, priority owner tests:

1. Argon vs GPT-6.1 Sol on long-horizon coding.
2. Argon vs Opus/Sonnet 5.5 on terminal/agent work.
3. Argon vs Astra on research where hallucination avoidance matters.
4. Argon on multimodal long-context tasks.

## Gemini 3.8 Flash

Remains the generally available Google worker baseline.

Its role is unchanged:

- fast multimodal execution;
- cheap coding worker;
- debugging/second opinion;
- high-volume processing with supervision.

Argon does not obsolete 3.8 Flash until Argon is actually broadly accessible and its economics/quality are validated.
