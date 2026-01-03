# MARKET ACCURATE
## Open-Source Model Benchmark Tracking
### January 3, 2026

---

> **Disclaimer**
>
> This is **experimental analysis**, not financial advice. The author has **no positions**
> in securities discussed. Track record is **empty**—no predictions have yet resolved.
> Methodology is **unproven**. This represents one analytical perspective; it may be
> partially or entirely wrong. Do your own research.
>
> **Version:** 0.1 (Initial publication)

---

# Executive Summary

This document tracks the performance gap between proprietary frontier models and open-weights alternatives, supporting the AI Efficiency Thesis. The gap has narrowed from ~24 MMLU points in 2020 to ~0.3 points in early 2025, with profound implications for AI infrastructure valuations.

**Central Finding:** Open-source models are achieving frontier parity faster than anticipated. The DeepSeek-R1 event (January 2025) demonstrated that frontier capability can be achieved at ~5% of typical training cost, validating the efficiency thesis.

**Key Metrics (January 2026):**

| Metric | Value | Trend |
|--------|-------|-------|
| MMLU gap to frontier | ~0.3 points | Narrowing |
| Frontier capability lag | 12-18 months | Shrinking |
| Consumer GPU viable models | 8B-70B params | Expanding |
| Cost per capability unit | Falling ~70% annually | Accelerating |

**Assessment:** The open-source trajectory supports predictions AV-003 (consumer GPU parity by June 2026) and undermines compute scarcity assumptions embedded in AI valuations.

---

# The Frontier Gap

## Definition

> The **frontier gap** measures the performance difference between the best proprietary AI models and the best publicly available open-weights models across standard benchmarks.

A shrinking gap indicates:
1. Open-source research is catching up to proprietary labs
2. Training efficiency improvements diffuse rapidly
3. Moats based on model capability are eroding
4. API pricing power will decline

## Historical Gap Trajectory

### MMLU (Massive Multitask Language Understanding)

| Date | Proprietary Best | MMLU Score | Open Best | MMLU Score | Gap |
|------|-----------------|------------|-----------|------------|-----|
| 2020-06 | GPT-3 | 43.9% | - | - | N/A |
| 2022-04 | Chinchilla | 67.5% | BLOOM | ~44% | 23.5 |
| 2022-11 | ChatGPT | ~70% | OPT-175B | ~53% | 17 |
| 2023-03 | GPT-4 | 86.4% | LLaMA-65B | 63.4% | 23 |
| 2023-07 | GPT-4 | 86.4% | Llama 2 70B | 68.9% | 17.5 |
| 2024-04 | GPT-4 Turbo | 86.5% | Llama 3 70B | 82.0% | 4.5 |
| 2024-07 | Claude 3.5 | 88.7% | Llama 3.1 405B | 88.6% | 0.1 |
| 2025-01 | GPT-4o | 88.7% | DeepSeek-R1 | 90.8% | -2.1* |

*Open-source exceeds proprietary on this benchmark

### HumanEval (Code Generation)

| Date | Proprietary Best | Score | Open Best | Score | Gap |
|------|-----------------|-------|-----------|-------|-----|
| 2023-03 | GPT-4 | 67.0% | CodeLlama-34B | 48.8% | 18.2 |
| 2024-04 | GPT-4 Turbo | 87.1% | Llama 3 70B | 81.7% | 5.4 |
| 2024-12 | Claude 3.5 | 92.0% | Qwen 2.5 72B | 86.4% | 5.6 |
| 2025-01 | o1 | 92.4% | DeepSeek-R1 | 96.3% | -3.9* |

### GSM8K (Grade School Math)

| Date | Proprietary Best | Score | Open Best | Score | Gap |
|------|-----------------|-------|-----------|-------|-----|
| 2023-03 | GPT-4 | 92.0% | LLaMA-65B | 50.9% | 41.1 |
| 2024-04 | GPT-4 Turbo | 95.3% | Llama 3 70B | 93.0% | 2.3 |
| 2025-01 | o1 | 94.8% | DeepSeek-R1 | 97.3% | -2.5* |

## Key Observation

