# Model Release Update — GPT-6.1 Sol, Claude Sonnet 5.5, and Gemini 4 Argon

_Last researched: 2026-10-04_

This update covers models released after the repository's September 24 baseline that materially change model-routing decisions.

## Included

- OpenAI GPT-6.1 Sol — released September 29, 2026
- Anthropic Claude Sonnet 5.5 — released September 28, 2026
- Google Gemini 4 Argon — announced September 30, 2026; restricted rollout

## Not promoted to current baselines

- Claude Haiku 5.5 — announced as coming in the following weeks, not released as of October 4.
- DeepSeek V4.1 Pro — anticipated/leaked but not officially released.
- OpenAI Astra Ultrafast — service tier, not a distinct model.
- Gemini 3.8 Live / Live Avatar — specialized realtime/audio/visual products rather than general coding/knowledge-work routing replacements.

The baseline rule remains: do not turn leaks, aliases, or service tiers into model records.

---

# Executive routing update

| Model | What changed | Current role prior | Main risk |
|---|---|---|---|
| **GPT-6.1 Sol** | Replaced GPT-6 Sol after 7 days; near-Astra independent benchmark result at dramatically lower task cost | OpenAI default serious engineering candidate | Slow throughput/latency; real Codex quality remains mixed |
| **Claude Sonnet 5.5** | Huge improvement over Sonnet 5; near-Opus performance in terminal/knowledge work | Well-scoped implementation / worker under Opus | Max effort is extraordinarily token-heavy |
| **Gemini 4 Argon** | Google returns to frontier tier; major agentic and reliability gains | Future frontier coding/knowledge/cyber candidate | Restricted access; almost no genuine public-user consensus yet |

---

# 1. GPT-6.1 Sol

## Provider position

OpenAI describes GPT-6.1 Sol as delivering near-Astra performance for complex coding, computer use, and professional work at lower cost.

Current API:

- input: $2 / 1M
- cached input: $0.10 / 1M
- output: $10 / 1M
- context: 1.05M
- max output: 128K
- reasoning: low / medium / high / xhigh / max
- tool support: web/file search, image generation, code interpreter, hosted shell, patching, skills, computer use, MCP, tool search
- multi-agent support: beta

Compared with GPT-6 Sol, list input/output price is unchanged but cached input falls from $0.20 to $0.10 per million.

Official sources:

- https://developers.openai.com/api/docs/models/gpt-6.1-sol
- https://developers.openai.com/api/docs/changelog
- https://deploymentsafety.openai.com/gpt-6-1-sol/respecting-auto-review

## Provider benchmark signal

OpenAI reports, among other comparisons:

- DeepSWE v1.1: GPT-6.1 Sol High 75.2%, above GPT-6 Sol's best reported 68.8%, at much lower task cost.
- OSWorld 2.0 offline: GPT-6.1 Sol Max 71.4% vs Astra 73.5%, at a fraction of Astra's cost.
- improved AutomationBench at matched effort.
- safety/HealthBench results much closer to Astra than GPT-6 Sol.

Provider results should remain labeled as provider self-reports.

## Independent benchmark signal

Artificial Analysis reports GPT-6.1 Sol Max at **52**, one point below Astra Max at 53.

At Max:

- cost per Intelligence Index task: about **$0.72**
- Astra Max: about $3.26
- GPT-6 Sol Max: about $1.05
- GPT-5.6 Sol Max: about $1.99

Artificial Analysis says every GPT-6.1 Sol effort setting extends the intelligence-vs-cost Pareto frontier.

Effort curve from current independent results:

| Effort | Intelligence Index | AA cost/task |
|---|---:|---:|
| Low | 42 | ~$0.13 |
| Medium | 48 | ~$0.21 |
| High | 50 | ~$0.32 |
| XHigh | 51 | ~$0.39 |
| Max | 52 | ~$0.72 |

High→Max adds only two broad-index points while more than doubling task cost.

A particularly interesting coding result: Artificial Analysis observed GPT-6.1 Sol XHigh outperforming Max on its Coding Agent Index, while costing far less than Astra.

Sources:

- https://artificialanalysis.ai/articles/gpt-6-1-sol-replaces-gpt-6-sol-after-just-7-days-with-near-astra-intelligence
- https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh/
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol

## Token efficiency

This is not simply a "uses fewer tokens" release.

Artificial Analysis reports GPT-6.1 Sol using roughly 10–30% **more output tokens** than GPT-6 Sol across effort settings, but producing enough more useful capability that low/medium settings are token-efficiency Pareto optimal.

Its cost advantage comes from:

- stronger results;
- cheaper cache reads;
- better task completion economics;

not simple token starvation.

## Speed is the major drawback

Independent measurements show GPT-6.1 Sol materially slower than GPT-6 Sol.

