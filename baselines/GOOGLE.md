# Google / Gemini Baseline

_Last researched: 2026-09-22_

## Current routing summary

| Model | Baseline role | Strong suits | Main weaknesses / cautions |
|---|---|---|---|
| Gemini 3.8 Flash | Fast, inexpensive multimodal worker / coding executor | Excellent DeepSWE result, very high throughput, 1M context, broad multimodal/tool support, strong finance/legal benchmark results | General intelligence trails frontier flagships; community reports instruction drift, shortcuts, context issues, and weaker browser/execution harness behavior |
| Gemini Pro line | No stable current baseline | Historically intended as Google's higher-capability tier | 3.5 Pro was delayed; do not assume unreleased/future Pro performance from Flash results |

## Gemini 3.8 Flash

### Independent benchmark signal

Current Artificial Analysis v4.3 reports:

- High: Intelligence Index **41**
- Medium: 40
- Low: 34
- High throughput roughly 260–330 output t/s depending measurement point
- High estimated cost per Intelligence Index task around $1.24

This is strong but materially below the current 53-point Astra/Fable frontier on broad intelligence.

Source:

- https://artificialanalysis.ai/models/releases/gemini-3-8-flash

### Provider signal

Google's model card shows unusually strong task-specific results for a Flash model:

- DeepSWE v1.1: **73.7%**
- Claude Opus 5 on the same table: 74.0%
- GPT-5.6 Sol: 72.7%
- GPT-5.6 Terra: 69.6%
- Finance Agent v2: 61.4%
- Harvey Legal Agent all-pass: 10.0%

It has:

- 1,048,576 input context
- 65,536 output limit
- text/image/video/audio/PDF input
- code execution
- computer use preview
- function calling
- search/Maps grounding
- structured outputs
- low/medium/high thinking

Sources:

- https://deepmind.google/models/model-cards/gemini-3-8-flash/
- https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash

### Human-review signal

Community opinion is sharply split between **"astonishing value"** and **"fast but needs supervision."**

Positive themes:

- very fast;
- strong frontend/design and debugging examples;
- good enough to pair with an expensive planner/reviewer;
- surprisingly strong large-codebase exploration;
- excellent subscription/API value.

Negative themes:

- ignores parts of long prompts;
- can take shortcuts or drift from rules;
- some users report hallucination, context loss, or dangerous repository edits;
- Antigravity/browser integration can be weaker than Codex/Claude Code even when the underlying answer quality is good;
- speed makes a wrong direction dangerous because the model can modify a lot quickly.

Representative threads:

- https://www.reddit.com/r/GeminiAI/comments/1wjmz5x/actually_gemini_38_flash_is_a_beast/
- https://www.reddit.com/r/opencode/comments/1w5yi10/gemini_38_flash_is_actually_quite_good/
- https://www.reddit.com/r/codex/comments/1w9t5ge/luna_max_vs_gemini_38_flash_high_which_one_is/
- https://www.reddit.com/r/GoogleGemini/comments/1w6yo7t/whats_your_coding_workflow_using_gemini_38_flash/
- https://www.reddit.com/r/Bard/comments/1wflr28/gemini38flash_is_pretty_good/

### Baseline prior

Strong candidate for:

- inexpensive implementation from a well-defined plan;
- multimodal analysis;
- debugging as a second opinion;
- high-volume code generation with review;
- finance/legal workflows where the task-specific benchmark profile is relevant.

Do **not** make it an unsupervised primary on a valuable repository until personal evidence establishes that its rule-following and cleanup behavior are reliable in the chosen harness.

A promising routing pattern from community reports is:

> Astra/Fable/Opus/Sol plans or reviews → Gemini 3.8 Flash executes.

---

## Current Pro-tier caveat

At Google I/O 2026, Google said Gemini 3.5 Pro was expected the following month. By July, Google instead said it remained in partner testing and would be broadly available "as soon as it's ready."

Sources:

- https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/

As of this baseline, do not invent a Gemini 3.5/4 Pro routing recommendation from unreleased performance.

The current public evidence supports evaluating **3.8 Flash on its own merits** rather than assuming it predicts the next Pro model.
