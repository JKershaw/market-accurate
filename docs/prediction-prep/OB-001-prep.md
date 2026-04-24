# Prediction Resolution Prep: OB-001

## Prediction Details

| Field | Value |
|-------|-------|
| ID | OB-001 |
| Claim | Open-weights models maintain parity (<2 point gap on MMLU, HumanEval, GSM8K) with proprietary frontier through 2026 |
| Made | 2026-01-03 |
| Resolves | December 31, 2026 |
| Status | Pending — Resolution Prep |

---

## Threshold Interpretation

Resolution requires:
- **CORRECT:** At end of 2026, the best open-weights model is within 2 points (absolute) of the best proprietary frontier model on each of MMLU, HumanEval, and GSM8K
- **INCORRECT:** On any of the three benchmarks, the best proprietary model opens a >2-point gap over the best open-weights model

**Key points:**
- "Best proprietary" = highest reported score on the benchmark (OpenAI, Anthropic, Google, xAI, or any other closed-source provider)
- "Best open-weights" = highest reported score for any model with openly released weights under a permissive license
- "Parity" = absolute score difference ≤ 2.0 points
- Gap measured at **end of 2026** — not an average across the year. A temporary gap that closes by Dec 31 does not resolve INCORRECT.

---

## Baseline as of Publication (Jan 2026)

Gap at publication (from [open-source-benchmarks-2026-01.md](/analysis/open-source-benchmarks-2026-01.md)):

| Benchmark | Best Proprietary | Score | Best Open | Score | Gap |
|-----------|------------------|-------|-----------|-------|-----|
| MMLU | GPT-4o / Claude 3.5 | 88.7% | DeepSeek-R1 | 90.8% | -2.1 (open leads) |
| HumanEval | o1 | 92.4% | DeepSeek-R1 | 96.3% | -3.9 (open leads) |
| GSM8K | o1 | 94.8% | DeepSeek-R1 | 97.3% | -2.5 (open leads) |

**Starting position favors CORRECT.** Open-weights leads or is at parity on all three. The path to INCORRECT requires a ≥2-point proprietary lead on at least one benchmark by Dec 31, 2026.

---

## Benchmark Specifications

### MMLU (Massive Multitask Language Understanding)

- 57 tasks covering STEM, humanities, social sciences, etc.
- 5-shot evaluation standard
- Use 0-shot CoT as an alternative only if that is what the model's release reports
- Source: [Papers With Code MMLU leaderboard](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu)

### HumanEval

- 164 Python programming problems
- Pass@1 as the primary metric
- Source: official OpenAI HumanEval repo and releases

### GSM8K

- 8.5K grade-school math word problems
- Chain-of-thought 8-shot standard
- Source: model technical reports and leaderboards

**Note on benchmark saturation:** MMLU is approaching saturation. Multiple frontier models now score in the 87–92% range, and differences may be within noise. At resolution time, if both best open and best proprietary are ≥90%, treat small differences with appropriate skepticism — record the comparison but flag the noise-floor concern.

### Handling alternative benchmarks

If MMLU becomes deprecated or superseded (e.g., MMLU-Pro replaces it fully in the community), the prep document governs: the default is to resolve against the original benchmarks. Only substitute if a clear community consensus (Papers With Code, leading labs) has moved to a replacement.

---

## Data Collection Protocol

### Step 1: Identify best-of-year scores

By Dec 31, 2026:

| Benchmark | Best Proprietary (2026) | Score | Best Open (2026) | Score | Gap | Verdict |
|-----------|--------------------------|-------|-------------------|-------|-----|---------|
| MMLU | TBD | TBD | TBD | TBD | TBD | TBD |
| HumanEval | TBD | TBD | TBD | TBD | TBD | TBD |
| GSM8K | TBD | TBD | TBD | TBD | TBD | TBD |

### Step 2: Source verification

For each score:
- Primary: model technical report or blog from releasing organization
- Secondary: Papers With Code, HuggingFace leaderboard, Artificial Analysis
- Tertiary: independent replications by researchers

Avoid vendor-reported scores that cannot be replicated. Prefer recent independent evaluations.

### Step 3: License verification

