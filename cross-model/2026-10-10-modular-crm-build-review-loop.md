# Modular CRM build/review loop: what worked, what struggled, how to run it better

- **Period:** 2026-10-04 to 2026-10-10
- **Setup:**
  - Claude audited and orchestrated, working through a claude.ai Project (coordinator, thread sessions, Remote Control onto the owner's Windows machine, Agent subagents).
  - Codex (GPT-6.1 Sol, in the owner's app session) implemented.
  - They talked only through `@codex` comments on GitHub PRs.
  - Codex's GitHub review bot acted as a second automated reviewer.
- **Cases:**
  - [Claude auditor/orchestrator](../models/claude-code/cases/2026-10-04-to-10-10-modular-crm-auditor-orchestrator.md)
  - [Codex implementer](../models/codex/cases/2026-10-05-to-10-08-modular-crm-sol-review-loop.md)
  - [Breadth-first prompt lineage](../evidence/prompt-lineage/2026-10-07-modular-crm-breadth-first-1-0.md)
- **Per-PR evidence:** [PR review table](../evidence/review-logs/2026-10-10-modular-crm-pr-review-table.md), built from GitHub API data.
- **Proposed next version:** [BUILD_REVIEW_LOOP_V2.md](BUILD_REVIEW_LOOP_V2.md), not yet executed.

Anything marked *(inferred)* was not directly measured.

## Measured

These numbers cover the 22 Codex PRs #7–#19 and #22–#30. #21 was Claude's roll-up and is excluded. Sources: GitHub timestamps, and the loop state log for when each task was posted.

| Measure | Value |
|---|---|
| Elapsed loop time, first task to last task sent | about 74h (2026-10-05 03:24Z → 10-08 05:22Z) |
| Codex: task posted → PR opened (median) | about 40 min; range 6 min to about 4h. Derived from the state log plus PR `created_at` |
| Claude: PR opened → first verdict (median) | 0.74h (mean 1.01h) |
| PR opened → final approval (median) | 1.02h (mean 2.58h; max 14.9h on #25, waiting overnight for Codex's fix) |
| PRs approved on first verdict | 14 of 22. Two of those (#16, #28) carried an open SHOULD FIX into the next slice |
| Claude findings in verdicts | 3 BLOCKER (#24, #25, #30) and 18 SHOULD FIX. 11 of the SHOULD FIXes were Claude's own; 7 were bot findings Claude verified and adopted |
| Codex review-bot inline findings | 16 (P1 8, P2 8) |
| Bot findings posted after a Claude approval | 10 on 4 PRs (#7, #26, #27, #29): 8 treated as real, 1 ruled latent, 1 never acknowledged (#7) |
| Codex implementer idle gaps | about 13h (10-06), about 4h (10-07), more than 60h (since 10-08 05:22Z) |
| Bot "create an environment" replies / "usage limit" replies | 48 / 10 |
| Owner merge latency after approval | about 1h to about 41h for merged PRs; #29 and #30 still open about 71h and 62h after approval |

**Reading:** when both models were live, one slice took about 1.5–2h end to end. The 74h for 22 PRs averages about 3.4h per PR, so roughly half the elapsed time was spent waiting on implementer availability. Review speed was not the bottleneck.

## What went well

1. **Two reviewers caught different things.**
   - **Claude's audits** stopped these from merging:
     - a sign-in limit bypass via a spoofed `X-Forwarded-For` header (#25 BLOCKER);
     - automations firing on events from before they were turned on (#24 BLOCKER);
     - overdue reminders that could never fire (#23);
     - a WAF rule that broke large invoices (#27);
     - multi-business users landing in the wrong business after re-login (#30 BLOCKER).
   - **Claude also caught a double-collection money bug on #16.** It approved the PR anyway and deferred the fix to #17. The bug was fixed before anything reached main, but this was not a block (see Struggles 6).
   - **The bot found 10 issues after Claude had approved.** Examples: lead conversion dropping pack details (#26), snapshot restore failing (#27), and a dead login link on custom domains (#29).
   - **The owner's external reviewer** found a missing location-scope check in Claude's own fix (PR #3).
   - On #8 and #30 Claude and the bot independently found the same defect about 2 minutes apart. That agreement is weak evidence that each reviewer is calibrated.
2. **"Don't trust the author's report" combined with Claude's own execution surface worked.** Claude re-ran the checks on real Postgres, `dockerd` and Playwright in the cloud container. That surface beat the owner's machine, which has no Docker. It found CI-only root causes (#9/#10 export latency) and a long-standing flaky test's root cause (#18).
3. **Self-contained task comments let Codex resume after gaps.** The rule "follow it even with no memory of this message" plus the protocol in `docs/AGENT_REVIEW_LOOP.md` let Codex resume after every idle gap without a new briefing.
4. **Codex enforced the protocol better than its author did.** It flagged:
   - a verdict that approved and requested a same-PR fix at once (#19);
   - an instruction that contradicted the repo doc (#19);
   - a verdict on a superseded head (#16);
   - a task buried inside an approval (#24);
   - a false-positive test result (#29).
   In each case Claude agreed and corrected itself.
5. **Parallel read-only exploration was cheap and useful.**
   - Day 1: a cloud exploration thread passed labelled leads to the Remote Control debugging session. One lead was a test script that ran no unit tests on macOS/Linux.
   - 2026-10-07: five parallel Agent audits produced a `file:line`-backed 1.0 plan in about 10 minutes.
6. **Authority stayed with the owner.** No agent merged or deployed anything. Every question to the owner was a one-word choice with a recommendation.

## What struggled

1. **The implementer's runtime was the binding constraint.** With no Codex cloud environment, every pickup needed the owner's app session and Codex quota. The loop has produced nothing since 2026-10-08 05:22Z.
2. **Claude designed the stacked-merge trap.** The kickoff rule ("stack on the latest approved branch") plus "merge oldest first" sent 11 of 12 merges to intermediate branches. A roll-up PR (#21) and mid-merge retargeting were needed. The same stacking had already stranded about 35k lines and 152 Industry Packs before the loop started.
3. **Owner merge latency deepened the stack.** Up to 9 approved PRs waited unmerged (2026-10-07 17:39Z). Each extra level raised the retargeting risk.
4. **Claude drifted from its own protocol.**
   - It said APPROVE while asking for a same-PR fix (#19).
   - It approved with an open SHOULD FIX twice (#16, #28).
   - It approved #9 with red CI. The failures were pre-existing, and fixing them became the #10 task.
   - It posted a verdict before the "Ready" signal (#11).
   - It appended the next task to a verdict (#24).
   - It changed the verdict format mid-run: the `VERDICT:` line disappeared from #24 on.
   Each case was handled reasonably, but every one was a place where the written protocol and Claude's behavior disagreed.
5. **Follow-ups could be lost.** The bot's #7 finding (zero-balance currency buckets) was logged as "fold into a later slice". No later comment, doc or commit references it again. Follow-ups lived in prose, not in a tracked backlog.
6. **The review taxonomy ratcheted toward hardening.** SHOULD FIX blocked merges, and follow-ups were folded into the next slice, so slices grew (#17, #18, #25). The owner had to step in on 2026-10-07; the agents did not self-correct toward his milestone.
7. **Polling continued while the implementer was idle *(inferred cost)*.** About 45 hourly "no change" wakes were logged. The Claude plan then hit its five-hour and seven-day limits, which delayed the #30 re-review by about 4h.
8. **Slice-level approval did not mean whole-product readiness.** The 2026-10-07 code audit found 9 BLOCKERs on a main where every slice had been approved. Examples: a customer could pay their own invoice with "test", staff could not be deactivated, and a solo owner could not do field work.
9. **Remote Control tied work to the owner's PC being awake.** The PR #6 audit waited because the computer was offline (2026-10-05 01:25Z).

## How to use these models better next time

The concrete prompts and checklists are in [BUILD_REVIEW_LOOP_V2.md](BUILD_REVIEW_LOOP_V2.md). In short:

**Setup**
1. **Give the implementer an always-on runtime** (a Codex cloud environment) before going unattended.
2. **Base every PR on main.** Stack only for a real dependency, and have the orchestrator retarget each stacked PR immediately before the owner merges it.
3. **Agree a merge cadence:** daily, or auto-merge for approved and green PRs. This is the owner's call, but each day of latency adds stacking risk.
4. **Give the implementer the token scopes its tasks need,** and forbid borrowing other credentials (#13).
5. **Budget quota for the second reviewer.**

**Protocol**
6. **Keep policy in the repo doc.** Comments carry tasks, never policy changes.
7. **Use one comment per instruction:** a verdict comment, then a separate task comment.
8. **Use a fixed verdict template** with a literal `VERDICT:` line. Approval means no open BLOCKER or milestone-class finding.
9. **Track follow-ups as issues, not prose,** so findings like #7's cannot vanish.

**Review**
10. **Tie the finding classes to the milestone from day one,** for example BLOCKER / 1.0 FIX / HARDEN LATER.
11. **Use two reviewers on money, authorization and data paths.** Treat each reviewer's findings as claims to verify, including the reviewer's own fixes.
12. **Walk the whole product every 4–5 merged slices,** as owner, office, technician and customer.

**Cost and attention**
13. **Back off polling after about 3 empty checks,** tell the owner once, and resume on the next PR event.
14. **Pick the execution surface per job:**
    - Remote Control for local-only reproductions;
    - the cloud container for Postgres, Docker and browser gates;
    - Agent subagents for parallel read-only audits and evidence gathering. This document's PR table was built by one.

## Public-prior reconciliation

| Model / role | Public prior (as of 2026-10-04) | Owner evidence here | Relationship |
|---|---|---|---|
| Claude Opus 5.5 as reviewer/orchestrator | [ANTHROPIC.md](../baselines/ANTHROPIC.md): "high-judgment architect / reviewer"; Medium/High for "architecture, ambiguous work, final review"; "Opus 5.5 plans/reviews → Sonnet 5.5 implements" | At medium effort it found 3 BLOCKERs and 11 original SHOULD FIXes across 22 PRs, with a median first verdict of 0.74h. It missed 10 later bot findings, and its own release-mechanics and protocol drift caused the only recovery work | **Adds operational nuance.** The review role is confirmed. The weak spots were process consistency and quota under continuous polling, which benchmarks do not measure |
| GPT-6.1 Sol as implementer | [2026-10-04 update](../research/models/2026-10-04-new-model-release-update.md): near-Astra quality at lower cost; slow throughput/latency; "real Codex quality remains mixed" | Median about 40 min from task to PR, and every review round was closed in one pass. The binding constraint was runtime availability and quota, not quality | **Adds operational nuance** on quality and availability. **Not comparable** on speed and token efficiency: effort level and token use were not recorded |
| Independent second reviewer (Codex review bot) | Corpus prior: separate authoring from review when semantic drift is costly ([ROUTING_GUIDE](ROUTING_GUIDE.md)) | It caught real defects after the primary reviewer approved, and matched the primary reviewer twice | **Confirms prior** |

## Routing implication

For this owner's repositories, the evidence supports:
- Codex (GPT-6.1 Sol) as the bulk implementer from compact, repo-grounded briefs;
- Claude Opus 5.5 as the independent gate and orchestrator, with its own execution environment;
- a second automated reviewer on high-risk diffs;
- the owner as merger and playtester.

This is a role-fit conclusion from one project, not a model ranking. A matched test (Sonnet 5.5 or Opus 5.5 implementing the same slice) would be needed to say anything about implementer choice.
