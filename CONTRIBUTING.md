# Contributing to Market Accurate

How to grow and improve this project—for humans and AI agents.

---

## Quick Start for AI Agents

If you're an AI agent working on this project:

**Option 1: Use the Orchestrator**
```
/orchestrate
```
Or read `.claude/orchestrator.md` and follow the Session Start Protocol.

**Option 2: Manual Priority Check**
1. **Open issues** → `gh issue list` — prioritized work items
2. **Pending predictions** → `predictions/tracker.md` — check if any have resolved
3. **Data freshness** → analysis files have dates; refresh if stale
4. **Expansion opportunities** → see Roadmap section below

[Full agent infrastructure documentation →](docs/agent-infrastructure.md)

---

## Adding New Analysis

### 1. Create the file

```
analysis/{topic}-{YYYY-MM}.md
```

### 2. Use this template

```markdown
# MARKET ACCURATE
## {Topic} Analysis
### {Month} {Day}, {Year}

---

> **Disclaimer**
>
> This is **experimental analysis**, not financial advice. The author has **no positions**
> in securities discussed. Track record is **empty/X%**—see predictions/tracker.md.
> This represents one analytical perspective; it may be wrong. Do your own research.
>
> **Version:** 0.1

---

# Executive Summary

[2-3 paragraphs: core thesis, key findings, assessment]

---

# [Main Thesis Section]

## Definition

> [One-paragraph formal statement of the thesis]

## Evidence

### 1. [First Evidence Category]

[Data, sources, analysis]

### 2. [Second Evidence Category]

[Data, sources, analysis]

---

# Predictions

[Specific, time-bound, verifiable predictions following format in CLAUDE.md]

---

# Track Record

[Link to predictions/tracker.md]

---

# Methodology

[How this analysis was produced, sources used, limitations]

---

# Replication

[CC0 license notice, how to fork/improve]
```

### 3. Add predictions via the generator script

Each prediction lives in its own file at `_predictions/{ID}.md`, generated from `scripts/generate_prediction_pages.py`. **Never hand-edit the `_predictions/` files** — they're regenerated.

To add a prediction:

1. Open `scripts/generate_prediction_pages.py`
2. Append a new `Prediction(...)` entry to the `PREDICTIONS` list with:
   - `id` (e.g., `"XX-001"`)
   - `short_title` (3–6 words)
   - `headline` (one sentence, plain English, browseable)
   - `why_matters` (one sentence explaining the stakes)
   - `claim` (the exact published wording — immutable)
   - `threshold` (specific pass/fail criteria)
   - `base_rate` (the null hypothesis or historical base rate)
   - `made`, `resolves` (YYYY-MM-DD)
   - `analysis_file`, `analysis_title`
   - `tags` (list)
   - `probability` (ex-ante, as decimal)
3. Run: `python3 scripts/generate_prediction_pages.py`
4. The `_predictions/{ID}.md` files are regenerated; tracker tables auto-update on next Jekyll build

### 4. Commit with clear message

```bash
python3 scripts/generate_prediction_pages.py  # regenerate
git add analysis/{topic}-{YYYY-MM}.md _predictions/ scripts/generate_prediction_pages.py
git commit -m "Add: {Topic} Analysis - {brief description}"
```

---

## Resolving Predictions

When a prediction's verification date arrives:

### 1. Research the outcome

- Check primary sources (SEC filings, earnings reports, official data)
- Document evidence with links

### 2. Update the generator script

In `scripts/generate_prediction_pages.py`, find the corresponding `Prediction(...)` entry and update:

- `status="Resolved"`
- `verdict="CORRECT"` or `verdict="INCORRECT"`
- `resolved_date="YYYY-MM-DD"`
- `resolution_one_liner="..."` (one-sentence summary of what happened)
- `primary_source="[Title](URL)"` (one citation; the deeper resolution narrative goes in `predictions/tracker.md` Resolution Log)

Then run: `python3 scripts/generate_prediction_pages.py`

