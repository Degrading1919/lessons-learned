
# Harness Efficiency Field Guide — Tokens, Context, and Five-Hour Windows

_Last researched: 2026-09-24_

## Purpose

Model choice is only one part of AI cost.

For agentic work, the harness determines what the model sees on every turn, which tools are advertised, when context is compacted, whether prompt caching survives, how many subagents are spawned, and whether a task consumes a subsidized subscription allowance or metered API dollars.

The useful question is:

> Which harness produces the most accepted work before a five-hour allowance, weekly allowance, or API budget is exhausted?

This guide separates four scarce resources:

1. subscription allowance;
2. API dollars;
3. wall-clock time;
4. human attention.

They are not interchangeable.

## Executive conclusions

### OpenAI subscription

For repository coding, Codex CLI is the current lean native-surface hypothesis.

Use Codex Desktop, IDE, or Work when its richer visual/desktop workflow materially helps the task. A small controlled community comparison found roughly 8,000–10,000 more startup context tokens on Desktop than CLI with matched model, effort, project instructions, skills, tools, and a no-tool control prompt. The sample was small and did not measure billing directly, so it should be reproduced rather than treated as a universal multiplier.

### Anthropic subscription

For repository coding, Claude Code CLI is the default native harness.

Claude Chat/Desktop and Claude Code share the same Pro/Max allowance. Claude Code is more autonomous and can consume more compute per human prompt, but Anthropic's own Economic Index shows it also completes similar work with far fewer human back-and-forth turns.

For writing, research, discussion, and analysis that do not need shell/file/tool loops, ordinary Claude Chat/Desktop avoids paying the autonomy/tool-loop tax.

### API harnesses

Cline, OpenCode, Cursor, and custom agents move cost into an API or separate usage pool unless a supported subscription connector is being used.

They are useful for:

- cross-provider routing;
- overflow after native limits;
- local/open models;
- explicit budgets;
- custom context/tool control.

They do not automatically make a native Claude or Codex five-hour window last longer.

### The largest harness lever is prompt caching

Anthropic's production data is unusually concrete:

- a naive multi-turn agent repeatedly resends its growing history, producing roughly quadratic uncached cost growth;
- real agent loops read a median about 84% of input from cache;
- the top 10% read 94% or more;
- below about 80%, Anthropic recommends investigating what is breaking the cache;
- prompt caching reduced measured agent-loop cost by 2.7–5.3x.

OpenAI documents the same core mechanism: exact stable prefixes, stable tools, append-only conversation history, and deferred tool discovery preserve cache reuse.

## 1. Why harnesses consume tokens

An agent request can include:

- provider instructions;
- harness instructions;
- repository instructions;
- skills;
- tool definitions;
- MCP schemas;
- prior messages;
- prior tool calls and results;
- current input.

Most of that may appear again on the next model call.

Anthropic explicitly notes that a 40-turn task sends its first turn 40 times. Without caching, cost grows roughly with the square of turn count.

OpenAI similarly emphasizes prompt caching because agent loops repeatedly send prior instructions, tool definitions, history, and results.

Sources:

- https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
- https://developers.openai.com/api/docs/guides/prompt-caching
- https://openai.com/index/unrolling-the-codex-agent-loop/

## 2. Subscription windows are not transparent token buckets

### OpenAI

Work and Codex share the applicable OpenAI agentic allowance. Usage depends on model, effort, inputs and outputs, speed mode, tools, and task complexity.

The five-hour percentage should be treated as provider accounting, not a transparent conversion from visible tokens.

Use the provider usage UI and Codex status command as the authoritative meter.

### Anthropic

Claude Chat/Desktop and Claude Code share Pro/Max subscription limits.

Anthropic's current help guidance gives approximate five-hour ranges such as:

- Pro: around 45 ordinary Claude messages or 10–40 Claude Code prompts;
- Max 5x: around 225 ordinary messages or 50–200 Code prompts;
- Max 20x: around 900 ordinary messages or 200–800 Code prompts.

Actual use varies with conversation length, attachments, repository size, model, and agent behavior.

