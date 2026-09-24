# Anthropic / Claude Model Field Guide — Reddit Consensus, Benchmarks, and Efficiency

_Last researched: 2026-09-24_

## Purpose

This report is the Anthropic counterpart to the OpenAI field guide.

It records the current public prior for Claude models that materially affect routing in Claude, Claude Code, the Claude API, and connected agentic workflows.

The question is not:

> Which Claude model has the highest benchmark score?

The question is:

> Which Claude model is worth spending on for this task, which failure modes should be expected, and how much token/quota/human-review cost is exchanged for the quality gained?

This report combines:

1. current Anthropic documentation;
2. independent Artificial Analysis benchmarks;
3. repeated themes from Claude-focused Reddit communities;
4. concrete public workflows where model roles are visible.

It remains separate from the owner's personal case corpus. Public evidence is a prior, not a substitute for the owner's own runs.

## Current routing set

The models that currently matter most for practical routing are:

- Claude Opus 5.5
- Claude Fable 5.1
- Claude Opus 5
- Claude Sonnet 5
- Claude Opus 4.8
- Claude Haiku 4.5
- Claude Mythos 5.1 for restricted trusted-access work

Anthropic says Claude Sonnet 5.5 and Claude Haiku 5.5 will follow Opus 5.5 in the coming weeks. They are **not** treated as current models until released.

Older models such as Opus 4.6, Opus 4.7, Sonnet 4.6, and Sonnet 4.5 remain active on the API for compatibility, but they are not the main routing set here. Opus 4.6 is still frequently praised by users for directness and judgment, while Opus 4.8 is the more relevant coding fallback because of its larger context and agentic behavior.

Official status:

- https://docs.anthropic.com/en/docs/about-claude/model-deprecations
- https://www.anthropic.com/system-cards
- https://www.anthropic.com/claude-opus-5-5

## How Reddit evidence was interpreted

Primary communities:

- r/ClaudeAI
- r/ClaudeCode
- r/Anthropic
- r/claude

Repeated themes across multiple independent threads were weighted more heavily than one spectacular success or failure.

Important biases:

- Claude communities are unusually sensitive to personality, writing style, and "feel," which is valuable for collaboration but not the same as objective coding correctness.
- Subscription users often report quota burn rather than API dollar cost.
- Launch-day Opus 5.5 sentiment is strongly positive but still subject to honeymoon bias.
- Opus 5 has enough weeks of use that its negative communication/reliability reputation is much more mature.
- Model + Claude Code + tools/subagents/context management should be treated as the system, not the model in isolation.

---

# Executive field guide

| Model | Current public role | Excels at | Common failure / bad fit | Efficiency prior | Forum confidence |
|---|---|---|---|---|---|
| **Claude Opus 5.5** | New flagship / high-end daily model | coding, UI/debugging, agentic knowledge work, clearer collaboration, long-session work | still expensive; launch evidence immature; minor sloppiness/bugs remain | unusually strong capability/price improvement; Medium/High likely better defaults than Max | low-medium |
| **Claude Fable 5.1** | Scarce planner / deep reviewer / hardest knowledge work | architecture, orchestration, low-level code, deep debugging, research, long-horizon analysis | very expensive, high quota burn, slow, more tokens than Fable 5, production fallback muddies pure-model comparisons | spend when correctness/judgment dominates cost; XHigh often dominates Max economically | medium-high |
| **Claude Opus 5** | Transition model / QA niche | benchmark-strong problem solving, adversarial review, some difficult tasks | verbosity, jargon, overreach, unnecessary refactors, instruction drift, context/amnesia complaints, high correction burden | clearest current Claude waste trap for normal implementation | high |
| **Claude Sonnet 5** | Thorough mid-tier agent | bounded coding, knowledge work, architecture exploration, tool use | extreme token use at high/max, can cost more per finished task than Opus-class alternatives, some technical-writing rigor complaints | Low/Medium/High can be sensible; Max is often economically irrational | high |
| **Claude Opus 4.8** | Proven behavioral fallback / implementer | practical judgment, Claude Code execution, long-context coding, review, frontend/integration | expensive relative to newer discounted options; not frontier benchmark leader anymore | strong known-behavior value when newer models create rework | high |
| **Claude Haiku 4.5** | Utility worker / search-read-classify subagent | exploration, retrieval, classification, quick MVPs, cheap reviews, context-grounded tasks | weak deep reasoning, poor complex terminal/automation benchmarks, instruction-following limits on harder code | good utility economics inside Claude ecosystem, but not globally cheap by 2026 standards | high |
| **Claude Mythos 5.1** | Restricted trusted-access specialist | high-risk cyber/life-science work under specialized safeguards | not a normal routing alternative | evaluate only in authorized workflows | medium |

