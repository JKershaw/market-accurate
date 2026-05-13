# Prediction Resolution Prep: AV-003

## Prediction Details

| Field | Value |
|-------|-------|
| ID | AV-003 |
| Claim | By June 2026, an open-weights model will match or exceed GPT-4 (March 2023) on MMLU, HumanEval, and GSM8K while running inference on a single consumer GPU (RTX 4090 class) |
| Made | 2026-01-03 |
| Resolves | June 30, 2026 |
| Status | Pending - Resolution Prep |

---

## Resolution Criteria

Prediction resolves **CORRECT** if a single open-weights model released before June 30, 2026 satisfies ALL of:

1. **MMLU ≥ 86.4%** (GPT-4 March 2023 score)
2. **HumanEval ≥ 67.0%** (GPT-4 March 2023 score)
3. **GSM8K ≥ 92.0%** (GPT-4 March 2023 score)
4. **Runs on RTX 4090** (24GB VRAM, consumer retail) with any quantization producing scores above

All four conditions must be met by **the same model** at the same quantization level.

Prediction resolves **INCORRECT** if no single model meeting these criteria exists by June 30, 2026.

---

## Current State (as of January 2026 publication)

Per the Open-Source Benchmarks analysis:

| Model | Size | Quantization | VRAM | MMLU | HumanEval | GSM8K |
|-------|------|--------------|------|------|-----------|-------|
| GPT-4 (Mar 2023) | — | proprietary | N/A | 86.4% | 67.0% | 92.0% |
| Llama 3.1 70B | 70B | Q4 | 22GB | 82.0% | 81.7% | 93.0% |
| Qwen 2.5 32B | 32B | Q4 | 20GB | 83.3% | 79.8% | 91.2% |
| DeepSeek-R1-Distill-32B | 32B | Q4 | 20GB | 87.5% | 85.4% | 95.6% |

**Preliminary read:** DeepSeek-R1-Distill-32B (released Jan 2025) already appears to satisfy all three benchmark thresholds on a Q4-quantized weight set that fits in 20GB. Prediction likely resolves CORRECT.

---

## Key Verification Requirements

The claim hinges on **reproducibility**, not just benchmark leaderboard numbers. Before resolving CORRECT, verify:

### 1. Benchmark integrity

| Risk | Mitigation |
|------|-----------|
| Benchmark contamination | Check model card for training data disclosure |
| Cherry-picked eval runs | Require at least two independent reproductions |
| Quantized score drop | Run benchmarks on the actual Q4 weights, not FP16 reference |

### 2. Hardware reproducibility

| Risk | Mitigation |
|------|-----------|
| Multi-GPU setup passed off as single | Require explicit single-GPU inference configs |
| VRAM limits exceeded via CPU offload | Require full-model-in-VRAM deployment |
| Exotic quantization not broadly usable | Require format usable in llama.cpp, vLLM, or Ollama |

### 3. Inference quality

| Risk | Mitigation |
|------|-----------|
| Low-throughput inference not practical | Require ≥5 tokens/sec on RTX 4090 |
| Context window degraded at quant | Require ≥8k usable context |

---

## Data Collection Protocol

### Step 1: Identify candidate models (as of resolution date)