A Code prompt can perform many internal model/tool turns, so prompts are not equivalent to completed tasks.

Sources:

- https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan
- https://www.anthropic.com/news/higher-limits-spacex

## 3. Codex CLI

### Strengths

- native subscription path;
- lean terminal surface;
- direct repository/shell access;
- first-party context and caching behavior;
- allowance visibility;
- easy task/session boundaries.

OpenAI recommends stable prompt prefixes, stable tool schemas, append-only history, deferred tool discovery, and explicit accounting for root-agent and subagent usage.

### Small controlled Desktop-vs-CLI comparison

An OpenAI Developer Community user collected 18 fresh-session readings: three per model per surface at Medium effort.

Their no-tool control prompt was equivalent to:

> Reply exactly OK. Do not inspect files or use tools.

Reported mean context:

| Model | Desktop | CLI | Desktop minus CLI |
|---|---:|---:|---:|
| Astra | about 29.5k | about 19.7k | about +9.8k |
| Sol | about 30.9k | about 22.8k | about +8.1k |
| Luna | about 28.8k | about 19.3k | about +9.5k |

Cautions:

- three readings per group;
- CLI percentage displays did not reconcile perfectly with token counts;
- context tokens are not the same as quota billing;
- answer quality was not measured.

Conclusion:

**Codex CLI should be our first efficiency baseline, not a declared universal winner.**

## 4. Codex Desktop / IDE / Work

Richer surfaces can improve:

- visual diffs;
- artifacts;
- desktop interaction;
- project/tool discovery;
- human workflow.

They can also introduce more fixed context through:

- UI/system instructions;
- integrations;
- plugins;
- skills;
- MCP tools;
- broader environment metadata.

Use them when the human-time savings or unique capabilities justify the context overhead.

## 5. OpenAI tools, plugins, MCPs, and subagents

OpenAI warns that tools, skills, plugins, MCPs, and accumulated history can bloat context.

Prompt cache reuse can be affected by changes to:

- tool names;
- descriptions;
- schemas;
- tool ordering;
- reasoning effort;
- verbosity;
- compaction state.

Tool search and deferred loading let a harness avoid advertising every tool on every request.

Subagents create their own model calls and usage. OpenAI's Agents API observability explicitly instructs developers to count root-agent work, subagent work, and retries.

Baseline rule:

> Keep the always-visible tool surface small and use multiagent fanout only when parallelism has a real payoff.

Sources:

- https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/
- https://developers.openai.com/api/docs/guides/prompt-caching
- https://developers.openai.com/api/docs/guides/tools-tool-search
- https://developers.openai.com/api/docs/guides/agents-api/observability

## 6. Claude Code CLI

Claude Code is Anthropic's strongest public prior for repository work.

Anthropic's Economic Index found Claude Code more autonomous than Chat/Cowork across most output categories. The mean gap was about 0.37 points on a five-point autonomy scale, and even the same Sonnet model remained about 0.26 points more autonomous in Code.

For blog/article work, the median Chat/Cowork workflow involved 13 human back-and-forth rounds while the median Claude Code workflow involved one human prompt.

Anthropic also found autonomy and token use positively correlated.

Meaning:

**Claude Code may spend more compute per prompt while completing more work per human interaction.**

Source:

- https://www.anthropic.com/research/economic-index-june-2026-report

## 7. Claude caching

Anthropic says prompt caching is its largest cost lever.

Across real agent traffic:

- median cache-read share was about 84%;
- top 10% exceeded about 94%;
- below roughly 80% should trigger investigation.

Measured agent-loop cost reductions were 2.7–5.3x.

Cache-breaking changes include:

- system-prompt edits;
- changing or reordering tools;
- incompatible effort/thinking changes;
- output-format changes;
- frequent context editing/compaction.

One dynamic line placed before the stable prefix can turn a cheap cache read into a full cache write.

Source:

- https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence

## 8. Claude tool/MCP overhead

Anthropic measured a triage agent with up to 502 tool definitions.

With all tools eagerly loaded, run cost rose from roughly $0.55 to $1.02.

With deferred tool search, cost remained around $0.56.