---

# 1. Claude Opus 5.5

## Evidence freshness

Released 2026-09-22.

Independent benchmark data is already available. Human consensus is only about two days old and therefore provisional.

## Benchmark prior

Artificial Analysis v4.3.2:

| Effort | Intelligence Index | Cost per AA task |
|---|---:|---:|
| Low | 42 | $0.55 |
| Medium | 51 | $1.34 |
| High | 54 | $1.82 |
| XHigh | 56 | $3.46 |
| Max | 58 | $5.98 |

Source:

- https://artificialanalysis.ai/models/releases/claude-opus-5-5

At Max, Artificial Analysis reports:

- Intelligence Index: 58
- AA-Briefcase: 1822
- GDPval-AA: 1846
- AutomationBench-AA: 70%
- Terminal-Bench 4.0: 60%
- SciCode: 67%
- output tokens/task: ~119k
- reasoning tokens/task: ~84k
- cost/task: ~$5.98

It currently leads the Artificial Analysis Intelligence Index and is several points ahead of Fable 5.1.

## Provider economics

Anthropic pricing:

- input: $4/M
- output: $20/M
- cache read: $0.20/M

Anthropic says typical default-setting workloads cost ~40% less than Opus 5, cache reads are 60% cheaper, and output is >30% faster.

Source:

- https://www.anthropic.com/claude-opus-5-5

## What early users like

### Communication quality

This is the clearest launch-day theme.

Users repeatedly say Opus 5.5:

- communicates more naturally;
- puts the important point first;
- is less full of Claude-specific jargon;
- is easier to audit during long coding sessions;
- writes shorter code comments and less prose.

This matters operationally because reading/steering cost is part of completed-task cost.

### UI and frontend debugging

One highly engaged r/ClaudeAI thread specifically praises its speed at finding UI bugs.

The owner's prior Claude Code evidence also suggests live-environment and frontend work is an Anthropic strength when the harness can inspect the real target environment.

### General coding speed and practical quality

Early users describe it as the first Claude release since earlier Opus generations that feels like a genuine upgrade rather than just a benchmark change.

Several users who abandoned Opus 5 for Codex are reconsidering Claude Code.

### Cache economics

Agentic workflows repeatedly reread the same repository state.

The reduction from $0.50/M to $0.20/M cache reads is therefore more important than the 20% list-price cut implies.

One Reddit user estimated 20–40% savings on their recent orchestrator workloads if they had run on 5.5.

## Early cautions

- still produces bugs;
- minor areas can be sloppy;
- some users still see over-verification/delegation habits;
- five-hour allowance can burn quickly on lower subscription tiers;
- day-one praise is likely inflated by honeymoon effects.

A particularly useful counterexample is a user who praises the voice/style improvement but says Opus 4.6 still had better task judgment on resume work.

## Efficiency conclusion

**Opus 5.5 is currently Anthropic's strongest public-prior default for high-end work, but Max is not the default setting.**

The effort curve is revealing:

- Medium: 51 for $1.34
- High: 54 for $1.82
- XHigh: 56 for $3.46
- Max: 58 for $5.98

