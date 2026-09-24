# Benchmark and Public-Prior Sources

_Last reviewed: 2026-09-24_

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

## Current OpenAI benchmark and field-guide sources

### Artificial Analysis — GPT-6 Astra release

https://artificialanalysis.ai/models/releases/gpt-6-astra

- **Type:** independent benchmark
- **Why useful:** effort-by-effort intelligence, speed and cost; exposes Astra's diminishing returns from High to Max.

### Artificial Analysis — GPT-6 Sol release

https://artificialanalysis.ai/models/releases/gpt-6-sol

- **Type:** independent benchmark
- **Why useful:** effort-by-effort intelligence and task-cost baseline for the new Sol tier.

### Artificial Analysis — GPT-6 Luna release

https://artificialanalysis.ai/models/releases/gpt-6-luna

- **Type:** independent benchmark
- **Why useful:** effort-by-effort intelligence and task-cost baseline for the high-volume tier.

### Artificial Analysis — GPT-6 Sol/Luna vs GPT-5.6

https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier

- **Date:** 2026-09-22
- **Type:** independent benchmark analysis
- **Why useful:** shows that lower GPT-6 task cost is primarily price-driven; both new models used slightly more output tokens than their predecessors. Also records coding-agent gains/regressions, hallucination behavior, and knowledge-work regressions.

### OpenAI — GPT-6 model catalog

https://developers.openai.com/api/docs/models

- **Type:** provider documentation
- **Why useful:** current flagship routing, exact model IDs, prices, context, reasoning options, and tools.

### OpenAI — GPT-6 Sol and Luna launch

https://openai.com/index/introducing-gpt-6-sol-and-luna/

- **Date:** 2026-09-22
- **Type:** provider self-report
- **Why useful:** launch pricing, official role split, provider coding/computer-use evaluations, availability, and caching changes.
- **Caution:** provider evaluation claims remain provider self-reports.

### OpenAI — GPT-6 caching

https://openai.com/index/better-prompt-caching-for-gpt-6/

- **Type:** provider engineering documentation
- **Why useful:** explains why persistent-agent context economics can differ from raw input-token totals.

### Reddit — GPT-6 Astra quota and role fit

https://www.reddit.com/r/ChatGPTPro/comments/1w8rqbt/gpt6_astra_usage/

https://www.reddit.com/r/ChatGPTPro/comments/1w9isu9/gpt6_astra_is_not_a_model_for_plus_users/

https://www.reddit.com/r/ChatGPTPro/comments/1wbs9cq/what_is_everyones_opinion_on_chatgpt6_astra_so_far/

- **Observed theme:** powerful end-to-end/research model with exceptionally strong quota-burn complaints.
- **Caution:** self-selected subscription users.

### Reddit — GPT-6 Sol early field reports

https://www.reddit.com/r/codex/comments/1wnto0j/sol_6_is_a_slop_fest/

https://www.reddit.com/r/codex/comments/1woiw95/something_is_wrong_with_gpt_6_sol/

https://www.reddit.com/r/codex/comments/1woa9fk/codex_usage_feels_brutally_much_better/

https://www.reddit.com/r/codex/comments/1woc006/new_model_drops_users_declare_it_sucks_within_37/

- **Observed theme:** major usage/value enthusiasm coexists with unusually strong early complaints about coding consistency and under-execution.
- **Caution:** only about two days of public history; launch-day backlash/honeymoon effects are substantial.

### Reddit — GPT-6 Luna early field reports

https://www.reddit.com/r/codex/comments/1wo11fj/gpt6_luna_review_after_3_hours_coding_on_a_big/

https://www.reddit.com/r/codex/comments/1wnmhnq/gpt56_luna_fans_how_does_gpt6_luna_feel_so_far/

https://www.reddit.com/r/codex/comments/1wox48m/luna_6_vs_luna_56/

- **Observed theme:** strongest enthusiasm is for bulk-worker economics; instruction-following and coding-quality reports are mixed.
- **Caution:** only about two days of public history.

### Reddit Devvit — r/codex Dexter

https://developers.reddit.com/apps/dexterthebot

- **Type:** concrete public application
- **Why useful:** GPT-6 Luna High is used for structured moderation decisions, with Luna also used for OCR/image description and human-review fallback.

## Current Anthropic benchmark and field-guide sources

### Artificial Analysis — Claude Opus 5.5 release

https://artificialanalysis.ai/models/releases/claude-opus-5-5

- **Date:** 2026-09-22
- **Type:** independent benchmark
- **Why useful:** effort-by-effort intelligence/task-cost curve; current frontier benchmark position; coding, automation, knowledge-work and token-use evidence.
- **Caution:** human evidence is still launch-week evidence.

### Artificial Analysis — Claude Fable 5.1 release

https://artificialanalysis.ai/models/releases/claude-fable-5-1

