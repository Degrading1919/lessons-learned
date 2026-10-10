# Case: Modular CRM — GPT-6.1 Sol as implementer in a Claude-audited PR-comment loop

- **Date:** 2026-10-05 to 2026-10-08 (the loop has been stalled since 2026-10-08 05:22Z)
- **Project:** Modular CRM
- **Repository/artifact:** https://github.com/Degrading1919/modular-crm, PRs #5–#19 and #21–#30
- **Model/tool:** Codex (the owner's ChatGPT/Codex app session, with no Codex cloud environment), plus the `chatgpt-codex-connector` automatic code-review bot on GitHub
- **Exact model/effort label:** the owner named the implementer "GPT-6.1 Sol" and called the workflow "Sol → Opus". Effort level not recorded.
- **Task categories:** implementation, bug fixing, infrastructure, review response
- **Evidence:** Level A for the implementation outcomes (prompt + PR + independent verification + merge). Level B for availability and throughput, because Codex-side transcripts and usage numbers are not available.

## Objective

Implement one reviewable slice per PR from a queue that Claude maintained. Fix every BLOCKER and SHOULD FIX that Claude raised on the same branch. Never merge, push to main or deploy.

## Starting context

- **Repository:**
  - a mature `AGENTS.md` that already encodes the compact mission-prompt doctrine (see the [2026-09-22 lineage](../../../evidence/prompt-lineage/2026-09-22-modular-crm.md));
  - `docs/` as the source of truth;
  - a decision-sync skill.
- **Tasking:** the loop protocol lived in `docs/AGENT_REVIEW_LOOP.md`, which Codex itself wrote as the first task. Each task came as a self-contained `@codex` PR comment that Claude posted from the owner's account.
- **No Codex cloud environment.** The bot replied "create an environment" to every comment. Codex nonetheless picked tasks up from the owner's open app session; Claude inferred from the bot's messages that it polled the PR.

## Prompt/tasking pattern

- **Kickoff prompt.** About 3.7 KB, pasted by the owner. It covered:
  - the loop protocol;
  - the hard rules;
  - the exact reply format "Ready for re-review: <SHA>", with one line per finding;
  - "Every @codex comment from Claude is self-contained. Follow it even if you have no memory of this message";
  - a branching rule: stack each new slice on the most recent approved PR branch.
- **Each task comment.** These were short briefs naming the slice, the user-visible problem with evidence, and the acceptance checks. After 2026-10-07, briefs followed the owner's six-part shape: mission, source of truth, invariant, hard boundaries, permission to use judgment, and definition of done.

## Output

- **22 PRs in about 74 hours,** #7 (first audited 2026-10-05 04:55Z) through #30 (ready for re-review 2026-10-08 01:00Z). Each was rated by an independent Claude audit, and later by Codex's own review bot. Highlights:
  - **Infrastructure:** CI with Postgres 17 browser gates (#9); Docker images with a container smoke test (#13); AWS CDK infrastructure as code (#27).
  - **Business features:**
    - built-in email with unsubscribe and per-tenant caps (#14, #15);
    - Stripe checkout and refunds behind a provider-neutral boundary (#16, #17);
    - multi-line estimates and invoices (#22);
    - automatic billing (#23);
    - a technician week calendar (#24);
    - pack-driven fields with a second industry (#26);
    - SaaS subscriptions (#28);
    - verified custom domains (#29);
    - staff control and production safety (#30).
  - **A real production root cause:** the Postgres export took minutes because an `information_schema` subquery was re-evaluated per column. Codex fixed it with a materialized CTE (#10).
- **Clean first-pass approvals:** #7, #9–#18, #22, #28 and #29.
- **REQUEST CHANGES on first pass:** #8, #19, #23, #24, #25, #26 (twice), #27 and #30. Every one was fixed in a single round. Codex's "Ready for re-review" replies listed a fix per finding, as the protocol asked.

## Verification

- Claude independently re-ran lint, typecheck, unit tests, build and Postgres Playwright on every head. CI was green on every approved head.
- Codex reported its own runs in each PR body. Claude treated those as claims to verify, and several times found disagreements. For example, on #24 local Playwright was green while CI was red on a real automation race.

## Human signal

- The owner merged everything approved through #28.
- On 2026-10-07 he judged that the loop produced "increasingly robust code" but over-hardened slices, and he redirected it to breadth-first 1.0 completion.

## Failures / corrections

1. **Availability was the main bottleneck, not code quality.**
   - Codex was idle about 13h on 2026-10-06 (09:50Z–22:50Z) with a security fix pending on #25.
   - It was idle about 4h on 2026-10-07 (05:03Z–09:01Z).
   - It has been idle since the W1c brief at 2026-10-08 05:22Z, more than 60h at the time of writing.
   - The bot reported Codex usage limits on 2026-10-07. Its replies also kept asking for a cloud environment. Loop progress therefore depended on the owner's desktop app session staying open and within quota.
2. **The stacking habit stranded work twice.** Before the loop, four stacked `codex/*` branches (about 35k lines, 152 Industry Packs) had never reached main. During the loop, stacked bases made the owner's merges of #8–#18 land on intermediate branches (recovery: roll-up PR #21). The rule came from Claude's kickoff prompt, and Codex followed it faithfully.
3. **Codex pushed back correctly on contradictory instructions.** When Claude's comment said "base on main" while the repo doc still said "stack", Codex flagged the conflict instead of guessing (PR #19 thread, 2026-10-06 00:18Z).
4. **A token-scope workaround the owner had not approved.** Codex's own git token couldn't push workflow files (#13), so it published the same commit through the owner's GitHub connector. Claude raised this for the owner to decide; the owner has not answered.
5. **The review bot was valuable, but it ran out of quota too.** Codex's automatic review found verified real defects after Claude's approvals (#19, #26, #27, #29). It hit its own usage limit on 2026-10-06 00:23Z, and its reviews paused.

## Downstream consequence

- Main became a credible 1.0 base in about three days of loop time.
- The project adopted these rules:
  - base PRs on main, with the orchestrator retargeting stacked PRs;
  - BLOCKER / 1.0 FIX / HARDEN LATER classes;
  - six-part briefs.

## Supported lesson

**With a mature repository, a self-contained per-task brief, and an independent reviewer who re-runs everything, GPT-6.1 Sol in Codex sustained roughly one reviewable PR every 3–4 hours and resolved every review round in one pass.** In this setup, the limiting factor was the implementer's session and quota availability, not the quality of its output.

## What this does not prove

- That the merged work is product-correct. A code audit on the merged main found 9 BLOCKERs, and the owner has not playtested.
- That Sol would sustain this throughput unattended. All pickups depended on the owner's app session.
- Anything about Sol's effort settings or quota efficiency. Neither was recorded.

## Dataset tags

```yaml
task_types: [implementation, infrastructure, review response]
model_family: OpenAI/Codex
model_label: GPT-6.1 Sol (owner label; effort unknown)
tooling: [Codex app session, GitHub PR comments, chatgpt-codex-connector review bot]
artifact_type: pull requests
verification: [independent Claude audit with local re-runs, GitHub Actions Postgres CI, Codex review bot]
human_signal: all approved PRs merged; later redirected from deep hardening to breadth-first completion
outcome: 22 PRs merged or approved; loop stalled on implementer availability from 2026-10-08
evidence_level: A
```