High captures most of the benchmark strength at less than one-third Max task cost.

### Baseline routing

- **Medium:** normal serious Claude Code work
- **High:** difficult implementation/review
- **XHigh:** hard cross-system or knowledge work
- **Max:** only when the remaining quality margin is worth ~3.3x High task cost

Do not infer that Opus 5.5 has already erased the behavioral value of Opus 4.8 or Fable 5.1 until matched owner tests exist.

---

# 2. Claude Fable 5.1

## Benchmark prior

Artificial Analysis v4.3:

| Effort | Intelligence Index | Cost per AA task |
|---|---:|---:|
| Low | 47 | $2.37 |
| Medium | 49 | $2.98 |
| High | 51 | $3.91 |
| XHigh | 53 | $5.98 |
| Max | 53 | $7.63 |

Source:

- https://artificialanalysis.ai/models/releases/claude-fable-5-1

The Max vs XHigh comparison is especially important:

- both score 53;
- XHigh costs ~$5.98/task;
- Max costs ~$7.63/task;
- XHigh uses ~61k output tokens/task;
- Max uses ~78k.

**Max is an obvious diminishing-return setting in the current independent benchmark.**

## Provider economics

Pricing:

- input: $10/M
- output: $50/M
- cache read: $0.25/M

Anthropic cut Fable 5.1 cache reads by 75% versus Fable 5.

Anthropic estimates:

- ~25% typical-workload savings;
- up to ~45% savings on highly agentic/coding workloads.

Sources:

- https://www.anthropic.com/claude/fable
- https://www.anthropic.com/claude-fable-and-mythos-5-1

## Important benchmark caveat

Artificial Analysis evaluated Fable 5.1 with Anthropic's production fallback system.

A small share of safety-flagged output was routed to Opus-family models.

Therefore a Fable 5.1 benchmark run is partly a measure of Anthropic's production model-routing system, not a perfectly isolated base model.

## What users repeatedly like

### Planning and orchestration

A very common Claude Code pattern is:

> Fable plans / reasons / reviews → Opus or Sonnet implements.

Users praise Fable for:

- big-picture repository understanding;
- migration strategy;
- complex tradeoffs;
- refactoring intent;
- difficult root-cause analysis;
- reviewing other models;
- long-running unsupervised reasoning.

### Low-level and difficult code

Forum reports are especially positive around:

- Rust;
- C/C++;
- assembly;
- low-level systems work;
- difficult debugging.

### Quality of reasoning

Even users who complain about the quota frequently describe the model as extraordinary.

## What users dislike

### Usage burn

This is the dominant complaint.

Examples include users reporting that a weekly Fable allowance can disappear in a few days even on Max plans.

### More tokens can still be cheaper per API prompt

A useful measured Reddit report compared 22,022 API calls across Fable 5 and 5.1.

The user found roughly:

- 31% more tokens/prompt on 5.1;
- but ~31% lower dollar cost/prompt because cache reads became dramatically cheaper.

This is the same lesson seen in GPT-6:

> token count and completed-work economics are different variables.

### Partial completion / "done but not done"

Some users report Fable:

- stopping early;
- claiming completion before the result works;
- creating follow-up issues instead of finishing;
- asking questions that could be resolved from context.

This is not as dominant as the positive capability signal, but it is important enough to preserve.

## Efficiency conclusion

Fable 5.1 is a **scarce thinking/review resource**, not a rational bulk implementer.

The sweet spot from public benchmarks is XHigh rather than Max.

### Baseline routing

Use for:

- architecture;
- governance;
- difficult debugging;
- low-level reasoning;
- major migration planning;
- repository-wide review;
- high-stakes research;
- hard orchestration.

Hand mechanical implementation down whenever a cheaper model can execute a verified plan.

---

# 3. Claude Opus 5

## Why it remains in this guide

Opus 5 is still active on the Claude API, but Opus 5.5 is the current successor.

