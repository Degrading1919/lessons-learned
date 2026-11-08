# Gemini vs Claude for Caelmor — subscription yield, Flash writing, and canon grounding

**As of:** 2026-11-08  
**Evidence class:** public research prior; *not* the owner's matched usage comparison or narrative preference case.  
**Question:** Is Google AI Pro/Ultra a better creative-writing subscription than Claude Pro/Max/Ultra for lore, dialogue, source-constrained quests, and iterative creative direction?

## Executive conclusion

**Pilot Google AI Pro ($19.99/mo) before cancelling Claude; favor Gemini 3.8 Flash High for high-volume prose and Gemini 4 Argon High for difficult creative drafts.** For actual Caelmor quests, still require a separately sourced canon gate. Opus 5.5 remains the known writing incumbent, not a proven winner or a proven nerf.

This is a much stronger writing proposition than the headline "Gemini 4 vs Opus" contest suggests: the smaller **Gemini 3.8 Flash High is #9 on current human Arena Creative Writing at 1489±7**, statistically close to several older Opus models, at $0.75/$3.75 per million input/output API tokens. GPT-6 Astra Max ranks much lower on *this human-preference category* despite extremely strong general benchmarks. General scientific/coding intelligence is not a synonym for fantasy prose preference.

However, do **not** assume Google has categorically more coding-agent quota. Both vendors use five-hour plus weekly limits, dynamic workload accounting, and capacity adjustments. Google *Antigravity* and the *Gemini web app* have separate meters; Google retired the old consumer-auth Gemini CLI in June 2026 in favor of Antigravity CLI.

## Price, quota, and interface comparison

| Product | US subscription | Published quota/reset principles | Material caveat |
|---|---:|---|---|
| **Google AI Pro** | $19.99/mo | 4x free Gemini-app usage, 1M chat context; rolling 5-hour allowance plus weekly cap. Antigravity Pro has a higher baseline 5-hour+weekly agent quota. | **Different app and Antigravity meters**; no public universal prompts/5h count. Gemini Flash-Lite remains available in chat after higher-tier cap. |
| **Google AI Ultra** | $99.99/mo | 5x Google AI Pro app usage; Antigravity highest baseline/weekly allowance; expanded access to Argon. | 5x is relative to **Google Pro**, not Claude Pro; some Ultra products/offerings have separate limits. |
| **Claude Pro** | $20/mo | Shared Claude chat/desktop/Code 5-hour and weekly allowance. | Effort, chat length, tools and project sources consume the same pool. |
| **Claude Max** | $100/mo | 5x Claude Pro every 5h and weekly, separate weekly Fable allowance. | Includes $100/month **claimable Claude API credits** after eligibility; those are for API, not an extension of chat/Code quota. |
| **Claude Ultra** | $200/mo | 10x Claude Pro weekly; verified accounts have **no five-hour limit** but still a weekly limit and separate Fable cap. | $200 monthly. Former Max 20x; not a $100 Ultra comparison. Includes $200/month claimable API credits. |

