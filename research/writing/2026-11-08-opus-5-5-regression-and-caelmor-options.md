# Opus 5.5 behavior controversy and Caelmor narrative routing

**As of:** 2026-11-08  
**Evidence class:** public/researched prior; NOT an owner-executed model bake-off or verified Caelmor regression  
**Decision:** keep Opus 5.5 in the candidate set, establish an XHigh/clean-session diagnostic, and blind-test non-Anthropic prose challengers. Do not write speculative model drift into Caelmor canon.

## What prompted this update

Reddit and X posts in early November assert that Claude Opus 5.5 became less capable, more repetitive, less attentive to instructions and less deliberate around October 23–November 3. This matters to Caelmor because the owner uses Opus for lore and quests and the [November 1 public narrative baseline](2026-11-01-caelmor-creative-writing-model-baseline.md) selected Opus 5.5 High as the first candidate.

A **change in user-visible behavior** is not the same claim as a **change in the underlying model weights**, nor does a coding failure imply a fiction-writing regression. Separate the claims.

## Evidence on the purported "nerf"

| Source and time | Finding | What it does and does not prove |
|---|---|---|
| [Shane Melaugh Nov. 8 account analysis](https://x.com/shanemelaugh/status/2119192075505893695), [readable recap](https://herald.jaaaames.com/) | About 1,400 Claude Code sessions examined. Claimed shift November 3 in visible thinking style; 14,560 pre-/14,871 post-change turns, median upfront thinking **84 → 54 tokens** at High (−36%), and a +47% relative script/edit crash index. A **single** debugging A/B reported High failing after 160 turns/$13 and XHigh solving in 5 turns/$0.85. | Useful observational lead, especially about High vs XHigh. No released matched prose outputs, no blinded canon accuracy comparison, no independent reproduction of the session analysis, and workload/serving/context confounders remain. A single bug is not a population estimate. |
| [Reddit complaint Nov. 5](https://www.reddit.com/r/ClaudeCode/comments/1xodr56/opus_55_is_definitely_getting_dumber_and_costlier/), [other complaint Nov. 2](https://www.reddit.com/r/ClaudeCode/comments/1xm57dz/is_it_just_me_or_did_opus_55_get_heavily_nerfed/), [Nov. 8 broad repost](https://www.reddit.com/r/claude/comments/1xql02s/is_opus_55_nerfed/) | Multiple users report repeated rejected approaches, partial completion and lower apparent reasoning. Others in the **same** threads report no change, including at high request volumes. | A real cluster of perceived quality problems; self-selected posts and reposts of the **same** experiment are not independent measurements or a countable consensus. |
| [LiveNerf, updated Nov. 8](https://github.com/ninjahawk/livenerf) | Pre-registered, pinned Claude Code CLI and harness; 46 days/90 samples per day. Three complete post-baseline 10-day windows found **no significant broad accuracy decrease**. Third window (days 31–40) scored +2.8 ± 2.3 percentage points relative to launch baseline. | Strong contrary evidence against a large *general* model regression through approximately Nov. 2, on its measured knowledge/math panel. November 3 onward falls in the still-incomplete days 41–50 window. A subtle effect, account-specific behavior, tool use, creative style or canon fidelity can evade this test. Detection power and ambiguous items are documented limitations. |
| [Nov. 8 independent user log analysis](https://www.reddit.com/r/ClaudeCode/comments/1xr66pd/i_dont_think_opus_55_was_nerfed_theyre_just/) | Author reports account-level serving experiment identifiers and a 20-request replay: replies with multiple tool calls 7 → 17 under one experiment. No established task-quality delta. | Suggests harness/serving behavior may vary even while model ID stays fixed; **not** an official Anthropic confirmation or a proven cause of the broader complaints. |
| [Anthropic thinking documentation](https://platform.claude.com/docs/en/build-with-claude/thinking) | Visible `thinking` content is a **summary**, not the model's raw chain of thought; summary behavior can change independently. Billed thinking tokens and displayed text are not interchangeable measures. | Changes in phrasing or visible "I'm / I should" frequencies do not establish shorter or worse hidden reasoning. Request usage counters and final-task results are better diagnostics. |
| [Anthropic Opus 5.5 migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide), [effort settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings) | Opus 5.5 defaults to **Medium** on API when effort is unspecified, versus Opus 5 High. Effort is configurable; XHigh provides deeper reasoning at higher cost. | An omitted/changed effort setting can produce an apparent regression. It does **not** prove that High was secretly lowered on November 3. |
| [Claude Code project effort bug report](https://github.com/anthropics/claude-code/issues/106126) | A user reported October 30 removal of an effort selector and a coordinator using Opus 5.5 Low in Claude Code Projects. | Surface-specific issue report; do not generalize to ordinary Claude Chat, API, or every Claude Code session. |
| [Anthropic April 23 postmortem](https://www.anthropic.com/research/april-23-postmortem) | Anthropic previously traced real Claude Code quality degradation to lower default effort, lost thinking history and system-prompt changes, with unchanged API/weights. | Establishes a *documented mechanism and precedent*, not an admission about November. |
| [Anthropic official service status](https://anthropic.statuspage.io/history) | No publicly listed Nov. 1–8 incident for model quality as of this review. | Status reports track incidents, not every routing/serving or quality experiment. Absence of an incident is not disproof. |

### Verdict

**Confidence in a visible Claude Code behavior shift: moderate.**  
**Confidence in an Opus 5.5 raw-weight/general-capability nerf: low / unproven.**  
**Confidence in a specifically degraded Caelmor narrative-writing capability: unknown until matched owner tests.**

The most useful immediate diagnostic is not "switch permanently to another provider." It is **Opus 5.5 High versus XHigh, new isolated context versus the existing lore session**, with identical source packets and blind output review. If a recent High failure reproduces while XHigh passes, consider XHigh for difficult quest causality/canon synthesis, but do not infer XHigh is aesthetically superior for every dialogue line.

## Did Anthropic change other models?

**Verified product changes:**

- [Claude Haiku 5.5 launched October 7](https://www.anthropic.com/claude-haiku-5-5): a genuine new model, 1M context, low-cost retrieval/classification/subagent role, not a silent change to Opus.
- [Haiku 4.5 was removed from the Claude Chat/Cowork/Design Free/Pro/Max model selector October 29](https://support.claude.com/en/articles/17444146-claude-haiku-4-5-was-removed-from-the-model-selector). Continuing older Haiku 4.5 chats now runs Haiku 5.5, although 4.5 remains available in Claude Code/API and some plans. This is a **documented model switch**, easily misread as a behavior regression.
- [Sonnet 5.5 cache reads were repriced October 7](https://www.anthropic.com/claude-haiku-5-5) from $0.20 to $0.10 per million tokens. Price change, not evidence of weakened weights.
- The [Opus 5.5 fallback policy](https://support.claude.com/en/articles/16049681-why-claude-switched-models-in-your-conversation-with-opus-5-or-opus-5-5) can switch narrow sensitive requests to Opus 5; ordinary fantasy writing is **not** a known trigger.

**Not established:** a November cross-family capability reduction in Sonnet 5.5, Fable 5.1, or Haiku 5.5. There are individual complaints, but no comparable date-matched public demonstration. Do not infer an all-Claude nerf from primarily Opus/Claude Code anecdotes.

## Narrative-specific evidence as of November 8

### Human preference versus model-judged writing

| Test | Signal | Limitation |
|---|---|---|
| [Arena Creative Writing, November 8](https://arena.ai/leaderboard/chat/text/creative-writing) | Gemini **4 Argon High 1526 ±10** (4,517 votes); **Opus 5.5 High 1517 ±12** (3,562); **Fable 5 High 1501 ±7** (9,853); **Opus 4.6 High 1498 ±6** (15,614). Opus 5.5 and Argon confidence intervals overlap. | Blind human taste on open prompts; not canon-constrained Caelmor quests. Older Opus remains a plausible style challenger, not a presumed capability winner. |
| [EQ-Bench Creative Writing v3](https://eqbench.com/creative_writing.html) | GPT-6 Astra ~2174 Elo, Fable 5.1 ~2163, Opus 5 ~2134, Opus 5.5 ~2051; newer third-party snapshots place Kimi K3.1 Pro near Astra. | LLM pairwise judge/style preferences, short form, judge bias; not comparable numerically to Arena. |
| [EQ-Bench Longform Writing](https://eqbench.com/creative_writing_longform.html) | Opus 5 ~86.3, Fable 5.1 ~85.3, Opus 5.5 ~84.6, Astra ~82.8 in the retrieved v1.11 snapshot. | Eight-part novella, LLM judged; not dozens of persistent quests with branching/player-state semantics. |
| [Lech Mazur constrained-story benchmark](https://github.com/lechmazur/writing) | Fable 5.1 and Opus 5.5 are very strong at integrating ten mandatory story elements. | Short model-judged stories; constraint integration is relevant to lore, but not proof of source attribution/canon fidelity. |
| [September Opus 5.5 writing-effort comparison](https://www.reddit.com/r/ClaudeAI/comments/1wr03jc/55_is_insane_it_almost_broke_our_benchmark_i/) | An author reported marked writing-quality gains from Medium to High/XHigh/Max, with sharply increasing cost and time. | Private scriptwriting benchmark from launch week; evidence that effort matters, not a current controlled Caelmor result. |

These benchmarks **disagree**. This is useful: human-pleasing prose, short-story rubric achievement, longform coherence, and canon-safe NPC/quest implementation are distinct tasks.

### Current candidates for Caelmor

| Candidate | Specific role worth testing | Strength or risk | Priority |
|---|---|---|---|
| **Claude Opus 5.5 High / XHigh** | Existing lore author; High→XHigh troubleshooting/quest-structure check | Proven market-level human prose preference, owner continuity; disputed late-2026 behavior; XHigh cost | **Keep as incumbent and diagnostic arm** |
| **Gemini 4 Argon High** | True independent author for atmospheric lore and NPC dialogue | Now [generally accessible since Oct. 13](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/), top human writing vote snapshot; test over-resolving mysteries and invented canon | **Highest-priority external prose challenger** |
| **Claude Fable 5.1 High** | Complex intertwined quests, region chronologies, revision under conflicting canon | Strong constrained/longform metrics; high cost and availability dependent | **High-priority narrative-structure challenger** |
| **GPT-6 Astra High** | Original independent lore author / prose and choice critic | Leads EQ-Bench v3; much weaker human Arena placement, high quota cost; risk of purple prose or unsolicited lore | **Independent style challenger** |
| **Claude Opus 5 or 4.6** | Literary benchmark/control; especially continuity with favored historical Claude voice | Strong longform or human taste; older API/surface availability and cost vary | **Optional stability/control arm** |
| **Kimi K3.1 Pro** | Exploratory independent story ideation/prose | [Officially available](https://www.kimi.com/en/blog/kimi-k3-1-pro); strong recent model-judged creative result but limited Caelmor-specific/human preference evidence | **Optional dark horse** |
| **Claude Sonnet 5.5 Medium/High** | Economical dialogue variants, quest-log copy, polish after director approval | Strong general implementation; lower Arena prose preference; narrative causality/voice must be checked | **Production worker only if pilot passes** |
| **Claude Haiku 5.5** | Extract approved facts/flags, route materials, produce candidate metadata | Very cheap under 100k-token prompts; not a final writer/canon authority | **Utility, not primary author** |
| **GPT-6.1 Sol** | Quest dependency and source-checking assistant | Strong reasoning/cost; lower human prose preference, should not be chosen as aesthetic lead | **Structure/review candidate** |

### Key style/context risk

The owner values Caelmor writing that feels **lived-in, restrained, regional, quietly mythic, spatially and temporally coherent**. It should not read like an encyclopedic lore dump, self-consciously purple fantasy prose, or modern quest-marker copy.

The greatest failure is not an imperfect metaphor; it is **smuggling invented facts into approved canon**, solving a mystery too quickly, violating player agency, or silently retconning a source conflict. A beautiful false fact is still a failure.

For player-facing quests, separate:

1. **Narrative architecture:** motive, stakes, clue fairness, choice consequences, pacing, player agency.
2. **Authorship:** place, voice, dialogue, implication, atmosphere.
3. **Canon/source validation:** every asserted fact grounded to an approved source, or clearly flagged as a new proposal.
4. **Creative Director approval:** independent of any model-generated score.

This is role separation, not a mandatory multi-agent fanout. A single model can do successive steps when time/quota makes that sensible, but the **canon gate must be separately checked**.

## Practical decision and next test

Do not change Caelmor's permanent writer from Reddit sentiment alone.

Run the [existing narrative evaluation](CAELMOR_NARRATIVE_EVAL_PROTOCOL.md) with a fast diagnostic stage before a full 8–12-pair bake-off.

**Stage A: investigate the alleged Opus change**

- Select an archived, already approved pre-November Opus lore/quest sample and its exact source packet, if available.
- In a new conversation with the same approved files and frozen prompt, run Opus 5.5 **High** and **XHigh**. Record platform, actual model label, effort, date, model selector status, context source hash, cost, and visible reasoning usage *when exposed*. Keep the existing long-session output as an **unmatched** reference if the original inputs cannot be reconstructed.
- If practical, run one matched API request and one Claude app request. Do not assume a Claude Code tool/effort behavior anomaly also occurs in Claude Chat.
- Blindly rate outputs on tone, canon, clue fairness, dialogue voice, pacing, agency, restraint, and revision fidelity. Compare exact canon violations before any stylistic preference.
- Do not use visible thinking summaries as a proxy for hidden thinking length. Count billed tokens separately.

**Stage B: replace/fill writing roles**

- Use identical, source-pinned Caelmor briefs with **Opus 5.5 High**, **Gemini 4 Argon High**, **GPT-6 Astra High**, and **Fable 5.1 High** (if accessible). Do not compensate one candidate with more source access or more tool abilities than another.
- Across lore microstory, NPC branches, quest structure, and canon conflict/revision tasks, preserve full outputs and record *director-blind* preference pairs.
- If Argon beats Opus on prose but loses canon fidelity, keep Argon for **proposals** and an independent canon checker as mandatory. If Fable wins difficult quest planning, route structure to it and prose to the preferred writer. If no challenger consistently wins, retain Opus with an XHigh escalation policy.
- Record accepted writing per quota, wall time, and human editing burden. Do not choose a winner by Elo alone.

**Recommended short-term operating choice:** Keep Opus 5.5 as the incumbent for already-in-progress Caelmor lore rather than disturbing continuity in the middle of a production phase. For the *next new* scene/quest, first run a clean **Opus High / Opus XHigh** comparison and **Argon High** challenger. Add Fable for especially intricate quest causality. Never approve model-generated canon without source verification.

## Evidence and source index

- [Previous Nov. 1 baseline](2026-11-01-caelmor-creative-writing-model-baseline.md)
- [Narrative evaluation protocol](CAELMOR_NARRATIVE_EVAL_PROTOCOL.md)
- [Opus 5.5 official default/effort](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- [Opus 5.5 migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)
- [Anthropic thinking summaries](https://platform.claude.com/docs/en/build-with-claude/thinking)
- [Anthropic April 23 quality postmortem](https://www.anthropic.com/research/april-23-postmortem)
- [LiveNerf daily record](https://github.com/ninjahawk/livenerf)
- [Nov. 8 Shane Melaugh analysis](https://x.com/shanemelaugh/status/2119192075505893695)
- [Server-experiment observational report](https://www.reddit.com/r/ClaudeCode/comments/1xr66pd/i_dont_think_opus_55_was_nerfed_theyre_just/)
- [Arena creative writing](https://arena.ai/leaderboard/chat/text/creative-writing)
- [EQ-Bench creative v3](https://eqbench.com/creative_writing.html)
- [EQ-Bench longform](https://eqbench.com/creative_writing_longform.html)
- [Constrained short-story benchmark](https://github.com/lechmazur/writing)
- [Gemini Argon worldwide release](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)
- [Haiku 5.5 release](https://www.anthropic.com/claude-haiku-5-5)