It matters because the community reaction is one of the clearest examples of benchmarks failing to predict practical collaboration quality.

## Benchmark prior

Artificial Analysis v4.3:

| Effort | Intelligence Index | Cost per AA task |
|---|---:|---:|
| Low | 40 | $1.10 |
| Medium | 45 | $2.19 |
| High | 48 | $3.61 |
| XHigh | 50 | $4.88 |
| Max | 51 | $5.86 |

Source:

- https://artificialanalysis.ai/models/releases/claude-opus-5

Those are strong numbers.

## Community consensus

The negative signal is mature and unusually consistent.

Repeated complaints include:

- unreadable jargon;
- walls of text;
- explaining simple issues in long abstract prose;
- unnecessary code comments;
- assuming work completed before verification;
- unrelated refactors;
- instruction drift;
- poor context continuity/amnesia;
- confidently going down a wrong path and later undoing it;
- high human effort required to understand and correct the model.

Representative threads:

- https://www.reddit.com/r/ClaudeCode/comments/1vbu4a7/opus_5_unreadable_jargon/
- https://www.reddit.com/r/ClaudeCode/comments/1vwec8t/im_done_with_opus_5/
- https://www.reddit.com/r/ClaudeCode/comments/1va445h/opus_5_feedback_megathread/
- https://www.reddit.com/r/ClaudeCode/comments/1vxmtnv/opus_5_is_too_wordy/

There are dissenters and successful tasks. Opus 5 can solve hard problems.

The problem is **completed-task cost**: even a correct model can be economically poor if the owner spends too much time decoding, steering, or repairing it.

## Surprising niche: adversarial reviewer

A small but interesting subset of users considers Opus 5 useful as a QA/adversarial verifier precisely because it is willing to challenge assumptions and explore edge cases.

That role avoids the biggest UX cost: the owner does not need to read or collaborate with its prose for hours.

## Efficiency conclusion

**Opus 5 is the clearest current Claude waste trap for normal implementation.**

If Opus 5.5 is available, the public evidence gives little reason to choose 5.0 as a default author.

Retain only where:

- a known workflow specifically performs better on it;
- it is used as an adversarial reviewer;
- compatibility requires it.

---

# 4. Claude Sonnet 5

## Benchmark prior

Artificial Analysis v4.3:

| Effort | Intelligence Index | Cost per AA task |
|---|---:|---:|
| Low | 25 | $0.51 |
| Medium | 28 | $1.00 |
| High | 32 | $1.79 |
| Max | 38 | $5.09 |

Source:

- https://artificialanalysis.ai/models/releases/claude-sonnet-5

The High→Max jump is one of the most important efficiency warnings in this entire model family:

- intelligence: 32 → 38
- cost/task: $1.79 → $5.09
- output tokens/task: ~44k → ~118k
- reasoning tokens/task: ~28k → ~88k

Source:

- https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-high-vs-claude-sonnet-5

## Provider economics

Current pricing:

- input: $2/M
- output: $10/M

Anthropic made the introductory $2/$10 pricing permanent.

Important tokenizer note: Anthropic says the same input can map to roughly **1.0–1.35x** as many tokens as the prior tokenizer depending on content.

Source:

- https://www.anthropic.com/news/claude-sonnet-5

## What users like

### Thoroughness

The model often checks many possible paths before committing.

For complex architecture, that can be worth paying for because late architectural mistakes are expensive.

### Bounded agentic work

Sonnet remains viable for:

- normal web-app implementation;
- devops;
- well-scoped defects;
- tool use;
- knowledge work;
- projects with strong acceptance tests and clear task cards.

A recent ClaudeAI thread reports a user successfully running web work primarily on Sonnet/Haiku without hitting weekly limits, because work is broken into clear Kanban-sized units and reviewed by other models.

### Writing / knowledge work

Some users find Sonnet 5 better than Opus 4.8 for blog-style writing and certain knowledge-work tasks.

## What users dislike

### "Token monster"

This is the dominant community complaint.

