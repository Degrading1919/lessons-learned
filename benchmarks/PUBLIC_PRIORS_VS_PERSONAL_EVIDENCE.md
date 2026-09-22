# Public Priors vs. Personal Evidence

_Last reviewed: 2026-09-22_

This document records how the project's observed AI results compare with the public benchmark and community signal that would otherwise influence model selection.

The public evidence is a **prior**, not the authority. The personal corpus exists precisely because benchmark performance does not measure every variable that matters here: subscription quota, prompt shape, repository maturity, MCP access, human playtesting, task duration, or role fit.

## Benchmark interpretation rules

- Prefer independent benchmark runs over provider claims.
- Keep model + effort + harness together when possible.
- Do not compare old and new benchmark versions as if scores are on the same scale.
- Community posts are workflow sentiment, not statistical evidence.
- A public benchmark can establish a reasonable prior; project evidence can confirm, contradict, or refine it.

## 1. GPT-5.6 Sol Max / Codex

### Public prior I would have adopted

At GPT-5.6's July 2026 launch, Artificial Analysis reported Sol Max in Codex at **80** on its then-current Coding Agent Index, ahead of Terra and Claude Opus 4.8. OpenAI likewise described Sol as its strongest coding model and highlighted state-of-the-art long-horizon/terminal results.

That public evidence would have made Sol a strong default prior for difficult repository-scale coding.

### Personal evidence

The Agentic AI run strongly confirms the capability prior:

- one mission-oriented prompt;
- mature repository context;
- broad end-to-end scope;
- coherent MVP output;
- strong owner reaction;
- downstream adoption of the prompting pattern by Modular CRM.

But it adds an operational fact the benchmark does not express well: the run consumed about **92% of one five-hour usage window**.

Public community reports in July 2026 also frequently praised GPT-5.6's quality while complaining about rapid quota consumption.

### Relationship

**Confirms capability; adds major operational nuance.**

The personal result makes me *more* confident in Sol for hard, integration-heavy work, but *less* likely to use it indiscriminately for routine tasks.

### Current-benchmark caution

Artificial Analysis changed its Coding Agent Index by September 2026. On v1.5, GPT-5.6 Sol Max remains very strong on **DeepSWE v1.1** but is no longer the overall leader. Comparing the July score of 80 directly to the September v1.5 score would be invalid because the benchmark composition changed.

This reinforces a repository rule: preserve the benchmark version and date.

## 2. GPT-5.6 Terra High / Codex

### Public prior I would have adopted

At launch, Terra scored close to the frontier on coding-agent evaluations while costing materially less per task than Sol. That would have suggested a strong cost/performance implementation model.

Artificial Analysis's broader intelligence/cost analysis was less flattering to Terra: it noted that Sol or Luna often occupied the generic intelligence/cost Pareto frontier instead.

Community opinion was mixed. Some Codex users reported good value; others reported surprisingly high quota burn or serious errors.

### Personal evidence

Adventurer's Rise gives Terra a cleaner, more positive role-specific signal:

- bounded server-authoritative feature work;
- good test discipline;
- strong user satisfaction with cost vs. accuracy/content creation;
- repeated reuse of the workflow.

Independent review still found integration defects in later composition-heavy work, preventing the conclusion from becoming "Terra needs no reviewer."

### Relationship

**Confirms the coding-value prior more strongly than the generic-intelligence prior.**

For this owner's workflow, Terra High appears more useful than a generic leaderboard alone would have led me to assume for bounded implementation.

This is exactly why task-specific personal evidence matters.

## 3. Claude Opus 4.8 / Claude Code

### Public prior I would have adopted

Around the same period, Opus 4.8 was a frontier model with strong coding/terminal results, but public coding-agent indexes generally did not put it above GPT-5.6 Sol in aggregate.

Public Claude Code guidance emphasized a different advantage: high autonomy, strong repository navigation, MCP, subagents, and using powerful models for planning/review while cheaper models handle routine execution.

### Personal evidence

The Adventurer's Rise Studio-integration run was unusually strong because Opus 4.8 High had **Roblox Studio MCP** access.

The successful task was not just code generation. It required:

- understanding existing repository authority;
- mapping runtime IDs to physical Studio objects;
- inspecting the live environment;
- avoiding duplicate health/combat authority;
- running bounded verification.

That task is poorly represented by standard patch-only coding benchmarks.

### Relationship

**Adds role/harness nuance rather than contradicting benchmarks.**

A benchmark might have routed the task to the numerically highest coding model. The personal evidence instead says:

> For live-environment integration, the model + Claude Code + MCP combination can be more important than a small aggregate benchmark gap.

## 4. Astra Low

### Public prior I would have adopted

Current public benchmark data exists for other Astra configurations, including much stronger/max variants, but that is not an apples-to-apples comparison with the observed **Astra Low** workflow.

### Personal evidence

