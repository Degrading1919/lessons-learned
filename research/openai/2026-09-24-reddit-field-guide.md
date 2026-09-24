# OpenAI Model Field Guide — Reddit Consensus, Benchmarks, and Efficiency

_Last researched: 2026-09-24_

## Purpose

This report captures the current public prior for the OpenAI models that are still practically relevant in ChatGPT, Work, Codex, and the API.

It is deliberately not a leaderboard.

The useful question is:

> What kind of work does each model appear to be worth spending on, where does it fail, and how much model/quota/token budget is being exchanged for the quality gained?

This report combines:

1. current OpenAI documentation;
2. independent Artificial Analysis benchmarks;
3. repeated themes across AI-focused Reddit communities;
4. concrete public usage examples when available.

It remains separate from the owner's personal cases. Reddit sentiment is anecdotal, self-selected, harness-dependent, and vulnerable to launch-day hype or backlash.

## Scope

The general-purpose OpenAI models currently worth routing between are:

- GPT-6 Astra
- GPT-6 Sol
- GPT-6 Luna
- GPT-5.6 Sol
- GPT-5.6 Terra
- GPT-5.6 Luna

GPT-6 Pro in Chat is powered by Astra rather than being treated here as a separate base model.

OpenAI also offers specialized models such as GPT-5.6 Cyber / Daybreak Red, GPT-Live-1, and image-generation models. Those are not compared in this general coding/reasoning efficiency matrix because their job is different.

GPT-5.5 and older models remain relevant as historical or compatibility references, but they are no longer the main routing set.

## Current family structure

OpenAI's current API guidance is explicit:

- **Astra:** hardest end-to-end work;
- **Sol:** balance intelligence and cost;
- **Luna:** focused, cost-sensitive, high-volume work.

GPT-6 Sol and Luna launched on 2026-09-22. They are available in ChatGPT Work and Codex and through the API; at launch they are separate from the models in ordinary Chat.

GPT-5.6 Terra has no direct GPT-6 Terra successor. That matters because Terra still occupies a behavior niche that some users prefer even though its API economics are less compelling after GPT-6.

Official sources:

- https://developers.openai.com/api/docs/models
- https://openai.com/index/introducing-gpt-6-sol-and-luna/
- https://help.openai.com/en/articles/6825453-chatgpt-plus

## How Reddit evidence was interpreted

The primary communities reviewed were:

- r/codex — strongest source for coding-agent behavior and subscription economics;
- r/ChatGPTPro — useful for research, professional work, Work/Codex usage, and Astra;
- r/OpenAI — broader model comparisons;
- r/ChatGPT — general-user behavior;
- r/WritingWithAI and writing discussions — useful for creative-writing failure modes.

Repeated themes across independent threads were weighted more heavily than one spectacular success or failure.

Upvotes are useful for locating experiences that resonated with a community, but they are not a scientific sample.

Complaint-heavy communities create negative-selection bias. Release-day threads create both honeymoon and backlash bias.

For GPT-6 Sol and Luna in particular, confidence remains provisional because only about two days of public use exist.

---

# Executive field guide

| Model | Current public role | Excels at | Common failure / bad fit | Efficiency prior | Forum confidence |
|---|---|---|---|---|---|
| **GPT-6 Astra** | Scarce architect / integrator / final reviewer | ambiguous end-to-end work, architecture, difficult debugging, computer use, research, UI/visual judgment, autonomous recovery | routine implementation, small fixes, tasks where overthinking is wasteful | expensive but can save rework; Low/Medium/High usually more rational than Max | medium-high |
| **GPT-6 Sol** | Cost-balanced lead / difficult implementer | coding-agent benchmarks, terminal work, automation, tool use, cheaper sustained agent work | early reports of under-execution, sloppy code, skill/tool misses, unexpected actions, omitted details | excellent on paper; Medium/High likely sweet spot, but first-pass quality is disputed | low-medium |
| **GPT-6 Luna** | High-volume worker / subagent | clear implementation, classification, transformations, tests, docs, structured output, background automations | ambiguous architecture, weakly specified work, instruction drift, tasks where errors are expensive | exceptional; likely best OpenAI quality-per-dollar worker if verification is cheap | low-medium |
| **GPT-5.6 Sol** | Proven legacy high-end engineer | architecture, debugging, backend, unusual codebases, orchestration, detailed review | expensive, can loop/overwork, now economically dominated by 6 Sol when 6 Sol behaves well | high quality but poor API value versus 6 Sol; useful behavioral fallback | high |
| **GPT-5.6 Terra** | Forgiving daily implementation workhorse | moderately ambiguous coding, routine repo work, tasks where intent is implicit in nearby files | awkward API price/performance position; not as deep as Sol and not as cheap as Luna | still a useful subscription/workflow underdog; API niche is thinner | high |
| **GPT-5.6 Luna** | Legacy cheap worker | clear bounded implementation, subagents, background tasks | weaker planning, general-chat shallowness, instruction errors | largely superseded economically by 6 Luna, but may remain a behavior fallback | high |