- **Type:** independent benchmark
- **Why useful:** exposes Fable's effort curve and the XHigh-vs-Max diminishing-return result.
- **Caution:** evaluated with Anthropic's default production fallback; not a perfectly isolated base-model measurement.

### Artificial Analysis — Claude Sonnet 5 release

https://artificialanalysis.ai/models/releases/claude-sonnet-5

- **Type:** independent benchmark
- **Why useful:** documents Sonnet's large token/task-cost growth with effort.

### Artificial Analysis — Claude Opus 5 release

https://artificialanalysis.ai/models/releases/claude-opus-5

- **Type:** independent benchmark
- **Why useful:** useful benchmark counterpoint to unusually negative real-user sentiment.

### Artificial Analysis — Claude Haiku 4.5

https://artificialanalysis.ai/models/claude-4-5-haiku-reasoning

- **Type:** independent benchmark
- **Why useful:** current cheap-tier capability/speed/cost baseline.

### Artificial Analysis — Claude Opus 4.8

https://artificialanalysis.ai/models/claude-opus-4-8

- **Type:** independent historical/current-performance reference
- **Why useful:** documents the older model's benchmark/cost profile while community and owner evidence preserve its behavioral value.

### Anthropic — Claude Opus 5.5

https://www.anthropic.com/claude-opus-5-5

- **Date:** 2026-09-22
- **Type:** provider self-report
- **Why useful:** price cuts, cache economics, communication goals, availability, and upcoming Sonnet/Haiku 5.5.
- **Caution:** provider benchmark claims remain provider self-reports.

### Anthropic — Claude Fable 5.1 / Mythos 5.1

https://www.anthropic.com/claude-fable-and-mythos-5-1

https://www.anthropic.com/claude/fable

- **Type:** provider documentation
- **Why useful:** pricing, cache discounts, access model, and trusted-access distinction.

### Anthropic — Claude Sonnet 5

https://www.anthropic.com/news/claude-sonnet-5

- **Type:** provider documentation
- **Why useful:** current permanent $2/$10 pricing, tokenizer caveat, and agentic positioning.

### Anthropic — Claude Opus 4.8

https://www.anthropic.com/news/claude-opus-4-8

- **Type:** provider documentation
- **Why useful:** price/context and intended agentic-collaboration behavior.

### Anthropic — model deprecations/status

https://docs.anthropic.com/en/docs/about-claude/model-deprecations

- **Type:** provider documentation
- **Why useful:** distinguishes active legacy models from retired models.

### Reddit — Opus 5.5 launch field reports

https://www.reddit.com/r/ClaudeAI/comments/1wnil7n/opus_55_in_claude_code_is_crazy_fast_especially/

https://www.reddit.com/r/Anthropic/comments/1wnl3k8/opus_55_first_impressions/

https://www.reddit.com/r/ClaudeAI/comments/1wo9lbs/opus_55_is_the_new_46/

- **Observed theme:** unusually positive speed, communication, UI/debugging and coding signal.
- **Caution:** only about two days of public use; honeymoon bias is substantial.

### Reddit — Fable 5.1 field reports

https://www.reddit.com/r/ClaudeAI/comments/1w5ai3j/fable_51_is_insane_and_it_burned_usage_which_is/

https://www.reddit.com/r/ClaudeAI/comments/1w5pnji/fable_5_vs_fable_51_across_22022_of_my_own_api/

- **Observed theme:** very strong capability/planning praise paired with severe quota complaints; cache discounts can reduce API dollars despite higher token counts.

### Reddit — Opus 5 sustained criticism

https://www.reddit.com/r/ClaudeCode/comments/1vbu4a7/opus_5_unreadable_jargon/

https://www.reddit.com/r/ClaudeCode/comments/1vwec8t/im_done_with_opus_5/

https://www.reddit.com/r/ClaudeCode/comments/1va445h/opus_5_feedback_megathread/

- **Observed theme:** mature complaints about verbosity, jargon, context drift, overreach and correction burden.
- **Caution:** negative-selection bias exists, but the theme persists across weeks and multiple high-engagement threads.

### Reddit — Sonnet 5 token economics

https://www.reddit.com/r/ClaudeAI/comments/1ukoszu/sonnet_5_is_a_token_monster/

https://www.reddit.com/r/ClaudeAI/comments/1uk0p07/opus_45_46_48_and_sonnet_5_token_data/

https://www.reddit.com/r/ClaudeAI/comments/1ukyy54/is_claude_sonnet_5_actually_worth_using_where_ive/

- **Observed theme:** good thoroughness and agentic work, but high/max effort can erase the apparent mid-tier price advantage.

### Reddit — Haiku 4.5 / mixed-tier workflows

https://www.reddit.com/r/ClaudeCode/comments/1r84b60/haiku_for_search_review_tasks/

https://www.reddit.com/r/ClaudeAI/comments/1oca664/haiku_45_is_really_really_good/

- **Observed theme:** useful search/read/classify/explore worker; users escalate to stronger models for reasoning/synthesis.

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
