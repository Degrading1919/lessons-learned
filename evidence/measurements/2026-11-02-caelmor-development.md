# Caelmor development evidence and resource accounting

This is a source ledger for [the case](../../models/codex/cases/2026-11-02-caelmor-procedural-architecture.md), not a benchmark or cost invoice. Capture ends before the retrospective request at **2026-11-03T04:09:25.235Z**, root rollout line 4812. The [sanitized counters](2026-11-02-caelmor-session-metrics.json) preserve source filenames, prefix hashes, line locators, model/effort contexts, response counts, child attribution and limitations. No raw transcript, hidden reasoning text, images, credentials, account identifier or unrelated chat is published.

## Source coverage and evidence strength

| Source | What was inspected | What it establishes / limitation |
|---|---|---|
| Root Codex rollout, session `01a19d8a-69dc-75b2-a578-ef6a604e13d7` | User requests, observable tool actions/results, task completions, turn contexts and token records before cutoff | Exact Sol model/effort, prompt evolution, Git failure, quota error and orchestration. Model-authored reports still require artifact checks. |
| All 15 direct child rollouts | Model/effort contexts, per-response counters and final reported task outcomes | Actual Luna High routing and scoped contributions; author-reported checks are not owner acceptance. Children are identified by root spawn results, not by searching unrelated chats. |
| ChatGPT **AI 3D Asset Research** | Available relevant task-design/feedback turns | Direct owner industrial-architecture direction plus separately labeled ChatGPT assessment; incomplete image attachments and no full private-history export. |
| User-supplied world prompt attachment | Full text, matched to execution reference | Neutral-silhouette acceptance and explicit world-aware construction assignment. |
| PR #85 GitHub snapshot and local commit graph | Five PR commits, open/unmerged head `c5772d6`, comments endpoint returned an empty list | Publication lineage and artifact scope; no PR-discussion evidence was silently invented. Local unpushed mixed `9eaaf1d` is documented through the public preservation record. |
| Pinned source/tests/reports/manifests | Prototype, v0.2/v0.3 historical validation and v0.4 source/evidence | Concrete implementation and executed-run records; not new retrospective benchmark runs. |
| Actual comparison/feature images | Neutral four-region panel, equivalent-function/status sheets, feature/PBR views | Inspectable visual progression; internal agent review and retrospective inspection are not human art sign-off. |

The scope is the entire available PR #85 development chain, not every earlier Caelmor task or unavailable private provider record. No generator code was changed, no Blender/Unity task executed and no new asset benchmark run for this retrospective.

## Recorded resources: keep the units separate

Independent extraction reconciled **2,809 globally unique response IDs** across **16 session logs**. Every session's sum of per-response `usage` matched its last included `thread_token_usage` snapshot; there were no duplicated response IDs. Cumulative milestone snapshots were **not** added. Repeated cached context is still processed input and is not duplicate evidence to remove from these counters.

| Recorded field | Root Sol High | 15 Luna High workers | Combined logs |
|---|---:|---:|---:|
| Unique responses | 514 | 2,295 | 2,809 |
| Total processed tokens (input + output) | 110,351,373 | 255,320,956 | 365,672,329 |
| Input tokens | 110,048,518 | 254,425,615 | 364,474,133 |
| Cached input, included in input | 109,081,856 | 251,161,728 | 360,243,584 |
| Output tokens | 302,855 | 895,341 | 1,198,196 |
| Reasoning output, included in output | 168,031 | 412,719 | 580,750 |

These are **logged processing counters**, not unique content tokens, current context size, API-billed tokens/dollars or a model quality score. Cached input is about 98.84% of recorded input; that does not establish an equivalent subscription discount or prove cache behavior was optimal. The counters quantify the large repeated-context surface; they do not isolate which reread, tool schema, compaction or worker caused avoidable use. Event-level `token_count.info.total_token_usage` can differ from the reconciled `token_usage_record` snapshot; do not combine the two accounting families.

**Subscription allowance:** root snapshots show the 300-minute counter rising from 0% to 100% by 19:51 UTC. Crucially, root `task_complete` at line **1797**, **2026-11-02T19:51:29.528Z**, terminated with **`usage_limit_exceeded`**. A later continuation resumed after a long gap; one resumed turn was separately interrupted. Subsequent snapshots had changing/reset identities, including 98% before a counter restart and a final **50% / 300-minute, 8% / 10,080-minute** reading at 04:03 UTC. Account-level windows can include concurrent activity; the reset/counter changes are not explained by the logs. **Do not sum those percentages or call the final 50% the project's total usage.** A null `rate_limit_reached_type` snapshot did not negate the actual quota termination.

**Elapsed time:** the root task starts at 18:35:24 UTC and reports v0.4 at 04:03:05 UTC, approximately 9 h 28 m later. That envelope includes pauses and the usage interruption. Five `task_complete` records contain elapsed turn durations; parallel child durations overlap, and turn time includes tools/waiting. Neither the envelope nor summed child time measures active inference, human time or billable compute. No reliable total human-attention duration or API-dollar cost was recovered.

**Coordination:** 15 successful direct spawns, 36 `followup_task` calls, 109 `send_message` calls, three each of list/wait calls, two root compactions and one interrupted root turn. All spawns requested and all child contexts observed `gpt-6-luna` / `high`; Luna Medium was requested as an option but was not observed in development. These counts show real coordination/context work; they do not, by themselves, prove it was wasteful. There is no worker-only or single-lead control run.

