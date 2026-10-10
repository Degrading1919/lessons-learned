# Prompt Lineage: Modular CRM moves the review loop from deep hardening to breadth-first 1.0

- **Project:** Modular CRM
- **Repository:** https://github.com/Degrading1919/modular-crm
- **Date:** 2026-10-07 19:02Z
- **Trigger:** owner reassessment after 22 audited Codex PRs

## Before (executed 2026-10-04 to 2026-10-07)

The owner briefed Claude as an **independent cross-model auditor**:

- **Review stance:** "do not assume the implementing model's report is correct... do not optimize for agreeing with it."
- **Finding classes:** BLOCKER / SHOULD FIX / FOLLOW-UP / NIT.
- **Verdicts:** APPROVE / APPROVE WITH FOLLOW-UP / REQUEST CHANGES.
- **Slice queue:** each new slice combined new work with the previous PR's follow-ups.

Effect (observed in the PR log):
- every SHOULD FIX blocked a PR;
- follow-ups from one PR were folded into the next slice's brief;
- slices widened into adjacent edge cases. Examples:
  - #17 bundled payment and email hardening;
  - #18 bundled refunds, reminders, receipts, field recovery and a test flake;
  - #25 bundled the rate limiter, logging, an error reporter and two automation recipes.

## Owner correction

> Up to now, the Sol → Opus workflow has been effective at producing increasingly robust code, but it has also encouraged deep hardening of individual slices and repeated expansion into adjacent edge cases. That has been valuable for foundational correctness, but it is no longer the optimal way to reach the owner's immediate goal.

New objective: "speed-run Modular CRM to a complete, coherent, deployable 1.0 with all intended customer-facing capabilities implemented, then freeze features so the owner can personally playtest". Explicitly no reduced MVP.

## After

- **Finding classes:** BLOCKER / 1.0 FIX / HARDEN LATER. Only the first two create work: "Do not keep the implementation loop alive merely because another technically valid improvement can be imagined."
- **Foundations named as non-negotiable:**
  - tenant isolation;
  - authorization;
  - money correctness;
  - state machines;
  - idempotency;
  - migrations;
  - webhooks;
  - real Postgres CI;
  - deploy safety.
- **Waves:**
  1. the lifecycle spine;
  2. a constrained grid website editor;
  3. Industry Packs at scale through config and validation;
  4. a code-verified gap audit;
  5. a whole-product integration audit;
  6. feature freeze.
- **Roles:** Claude was promoted to lead orchestrator. Codex briefs take six parts: mission, source of truth, invariant, hard boundaries, judgment permission, done.

Claude's first execution of the new pattern took about 10 minutes of wall time (19:05Z → 19:15Z). It ran five parallel code audits, one Agent subagent per product area, and produced `PLAN_1_0.md`: 9 BLOCKERs with `file:line` evidence, about 14–18 PRs in waves, and an explicit HARDEN LATER list (two-way SMS, deposits, tips, autopay, QuickBooks sync and others).

## Downstream outcome (so far)

- Two PRs ran under the new rules: #29 custom domains and #30 production safety plus staff control.
  - #29 was approved with one carried-over item classified as a 1.0 FIX, not a blocking SHOULD FIX.
  - #30 got one BLOCKER round (multi-membership login) and was approved at its second head.
- The loop then stalled on implementer availability (see the [Codex case](../../models/codex/cases/2026-10-05-to-10-08-modular-crm-sol-review-loop.md)).
- **There is not yet enough evidence** to say whether the new taxonomy shortened cycle time or reduced scope creep. Re-evaluate after the spine waves land and the owner playtests.

## Lesson

A review taxonomy is a throughput control, not only a quality control. "SHOULD FIX blocks merge" plus "fold follow-ups into the next slice" is a ratchet toward hardening. Tying the classes to the owner's actual milestone ("predictably hit by a normal user before freeze") is how the owner tried to keep rigor on foundations without letting every valid finding create work.