Anthropic also reports programmatic tool calling reducing input tokens by about 24% on an agentic search benchmark while improving performance, because intermediate tool chatter stayed outside the main model history.

Sources:

- https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context

## 9. Claude Chat/Desktop and Cowork

Use ordinary Claude Chat/Desktop for work that does not need a coding-agent loop:

- writing;
- research synthesis;
- discussion;
- analysis;
- pasted-document review.

Claude Code and Chat/Desktop share the allowance, so the distinction is about useful work per quota and human effort.

Cowork is useful when desktop/app/file interaction is the task. Public controlled quota comparisons against Claude Code are currently insufficient, so it should be chosen for capability rather than presumed efficiency.

## 10. Anthropic harness implementation can change apparent model quality

Anthropic published a 2026 postmortem where a Claude Code prompt-cache handling change incorrectly cleared thinking history every turn. The underlying API/inference service was not the problem.

This is important evidence that:

> apparent model degradation can actually be a harness/cache/context bug.

Source:

- https://www.anthropic.com/engineering/april-23-postmortem

## 11. Cline

Cline normally uses provider/API billing rather than the user's native Claude or ChatGPT five-hour subscription pool.

Cline documents that a task accumulates:

- conversation history;
- file content;
- command output;
- tool results;
- system/rule content.

It recommends focused tasks and says a .clineignore file can dramatically reduce baseline token usage.

Source:

- https://docs.cline.bot/core-workflows/task-management

### Why the exact provider route matters

Recent Cline issues document cases where:

- OpenAI-compatible/LiteLLM routes to Anthropic did not emit Anthropic cache controls;
- Bedrock prompt caching did not engage through a particular adapter;
- compaction authentication failure created reread/compaction loops.

These are route/version-specific bugs, not a claim that Cline is generally broken.

They demonstrate that:

**the same model can become dramatically more expensive through a harness/provider adapter that breaks caching.**

For Claude through Cline, prefer a direct Anthropic API route unless an alternative route's cache behavior has been verified.

## 12. OpenCode

OpenCode supports many providers and local models.

Its current provider documentation offers ChatGPT Plus/Pro authentication for OpenAI.

It explicitly states that Anthropic prohibits using Claude Pro/Max consumer subscriptions through third-party plugins; those bundled plugins were removed.

Source:

- https://opencode.ai/docs/providers

OpenCode also exposes explicit automatic/provider-native compaction controls.

Sources:

- https://opencode.ai/v2/docs/compaction
- https://opencode.ai/v2/docs/config

Baseline:

- useful for cross-provider routing, local models, and overflow;
- A/B against Codex before assuming ChatGPT subscription quota efficiency;
- use authorized API access for Anthropic.

## 13. Cursor

Cursor currently uses monthly usage pools.

Third-party models are charged against the Other Models pool at model API pricing.

Cursor first-party models such as Composer/Grok use a separate pool.

Current docs say:

- Pro: $20/month;
- Pro Plus: $60/month;
- Ultra: $200/month;
- daily Agent users often consume $60–$100/month total usage;
- power users often consume $200+/month.

BYOK on individual plans causes the provider to bill the model directly and does not consume Cursor's included model pool.

Sources:

- https://cursor.com/docs/models-and-pricing
- https://prod.cursor.com/help/models-and-usage/usage-limits
- https://prod.cursor.com/help/models-and-usage/api-keys

Conclusion:

**Cursor is attractive for its IDE and first-party/subsidized models, not as the obvious way to stretch a separate Claude/OpenAI five-hour subscription.**

## 14. Native subscription vs API harness

Heavy subscription users can receive much more inference value than the monthly subscription price would buy at list API rates.

Community measurements show this can be a very large subsidy, although the exact multiplier varies by user, model, time period, and workload.

A recent Claude user reported $7,470 in API-equivalent usage during a $200 subscription month. That is anecdotal and should not be generalized, but it demonstrates why heavy native use can be economically compelling.

The robust rule is:

> If a native subscription already provides the premium model and the native harness performs well, consume the appropriate subsidized allowance before paying list API rates for the same model.