A model counts as "open-weights" only if:
- Weights are downloadable under a license that permits use (Llama, MIT, Apache, or similar)
- "Open API" is not sufficient (no weights access)
- "Research-only" or restricted-commercial licenses still count as open-weights

Models with partial releases (instruct-tuned public, base private) count as open if the publicly released variant achieves the score.

---

## Edge Cases

| Case | Handling |
|------|----------|
| Proprietary model reports score without released weights | Counts as proprietary |
| Open model reports score but weights not yet released | Does NOT count until weights are public |
| Fine-tuned variant of open model scores higher than base | Counts as open-weights |
| Proprietary model gated behind high pricing / enterprise-only | Still proprietary — gating doesn't change category |
| Model from a Chinese lab (DeepSeek, Qwen) with uncertain licensing | Counts as open if weights are public and technically usable, regardless of export-control concerns |
| A new benchmark version (MMLU → MMLU-Pro) | Use original MMLU if still published; default to original |

---

## Interim Check (April 2026)

Models released or updated in Q1 2026 (directional; verify at resolution):

- GPT-5 variants (OpenAI, Feb 2026) — new proprietary baseline
- Claude 4 family (Anthropic, Q1 2026) — new proprietary baseline
- Gemini 2.5 (Google, Q1 2026) — new proprietary baseline
- DeepSeek-V4 or R2 (expected H1 2026) — key open-weights candidate
- Llama 4 (Meta, expected 2026) — key open-weights candidate
- Qwen 3 series (Alibaba, Q1 2026) — key open-weights candidate

**Current read:** Proprietary frontier has advanced (GPT-5 reportedly scores in 92–94% MMLU range; Claude 4 similar). Open-weights DeepSeek-V4 has been reported to achieve 91–93% MMLU. Gap appears to have widened slightly from -2.1 (open leading) toward ~+1 (proprietary marginally ahead) — but still under the 2-point threshold.

Updated subjective probability of CORRECT: **~65%** (up from original ~55%, because the proprietary advances through Q1 2026 have been matched within the 2-point threshold by rapid open-weights releases).

---

## Risk Factors

Reasons OB-001 could resolve INCORRECT:

1. **Proprietary labs accelerate inference-time compute advantage** (o-series reasoning models): if reasoning at inference doubles effective capability, benchmarks may reflect this even when base model weights are similar quality
2. **Open-weights labs lose momentum** — DeepSeek faces export controls, Meta's Llama team restructures, Alibaba/Qwen slows
3. **Data contamination detected** — If open-weights models are found to have benchmark data in training, scores may need retraction
4. **Closed labs release narrow-domain models** that dominate specific benchmarks

Reasons OB-001 likely resolves CORRECT:

1. Open-weights lead on all three benchmarks as of Jan 2026 — proprietary would need to open a 2+ point gap *and* open-weights not respond
2. Knowledge distillation makes proprietary advances rapidly diffuse to open-weights
3. Training cost continues falling — more labs can afford frontier-class training
4. Saturation means 2-point gaps are hard to open on benchmarks near 90–95%

---

## Resolution Checklist

- [ ] Collect best-of-year scores on MMLU, HumanEval, GSM8K for both proprietary and open-weights
- [ ] Verify license status for open-weights candidates
- [ ] Verify sources are reliable (technical reports, not marketing claims)
- [ ] Compute gap per benchmark
- [ ] Apply ≤2-point parity rule on all three
- [ ] Update predictions/tracker.md
- [ ] Update analysis/open-source-benchmarks-2026-01.md Track Record
- [ ] Update ai-valuation-2026-01.md if relevant (OB-001 supports AV-003)
- [ ] Commit: "Resolve: OB-001 — {outcome summary}"

---

## Sources

- [Papers With Code MMLU](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu)
- [Papers With Code HumanEval](https://paperswithcode.com/sota/code-generation-on-humaneval)
- [Papers With Code GSM8K](https://paperswithcode.com/sota/arithmetic-reasoning-on-gsm8k)
- [HuggingFace Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [Artificial Analysis](https://artificialanalysis.ai/)
- [LMSYS / Chatbot Arena](https://chat.lmsys.org/)
- Model technical reports (linked from official lab pages)

---

*Prepared: 2026-04-24*