Sources:
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [r/LocalLLaMA weekly roundups](https://www.reddit.com/r/LocalLLaMA/)
- HuggingFace model tags: `gguf`, `Q4_K_M`, `<35B`
- Artificial Analysis consumer-hardware track

### Step 2: Filter to RTX 4090-viable

- Parameter count: ≤35B (Q4 quant fits in 24GB with KV cache)
- Publicly released weights
- Non-commercial acceptability not required; **open-weights** required

### Step 3: Benchmark verification

For each candidate:
- MMLU (5-shot, standard eval)
- HumanEval (pass@1)
- GSM8K (8-shot CoT)

Record:
- Reference source for scores
- Quantization used for reported scores
- Whether Q4-quantized scores match FP16 reference

### Step 4: Community reproduction

Require at least one of:
- LM Eval Harness reproduction on Q4 weights
- Community testing thread with consistent numbers
- Independent leaderboard posting (Artificial Analysis, LMSYS)

---

## Likely Resolution Scenarios

| Scenario | Probability (subjective) | Outcome |
|----------|-------------------------|---------|
| DeepSeek-R1-Distill holds up on clean eval | 60% | CORRECT |
| Newer model (Qwen 3, Llama 4, etc.) clears bar | 30% | CORRECT |
| All candidates fail on one of three benchmarks under strict eval | 8% | INCORRECT |
| Benchmark contamination invalidates top candidates | 2% | INCORRECT |

**Subjective ex-ante probability of CORRECT: ~90%**

---

## Edge Cases to Pre-Resolve

### What counts as "GPT-4 March 2023"?

Use published scores from the OpenAI GPT-4 Technical Report:
- MMLU: 86.4% (5-shot)
- HumanEval: 67.0% (pass@1, zero-shot)
- GSM8K: 92.0% (SFT + CoT prompting)

Do NOT use GPT-4 Turbo or later OpenAI model scores.

### What counts as "consumer GPU (RTX 4090 class)"?

Accept: RTX 4090 (24GB), RTX 5090 (32GB, released late 2024), RTX 4090 Ti
Reject: RTX 6000 Ada, H100, A100, multi-GPU rigs, Mac Studio unified memory

### What counts as "running inference"?

Accept: Full-model weights loaded in VRAM, standard decoding
Reject: CPU offload, RAM-paged inference, multi-GPU sharding, mixture-of-experts routed across devices

---

## Resolution Checklist

On or before June 30, 2026:

- [ ] Identify top 5 candidate open-weights models ≤35B parameters
- [ ] Gather benchmark scores from leaderboards + model cards
- [ ] Verify Q4 weights are publicly downloadable
- [ ] Cross-check community reproductions
- [ ] Apply strict threshold check (all 3 benchmarks)
- [ ] Document one-line summary with model name and scores
- [ ] Determine: CORRECT or INCORRECT
- [ ] Update predictions/tracker.md
- [ ] Update analysis/open-source-benchmarks-2026-01.md Track Record
- [ ] Commit: "Resolve: AV-003 - {model name, outcome}"

---

## Sources

- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [Papers With Code MMLU](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu)
- [Artificial Analysis](https://artificialanalysis.ai/)
- [Open-Source Benchmarks Analysis](/analysis/open-source-benchmarks-2026-01.md)

---

*Prepared: 2026-04-18*

---

## Addendum (May 8, 2026): Updated candidate list (T-53 days)

With ~7 weeks until resolution, the field of qualifying candidates has expanded substantially since the April prep. The threshold (MMLU ≥86.4 / HumanEval ≥67 / GSM8K ≥92, single RTX 4090) is now cleared by **multiple** independent models, not just DeepSeek-R1-Distill-32B.

### Current top candidates (open-weights, ≤35B parameters, RTX-4090-viable)

| Model | Params | Quant | RTX 4090 fit | MMLU | HumanEval | GSM8K | Source |
|-------|--------|-------|--------------|------|-----------|-------|--------|
| DeepSeek-R1-Distill-32B | 32B | Q4 | 20GB ✓ | 87.5% | 85.4% | 95.6% | Jan 2025 release; verified by community reproductions |
| Qwen 3 32B | 32B | Q4 | 22GB ✓ (~38 tok/s on RTX 4090) | reported ≥87% | reported ≥85% | reported ≥93% | [Awesome Agents leaderboard](https://awesomeagents.ai/leaderboards/home-gpu-llm-leaderboard/), [ToolHalla 2026 RTX 4090 guide](https://toolhalla.ai/blog/best-local-llms-rtx-4090-2026) |
| Qwen 3 14B | 14B | Q4 | <12GB ✓ | 81.1% | — | — | Below MMLU threshold; flagged for completeness |
| Qwen3.6-27B | 27B | Q4 | ~16GB ✓ | competitive | reported "beats 397B on coding" | — | [BuildFastWithAI](https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026) — needs strict-eval verification |
| Llama 3.3 70B (Q4 K_M) | 70B | Q4_K_M | ~40GB ✗ | 88% | 89% | 90% | Reportedly does **not** fit single 24GB; multi-GPU only — fails AV-003 hardware criterion |

### Verification status

The DeepSeek-R1-Distill-32B candidate alone is sufficient to resolve AV-003 CORRECT subject to the strict-eval verification steps in the original prep doc. As of May 8, 2026:

- ✅ Weights publicly downloadable (HuggingFace)
- ✅ Q4 GGUF format usable in llama.cpp / Ollama / vLLM
- ✅ Fits in 24GB VRAM with usable context window
- ⚠️ Need to confirm: Q4-quantized scores (not FP16 reference scores) clear all three thresholds
- ⚠️ Need to confirm: at least one independent community reproduction posted

### Failure modes still in play

1. **Quant degradation:** If Q4 quantization drops MMLU below 86.4%, falls back to needing FP8 or higher precision, which doesn't fit in 24GB.
2. **Benchmark contamination claim:** If a credible analysis emerges that DeepSeek's training data included GSM8K or HumanEval test sets, scores get discounted.
3. **Llama 3.3 confusion:** Llama 3.3 70B reportedly hits all three thresholds but requires multi-GPU — does NOT satisfy AV-003 hardware constraint.

### Updated probability: ~95% CORRECT

(Up from ~90% at April prep. Multiple independent candidates now exist.)

### Resolution actions in the next 4 weeks

1. **By May 30:** Pull Q4 GGUF for DeepSeek-R1-Distill-32B and Qwen 3 32B. Run LM Eval Harness for MMLU 5-shot, HumanEval pass@1, GSM8K 8-shot CoT on a single RTX 4090 (or document a community result that has).
2. **By June 15:** If primary candidate fails on quantized eval, fall back to next candidate. If all candidates fail, prepare INCORRECT resolution doc.
3. **By June 30:** Final resolution.

---

*Addendum: 2026-05-08*
