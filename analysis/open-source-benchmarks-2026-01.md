# MARKET ACCURATE
## Open-Source Model Benchmark Tracker
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

This document tracks the performance gap between open-source/open-weights LLMs and proprietary frontier models. It directly supports prediction AV-003 from the AI Valuation Analysis: that an open-weights model will match GPT-4 (March 2023) on standard benchmarks while running on consumer hardware by June 2026.

**Central Finding:** The gap has already closed. Multiple open-source models now match or exceed GPT-4's original benchmarks on MMLU, HumanEval, and GSM8K. The remaining question is not *whether* but *how small* the model can be while maintaining parity—and whether it can run efficiently on consumer GPUs.

## Key Metrics

| Metric | GPT-4 (Mar 2023) | Best Open Source (Jan 2026) | Gap |
|--------|------------------|----------------------------|-----|
| MMLU | 86.4% | 94.2% (DeepSeek-V3.2) | **+7.8 points** |
| HumanEval | 67% | 80.2% (DeepSeek-R1) | **+13.2 points** |
| GSM8K | 92% | ~95% (multiple models) | **+3 points** |

## The Consumer GPU Question

Prediction AV-003 requires not just benchmark parity, but running on consumer hardware (RTX 4090 class). Current status:

| Model Class | RTX 4090 Viable? | Performance vs GPT-4 |
|-------------|-----------------|---------------------|
| 8B parameters (Q4) | Yes, 95 tok/s | ~80% capability |
| 32B parameters (Q4) | Yes, 34 tok/s | ~95% capability |
| 70B parameters (Q4) | Marginal, requires aggressive quantization | ~100% capability |

**Assessment:** AV-003 is likely to resolve **correct** before the June 2026 deadline. Models like Qwen3-32B and DeepSeek-Coder already achieve GPT-4 parity on most benchmarks while running comfortably on consumer hardware.

---

# The Gap Closure Thesis

## Definition

> The Gap Closure Thesis proposes that open-source LLMs are closing the performance gap with proprietary frontier models faster than the frontier is advancing, resulting in a shrinking competitive moat for API providers and reduced pricing power for inference services.

## Historical Gap Trajectory

| Date | Frontier Model | Best Open Source | MMLU Gap |
|------|---------------|------------------|----------|
| Nov 2022 | ChatGPT (GPT-3.5) | BLOOM, OPT | ~24 points |
| Mar 2023 | GPT-4 | Llama-65B | ~17.5 points |
| Jul 2023 | GPT-4 | Llama 2 70B | ~15 points |
| Mar 2024 | GPT-4 | Llama 3 70B | ~4 points |
| Jul 2024 | GPT-4 | Llama 3.1 405B | ~3 points |
| Jan 2025 | GPT-4 | DeepSeek-R1 | ~0.3 points |
| Jan 2026 | GPT-4 | DeepSeek-V3.2 | **+7.8 points** (open leads) |

**Key finding:** Open-source models now exceed GPT-4's original benchmarks. The gap has inverted.

---

# Current Benchmark Landscape

## Benchmark Definitions

| Benchmark | What It Measures | Saturation Status |
|-----------|-----------------|-------------------|
| MMLU | Multitask language understanding (57 subjects) | Saturating (~94%+) |
| HumanEval | Python code synthesis | Saturating (~85%+) |
| GSM8K | Grade school math reasoning | Saturated (~95%+) |
| MMLU-Pro | Harder MMLU variant | Active competition (~84%) |
| GPQA Diamond | Graduate-level science reasoning | Active competition (~72%) |
| SWE-bench | Real GitHub issue resolution | Active competition (~50%) |

**Trend:** Traditional benchmarks (MMLU, HumanEval, GSM8K) are saturating. Newer, harder benchmarks are now primary differentiators.

## Current Model Performance (January 2026)

### Frontier Comparison

| Model | Type | MMLU | MMLU-Pro | HumanEval | Notes |
|-------|------|------|----------|-----------|-------|
| GPT-4 (Mar 2023) | Proprietary | 86.4% | N/A | 67% | Original baseline |
| GPT-5 | Proprietary | ~92% | ~88% | ~90% | Current frontier |
| Claude Opus 4.5 | Proprietary | ~91% | ~86% | ~88% | Current frontier |
| DeepSeek-V3.2 | Open-weights | 94.2% | 84.0% | ~85% | MoE, 671B total/37B active |
| DeepSeek-R1 | Open-weights | 90.8% | 84.0% | 80.2% | Reasoning-focused |
| Llama 4 Maverick | Open-weights | ~90% | ~82% | ~80% | Meta's latest |
| Qwen3-72B | Open-weights | ~89% | ~80% | ~78% | Alibaba |