---

# 1. GPT-6 Astra

## Benchmark prior

Artificial Analysis v4.3.2 reports:

| Effort | Intelligence Index | Cost per AA task |
|---|---:|---:|
| Low | 46 | $0.82 |
| Medium | 50 | $1.54 |
| High | 51 | $1.73 |
| XHigh | 52 | $2.31 |
| Max | 53 | $3.26 |

Source:

- https://artificialanalysis.ai/models/releases/gpt-6-astra

The important economic observation is diminishing returns.

High reaches 51 at about $1.73/task. Max reaches 53 at about $3.26/task. Max is therefore not a rational default merely because it is available.

OpenAI positions Astra as the best model across the board and specifically for the hardest end-to-end work.

## What users repeatedly like

### End-to-end autonomy

The positive coding consensus is less about typing better code and more about staying with an entire problem:

> inspect → understand → change → run → diagnose → repair → retest.

Users repeatedly describe Astra as more useful when the hard part is maintaining the whole mental model rather than generating an isolated function.

### Architecture and orchestration

A common community routing pattern is to let Astra:

- understand the repository;
- rewrite agent instructions;
- establish architecture;
- create work packages;
- review other models;
- intervene on difficult blockers.

This matches the owner's later Margins lesson: scarce reasoning capacity creates more marginal value in review/orchestration than in twelve hours of mechanical implementation.

### Research and professional work

r/ChatGPTPro reports are generally positive about research, source handling, inference, and difficult professional tasks.

### UI and visual judgment

Several Codex users prefer Astra for frontend/UI work and visual judgment even when they route backend implementation to cheaper models.

### Long-form writing — ability is high, usefulness is polarized

Some long-form writers report a major improvement in continuity, character voices, style adherence, planning, and chapter-scale work.

Other writers report over-sanitization, style flattening, or guardrail interference.

The safest baseline is:

**Astra appears to have strong writing capability, but creative usefulness is unusually workflow- and guardrail-sensitive.**

For now it is easier to trust as:

- editor;
- continuity checker;
- structure/outline model;
- style critic;

than to assume it is the universal best prose generator.

## What users repeatedly dislike

### Quota burn

This is the clearest Astra consensus.

Examples include Plus/Pro users reporting:

- a five-hour allowance disappearing in minutes;
- weekly pools disappearing during one difficult task;
- tasks ending before completion because the reasoning budget consumed the available allowance.

Representative threads:

- https://www.reddit.com/r/ChatGPTPro/comments/1w8rqbt/gpt6_astra_usage/
- https://www.reddit.com/r/ChatGPTPro/comments/1w9isu9/gpt6_astra_is_not_a_model_for_plus_users/
- https://www.reddit.com/r/codex/comments/1wciwc1/gpt56_astra_burns_quota_4_times_faster_than_gpt56/

### Overengineering

A repeated complaint is "cathedral building": Astra can turn a straightforward feature or fix into a more elaborate architecture than the task requires.

This is not evidence that the architecture is necessarily bad. It is a role-fit problem.

### Practical intuition is not uniformly better

Some experienced users describe Astra as obviously clever but occasionally worse than 5.6 Sol at practical judgment: choosing the simple fix, understanding implied intent, or knowing when to stop.

