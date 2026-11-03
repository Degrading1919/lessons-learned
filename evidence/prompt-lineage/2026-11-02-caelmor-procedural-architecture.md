# Prompt lineage: Caelmor procedural architecture

- **Case:** [development retrospective](../../models/codex/cases/2026-11-02-caelmor-procedural-architecture.md).
- **Period:** November 2–3, 2026 UTC; same development chat and PR #85, not independent trials.
- **Sources:** owner messages in Codex chat **Build Caelmor Architectural Generator**, root session `01a19d8a-69dc-75b2-a578-ef6a604e13d7`; relevant ChatGPT chat **AI 3D Asset Research**, `6ae7c2d0-50ac-83ea-9a83-254edb653a68`; attached world-construction prompt, subsequently executed. Private session locators are provenance, not public transcript links. Only task-relevant excerpts/paraphrases are reproduced here.

## P0 — make a functioning procedural tool

**Executed, 2026-11-02 18:35 UTC.** Root log line 15. The owner requested a standalone Blender add-on generating detailed Lowmark buildings through parametric geometry, not prefab assembly. It named the research brief, licensed open-source study, deterministic seeds, irregular footprints/intersecting roofs and actual Blender/render verification. It authorized autonomous engineering and preferred Luna High for bounded geometry, implementation, tests and documentation, with stronger orchestration for architecture/integration/review. It specifically asked to optimize progress per allowance, avoid wasteful parallelism and independently verify worker output.

**Observed consequence:** a working five-function prototype, 14 tests, 80 stress cases and Blender/package evidence; local mixed commit `9eaaf1d` and failed main publication. The following message called it a promising milestone, not a finished asset pipeline. [Public isolated prototype](https://github.com/Degrading1919/Caelmor-Repo/commit/ecb109013c7723ec920feb9f04161b7df66bf9dc).

## P1 — preserve it, isolate publication, improve exterior construction

**Executed, 19:03 UTC.** Root line 754. The owner's direct assessment was that timber/roofing repeated, a conspicuous light roof-tile rectangle looked wrong, braces were awkward and materials overly clean/uniform. The instruction favored construction-driven variation and meaningful repairs over arbitrary decoration. It also explicitly authorized inspecting the mixed commit, preserving unrelated work and publishing only generator files through a PR based on remote main.

**Observed consequence:** isolated PR #85; semantic frame/shingle schedules, surface/material corrections and later roof regression gates. Do not attribute all later improvements to prompt wording: implementation, tests and explicit visual diagnosis changed too.

## P2 — correct the interpretation of the brown lines

**Executed correction, 19:30 UTC.** Root line 1406. Direct owner wording:

> The tops of the walls are still poking through the roofs, that is what the brown lines on the roof is

This identified a geometric defect rather than merely an unattractive color. The follow-up added full-section/slope-aware roof clearance and adversarial fixtures. The later diagnostic documented a 139 mm timber post breach. Two subsequent **“continue”** messages preserved the active mission; one resumed turn was interrupted. An intervening run had actually terminated with `usage_limit_exceeded`—see the [resource record](../measurements/2026-11-02-caelmor-development.md), not a guessed explanation for the pause.

## P3 — expand region, status and purpose

**Executed, 2026-11-03 00:28 UTC.** Root line 1845. The owner requested four dossier-grounded regional contexts, socioeconomic variation and a much broader range of residential, commercial, agricultural, industrial, civic and defensive functions. Windows-to-beam clearance was explicitly confirmed as an issue. RS3 settlement diversity supplied feel/systemic inspiration; copying designs, names/catalogs or displacing Caelmor canon was not authorized. Unity integration/performance and interiors were excluded.

**Observed consequence:** v0.3's 20 functions/17 local contexts, wealth/upkeep controls, real geometry differences, more clearance tests and efficient geometry. The actual gallery still did not meet the desired architectural diversity. A green matrix of valid combinations did not settle visual interpretation.

## P4 — require architectural reasoning and neutral recognition

**Prompt authored in ChatGPT, then executed in Codex at 02:06 UTC.** Root line 3414 references the supplied `Pasted text.txt`; its contents were separately inspected. In **AI 3D Asset Research**, the owner first described the intended contrast directly:

> It makes sense for lowmark to become more farm style houses, since theyre known for farming, but for emberholt, I envisoned brutalish iron structures.

The rest of that message described a less sinister city of smiths/fire/iron, rather than wood houses. This is direct artistic direction, not an assertion that a reference design should be copied. ChatGPT then drafted the prompt after the owner asked for it. Its core acceptance pattern was:

- derive construction from geography, resources, industry, climate, culture and history;
- make silhouette, structural systems, foundations, proportions and characteristic details region-specific;
- preserve approved canon and label art inferences;
- compare equivalent functions/status levels in neutral materials;
- reject results that remain architecturally interchangeable;
- implement actual geometry, preserve legacy/edit/export behavior and update PR #85 without merging.

The prompt's concise governing statement was **“The objective is architectural reasoning, not simply greater randomization.”** It asked for four untextured regional homes that read as products of four civilizations. This was more specific about the *quality criterion*, while leaving routine construction decisions to the agent.

**Observed consequence:** v0.4 regional volume/roof/support grammars. Initial Lowmark/Thornfell views were rejected internally and revised; the later blind worker review distinguished all four. The lead's final report still documented repetition and blank faces. This supports an improved construction system, not a claim that the revised prompt alone caused success or eliminated human correction.

## Later assessments: separate who said what

After the owner shared the final report/render, ChatGPT said the four regions were recognizable without textures, but criticized weak socioeconomic differences, overly ceremonial Thornfell gables and generic/modern-looking Emberholt massing. The relevant ChatGPT turn is `99126fea-b52e-49e1-966c-75f00c9ab262`, assistant item `37fd7364-cd6a-44b7-a17d-e4c6ab545a8e`. Those are **assistant visual judgments**, not direct owner acceptance/rejection and not an independent human study. The chat API did not include the attached image bytes; public gallery artifacts are the inspectable image evidence.

The owner then requested documentation of the full experience, including failures, necessary versus excessive testing and efficient model use (ChatGPT turn `e17ab17e-8bfa-4071-8ee4-d43f400ba79e`). The corresponding Codex retrospective began at **04:09:25 UTC** and is excluded from development telemetry. This documentation mission is not an additional generator implementation iteration.

## What the lineage supports

These were executed, sequential refinements with preserved artifacts—not a same-prompt model comparison or a fabricated chosen/rejected pair. There is no evidence that the owner rejected autonomy itself. The failure was that technical completeness and named variation were being used as weak proxies for the intended architectural quality. The productive correction specified observable artistic relationships and actual comparison evidence, while keeping engineering decisions delegated.

Future prompts should retain mission/source/scope/autonomy, but express *what a viewer must recognize*, request matched neutral and material views early, and require rejected outputs to be revised. Do not require the owner to diagnose every construction intersection after a large feature expansion.