Users report:

- much higher thinking-token use than Sonnet 4.6;
- longer agent loops;
- task-level cost approaching or exceeding more capable Opus-class models;
- max effort being disproportionately expensive.

Artificial Analysis independently confirms the mechanism: at Max, Sonnet 5 generated ~370M tokens across the Intelligence Index, far above the model-set median.

### Technical/academic writing complaints

Some users report:

- over-paraphrasing;
- reducing precision in technical definitions;
- weaker preference for primary academic sources;
- too much prose when technical directness is requested.

This is task-dependent, but it makes Sonnet a weaker public prior for precision-sensitive technical writing than its general "knowledge work" positioning might imply.

## Efficiency conclusion

**Sonnet 5 is useful, but Max is frequently the wrong economic choice.**

Low/Medium/High preserve the model's mid-tier role.

Max turns a mid-tier sticker price into frontier-level task cost without frontier-level benchmark performance.

### Baseline routing

Good for:

- clear implementation;
- normal repo work;
- well-scoped architecture exploration;
- knowledge work;
- default Claude usage when Fable/Opus is unnecessary.

Avoid Max by default.

---

# 5. Claude Opus 4.8

## Why an older model is still important

Opus 4.8 remains active and has a mature reliability reputation.

Anthropic released it as a model with sharper judgment, more honesty about its progress, and longer independent execution.

Pricing:

- input: $5/M
- output: $25/M
- cache read: $0.50/M

Source:

- https://www.anthropic.com/news/claude-opus-4-8

Artificial Analysis current Max data:

- cost/task: ~$4.08
- output tokens/task: ~71k
- reasoning tokens/task: ~52k
- context: 1M
- output speed: ~58 t/s

## Community consensus

Opus 4.8 is a major **behavioral fallback**.

Users repeatedly return to it after frustration with Opus 5.

Common praise:

- practical judgment;
- directness;
- reliable code execution;
- large-context coding;
- fewer irrelevant refactors;
- good Claude Code behavior;
- better first-pass trust than newer-but-problematic models.

A common modern workflow is:

> Fable 5.1 plans/reviews → Opus 4.8 implements.

The owner's Adventurer's Rise Studio-MCP case independently supports 4.8 as a strong environment-integrated implementation model.

## Weaknesses

- older and no longer benchmark-frontier;
- expensive API pricing relative to newer alternatives;
- can still consume significant quota at high/max;
- massive multi-agent audits can become absurdly expensive/slow.

## Efficiency conclusion

**Opus 4.8 is the strongest Anthropic behavioral underdog.**

It survives because first-pass practical judgment can be more valuable than a newer benchmark score.

Retain until Opus 5.5 proves itself over longer use.

---

# 6. Claude Haiku 4.5

## Current status

Haiku 4.5 remains the current Haiku model as of 2026-09-24.

Anthropic says Haiku 5.5 will follow Opus 5.5 in the coming weeks.

## Benchmark prior

Artificial Analysis reasoning variant:

- Intelligence Index: 17
- cost/task: ~$0.21
- output speed: ~109 t/s
- output tokens/task: ~18k
- context: 200k
- pricing: $1/M input, $5/M output, $0.10/M cache hits

Source:

- https://artificialanalysis.ai/models/claude-4-5-haiku-reasoning

Important limitations:

- AutomationBench-AA: 3%
- Terminal-Bench 4.0: 0%
- long-context reasoning: substantially below frontier models

This is not a small frontier engineer in 2026.

## What users like

### Search / read / classify subagent

This is Haiku's cleanest role.

A recurring pattern:

> Haiku searches/reads/classifies → Sonnet/Opus/Fable synthesizes or decides.

One Claude Code user running six agents describes Haiku as the workhorse for tasks where the answer is mostly contained in retrieved content.

### Fast MVP / rough prototyping

Users praise the response-time/quality ratio for first-pass prototypes.

### Explore-agent behavior

