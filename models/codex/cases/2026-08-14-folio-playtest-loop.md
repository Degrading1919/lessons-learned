# Case: Folio — Autonomous Build Followed by Human Product QC

- **Date:** 2026-08-14
- **Project:** Folio
- **Location:** local `C:\Dev\budget-app\`
- **Model/tool:** Codex
- **Task categories:** desktop app, Tauri/React/Rust, finance UX, iterative implementation
- **Evidence:** Level B

## Workflow

The accepted operating model was:

1. give Codex a broad functional phase
2. let it inspect/build/test/package locally
3. run the app as a real user
4. report concrete friction
5. convert that friction into the next correction prompt

The project owner explicitly preferred this over endlessly refining specifications before a usable app existed.

## Phase 1 result

Phase 1 was successful enough to use, but real playtesting exposed issues that technical implementation alone had not resolved:

- date-based pay schedules
- calendar due-date behavior
- category dropdown behavior
- $0 original-balance handling
- precomputed-interest handling
- backup/restore
- naming/UX issues
- planning graph behavior

A later correction prompt required a true month-by-month avalanche/snowball simulation with rolled-over minimum payments and centralized Rust calculations.

## Supported lesson

**For product software, reaching a coherent usable build and then collecting human friction can create higher-value next tasks than trying to predict every UX requirement in the initial prompt.**

This is the same principle later visible in Margins owner playtesting: tests can verify contracts, but only use reveals some workflow failures.
