# Case: Claude — Bible Project Skill/Governance Bake-Off

- **Date:** 2026-07-24
- **Project:** The Bible Video Game
- **Repository:** https://github.com/Degrading1919/The_Bible_Video_Game
- **Model/tool:** Claude; strongest compared response recorded under the session label "Claude 5 max"
- **Task categories:** skill design, governance, role boundaries, theological/content-risk control
- **Evidence:** Level B

## Problem

The project needed to decide which AI skills should exist and how they should be governed.

This was not primarily a code-generation problem. It was an authority-design problem: which workflows should create content, which should review it, and which should be deterministic.

## Comparative result

The strongest Claude response separated **Sacred Event Protection Reviewer** from authorship.

That was a material design insight:

- a protection/gating role should detect violations
- it should not silently become the author/re-writer of the material it is judging
- Ancient Material Culture research should remain a separate specialist concern
- deterministic formatting should be implemented as a script rather than consuming LLM judgment
- a generic Codex Writer should be gated/deferred rather than given broad authority

## Human signal

The Claude response was judged stronger than the compared GPT responses for this governance task.

The cost-adjusted conclusion still did not make the maximum model the daily default. The user preferred cheaper capable models for routine implementation and frontier reasoning for major governance/review.

## Repository evidence

The Bible project contains the completed LLM-skills research synthesis:

https://github.com/Degrading1919/The_Bible_Video_Game/commit/ba756a045e9fafc3e52825cff3a01251e1ecf4ab

## Supported lesson

**Use stronger reasoning models where the task is about authority, boundaries, and semantic risk — not merely because the task involves AI.**

This case also supports separating:

- generative work
- review/gating
- deterministic transformation
