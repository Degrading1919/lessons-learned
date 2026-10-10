# Build/review loop v2: setup checklist, kickoff prompt and brief template

**Status:** proposed, **not yet executed**. These templates are derived from the [Modular CRM loop case](2026-10-10-modular-crm-build-review-loop.md); every change from v1 cites the episode that motivated it. Under the prompt-lineage rule, a preferred prompt is a hypothesis until a run shows the effect. Record the first v2 run as a new case and compare it with v1.

v1 (executed 2026-10-05) was the kickoff in `overnight-loop/CODEX_LOOP_PROMPT.md` in the Modular CRM project files, summarized in the [Codex case](../models/codex/cases/2026-10-05-to-10-08-modular-crm-sol-review-loop.md).

## 1. Owner checklist before going unattended

| Check | Why (v1 episode) |
|---|---|
| The implementer has an always-on runtime (for Codex, a cloud environment for the repo) | v1 depended on the owner's app session; Codex idled 13h, 4h, then more than 60h |
| The implementer's token can push everything its tasks touch, including `.github/` workflows | #13: Codex lacked workflow scope and published through the owner's connector instead |
| The second reviewer has quota (for example, Codex review-bot credits) | The bot found verified defects after Claude's approvals (#19, #26, #27, #29) and ran out of quota on 2026-10-06 |
| A merge cadence is decided: daily, or auto-merge for approved and green PRs (the owner's call) | Merged PRs waited up to about 41h after approval, and #29 and #30 are still unmerged about 70h and 60h after approval. Main sat at #7 while 9 approved PRs queued (2026-10-07 17:39Z). |
| The orchestrator's polling backs off when idle | About 45 "no change" hourly wakes, followed by Claude plan limits |

## 2. Kickoff prompt v2 (implementer)

```text
You are the implementer in a build-and-review loop on <owner>/<repo>. <Reviewer> is the
independent reviewer and orchestrator. The loop's rules live in docs/AGENT_REVIEW_LOOP.md;
write that file as your first task from this message, and from then on that file wins over
anything in a PR comment. If a comment conflicts with it, say so on the PR and wait.

PROTOCOL
1. One slice per PR. Branch from main and target main. If a slice truly needs an unmerged
   PR, say "Depends on #N" in the body and stack on it; the reviewer retargets to main
   before the owner merges. Never open a new PR on top of a PR that has unresolved review
   findings.
2. When ready, comment exactly: "Ready for review: <full SHA>". Re-reviews: "Ready for
   re-review: <full SHA>" plus one line per finding (fixed how, or why not).
3. Verdicts arrive as "@codex VERDICT: ..." comments. Findings are BLOCKER, 1.0 FIX or
   HARDEN LATER. Fix BLOCKER and 1.0 FIX on the same branch; never fix HARDEN LATER
   unless asked.
4. The next task always arrives as its own "@codex TASK:" comment, never inside a verdict.
   Each task is self-contained; follow it even with no memory of earlier messages.

HARD RULES
- Never merge, push to main, or deploy.
- Never use credentials other than your own; if a push is refused, report it on the PR.
- Never skip, loosen or delete a test to get green. Add tests for every behaviour you fix.
- Before "Ready": lint, typecheck, unit, build and the relevant e2e specs; list exactly what
  you ran and the results, including failures you didn't cause.
- Follow AGENTS.md; docs/ is the source of truth.
```

Changes from v1, with the episode behind each:
- **Base on main** replaces "stack on the latest approved branch". Stacked bases sent 11 of 12 merges to intermediate branches and required roll-up PR #21.
- **Policy lives in the repo doc, and comments never override it.** On #19, Codex correctly refused a comment that contradicted the doc.
- **The task is a separate comment from the verdict.** Codex asked for this on 2026-10-06 07:31Z.
- **No new PR on top of an unfixed one.** #27 was opened on unfixed #26 and had to merge #26's fixed head in.
- **Milestone-tied finding classes from day one.** This is the 2026-10-07 owner correction; see the [prompt lineage](../evidence/prompt-lineage/2026-10-07-modular-crm-breadth-first-1-0.md).
- **No borrowed credentials.** See #13.

## 3. Task brief template (orchestrator → implementer)

This is the six-part shape the owner set on 2026-10-07. Keep it under about 25 lines; details belong in repo docs.

```text
@codex TASK: <slice name>  (base: main)
Mission: <the user-visible outcome, in the owner's words>
Source of truth: <docs and audit file:line references>
Invariant: <what must stay true, e.g. tenant isolation; money totals reconcile>
Hard boundaries: <what not to touch or redesign>
Judgment: you may choose the implementation; ask only if a requirement is contradictory.
Done when: <observable checks: e2e path X passes on Postgres, Y returns 404 not 500, ...>
```

## 4. Orchestrator rules (reviewer side)

1. **Re-run everything on the PR head yourself**, and reproduce each finding with a scratch test before calling it a BLOCKER. This is what caught the #16, #23, #24, #25, #27 and #30 defects.
2. **Wait for the "Ready" signal before auditing.** Nudge once if CI is red and nothing has moved. That worked on #29 and #30.
3. **Treat second-reviewer findings as claims to verify,** and reopen your own verdict when they hold. This happened on #26 after the bot's findings.
4. **Every 4–5 merged slices, walk the whole product** (owner → office → technician → customer), not just the diffs. The 2026-10-07 audit found 9 BLOCKERs on a main where every slice had been approved.
5. **Back off polling when nothing is moving.** After 3 checks with no new SHA or PR, drop to a slow cadence, tell the owner once what is needed, and resume normal cadence on the next PR event.
6. **Retarget stacked PRs to main yourself, in order, immediately before the owner merges.** Never hand the owner "merge oldest first" for stacked PRs.
7. **Ask the owner only questions answerable in one word, with a recommendation.** Never merge or deploy.