Claude Code has historically used Haiku for codebase exploration/search to save context.

### Cheap repeated judgments

Examples include:

- code review;
- classification;
- search;
- retrieval;
- generating candidate test cases;
- repeated grading with a strict pass/fail rubric.

## What users dislike

### Instruction following on harder code

Some users find it too weak compared with Sonnet for implementation unless strong patterns/examples are supplied.

### Globally weak value in 2026

Haiku is cheap *inside the Claude family*, but it is not especially cheap relative to modern external worker models.

Artificial Analysis has many newer models that are substantially more capable at similar or lower cost.

This matters if the harness does not require Anthropic-native integration.

## Efficiency conclusion

**Haiku is an Anthropic ecosystem utility worker, not a general-purpose cheap frontier model.**

Use it where the answer is mostly in retrieved context and verification is deterministic.

Do not use it as the architecture or difficult implementation tier.

---

# 7. Claude Mythos 5.1

Anthropic says Fable 5.1 and Mythos 5.1 share the same underlying model family but differ in safeguard/access configuration.

Mythos is designed for trusted high-risk cybersecurity and life-science workflows.

Source:

- https://www.anthropic.com/claude-fable-and-mythos-5-1

This is not a normal cost/quality routing alternative.

### Baseline routing

Use only when:

- the workflow is authorized;
- the access tier is available;
- the specialized safety configuration is materially relevant.

Do not compare Mythos against ordinary Sonnet/Opus workers as though it is a consumer tier.

---

# The Claude "token spinach" problem

Anthropic exposes a particularly useful lesson:

> **price per token can badly misrepresent price per finished task.**

## 1. Sonnet 5 is the canonical example

It is cheaper per token than Opus models.

At Max, it can consume so many reasoning/output tokens that its AA task cost (~$5.09) exceeds Opus 4.8 (~$4.08).

Therefore:

> cheaper model + more thinking != cheaper task.

## 2. Fable 5.1 shows the opposite effect

A measured Reddit corpus found ~31% more tokens/prompt than Fable 5, but ~31% lower dollar cost/prompt because cache-read pricing collapsed.

Therefore:

> more tokens != higher dollar cost.

## 3. Opus 5 shows human-attention cost

Even where benchmark intelligence is strong, user reports describe so much jargon, overreach, and correction that collaboration becomes slower.

Therefore:

> correct-ish output + high steering/reading cost can still be poor efficiency.

## 4. Cache economics matter more for Claude than most casual comparisons acknowledge

Claude Code and long-running agents repeatedly reread repository context.

Current cache reads:

- Opus 5.5: $0.20/M
- Fable 5.1: $0.25/M
- Haiku 4.5: $0.10/M

This can materially change the cost of a persistent agent even if input/output list prices look high.

## 5. Subscription quota and API economics are different currencies

A Fable API workload can become cheaper after cache discounts while a subscription user simultaneously feels their weekly bar draining faster.

Do not infer subscription allowance directly from API rates.

## 6. Human readability is an economic variable

Opus 5 is the strongest example.

A model that requires the owner to reread every answer three times or clean verbose comments from the repository can be more expensive than a nominally pricier model that communicates clearly.

---

# Current Anthropic underdogs

## 1. Opus 4.8 — strongest behavioral underdog

It is older and not the benchmark leader.

Users still trust it.

That makes it the strongest "known good" Claude Code fallback while Opus 5.5 matures.

## 2. Haiku 4.5 — utility underdog

For:

- search;
- read;
- classify;
- extract;
- explore;
- repeated rubric-based judgments;

it can deliver useful work without spending Opus/Fable quota.

Its weakness is that external 2026 worker models often beat its price/capability ratio.

## 3. Opus 5.5 Medium/High — effort-setting underdog

The biggest savings may come from not selecting Max.

High scores 54 at ~$1.82/task versus Max 58 at ~$5.98.

## 4. Sonnet 5 Low/Medium/High — not Max