## Efficiency conclusion

**Astra is not the waste-of-time model. Astra at excessive effort on ordinary work is the waste trap.**

The benchmark curve strongly supports this:

- Low already reaches 46;
- Medium reaches 50;
- High reaches 51;
- the last two points from High to Max almost double AA task cost.

### Baseline routing

Use Astra when:

- ambiguity is high;
- multiple systems must be integrated correctly;
- architectural mistakes are expensive;
- the task requires computer use or difficult environment navigation;
- a cheaper model has already failed;
- you need a final independent reviewer.

Prefer Low/Medium first. Escalate effort because the task proved difficult, not because Max exists.

---

# 2. GPT-6 Sol

## Confidence warning

GPT-6 Sol released on 2026-09-22.

The benchmark evidence is mature enough to use. The human evidence is **not**.

The unusually strong early Reddit backlash should be recorded, but it should not be mistaken for a settled long-term verdict.

## Benchmark prior

Artificial Analysis v4.3.2:

| Effort | Intelligence Index | Cost per AA task |
|---|---:|---:|
| Low | 34 | $0.13 |
| Medium | 40 | $0.25 |
| High | 43 | $0.37 |
| XHigh | 44 | $0.53 |
| Max | 48 | $1.06 |

Sources:

- https://artificialanalysis.ai/models/releases/gpt-6-sol
- https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier

Compared with GPT-5.6 Sol Max:

- Intelligence Index: 48 vs 47;
- Coding Agent Index: 57 vs 55;
- AA cost per task: $1.06 vs $1.99;
- output tokens per task: about 31k vs 29k.

That last point is important.

GPT-6 Sol's lower cost does **not** come from simply using half as many tokens. It actually emitted slightly more output tokens in the AA evaluation. The savings come primarily from the lower token price.

Independent results are mixed by task:

Improvements include:

- Terminal-Bench;
- AutomationBench;
- Coding Agent Index;
- lower hallucination rate.

Regressions include:

- GDPval-AA;
- some long-form professional deliverable quality;
- omitted rubric elements in shorter outputs.

Artificial Analysis also found GPT-6 Sol answered fewer factual questions. That reduced hallucinations, but some of the apparent reliability improvement comes from selective non-answering.

## What early users like

### Usage longevity

Several users report dramatically better subscription mileage than Astra and 5.6 Sol.

One current routing pattern reported after a full workday is:

- Sol as project lead;
- Luna for simpler delegated work;
- Astra only for hard blockers.

### Backend / coding-agent economics

The official and independent coding-agent numbers give this model a strong prior for:

- sustained repo work;
- terminal tasks;
- backend engineering;
- automation;
- agentic workflows.

### Medium/High economics

The AA curve makes Medium and High unusually compelling:

- Medium: 40 for $0.25/task;
- High: 43 for $0.37/task;
- XHigh: 44 for $0.53/task;
- Max: 48 for $1.06/task.

High gains most of the practical capability before the expensive Max jump.

## What early users dislike

### "Cheaper but worse where it matters"

This is currently one of the most repeated r/codex themes.

High-engagement threads report:

- sloppy implementation;
- needing much more explicit handholding;
- confusing itself and undoing repairs;
- unrequested commits/pushes;
- ignoring available skills;
- weak simple-tool execution;
- feeling more like an improved Terra than a true 5.6 Sol successor.

Representative threads:

- https://www.reddit.com/r/codex/comments/1wnto0j/sol_6_is_a_slop_fest/
- https://www.reddit.com/r/codex/comments/1woiw95/something_is_wrong_with_gpt_6_sol/
- https://www.reddit.com/r/codex/comments/1wotvyv/gpt_6_sol_is_an_idiot/
- https://www.reddit.com/r/codex/comments/1wo7pz8/all_they_needed_to_do_was_fix_the_token_burn_with/
- https://www.reddit.com/r/codex/comments/1wnmb6z/gpt_6_sol_is_actually_a_nerf_to_usage_speculation/

These reports are too numerous to ignore, but they are still only two days of self-selected experience.

