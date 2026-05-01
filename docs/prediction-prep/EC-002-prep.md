# Prediction Resolution Prep: EC-002

## Prediction Details

| Field | Value |
|-------|-------|
| ID | EC-002 |
| Claim | Lithium-ion battery pack prices will fall below $100/kWh for EV applications by end of 2026 |
| Made | 2026-01-03 |
| Resolves | December 31, 2026 |
| Status | Pending - Resolution Prep |

---

## Resolution Criteria

Prediction resolves **CORRECT** if:

- BloombergNEF (BNEF) annual battery price survey or equivalent reports the **EV pack volume-weighted average price** for full-year 2026 below $100/kWh.
- Strict inequality: $99.99/kWh or below resolves CORRECT; $100.00/kWh resolves INCORRECT (per pre-registration tie-breaker).

Prediction resolves **INCORRECT** if:

- BNEF or equivalent reports 2026 EV pack volume-weighted average ≥ $100/kWh.

---

## Source priority

| Priority | Source | Why |
|----------|--------|-----|
| 1 | BloombergNEF Annual Battery Price Survey | Industry-standard reference, decade-plus methodology |
| 2 | Wood Mackenzie Battery Pricing | Independent corroboration |
| 3 | Goldman Sachs / RMI battery price tracking | Investment-bank cross-check |
| 4 | Major automaker disclosures (Tesla, BYD, GM Ultium) | Direct cost data |

If BNEF does not publish before resolution, escalate to source 2 (Wood Mackenzie).

---

## Measurement Conventions

| Detail | Specification |
|--------|---------------|
| Scope | EV pack (full pack price), not cell only |
| Average type | Volume-weighted across global production |
| Currency | USD per kWh (nominal, not real) |
| Period | Full calendar year 2026 |
| Inclusion | All chemistries (NMC, NCA, LFP, etc.) weighted by volume |
| Exclusion | Stationary storage packs (different segment) |

**Note on segment:** BNEF reports both "EV pack" and "stationary storage" separately. Stationary already crossed $70/kWh. The prediction is specifically about EV packs.

---

## Baseline Data

From Energy & Climate Analysis (2026-01-03):

| Year | EV Pack Average | YoY |
|------|----------------|-----|
| 2013 | $684/kWh | — |
| 2019 | $156/kWh | — |
| 2023 | $139/kWh | -11% |
| 2024 | $117/kWh | -16% |
| 2025 | $108/kWh | -8% |
| 2026 (target) | <$100/kWh | -7%+ |

**Required deflation rate to satisfy:** 8% YoY or steeper from 2025 → 2026.

**Recent trajectory:** Declines have averaged ~10% annually for the past five years. 8% YoY is *below* the recent trend, meaning the prediction is well-supported by extrapolation. The risk is metals-price reversal or supply chain disruption.

---

## Interim Monitoring Points

| Quarter | EV Pack Spot/Contract Price | Notes |
|---------|-----------------------------|-------|
| Q1 2026 | | China LFP pack rumors of <$80/kWh |
| Q2 2026 | | BNEF mid-year update |
| Q3 2026 | | Year-end forecast revision |
| Q4 2026 | | Final survey input window |

The BNEF annual survey publishes in **late November / early December** of the survey year. The 2026 number will be available by mid-December 2026.

---

## Rationale Snapshot

From Energy & Climate Analysis:

- Multi-year structural decline in pack pricing
- China LFP economics already deeply below $100/kWh (~$84/kWh in 2025)
- North America/Europe higher ($122 / $131/kWh) but trending down
- 2025–2026 driver: lithium oversupply, scale, manufacturing efficiency
- Stationary storage already at $70/kWh (segment proves cost floor much lower)

**Confidence:** Originally rated Moderate. Current view: **High**. Volume-weighted pricing is dominated by Chinese production; Chinese LFP is already well below $100/kWh.

---

## Key Risks to Prediction

### Risks favoring INCORRECT (price stays ≥ $100/kWh)

- Lithium carbonate price spike (geopolitical, supply disruption)
- Tariff regime change makes Chinese cells inaccessible to Western EVs (forces higher-cost mix into the global average — though BNEF measures by point-of-production, not point-of-sale, so this risk is muted)
- BNEF methodology change (e.g., excluding LFP from "EV pack" definition)
- Cobalt or nickel supply shock
- Manufacturing capacity rationalization (consolidation reduces price competition)

### Risks favoring CORRECT (price falls below $100/kWh)

- China continues 15–20% YoY pack-price declines
- Sodium-ion commercialization adds price pressure
- LFP further displaces NMC in share, dragging average down
- Recycled-cathode supply scales, easing raw-material cost
- Tesla 4680 / BYD Blade cell economics continue to improve

---

## Likelihood Assessment

| Scenario | Probability | Outcome |
|----------|-------------|---------|
| <$95/kWh (strong continuation) | 40% | CORRECT |
| $95–99/kWh (just under threshold) | 30% | CORRECT |
| $100–105/kWh (just over threshold) | 20% | INCORRECT |
| >$105/kWh (price reversal) | 10% | INCORRECT |

**Subjective ex-ante probability of CORRECT: ~70%**

The 2025 print at $108/kWh combined with a stable ~10% YoY decline puts 2026 squarely in the $95–100 range. A $99.99/kWh outcome is not implausible — the strict-inequality tie-breaker would matter.

---

## Tie-breaker scenarios to plan for

If the final BNEF print rounds to exactly $100/kWh (e.g., reported as "approximately $100" or "$100" without sub-dollar precision):

- Default per pre-registration framework: tie resolves INCORRECT
- However: if BNEF reports e.g. "$99/kWh" without sub-dollar precision, treat that as <$100 (CORRECT)
- If BNEF reports "$100/kWh" and Wood Mackenzie reports "$98/kWh" for the same period, escalate to dual-source averaging — outcome favors CORRECT only if the average is strictly <$100

---

## Data Sources

| Source | Usage |
|--------|-------|
| BloombergNEF | Primary survey |
| Wood Mackenzie | Cross-verification |
| Goldman Sachs Equity Research | Battery cost commentary |
| Tesla Investor Day | Cost roadmap |
| BYD Annual Report | Pack-cost claims |
| RMI / IEA reports | Independent triangulation |

---

## Resolution Checklist

In December 2026 / January 2027:

- [ ] Wait for BNEF annual battery price survey (typically late November / early December)
- [ ] Record 2026 EV pack volume-weighted average price
- [ ] Cross-check against Wood Mackenzie if available
- [ ] Apply strict-inequality threshold ($99.99 or below = CORRECT)
- [ ] Document with linked report
- [ ] Determine: CORRECT or INCORRECT
- [ ] Update predictions/tracker.md
- [ ] Update analysis/energy-climate-2026-01.md Track Record
- [ ] Commit: "Resolve: EC-002 — 2026 EV pack ${X}/kWh, outcome"

---

## Sources

- [BloombergNEF Battery Price Survey](https://about.bnef.com/insights/clean-transport/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices-bloombergnef/) (most recent edition)
- [Wood Mackenzie Battery](https://www.woodmac.com/)
- [Energy & Climate Analysis](/analysis/energy-climate-2026-01.md)

---

*Prepared: 2026-05-01*
