# Case: Modular CRM — Claude as cross-model auditor, then lead orchestrator of a Codex build loop

- **Date:** 2026-10-04 to 2026-10-10
- **Project:** Modular CRM
- **Repository/artifact:** https://github.com/Degrading1919/modular-crm (PRs #3, #5, #6; Codex PRs #7–#19 and #22–#30; Claude's roll-up PR #21)
- **Model/tool:** Claude in a claude.ai Project: one coordinator session in the project chat, task-specific thread sessions in the cloud, Claude Code sessions on the owner's Windows machine via Remote Control, and Agent-tool subagents inside threads
- **Exact model/effort label:** loop thread recorded by the platform as `claude-opus-5-5`, effort `medium`, permission mode `auto`. The owner called the workflow "Sol → Opus". The model and effort for the Remote Control sessions (debugging pass, PR #5/#6 audits) were not recorded.
- **Task categories:** debugging, code review, orchestration, task design, release management, UX audit
- **Evidence:** Level A for the audit role (prompts, PRs, verification, owner signal and downstream merges). Level B for the orchestrator role (the loop stalled before the post-strategy-change slices could be measured).

## Objective

There were three phases:

1. **2026-10-04 (independent debugging and audit).** Find defects that survived Codex's own verification, then audit Codex PRs #5 and #6 without trusting the author's report.
2. **2026-10-05 to 10-07 (overnight loop).** The owner asked Claude to run an automated orchestrator overnight: watch Codex's output, audit it, and send fixes or the next prompt back to Codex, "and wake up to the CRM being completely ready to push to AWS". He later widened the goal to "the next best CRM since jobber... bug free, fully functional", adding that the overnight deadline "is a stretch, but its not literal".
3. **2026-10-07 19:02Z onward (lead orchestrator, breadth-first 1.0).** See [the prompt lineage](../../../evidence/prompt-lineage/2026-10-07-modular-crm-breadth-first-1-0.md).

## Starting context

- **Repository:** a mature `AGENTS.md`, with `docs/` as the source of truth, a decision-sync skill and a CI-less test suite. Main was at PR #2. Four stacked Codex branches (tip `codex/human-centered-ux`, about 35k lines, 152 Industry Packs) had never been merged.
- **Tools:**
  - GitHub through MCP, with comments posted from the owner's own account.
  - Hourly routines; a routine is the most frequent polling this platform allows.
  - PR-activity subscriptions.
  - A shared project folder for state files.
  - Remote Control onto the owner's machine, which runs PGlite and Mailpit with no Docker.
  - The cloud container. It can run real Postgres 16, start `dockerd` and run Playwright.
- **No ChatGPT/Codex connector.** The only channel to Codex was `@codex` PR comments.

## Prompt/tasking pattern

- **Owner → Claude, audit phase.** These were long, structured review prompts, for example the debugging-pass, P0-B and P0-C audit briefs. Each named the invariant to check, the specific risk areas, an explicit "do not trust the implementer's report" instruction, a verdict vocabulary (APPROVE / APPROVE WITH FOLLOW-UP / REQUEST CHANGES; BLOCKER / SHOULD FIX / FOLLOW-UP / NIT) and review-only boundaries.
- **Owner → Claude, loop phase.** The loop request was one paragraph. Claude chose the design (GitHub comments, approved PRs held for the owner) after asking two one-word questions: the channel (GitHub or the owner's PC) and whether to merge or hold.
- **Claude → Codex.** Claude wrote a kickoff prompt (summarized in the [Codex case](../../codex/cases/2026-10-05-to-10-08-modular-crm-sol-review-loop.md)). It defined the loop protocol, the hard rules (never merge, push to main or deploy; no test loosening; one slice per PR) and the first task. Codex was told to write the loop into `docs/AGENT_REVIEW_LOOP.md`, so later `@codex` comments could be self-contained.
- **Autonomy.** Claude acted without asking on reversible steps: verdicts, next tasks, retargeting PR bases and opening the roll-up PR #21. Merging and deploying stayed with the owner throughout.

## Output

- **Debugging pass** ([PR #3](https://github.com/Degrading1919/modular-crm/pull/3), Remote Control on the owner's machine). Four reproduced, root-caused defects, each with a failing-first regression test:
  - technicians could PATCH any ticket at their branch;
  - a PGlite connection-slot leak after abrupt disconnects;
  - 500s and silently saved invalid data on malformed record input;
  - identical signup retries were rejected as conflicts.
  - Test-harness fixes:
    - the web `test` glob ran no unit tests on macOS/Linux;
    - a month-boundary test failure;
    - a 1-in-64 tamper-test flake.
  - A parallel read-only cloud exploration thread passed the coordinator leads, explicitly labelled "leads to verify yourself, not conclusions". The local session then confirmed several of them.
- **Audits of Codex PRs [#5](https://github.com/Degrading1919/modular-crm/pull/5) and [#6](https://github.com/Degrading1919/modular-crm/pull/6).** Both started as REQUEST CHANGES with runtime-reproduced SHOULD FIXes:
  - #5: seeded Office could create business locations, and the Payments rows linked to a guaranteed 404;
  - #6: mileage overtook a failed clock-in in the offline queue, and re-publishing a route with a canceled stop was a dead end.
  - Both were approved after one fix round.
- **Overnight loop, 2026-10-05 03:24Z → 2026-10-08 05:22Z.** 22 Codex PRs (#7–#19, #22–#30) were audited. For each one Claude pulled the head and ran lint, typecheck, unit tests, build and Postgres Playwright itself, and often wrote a scratch reproduction. Verdicts were posted as `@codex` comments with the next task attached.
  - Defects Claude's audits caught before merge included:
    - an `X-Forwarded-For` spoof that allowed unlimited password guessing (#25 BLOCKER);
    - double collection when staff recorded a payment while a hosted checkout was open (#16). This was approved with the SHOULD FIX open and fixed in #17, before either PR reached main;
    - newly activated automations firing on old events (#24 BLOCKER, pre-existing but exposed);
    - a WAF rule that would have 403'd any large estimate or invoice (#27);
    - most invoices getting no due date, so overdue reminders never fired (#23);
    - multi-membership users landing in the wrong business after re-login (#30 BLOCKER).
  - Claude also root-caused a long-standing flaky technician test to PGlite interleaving protocol packets across clients (#18).
- **Release management.** When the owner's merges of stacked PRs #8–#18 landed on each other's branches instead of main, Claude detected it from main's history and opened roll-up [PR #21](https://github.com/Degrading1919/modular-crm/pull/21). It then retargeted #22–#28 to main mid-sequence while the owner merged; #19's changes reached main through #22. Main's final tip contained the audited #28 head.
- **1.0 plan (2026-10-07 19:05Z → 19:15Z).** Five parallel code audits (Agent subagents, one per product area) produced `PLAN_1_0.md`: 9 BLOCKERs with `file:line` evidence and a 14–18 PR wave plan, in about 10 minutes of wall time.
- **Communication artifacts.** Every PR outcome was mirrored to a state file (`LOOP_STATE.md`) and morning summaries (`MORNING_SUMMARY.md`), written in plain business language for the owner.

## Measured review performance

From GitHub data across the 22 Codex PRs ([review table](../../../evidence/review-logs/2026-10-10-modular-crm-pr-review-table.md)):
- **Speed:** median 0.74h from PR opened to Claude's first verdict, and 1.02h to final approval.
- **Findings:** 3 BLOCKERs and 18 SHOULD FIXes. 11 of the SHOULD FIXes were Claude's own; 7 were bot findings Claude verified and adopted.
- **Reversals:**
  - Claude reversed one approval after bot findings (#26).
  - It downgraded one approval after Codex pointed out the verdict contradicted itself (#19).
- **Bot findings after a standing Claude approval:** 10, on #7, #26, #27 and #29. Claude treated 8 as real and ruled 1 latent. The #7 finding was never acknowledged again.

## Verification

- Claude ran its own checks for every verdict rather than quoting CI or Codex's PR body. The loop state records the local unit counts and Postgres Playwright counts for each PR, from 47/47 on #9 to 87/87 on #30.
- Real Postgres 16, `dockerd` image builds and container smoke runs were executed in the cloud container. That surface does not exist on the owner's machine, which has no Docker.
- An independent reviewer outside Claude (the owner's own reviewer) checked PR #3 and found two correctness issues in Claude's fix. Details are under Failures below.

## Human signal

- PR #3 was approved by the owner's independent reviewer after one correction round, and merged.
- Overnight trust: "Do everything in your power to assure this CRM becomes the next best CRM since jobber... just a display in how much confident I have in you guys."
- The owner merged every Codex PR Claude approved through #28 (#7–#19, #22–#28), plus Claude's roll-up #21. This shows adoption, not correctness; see "What this does not prove".
- On 2026-10-07 he wrote that the "Sol → Opus workflow has been effective at producing increasingly robust code, but it has also encouraged deep hardening of individual slices and repeated expansion into adjacent edge cases". He then replaced the review philosophy (see the prompt lineage) and promoted Claude from auditor to lead orchestrator.

## Failures / corrections

1. **Claude's own fix was incomplete.** The independent review of PR #3 found that the new technician ticket rule dropped the location-scope check that `V1_PERMISSIONS.md` requires, and that the GET list and PATCH used different scopes. Claude's debugging pass had fixed one authorization hole and left an adjacent one.
2. **Claude caused the stacked-merge accident.** Claude's own kickoff prompt told Codex to branch each slice from the latest approved PR and set that branch as the PR base. Claude's morning summary then told the owner to "merge them oldest first" without warning that the bases would make the merges land on each other's branches. Result: of 12 merges, only #7 reached main, and a roll-up PR was needed. The same habit had already stranded the pre-loop `codex/*` stack (152 packs, still not on main).
3. **Claude gave contradictory instructions mid-stream.** After the accident Claude told Codex in a PR comment to base new PRs on main. Codex replied that this conflicted with the kickoff rule in the repo doc and that approved PRs can't be changed. Codex was right. Claude withdrew the instruction, and from then on retargeted stacked PRs to main itself before each merge.
4. **A second reviewer caught what Claude missed.**
   - Codex's own GitHub review bot found real problems after Claude had approved:
     - #26: four issues, including two regressions;
     - #27: a database snapshot restore that would fail (P1);
     - #19: three P2s;
     - #29: a login 404 on custom domains.
   - Claude verified each one and reopened its verdict instead of defending it.
5. **Polling burned quota while nothing happened (inferred cost).**
   - The hourly routine logged about 45 "no change" wakes between 2026-10-08 06:26Z and 2026-10-10 02:25Z.
   - The thread then spent hours waiting on the Claude plan's five-hour and seven-day usage limits. Retry notices filled the project chat from 2026-10-10 03:27Z to 15:31Z.
   - A five-hour-limit wait delayed the #30 re-review by about 4 hours.
   - The platform reports a cumulative metered figure of about $167 for the loop thread (output ≈ 0.73M tokens, cache reads ≈ 400M tokens). That is the platform's usage figure for the whole thread, not a billed amount, and how much of it the idle polls account for is not measured.
6. **Claude did not always follow its own protocol.**
   - It approved with an open SHOULD FIX (#16, #28).
   - It approved with red CI that it judged pre-existing (#9).
   - It posted a verdict 76 seconds before Codex's "Ready" signal (#11).
   - It appended the next task to a verdict (#24). Codex asked for it to be reposted.
   - It dropped the literal `VERDICT:` line from #24 onward.
7. **A follow-up was lost.** The bot's P2 on #7 (zero-balance currency buckets) was logged as "fold into a later slice", and no later comment, doc or commit references it again.
8. **Overclaiming was avoided but not perfect.** Claude told the owner up front that it could not promise an AWS-ready CRM overnight. It flagged a suspicious 22.8k-line PR as "I haven't checked that"; the size later turned out to be mostly a generated Drizzle snapshot. The first morning summary still said "Merge them oldest first" without the base-branch caveat (item 2).

## Downstream consequence

- Main went from PR #2 to #28 in three days. Main now has:
  - CI with Postgres browser gates;
  - Docker images;
  - AWS infrastructure as code;
  - email and payments behind provider-neutral boundaries;
  - multi-line billing;
  - a calendar;
  - SaaS subscriptions;
  - pack-driven fields with a second industry.
- The owner changed the review taxonomy to BLOCKER / 1.0 FIX / HARDEN LATER and made Claude the lead orchestrator.
- Project rule after the accident: base PRs on main where possible. Otherwise the orchestrator retargets each stacked PR to main, in order, immediately before the owner merges it.

## Supported lesson

**When Claude has its own execution surface (real Postgres, containers, browser tests) and an explicit "don't trust the author" mandate, it is an effective independent gate for a Codex implementer.** It reproduced and blocked several security and money defects that green CI and the author's report had passed. It is not a sufficient gate on its own: a second reviewer (Codex's review bot, or the owner's external reviewer) caught real defects after Claude's approvals, and an external reviewer caught a gap in Claude's own fix.

**Claude was weaker at release mechanics it had designed itself than at code review.** The stacked-base rule and the "merge oldest first" advice caused the only incident that needed recovery work.

## Public-prior reconciliation

- **Prior:** [baselines/ANTHROPIC.md](../../../baselines/ANTHROPIC.md) positions Opus 5.5 as a "high-judgment architect / reviewer", with Medium/High effort for final review.
- **This case adds operational nuance.** At medium effort the review role held up: it caught BLOCKERs that CI and the author missed, at a median 0.74h per first verdict.
- **What the prior doesn't capture:**
  - protocol consistency over many review rounds;
  - release mechanics;
  - quota drain from continuous orchestration polling.
- **No matched comparison exists.** Nothing here compares Opus 5.5 with Opus 4.8, Fable 5.1 or Sonnet 5.5 in the same reviewer role.

## What this does not prove

- That approved PRs are bug-free. The 1.0 code audit afterwards found 9 BLOCKERs on the merged main (for example, a customer could mark their own invoice paid with a "test" payment). No owner playtest has happened yet.
- That Claude Opus 5.5 reviews better than Codex Sol. The two reviewed different things at different times, and each caught defects the other missed.
- That the hourly-routine design is efficient. It was the only polling primitive available, and its cost was never measured separately from audit work.

## Dataset tags

```yaml
task_types: [code review, debugging, orchestration, release management, task design]
model_family: Anthropic/Claude
model_label: claude-opus-5-5 (loop thread, effort medium); Remote Control sessions unrecorded
tooling: [claude.ai Projects, Claude Code, Remote Control, GitHub MCP, hourly routine, PR subscriptions, Agent subagents, Postgres 16, dockerd, Playwright]
artifact_type: PR verdicts, roll-up PR, debugging PR, plan documents
verification: [independent lint/typecheck/unit/build, Postgres Playwright, container smoke, scratch reproductions, external reviewer on PR #3]
human_signal: high trust, all approved PRs merged, then explicit correction of review depth
outcome: 22 Codex PRs audited and merged path cleared; loop stalled 2026-10-08 on implementer availability
evidence_level: A (audit) / B (orchestration)
```