### Concision may be cutting both ways

OpenAI intentionally trained GPT-6 Sol/Luna toward:

- shorter answers;
- less jargon;
- fewer low-value details.

Artificial Analysis independently observed poorer presentation quality and omitted rubric elements on some knowledge-work tasks.

That creates a plausible explanation for the human complaint:

> the model feels as though it did not fully execute the task.

This does not prove every complaint has the same cause.

## Efficiency conclusion

On benchmarks, GPT-6 Sol is a **major efficiency upgrade, not a major raw-capability upgrade**.

The human question is whether its lower first-pass reliability in some workflows causes enough retries to erase those savings.

### Baseline routing

Provisional:

- **Medium:** ordinary serious engineering;
- **High:** likely current sweet spot for difficult implementation;
- **XHigh:** use when review shows High is missing depth;
- **Max:** integration-heavy work where the extra terminal/coding performance justifies roughly 3x High's task cost.

Until the early behavioral complaints settle, keep GPT-5.6 Sol available as a fallback for workflows where GPT-6 Sol under-executes or mishandles tools.

---

# 3. GPT-6 Luna

## Why Luna is the surprising underdog

The public conversation before release was largely "please give us a Luna that Astra does not need to constantly repair."

Early evidence suggests GPT-6 Luna may be the most consequential efficiency release in the family even though it is nowhere near Astra in raw intelligence.

## Benchmark prior

Artificial Analysis v4.3.2:

| Effort | Intelligence Index | Cost per AA task |
|---|---:|---:|
| Low | 21 | $0.0045 |
| Medium | 29 | $0.02 |
| High | 32 | $0.03 |
| XHigh | 34 | $0.04 |
| Max | 37 | $0.07 |

Sources:

- https://artificialanalysis.ai/models/releases/gpt-6-luna
- https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier

At Max:

- intelligence remains 37, equal to 5.6 Luna Max;
- cost falls from about $0.18 to $0.07 per AA task;
- output tokens actually increase from about 41k to 51k;
- Coding Agent Index falls from 43 to 41.

So this is not a simple "new Luna is smarter" story.

It is primarily an **enormous cost-efficiency story with mixed benchmark movement**.

## What early users like

### Bulk implementation from a strong plan

One of the clearest repeated workflows is:

1. use a stronger model to plan/review;
2. give Luna detailed tasking;
3. let Luna perform most of the coding grind;
4. return to the stronger model periodically for architecture/review.

A recent r/codex report described three hours of Luna High/XHigh coding while retaining 85% of the five-hour usage pool.

Representative thread:

- https://www.reddit.com/r/codex/comments/1wo11fj/gpt6_luna_review_after_3_hours_coding_on_a_big/

### Concision

Users coming from 5.6 Luna notice substantially less self-directed "yapping."

For operational agents, that can be a feature.

### Structured production use

The current r/codex moderator-support application "Dexter" uses GPT-6 Luna High for moderation decisions and Luna for OCR/image description.

That is a concrete public use case for:

- classification;
- strict JSON;
- rule following;
- OCR/image analysis;
- human-review fallbacks.

Source:

- https://developers.reddit.com/apps/dexterthebot

### Absolute cost is tiny

Even Max costs only about $0.07 per AA Intelligence task.

That makes a different economics possible:

> If verification is automated and cheap, spending a little more Luna reasoning is often preferable to immediately escalating to Sol.

## What early users dislike

### Instruction following is not settled

Reports include:

- ignoring instructions;
- silly implementation mistakes;
- slower project progress than 5.6 Luna;
- context loss;
- looping during infrastructure/refactor tasks.

Representative threads:

- https://www.reddit.com/r/codex/comments/1wox48m/luna_6_vs_luna_56/
- https://www.reddit.com/r/codex/comments/1woxxj2/this_needs_more_attention/
- https://www.reddit.com/r/codex/comments/1wnmhnq/gpt56_luna_fans_how_does_gpt6_luna_feel_so_far/

The evidence is genuinely mixed.

That is exactly why Luna should be assigned work with a cheap acceptance test.

## Efficiency conclusion

