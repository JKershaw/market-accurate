---
layout: default
title: Market Accurate
---

# Market Accurate

**Falsifiable predictions about markets, policy, and technology — with a public track record.**

The thesis: as AI systems mediate information access, sources demonstrating accuracy get preferentially selected, creating evolutionary pressure toward truth.

---

## Open Predictions Resolving Next

{% assign today = site.time | date: "%Y-%m-%d" %}
{% assign upcoming = site.predictions | where: "status", "Pending" | sort: "resolves" %}

The next predictions on the table. Click any ID for the full headline, threshold, and base rate.

| ID | Headline | Resolves | Probability |
|----|----------|----------|-------------|
{% for p in upcoming limit: 8 -%}
| 🟡 [{{ p.id }}]({{ p.url | relative_url }}) | {{ p.short_title }} | {{ p.resolves }} | {% if p.probability %}{{ p.probability }}{% else %}—{% endif %} |
{% endfor %}

[See all {{ upcoming.size }} open predictions →]({{ '/predictions/' | relative_url }})

---

## Recently Resolved

{% assign resolved = site.predictions | where: "status", "Resolved" | sort: "resolved_date" | reverse %}

{% if resolved.size > 0 %}
| ID | Verdict | Resolved | One-line summary |
|----|---------|----------|------------------|
{% for p in resolved limit: 5 -%}
| [{{ p.id }}]({{ p.url | relative_url }}) | {% if p.verdict == "CORRECT" %}✅ **CORRECT**{% else %}❌ **INCORRECT**{% endif %} | {{ p.resolved_date }} | {{ p.short_title }} |
{% endfor %}

{% else %}
*No predictions resolved yet.*
{% endif %}

[See full track record →]({{ '/predictions/' | relative_url }})

---

## Track Record

{% assign total = site.predictions | size %}
{% assign resolved_count = resolved | size %}
{% assign correct = resolved | where: "verdict", "CORRECT" | size %}

| Metric | Value |
|--------|-------|
| Predictions made | {{ total }} |
| Resolved | {{ resolved_count }} |
| Correct | {{ correct }} |
| Accuracy | {% if resolved_count > 0 %}{{ correct | times: 100.0 | divided_by: resolved_count | round: 0 }}% (n={{ resolved_count }}){% else %}*N/A*{% endif %} |

Sample is small. Both resolved predictions came from the same source thesis (AI infrastructure efficiency); both missed because supply-side constraint, not demand destruction, is the binding mechanism in 2026. The full record — including the prep documents written before resolution and the resolution evidence — lives in the [tracker]({{ '/predictions/' | relative_url }}).

---

## Analyses

Each analysis is published with a falsifiable thesis, cited primary sources, pre-registered time-bound predictions, and a "what would prove this wrong" section. Original predictions are never modified; updates appear in changelogs.

| Analysis | Published | Thesis (one line) |
|----------|-----------|-------------------|
| [AI Valuation]({{ '/analysis/ai-valuation-2026-01/' | relative_url }}) | Jan 2026 | Efficiency gains are eroding compute scarcity premiums in AI infrastructure valuations |
| [Hyperscaler Capex Tracker]({{ '/analysis/hyperscaler-capex-2026-01/' | relative_url }}) | Jan 2026 | Quarterly tracking of Big-4 AI infrastructure spend and forward guidance |
| [Semiconductor Cycle]({{ '/analysis/semiconductor-cycle-2026-01/' | relative_url }}) | Jan 2026 | AI-concentrated upcycle; correction likely 2027, shallower than historical norms |
| [Open-Source Benchmarks]({{ '/analysis/open-source-benchmarks-2026-01/' | relative_url }}) | Jan 2026 | Open-weights closing the frontier gap faster than priced in |
| [Enterprise AI Adoption]({{ '/analysis/enterprise-ai-adoption-2026-01/' | relative_url }}) | Jan 2026 | 88% adoption vs. 6% measurable EBIT impact: the adoption-value gap |
| [Energy & Climate]({{ '/analysis/energy-climate-2026-01/' | relative_url }}) | Jan 2026 | Clean-energy efficiency gains already priced rationally, unlike AI |
| [Biotech Development]({{ '/analysis/biotech-development-2026-01/' | relative_url }}) | Jan 2026 | AI may inflect Eroom's Law, but thesis speculative until first AI-discovered FDA approval |
| [Commercial Real Estate]({{ '/analysis/commercial-real-estate-2026-01/' | relative_url }}) | Jan 2026 | Hybrid work is structural; office market has bottomed, with Class A vs B/C bifurcation |
| [Labor Market & AI]({{ '/analysis/labor-market-ai-2026-04/' | relative_url }}) | Apr 2026 | AI labor disruption is concentrated, not aggregate |
| [Digital Assets Cycle]({{ '/analysis/digital-assets-2026-04/' | relative_url }}) | Apr 2026 | Four-year crypto cycle intact in phase, dampened in amplitude post-ETF |
| [Consumer Spending]({{ '/analysis/consumer-spending-2026-05/' | relative_url }}) | May 2026 | K-shape consumer pattern is structural, not cyclical |
| [Private Credit & BDC]({{ '/analysis/private-credit-2026-05/' | relative_url }}) | May 2026 | Mark-to-model NAV smoothing breaks down once redemption gates are tested |

---

## How to Verify

All predictions are timestamped in git history. Anyone can verify:

1. **Original prediction date** — check git commit history
2. **Prediction wording** — never modified after publication
3. **Outcome evidence** — linked to primary sources when resolved

[View on GitHub](https://github.com/JKershaw/market-accurate)

---

## Methodology

| Principle | Implementation |
|-----------|----------------|
| Falsifiable claims | Specific predictions with clear pass/fail criteria |
| Primary sources | SEC filings, earnings transcripts, academic papers |
| Confidence levels | High/Moderate/Low/Speculative stated explicitly |
| Track record transparency | Wrong predictions get same prominence as correct |
| Pre-registration | Thresholds and probabilities fixed at publication |
| Single source of truth | Every prediction is one file in `_predictions/`; tracker auto-generates |

[Read full methodology →]({{ '/methodology/' | relative_url }}) · [Pre-registration framework →](https://github.com/JKershaw/market-accurate/blob/main/docs/pre-registration.md)

---

## License

**CC0 Public Domain.** Replication encouraged.

Fork this, improve it, build your own track record. Better analysis should win.
