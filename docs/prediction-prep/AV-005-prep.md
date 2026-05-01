# Prediction Resolution Prep: AV-005

## Prediction Details

| Field | Value |
|-------|-------|
| ID | AV-005 |
| Claim | The combined market cap of NVIDIA + AMD + Arm Holdings will be lower on December 31, 2026 than on January 3, 2026 |
| Made | 2026-01-03 |
| Resolves | December 31, 2026 |
| Status | Pending - Resolution Prep |

---

## Resolution Criteria

Prediction resolves **CORRECT** if:

- (NVDA + AMD + ARM combined market cap, close of business Dec 31, 2026) < (combined market cap, close of business Jan 3, 2026)
- Strict inequality. A tie within rounding (≤0.1% difference) resolves INCORRECT (we want a real signal, not measurement noise).

Prediction resolves **INCORRECT** if:

- Combined market cap on Dec 31, 2026 is greater than or equal to the Jan 3, 2026 baseline.

---

## Measurement Conventions

| Detail | Specification |
|--------|---------------|
| Market cap source | Yahoo Finance, Bloomberg, or company-reported diluted-share-count × close price |
| Tickers | NVDA (NASDAQ), AMD (NASDAQ), ARM (NASDAQ) |
| Currency | USD |
| Share count | Diluted, as of the most recent reported quarter |
| Splits | Adjust both endpoints to the same split-adjusted basis if any split occurs |
| Spinoffs/M&A | If any of the three is acquired or merged, prediction resolves INCONCLUSIVE per pre-registration framework |

**Note on Arm:** ARM trades with a relatively small public float (SoftBank still holds majority). Use shares outstanding (not float) for the market-cap calculation, consistent with standard market-cap convention.

---

## Baseline Data (Jan 3, 2026)

Required to be locked in before resolution:

| Company | Ticker | Jan 3, 2026 Close | Diluted Shares | Market Cap |
|---------|--------|------------------|---------------|------------|
| NVIDIA | NVDA | _to lock_ | _to lock_ | _to lock_ |
| AMD | AMD | _to lock_ | _to lock_ | _to lock_ |
| Arm | ARM | _to lock_ | _to lock_ | _to lock_ |
| **Combined** | — | — | — | **_to lock_** |

**Action item:** Run `scripts/fetch_index_returns.py` (or equivalent) to lock these baseline figures and commit them as a snapshot file. This must be done well before December 2026 so the baseline cannot drift.

**Approximate baseline (from analysis at Jan 3, 2026 publication, for sanity-check):**
- NVDA: ~$3.0T
- AMD: ~$240B
- ARM: ~$140B
- Combined: ~$3.4T

These figures are illustrative; the resolution will use the locked snapshot.

---

## Interim Monitoring Points

| Date | NVDA | AMD | ARM | Combined | YTD vs. Baseline |
|------|------|-----|-----|----------|------------------|
| Mar 31, 2026 | | | | | |
| Jun 30, 2026 | | | | | |
| Sep 30, 2026 | | | | | |
| Dec 31, 2026 | | | | | |

Negative YTD vs. baseline means the prediction is on track to resolve CORRECT. Positive means INCORRECT.

---

## Rationale Snapshot

From AI Valuation Analysis (2026-01-03):

- AI compute scarcity premium ~30–40% above neutral, expected to compress 20–40%
- DeepSeek event already showed -$589B single-day NVDA loss
- Open-source closing capability gap (validated by April 2026 update)
- Hyperscaler ROI gap suggested capex deceleration

From April 2026 Interim Update:

- Hyperscaler 2026 guidance came in at $625B+ combined Big 4 — *materially higher* than baseline
- Supply-constraint story (Microsoft 1.5GW freeze, AWS pause) reduces *delivered* capacity but does not reduce the *bill of materials* purchased — actually arguably bullish for GPU vendors short-term
- AV-001 resolved INCORRECT (NVDA Q4 FY26 +75% YoY)

**Updated subjective probability of CORRECT: dropped from ~50% (Jan) to ~25% (Apr).** The supply-constraint world is ambiguous-to-bullish for these three names. The original demand-destruction case has not materialized in 2026 to date.

---

## Key Risks to Prediction