**GPT-6 Luna is the strongest OpenAI underdog candidate.**

Not because it is secretly Astra.

Because there is a huge set of tasks for which "good enough + testable + nearly free" beats "best possible first draft."

### Best provisional tasks

- bounded code changes;
- tests;
- documentation;
- migrations with clear invariants;
- transformations;
- extraction/classification;
- structured JSON;
- background agents;
- subagents;
- triage;
- OCR/image-description workflows;
- mechanical review/fix loops.

### Bad provisional tasks

- architecture from a vague goal;
- semantic integration across many systems;
- high-cost destructive operations without a verifier;
- tasks where one wrong assumption creates hours of cleanup.

### Effort routing

Because absolute cost remains tiny:

- High is a strong default;
- XHigh is attractive for slightly ambiguous worker tasks;
- Max is defensible when the task is still clearly bounded and verified.

Do not assume Max makes Luna an architect.

---

# 4. GPT-5.6 Sol

## Current status

Artificial Analysis now marks 5.6 Sol as superseded for current benchmarking by GPT-6 Sol.

It is still operationally relevant because:

1. users know its behavior;
2. it remains part of current ChatGPT usage;
3. early GPT-6 Sol behavior is disputed;
4. a known model can outperform a cheaper replacement on a specific workflow.

## Stable community strengths

Two months of r/codex reports consistently associate 5.6 Sol with:

- difficult debugging;
- backend work;
- large/unusual codebases;
- architecture;
- optimization;
- orchestration;
- finding implicit assumptions.

This agrees with the owner's Agentic AI case.

## Stable complaints

- high quota consumption;
- long validation/testing loops;
- overengineering;
- occasional loss of the main goal after extended work;
- destructive or over-broad actions in some agentic workflows;
- expensive use at high/max effort.

Representative public discussion:

- https://www.reddit.com/r/codex/comments/1utzi5w/gpt56_sol_vs_terra_vs_luna_my_early_guide_to/
- https://www.reddit.com/r/codex/comments/1v5norf/gpt56_in_codex_may_have_the_same_token_pricing/

## Efficiency conclusion

As an API default, 5.6 Sol is now difficult to justify when GPT-6 Sol works:

- 5.6 Sol Max: 47 index, about $1.99/task;
- 6 Sol Max: 48 index, about $1.06/task.

But **behavioral stability is itself valuable**.

The correct current status is:

> legacy-active fallback / known-behavior high-end engineer.

Do not remove it from routing until GPT-6 Sol has enough evidence to replace it for the owner's own tasks.

---

# 5. GPT-5.6 Terra

## Why Terra remains interesting

GPT-6 launched without a Terra model.

At the same time, GPT-6 Sol moved into approximately Terra's former token-price territory.

On pure API economics, Terra's niche therefore looks much weaker.

Artificial Analysis reports Terra Max:

- Intelligence Index 42;
- about $1.40 per AA task;
- $2/M input;
- $12/M output.

Source:

- https://artificialanalysis.ai/models/gpt-5-6-terra

GPT-6 Sol High reaches 43 for about $0.37 per AA task.

On a spreadsheet, Terra should be obsolete.

Reddit and the owner's own evidence make the answer less simple.

## Stable community strength: prompt convenience

The most useful Terra advocates describe it as a model for work where:

- the repository is reasonably coherent;
- the desired change is understandable from nearby files;
- the prompt is not exhaustively specified;
- Luna would need a more explicit handoff;
- Sol would be unnecessary.

This is a **human-attention efficiency** advantage rather than a token-price advantage.

Representative discussion:

- https://www.reddit.com/r/codex/comments/1v21pa4/does_anyone_even_use_gpt_56_terra/
- https://www.reddit.com/r/codex/comments/1vf3i0r/after_researching_gpt56_models_heres_the_simple/

## Weakness

Terra is squeezed from both sides:

- Luna is cheaper;
- Sol is deeper;
- GPT-6 Sol now has stronger benchmark economics at comparable token prices.

## Efficiency conclusion

**Terra High is the surprising 5.6 underdog, but only if it reduces human prompting/review enough to matter.**

