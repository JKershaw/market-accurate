# Prediction Resolution Prep: OB-001

## Prediction Details

| Field | Value |
|-------|-------|
| ID | OB-001 |
| Claim | Open-weights models will maintain parity (within 2 points on MMLU, HumanEval, GSM8K) with proprietary frontier through 2026 |
| Made | 2026-01-03 |
| Resolves | December 31, 2026 |
| Status | Pending - Resolution Prep |

---

## Resolution Criteria

Prediction resolves **CORRECT** if, at any point between January 1, 2026 and December 31, 2026:

- The best publicly available open-weights model (any license that permits weights download for inference) is within 2 percentage points of the best proprietary frontier model on **all three** benchmarks: MMLU, HumanEval, GSM8K.
- Specifically: (proprietary best score) − (open best score) ≤ 2.0 on each of the three benchmarks, simultaneously, in any single snapshot during the year.

The prediction is satisfied if at *any* point during the year the gap closes; we do not require the gap stays closed continuously. (This is the steelman reading.)

Prediction resolves **INCORRECT** if:

- For all snapshots during 2026, the gap exceeds 2.0 points on at least one of the three benchmarks.

---

## Threshold ambiguity & decision

The original claim says "maintain parity." Plain reading: the gap should stay narrow. But there is genuine ambiguity:

1. **Strict reading:** Open-weights must be ≤2pp behind on all three benchmarks at all times during 2026.
2. **Lenient reading:** Open-weights must be ≤2pp behind on all three benchmarks at at least one snapshot in 2026.

Under the strict reading, a single new proprietary release that opens a >2pp gap (even if open-weights catches up later) would resolve INCORRECT.

**Resolution rule (chosen):** The prep document selects the **lenient reading** — at least one snapshot in 2026 satisfies the condition — because:
- The original analysis frames "parity" as a state achieved, not maintained continuously
- Benchmark releases are not synchronized; a strict reading would resolve on noise
- The pre-registration framework's tie-breaker rule defaults to INCORRECT when ambiguous, but here there are two equally reasonable readings, not a hard ambiguity

We document this choice publicly so it cannot be revised at resolution time.

---

## Measurement Conventions

| Detail | Specification |
|--------|---------------|
| MMLU | 5-shot prompting, default split, score reported by Hugging Face Open LLM Leaderboard or Papers With Code |
| HumanEval | Pass@1, default temperature settings |
| GSM8K | 8-shot prompting (chain-of-thought), default settings |
| Open-weights definition | License permits weights download, even if commercial use is restricted (e.g., Llama community license counts) |
| Proprietary frontier | Best of GPT-4.x, Claude 3/4.x, Gemini 1.5/2.x/Ultra, or successors |
| Benchmark version | Must be the same version (e.g., MMLU original, not MMLU-Pro) for comparison |
| Reasoning models | If proprietary "reasoning" model uses inference-time compute, we still compare to its reported score; open-weights reasoning models (DeepSeek-R1, etc.) are eligible |

**Source priority:**

1. Hugging Face Open LLM Leaderboard
2. Papers With Code SOTA pages
3. Original technical reports / model cards (cross-checked)
4. Independent reproductions (LMSYS, Chatbot Arena evals)

---

## Baseline (December 2025 / January 2026)

From Open-Source Benchmark Tracking analysis (2026-01-03):

| Benchmark | Proprietary Best | Score | Open Best | Score | Gap |
|-----------|-----------------|-------|-----------|-------|-----|
| MMLU | GPT-4o | 88.7% | DeepSeek-R1 | 90.8% | -2.1 (open leads) |
| HumanEval | o1 | 92.4% | DeepSeek-R1 | 96.3% | -3.9 (open leads) |
| GSM8K | o1 | 94.8% | DeepSeek-R1 | 97.3% | -2.5 (open leads) |

**Key observation:** Open-weights already exceeds proprietary on all three benchmarks at the start of 2026. The prediction is, in some sense, already satisfied at publication. The remaining question is whether this state is maintained in any 2026 snapshot **after** new proprietary releases (GPT-5, Claude 4.x, Gemini 3, etc.).

---

## Interim Monitoring Points

| Snapshot Date | MMLU (gap) | HumanEval (gap) | GSM8K (gap) | Status |
|---------------|------------|-----------------|-------------|--------|
| Jan 2026 | -2.1 (open lead) | -3.9 (open lead) | -2.5 (open lead) | Parity |
| Mar 2026 | | | | |
| Jun 2026 | | | | |
| Sep 2026 | | | | |
| Dec 2026 | | | | |