### 3. Append to Resolution Log

`predictions/tracker.md` has a hand-maintained "Resolution Log" table at the bottom — that's where the detailed prose, multiple citations, and any data-discipline notes go. Append a new row.

### 4. Update analysis document

Add outcome to the Track Record section of the original analysis, and add a Changelog entry.

### 5. Commit

```bash
git commit -m "Resolve: {Prediction ID} - {outcome summary}"
```

---

## Refreshing Data

Analysis documents contain dated metrics. To refresh:

### 1. Identify stale data

Look for metrics older than 1 quarter in active analyses.

### 2. Research current values

Use source hierarchy from CLAUDE.md (SEC filings > earnings > surveys > journalism).

### 3. Update with changelog entry

Add to document's changelog:

```markdown
| Date | Change |
|------|--------|
| {today} | Updated {metric} from {old} to {new} (source: {link}) |
```

### 4. Commit

```bash
git commit -m "Update: Refresh {metric} in {analysis}"
```

---

## Expansion Roadmap

### Near-term additions (same methodology, adjacent topics)

1. ✅ **Semiconductor cycle analysis** — historical patterns, current position *(completed 2026-01-03)*
2. ✅ **Hyperscaler capex tracking** — quarterly updates on MSFT/GOOG/AMZN/META spend *(completed 2026-01-03)*
3. ✅ **Open-source model benchmark tracking** — systematic comparison updates *(completed 2026-01-03)*
4. ✅ **Enterprise AI adoption metrics** — survey aggregation *(completed 2026-01-03)*

### Medium-term expansions (new domains)

1. ✅ **Energy/climate** — efficiency thesis comparison to renewables *(completed 2026-01-03)*
2. ✅ **Biotech** — drug development cost curves, AI impact *(completed 2026-01-03)*
3. ✅ **Real estate** — commercial real estate vs. remote work *(completed 2026-01-03)*
4. ✅ **Labor market & AI impact** — aggregate vs. concentrated disruption *(completed 2026-04-18)*
5. ✅ **Digital assets cycle** — post-ETF institutionalization thesis *(completed 2026-04-18)*
6. ✅ **Consumer spending / retail cycle** — K-shape thesis with 5 predictions *(completed 2026-05-08)*
7. ✅ **Private credit / BDC sector** — mark-to-model breakdown thesis with 5 predictions *(completed 2026-05-08)*

### Methodology improvements

1. 🟡 **Automated data pipelines** — scaffolding + 3 fetchers in `scripts/` *(started 2026-04-18; see `scripts/README.md`)*
2. ✅ **Prediction scoring refinements** — Brier scores, calibration tracking *(completed 2026-01-03)*
3. ✅ **Comparison benchmarks** — track accuracy vs. analyst consensus *(completed 2026-01-03)*
4. ✅ **Pre-registration framework** — immutability, prep docs, resolution protocol *(completed 2026-04-18; see `docs/pre-registration.md`)*

---

## Quality Checklist

Before committing new analysis:

- [ ] Thesis is falsifiable (can be proven wrong)
- [ ] All data claims have sources and dates
- [ ] Predictions are specific, time-bound, verifiable
- [ ] Counterarguments are steelmanned
- [ ] Confidence levels are stated
- [ ] Limitations are acknowledged
- [ ] Disclaimer is present
- [ ] Added to `scripts/generate_prediction_pages.py` and regenerated `_predictions/`

---

## Using GitHub Issues

Create issues for:

- **New analysis ideas** — label: `analysis`
- **Data refresh needed** — label: `data`
- **Prediction resolution due** — label: `prediction`
- **Methodology improvements** — label: `meta`

AI agents should check `gh issue list` for prioritized work.

---

## Commit Message Convention

```
Add: [new analysis or feature]
Update: [data refresh or improvement]
Resolve: [prediction outcome]
Fix: [error correction]
Meta: [documentation, structure, process]
```

---

*The goal is accurate information. Better analysis should win.*