### Risks favoring CORRECT (combined market cap declines)

- Q4 FY26 → Q4 FY27 (Jan 2027 reporting) deceleration ≥ 20pp at NVIDIA
- DeepSeek-style efficiency event late in 2026 wipes ≥ 20% off NVDA in a single session
- Hyperscaler explicitly cuts FY27 capex guidance during 2026
- China escalation: tariff/export-control shock that disproportionately hits these three
- Broad market drawdown of 15–20% with these as high-beta names

### Risks favoring INCORRECT (combined market cap holds or rises)

- Continued capex acceleration through 2026
- Supply-constraint binds → existing GPU/IP holders gain pricing power
- Inference-economy buildout drives Arm royalty growth (smartphone + datacenter)
- AMD MI400 ramp lifts AMD into Nvidia's slipstream
- AI-agent buildout creates step-function compute demand
- Government / sovereign AI commitments (US, EU, UAE, etc.) sustain demand floor

---

## Sub-component analysis

### NVIDIA (~88% of combined market cap)

NVDA dominates the combined figure. The prediction is effectively a bet on NVIDIA. AMD and ARM matter only for the marginal 12%.

| Driver | Direction |
|--------|-----------|
| Datacenter revenue growth | Bull (Apr 2026) |
| Gross margin (H100/Blackwell mix) | Mild compression on Blackwell ramp |
| Hyperscaler concentration | Risk |
| Custom-silicon competition (TPU, Trainium, Maia) | Negative |
| Sovereign AI | Positive |

### AMD (~7%)

| Driver | Direction |
|--------|-----------|
| MI300X / MI325X traction | Modest positive |
| Server CPU share gain (Bergamo) | Positive |
| AI accelerator ramp execution | Risk |
| Consumer PC cyclical recovery | Modest positive |

### ARM (~5%)

| Driver | Direction |
|--------|-----------|
| Smartphone royalty growth | Stable |
| Datacenter penetration (Ampere, Graviton, Cobalt) | Positive |
| AI-PC adoption (Snapdragon X-class) | Modest positive |
| SoftBank overhang (block-sale risk) | Negative |

---

## Likelihood Assessment

| Scenario | Probability | Outcome |
|----------|-------------|---------|
| Combined down ≥10% | 15% | CORRECT |
| Combined down 0–10% | 15% | CORRECT |
| Combined flat (within 0.1%) | <1% | INCORRECT (tie rule) |
| Combined up 0–15% | 25% | INCORRECT |
| Combined up 15–30% | 25% | INCORRECT |
| Combined up >30% | ~20% | INCORRECT |

**Subjective ex-ante probability of CORRECT (April 2026 update): ~30%**

This is a contrarian prediction. The original Jan 2026 thesis assumed efficiency would translate to demand erosion within 2026. As of April 2026, this has not happened; if anything, the data is going the other way.

---

## Data Sources

| Source | Usage |
|--------|-------|
| Yahoo Finance | Daily close, market cap |
| NASDAQ Index Services | Volume, official closes |
| Company 10-Q filings | Diluted share count |
| Bloomberg / FactSet | Cross-verification |

---

## Resolution Checklist

On January 1–3, 2027:

- [ ] Pull NVDA, AMD, ARM closes for Dec 31, 2026
- [ ] Verify diluted share counts from latest 10-Qs
- [ ] Compute Dec 31, 2026 combined market cap
- [ ] Compare to locked Jan 3, 2026 baseline
- [ ] Determine: CORRECT or INCORRECT (per strict-inequality rule)
- [ ] Document with screenshot or API response
- [ ] Update predictions/tracker.md
- [ ] Update analysis/ai-valuation-2026-01.md Track Record
- [ ] Update docs/analyst-comparison.md (this is one of our marquee contrarian predictions)
- [ ] Commit: "Resolve: AV-005 — combined market cap {up/down X%, outcome}"

---

## Sources

- [NVIDIA Investor Relations](https://investor.nvidia.com/)
- [AMD Investor Relations](https://ir.amd.com/)
- [Arm Investor Relations](https://investors.arm.com/)
- [AI Valuation Analysis](/analysis/ai-valuation-2026-01.md)

---

*Prepared: 2026-05-01*