Official sources:
- [Gemini apps limits](https://support.google.com/gemini/answer/16275805)
- [Google One AI plans](https://one.google.com/about/google-ai-plans/)
- [Antigravity plans](https://www.antigravity.google/docs/plans)
- [Google AI Pro/Antigravity overage](https://support.google.com/googleone/answer/14534406)
- [Gemini CLI consumer auth deprecation June 18](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals)
- [Claude shared five-hour/weekly limits](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- [Claude Max](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- [Claude Ultra](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan)
- [Claude monthly API credits](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)

**Do not infer exact quota ratios between providers.** A "5x" label is internally relative. A 5-hour % in one product does not map to the same amount of computation in another.

## The "Gemini 3.5" name

Most positive "3.5" usage reports concern **Gemini 3.5 Flash** (often **Medium** effort in Antigravity), released May 19. Google introduced newer **3.6, 3.7, 3.8 Flash** models subsequently; Gemini 3.8 Flash is the more directly relevant *current* fast writer. Google announced 3.5 Pro but the public November active API model list does not establish a generally available 3.5 Pro.

- [Gemini 3.5 Flash announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)
- [Gemini API current and deprecated model list](https://ai.google.dev/gemini-api/docs/deprecations)

## Human subscription/agent experiences — evidence for and against

| Dated user report | Observed outcome | Scope/caveat |
|---|---|---|
| [May 24: Flash 3.5 Medium](https://www.reddit.com/r/google_antigravity/comments/1tm8iug/i_really_like_flash_35_medium_it_still_lasts/) | After a week of tooling/prompt adjustments, user reports executing 5+ pre-planned coding changes while Antigravity usage remained at 100%, with fewer major review findings. Explicitly prefers Medium and a separate planner. | One user's adapted extension/harness, not a default first-party consumption rate. |
| [May 22: Flash 3.5 broad versatility](https://www.reddit.com/r/google_antigravity/comments/1tkkssm/flash_35_just_super_good_dont_want_to_use_pro/) | Users praise Flutter projects, code documentation and multi-tool PDF/spreadsheet/authenticated-web workflows, some finishing quicker than Codex/Claude. | Other comments in same thread complain of exhausting quota in about an hour. |
| [Oct 27: 3.8 Medium across coursework/Obsidian](https://www.reddit.com/r/google_antigravity/comments/1xh8eet/how_are_you_using_ag_to_go_through_your_usage/) | Pro subscriber reports only ~10% weekly use across ~14 conversations, PDF/image reading, coding, plots and source notes. | Light-to-moderate workload; not nonstop autonomous coding. |
| [Oct 31: measured 3.8 Antigravity](https://www.reddit.com/r/google_antigravity/comments/1xk8jm1/i_did_the_math_on_google_antigravitys_token/) | 55 generations, 2.6M cached and 199K uncached input, 24.8K output cost ~1% five-hour. A heavy 112-generation run cost ~7% five-hour and ~3% weekly. | Single Pro account, significant custom rules/MCPs and 256K **harness** context; reported percentage/accounting is not a Google guarantee. |
| [Nov 1: Antigravity sudden burn](https://www.reddit.com/r/GeminiAI/comments/1xkz4da/antigravity_changed_from_low_to_high_usage_pro/) | User reports ~1% per two minutes and weekly quota trajectory of two days; commenter reports Argon Low only 10–15 queries or Medium ~5 before limit. | Anecdotal, may reflect teamwork/agent settings, account routing, capacity or model. |
| [Nov 7: contradictory Argon mileage](https://www.reddit.com/r/Googlebook/comments/1xqa7pw/antigravity_pro_plan_usage_limits_are_nowgenerous/) | One user reports hour of Argon app building with 99% allowance remaining; another says hit limits after four days; another exhausted a window after ~3 hours. | Mutually conflicting product/account observations; don't average them as a universal claim. |
| [Oct 21: switch Google → Claude](https://www.reddit.com/r/google_antigravity/comments/1xbkevo/switched_from_geminiantigravity_to_claude_after_3/) | A high-volume user reports roughly 3x **more** work on Claude at comparable 5x subscription tier, citing better trust, fewer corrections and cleaner agentic tool work. | Opposite of "Google always lasts longer"; API/client workload not controlled. |
| [Oct 18–Nov 8: Claude limit concerns](https://www.reddit.com/r/ClaudeCode/comments/1x99xhm/have_the_limits_been_lowered_significantly_since/), [Oct 23 usage measurement](https://www.reddit.com/r/ClaudeCode/comments/1xdoal7/did_claude_code_usage_limits_get_stricter_again/), [Nov 8 fresh discussion](https://www.reddit.com/r/ClaudeCode/comments/1xqqco0/anyone_else_hitting_usage_limits_quicker_last/) | Multiple users report faster weekly depletion, e.g., one describes 42% of session using 11% of weekly allowance on Opus High. Others see no change. | Real recent cluster, but **no provider-confirmed universal 2026 quota reduction**; compute accounting/effort/context changes are possible. |

**Conclusion on quota:** Google's Flash series offers credible reports of exceptional task yield, and Claude's recent usage complaints are serious. Yet Antigravity also has longstanding quota volatility and some users experience *better* work-per-limit in Claude. For primarily **non-agentic fiction in Gemini app**, Google Pro is more attractive than the Antigravity coding reports would alone imply. Do not mix these two task modalities in one claim.

## Human creative-writing scores (November 8 Arena)

Source: [Arena creative writing, blind human votes](https://arena.ai/leaderboard/chat/text/creative-writing). Scores include uncertainty and update continuously. The ranking below is a task-specific preference prior, not Caelmor canon verification.

| Model and effort | Human score | Published API input/output per 1M | Creative role hypothesis |
|---|---:|---:|---|
| Gemini 4 Argon High | **1526 ±10** | $2 / $10 | premium prose challenger |
| Claude Opus 5.5 High | **1517 ±12** | $4 / $20 | incumbent prose |
| Claude Opus 4.6 High | 1498 ±6 | $5 / $25 | older Claude literary style control |
| **Gemini 3.8 Flash High** | **1489 ±7** | **$0.75 / $3.75** | **low-cost high-quality prose and drafts** |
| Gemini 3.7 Flash High | 1487 ±8 | $0.75 / $3.75 | lower-cost historical comparator |
| Gemini 3.5 Flash Medium | 1469 ±7 | $0.75 / $4.50 | lower-effort draft/revision candidate |
| Claude Sonnet 5.5 XHigh | 1465 ±12 | $2 / $10 | dialogue/quest rewrite worker; not automatically a better writer than Flash |
| Gemini 3.5 Flash High | 1465 ±7 | $0.75 / $4.50 | lower-cost historical comparator |
| Gemini 3.5 Flash-Lite | 1436 ±8 | $0.15 / $1.25 | summaries/metadata, not primary prose |
| Claude Haiku 5.5 High | **1363 ±12** | **$0.10 / $0.50** (<100K inputs) | extraction, labels, light edits; **not** default Caelmor author |

Notes:
- Gemini 3.8 Flash is **28 score points below** Opus 5.5, so it is not statistically tied with Opus 5.5; it *is* statistically close to Opus 4.7 High and the broad score region of Opus 4.6.
- The human leaderboard is **not** a direct test of reliable multi-scene continuity, source citations, or respecting conflicting canon.
- API pricing is **not** the number of prompts allowed on subscriptions. Raw $/M prices are mainly useful for a future overflow/BYOK comparison.
- Some scores marked preliminary on Arena (including Flash 3.8) must remain public priors, not owner facts.
- A [user-built 600-sample 12-genre creative-writing evaluation](https://www.reddit.com/r/GeminiAI/comments/1wbd7va/best_creative_writing_models_of_2026_v3_17_models/) names Gemini 3.8 Flash the style/pacing MVP and GLM 5.3 better at worldbuilding logic. This is a creator-defined, not independent, matched Caelmor test.
- A writer in [r/WritingWithAI](https://www.reddit.com/r/WritingWithAI/comments/1vsn02e/gemini_37_flash_is_surprisingly_good/) switched ideation/organization to Flash, praising concision and idea integration; others report [flat emotional loops](https://www.reddit.com/r/GeminiAI/comments/1vectc9/anyone_else_finding_geminis_rpcreative_writing_a/) and [lost POV/story instructions](https://www.reddit.com/r/GeminiAI/comments/1ryp826/gemini_piss_me_off_creative_writing/).
- One [Reddit story discussion](https://www.reddit.com/r/GeminiAI/comments/1wldbe6/thank_you_gemini_just_what_my_story_needed/) reports abrupt safety/wellness pivots on explicitly fictional content; other writers say Gemini 3.8 improved creativity but guardrails remain task/surface-sensitive.

## Canon / documents / cache

**Google Gems is a good Caelmor fit in concept:**

- Set a distinct Gem instruction profile for tone/voice and hard source authority.
- Attach **approved region/character/quest docs from Google Drive** as Knowledge.
- Google says Gems use the **latest Drive version** when those documents change.
- Gemini AI Pro/Ultra app supports a 1M-token nominal context.
- Use targeted chapter/scene source packets, not a giant undifferentiated lore dump.
- Require explicit `ESTABLISHED / PROPOSED / CONFLICT / UNKNOWN` labeling for all new facts.
- Blind-check at least one existing source conflict and one delayed callback across several scenes, including a narrow revision that preserves everything else.

Sources:
- [Gems with Drive sources and update behavior](https://support.google.com/gemini/answer/15146780)
- [Gemini app upload limits and GitHub repo option](https://support.google.com/gemini/answer/14903178)
- [Gemini app context and history accounting](https://support.google.com/gemini/answer/16275805)

**1M context is not a guarantee of accurate recall.** Also, user-visible Gemini app persistence and Google Drive update propagation are not equivalent to **API prompt-cache discount**; don't claim invisible consumer cache hit rates. The Antigravity agent surface may expose only ~256K usable context in its own tool-heavy session, regardless of the base model's theoretical 1M.

The alternative model's biggest risk for Caelmor is a **beautiful invented connection between canon sources**. One [heavy cross-provider user's report](https://www.reddit.com/r/GeminiAI/comments/1udul3d/after_months_of_using_claude_chatgpt_gemini_and/) identifies precisely this kind of long-context instruction/condition mixing; it is strong qualitative caution, not an error-rate estimate.

## Recommended subscription decision

**If the main goal is creative lore, dialogue and constrained story development:** Trial **Google AI Pro ($19.99/month)** with a *Gemini Gem linked to approved Drive lore*, **3.8 Flash High** for drafting/revision, **Argon High** for difficult scenes. Do **not** immediately pay $99.99 for Ultra; the pay-for-usage case isn't established without actual Pro quota data.

**If the main goal is unattended repo changes / tool-heavy Claude Code:** Claude Max may still deliver more useful accepted work; a Google Antigravity quota meter does not equal the Gemini app meter, and recent users report both directions.

**Before canceling Claude:** Three side-by-side, identically sourced scenes/quest tasks, blind preference with canon hard gate, plus quota before/after and human revision time. Do not compare one Claude long session against a fresh Gemini session; freeze the same source bundle.

**Decision threshold:** Switch narrative subscription if **3.8 Flash / Argon** pass the canon gate at comparable or better quality, produce less human editing, and the included Pro quota lasts through a representative week. Keep Claude if it wins crucial quest causality or if Google loses source constraints during edits.

This report is a **dated public prior**, not a confirmed subscription winner.
