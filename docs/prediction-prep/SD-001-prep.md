# Prediction Resolution Prep: SD-001

## Prediction Details

| Field | Value |
|-------|-------|
| ID | SD-001 |
| Claim | A controlled AI-code-security benchmark published in 2026 will still show AI-generated code introducing security vulnerabilities in at least 30% of tasks |
| Made | 2026-06-13 |
| Resolves | 2027-02-28 |
| Ex-ante probability | 0.75 |
| Status | Pending - Resolution Prep |

---

## Resolution Criteria

Resolves **CORRECT** if the next Veracode GenAI Code Security Report (or an equivalent controlled, multi-model benchmark) published in 2026 and available by Feb 28, 2027 shows AI-generated code introducing an OWASP-class security vulnerability in **≥30% of evaluated tasks**.

Resolves **INCORRECT** if such a study published in 2026 shows a rate **<30%**.

Resolves **INCONCLUSIVE** if no qualifying controlled study is published in 2026 (per "When to Retire a Prediction" — named-source unavailability).

---

## Threshold Disambiguation Checklist (resolved readings)

Per `docs/pre-registration.md#threshold-disambiguation-checklist`, pinned **now**:

| Class | Resolved reading |
|-------|------------------|
| 1. Aggregate vs sub-segment | The **overall** AI-generated-code vulnerability rate across the benchmark's task set, not a single best/worst language subset. |
| 2. Series / definition | A **controlled benchmark** (a fixed task suite run across models in a lab setting), explicitly **NOT** field/production telemetry (PR merge rates, real-repo CVE counts). Veracode's GenAI Code Security Report is the reference series. |
| 3. Cohort / segment | All evaluated models pooled (the benchmark's headline rate), not a cherry-picked model. |
| 4. Central tendency vs tail | The benchmark's **headline/aggregate** pass-fail rate, not the worst category (e.g., not "86% XSS failure"). |
| 5. Anchor & window | Study must be **published in 2026** and accessible by Feb 28, 2027. A 2025 study (the 45% baseline) does **not** satisfy "published in 2026." |
| 6. Named-source strictness | **Veracode preferred.** An equivalent controlled academic/industry benchmark (e.g., a peer-reviewed multi-model code-security study) qualifies. Vendor self-assessments of their own model do **not** qualify. |
| 7. Units / provenance | Metric = **% of tasks** in which generated code contains an injected/known vulnerability class. Not CVEs-per-KLOC, not lines, not a CVSS average. |

**If two defensible readings give opposite verdicts and none was pinned above → INDETERMINATE, not favorable default.**

---

## Baseline (as of publication, June 13, 2026)

| Data point | Value | Source |
|-----------|-------|--------|
| Veracode GenAI Code Security Report (Oct 2025) | **45%** of tasks introduced a vulnerability across 100+ models; XSS 86% / log-injection 88% failure; "larger/newer models did not improve security" | Veracode (primary) |
| GitClear (Feb 2025) | Code churn 3.1% (2020) → 5.7% (2024); duplicated blocks up ~8× | GitClear (corroborating, different metric) |
| Google DORA (Sep 2025) | AI adoption has a negative relationship with delivery stability | DORA (corroborating) |

The 30% threshold sits well below the 45% 2025 baseline, and the Veracode finding that newer models did not improve security is the core reason the ex-ante probability is 0.75 rather than a coin flip.

---

## Resolution Checklist

On/before Feb 28, 2027:

- [ ] Locate the next Veracode GenAI Code Security Report (or equivalent controlled study) published in 2026
- [ ] Extract the headline % of tasks with an injected vulnerability
- [ ] Confirm it is a controlled benchmark, not field telemetry
- [ ] Apply the ≥30% threshold; if no 2026 study exists, resolve INCONCLUSIVE
- [ ] Document with citation; update tracker.md and the analysis Track Record
- [ ] Commit: `Resolve: SD-001 — {rate, outcome}`

---

*Prepared: 2026-06-13*
