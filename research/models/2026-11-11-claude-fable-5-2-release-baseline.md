# Claude Fable 5.2 — November 2026 release baseline

**As of:** 2026-11-11 (two days after release, community confidence LOW)  
**Release:** 2026-11-09  
**Evidence class:** provider claims + independent benchmarks + first-person public reports; **not** an owner-observed case or Caelmor preference test.  
**Primary decision:** Fable 5.2 is a high-end **hard-problem advisor/architect/reviewer** candidate. It is **not** the default Caelmor prose writer or subscription-efficient daily coder merely because it tops an intelligence index.

## Executive assessment

- **Provider narrative:** major step forward from Fable 5.1 on coding, difficult reasoning, science and visual analysis, with up to 30% faster output and 20% lower list input/output prices. Anthropic itself recommends **Opus 5.5 for most everyday coding/knowledge tasks**, escalating to Fable when complexity justifies it.
- **Independent result:** Artificial Analysis Intelligence Index **v5.0.1** scores **65 at Max (#1 on the retrieved board)**. Low 54, Medium 56, High 62, XHigh 62, Max 65, but benchmark task cost rises sharply. **These scores cannot be numerically compared to the prior repository's v4.3 Fable 5.1 scores.**
- **Community:** striking first-hand examples of better planning and difficult debugging, but also reports of half answers, confident wrong assumptions, frequent compaction and usage windows disappearing within minutes. Positive and negative anecdotes are both new and self-selected; no stable consensus after two days.
- **Creative writing:** a new author-run ToneBench reports better scripted writing at High/XHigh than Fable 5.1 and improved structure/length control, **but not better tone adherence**. Its own test favors **Opus 5.5 XHigh for equivalent writing quality at lower cost**. This is one private benchmark, not a blind Caelmor result.
- **Subscription caution:** Fable availability is plan-specific; launch promotion and resets are temporary and do not increase steady-state included allowance. See official terms below.

## Verified product specification

| Attribute | Fable 5.2 |
|---|---|
| Exact model ID | `claude-fable-5-2` |
| Context | 1,000,000 tokens |
| Max output | 128,000 tokens |
| Modalities | Text and image input → text |
| Thinking | Adaptive, always on |
| Default effort | **High according to the model/API overview**; launch discussion describes Medium for some Claude app/Code experiences. **Record actual surface and setting rather than assuming they are identical.** |
| List API input/output | **$8/$40 per million tokens**; Fable 5.1 was $10/$50 |
| Cache read | **$0.20/M** |
| 5-min cache write | **$10/M** |
| 1-hour cache write | **$16/M** |
| Optional fast mode | Up to 2.5× output rate at **$16/$80/M** input/output; no lower cost per token |
| Release and availability | Nov. 9; Claude, Claude Code, Claude API, AWS, Google Cloud, Azure, subject to plan and organization settings |

Sources:
- [Official release](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- [Fable 5.2 model overview: exact price/cache/context/default effort](https://platform.claude.com/docs/en/models/fable-5-2/overview)
- [Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)

**Important fallback and security distinction:** Fable 5.2 and restricted **Mythos 5.2** share an underlying model, but Fable has additional cyber/biology safeguards; some blocked requests may be transparently answered by Opus-family models. A provider-reported 55% reduction in unnecessary cyber/bio blocks vs Fable 5.1 concerns those safety domains; do **not** extrapolate it to fiction or general refusal behavior. Mythos 5.2 is **not** a normal consumer routing option.

## Anthropic provider results (self-reported)

At the cited provider-selected effort settings:

| Test | Fable 5.2 | Fable 5.1 | Opus 5.5 |
|---|---:|---:|---:|
| FrontierCode 2.0 | **49.1% XHigh** | 32.4% XHigh | 45.5% |
| FrontierSWE v2 | **69.9%** | 56.3% | 62.3% |
| AutomationBench | **51.4%** | 31.4% | 42.5% |
| Terminal-Bench-Science 0.1 | **74.6%** | 52.6% | 58.7% |
| Humanity’s Last Exam with tools | **74.2%** | 65.6% | 67.7% |
| Chartography no tools | **73.4%** | 44.8% | 64.4% |

These are Anthropic's evaluations; compare versions, effort and safeguards before drawing universal conclusions. Its real-project examples involve elaborate test harnesses, including teams of hundreds to 1,000 agents; they are **not** evidence that one consumer subscription can reproduce that output cheaply.

Anthropic says it saw a High-effort Fable 5.2 FrontierCode score around 45.3%, near Opus 5.5's Max 45.5% at roughly half the evaluated cost per task; XHigh reached 49.1%. These are benchmark-specific, not general price multipliers.

Primary source: [Anthropic November 9 release and evaluation](https://www.anthropic.com/claude-fable-and-mythos-5-2).

## Independent cost/intelligence comparison

Artificial Analysis **Intelligence Index v5.0.1**, Nov. 9–11 snapshot:

| Effort | Intelligence score | AA cost/task | Approx. output tokens/task |
|---|---:|---:|---:|
| Low | 54 | $3.10 | 35.9K |
| Medium | 56 | $3.80 | 43.1K |
| High | 62 | $9.08 | 97.8K |
| XHigh | 62 | $14.83 | 161.9K |
| Max | 65 | $26.54 | 273.8K |

The index's methodology changed to v5.0.1. **Prior Fable 5.1 Intelligence Index 53 on v4.3 is not a valid point-by-point baseline.** Compare 5.1 using the same v5.0.1 recalculation if necessary.

On this broad index, **High is the most defensible hard-task effort setting**: XHigh costs ~63% more yet scores the same after rounding; Max costs ~2.9× High for three additional points. That does not prohibit XHigh on a narrower task; Anthropic's FrontierCode and one writing-specific evaluation show XHigh can improve those tasks.

Max scored first on AA's new index, but was extremely expensive and slow (about 45 minutes per index task by AA's derived measure). Fast mode increases throughput for extra money; it does not repair quota economics.

Sources:
- [Artificial Analysis Fable 5.2](https://artificialanalysis.ai/models/releases/claude-fable-5-2)
- [Fable 5.2 Max model details](https://artificialanalysis.ai/models/claude-fable-5-2)
- [Independent per-effort comparison](https://www.rdworldonline.com/wp-content/uploads/2026/11/fable-5-2-index-cost-iframe-1.html)

## Human community signal, Nov. 9–11

### Positive: substantial capability and sometimes higher efficiency at controlled effort

- [Early-access walkthrough (r/ClaudeAI)](https://www.reddit.com/r/ClaudeAI/comments/1xs2wdl/fable_52_review_here_is_whats_actually_different/) reports subjectively faster work than 5.1, Medium being adequate for the author's tests, and fewer perceived friction points. This is a single self-report and repeats provider claims for untested safety changes.
- [Fable 5.1 vs 5.2 discussion (r/ClaudeCode)](https://www.reddit.com/r/ClaudeCode/comments/1xte4kz/fable_52_vs_fable_51_in_cc/) includes praise that 5.2 is better and cheaper than 5.1; another user in the same thread found little difference versus Opus 5.5 even on larger tasks, making Fable's higher cost hard to justify.
- [Provider customer reports](https://www.anthropic.com/claude-fable-and-mythos-5-2) praise difficult coding, long-horizon work, willingness to re-evaluate wrong assumptions, research/engineering. These are selected customer testimonials (not independent Reddit measurements).

### Negative: severe quota burn, compaction and uneven practical judgment

- [High-engagement user thread (r/claude)](https://www.reddit.com/r/claude/comments/1xskbif/hows_everyone_finding_claude_fable_52_so_far/) includes multiple accounts of five-hour usage disappearing after a few prompts or within minutes, including one claiming 100% → 0% in three minutes on Pro. Subscription accounting and workloads are not standardized; this establishes **risk**, not a stable per-task burn multiplier.
- [Fable 5.1 vs 5.2](https://www.reddit.com/r/claude/comments/1xsf10k/fable_51_vs_52/) includes reports of Chat/Cowork compaction nearly every message and inconsistent apparent 200K vs 1M context behavior; other commenters suggest a glitch. Treat this as a **surface-specific launch issue hypothesis**, not proof the base model is limited to 200K.
- [Civil engineering, 16-hour first-person report](https://www.reddit.com/r/ClaudeAI/comments/1xsv2s0/unconvinced_by_claude_fable_52/) prefers Opus 5.5's directness and uncertainty communication, reporting Fable 5.2's confident wrong assumptions and partial answers. One user's professional workflow; important contradiction to claims of general judgment superiority.
- [r/ClaudeCode thread](https://www.reddit.com/r/ClaudeCode/comments/1xte4kz/fable_52_vs_fable_51_in_cc/) explicitly preserves disagreement rather than a "unanimous best-model" narrative.
- A [crossposted summary](https://www.reddit.com/r/ClaudeCoding/comments/1xt2wbe/tldr_hows_everyone_finding_claude_fable_52_so_far/) describes reports of over-delegation, including many Fable subagents. These should be inspected as potential **harness configuration/fanout** costs before treating them as model intrinsic costs; avoid double-counting summaries/reposts as independent evidence.

**Do not turn contemporaneous speculation about "Anthropic nerfed Opus 5.5 to push Fable" into a fact.** No controlled, cross-account evidence in this research establishes it; see [separate November 8 investigation](../writing/2026-11-08-opus-5-5-regression-and-caelmor-options.md).

### November 10 usage accounting correction

An [official @ClaudeDevs announcement](https://x.com/ClaudeDevs/status/2120275296637321476) states Anthropic fixed issues that consumed more limits than intended, and provided one **full across-model usage reset** to Pro, Max, Ultra and Team subscribers, redeemable before Dec. 10, 2026. It did not specify which workloads were affected or how much. Thus **some launch-window burn reports may reflect temporary accounting bugs**, while Fable's genuinely expensive token/task behavior remains independently documented. Do not treat the reset as a permanent quota increase.

## First creative-writing-specific evidence

A [writer's Nov. 10 ToneBench report](https://www.reddit.com/r/ClaudeAI/comments/1xsk4qj/claude_fable_52_is_a_big_upgrade_over_51/) tested all five efforts on a multi-judge script-writing evaluation:

| Effort | ToneBench Elo | Measured API cost/script | Time |
|---|---:|---:|---:|
| Low | 2416 | $0.46 | 1.4 min |
| Medium | 2426 | $0.56 | 1.8 min |
| High | 2520 | $1.22 | 4 min |
| XHigh | **2676** | $2.22 | 7 min |
| Max | 2651 | $5.75 | 20 min |

Their account: Fable 5.2 was less generically wordy, gave clearer visual cues, better script structure and length control than 5.1, **but did not improve tone compliance**. In their own result, **Opus 5.5 XHigh tied Fable 5.2 XHigh at $1.00 versus $2.22 per script**. Importantly, the score uplift was driven heavily by one LLM judge (GPT-6.1 Sol), and their sole human-typed judge scored 5.2 below 5.1.

This is a valuable **task-specific** comparison but not a blinded human preference study and not Caelmor canon verification. The general AA index says **High** is the efficiency sweet spot; this private script benchmark says **XHigh** may be worth it for a particular creative rubric. Both can be true.

**Conclusion for lore:** Fable 5.2 is a serious **quest-causality, source-conflict, branching-logic and structural-revision challenger**. There is currently insufficient evidence to promote it as the best voice, dialogue, mythic prose or persistent canon writer.

## Subscription access, Nov. 9–16 launch offer

Official permanent policy: [Fable on your Claude plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan).

- **Claude Pro ($20)**: Fable normally uses **pay-as-you-go credits**, not the included subscription pool.
- **Claude Max/Ultra**: Fable is included up to **50% of the shared weekly usage limit** (not an extra 50% added allowance); usage consumes subscription quota more quickly.
- **Temporary Nov. 9–16, 2026 offer**: eligible Pro users get Fable included within up to 50% of weekly usage and one Fable limit reset. After Nov. 16 11:59 p.m. PT, Fable returns to credits on Pro.
- **Max/Ultra temporary reset**: 1–3 Fable resets depending on subscription tenure, expiring Mar. 8, 2027; a Fable reset restores weekly Fable-attributed usage but not weekly usage on other models, while refilling the entire five-hour limit where applicable.
- Nov. 10 **separate full all-model reset** reported by Anthropic; expires Dec. 10, 2026. Check `Settings → Usage` for eligibility and actual reset controls.
- The launch promotion covers **Fable 5, 5.1 and 5.2**, so trialing Fable this week is attractive; do not infer steady-state affordability from the promotion.

Source: [Official Fable 5.2 launch offer and reset mechanics](https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers).

## Routing recommendation

| Work type | Starting model | When to try Fable 5.2 | Not recommended |
|---|---|---|---|
| Caelmor regional lore / atmospheric prose | Opus 5.5 High or Gemini Argon/Flash candidate | Independent sample author, if blind preference demands it | Making Fable Max routine prose default |
| Caelmor quest dependencies, moral tradeoffs, branching consequence logic | Opus 5.5 or Fable 5.2 **Medium/High** | Complicated interdependent quest design and contradictions | Using general intelligence score as prose quality proof |
| Long-lore source reconciliation / canon-conflict audit | Fable 5.2 Medium/High for a **bounded audit** | When cheaper reviewer misses semantic inconsistencies | Allowing the audit to invent established canon |
| Routine dialogue variants, labels, summaries | Gemini 3.8 Flash / Sonnet 5.5 / Haiku extraction | Rarely | Spending Fable quotas on mechanical copy |
| High-risk systems architecture / intractable engineering | Fable 5.2 High | Escalate XHigh only on observed need; Max exceptionally | Huge speculative Fable subagent fanout |
| Daily Claude Code implementation | Opus 5.5/Sonnet 5.5 | Specific hard blocker or high-leverage review | Fable 5.2 Max for repetitive implementation |

**Suggested experiment:** freeze an approved Caelmor lore packet and one quest brief; compare Opus 5.5 High, Fable 5.2 Medium, Fable 5.2 High, and Gemini 3.8 Flash High. First score grounded canon constraints; next score dialogue/voice, atmosphere, meaningful player choices and revision fidelity; last compare actual subscription percentage / API cost / human correction minutes. Keep the owner's prior blind narrative protocol as the authority.

## Confidence and updates

- Model identity, pricing, access, provider releases: **high**.
- Independent broad benchmark capability/cost at measured efforts: **high for that benchmark, not creative work**.
- Launch-week community quality consensus: **low** due to two days of small, conflicting samples.
- Fable 5.2 creative-writing superiority over Opus 5.5 or Gemini: **unproven**.
- Five-hour allowance multiplier or stable dollars/task for personal work: **unknown**.

Revisit after two weeks of independent matched user reports and, ideally, a recorded owner Caelmor A/B artifact. Preserve the prior Fable 5.1 evidence as **historical**, not erased.