## Supported task attribution

The JSON records each child session ID and completion line. The table summarizes **reported contributions**, independently cross-checked against the relevant modules/reports where available. It does not assign sole credit or blame for final integrated files.

| Worker(s) | Supported contribution | Review or correction still needed |
|---|---|---|
| `facades`, `blender_addon`, `verification` | Initial facade primitives, Blender backend/UI and tests/render/package evidence | Facade author explicitly left Blender visual validation to others; later roof/assembly defects escaped initial checks. |
| `frame_quality`, `surface_quality`, `exterior_qa` | Frame schedule/clearance; original color/normal/roughness maps and export tint parity; exterior gallery/provenance | Owner clarified roof lines were geometry; integrated datums/full sections and actual renders mattered. |
| `regional_models`, `expanded_facades`, `regional_ui_materials`, `world_generator_qa` | Region/type/wealth profiles, assembly-safe openings, circulation details, UI/materials, stress/BVH/render evidence | NameError/type/category/override corrections; broader type/profile coverage did not solve visual sameness. |
| `traditions_research`, `rural_highland_language`, `mire_language` | Regional research/Emberholt, Lowmark/Thornfell, Mire construction modules | API/context mismatch, invalid context fixture, duplicate keyword, initially syntax-only Mire check, connector alignment and root integration fixes. |
| `world_qa`, `blind_architecture_review` | Cross-region mesh/access/protection/export checks, evidence replay, neutral recognition review | Initial Lowmark/Thornfell similarity triggered revision; final review still noted generic Emberholt/shared details. Agent recognition is not owner approval. |

The root owned roof geometry, shared contracts, integration, independent reruns and final visual inspection. A research summary's Ashspire interpretation was corrected against the dossier; a context-specific gate exit and world-versus-legacy input behavior also required lead review. This supports guarded delegation, not “Luna cannot reason” or “Sol always fixes it.”

## Failures and accounting cautions

The main push failed once, non-fast-forward, and stopped as required; later generator-branch publications succeeded. An isolated unittest invocation also failed to import the package from its working path. Across 280 root `exec` output blocks, extraction found 18 nested nonzero results, mixing expected/probing validation failures, assertions, patch and command errors. Compound calls prevent interpreting that as 18 independent defects or a clean retry metric. The task-level quota error is a separate event and must not be lost by counting shell exits only.

No actual matched cost experiment exists. It is plausible that deterministic manifest checks, narrower result outputs, earlier cheap geometry checks, small neutral galleries before broad expansion, and targeted rerendering could reduce corrections/context. It is also plausible that strong early architecture could avoid late rewrite. The project establishes mechanisms and candidates for controlled experiments, **not quantified savings** or a universally cheapest model.

An observed scheduling example: root custom-tool calls at lines 4680/4687 (03:59:24/03:59:36 UTC) trim trailing blank lines in three regional sources, rebuild/reinstall the package in World and legacy modes, and launch the full evidence replay again. Later calls at 4711, 4718, 4729, 4742, 4749, 4755 and 4761 include short waits on that replay. Package byte identity changed, but this was not a new geometry feature. Freezing formatting before final evidence and using fewer meaningful polls are supported process improvements; their counterfactual savings were not measured.

## Reproduction and public artifact references

With the original local logs available, run `py -3 scripts/extract_caelmor_session_metrics.py --root-log <root-rollout.jsonl>`. The extractor selects only the 15 children identified in the checked-in case measurement. It emits counters/provenance, never raw messages; the script requires private input logs that are not bundled. Prefix hashes stop before the retrospective request, keeping later documentation usage outside the development record.

- [Pinned v0.4 validation](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/WORLD_VALIDATION.md)
- [Pinned v0.3/v0.2 validation](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/VALIDATION.md)
- [V0.3 gallery baseline](https://github.com/Degrading1919/Caelmor-Repo/blob/bb3349a69669708919207abcfb6b666ceb0df692/CODE/Scripts/architectural_generator/evidence/expanded_type_gallery.png)
- [V0.4 four-region clay view](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/evidence/world_first_four_clay_labelled.png)
- [V0.4 function matrix](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/evidence/world_matrix_clay_labelled.png)
- [V0.4 matched wealth sheet](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/evidence/world_wealth_cottages_clay_labelled.png)
- [Geometry/source replay](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/evidence/world_source_equivalence.json)
- [Final native World install report](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/evidence/world_installed_extension_verification.json)

References distinguish public durable artifacts from private session locators and agent-reported results. Where a gallery reused an earlier render, geometry replay supports equivalence for recorded settings; it does not prove unchanged rendering inputs or human artistic acceptance.

## Retrospective verification

The documentation audit independently reran the counter extraction and matched all 16 session sums/snapshots. It checked 58 local Markdown targets and 25 pinned Caelmor Git objects/paths, all model contexts, child IDs, counter partitions, the task-level quota error and dataset references. Repository validators passed for 10 cases, 24 public model baselines and 9 harness baselines; only the new case row was added to those datasets. Luna High reviewed the technical record and resource account; lead review checked their findings against the original source, including the full initial failure message and usage-limit event. A misleading deck-clearance phrase was corrected. These are documentation/source checks, not new asset tests or artistic approval.