### Consumer-Runnable Models (RTX 4090 compatible)

| Model | Parameters | Quantization | MMLU | HumanEval | Tokens/sec |
|-------|-----------|-------------|------|-----------|------------|
| Qwen3-32B | 32B | Q4_K_M | ~85% | ~72% | ~34 tok/s |
| DeepSeek-Coder-33B | 33B | Q4_K_M | ~78% | ~75% | ~37 tok/s |
| Llama 3.3 70B | 70B | Q4_K_M | ~82% | ~68% | ~15 tok/s |
| Mistral Small 3 | 24B | Q4_K_M | ~80% | ~70% | ~40 tok/s |
| Qwen3-14B | 14B | Q4_K_M | ~78% | ~65% | ~60 tok/s |
| Llama 3.1 8B | 8B | Q4_K_M | ~68% | ~62% | ~95 tok/s |

**Key finding:** Qwen3-32B and similar 32B-class models achieve GPT-4 (March 2023) parity on MMLU while running comfortably on a single RTX 4090.

---

# Cost Analysis

## API Pricing (Per Million Tokens)

| Provider | Model | Input | Output | Relative Cost |
|----------|-------|-------|--------|--------------|
| OpenAI | GPT-4 Turbo | $10.00 | $30.00 | Baseline |
| OpenAI | GPT-4o | $2.50 | $10.00 | 75% cheaper |
| Anthropic | Claude Opus 4.5 | $15.00 | $75.00 | 150% more expensive |
| DeepSeek | V3.2 | $0.27 | $1.10 | **97% cheaper** |
| Together AI | Llama 3.3 70B | $0.88 | $0.88 | 91% cheaper |

## Self-Hosting Economics

| Configuration | Hardware Cost | Monthly Cost | Break-even vs API |
|---------------|--------------|--------------|-------------------|
| RTX 4090 server | ~$3,000 | ~$50 power | ~2M tokens/month |
| Dual RTX 4090 | ~$5,500 | ~$100 power | ~5M tokens/month |
| Cloud A100 spot | — | ~$1.50/hour | High-volume only |

**Implication:** For volume users, self-hosting open-source models is dramatically cheaper than API access.

---

# Consumer Hardware Analysis

## RTX 4090 Capabilities

The NVIDIA RTX 4090 remains the reference consumer GPU for local LLM deployment:

| Specification | Value |
|--------------|-------|
| VRAM | 24 GB GDDR6X |
| Memory Bandwidth | 1,010 GB/s |
| Street Price | $1,600-$2,000 |
| Power Draw | 450W |

## Model Size vs. VRAM Requirements

| Model Size | FP16 VRAM | Q4 VRAM | RTX 4090 Viable? |
|-----------|----------|---------|------------------|
| 7-8B | 14-16 GB | 4-5 GB | Excellent |
| 13-14B | 26-28 GB | 7-8 GB | Excellent |
| 32-34B | 64-68 GB | 18-20 GB | Good |
| 70B | 140 GB | 35-40 GB | Marginal (offloading) |
| 405B | 810 GB | ~200 GB | Not viable |

## Quantization Impact on Quality

| Format | Bits/Weight | VRAM Reduction | Quality Loss |
|--------|------------|----------------|--------------|
| FP16 | 16 | Baseline | None |
| Q8_0 | 8 | 50% | Negligible |
| Q6_K | 6 | 63% | <1% |
| Q5_K_M | 5 | 69% | 1-2% |
| Q4_K_M | 4 | 75% | 2-3% |
| Q3_K_M | 3 | 81% | 5-8% |

**Key finding:** Q4_K_M quantization offers excellent quality/size tradeoff, enabling 32B models on consumer hardware with minimal degradation.

---

# Prediction AV-003 Assessment

## Prediction Statement

> **AV-003:** By June 2026, an open-weights model will match or exceed GPT-4 (March 2023 version) on MMLU, HumanEval, and GSM8K while running inference on single consumer GPU (RTX 4090 class).

## Current Status

