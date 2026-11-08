# Creative writing and canon fidelity — public model baseline

**As of:** 2026-11-01 (historical snapshot; see November 8 update)  
**Status:** Public research prior, NOT a Caelmor model bake-off or owner-observed result  
**Scope:** Fantasy lore, narrative structure, NPC conversations, atmospheric prose, and revision against Caelmor canon.

> **Current evidence update (2026-11-08):** The reported Opus 5.5 behavioral shift is unproven as a model-capability regression, but deserves a matched High/XHigh test. Gemini 4 Argon is now broadly accessible and is a first-line independent prose challenger. See the [Opus regression and narrative-options assessment](2026-11-08-opus-5-5-regression-and-caelmor-options.md) before treating this November 1 candidate order as current.

## Executive finding

**First candidate: Claude Opus 5.5 (High).** The strongest directly human-rated public signal favors it, with corroborating reports of improved scene-state tracking and style-rule adherence. **Primary challenger: GPT-6 Astra (High)**, which leads EQ-Bench's model-judged short creative-writing benchmark. **Literary specialist challengers: Claude Fable 5.1 (High) and Claude Opus 5 (High/XHigh)**, strong in constrained short stories and longform; Fable availability depends on the user's actual surfaces. **External cross-family challenger: Gemini 4 Argon (High)** if accessible; human Arena results are strong, but EQ-Bench's model-judged result is weaker. None is yet proven best for Caelmor's canon-grounded work.

Do not route the whole narrative pipeline to the model with the highest generic intelligence score. Prefer a prose author, independent canon checker, and director approval. Work/computer-use capability is an *environment affordance*, not evidence of better writing.

## Independent and human-preference evidence

Source values are snapshots, not stable ranks; benchmarks use different prompts, judges, model effort levels, and rating scales. Do not combine numerical scores across benchmarks.