API harnesses still win when flexibility, model routing, local models, observability, or custom optimization materially improve accepted-task economics.

## 15. Compaction

Compaction can:

- reduce active context;
- prevent overflow;
- lower future input size.

It can also:

- cost a summarization call;
- break a cached prefix;
- lose details;
- trigger file rereads;
- cause pathological reread/compact loops if implemented badly.

OpenAI explicitly notes that compaction can reduce prompt-cache reuse.

Anthropic measures the cost of re-caching after context changes.

Therefore:

**judge compaction by net completed-task cost, not by the smaller visible context alone.**

## 16. Fresh sessions vs long sessions

Continue a session when:

- the goal is the same;
- repository decisions remain relevant;
- cache reuse is healthy;
- the agent remains on track.

Start fresh when:

- the feature/goal changes;
- irrelevant history dominates;
- stale assumptions keep resurfacing;
- compaction/reread loops start;
- a different tool/model/authority surface is required.

The correct boundary is the task, not an arbitrary turn count.

## 17. Recommended owner stack

### OpenAI coding

Default:

**Codex CLI**

Routing:

- GPT-6 Sol Medium/High for serious implementation;
- GPT-6 Luna High/XHigh for clear worker tasks;
- Astra Medium/High for architecture, blockers, and final review.

Configuration:

- minimal always-on MCPs;
- deferred tools/skills;
- narrow subagent fanout;
- cheap subagent models/efforts;
- record five-hour percentage before and after meaningful tasks.

### Anthropic coding

Default:

**Claude Code CLI**

Routing:

- Opus 5.5 Medium/High for serious daily work;
- Opus 4.8 as known-behavior fallback;
- Fable High/XHigh for architecture/review;
- Haiku for search/read/classify;
- Sonnet at controlled effort for bounded implementation.

Configuration:

- stable instructions and tool definitions;
- deferred tool loading;
- tightly scoped subagents;
- cache-read monitoring where visible;
- investigate sustained cache-read rates below about 80%.

### Non-agentic Claude work

Use Claude Chat/Desktop for research, writing, discussion, and document analysis that does not need shell/files/autonomous verification.

### Overflow and provider routing

Use Cline/OpenCode for:

- API overflow;
- cheaper workers;
- local/open models;
- provider flexibility.

Verify caching on the exact provider route.

### Cursor

Use when the IDE and Cursor's first-party models justify the subscription.

Do not buy it primarily to obtain additional premium Claude/OpenAI allowance.

## 18. What to optimize

Do not optimize:

> tokens per request

Optimize:

> accepted work per scarce resource

Track:

- five-hour percentage;
- weekly percentage;
- API dollars;
- wall time;
- human corrections;
- first-pass acceptance;
- cache reads;
- tool calls;
- subagents;
- compactions;
- later regressions.

The Harness A/B Test Protocol in this repository defines the controlled measurements.

## Source registry

### OpenAI

- https://developers.openai.com/api/docs/guides/prompt-caching
- https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics
- https://developers.openai.com/api/docs/guides/agents-api/observability
- https://developers.openai.com/api/docs/guides/tools-tool-search
- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/
- OpenAI Help: Using Codex with your ChatGPT plan
- OpenAI Help: Managing usage with GPT-6 Astra in Work and Codex

### Anthropic

- https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context
- https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan
- https://www.anthropic.com/news/higher-limits-spacex
- https://www.anthropic.com/research/economic-index-june-2026-report
- https://www.anthropic.com/engineering/april-23-postmortem

### Cline

- https://docs.cline.bot/core-workflows/task-management
- https://github.com/cline/cline/issues/13667
- https://github.com/cline/cline/issues/12913
- https://github.com/cline/cline/issues/14328

### OpenCode

- https://opencode.ai/docs/providers
- https://opencode.ai/v2/docs/compaction
- https://opencode.ai/v2/docs/config

### Cursor

- https://cursor.com/docs/models-and-pricing
- https://prod.cursor.com/help/models-and-usage/usage-limits
- https://prod.cursor.com/help/models-and-usage/api-keys