Example at High:

- GPT-6.1 Sol: ~48–50 output tokens/sec in current AA measurements
- GPT-6 Sol High: ~89 tokens/sec

XHigh also shows very long time-to-first-answer-token in independent measurements.

Reddit's strongest negative consensus is therefore **latency**, not price.

Several users describe it as "painfully slow" while simultaneously saying their five-hour/weekly allowance lasts dramatically longer.

OpenAI subsequently said the release faced unusually high demand and that additional capacity was being brought online, so launch-week speed should not be assumed permanent.

## Community consensus — positive

Repeated themes in r/codex:

- substantially better than GPT-6 Sol;
- feels like the actual successor to GPT-5.6 Sol;
- extremely good subscription-usage efficiency;
- strong backend / workhorse behavior;
- users can run it for hours where Astra would exhaust a window quickly;
- strong value on Plus/Pro when speed is tolerable.

Representative threads:

- https://www.reddit.com/r/codex/comments/1wtq7vg/gpt61_sol_is_very_good_for_the_plus_users/
- https://www.reddit.com/r/codex/comments/1wtyhlo/gpt_61_sol_is_so_good_its_actually_much_more/
- https://www.reddit.com/r/codex/comments/1wvg7rj/gpt61sol_is_a_really_good_work_model_right_now/
- https://www.reddit.com/r/codex/comments/1wtvwvl/are_you_guys_seeing_this/

## Community consensus — negative

Repeated counterthemes:

- very slow throughput;
- some tasks still under-execute prompts;
- frontend/UI output receives more criticism than backend work;
- individual reports of poor terminal/tool behavior;
- reports of fake/inadequate tests and excessive investigation;
- some experienced users still prefer Opus 5.5 or Sonnet 5.5 for first-pass quality.

Representative threads / issue:

- https://www.reddit.com/r/codex/comments/1wuatzt/gpt61_sol_feels_unlimited_because_it_runs_at_20/
- https://www.reddit.com/r/OpenaiCodex/comments/1wtrad9/gpt_61_sol_has_been_pretty_disappointing_that_i/
- https://www.reddit.com/r/codex/comments/1wuuc4e/gpt_61_sol_caught_faking_tests/
- https://github.com/openai/codex/issues/50121

The "fake tests" report is anecdotal and may involve harness behavior. It should be treated as a verification warning, not a general model verdict.

## Current routing prior

**GPT-6.1 Sol High is the strongest current OpenAI default candidate for serious daily engineering.**

XHigh is unusually attractive for hard coding/agent tasks because independent coding-agent results are strong and cost remains low.

Max should not be selected automatically.

Astra remains the stronger prior when:

- ambiguity is extreme;
- architecture/judgment is the bottleneck;
- the cost of a wrong global decision dominates inference cost.

For frontend/visual design, the community signal currently favors Opus/Sonnet 5.5 more strongly than GPT-6.1 Sol.

Confidence: **medium-high**, with speed/capacity still moving.

---

# 2. Claude Sonnet 5.5

## Provider position

Anthropic calls Sonnet 5.5 a clear upgrade over Sonnet 5 and a faster, lower-cost complement to Opus 5.5.

Target strengths:

- well-scoped everyday tasks;
- bug fixing;
- polished documents/slides/spreadsheets;
- design;
- fast iteration.

Anthropic says it runs 30%+ faster and costs up to 30% less for most work than Sonnet 5 despite identical token list prices.

Current pricing:

- cache read: $0.20 / 1M
- input: $2 / 1M
- output: $10 / 1M
- 1M context

In Claude Code, the `sonnet` alias now resolves to Sonnet 5.5 and defaults to **Medium** effort.

Sources:

- https://www.anthropic.com/claude-sonnet-5-5
- https://claude.dev/blog/building-with-claude-sonnet-5-5/

## Provider benchmark signal

Anthropic reports:

- Terminal-Bench 4.0: 70.6%, a massive improvement over Sonnet 5;
- GDPval-AA performance within roughly two points of Opus 5.5;
- strong long-horizon work and image understanding;
- improved behavioral audit results.

Provider benchmark claims remain provider self-reports.

## Independent benchmark signal

Artificial Analysis reports Sonnet 5.5 Max at **56**, currently just behind Opus 5.5 Max at 58.

Independent results include:

- Terminal-Bench 4.0: 64%, above Opus 5.5/Astra in that AA run;
- AA-Briefcase and GDPval-AA near Opus 5.5;
- AutomationBench-AA near/above Opus 5.5;
- lower factual/scientific strength than Opus 5.5.

Effort curve:

| Effort | Intelligence Index | AA cost/task |
|---|---:|---:|
| Low | 36 | ~$0.42 |
| Medium | 41 | ~$0.59 |
| High | 47 | ~$1.12 |
| XHigh | 52 | ~$2.75 |
| Max | 56 | ~$7.67 |

