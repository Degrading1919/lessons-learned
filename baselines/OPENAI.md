# OpenAI Baseline

_Last researched: 2026-09-22_

## Current routing summary

| Model | Baseline role | Strong suits | Main weaknesses / cautions |
|---|---|---|---|
| GPT-6 Astra | Hardest end-to-end, ambiguous, autonomous work | Frontier reasoning, long-horizon coding, computer use, professional artifacts, judgment under ambiguity | Very expensive/quota-heavy; reports of overengineering, inconsistent service quality, and poor value on ordinary tasks |
| GPT-5.6 Sol | High-end daily engineering / integration | Strong coding, debugging, architecture, research, agentic work | Can overthink/overbuild; much more quota than Terra/Luna; now below Astra/Fable on current frontier indexes |
| GPT-5.6 Terra | Balanced implementation workhorse | Strong bounded coding, everyday agent work, useful middle ground when prompt is imperfect | Public cost frontier is not always better than a neighboring Luna/Sol effort level; mixed forum opinion on whether the tier has a unique niche |
| GPT-5.6 Luna | Cheap high-volume executor | Extremely low price, fast, capable on clear tasks, background/subagent work | Less reliable for ambiguous architecture and difficult integration; benefits from strong planning/review |

## GPT-6 Astra

### Independent benchmark signal

Artificial Analysis currently places Astra at the frontier. On Intelligence Index v4.3 it scores **53**, tied with Claude Fable 5.1 and ahead of GPT-5.6 Sol at 47. Artificial Analysis also reports Astra on much of the intelligence-vs-cost-per-task Pareto frontier and says it ties Fable 5.1 on its Coding Agent Index at lower measured task cost.

Sources:

- https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3
- https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra

### Provider signal

OpenAI positions Astra as its hardest-work model: coding, computer use, browsing, professional work, research, science, and high-judgment autonomous execution.

Notable reported comparisons include:

- OSWorld 2.0: 72.6 vs Sol 65.7
- AutomationBench: 41.4 vs Sol 18.1
- BenchCAD: 95.9 vs Sol 83.3
- ExploitBench: 100 vs Sol 78.5

Astra has a 1.05M-token context window and API pricing of $10/M input and $50/M output.

Sources:

- https://openai.com/index/gpt-6-astra/
- https://developers.openai.com/api/docs/models/gpt-6-astra

### Human-review signal

Reddit sentiment is unusually consistent on one point: **Astra can be exceptional, but it burns allowance aggressively**.

Recurring positive themes:

- better at taking a vague “figure it out” task all the way through;
- stronger persistence and autonomous debugging;
- useful as architect/orchestrator on difficult work.

Recurring negative themes:

- quota can disappear extremely quickly in Codex;
- polling/subagent orchestration can create huge context burn;
- some users report overengineering small tasks;
- some report periods of degraded behavior where the model prematurely stops or handles only part of a specification.

Representative threads:

- https://www.reddit.com/r/codex/comments/1wciwc1/gpt6_astra_burns_quota_4_times_faster_than_gpt56/
- https://www.reddit.com/r/codex/comments/1wa9c9d/i_investigated_why_gpt6_astra_burns_quota_so_fast/
- https://www.reddit.com/r/codex/comments/1w8kj40/astra_is_amazing_but_truly_unaffordable_at/
- https://www.reddit.com/r/codex/comments/1whcb1h/gpt6_astra_seems_to_spend_most_of_the_time_in_a/

### Baseline prior

Use Astra when **failure to integrate the whole problem is more expensive than model usage**.

Do not default to Astra for routine feature work simply because it is the strongest OpenAI model.

---

## GPT-5.6 Sol

### Benchmark/provider signal

At launch, Sol led the then-current coding-agent benchmark with a reported score of 80. Under the newer v4.3 Intelligence Index it scores 47; that lower number is primarily a benchmark-version change, not evidence that the model literally lost 33 points of ability.

