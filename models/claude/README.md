# Claude

## Strongest observed role: governance and high-level judgment

The clearest direct model comparison came from The Bible Video Game skill/governance work.

In a multi-model bake-off, Claude's strongest response separated:

- **Sacred Event Protection Reviewer** — a gate/reviewer
- **authorship/content generation** — a different role

That distinction mattered because a protection role allowed to rewrite the content it was supposed to police would blur authority and increase the risk of silent semantic drift.

The same response prioritized Ancient Material Culture research separately and treated deterministic formatting as a script problem rather than an LLM problem.

## Model selection lesson

The project-level conclusion was not "Claude for everything."

The useful split was approximately:

- daily implementation/scaffolding: a cost-efficient capable model
- high-stakes governance/architecture: Claude high/Opus or GPT Sol high
- deterministic formatting/validation: code, not an LLM

This is a recurring principle throughout the corpus:

> Spend frontier reasoning on judgment that cannot be cheaply encoded as deterministic procedure.

## Prompting preference

The user repeatedly preferred concise prompts for Claude as well.

For Studio/MCP integration in Adventurer's Rise, the user rejected a verbose prompt and accepted a compact one centered on:

- adapters
- stable IDs
- no duplicate authority
- bounded playtest
- concise report

## Evidence limits

The full external Claude transcripts are not available in this corpus. Claude cases therefore correlate:

1. ChatGPT-authored task/prompt
2. repository artifact or PR
3. user reaction after the Claude run
4. later review results

See the Claude Code section for the strongest concrete implementation example.


## Current public model prior — 2026-09-24

Owner-observed Claude cases remain the primary evidence.

For current Anthropic model economics and Reddit consensus, use the [2026-09-24 Anthropic model field guide](../../research/anthropic/2026-09-24-reddit-field-guide.md) as a **public prior only**.

Current research hypothesis:

- **Opus 5.5 Medium/High:** new high-end daily Claude candidate;
- **Fable 5.1 High/XHigh:** scarce architecture/orchestration/review resource;
- **Opus 4.8:** proven behavioral fallback;
- **Sonnet 5 controlled effort:** bounded implementation/knowledge work;
- **Haiku 4.5:** search/read/classify/explore utility worker;
- **Opus 5:** avoid as normal author unless a specific workflow proves otherwise.

Do not rewrite historical Opus 4.8/Fable cases as conclusions about Opus 5.5.
