# Prediction Resolution Calendar

Upcoming prediction verification dates and resolution requirements.

---

## Q1 2026 (January - March)

### February 2026

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| AV-001 | NVIDIA Q4 FY26 datacenter revenue YoY growth <50% | NVIDIA earnings report | Check datacenter segment YoY growth rate |

**AV-001 Resolution Details:**
- **Claim:** NVIDIA Q4 FY2026 datacenter revenue YoY growth will be below 50%
- **Baseline:** Recent quarters showed 50-66% YoY growth, down from 100%+ in 2024
- **Sources to check:** NVIDIA Investor Relations, SEC 10-Q filing, earnings transcript
- **Threshold:** YoY growth rate < 50%

---

## Q2 2026 (April - June)

### May 2026

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| AV-002 | Hyperscaler capex language moderation in Q1 2026 | Q1 earnings calls | Review MSFT/GOOG/AMZN transcripts |

**AV-002 Resolution Details:**
- **Claim:** At least one hyperscaler uses moderating language regarding AI capex
- **Target phrases:** "optimizing," "efficiency-focused," "disciplined," "slower pace"
- **Sources to check:** Earnings call transcripts for Microsoft, Google, Amazon
- **Threshold:** Explicit language suggesting capex growth rate reduction

### June 30, 2026

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| AV-003 | Open-weights model matches GPT-4 on consumer GPU | Benchmark leaderboards | Compare MMLU, HumanEval, GSM8K scores |

**AV-003 Resolution Details:**
- **Claim:** Open-weights model matches/exceeds GPT-4 (March 2023) on MMLU, HumanEval, GSM8K while running on RTX 4090
- **GPT-4 baselines:** MMLU ~86.4%, HumanEval ~67%, GSM8K ~92%
- **Sources to check:** HuggingFace leaderboard, Papers With Code, model cards
- **Threshold:** Equal or better on ALL THREE benchmarks

---

## Q3 2026 (July - September)

### July 1, 2026

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| SC-002 | SOX underperforms S&P 500 in H1 2026 | Financial data providers | Calculate total return comparison |

**SC-002 Resolution Details:**
- **Claim:** SOX index total return < S&P 500 total return for H1 2026
- **Period:** January 1, 2026 through June 30, 2026
- **Sources to check:** Yahoo Finance, Bloomberg, index provider sites
- **Threshold:** SOX total return < S&P 500 total return

---

## Q4 2026 (October - December)

### October 2026

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| SC-001 | DRAM prices peak Q1/Q2, decline Q3 | Industry price reports | Compare QoQ contract prices |
| AV-004 | Enterprise AI spend growth intentions <25% | Gartner/Forrester surveys | Check published survey results |
| HC-002 | Hyperscaler reduces capex guidance | Earnings guidance | Monitor guidance changes |

**SC-001 Resolution Details:**
- **Claim:** DRAM contract prices peak Q1/Q2 2026, decline QoQ in Q3 2026
- **Sources to check:** TrendForce, DRAMeXchange, memory vendor earnings
- **Threshold:** Q3 prices lower than Q2 (or Q1 peak)

**AV-004 Resolution Details:**
- **Claim:** Major enterprise survey reports AI spending growth intentions <25% YoY
- **Sources to check:** Gartner IT spending forecasts, Forrester predictions, IDC surveys
- **Threshold:** Growth intentions below 25% YoY

**HC-002 Resolution Details:**
- **Claim:** At least one hyperscaler reduces full-year capex guidance mid-year
- **Sources to check:** Earnings guidance from MSFT/GOOG/AMZN/META
- **Threshold:** Explicit reduction in stated guidance range

### December 31, 2026

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| AV-005 | NVIDIA+AMD+Arm market cap lower than Jan 3, 2026 | Financial data | Compare market caps |
| HC-001 | Combined Big 4 quarterly capex peaks <$150B | Quarterly filings | Sum quarterly capex reports |

**AV-005 Resolution Details:**
- **Claim:** Combined market cap of NVIDIA + AMD + Arm lower on Dec 31, 2026 than Jan 3, 2026
- **Baseline (Jan 3, 2026):** Record combined market cap at publication
- **Sources to check:** Yahoo Finance, market data providers
- **Threshold:** Combined market cap < baseline

**HC-001 Resolution Details:**
- **Claim:** Combined Big 4 quarterly capex peaks below $150B in 2026
- **Sources to check:** Quarterly earnings reports for MSFT/GOOG/AMZN/META
- **Threshold:** No quarter in 2026 exceeds $150B combined

---

## 2027

### January 2027

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| SC-004 | Foundry utilization divergence | TSMC reports/analyst data | Compare trailing vs leading edge |

### February 2027

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| SC-003 | Equipment vendor revenue decline | Quarterly earnings | Check ASML/AMAT/LRCX/KLAC |

### June 30, 2027

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| AV-006 | Efficiency narrative in 5+ mainstream articles | News archives | Search WSJ/FT/Bloomberg |

### December 31, 2027

| ID | Prediction | Verification Source | Action |
|----|-----------|-------------------|--------|
| AV-007 | Hyperscaler absolute capex reduction YoY | Annual filings | Compare 2027 vs 2026 capex |
| SC-005 | SOX 20%+ peak-to-trough decline in 2027 | Index data | Track peak and trough prices |
| SC-006 | Auto semi growth > AI growth in one quarter | Industry reports | Compare segment growth rates |

---

## Resolution Checklist

When a prediction's verification date arrives:

- [ ] Gather evidence from primary sources
- [ ] Verify against stated threshold
- [ ] Document outcome with links
- [ ] Move prediction to "Resolved" in tracker.md
- [ ] Update cumulative statistics
- [ ] Update analysis document track record
- [ ] Commit with message: `Resolve: {ID} - {outcome summary}`

---

*Updated: 2026-01-03*
