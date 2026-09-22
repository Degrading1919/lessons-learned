# Case: Margins — From Prompting Skill to Measured 3D Production Loop

- **Dates:** 2026-08-06 through 2026-09-16
- **Project:** Margins
- **Repository:** https://github.com/Degrading1919/margins
- **Tool:** Tripo 3D with ChatGPT-authored prompting discipline and Blender downstream cleanup
- **Evidence:** Level A/B

## Stage 1 — encode prompting discipline

PR #24 added the repository-local Tripo prompting skill:

https://github.com/Degrading1919/margins/pull/24

The skill separated:

- documented Tripo capabilities
- Margins project constraints
- working heuristics

It explicitly prohibited guarantees about:

- exact topology
- exact polygon counts
- rigging success
- production readiness
- cleanup time

## Stage 2 — learn from rejected visuals

The user rejected an early door/reference result as unusable.

The next prompting direction became materially more specific:

- real thickness
- softened/beveled construction
- believable stylized proportions
- restrained surface wear
- neutral 3/4 studio presentation
- low-to-mid-poly feel without toy/cartoon distortion

This created a better visual target than generic "stylized contemporary Americana" alone.

## Stage 3 — convert generation into measurements

PR #43 established the 13-bin production asset catalog:

https://github.com/Degrading1919/margins/pull/43

Instead of guessing budgets in advance, it recorded representative source geometry and approved LOD0 ceilings asset by asset.

This eventually supported concrete Tripo face-limit guidance and production intake validation.

## Supported lesson

**The productive use of generative 3D is an iterative measurement loop, not prompt perfection.**

Prompt quality matters, but the stronger system is:

1. generate
2. inspect
3. reject/accept with concrete reasons
4. normalize downstream
5. measure
6. update project standards
7. generate the next asset with better constraints

That turns AI asset generation into a learning production pipeline rather than a sequence of disconnected prompts.
