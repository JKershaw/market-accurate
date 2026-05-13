---
layout: default
title: Prediction Tracker
permalink: /predictions/
---

# Prediction Tracker

All predictions made by Market Accurate analyses, their outcomes, and cumulative accuracy statistics.

This page is **auto-generated** from the [`_predictions/`](https://github.com/JKershaw/market-accurate/tree/main/_predictions) collection. Each prediction has its own page with headline, why-it-matters, threshold, base rate, and resolution. Click any ID for the full prediction.

To add a prediction or record a resolution, edit `scripts/generate_prediction_pages.py` and rerun it. **Never** hand-edit individual `_predictions/{ID}.md` files — they're regenerated.

---

## Cumulative Statistics

{% assign total = site.predictions | size %}
{% assign resolved = site.predictions | where: "status", "Resolved" %}
{% assign resolved_count = resolved | size %}
{% assign correct = resolved | where: "verdict", "CORRECT" | size %}
{% assign incorrect = resolved | where: "verdict", "INCORRECT" | size %}

| Metric | Value |
|--------|-------|
| Total Predictions | {{ total }} |
| Resolved | {{ resolved_count }} |
| Correct | {{ correct }} |
| Incorrect | {{ incorrect }} |
{% if resolved_count > 0 %}
| Accuracy | {{ correct | times: 100.0 | divided_by: resolved_count | round: 0 }}% (n={{ resolved_count }}) |
{% else %}
| Accuracy | *N/A* |
{% endif %}
| Calibration | {% if resolved_count >= 30 %}see by-confidence-band breakdown below{% else %}Insufficient data (need n≥30){% endif %} |

**Note on Brier scores:** Predictions made before April 18, 2026 (the formal pre-registration framework's introduction) lack stated ex-ante probabilities. Per protocol, such predictions are scored at 0.50, yielding a Brier contribution of 0.25 each regardless of outcome. Newer predictions carry explicit probabilities in their front matter.

---

## Active Predictions

🟡 = Pending · ✅ = Resolved CORRECT · ❌ = Resolved INCORRECT

{% assign analyses = site.predictions | map: "analysis_title" | uniq %}
{% for analysis in analyses %}
{% assign group = site.predictions | where: "analysis_title", analysis | where: "status", "Pending" | sort: "resolves" %}
{% if group.size > 0 %}

### {{ analysis }}

| ID | Headline | Resolves | Probability |
|----|----------|----------|-------------|
{% for p in group -%}
| 🟡 [{{ p.id }}]({{ p.url }}) | {{ p.short_title }} | {{ p.resolves }} | {% if p.probability %}{{ p.probability }}{% else %}—{% endif %} |
{% endfor %}

{% endif %}
{% endfor %}

---

## Resolved Predictions

{% assign resolved_sorted = site.predictions | where: "status", "Resolved" | sort: "resolved_date" %}
{% if resolved_sorted.size > 0 %}

| ID | Prediction | Made | Resolved | Verdict |
|----|-----------|------|----------|---------|
{% for p in resolved_sorted -%}
| {% if p.verdict == "CORRECT" %}✅{% else %}❌{% endif %} [{{ p.id }}]({{ p.url }}) | {{ p.short_title }} | {{ p.made }} | {{ p.resolved_date }} | **{{ p.verdict }}** |
{% endfor %}

{% else %}

*No predictions resolved yet.*

{% endif %}

---

## By Analysis

| Analysis | Predictions | Resolved | Correct | Accuracy |
|----------|-------------|----------|---------|----------|
{% for analysis in analyses -%}
{% assign group_all = site.predictions | where: "analysis_title", analysis -%}
{% assign group_resolved = group_all | where: "status", "Resolved" -%}
{% assign group_correct = group_resolved | where: "verdict", "CORRECT" | size -%}
{% assign group_total = group_all | size -%}
{% assign group_resolved_count = group_resolved | size -%}
| {{ analysis }} | {{ group_total }} | {{ group_resolved_count }} | {{ group_correct }} | {% if group_resolved_count > 0 %}{{ group_correct | times: 100.0 | divided_by: group_resolved_count | round: 0 }}%{% else %}N/A{% endif %} |
{% endfor %}

---

## Methodology

### What counts as correct?

Each prediction has explicit criteria defined at time of publication:

- **Quantitative predictions:** Must meet stated threshold (e.g., "<50% growth")
- **Binary predictions:** Must occur by stated deadline
- **Qualitative predictions:** Evaluated against stated criteria with evidence

### Immutability

- Predictions are **never modified** after publication
- Original wording preserved exactly as written in each `_predictions/{ID}.md` file
- Only outcome and verdict fields updated upon resolution
- All changes logged in git history
- The pre-registration framework (`docs/pre-registration.md`) defines the immutability protocol formally

### Verification

Anyone can verify predictions by:

1. Checking git commit history for original prediction date
2. Comparing against public data sources at resolution date
3. Reviewing linked primary-source evidence

### Brier score calculation

For predictions with stated ex-ante probability, Brier = (probability - outcome)². Lower is better.

Predictions without a stated ex-ante probability (the pre-Apr-2026 batch) default to 0.50 per the pre-registration framework, yielding a contribution of 0.25 regardless of outcome. Future predictions must carry explicit probabilities at publication.

---

## Resolution Log

Detailed evidence and reasoning for each resolution. Predictions move from Pending to Resolved here. The narrative format preserves citation depth and any data-discipline notes.

| Date | ID | Action | Evidence |
|------|----|--------|----------|
| 2026-04-19 | [AV-001](/predictions/AV-001/) | Resolved INCORRECT | NVIDIA Q4 FY26 Data Center revenue $62.3B (+75% YoY) reported Feb 25, 2026 — well above the <50% threshold. Sources: [CNBC](https://www.cnbc.com/2026/02/25/nvidia-nvda-earnings-report-q4-2026.html), [ServeTheHome](https://www.servethehome.com/nvidia-reports-q4-fy2026-earnings-data-center-and-proviz-drive-revenue-records/), [NVIDIA FY25 press release](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2025) for the $35.6B Q4 FY25 baseline. |
| 2026-05-08 | [AV-002](/predictions/AV-002/) | Resolved INCORRECT | Q1 2026 calendar earnings cycle (April 29 – May 1, 2026) produced no moderation language from MSFT/GOOG/AMZN. All four hyperscalers raised or reiterated aggressive 2026 capex: Microsoft ~$190B for calendar 2026 (incl. ~$25B for higher component pricing); Alphabet raised range to $180–190B (from $175–185B); Amazon reiterated $200B; Meta raised to $125–145B (from $115–135B). Dominant exec language was supply-side ("compute constrained" — Pichai; "constrained at least through 2026" — Hood) and component-cost driven, not capex-rate moderation. Sources: [CNBC: Microsoft Q3 FY2026](https://www.cnbc.com/2026/04/29/microsoft-msft-q3-earnings-report-2026.html), [The Register: $190B capex](https://www.theregister.com/2026/04/30/microsoft_q3_2026/), [CNBC: Alphabet Q1 2026](https://www.cnbc.com/2026/04/29/alphabet-googl-q1-2026-earnings.html), [Alphabet Q1 release](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm), [CNBC: Amazon Q1 2026](https://www.cnbc.com/2026/04/29/amazon-amzn-q1-earnings-report-2026.html), [Meta Q1 release](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx), [Fortune: Meta $145B](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/). |

---

## How to use this tracker

### For consumers
- Check cumulative accuracy before weighting this source
- Click any prediction ID for the full headline, threshold, and base rate
- Compare track record to alternatives

### For replicators
- Fork and maintain your own prediction tracker
- Use the same `_predictions/` collection structure for comparability
- Build independent track record

---

*This page is auto-generated from `_predictions/`. Edit `scripts/generate_prediction_pages.py` to add or resolve predictions.*
