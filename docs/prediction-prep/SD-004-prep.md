# Prediction Resolution Prep: SD-004

## Prediction Details

| Field | Value |
|-------|-------|
| ID | SD-004 |
| Claim | No single-employee company will reach a $1B valuation or $1B annual revenue, credibly documented, by December 31, 2026 |
| Made | 2026-06-13 |
| Resolves | 2026-12-31 |
| Ex-ante probability | 0.80 (that the claim holds — i.e., no such company) |
| Status | Pending - Resolution Prep |

---

## Resolution Criteria

Resolves **INCORRECT** (the disconfirming event occurred) if, on or before Dec 31, 2026, a company with **exactly one full-time human** (the founder) is documented by WSJ, FT, Bloomberg, or TechCrunch as having reached **either**:

- (a) a **$1B valuation** in a priced funding round, **or**
- (b) **$1B annual revenue** (ARR or trailing-12-month).

Resolves **CORRECT** if no such company is documented by the date.

This is the contrarian position to Dario Amodei's May-2025 stated 70–80% odds of a $1B one-person company by 2026.

---

## Threshold Disambiguation Checklist (resolved readings)

Per `docs/pre-registration.md#threshold-disambiguation-checklist`, the readings are pinned **now**, before the verification date:

| Class | Resolved reading |
|-------|------------------|
| 1. Aggregate vs sub-segment | N/A (single-entity claim) |
| 2. Series / definition | "One-person" = **one full-time human employee** (the founder). Contractors, agencies, and AI agents are permitted — this matches Amodei's framing and is the interesting version of the claim. A company with 2+ full-time employees does not qualify as a disconfirming case. |
| 3. Cohort / segment | Any company globally; no sector restriction. |
| 4. Central tendency vs tail | A **single** qualifying company is a disconfirming event (this is an existence claim, so the tail counts — by design, since the prediction is that even the most extreme case won't reach $1B). |
| 5. Anchor & window | The $1B threshold must be reached **on or before Dec 31, 2026**. A round/revenue milestone announced in 2027 for 2026 activity does not count unless the milestone itself was reached in 2026. |
| 6. Named-source strictness | Documentation must come from **WSJ, FT, Bloomberg, or TechCrunch**. A company press release alone, or an aggregator/blog, does not suffice (valuations and revenue self-claims are routinely inflated). |
| 7. Units / provenance | **Valuation** = post-money in a *priced* round (not a SAFE cap, not a secondary tender rumor). **Revenue** = ARR or TTM revenue, not GMV/bookings/"run-rate aspiration." Either one reaching $1B is disconfirming. |

**If two defensible readings give opposite verdicts and none was pinned above → INDETERMINATE, not favorable default.** (Per Known Failure Mode #2.)

---

## Baseline (as of publication, June 13, 2026)

| Data point | Value | Source |
|-----------|-------|--------|
| Largest documented solo-founder ARR/outcome | Base44 (Maor Shlomo): solo, ~$3.5M ARR, sold to Wix for ~$80M | Wix deal widely reported (2025) |
| Other solo portfolios | Pieter Levels ~$3.1–3.5M ARR; Marc Lou ~$1.03M (2025) | Secondary |
| Amodei claim | "$1B one-person company by 2026," 70–80% odds | Reported May 2025 |

The gap between the largest verified solo outcome (~tens of millions) and $1B is ~20–30×. No verified one-person company is within an order of magnitude of the threshold as of mid-2026.

---

## Resolution Checklist

On/before Dec 31, 2026:

- [ ] Search WSJ/FT/Bloomberg/TechCrunch for any single-employee company at $1B valuation or revenue in 2026
- [ ] Confirm headcount = one full-time human (contractors/AI permitted)
- [ ] Confirm valuation is a priced round OR revenue is ARR/TTM (not GMV/bookings)
- [ ] Determine CORRECT (none found) or INCORRECT (one found)
- [ ] Document with citation; update tracker.md and the analysis Track Record
- [ ] Commit: `Resolve: SD-004 — {outcome}`

---

*Prepared: 2026-06-13*