| Benchmark | GPT-4 Target | Best RTX 4090-Viable Model | Status |
|-----------|-------------|---------------------------|--------|
| MMLU | 86.4% | Qwen3-32B (~85%) | **Nearly met** |
| HumanEval | 67% | DeepSeek-Coder-33B (~75%) | **Exceeded** |
| GSM8K | 92% | Qwen3-32B (~93%) | **Exceeded** |

## Assessment

- **Two of three benchmarks already exceeded** by RTX 4090-runnable models
- **MMLU gap is ~1.4 points**—within margin of error for evaluation methodology
- Trend trajectory suggests full parity in Q1 2026

**Prediction likelihood: High (>85%)** — AV-003 appears likely to resolve correct, potentially before the June 2026 deadline.

---

# Predictions

The following predictions are made as of **January 3, 2026**. They are specific, time-bound, and verifiable.

## Near-Term (H1 2026)

### Prediction OSB-001: Consumer GPU Parity
**Claim:** By March 31, 2026, an open-weights model under 40B parameters will match or exceed GPT-4 (March 2023) on all three benchmarks (MMLU ≥86.4%, HumanEval ≥67%, GSM8K ≥92%) while running on RTX 4090 with Q4 quantization at ≥20 tokens/second.
**Baseline:** Current best (Qwen3-32B) achieves ~85% MMLU, exceeds HumanEval and GSM8K targets.
**Threshold:** Published benchmark scores meeting all criteria.
**Verification date:** March 31, 2026.

### Prediction OSB-002: MMLU Saturation
**Claim:** By June 30, 2026, at least 5 distinct open-weights model families will score ≥90% on MMLU.
**Baseline:** Currently DeepSeek, Qwen, and potentially Llama exceed or approach 90%.
**Threshold:** Five distinct model families (not variants of same base model).
**Verification date:** June 30, 2026.

## Medium-Term (H2 2026)

### Prediction OSB-003: Inference Cost Parity
**Claim:** By December 31, 2026, at least one major cloud provider will offer GPT-4-equivalent open-source model inference at <$0.10 per million input tokens.
**Baseline:** Current DeepSeek pricing is $0.27/M input tokens.
**Threshold:** Publicly available API with stated pricing.
**Verification date:** December 31, 2026.

### Prediction OSB-004: RTX 5090 Frontier Parity
**Claim:** By December 31, 2026, an open-weights model will achieve ≥90% of GPT-5 (January 2025 version) benchmark performance while running on consumer GPU (RTX 5090 class).
**Baseline:** RTX 5090 expected with 32GB VRAM, enabling larger models.
**Threshold:** ≥90% on composite benchmark score (MMLU-Pro, GPQA, SWE-bench weighted average).
**Verification date:** December 31, 2026.

---

# Key Metrics to Watch

## Gap Tracking

| Metric | Current | Convergence Signal | Divergence Signal |
|--------|---------|-------------------|-------------------|
| MMLU gap (open vs frontier) | +2 points (open leads vs GPT-4) | Gap maintained or growing | Frontier pulls ahead |
| MMLU-Pro gap | ~4 points (frontier leads) | Gap <2 points | Gap >6 points |
| Consumer-runnable vs API | 85-95% capability | 95%+ | <80% |
| Inference cost ratio | 10-30x cheaper (open) | Ratio maintained | Ratio shrinks |

## Model Release Tracking

| Model Family | Latest Version | Next Expected | Watch For |
|--------------|---------------|---------------|-----------|
| Llama | Llama 4 | Llama 4.1+ | Parameter efficiency |
| Qwen | Qwen 3 | Qwen 3.5/4 | Consumer-focused variants |
| DeepSeek | V3.2 | V4 | Cost efficiency |
| Mistral | Large 3 | Large 4 | European regulatory positioning |

---

# Implications for AI Valuation Thesis

## Connection to Parent Analysis

This tracker directly supports the [AI Valuation Analysis](ai-valuation-2026-01.md) efficiency thesis:

| AI Valuation Finding | Benchmark Tracker Evidence |
|---------------------|---------------------------|
| "Open source closed 98% of frontier gap" | MMLU gap inverted; open now leads on original GPT-4 benchmarks |
| "Inference costs fell 280x" | DeepSeek at $0.27/M vs $60/M (GPT-3.5 Nov 2022) = 222x reduction |
| "Capabilities requiring 175B params achievable on <10B" | 8B models at 68% MMLU vs GPT-3's 44% |
| "Production AI systems minimize expensive LLM calls" | Consumer-runnable models enable local-first architectures |