The Margins implementation experience showed that a giant Astra Low task could consume roughly 12 hours across multiple usage windows. The owner later found Astra more attractive as a reviewer/orchestrator.

### Relationship

**Not safely comparable to public Astra Max results.**

The personal lesson is about **role fit and quota economics**, not a claim that the Astra family is weak.

This distinction should remain explicit.

## 5. Claude for governance/reviewer work

### Public prior I would have adopted

Public model rankings tend to emphasize coding, reasoning, or general intelligence. They provide much weaker direct measurement of authority design, theological/content governance, or whether an AI correctly separates authorship from gating.

Anthropic's own workflow guidance commonly positions stronger models for planning and harder judgment while cheaper models can carry daily execution.

### Personal evidence

The Bible project bake-off favored Claude for a governance decision because it separated:

- Sacred Event Protection review;
- content authorship;
- historical/material-culture research;
- deterministic formatting.

That is a role-design judgment, not a raw coding result.

### Relationship

**Broadly consistent with public role guidance, but personal evidence measures a dimension benchmarks barely cover.**

## 6. Tripo 3D

### Public prior I would have adopted

Current Tripo documentation advertises:

- quad output;
- smart low-poly generation;
- explicit face limits;
- retopology;
- improved production-oriented mesh models.

Recent community reports say topology has improved substantially, including cases where generated meshes need much less rebuilding than older tools.

At the same time, both official production guidance and community workflows still show Blender/DCC cleanup, rigging, engine validation, and manual fixes as normal parts of game-asset production.

### Personal evidence

Margins independently converged on:

> generate → inspect → Blender cleanup/normalization → downstream material/engine validation → measure → update standards.

The user also rejected visually poor outputs and moved toward more concrete shape/construction prompting rather than generic style adjectives.

### Relationship

**Strongly confirms the practical public workflow, with one update: newer Tripo generations may deserve less pessimistic assumptions about topology than older experience did.**

The repository should continue measuring actual outputs rather than freezing the tool's 2025/early-2026 limitations into permanent rules.

## 7. Mission-oriented prompts and repository context

### Public prior I would have adopted

Older coding-agent advice often favored relatively bounded issue-sized tasks and detailed task descriptions.

More recent agent-engineering guidance has shifted toward repository-native context and stronger autonomy.

OpenAI's harness-engineering write-up explicitly says to give Codex **a map, not a 1,000-page instruction manual**: keep `AGENTS.md` short and put deeper source-of-truth material in structured repository documentation.

Anthropic's context-engineering guidance similarly emphasizes just-in-time environment navigation and increasing model autonomy as capabilities improve.

### Personal evidence

Agentic AI and Modular CRM independently converged on the same pattern:

- detailed truth in repository docs;
- compact task prompt;
- mission;
- hard guardrails;
- useful references;
- permission to make routine engineering decisions;
- genuine-blocker-only escalation.

### Relationship

**The personal evidence strongly confirms the newer public agent-engineering direction and contradicts the older habit of copying the whole specification into every task prompt.**

This is one of the strongest places where the owner's empirical workflow is not merely anecdotal; it lines up with how frontier-agent teams now describe their own repositories.

## 8. Human review and playtesting

### Public prior I would have adopted

Coding benchmarks reward task resolution, tests, and verifier success. They increasingly include long-horizon repository work, but they still cannot fully measure whether a product feels coherent to its owner.

### Personal evidence

Margins and Folio repeatedly found issues after technically successful implementation:

- workflow dead ends;
- confusing UX;
- incorrect product assumptions;
- poor visual choices;
- gaps that tests did not capture.

### Relationship

**Adds a dimension benchmarks structurally under-measure.**

The personal corpus should keep human use as a separate acceptance layer rather than treating benchmark-style verification as final.

## Bottom line

If I had relied mostly on public benchmarks before seeing this history, my prior routing would have been roughly:

1. highest coding-agent score for the hardest coding task;
2. cheaper frontier model for routine coding;
3. Claude/Opus for difficult reasoning;
4. Tripo for fast 3D generation with expected cleanup.

The personal corpus changes that into a more useful routing model:

1. choose by **task bottleneck and harness**, not model prestige;
2. spend Sol-level quota where long-horizon integration justifies it;
3. use Terra-level capability aggressively for bounded implementation when it performs well in the actual repo;
4. use strong independent models for review/governance;
5. prefer live-environment MCP access for environment-integration tasks;
6. treat quota/time/human-attention as performance metrics;
7. keep product playtesting outside the automated-verification score;
8. treat public benchmark rankings as priors that the personal corpus is allowed to override.

## Sources to re-check on future updates

Public benchmarks move quickly. Future agents should reverify:

- Artificial Analysis Coding Agent Index and methodology;
- current provider eval pages for the exact model/configuration;
- benchmark version changes such as Terminal-Bench;
- current community reports only when workflow sentiment is useful;
- current Tripo generation/retopology documentation.

Do not preserve numeric leaderboard claims indefinitely without a date and benchmark version.
