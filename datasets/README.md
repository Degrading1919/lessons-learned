# Dataset Guide

## Current dataset

`cases.jsonl` contains one JSON object per observed task/outcome case.

It is designed for:

- retrieval
- filtering by task/model/tool
- qualitative preference analysis
- routing experiments
- longitudinal comparisons
- later conversion into supervised or preference-evaluation datasets

## Current case fields

| Field | Meaning |
|---|---|
| `id` | Stable case identifier |
| `date` | Date of the observed task/result |
| `project` | Project name |
| `repo` | Public repository URL when available |
| `model_family` | Provider/tool family as observed |
| `model_label` | Exact session/model label when known |
| `task_types` | Tags describing the work |
| `prompt_pattern` | Concise characterization of tasking style |
| `artifact` | Commit/PR/local artifact reference |
| `verification` | Tests, build, playtest, review, etc. |
| `human_signal` | Direct user reaction/preference evidence |
| `outcome` | What happened after the output |
| `lesson` | Narrow supported conclusion |
| `evidence_level` | A, B, or C per METHODOLOGY.md |

Future cases may also add `reasoning_effort`, `agent_harness`, `autonomy_level`, `tooling`, `resource_signal`, and `public_prior_alignment` when those values are actually evidenced. Historical rows do not need fabricated values merely to satisfy a newer schema.

## Why this is not yet a conventional RLHF preference dataset

Traditional pairwise preference data requires something closer to:

- same or comparable prompt
- candidate output A
- candidate output B
- explicit preference or ranking
- ideally a reason for the preference

Most historical project sessions preserve the chosen artifact better than the rejected full output.

Creating fake "chosen/rejected" pairs from incomplete recollection would damage the dataset.

## Future preference-pair format

When both outputs are actually available, add `preference_pairs.jsonl` with records shaped like:

```json
{
  "id": "stable-id",
  "task": "...",
  "context": "...",
  "candidate_a": {
    "model": "...",
    "output_ref": "..."
  },
  "candidate_b": {
    "model": "...",
    "output_ref": "..."
  },
  "preferred": "a",
  "preference_reason": "...",
  "verification": ["..."],
  "confidence": "high"
}
```

Do not create a pair unless the candidates and preference are actually evidenced.

## Future prompt-evolution format

Prompt revisions are a different type of preference signal.

When both prompt versions and downstream outcomes are known, preserve them under `evidence/prompt-lineage/`.

A future machine-readable file can represent:

- rejected prompt pattern
- accepted prompt pattern
- same/different downstream model
- whether both prompts were executed
- outcome delta
- user reason for revision

Do not treat a prompt preference as an output preference unless both downstream outputs exist.