The owner's Adventurer's Rise evidence strongly supports exactly that role.

This is a model whose personal evidence should outweigh generic Pareto charts.

---

# 6. GPT-5.6 Luna

## Current status

5.6 Luna established the cheap-worker pattern that GPT-6 Luna now extends.

Artificial Analysis Max:

- Intelligence Index 37;
- about $0.18 per task;
- 5.6 Luna actually scores two points higher than 6 Luna on the current Coding Agent Index.

This prevents a simplistic claim that 6 Luna dominates every task.

## Stable strengths

- well-specified implementation;
- high-volume background work;
- inexpensive subagents;
- review/fix loops;
- basic extraction/transformation;
- work where strong tests catch mistakes.

## Stable weaknesses

General-chat and coding complaints repeatedly include:

- superficial answers;
- weak roleplay/creative depth;
- instruction-following mistakes;
- poor architecture when intent is implicit;
- requiring stronger models to repair errors.

Before GPT-6 Luna launched, a common r/codex complaint was that an Astra + Luna pipeline could lose its savings because Astra spent too much time correcting Luna.

Representative thread:

- https://www.reddit.com/r/codex/comments/1wc3k1y/we_need_gpt6_luna/

## Efficiency conclusion

GPT-5.6 Luna is now mainly a **behavioral fallback**.

GPT-6 Luna is dramatically cheaper, but keep 5.6 available when a specific task/harness demonstrates better instruction-following or coding behavior.

---

# The "token spinach" problem: what efficiency actually means

Token price is only one term in the cost function.

For agentic work, a more useful approximation is:

> **completed-task cost = generation + context/cache + retries + reviewer-model cost + human steering + wall time + failure/rework risk**

This explains several otherwise contradictory observations.

## 1. Cheaper tokens do not mean fewer tokens

Independent testing found:

- GPT-6 Sol Max: about 31k output tokens/task vs 29k for 5.6 Sol;
- GPT-6 Luna Max: about 51k vs 41k for 5.6 Luna.

Yet both are substantially cheaper because per-token pricing fell.

Therefore:

**GPT-6's efficiency improvement is primarily economic/infrastructure efficiency, not necessarily greater token parsimony.**

## 2. A cheap worker can become expensive if the reviewer constantly repairs it

This is the historical 5.6 Luna problem and the key risk for GPT-6 Luna.

If a $0.07 worker produces three bad implementations that consume a strong reviewer's time, the nominal token savings are irrelevant.

## 3. An expensive model can be cheaper if it gets the architecture right once

This is where Astra earns its place.

Astra can be rational when one incorrect architectural decision would create hours of downstream work.

The mistake is using that same logic for every single implementation task.

## 4. Reasoning effort has diminishing returns

### Astra

High → Max:

- 51 → 53 intelligence;
- $1.73 → $3.26/task.

### GPT-6 Sol

High → Max:

- 43 → 48;
- $0.37 → $1.06/task.

### GPT-6 Luna

High → Max:

- 32 → 37;
- $0.03 → $0.07/task.

The marginal five points mean different things at these absolute prices.

For Luna, Max can still be trivial in dollar terms.

For Astra, blindly selecting Max can double an already expensive workload.

## 5. Subscription quota is not the same thing as API price

Reddit users repeatedly assume a 50% API price cut should mean 2x subscription usage.

Observed limits do not map that cleanly.

Reports after the GPT-6 launch suggest subscription mileage improved, but not necessarily in direct proportion to API price.

Treat:

- API dollars;
- ChatGPT/Codex credits;
- five-hour window;
- weekly allowance;

as separate resource currencies.

## 6. Harness behavior can dominate model economics

Agent harnesses can spend tokens on:

- repeated repository scans;
- subagent polling;
- large tool descriptions;
- unchanged context;
- recursive reviewer loops;
- verbose progress state.

GPT-6 improved prompt caching, with a 90% cached-input discount, specifically because persistent agents repeatedly carry the same context.

Source:

- https://openai.com/index/better-prompt-caching-for-gpt-6/

A "wasteful model" complaint can therefore actually be:

- a model problem;
- a reasoning-effort problem;
- a harness problem;
- a repository-context problem;
- an orchestration problem.

Record which one the evidence supports.

---

# Current underdogs

## GPT-6 Luna — strongest current underdog

The raw score does not look exciting next to Astra.

The economics do.

If a task is:

- easy to specify;
- cheap to test;
- safe to retry;

Luna may produce more completed work per allowance than any other OpenAI model.

## GPT-5.6 Terra — workflow underdog

Its benchmark/API economics are being squeezed out.

But users who dislike writing exhaustive handoffs still find value in its "understands enough without Sol pricing" behavior.

The owner's own Adventurer's Rise results support this more strongly than the generic public curve does.

## Astra Low/Medium — effort-setting underdog

The underdog is not always a small model.

Astra Low scores 46 at $0.82/task, while Max scores 53 at $3.26.

For many hard tasks, **Astra Low/Medium may be a better buy than selecting Sol Max or Astra Max automatically**, especially when the value is architectural judgment rather than exhaustive execution.

---

# Current waste traps

These are not declarations that the model itself is worthless.

They are combinations where the marginal quality is unlikely to justify the spend.

## Astra High/Max on routine implementation

Using Astra Max to:

- rename fields;
- write ordinary CRUD;
- make isolated UI changes;
- run mechanical migrations;
- generate repetitive tests;

is difficult to justify unless the surrounding system makes the change unusually dangerous.

## GPT-6 Sol Max by default

High scores 43 at about $0.37/task. Max scores 48 at about $1.06.

Use Max because High failed or because the task is integration/terminal-heavy, not because "Max must be best."

## GPT-5.6 Sol via API when GPT-6 Sol works

The price/performance difference is too large to ignore.

Keep 5.6 Sol for proven behavioral compatibility, not as the new default.

## GPT-5.6 Luna via API when GPT-6 Luna works

Same logic.

Its remaining value is task-specific behavior, not economics.

## Luna on vague architecture

The worker is only cheap if the work survives review.

Giving Luna an underspecified architecture problem can convert low token cost into high rework cost.

## Giant mixed-role prompts without a role split

The corpus and Reddit both increasingly point toward:

> strong planner/reviewer → cheaper implementer(s) → tests → strong integration review

rather than one scarce model acting as:

- architect;
- coder;
- tester;
- reviewer;
- documenter;
- debugger;

for every hour of a large task.

---

# Provisional OpenAI routing by task

| Task | First public-prior choice | Why | Escalation / fallback |
|---|---|---|---|
| Ambiguous architecture | Astra Medium/High | judgment and system integration | Astra Max only if stakes justify it; 5.6 Sol for known behavior |
| Hard cross-system integration | Astra or 5.6 Sol; 6 Sol under test | failures are expensive | independent review mandatory |
| Normal serious coding | GPT-6 Sol Medium/High | benchmark cost/capability | 5.6 Sol if 6 Sol under-executes |
| Moderately ambiguous routine coding | 5.6 Terra High remains credible | lower prompting burden | compare against 6 Sol Medium |
| Bulk implementation from a plan | GPT-6 Luna High/XHigh | very low cost, adequate capability | Sol review |
| Mechanical migrations / tests / docs | GPT-6 Luna | cheap and verifiable | retry or escalate only failing pieces |
| Background classification / structured JSON | GPT-6 Luna High | concrete production-style evidence | human-review fallback |
| Repository-wide final review | Astra Low/Medium/High | scarce judgment has leverage | 5.6 Sol or 6 Sol Max as cheaper reviewer |
| Difficult debugging | 5.6 Sol proven; Astra for hardest | stable human evidence | test 6 Sol High as replacement |
| UI / visual judgment | Astra | strongest current community signal | human visual review |
| Research / sourced synthesis | Astra | strong Pro-user reports | 5.6 Sol / 6 Sol pending direct evidence |
| Long-form creative writing | Astra is high capability but polarized | continuity/style strengths vs guardrails | test on actual style before standardizing |

---

# What would change this baseline

The most valuable future evidence is not another Reddit thread.

It is a controlled personal comparison.