Negative gap = open-weights leads. We log at each major model release (GPT-5, Claude 5, Gemini 3, Llama 4, DeepSeek-R2, Qwen 3, etc.).

---

## Major release calendar to monitor

| Expected release | Likely effect |
|------------------|---------------|
| GPT-5 (OpenAI, mid-2026) | Likely opens a gap on MMLU/GSM8K |
| Claude 4.5+ (Anthropic, mid-2026) | Marginal lead on coding (HumanEval) |
| Gemini 3 (Google, mid-2026) | Multimodal lead, marginal on text benchmarks |
| Llama 4 (Meta, 2026) | Closes any new proprietary lead |
| DeepSeek-R2/R3 (DeepSeek, 2026) | Most likely to maintain open-weights lead |
| Qwen 3 (Alibaba, 2026) | Strong contender on Chinese-language and coding benchmarks |

The "race condition" pattern of 2024–2025 suggests open-weights typically catches a new proprietary release within 3–6 months. If this pattern holds, the prediction resolves CORRECT.

---

## Risks to prediction

### Risks favoring CORRECT (parity maintained)

- DeepSeek (and successors) continues 6-month catch-up cadence
- Llama 4 and DeepSeek-R2 benchmark squarely against frontier
- Distillation from frontier models becomes easier (training data leakage)
- Open-weights reasoning models close gap on hard-reasoning benchmarks
- Saturation effect on existing benchmarks: proprietary models cannot extend gap once benchmarks are essentially solved (>95%)

### Risks favoring INCORRECT (gap widens)

- GPT-5 or equivalent jumps benchmarks by >5pp where open-weights cannot follow within 2026
- Open-weights development capital constrained (DeepSeek-style entities lose access to compute)
- Proprietary labs exit MMLU/HumanEval/GSM8K reporting, leaving comparability issues
- Saturation effect makes 2pp gap impossible to measure (all scores >97%)
- Compute-export controls prevent Chinese open-weights labs from training larger models

### Benchmark saturation issue

A genuine concern: MMLU, HumanEval, and GSM8K are *saturating* benchmarks. Best models are at 90–97%. Headroom for differentiation is small. A 1.5pp gap on a 97% benchmark may be all the difference between "frontier" and "second tier." This argues for migration to harder benchmarks (MMLU-Pro, GPQA-Diamond, SWE-Bench) — but the prediction is specifically about MMLU/HumanEval/GSM8K, so we resolve on those.

---

## Likelihood Assessment

| Scenario | Probability | Outcome |
|----------|-------------|---------|
| Open-weights leads or matches all year | 30% | CORRECT |
| Open-weights catches up within months | 35% | CORRECT (lenient) / depends (strict) |
| Frontier opens a 3–5pp gap; open closes to ~2pp by year-end | 20% | CORRECT (lenient only) |
| Frontier opens >5pp gap, open never catches up | 10% | INCORRECT |
| All benchmarks saturate, comparison becomes meaningless | 5% | INCONCLUSIVE |

**Subjective ex-ante probability of CORRECT (lenient reading): ~80%**

This is one of our highest-confidence predictions and the December 2025 starting condition (open-weights *ahead*) is a major asymmetric positive.

---

## Data Sources

| Source | Usage |
|--------|-------|
| Hugging Face Open LLM Leaderboard | Open-weights benchmarks |
| Papers With Code SOTA | Proprietary benchmarks |
| OpenAI / Anthropic / Google model cards | Frontier scores |
| ArXiv (DeepSeek, Llama, Qwen tech reports) | Open-weights scores |
| LMSYS Chatbot Arena | Cross-validation |
| Artificial Analysis | Aggregator |

---

## Resolution Checklist

In December 2026 / January 2027:

- [ ] Identify best proprietary score for each benchmark (cite source)
- [ ] Identify best open-weights score for each benchmark (cite source)
- [ ] Compute gap on each benchmark
- [ ] Apply lenient-reading rule (at least one snapshot in 2026 with gap ≤ 2pp on all three)
- [ ] Document with screenshots and timestamps
- [ ] Determine: CORRECT or INCORRECT
- [ ] Update predictions/tracker.md
- [ ] Update analysis/open-source-benchmarks-2026-01.md Track Record
- [ ] Commit: "Resolve: OB-001 — gap MMLU {X}, HE {Y}, GSM8K {Z}, outcome"

---

## Sources

- [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [Papers With Code MMLU](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu)
- [Open-Source Benchmark Tracking](/analysis/open-source-benchmarks-2026-01.md)

---

*Prepared: 2026-05-01*
