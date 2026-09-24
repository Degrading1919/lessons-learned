
# Harness Baseline

_Last researched: 2026-09-24_

See the full [Harness Efficiency Field Guide](../research/harnesses/2026-09-24-token-and-window-efficiency.md).

## Core conclusion

**Harness efficiency can matter as much as model choice.**

The main cost mechanisms are:

1. repeated history/context;
2. prompt-cache hit rate;
3. tool/MCP schema size;
4. tool-result accumulation;
5. subagent fanout;
6. compaction behavior;
7. reasoning effort;
8. retries/rework;
9. native subscription subsidy versus API billing.

## Current baseline

| Harness | Billing / allowance | Best role | Efficiency prior |
|---|---|---|---|
| Codex CLI | Shared OpenAI Work/Codex allowance | OpenAI repository coding | Current lean native-surface hypothesis |
| Codex Desktop/IDE/Work | Same OpenAI allowance | Rich visual/desktop workflow | Use when UX/tools justify extra context |
| Claude Code CLI | Shared Claude Pro/Max allowance | Anthropic repository coding | Default native Claude coding harness |
| Claude Chat/Desktop | Same Claude allowance | Non-agentic writing/research | Avoids unnecessary coding-agent loop |
| Claude Cowork | Same Claude allowance | Desktop/app agent work | Capability-driven; quota advantage unproven |
| Cline | Usually API/PAYG | Cross-provider/local/overflow | Efficient only when provider route caches correctly |
| OpenCode | ChatGPT connector or API/local | Cross-provider terminal routing | A/B against Codex before assuming quota benefit |
| Cursor | Monthly Cursor pools/BYOK | IDE + Cursor first-party models | Premium third-party models use API-style accounting |
| Custom API agent | PAYG | Maximum control | Potentially efficient if caching/tools are engineered well |

## Hard evidence

Anthropic measured:

- median agent-loop cache reads around 84% of input;
- top 10% around 94%+;
- <80% as a reason to inspect cache behavior;
- prompt caching cutting measured agent-loop cost 2.7–5.3x.

Anthropic also measured eager loading of hundreds of tools raising a run from roughly $0.55 to $1.02, while deferred tool search held it near $0.56.

OpenAI documents the same major levers: stable prompt prefixes, stable tools, deferred tool search, subagent accounting, and compaction-aware caching.

A small controlled community test found Codex Desktop starting roughly 8k–10k context tokens above CLI across Astra, Sol, and Luna. Treat this as a hypothesis to reproduce, not a billing fact.

## Owner-oriented recommendation

### OpenAI coding

- Codex CLI first.
- Minimal MCP/plugin surface.
- Sol Medium/High serious work.
- Luna High/XHigh worker tasks.
- Astra Medium/High architecture/blockers/review.
- Measure five-hour percentage before/after meaningful tasks.

### Anthropic coding

- Claude Code CLI first.
- Opus 5.5 Medium/High serious work.
- Opus 4.8 fallback.
- Fable High/XHigh architecture/review.
- Haiku search/read/classify.
- Controlled Sonnet for bounded work.
- Keep cache/tool behavior stable.

### API/overflow

Cline/OpenCode are flexibility and overflow tools, not presumed subscription optimizers.

For Cline + Claude, verify actual cache reads on the exact route.

### Cursor

Use when its IDE or first-party models provide enough value. Do not choose it mainly to obtain more OpenAI/Claude premium-model allowance.

## Measurement

Optimize:

> accepted work / scarce resource

Use the [Harness A/B Test Protocol](../research/harnesses/HARNESS_AB_TEST_PROTOCOL.md).
