# Cross-Model Routing Guide

This is a current routing heuristic derived from the user's own project evidence. It is not a permanent ranking.

## Route by bottleneck

| Task bottleneck | Current best-supported role |
|---|---|
| Product definition / task shaping | ChatGPT |
| Large end-to-end repo implementation with mature specs | Codex with a high-capability configuration when the integration burden justifies it |
| Routine bounded implementation | Codex with a cost-efficient capable configuration such as the observed Terra High workflow |
| Architecture/governance judgment | High-reasoning ChatGPT/Claude reviewer |
| Live Studio/Blender integration | Claude Code or another code agent with the relevant MCP/environment access |
| 3D base generation | Tripo 3D |
| Repeatable 3D cleanup/validation | Blender scripts/tools + human/agent review |
| Deterministic formatting/validation | Code/scripts, not an LLM |
| Final product acceptance | Human playtest/use |

## OpenAI public-prior overlay — 2026-09-24

This subsection is **research guidance, not owner-observed evidence**. See `research/openai/2026-09-24-reddit-field-guide.md`.

| Bottleneck | Current OpenAI prior | Confidence |
|---|---|---|
| Ambiguous architecture / difficult integration | GPT-6 Astra Medium/High | Medium-high |
| Serious daily coding / agentic work | GPT-6 Sol Medium/High | Provisional; launch-week behavior is contested |
| Bounded bulk implementation from a clear plan | GPT-6 Luna High/XHigh | Provisional; strongest cost-efficiency candidate |
| Known difficult engineering where GPT-6 Sol misbehaves | GPT-5.6 Sol | High as a behavioral fallback |
| Moderately ambiguous routine repo work | GPT-5.6 Terra High | High owner evidence; public API economics are weaker |
| Legacy cheap-worker behavior | GPT-5.6 Luna | High as a fallback, not the economic default |

Important:

- GPT-6 Sol/Luna are primarily **cost-efficiency** releases so far, not clean across-the-board quality wins over 5.6.
- Astra Max is not the default. Independent benchmarks show strong diminishing returns above Medium/High.
- Luna is cheap only when verification is cheap. Retry/reviewer cost can erase token savings.
- GPT-6 Sol/Luna had only about two days of public use when this overlay was written, so Reddit consensus remains provisional.
- Keep 5.6 models routable until matched owner tests demonstrate that the GPT-6 replacement is behaviorally better on the relevant workflow.

## Anthropic public-prior overlay — 2026-09-24

This subsection is **research guidance, not owner-observed evidence**. See `research/anthropic/2026-09-24-reddit-field-guide.md`.

| Bottleneck | Current Anthropic prior | Confidence |
|---|---|---|
| Serious daily Claude Code | Opus 5.5 Medium/High | Provisional; very strong launch signal |
| Architecture / orchestration | Fable 5.1 High/XHigh or Opus 5.5 High | Medium-high |
| Known-behavior repo implementation | Opus 4.8 | High behavioral confidence |
| Bounded normal implementation | Sonnet 5 Low/Medium/High | High, with strict effort control |
| Search/read/classify/explore | Haiku 4.5 | High utility-role confidence |
| Adversarial QA | Opus 5 can have niche value | Medium; poor authoring prior |
| Restricted high-risk research | Mythos 5.1 / verified Opus access | Access-dependent |

Important:

- Opus 5.5 is currently the strongest public-prior Claude default, but it is only days old.
- Fable 5.1 is best treated as scarce judgment/review, not bulk implementation.
- Opus 5 is the strongest Claude waste-trap candidate because human correction/readability costs undermine its benchmark strength.
- Sonnet 5 is not automatically cheap; Max effort can cost more per finished benchmark task than older Opus.
- Haiku 4.5 is useful inside Claude Code for retrieval/exploration, but Anthropic currently lacks an obvious equivalent to GPT-6 Luna's modern low-cost worker economics.
- Opus 4.8 remains routable because mature human and owner evidence supports its practical judgment.

## The routing pattern that appears most efficient

### Build

Use a capable implementation model with:

- repository source of truth
- clear mission
- hard guardrails
- enough autonomy to finish

### Review

Use an independent strong reasoning model to inspect:

- architecture
- edge cases
- cross-system integration
- silent assumptions
- test gaps

### Correct

Send the implementer a **narrow correction task** grounded in specific review findings.

### Playtest

Use the product as a user.

Convert real friction into the next task.

This loop repeatedly appears more useful than trying to make one giant prompt eliminate all future defects.

## Do not route by prestige

The corpus contains multiple warnings against "always use the biggest model":

- Terra High produced strong bounded implementation at attractive cost.
- GPT-6 Luna is now the strongest public-prior worker candidate, but its launch-week instruction-following evidence is mixed.
- GPT-6 Astra effort selection matters: Medium/High captures most benchmark capability before Max-level cost.
- Astra Low appeared more economically useful in reviewer/orchestrator roles than as the owner of an enormous implementation wave.
- deterministic transformations should be scripts.
- Tripo is useful for raw geometry but cannot guarantee production readiness.
- live environment access can matter more than raw reasoning score.

## Prompt-size rule

If the repository already contains the details, the task prompt should usually get **shorter**, not longer.

A strong autonomous prompt typically needs:

- mission
- source of truth
- non-negotiable boundaries
- useful external references
- permission to use engineering judgment
- completion evidence standard

Detailed behavior should remain in durable project docs where every future agent can inspect it.

## When to use more prescriptive prompts

Prescriptive prompts are still useful when:

- fixing a known defect list
- performing a migration with exact invariants
- changing only a bounded surface
- preserving an approved architecture
- reviewing a specific PR
- executing a high-risk operation where freedom is undesirable

The Agentic AI lesson is not "always be vague." It is "match task freedom to task maturity."