The economic warning is extreme:

**Sonnet 5.5 Max used about 193k output tokens per Intelligence Index task — the highest Artificial Analysis had measured — about 7x Astra Max.**

At Max, Sonnet 5.5's task cost is actually higher than Opus 5.5 Max despite being half the list token price.

Sources:

- https://artificialanalysis.ai/articles/claude-sonnet-5-5/
- https://artificialanalysis.ai/models/releases/claude-sonnet-5-5
- https://artificialanalysis.ai/models/claude-sonnet-5-5-xhigh
- https://artificialanalysis.ai/models/claude-sonnet-5-5-high/

## Community consensus — strongest positive

The clearest emerging coding workflow is:

> **Opus 5.5 plans/reviews → Sonnet 5.5 implements.**

Users point to Sonnet's strong Terminal-Bench result and half-price token rates versus Opus.

A particularly useful community A/B tested 10 real coding tasks × 3 runs/config at High effort in Claude Code and pi-agent:

- Sonnet 5.5 and Opus 5.5 both passed 30/30 in that sample;
- Sonnet completed Claude Code attempts in ~53s vs Opus ~108s;
- estimated API cost ~ $0.15 vs $0.36 per task;
- Sonnet 5.5 improved materially over Sonnet 5 in pass rate, turns, and output tokens.

This is still one user's workload, but it is stronger evidence than a vibe report because the task set and repeated runs are described.

Source:

- https://www.reddit.com/r/ClaudeAI/comments/1wsqp51/sonnet_55_vs_opus_55_vs_sonnet_5_in_claude_code/

Other repeated praise:

- very good bug fixing;
- strong UI/design/front-end output;
- much faster than Opus;
- clearer/less meandering than Sonnet 5;
- strong value for well-specified coding.

## Community counterevidence

The community is split on **where the economic crossover occurs**.

At low/medium/high effort Sonnet can be highly attractive.

At XHigh/Max, the model's enormous reasoning/output-token use can eliminate or reverse the apparent savings.

One high-engagement comparison of a 3D coding task reported Sonnet spawning far more agents and costing dramatically more than GPT-6.1 Sol for a similar-looking result. That comparison is heavily harness/fanout-confounded and should not be treated as a pure base-model benchmark, but it demonstrates the exact completed-task-cost risk this repository tracks.

Source:

- https://www.reddit.com/r/ClaudeAI/comments/1wu7ujz/sonnet_55_30x_more_expensive_than_gpt_61_sol_on/

Non-coding feedback also includes complaints that Sonnet 5.5 can feel cautious, hedgy, or less warm than Opus.

## Current routing prior

**Sonnet 5.5 Medium/High is now Anthropic's strongest implementation-worker prior.**

Use Opus 5.5 when:

- ambiguity/judgment dominates;
- architectural decisions are hard to verify;
- final review matters more than throughput.

Use Sonnet 5.5 when:

- the task is well-scoped;
- acceptance tests are strong;
- speed and task throughput matter;
- parallel worker execution is valuable.

Avoid reflexive Max.

Confidence: **medium-high**, with only one week of community history.

---

# 3. Gemini 4 Argon

## Availability warning

Gemini 4 Argon is not yet broadly available.

Google initially released it to trusted cyber defenders and selected testers through Fairwind and says broader rollout will begin with paid API customers and Google AI Ultra subscribers.

As a result, current Reddit discussion is mostly:

- benchmark reaction;
- access frustration;
- speculation.

It is **not** a mature real-user consensus.

This baseline should therefore remain low-confidence until meaningful public access exists.

## Provider position

Google positions Argon as its frontier model for:

- long-horizon coding;
- enterprise knowledge work;
- finance/legal;
- multimodal professional work;
- cybersecurity defense.

Specifications / launch economics:

- 1M context window;
- up to 1M output through Long Decode Continuation;
- text/image/video/speech input;
- introductory $2/M input, $10/M output;
- cached input 95% discounted;
- standard post-promotion pricing $4/M input, $20/M output.

Google reports:

- DeepSWE v1.1: 77.9%;
- AutomationBench: 51.3%;
- LVBench: 91.7%;
- CWE-bench v1: 68%;
- large internal code migrations including C/C++→Rust.

Source:

- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/

## Independent benchmark signal

Artificial Analysis reports Argon High at **53**, matching Astra Max and one point above GPT-6.1 Sol Max on the current broad Intelligence Index.

At the temporary launch discount:

- cost/task: ~$1.99;
- Astra Max: ~$3.26;
- GPT-6.1 Sol Max: ~$0.72.

After standard pricing returns, AA estimates Argon around ~$3.98/task.

Important token-efficiency detail:

- Argon: ~62k output tokens/task
- Astra Max: ~27k

Its launch cost efficiency is therefore mainly **price-driven**, not token-driven.

### Agentic strengths

Independent AA results:

- AutomationBench-AA: **78%**, current #1 in the cited run;
- Terminal-Bench 4.0: **57%**;
- AA-Briefcase: solid but presentation/analytical quality trails some frontier competitors.

### Reliability / hallucination

This is Argon's most unusual independent result.

AA reports a **15% hallucination rate**, the lowest among leading models scoring 45+ on its Intelligence Index at the time.

But Argon's factual accuracy was only 50%, below Astra's 63%.

Interpretation:

> Argon appears much more willing to say "I don't know" than confidently guess.

That may be extremely valuable for research/review workflows even when raw answer rate is lower.

Source:

- https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs

## Current community signal

The strongest Reddit consensus is not yet about quality.

It is:

> **"We cannot really use it yet."**

Repeated complaints focus on:

- restricted Fairwind rollout;
- lack of Pro/general API access;
- concern that Google is announcing a model before ordinary developers can test it.

The limited actual user commentary is mixed:

- visual/demo outputs can be impressive;
- some users think its agent/coding results look closer to GPT-6.1 Sol/Sonnet 5.5 than to an undisputed new #1;
- users remain skeptical of provider headline benchmarks until broad access.

Representative threads:

- https://www.reddit.com/r/GeminiAI/comments/1wufc6s/gemini_4_argon_release/
- https://www.reddit.com/r/GeminiAI/comments/1wufgo3/gemini_4_argon_our_next_era_of_frontier/
- https://www.reddit.com/r/Bard/comments/1wuskma/gemini_4_argon_first_impressions/

## Current routing prior

**Watchlist frontier model, not a current default.**

Once generally accessible, priority tests should be:

1. Argon vs GPT-6.1 Sol on a long-horizon software-engineering task.
2. Argon vs Opus 5.5 on terminal/tool use.
3. Argon vs Astra on sourced research where hallucination behavior matters.
4. Argon on multimodal long-context work with video/charts/documents.

Confidence: **low**, because availability prevents robust community validation.

---

# 4. What did not release

## Claude Haiku 5.5

Anthropic still says Haiku 5.5 will join the 5.5 family "in the coming weeks."

No current baseline should be created.

## DeepSeek V4.1 Pro

Community leaks and references exist, but DeepSeek has not released it.

DeepSeek V4.1 Flash remains the current real model.

Do not convert OpenCode sitemap leaks into a model record.

## Meta

No post-September-24 model release materially changes the existing Muse Spark / Llama baseline.

## Kimi

No verified post-September-24 successor to Kimi K3 / K2.7 Code was found.

## OpenAI Astra Ultrafast

Ultrafast is a processing/service tier for GPT-6 Astra, not a distinct base model.

It belongs in harness/service economics if we evaluate it, not in the model baseline dataset.

---

# 5. New cross-provider routing hypothesis

Based on public evidence only:

### Architecture / ambiguous high-judgment work

1. Opus 5.5 High
2. Astra Medium/High
3. Fable 5.1 High/XHigh

GPT-6.1 Sol is becoming credible here but is still better established as a workhorse than as the highest-judgment choice.

### Serious daily coding

1. GPT-6.1 Sol High/XHigh — strongest current cost/quality prior
2. Opus 5.5 Medium/High — strongest collaboration/judgment prior
3. Sonnet 5.5 Medium/High — strongest Anthropic worker prior

### Well-scoped implementation workers

1. GPT-6 Luna High/XHigh when verification is cheap
2. Sonnet 5.5 Medium/High when more reasoning/design quality is needed
3. GPT-6.1 Sol Medium/High for tasks where failure/rework costs more than Luna's savings

### Frontend / visual design

Current public sentiment favors:

1. Opus 5.5
2. Sonnet 5.5
3. GPT-6.1 Sol

This is community evidence, not a controlled benchmark.

### Research where hallucination avoidance matters

Gemini 4 Argon becomes very interesting **once accessible**, because its independent non-hallucination result is unusually strong.

---

# 6. Priority owner experiments

The public evidence now creates three high-value A/B tests:

1. **GPT-6.1 Sol High/XHigh vs Opus 5.5 High** on the same serious repository task.
2. **Sonnet 5.5 High vs GPT-6.1 Sol High** on a well-scoped implementation, measuring first-pass acceptance, wall time, quota, subagent fanout, and reviewer burden.
3. **Sonnet 5.5 High vs Opus 5.5 High** using the same Claude Code repository task.

When Argon becomes accessible:

4. **Gemini 4 Argon vs GPT-6.1 Sol / Opus 5.5** on long-horizon coding and research.

These should use the existing Harness A/B Test Protocol rather than informal impressions.