| Benchmark and procedure | Selected results as retrieved | Interpretation and limits |
|---|---|---|
| [Arena Creative Writing](https://arena.ai/leaderboard/chat/text/creative-writing), **2026-10-27**; blind pairwise **human choices** | Opus 5.5 High **1520 ±13** (2,672 votes); Gemini 4 Argon High **1517 ±13** (2,720); Gemini 4 Carbon High **1515 ±20** (990, preliminary); Claude Fable 5 High **1501 ±7** (9,760); Fable 5.1 Max **1489 ±11** (3,884); GPT-6 Astra Max **1450 ±11** (3,323) | Most direct large-scale human taste signal. Near-top intervals overlap. Creative-writing subset has narrower coverage than full vote count shown on site. Model effort differs; preferences are not constrained to Caelmor lore. |
| [Lech Mazur short-story benchmark](https://github.com/lechmazur/writing), retrieved 2026-11-01; matched 600–800-word stories with **ten compulsory elements**, model judges and order swaps | Fable 5.1 High **3.745** (95% bootstrap **3.663–3.829**); Opus 5.5 High **3.693** (**3.586–3.776**); Opus 5 XHigh **3.685** (**3.635–3.735**); Astra High **3.416** (**3.355–3.494**) | Strong test of integrating disparate story constraints; top three intervals overlap. **Model-judged, not human-rated**; curated combinable prompts, not long-running world-bible continuity. Results are relative within this pool. |
| [EQ-Bench Creative Writing v3](https://eqbench.com/creative_writing.html), retrieved 2026-11-01; 32 prompts × 3 generations, rubric + model-judged pairwise rating | Astra **2174**; Fable 5.1 **2162.7**; Opus 5 **2133.5**; GPT-6 Sol **2124.6**; Opus 5.5 **2050.8**; Gemini 4 Argon **1758** | Astra leads a substantially different writing evaluation. [Method](https://eqbench.com/about.html): pairwise judge Opus 5; rubric judge GLM 5.3; known judge style/self-bias and 4,000-character truncation. Not a measure of canon accuracy or conversation choices. |
| [EQ-Bench Longform Writing](https://eqbench.com/creative_writing_longform.html), retrieved 2026-11-01; plan/revise/write over eight ~1k-word turns, judged by Claude Sonnet 4.6 | Opus 5 **86.3**; Fable 5.1 **85.3**; Opus 5.5 **84.6**; Astra **82.8**; GPT-6 Sol **82.8** | More relevant to multi-scene cohesion than a single scene, though LLM-judged and short of novel-length; scores are not cross-compatible with v3 Elo. |

**Evidence reconciliation:** Human preference points first to Opus 5.5; EQ-Bench short form to Astra; constrained-story comparisons to Fable/Opus; longform to Opus 5. No evidence establishes a universal best writer. The disagreement is a reason to test Caelmor tasks—not to average rankings.

## Human field reports (self-selected; not controlled model tests)

- [GPT-6 Astra writing report](https://www.reddit.com/r/WritingWithAI/comments/1wbfc18/chatgpt6_astra_high_on_creative_writing/), 2026-09-09: author praises distinctive voices, dialogue flow, and grounded impact; a positive single-case impression, not a cross-model assessment.
- [Opus 5.5 fiction report](https://www.reddit.com/r/ClaudeAIJailbreak/comments/1wnmbfx/opus_55_writing_is_peak_surpassing_46/), 2026-09-22: author reports warmer prose and better scene object/timeline state tracking; early release enthusiasm, not independent validation.
- [Opus 5.5 rules/continuity report](https://www.reddit.com/r/claudexplorers/comments/1wxhppk/it_just_occurred_to_me_that_opus_55_actually/), 2026-10-04: reports sustained banned-phrase/style compliance through several chapters; one commenter reports **Fable 5.1** held their lore restrictions better than Opus 5.5. Directly relevant hypothesis for Caelmor's canon constraints.
- [Fable 5.1 disagreement](https://www.reddit.com/r/ClaudeAI/comments/1w6gtgx/fable_vs_fable_51_for_creative_writing/), 2026-09-03: one user describes more natural style and fewer edits; another reports severe continuity and editing failures on a 95,000-word manuscript. Both are unverified individual experiences; do not report a consensus.
- [Sonnet 5.5 concerns](https://www.reddit.com/r/claudexplorers/comments/1x67arn/sonnet_55s_writing/), 2026-10-15: writer complains of incoherent character actions and spatial descriptions; others prefer Opus 5.5. Useful counter-signal, not evidence Sonnet cannot write.
- [Opus 5.5 style disagreement](https://news.ycombinator.com/item?id=49803892): favorable comparisons with Astra and praise for clarity coexist with strong complaints about excess verbosity. Test restraint directly.

**Caveat:** These reports are self-selected and often lack exact prompts, settings, full outputs, verification, or systematic paired comparisons. Avoid treating popularity/upvotes or vivid anecdotes as a quality score.

## Caelmor-specific model candidates

| Candidate | Proposed role to test | Main hypothesis | Main failure to probe | Public-prior confidence |
|---|---|---|---|---|
| **Claude Opus 5.5 High** | First-pass lore prose, scenes, NPC conversations | High human-rated writing, continuity, natural dialogue | Flowery exposition, invention beyond supplied canon, style drift | **Medium-high for prose; untested for Caelmor canon** |
| **GPT-6 Astra High** | Independent author and high-judgment narrative critic | Excellent creative v3 performance and strong stylistic potential | Overwriting, unsolicited world additions, high usage cost | **Medium for prose; untested canon** |
| **Claude Fable 5.1 High** | Canon-constrained longform/structural challenger, if available | Strong constrained short-story integration | Subtle continuity slips and editorial overcorrection reported | **Medium; access uncertain** |
| **Claude Opus 5 High/XHigh** | Literary comparison anchor, if available | Leading longform and strong short-story result | Mannered prose/repetition; potentially poor cost | **Medium; access uncertain** |
| **Gemini 4 Argon High** | Cross-provider challenger, if accessible | Near-lead human-rated prose | Uneven model-judged creative result; restricted availability | **Medium for writing, low for access** |
| **Claude Sonnet 5.5** | Lower-cost revision/dialogue worker candidate | Accessible capable drafting | Scene logic, constraint drift, weak artistic differentiation | **Low-medium for this role** |
| **GPT-6.1 Sol** | Lower-cost structural reviewer/assistant comparator | Strong general reasoning and repo work | Lower creative Arena preference than leaders | **Low-medium for literary authorship** |

Model availability in desktop Work modes and exact effort settings must be confirmed per run; never assume a named model, API mode, or toolset is available merely because the subscription exists. Opus 5.5 is the **first test**, not a certified winner.

## What public benchmarks do not establish

No cited benchmark proves that a model can take Caelmor's authoritative, occasionally conflicting documents and produce **correct, atmospheric, coherent, lore-safe** quests and branching conversations over repeated revisions. Lexical style, constrained narrative structure, context retention, factual/canon retrieval, and player-facing readability are different skills.

In Caelmor, grounded restraint is non-negotiable. Quiet implication, consequences, regional voice, and consistent chronology matter more than elaborate language. A beautiful contradiction loses to a less beautiful but valid draft. A model should distinguish approved fact, source-backed inference, candidate proposal, and unresolved question. Missing lore is not a license to silently create canon.

## Provisional routing decision

**Public baseline:** Begin head-to-head testing with **Opus 5.5 High** and **GPT-6 Astra High**; add **Fable 5.1 High** or **Opus 5** if the exact model is available, and **Gemini 4 Argon** for an external comparator if accessible. Use Claude or ChatGPT Desktop Work where source retrieval and file work are needed, but record **model + effort + harness + attached files/tools** independently.

**No real Caelmor output was generated or graded in this research.** This is not a personal case, preference pair, model selection lock, license to retcon canon, or reason to fine-tune a local model yet.

See [Caelmor narrative bake-off protocol](../writing/CAELMOR_NARRATIVE_EVAL_PROTOCOL.md) for tasks, acceptance gates, and data capture.