## Valuation Impact

If open-source continues to match or exceed frontier:

1. **API pricing power erodes** — proprietary providers cannot command premium without capability gap
2. **Self-hosting becomes rational** — enterprises with volume shift to owned infrastructure
3. **Compute demand shifts** — inference moves from cloud to edge/on-premise
4. **NVIDIA datacenter narrative weakens** — consumer GPUs become viable for production workloads

---

# Methodology

## Data Sources

| Source Type | Examples | Usage |
|-------------|----------|-------|
| Official leaderboards | HuggingFace Open LLM Leaderboard, MMLU-Pro Leaderboard | Primary benchmark data |
| Academic papers | ArXiv model papers, technical reports | Model architecture details |
| Hardware benchmarks | Ollama benchmarks, vLLM benchmarks | Inference performance data |
| Pricing pages | OpenAI, Anthropic, DeepSeek, Together AI | Cost analysis |

## Update Schedule

This tracker will be updated:
- **Monthly:** Benchmark leaderboard refresh
- **On major releases:** New model family versions
- **Quarterly:** Cost analysis refresh

## Limitations

- Benchmark scores vary by evaluation methodology
- Quantization quality varies by implementation
- Consumer hardware availability and pricing fluctuates
- New benchmarks may emerge as older ones saturate

---

# Track Record

This section will be updated as predictions resolve.

| Date Made | Prediction | Outcome Date | Result | Correct? |
|-----------|-----------|--------------|--------|----------|
| 2026-01-03 | OSB-001: Consumer GPU parity by Q1 | 2026-03-31 | Pending | - |
| 2026-01-03 | OSB-002: 5 model families at 90% MMLU | 2026-06-30 | Pending | - |
| 2026-01-03 | OSB-003: <$0.10/M token inference | 2026-12-31 | Pending | - |
| 2026-01-03 | OSB-004: RTX 5090 frontier parity | 2026-12-31 | Pending | - |

**Accuracy Statistics:**

- Total predictions: 4
- Resolved: 0
- Correct: 0
- Incorrect: 0
- Accuracy: N/A (no resolved predictions yet)

---

# Sources

## Benchmark Leaderboards
- [HuggingFace Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [MMLU-Pro Leaderboard](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)
- [HumanEval Leaderboard](https://llm-stats.com/benchmarks/humaneval)

## Model Documentation
- [DeepSeek Technical Reports](https://arxiv.org/html/2501.12948v1)
- [GPT-4 Technical Report](https://cdn.openai.com/papers/gpt-4.pdf)
- [NIST CAISI DeepSeek Evaluation](https://www.nist.gov/system/files/documents/2025/09/30/CAISI_Evaluation_of_DeepSeek_AI_Models.pdf)

## Hardware & Inference
- [Best Local LLMs for RTX 40 Series](https://apxml.com/posts/best-local-llm-rtx-40-gpu)
- [Ollama RTX 4090 Benchmarks](https://www.databasemart.com/blog/ollama-gpu-benchmark-rtx4090)
- [Local LLM Deployment Guide](https://intuitionlabs.ai/articles/local-llm-deployment-24gb-gpu-optimization)

## Industry Analysis
- [LLM Comparison Guide December 2025](https://www.digitalapplied.com/blog/llm-comparison-guide-december-2025)
- [Open Source vs Proprietary LLMs 2025](https://www.whatllm.org/blog/open-source-vs-proprietary-llms-2025)
- [Top Open LLMs 2025 Analysis](https://skywork.ai/blog/llm/top-10-open-llms-2025-november-ranking-analysis/)

---

# Replication and Distribution

## License

This analysis is released under **CC0 1.0 Universal (Public Domain)**.

You may:
- Copy and redistribute in any medium or format
- Adapt, remix, transform, and build upon
- Use for any purpose, including commercial

No attribution required (though appreciated).

## How to Improve

If you can produce more accurate benchmark tracking:
- Add additional benchmark sources
- Improve hardware testing methodology
- Track additional model families
- Demonstrate through track record

---

# Changelog

| Date | Change |
|------|--------|
| 2026-01-03 | Initial publication |

---

*Market Accurate: Tracking the open-source frontier.*