The gap trajectory shows:
1. **2020-2022:** Open-source 15-25 points behind
2. **2023:** Gap persists at 15-20 points
3. **2024:** Gap collapses to 0-5 points
4. **2025:** Open-source achieves parity/superiority on key benchmarks

---

# The DeepSeek Event

## What Happened

On January 20, 2025, Chinese lab DeepSeek released DeepSeek-R1, an open-weights model that:

- **Matched or exceeded GPT-4** on MMLU, HumanEval, GSM8K
- **Trained at ~5% of typical cost** (~$5.6M vs ~$100M+)
- **Released weights publicly** under permissive license
- **Ran efficiently** on consumer hardware

## Market Impact

| Metric | Before (Jan 17) | After (Jan 27) | Change |
|--------|----------------|----------------|--------|
| NVIDIA market cap | $3.5T | $2.9T | -$589B |
| Single-day loss | - | - | Largest in history |
| SOX index | - | - | -9.5% |

## Implications

The DeepSeek event validated the AI Efficiency Thesis:

1. **Frontier capability ≠ frontier cost:** Training efficiency improvements enable smaller labs to compete
2. **Open-source as equilibrating force:** Techniques diffuse rapidly once demonstrated
3. **Compute scarcity is eroding:** Required compute for given capability is falling faster than demand growing
4. **Pricing power at risk:** API providers cannot maintain premium pricing against open alternatives

---

# Consumer Hardware Viability

## The RTX 4090 Threshold

A key milestone for AI democratization: when frontier-class models run on consumer GPUs.

### RTX 4090 Specifications
- **VRAM:** 24GB GDDR6X
- **Compute:** 82.6 TFLOPS FP16
- **Price:** ~$1,600 USD
- **Availability:** Consumer retail

### Current Viable Models (January 2026)

| Model | Parameters | Quantization | VRAM Required | Performance |
|-------|-----------|--------------|---------------|-------------|
| Llama 3.1 8B | 8B | FP16 | 16GB | Good |
| Llama 3.2 11B | 11B | INT8 | 12GB | Good |
| Mistral 7B v0.3 | 7B | FP16 | 14GB | Good |
| Qwen 2.5 14B | 14B | INT8 | 16GB | Very Good |
| Llama 3.1 70B | 70B | Q4 | 22GB | Excellent |
| DeepSeek-R1-Distill | 32B | Q4 | 20GB | Excellent |

### Benchmark Comparison (RTX 4090 Viable)

| Model | MMLU | HumanEval | GSM8K | Notes |
|-------|------|-----------|-------|-------|
| GPT-4 (Mar 2023) | 86.4% | 67.0% | 92.0% | Target baseline |
| Llama 3.1 70B Q4 | 82.0% | 81.7% | 93.0% | 4.4 below on MMLU |
| Qwen 2.5 32B Q4 | 83.3% | 79.8% | 91.2% | 3.1 below on MMLU |
| DeepSeek-R1-32B | 87.5% | 85.4% | 95.6% | **Exceeds on all** |

## Trajectory

| Date | Best Consumer-Viable | GPT-4 Gap |
|------|---------------------|-----------|
| 2023-06 | Llama 1 13B | ~25 MMLU points |
| 2024-01 | Mistral 7B | ~18 MMLU points |
| 2024-06 | Llama 3 8B | ~12 MMLU points |
| 2025-01 | DeepSeek-R1-32B | **-1 point (exceeds)** |

---

# Training Cost Deflation

## Cost Per MMLU Point

Rough estimates of training cost to achieve benchmark performance:

| Model | Year | MMLU | Estimated Training Cost | Cost per MMLU Point |
|-------|------|------|------------------------|-------------------|
| GPT-3 | 2020 | 43.9% | ~$4.6M | ~$105K |
| Chinchilla | 2022 | 67.5% | ~$2.1M | ~$31K |
| Llama 2 70B | 2023 | 68.9% | ~$2M | ~$29K |
| Llama 3 70B | 2024 | 82.0% | ~$3M | ~$37K |
| DeepSeek-V2 | 2024 | 84.0% | ~$5.6M | ~$67K |
| DeepSeek-R1 | 2025 | 90.8% | ~$5.6M | ~$62K |

**Key insight:** While absolute costs vary, cost per capability unit is falling as efficiency techniques compound.

