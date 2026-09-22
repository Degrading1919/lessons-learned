# Benchmark and Public-Prior Sources

_Last reviewed: 2026-09-22_

These sources are used only to establish public priors and context. They do not override the project owner's direct evidence.

## Coding-agent benchmarks

### Artificial Analysis — Coding Agent Index methodology

https://artificialanalysis.ai/methodology/coding-agents-benchmarking

- **Type:** independent benchmark organization
- **Why useful:** evaluates model + agent harness combinations on long-horizon software engineering, terminal use, and repository Q&A; reports cost, tokens, and wall time.
- **Caution:** benchmark versions change. Preserve the version/date with any numeric claim.

### Artificial Analysis — GPT-5.6 launch analysis

https://artificialanalysis.ai/articles/gpt-5-6-has-landed

- **Date:** 2026-07-09
- **Type:** independent prerelease evaluation
- **Why useful:** historical public prior for Sol, Terra, and Luna near the time of several personal cases.
- **Caution:** uses an older Coding Agent Index version than the current September 2026 index.

### Artificial Analysis — current coding-agent leaderboard

https://artificialanalysis.ai/agents/coding-agents

- **Type:** independent benchmark
- **Why useful:** current comparison across native coding-agent harnesses.

### Artificial Analysis — Claude Code vs Codex

https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-codex

- **Type:** independent comparative benchmark
- **Why useful:** explicitly demonstrates that the harness is part of the evaluated system.

## Provider sources

### OpenAI — GPT-5.6

https://openai.com/index/gpt-5-6/

- **Type:** provider self-report
- **Why useful:** launch-era model/eval claims, pricing, and model-family positioning.
- **Caution:** do not present provider benchmark claims as independent validation.

### OpenAI — Harness engineering

https://openai.com/index/harness-engineering/

- **Type:** provider engineering report
- **Why useful:** repository-native agent workflow; explicitly argues for a short AGENTS.md as a map and structured repository documentation as the system of record.

### OpenAI — How OpenAI uses Codex

https://openai.com/business/guides-and-resources/how-openai-uses-codex/

- **Type:** provider workflow guidance
- **Why useful:** task shaping, AGENTS.md, development environment, and verification practices.

### Anthropic — Effective context engineering for AI agents

https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

- **Type:** provider engineering guidance
- **Why useful:** just-in-time context retrieval, Claude Code environment navigation, and autonomy/task-shape guidance.

### Anthropic — Claude Code Foundations

https://www.anthropic.com/webinars/claude-code-foundations

- **Type:** provider workflow guidance
- **Why useful:** CLAUDE.md, MCP, subagents, and model-role routing.

### Anthropic — Claude Opus 5

https://www.anthropic.com/news/claude-opus-5

- **Date:** 2026-07-24
- **Type:** provider self-report
- **Why useful:** documents the generational change from Opus 4.8 and demonstrates why historical model labels must not be treated as current rankings.

## Tripo

### Tripo — text-to-3D developer documentation

https://developers.tripo3d.ai/en/docs/generation-text-to-model/standard

- **Type:** official product documentation
- **Why useful:** current face limits, quad output, smart-low-poly behavior, output orientation, and generation constraints.

### Tripo — retopology

https://developers.tripo3d.ai/en/docs/mesh-decimate

- **Type:** official product documentation
- **Why useful:** current automated retopology capabilities.

### Tripo — game-production pipeline

https://www.tripo3d.ai/blog/ai-3d-asset-pipeline-for-game-studios

- **Type:** provider production guidance / marketing
- **Why useful:** even Tripo's own production guidance treats generation as one stage in a pipeline with cleanup, QA, and engine validation.
- **Caution:** marketing claims require independent project validation.

## Community-sentiment examples

Community sources are used only to identify recurring workflow complaints or praise.

### GPT-5.6 quota/quality discussion

https://www.reddit.com/r/codex/comments/1v5norf/gpt56_in_codex_may_have_the_same_token_pricing/

https://www.reddit.com/r/codex/comments/1uue8ad/so_what_do_we_think_of_gpt_56/

- **Observed theme:** strong results paired with frequent complaints about quota consumption.
- **Caution:** anecdotal, self-selected users.

### Terra cautionary report

https://www.reddit.com/r/codex/comments/1ut3u5l/very_bad_first_experience_with_gpt_56_terra/

- **Observed theme:** individual reports include serious implementation mistakes.
- **Caution:** one anecdote; do not generalize.

### Tripo production/cleanup discussion

https://www.reddit.com/r/Tripo_ai/comments/1win6lm/tried_a_full_ai_3d_workflow_from_high_poly_to/

https://www.reddit.com/r/TopologyAI/comments/1vulukn/tripo_p20_is_so_insanely_op_that_it_blew_my_mind/

- **Observed theme:** topology quality has improved, but cleanup/production review remains normal.
- **Caution:** community showcases are not controlled benchmarks.

## Use rule

When a future agent writes a public-prior comparison:

1. record the exact source;
2. record date/version;
3. label provider self-report vs independent benchmark vs community anecdote;
4. compare only sufficiently similar model/harness/task conditions;
5. state whether the personal case confirms, contradicts, adds operational nuance, or is not comparable.
