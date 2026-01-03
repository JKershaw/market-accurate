# Prediction Tracker

This file tracks all predictions made by Market Accurate analyses, their outcomes, and cumulative accuracy statistics.

---

## Active Predictions

### AI Valuation Analysis (2026-01-03)

| ID | Prediction | Made | Resolves | Status |
|----|-----------|------|----------|--------|
| AV-001 | NVIDIA Q4 FY26 datacenter revenue YoY growth <50% | 2026-01-03 | 2026-02 | Pending |
| AV-002 | Hyperscaler capex language moderation in Q1 2026 | 2026-01-03 | 2026-05 | Pending |
| AV-003 | Open-weights model matches GPT-4 on consumer GPU | 2026-01-03 | 2026-06-30 | Pending |
| AV-004 | Enterprise AI spend growth intentions <25% YoY | 2026-01-03 | 2026-10 | Pending |
| AV-005 | NVIDIA+AMD+Arm combined market cap lower than Jan 3 | 2026-01-03 | 2026-12-31 | Pending |
| AV-006 | Efficiency narrative in 5+ mainstream financial articles | 2026-01-03 | 2027-06-30 | Pending |
| AV-007 | At least one hyperscaler reduces absolute AI capex YoY | 2026-01-03 | 2027-12-31 | Pending |

### Hyperscaler Capex Tracker (2026-01-03)

| ID | Prediction | Made | Resolves | Status |
|----|-----------|------|----------|--------|
| HC-001 | Combined Big 4 quarterly capex peaks below $150B in 2026 | 2026-01-03 | 2026-12-31 | Pending |
| HC-002 | At least one hyperscaler reduces full-year capex guidance mid-2026 | 2026-01-03 | 2026-10-31 | Pending |

### Semiconductor Cycle Analysis (2026-01-03)

| ID | Prediction | Made | Resolves | Status |
|----|-----------|------|----------|--------|
| SC-001 | DRAM contract prices peak in Q1/Q2 2026, decline QoQ in Q3 | 2026-01-03 | 2026-10 | Pending |
| SC-002 | SOX index underperforms S&P 500 in H1 2026 | 2026-01-03 | 2026-07-01 | Pending |
| SC-003 | Major equipment vendor reports YoY revenue decline in Q3/Q4 2026 | 2026-01-03 | 2027-02 | Pending |
| SC-004 | TSMC trailing-edge utilization <70% while leading-edge >90% Q4 2026 | 2026-01-03 | 2027-01 | Pending |
| SC-005 | SOX experiences 20%+ peak-to-trough decline in 2027 | 2026-01-03 | 2027-12-31 | Pending |
| SC-006 | Automotive semi revenue growth exceeds AI/datacenter in one quarter 2027 | 2026-01-03 | 2027-12-31 | Pending |

### Open-Source Benchmark Tracking (2026-01-03)

| ID | Prediction | Made | Resolves | Status |
|----|-----------|------|----------|--------|
| OB-001 | Open-weights maintains parity (<2 point gap) with proprietary frontier through 2026 | 2026-01-03 | 2026-12-31 | Pending |
| OB-002 | 4B parameter model matches Llama 2 70B on mobile device | 2026-01-03 | 2026-12-31 | Pending |
| OB-003 | Frontier-class training (MMLU >85%) for under $1M | 2026-01-03 | 2026-12-31 | Pending |

### Enterprise AI Adoption Metrics (2026-01-03)

| ID | Prediction | Made | Resolves | Status |
|----|-----------|------|----------|--------|
| EA-001 | Enterprise AI spending growth forecast <25% for 2027 by Q2 2026 | 2026-01-03 | 2026-06-30 | Pending |
| EA-002 | Major consulting firm publishes >80% AI project failure rate | 2026-01-03 | 2026-12-31 | Pending |
| EA-003 | 3+ Fortune 500 companies disclose quantified AI ROI in earnings | 2026-01-03 | 2027-02 | Pending |

---

## Resolved Predictions

| ID | Prediction | Made | Resolved | Outcome | Correct? |
|----|-----------|------|----------|---------|----------|
| *None yet* | | | | | |

---

## Cumulative Statistics

| Metric | Value |
|--------|-------|
| Total Predictions | 21 |
| Resolved | 0 |
| Correct | 0 |
| Incorrect | 0 |
| Accuracy | N/A |
| Brier Score | N/A |

---

## Methodology

### What Counts as Correct?

Each prediction has explicit criteria defined at time of publication:

- **Quantitative predictions:** Must meet stated threshold (e.g., "<50% growth")
- **Binary predictions:** Must occur by stated deadline
- **Qualitative predictions:** Evaluated against stated criteria with evidence

### Immutability

- Predictions are **never modified** after publication
- Original wording preserved exactly as written
- Only outcome and correctness fields updated upon resolution
- All changes logged with timestamps

### Verification

Anyone can verify predictions by:
1. Checking git commit history for original prediction date
2. Comparing against public data sources at resolution date
3. Reviewing linked evidence for outcome determination

---

## Resolution Log

*This section documents when and how predictions are resolved.*

| Date | ID | Action | Evidence |
|------|----|--------|----------|
| *None yet* | | | |

---

## How to Use This Tracker

### For Consumers
- Check cumulative accuracy before weighting this source
- Verify claims against linked evidence
- Compare track record to other sources

### For Replicators
- Fork and maintain your own prediction tracker
- Use same format for comparability
- Build independent track record

---

*Updated: 2026-01-03 (added OB-001 through OB-003, EA-001 through EA-003)*