Sonnet can still be useful when effort is controlled.

The mistake is treating Max as the natural setting for a "cheaper" model.

---

# Current waste traps

A waste trap is a routing pattern, not a claim that the base model is universally bad.

## Opus 5 for normal implementation

Current strongest waste trap.

Strong benchmark capability does not overcome the mature human signal around verbosity, overreach, context drift, and correction burden.

## Sonnet 5 Max as a default

At Max, the token appetite destroys the economic rationale of choosing Sonnet.

## Fable 5.1 Max when XHigh scores the same

Current independent benchmark:

- XHigh: 53 at ~$5.98
- Max: 53 at ~$7.63

Unless a task-specific benchmark or owner evidence says otherwise, Max is wasted spend.

## Opus 5.5 Max by default

High→Max:

- 54 → 58 intelligence
- $1.82 → $5.98/task

Use Max because the remaining four points matter, not because it is available.

## Haiku on deep coding/architecture

Cheap output becomes expensive when a stronger model must repair it.

## Using one expensive Claude for the entire lifecycle

The public workflow increasingly resembles:

> Fable/Opus plans or reviews → Opus/Sonnet/Haiku executes according to difficulty → tests → stronger final review

rather than one premium model doing every search, edit, test, summary, and QA pass.

---

# Provisional Anthropic routing by task

| Task | First public-prior choice | Why | Escalation / fallback |
|---|---|---|---|
| Ambiguous architecture | Fable 5.1 High/XHigh or Opus 5.5 High | deep judgment | Opus 4.8 for known behavior |
| Serious daily Claude Code | Opus 5.5 Medium/High | strongest current capability/economics | Opus 4.8 if 5.5 behavior disappoints |
| Major migration planning | Fable 5.1 High/XHigh | orchestration/tradeoffs | 5.5 review |
| Difficult low-level debugging | Fable 5.1 / Opus 5.5 | strongest reasoning signal | Opus 4.8 behavioral fallback |
| Frontend/UI implementation/debugging | Opus 5.5 | strong early forum signal | Opus 4.8 |
| Normal bounded coding | Sonnet 5 Low/Medium/High or Opus 5.5 Medium | controlled task size | 4.8 if Sonnet requires repeated fixes |
| Search/read/explore | Haiku 4.5 | cheap and fast | Sonnet for synthesis |
| Classification/extraction | Haiku 4.5 | retrieved-context utility | Sonnet/Opus for ambiguous judgment |
| Repository-wide final review | Fable 5.1 XHigh or Opus 5.5 High/XHigh | global reasoning | independent cross-provider reviewer |
| Adversarial QA | Opus 5 can have niche value | challenges assumptions | do not use as primary author |
| High-risk authorized cyber/life sciences | Mythos 5.1 / verified Opus 5.5 access | specialized safeguards/access | follow program restrictions |

---

# Most important Anthropic-vs-OpenAI economic difference

OpenAI now has a very clear cheap-worker tier in GPT-6 Luna.

Anthropic currently does **not** have an equivalent modern low-cost worker.

Haiku 4.5 is:

- older;
- only 200k context;
- weak on current terminal/automation benchmarks;
- $1/$5 per million tokens.

That helps explain why Claude users increasingly use mixed-provider workflows:

> Claude/Fable/Opus for planning and judgment → Codex/Gemini/other cheaper workers for implementation.

Anthropic says Haiku 5.5 is coming soon. That release may materially change this conclusion.

---

# What should be tested personally next

The highest-value controlled experiments for this repository are:

1. **Opus 5.5 High vs Opus 4.8 High** on the same Studio/MCP or repo integration task.
2. **Opus 5.5 High vs Fable 5.1 High/XHigh** on architecture/review.
3. **Sonnet 5 High vs Terra High / GPT-6 Luna Max** on a bounded implementation.
4. **Haiku 4.5 vs GPT-6 Luna** on search/read/classify/subagent work.
5. Measure:
   - first-pass acceptance;
   - total tokens;
   - cache reads;
   - retries;
   - number of user corrections;
   - reviewer-model time;
   - wall time;
   - five-hour/weekly quota consumed;
   - post-merge regressions.