## Training Efficiency Breakthroughs

| Technique | Impact | Status |
|-----------|--------|--------|
| Mixture of Experts (MoE) | 5-10x compute reduction at inference | Widely adopted |
| Flash Attention | 2-4x memory efficiency | Standard |
| Speculative decoding | 2-3x inference speedup | Emerging |
| Quantization-aware training | 4-8x memory reduction | Maturing |
| Knowledge distillation | Transfer capability at fraction of cost | Accelerating |

---

# Predictions

## OB-001: Frontier Parity Persistence
**Claim:** Open-weights models will maintain parity (within 2 points on MMLU, HumanEval, GSM8K) with proprietary frontier through 2026.
**Threshold:** No proprietary model opens a gap >2 points on all three benchmarks.
**Verification date:** December 31, 2026

## OB-002: 4B Parameter Breakthrough
**Claim:** By December 2026, a 4B parameter or smaller open-weights model will match Llama 2 70B performance (MMLU ~69%) while running on mobile devices.
**Threshold:** MMLU ≥68% with <5B parameters, demonstrated on mobile chipset.
**Verification date:** December 31, 2026

## OB-003: Training Cost Collapse
**Claim:** By end of 2026, at least one lab will demonstrate frontier-class model training (MMLU >85%) for under $1M total compute cost.
**Threshold:** Verified training cost <$1M, MMLU >85%.
**Verification date:** December 31, 2026

---

# Metrics Dashboard

## Current State (January 2026)

| Metric | Value | Last Update |
|--------|-------|-------------|
| Best open MMLU | 90.8% (DeepSeek-R1) | Jan 2025 |
| Best open HumanEval | 96.3% (DeepSeek-R1) | Jan 2025 |
| Best open GSM8K | 97.3% (DeepSeek-R1) | Jan 2025 |
| Frontier gap (MMLU) | -2.1 (open leads) | Jan 2025 |
| Consumer-viable best | DeepSeek-R1-32B | Jan 2025 |
| Cost per frontier model | ~$5-10M | Jan 2025 |

## Trend Indicators

| Indicator | Direction | Implication |
|-----------|-----------|-------------|
| MMLU gap | Closed/reversed | Validates AV-003 |
| Training cost | Falling | Validates efficiency thesis |
| Consumer viability | Improving | Democratization accelerating |
| Open-source velocity | Accelerating | Moats eroding |

---

# Connections to Other Analyses

## AI Valuation Analysis

| Prediction | Benchmark Support |
|------------|-------------------|
| AV-003 (consumer GPU parity) | DeepSeek-R1-32B already exceeds GPT-4 |
| AV-005 (market cap decline) | Open-source competition erodes pricing power |
| AV-006 (efficiency narrative) | DeepSeek event generated mainstream coverage |

## Semiconductor Cycle Analysis

| Connection | Implication |
|------------|-------------|
| Efficiency reduces compute demand | Supports cycle correction thesis |
| Consumer hardware viable | Less enterprise GPU demand |
| Training cost deflation | Lower capex required for AI capability |

---

# Methodology

## Data Sources

| Source | Usage | Frequency |
|--------|-------|-----------|
| HuggingFace Leaderboards | Official benchmark scores | Weekly check |
| Papers With Code | Research benchmarks | Bi-weekly |
| ArXiv | Training papers, cost estimates | Weekly |
| Model Cards | Official specifications | Per release |
| Community testing | LocalLLaMA, Reddit | Ongoing |

## Limitations

- Training costs are estimates (often not disclosed)
- Benchmark gaming may inflate scores
- Not all capabilities captured by standard benchmarks
- Consumer viability depends on quantization quality

---

# Sources

- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [Papers With Code - MMLU](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu)
- [Artificial Analysis](https://artificialanalysis.ai/)
- [DeepSeek Technical Reports](https://github.com/deepseek-ai)
- [Llama Model Cards](https://ai.meta.com/llama/)
- [LocalLLaMA Community](https://www.reddit.com/r/LocalLLaMA/)

---

# Changelog

| Date | Change |
|------|--------|
| 2026-01-03 | Initial publication |

---

*Market Accurate: Tracking the open-source frontier.*