Priority experiments:

1. same bounded coding task: **6 Luna High/Max vs 5.6 Terra High**;
2. same serious implementation: **6 Sol High vs 5.6 Sol High**;
3. same architecture review: **Astra Low/Medium vs Sol Max**;
4. same planner-worker workflow: **Astra/Sol planner → Luna workers** versus one-model ownership;
5. measure not only tokens, but:
   - first-pass acceptance;
   - number of corrections;
   - total quota consumed;
   - human interventions;
   - wall time;
   - regression count after tests/playtest.

Those comparisons would convert these public priors into evidence that is actually optimized for the owner's workflow.

---

# Representative source registry

## Official OpenAI

- https://openai.com/index/gpt-6-astra/
- https://openai.com/index/introducing-gpt-6-sol-and-luna/
- https://developers.openai.com/api/docs/models
- https://openai.com/index/better-prompt-caching-for-gpt-6/
- https://openai.com/index/gpt-5-6/
- https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/

## Independent benchmark sources

- https://artificialanalysis.ai/models/releases/gpt-6-astra
- https://artificialanalysis.ai/models/releases/gpt-6-sol
- https://artificialanalysis.ai/models/releases/gpt-6-luna
- https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier
- https://artificialanalysis.ai/models/releases/gpt-5-6-sol
- https://artificialanalysis.ai/models/gpt-5-6-terra
- https://artificialanalysis.ai/models/releases/gpt-5-6-luna

## Reddit / community

### Astra

- https://www.reddit.com/r/ChatGPTPro/comments/1w8rqbt/gpt6_astra_usage/
- https://www.reddit.com/r/ChatGPTPro/comments/1w9isu9/gpt6_astra_is_not_a_model_for_plus_users/
- https://www.reddit.com/r/ChatGPTPro/comments/1wbs9cq/what_is_everyones_opinion_on_chatgpt6_astra_so_far/
- https://www.reddit.com/r/codex/comments/1wcpz5j/gpt6sol_staged_in_openai_api/

### GPT-6 Sol

- https://www.reddit.com/r/codex/comments/1wnh1jg/gpt6_sol_model/
- https://www.reddit.com/r/codex/comments/1wnto0j/sol_6_is_a_slop_fest/
- https://www.reddit.com/r/codex/comments/1woiw95/something_is_wrong_with_gpt_6_sol/
- https://www.reddit.com/r/codex/comments/1wotvyv/gpt_6_sol_is_an_idiot/
- https://www.reddit.com/r/codex/comments/1wo7pz8/all_they_needed_to_do_was_fix_the_token_burn_with/
- https://www.reddit.com/r/codex/comments/1woa9fk/codex_usage_feels_brutally_much_better/
- https://www.reddit.com/r/codex/comments/1woc006/new_model_drops_users_declare_it_sucks_within_37/

### GPT-6 Luna

- https://www.reddit.com/r/codex/comments/1wnhyh0/gpt_6luna_benchmarks/
- https://www.reddit.com/r/codex/comments/1wnmhnq/gpt56_luna_fans_how_does_gpt6_luna_feel_so_far/
- https://www.reddit.com/r/codex/comments/1wo11fj/gpt6_luna_review_after_3_hours_coding_on_a_big/
- https://www.reddit.com/r/codex/comments/1wox48m/luna_6_vs_luna_56/
- https://www.reddit.com/r/codex/comments/1woxxj2/this_needs_more_attention/
- https://developers.reddit.com/apps/dexterthebot

### GPT-5.6 family

- https://www.reddit.com/r/codex/comments/1wc3k1y/we_need_gpt6_luna/
- https://www.reddit.com/r/codex/comments/1v21pa4/does_anyone_even_use_gpt_56_terra/
- https://www.reddit.com/r/codex/comments/1vf3i0r/after_researching_gpt56_models_heres_the_simple/
- https://www.reddit.com/r/codex/comments/1utzi5w/gpt56_sol_vs_terra_vs_luna_my_early_guide_to/
- https://www.reddit.com/r/codex/comments/1v5norf/gpt56_in_codex_may_have_the_same_token_pricing/