OpenAI positions Sol as the GPT-5.6 flagship for complex coding, knowledge work, cyber, and science.

Sources:

- https://openai.com/index/gpt-5-6/
- https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3

### Human-review signal

Strong reports emphasize:

- good ownership of well-structured repository work;
- strong complex debugging and architecture;
- usefulness as supervisor/orchestrator.

Negative reports emphasize:

- overthinking and enterprise-grade overengineering on small tasks;
- quota use at high reasoning;
- stronger need for repository ownership boundaries than older models;
- occasional claims of completion that require scrutiny.

Representative threads:

- https://www.reddit.com/r/codex/comments/1utzi5w/gpt56_sol_vs_terra_vs_luna_my_early_guide_to/
- https://www.reddit.com/r/codex/comments/1uysgci/i_have_never_been_gaslighted_this_much_by_any/
- https://www.reddit.com/r/codex/comments/1v5norf/gpt56_in_codex_may_have_the_same_token_pricing/

### Baseline prior

Strong default for difficult engineering when Astra is unnecessary or too expensive.

Best results should be expected when the repo has clear authority, ownership, and completion criteria.

---

## GPT-5.6 Terra

### Independent benchmark signal

On current Artificial Analysis v4.3, Terra Max scores **42**. At current public API pricing it is $2/M input and $12/M output.

Artificial Analysis reports Terra Max around $1.40 per Intelligence Index task, though adjacent model/effort combinations can be more cost-efficient.

Sources:

- https://artificialanalysis.ai/models/gpt-5-6-terra
- https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/

### Human-review signal

Forum opinion is split in an informative way.

Positive reports call Terra a strong daily coding driver, especially when the work is not perfectly specified and Luna would need a more carefully written handoff.

Critics argue that Terra can fall into an awkward middle: Luna at higher effort handles routine work more cheaply, while Sol at lower/medium effort handles hard work more reliably.

Representative threads:

- https://www.reddit.com/r/codex/comments/1vf3i0r/after_researching_gpt56_models_heres_the_simple/
- https://www.reddit.com/r/codex/comments/1v21pa4/does_anyone_even_use_gpt_56_terra/
- https://www.reddit.com/r/codex/comments/1us5y77/gpt_56_terra_a_record_for_future_degradations/

### Baseline prior

Tentative **daily implementation workhorse**, especially for moderately ambiguous tasks where Luna would require more planning overhead.

This is one model where the owner's own future evidence should matter more than generic Pareto charts.

---

## GPT-5.6 Luna

### Independent benchmark signal

Artificial Analysis currently reports:

- Luna Max: Intelligence Index **37**
- Luna High: around 32
- Luna Max output speed around 159 t/s
- current API price: $0.20/M input, $1.20/M output

That makes Luna unusually capable for its token price.

Sources:

- https://artificialanalysis.ai/models/gpt-5-6-luna
- https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/

### Human-review signal

Community reports increasingly treat Luna as more than a trivial-task model.

Positive themes:

- enormous subscription mileage after OpenAI's July quota/pricing change;
- capable of long unattended execution from a high-quality handoff;
- useful for review-fix loops and clearly defined implementation;
- excellent background/subagent economics.

Weakness themes:

- needs a better plan than Sol/Astra for ambiguous tasks;
- not the first choice for architecture or difficult cross-system judgment.

Representative threads:

- https://www.reddit.com/r/codex/comments/1vcqiwq/opus_5_approves_gpt_56_lunas_max_work/
- https://www.reddit.com/r/codex/comments/1vb12jt/chatgpt_codex_quota_update/
- https://www.reddit.com/r/codex/comments/1utzi5w/gpt56_sol_vs_terra_vs_luna_my_early_guide_to/

### Baseline prior

Use aggressively for **well-specified implementation, bulk work, subagents, monitors, review-fix loops, and tasks with cheap verification**.

A particularly promising pattern is:

> strong model plans/reviews → Luna executes.