Those tests would reveal whether Anthropic's stronger collaboration/judgment offsets its generally weaker low-cost worker economics for the owner's workflow.

---

# Representative source registry

## Anthropic

- https://www.anthropic.com/claude-opus-5-5
- https://www.anthropic.com/claude/fable
- https://www.anthropic.com/claude-fable-and-mythos-5-1
- https://www.anthropic.com/news/claude-sonnet-5
- https://www.anthropic.com/news/claude-opus-4-8
- https://docs.anthropic.com/en/docs/about-claude/model-deprecations
- https://www.anthropic.com/system-cards

## Artificial Analysis

- https://artificialanalysis.ai/models/releases/claude-opus-5-5
- https://artificialanalysis.ai/models/releases/claude-fable-5-1
- https://artificialanalysis.ai/models/releases/claude-opus-5
- https://artificialanalysis.ai/models/releases/claude-sonnet-5
- https://artificialanalysis.ai/models/claude-4-5-haiku-reasoning
- https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-command-a-plus

## Reddit — Opus 5.5

- https://www.reddit.com/r/Anthropic/comments/1wnl3k8/opus_55_first_impressions/
- https://www.reddit.com/r/ClaudeAI/comments/1wnil7n/opus_55_in_claude_code_is_crazy_fast_especially/
- https://www.reddit.com/r/ClaudeAI/comments/1wnpit2/claude_is_back/
- https://www.reddit.com/r/ClaudeAI/comments/1wo9lbs/opus_55_is_the_new_46/
- https://www.reddit.com/r/claude/comments/1wnwsg7/opus_55_worth_coming_back_from_codex/

## Reddit — Fable 5.1

- https://www.reddit.com/r/ClaudeAI/comments/1w5ai3j/fable_51_is_insane_and_it_burned_usage_which_is/
- https://www.reddit.com/r/ClaudeAI/comments/1w5pnji/fable_5_vs_fable_51_across_22022_of_my_own_api/
- https://www.reddit.com/r/ClaudeAI/comments/1wd15a1/opus_46_was_our_wet_dream_of_ai/

## Reddit — Opus 5

- https://www.reddit.com/r/ClaudeCode/comments/1vbu4a7/opus_5_unreadable_jargon/
- https://www.reddit.com/r/ClaudeCode/comments/1vwec8t/im_done_with_opus_5/
- https://www.reddit.com/r/ClaudeCode/comments/1va445h/opus_5_feedback_megathread/
- https://www.reddit.com/r/ClaudeCode/comments/1vxmtnv/opus_5_is_too_wordy/

## Reddit — Sonnet 5

- https://www.reddit.com/r/ClaudeAI/comments/1ukoszu/sonnet_5_is_a_token_monster/
- https://www.reddit.com/r/ClaudeAI/comments/1ukyy54/is_claude_sonnet_5_actually_worth_using_where_ive/
- https://www.reddit.com/r/ClaudeAI/comments/1uk0p07/opus_45_46_48_and_sonnet_5_token_data/
- https://www.reddit.com/r/ClaudeAI/comments/1ut532i/sonnet_5_writing_increasing_amounts_of_slop_and/

## Reddit — Haiku 4.5 / mixed-model workflows

- https://www.reddit.com/r/ClaudeCode/comments/1r84b60/haiku_for_search_review_tasks/
- https://www.reddit.com/r/ClaudeAI/comments/1oca664/haiku_45_is_really_really_good/
- https://www.reddit.com/r/ClaudeCode/comments/1orlzuc/haiku_45_vs_sonnet_45_my_ccusage_data_as_a_claude/
- https://www.reddit.com/r/ClaudeAI/comments/1wkegrv/is_anyone_else_doing_just_fine_with_more_basic/
