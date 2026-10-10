# Modular CRM build/review loop: what worked, what struggled, how to run it better

- **Period:** 2026-10-04 to 2026-10-10
- **Setup:** Claude (claude.ai Project: a coordinator, thread sessions, Remote Control onto the owner's Windows machine, Agent subagents) audited and orchestrated. Codex (GPT-6.1 Sol, in the owner's app session) implemented. The two were connected only through `@codex` GitHub PR comments.
- **Cases:**
  - [Claude auditor/orchestrator](../models/claude-code/cases/2026-10-04-to-10-10-modular-crm-auditor-orchestrator.md)
  - [Codex implementer](../models/codex/cases/2026-10-05-to-10-08-modular-crm-sol-review-loop.md)
  - [Breadth-first prompt lineage](../evidence/prompt-lineage/2026-10-07-modular-crm-breadth-first-1-0.md)

Claims are tied to the episode they come from. Anything marked *(inferred)* was not directly measured.

## What went well

1. **The cross-model gate caught real defects in both directions.**
   - Claude's audits blocked an auth-limiter bypass via a spoofed `X-Forwarded-For` header (#25), double payment collection (#16), stale automations firing (#24), a WAF rule that broke large invoices (#27) and wrong-business login (#30).
   - Codex's review bot then caught real issues Claude had approved (#19, #26, #27, #29).
   - The owner's own external reviewer caught a missing location check in Claude's own debugging fix (PR #3).
   - No single reviewer would have caught all of these.
2. **"Don't trust the author's report" plus an execution surface worked.**
   - Claude re-ran everything for each verdict, on real Postgres, `dockerd` and Playwright in its cloud container.
   - That surface exceeded the owner's local machine, which has no Docker. The cloud container was the right place for the gate.
3. **Self-contained task comments made Codex stateless-safe.** "Every @codex comment is self-contained. Follow it even if you have no memory of this message", together with the loop written into `docs/AGENT_REVIEW_LOOP.md`, let Codex resume after session gaps without re-briefing.
4. **The fixed reply protocol made re-review cheap.** "Ready for re-review: <SHA>", with one line per finding, meant every REQUEST CHANGES round closed in one pass.
5. **Parallel read-only exploration helped.**
   - On day 1, a cloud exploration thread fed the Remote Control debugging session labelled leads ("verify yourself, not conclusions"). This surfaced a test script that ran no unit tests on macOS/Linux.
   - On 2026-10-07, five parallel Agent audits turned a strategy change into a `file:line`-backed 1.0 plan in about 10 minutes.
6. **The owner kept merging authority and was told plainly what was waiting on him.** The morning summaries said what landed, each verdict, what waited on him, and what still blocked AWS. Nothing was merged or deployed by an agent.

## What struggled

1. **Implementer availability was the binding constraint.**
   - Codex idled about 13h, about 4h, and then more than 60h. Usage-limit messages show up in the record.
   - There was no Codex cloud environment, so each pickup depended on the owner's desktop app session.
   - The loop has produced nothing since 2026-10-08 05:22Z.
2. **Stacked PR bases plus "merge oldest first" was a trap.**
   - Claude's own kickoff rule, which Codex followed, made 11 of 12 merges land on intermediate branches.
   - The same habit had already stranded about 35k lines and 152 Industry Packs on an unmerged `codex/*` stack before the loop began.
3. **Rule changes made in comments conflicted with rules in the repo doc.** Claude's "base on main" comment contradicted `AGENT_REVIEW_LOOP.md`. Codex correctly refused to guess.
4. **Review depth ratcheted into hardening.** The owner had to step in to change the taxonomy (see the prompt lineage). The agents did not self-correct toward the owner's real milestone.
5. **The orchestrator kept polling while the implementer was idle *(inferred cost)*.**
   - About 45 hourly "no change" wakes were logged after Codex went idle.
   - The Claude plan then hit its five-hour and seven-day limits, delaying one re-review by about 4h and filling the project chat with retry notices.
6. **Approved and merged still didn't mean usable.**
   - The post-merge code audit found 9 BLOCKERs on main. Examples: a customer could mark their own invoice paid with a test payment; staff couldn't be deactivated; a solo owner couldn't do field work.
   - The PR-at-a-time gate checked slices, not whole-product paths.

## How to use these models better next time

**Setup**

1. **Give the implementer an always-on runtime before starting an unattended loop.** Here that meant a Codex cloud environment. Otherwise the loop runs only while the owner's app session is open and within quota.
2. **Base every PR on main, and have the orchestrator merge-order or retarget.** Never let the implementer stack by default. If stacking is unavoidable, the orchestrator retargets each PR to main immediately before the owner merges it. That has been the project rule since 2026-10-06.
3. **Put every loop rule in the repo doc and change it there.** Each task comment should then cite the doc rather than override it. Comments carry tasks, not policy.
4. **Grant the implementer the token scopes it needs** (for example, workflow-file pushes). Otherwise it improvises through other credentials.

**Tasking**

5. **Set the review taxonomy from the milestone on day one,** for example BLOCKER / 1.0 FIX / HARDEN LATER. Don't let "should fix" plus "fold follow-ups into the next slice" become the default.
6. **Keep briefs to the six-part shape:** mission, source of truth, invariant, hard boundaries, judgment permission, done. This matches the existing [prompt-size rule](ROUTING_GUIDE.md#prompt-size-rule).
7. **Run a whole-product path audit periodically, not only per-PR audits.** For example, every 5 PRs run owner → office → technician → customer walkthroughs. The 9 BLOCKERs found on 2026-10-07 were invisible slice by slice.

**Review**

8. **Keep two independent reviewers on anything touching money, auth or data.** Claude's audit plus the Codex review bot (or the owner's external reviewer) caught disjoint sets of defects. Budget quota for the bot. It ran out on 2026-10-06.
9. **Treat the reviewer's own fixes as needing review too.** PR #3 shows Claude's own debugging fix had an authorization gap.

**Cost and attention**

10. **Back off polling when the implementer is idle** *(inferred)*. After about 3 idle checks, drop to a slow cadence and tell the owner once. Spend Claude quota on audits, not "no change" logs.
11. **Pick the execution surface per job:**
    - Remote Control on the owner's machine to reproduce local-only issues (PGlite and Windows setup);
    - the cloud container for gates that need Postgres, Docker or browsers;
    - Agent subagents for parallel read-only audits.
12. **Ask the owner only one-word questions with a recommendation.** Examples: GitHub vs PC, merge vs hold. Everything reversible was done without asking, and nothing irreversible was done at all.

## Routing implication

For this owner's repositories, the evidence supports:

- Codex (GPT-6.1 Sol) as the bulk implementer from compact repo-grounded briefs;
- Claude Opus 5.5 as the independent gate and orchestrator, with its own execution environment;
- a second automated reviewer on high-risk diffs;
- the owner as merger and playtester.

This is a role-fit conclusion from one project, not a model ranking.
