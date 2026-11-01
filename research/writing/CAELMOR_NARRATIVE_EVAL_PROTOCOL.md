# Caelmor lore, story, and dialogue — matched model evaluation protocol

**Created:** 2026-11-01  
**Status:** Proposed experiment; no observed runs or winner  
**Goal:** Select the best *practical setup* for writing Caelmor material without violating canon.

## Authority and inputs

Use current approved Caelmor sources, not recollection or a bundled snapshot presumed current. Freeze **the same repository commit**, relevant Phase 1 canon, relevant region dossiers, and current conflict notes across all compared runs. Record the exact source bundle/hash and any unresolved same-tier conflict before writing. If a task depends on a disputed fact, require the model to flag it rather than choose a side. Source packages must be identical across models.

Game canon and source constraints come from the Creative Director and current approved docs; **output is always proposal until approved**. Do not create production JSON, schemas, C#, or canon edits. World & Quest Designer creative work requires director brainstorming before a final deliverable; benchmark scenarios are explicitly hypothetical drafts for comparison, not approved game content.

## Candidate test matrix

Start with **Claude Opus 5.5 High** versus **GPT-6 Astra High**. Add **Claude Fable 5.1 High** or **Opus 5** if available; consider Gemini 4 Argon and a cheaper Sonnet/6.1 Sol worker. Keep **model, effort, and harness** separate. Compare Chat/desktop text-only separately from Work-with-repo access; do not confuse superior retrieval with superior base prose. Use the same prompt, source files, word budget, tool permissions, and revision turns.

## Four blind tasks (at least two seeds each)

1. **Lore microstory (350–550 words).** A grounded Lowmark scene told through mundane action and place, with three explicit canon anchors and two details that must *not* be assumed. Exposition should remain subtle, not spell out the world history.
2. **NPC conversation (12–20 exchanges).** Two region-grounded voices with different practical aims, player questions, and a meaningful branch that acknowledges the player's choices. Avoid modern slang, encyclopedic exposition, fake branching, and invented gameplay rewards.
3. **Quest design + excerpt.** An unusual but feasible solo-first local mystery, clue chain, fair resolution and two meaningful choices. Preserve the existing quest/system scope. Separate proposal from facts and do not assert invented NPCs as canon.
4. **Canon-conflict + revision challenge.** Plant a known forbidden inference and a genuine unresolved source conflict in the source packet. Require source-specific notes, abstention on disputed facts, then revise a scene based on one narrow director correction without losing earlier constraints.

Do not score the experiment until the director selects and freezes actual source-backed prompts; neither the model nor a judge may choose an easy test for itself.

## Scoring and gates

**Canon pass/fail gate before prose scores:** any material contradiction of locked canon, false attribution to an approved file, or unflagged resolution of disputed canon **fails**. Mark ungrounded embellishment as proposal versus established fact; do not penalize clearly labeled low-stakes original content merely for being new. Count invented hard facts, incorrect source claims, and missed conflicts separately.

For passes, score each dimension 1–5 with brief evidence:

| Dimension | Weight |
|---|---:|
| Tone and atmosphere: quiet, grounded, lived-in mythic setting | 20% |
| Distinct, convincing voices and natural dialogue | 20% |
| Narrative causality, subtext, spatial and temporal continuity | 20% |
| Discovery, agency, interesting local premise, useful player choice | 15% |
| Restraint: no purple prose, generic fantasy, or exposition dumping | 15% |
| Revision fidelity: changes only requested elements | 10% |

Canon is a **hard gate**, not a point bonus that pretty writing can offset.

Use director blind A/B preferences for *same-task outputs*; randomize candidate labels and swap display order where practical. A separate high-judgment model may issue structured criticisms, but it must **cite source text** for canon findings and is not a substitute for director preference. Do not use the producing model as sole judge. Report disagreements.

## Record and promotion

For each run preserve task ID, date, exact model/effort, Chat/Work/Claude harness, tools, source commit/hash, prompt and turn lineage, full output/reference, director's choice and reason, canon defects with citations, cost signal (quota/tokens/time if observed), and corrections/retries. Do not invent missing values.

Start with **8–12 matched task pairs** (minimum 2 prompts per task type) and repeated revision turns. If results are close, add more samples rather than declare a winner. Add personal cases to the existing corpus only after actual observed executions. Preference-pair records require both real outputs and the recorded preference. The key outcome is **accepted Caelmor writing per scarce unit of time/usage**, not leaderboard prestige.

A model may become preferred for one task and not another: e.g., lore guardrail critic, NPC dialogue writer, quest structure designer, prose editor. Keep human approval for canon.