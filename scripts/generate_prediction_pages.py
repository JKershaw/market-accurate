#!/usr/bin/env python3
"""Generate per-prediction pages for the _predictions/ Jekyll collection.

This is the single source for prediction page generation. Editing a prediction's
metadata or headline should happen here, then this script regenerates the page.

Resolved-prediction fields (verdict, resolved date, evidence) are also defined
here so that resolutions update via the same path.

Usage:
    python3 scripts/generate_prediction_pages.py
"""

from __future__ import annotations

import os
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
COLLECTION_DIR = REPO_ROOT / "_predictions"


@dataclass
class Prediction:
    """One prediction. The single source of truth for its public-facing page."""

    id: str
    short_title: str
    headline: str  # one sentence, plain English
    why_matters: str  # one sentence
    claim: str  # exact published wording
    threshold: str
    base_rate: str  # null hypothesis or historical base rate, ≤2 sentences
    made: str  # YYYY-MM-DD
    resolves: str  # YYYY-MM-DD
    analysis_file: str  # filename stem in analysis/
    analysis_title: str
    tags: list[str] = field(default_factory=list)
    probability: str | None = None  # e.g. "0.55"; None if not pre-registered
    status: str = "Pending"  # "Pending" or "Resolved"
    verdict: str | None = None  # "CORRECT" or "INCORRECT"; None if pending
    resolved_date: str | None = None
    resolution_one_liner: str | None = None
    primary_source: str | None = None  # citation with URL
    resolution_detail_anchor: str | None = None  # link to tracker resolution log


# ---------------------------------------------------------------------------
# Data: all 52 predictions
# ---------------------------------------------------------------------------

PREDICTIONS: list[Prediction] = [
    # ----- AI Valuation Analysis (7) -----
    Prediction(
        id="AV-001",
        short_title="NVIDIA datacenter growth <50%",
        headline="NVIDIA's Q4 FY26 datacenter revenue will grow less than 50% year-over-year.",
        why_matters="A clean miss versus consensus would confirm that AI-compute demand is decelerating despite the headline narrative; a beat would suggest the efficiency-thesis is wrong about timing.",
        claim="NVIDIA Q4 FY2026 (reporting Feb 2026) datacenter revenue YoY growth will be below 50%.",
        threshold="YoY growth in Data Center segment revenue strictly less than 50% in NVIDIA's Q4 FY26 10-Q filing.",
        base_rate="Trailing four quarters had shown 50–66% YoY growth (decelerating from 100%+ in 2024). Base-rate (null) probability of clearing the <50% threshold in the immediately-next quarter: ~25%.",
        made="2026-01-03",
        resolves="2026-02-25",
        analysis_file="ai-valuation-2026-01",
        analysis_title="AI Valuation Analysis",
        tags=["ai-infrastructure", "semiconductors"],
        probability=None,
        status="Resolved",
        verdict="INCORRECT",
        resolved_date="2026-02-25",
        resolution_one_liner="Data Center revenue was $62.3B, +75% YoY versus $35.6B prior-year — well above the 50% threshold.",
        primary_source="[NVIDIA Q4 FY26 earnings report (CNBC summary, Feb 25 2026)](https://www.cnbc.com/2026/02/25/nvidia-nvda-earnings-report-q4-2026.html)",
    ),
    Prediction(
        id="AV-002",
        short_title="Hyperscaler capex moderation",
        headline="By the May 2026 earnings cycle, at least one of Microsoft, Google, or Amazon will publicly signal they're slowing AI infrastructure spending.",
        why_matters="If hyperscalers don't moderate, the demand-destruction-via-efficiency channel that underpins the AI Valuation thesis is empirically failing at the capex level.",
        claim="At least one of Microsoft, Google, Amazon will use moderating language (\"optimizing,\" \"efficiency-focused,\" \"disciplined,\" \"slower pace\") regarding AI capex in Q1 2026 earnings calls.",
        threshold="Explicit language from CEO/CFO/cloud-head in a Q1 2026 calendar earnings call indicating capex growth-rate reduction. OR a numerical reduction in stated FY26 capex guidance.",
        base_rate="No major hyperscaler had used moderation language in the prior four earnings cycles; Microsoft's FY26 \"slower pace\" reference in Q4 2025 was the only precedent. Base-rate probability of ≥1 moderating in any single Q1 cycle: ~30%.",
        made="2026-01-03",
        resolves="2026-05-08",
        analysis_file="ai-valuation-2026-01",
        analysis_title="AI Valuation Analysis",
        tags=["ai-infrastructure", "hyperscalers"],
        probability=None,
        status="Resolved",
        verdict="INCORRECT",
        resolved_date="2026-05-08",
        resolution_one_liner="All four hyperscalers raised or reiterated 2026 capex (~$700B combined midpoint) with no moderation language. Dominant narrative: supply-side constraint (\"compute constrained\" — Pichai, Hood).",
        primary_source="[The Register: Microsoft Q3 FY26 — $190B capex](https://www.theregister.com/2026/04/30/microsoft_q3_2026/)",
    ),
    Prediction(
        id="AV-003",
        short_title="Open-source GPT-4 parity on consumer GPU",
        headline="By June 2026, an open-weights AI model will match GPT-4 (March 2023) on standard benchmarks while running on a single consumer GPU.",
        why_matters="Demonstrates that frontier capability no longer requires datacenter infrastructure — direct evidence for the efficiency thesis at the model-architecture level, regardless of what hyperscaler capex does.",
        claim="By June 30, 2026, an open-weights model will match or exceed GPT-4 (March 2023 version) on MMLU, HumanEval, and GSM8K while running inference on a single consumer GPU (RTX 4090 class).",
        threshold="A single open-weights model, with publicly-downloadable Q4-or-better quantized weights fitting in 24GB VRAM, scoring MMLU ≥86.4%, HumanEval ≥67.0%, and GSM8K ≥92.0% — all three thresholds met by the same model on a single GPU.",
        base_rate="DeepSeek-R1-Distill-32B (Jan 2025) had already been reported as clearing all three thresholds at the time of prediction. Base-rate probability: ~85%.",
        made="2026-01-03",
        resolves="2026-06-30",
        analysis_file="ai-valuation-2026-01",
        analysis_title="AI Valuation Analysis",
        tags=["ai-infrastructure", "open-source"],
        probability=None,
    ),
    Prediction(
        id="AV-004",
        short_title="Enterprise AI spend <25% YoY",
        headline="By Q3 2026, a major analyst will forecast enterprise AI spending growth below 25% YoY.",
        why_matters="Tests whether the adoption-vs-ROI gap is starting to translate into forward spending intentions — the demand-side companion to the AI Valuation efficiency thesis.",
        claim="Major enterprise survey (Gartner, Forrester, IDC) will report AI spending growth intentions below 25% YoY by Q3 2026.",
        threshold="Any published Gartner, Forrester, or IDC forecast showing AI spending growth intentions <25% YoY by end of Q3 2026.",
        base_rate="2024–2025 surveys ran 30–50%+. Base-rate probability of falling below 25% within ~9 months: ~30%.",
        made="2026-01-03",
        resolves="2026-10-31",
        analysis_file="ai-valuation-2026-01",
        analysis_title="AI Valuation Analysis",
        tags=["ai-infrastructure", "enterprise-ai"],
        probability=None,
    ),
    Prediction(
        id="AV-005",
        short_title="NVIDIA+AMD+Arm market cap lower",
        headline="The combined market cap of NVIDIA, AMD, and Arm will be lower on December 31, 2026 than on January 3, 2026.",
        why_matters="The price-level test of the AI infrastructure compression thesis: if the trio's market cap is materially higher despite the efficiency story being real, the thesis is failing at the valuation channel.",
        claim="The combined market cap of NVIDIA + AMD + Arm will be lower on December 31, 2026 than on January 3, 2026.",
        threshold="Sum of NVDA + AMD + ARM market caps at close December 31, 2026 strictly less than sum at January 3, 2026 (~$4.91T using corrected baselines per AV-005 prep doc).",
        base_rate="Base-rate probability of all three semi names being collectively lower over a 12-month window in a non-recession year: ~25%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="ai-valuation-2026-01",
        analysis_title="AI Valuation Analysis",
        tags=["ai-infrastructure", "semiconductors", "valuation"],
        probability=None,
    ),
    Prediction(
        id="AV-006",
        short_title="Efficiency narrative goes mainstream",
        headline="By mid-2027, AI efficiency gains will be cited as an infrastructure-stock risk factor in at least 5 mainstream financial articles.",
        why_matters="Tests whether the analytical thesis enters consensus discourse — a leading indicator for valuation transmission.",
        claim="By mid-2027, \"AI efficiency gains\" will be cited in mainstream financial press (WSJ, FT, Bloomberg) as a recognized risk factor for AI infrastructure stocks, with at least 5 major articles.",
        threshold="At least 5 articles in WSJ, FT, or Bloomberg between Jan 2026 and June 30, 2027 that explicitly identify AI compute efficiency as a risk factor for AI infrastructure equities.",
        base_rate="Some efficiency-thesis coverage already exists in the relevant publications. Base-rate probability: ~60%.",
        made="2026-01-03",
        resolves="2027-06-30",
        analysis_file="ai-valuation-2026-01",
        analysis_title="AI Valuation Analysis",
        tags=["ai-infrastructure", "media-narrative"],
        probability=None,
    ),
    Prediction(
        id="AV-007",
        short_title="Hyperscaler absolute capex cut",
        headline="At least one major hyperscaler will reduce absolute AI capex year-over-year by end of 2027.",
        why_matters="The hard form of the capex moderation thesis — not a growth-rate slowdown but an absolute dollar cut. The clearest possible signal that the efficiency thesis is binding at the spend level.",
        claim="At least one major hyperscaler (Microsoft, Google, Amazon, Meta) will reduce absolute AI capex YoY by end of 2027.",
        threshold="Any of MSFT/GOOG/AMZN/META reports calendar-2027 capital expenditure strictly less than calendar-2026 capex in their official financial filings.",
        base_rate="Base-rate probability of any single hyperscaler cutting absolute capex YoY in a non-recession year: ~10%.",
        made="2026-01-03",
        resolves="2027-12-31",
        analysis_file="ai-valuation-2026-01",
        analysis_title="AI Valuation Analysis",
        tags=["ai-infrastructure", "hyperscalers"],
        probability=None,
    ),

    # ----- Hyperscaler Capex Tracker (2) -----
    Prediction(
        id="HC-001",
        short_title="Big-4 quarterly capex <$150B",
        headline="No single quarter in 2026 will see combined Big-4 hyperscaler capex exceed $150B.",
        why_matters="A direct test of whether the unprecedented AI capex trajectory can sustain itself for a full year, or whether ROI pressure or supply constraints force a cap.",
        claim="Combined Big-4 (MSFT/GOOG/AMZN/META) quarterly capex will peak below $150 billion in any quarter of 2026.",
        threshold="No 2026 calendar quarter shows combined MSFT + GOOGL + AMZN + META capex (cash capex including finance leases) ≥$150B per official 10-Q filings.",
        base_rate="Q3 2025 combined capex was ~$113B. Annualizing $700B FY26 guidance gives ~$175B avg quarterly. Base-rate probability of staying below $150B in every quarter: ~15%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="hyperscaler-capex-2026-01",
        analysis_title="Hyperscaler Capex Tracker",
        tags=["ai-infrastructure", "hyperscalers"],
        probability=None,
    ),
    Prediction(
        id="HC-002",
        short_title="Hyperscaler cuts FY26 guidance",
        headline="At least one hyperscaler will cut their full-year 2026 capex guidance mid-year.",
        why_matters="Mid-year guidance cuts are the textbook leading indicator of capex cycle peaks — the most concrete signal short of an outright YoY reduction.",
        claim="At least one hyperscaler will reduce full-year capex guidance mid-year in 2026 (lower guidance than previously stated for that year).",
        threshold="Explicit reduction in stated 2026 capex guidance range by any of MSFT/GOOG/AMZN/META during 2026.",
        base_rate="Guidance pattern through Q1 2026 has been monotonically upward. Base-rate probability: ~15%.",
        made="2026-01-03",
        resolves="2026-10-31",
        analysis_file="hyperscaler-capex-2026-01",
        analysis_title="Hyperscaler Capex Tracker",
        tags=["ai-infrastructure", "hyperscalers"],
        probability=None,
    ),

    # ----- Semiconductor Cycle (6) -----
    Prediction(
        id="SC-001",
        short_title="DRAM prices peak Q1/Q2",
        headline="DRAM contract prices will peak in Q1 or Q2 2026 and decline in Q3.",
        why_matters="Memory pricing is the classic semiconductor cycle leading indicator — a Q3 decline would mark this cycle's inflection point.",
        claim="DRAM contract prices will peak in Q1 or Q2 2026, with Q3 2026 showing quarter-over-quarter price decline.",
        threshold="TrendForce/DRAMeXchange contract pricing data shows Q3 2026 average DRAM contract prices lower than Q2 2026 average.",
        base_rate="Historical 3-4 year DRAM cycle suggests this is plausible timing. Base-rate probability: ~50%.",
        made="2026-01-03",
        resolves="2026-10-31",
        analysis_file="semiconductor-cycle-2026-01",
        analysis_title="Semiconductor Cycle Analysis",
        tags=["semiconductors", "memory"],
        probability=None,
    ),
    Prediction(
        id="SC-002",
        short_title="SOX underperforms S&P 500",
        headline="The SOX semiconductor index will underperform the S&P 500 in the first half of 2026.",
        why_matters="The simplest possible test of whether the semiconductor sector's 2024–2025 outperformance was the cycle peak.",
        claim="The SOX index will underperform the S&P 500 in H1 2026 (January–June).",
        threshold="SOX total return < S&P 500 total return between Jan 1, 2026 and June 30, 2026.",
        base_rate="SOX returned +41% in 2025 vs S&P 500's ~25%. Base-rate probability of mean reversion in any given 6-month window: ~50%.",
        made="2026-01-03",
        resolves="2026-07-01",
        analysis_file="semiconductor-cycle-2026-01",
        analysis_title="Semiconductor Cycle Analysis",
        tags=["semiconductors", "valuation"],
        probability=None,
    ),
    Prediction(
        id="SC-003",
        short_title="Equipment vendor YoY decline",
        headline="At least one major semiconductor equipment vendor will report a year-over-year revenue decline in Q3 or Q4 2026.",
        why_matters="Equipment vendors lead the cycle — a YoY revenue decline would be the cleanest cycle-turn signal absent a memory price collapse.",
        claim="At least one major equipment vendor (ASML, Applied Materials, Lam Research, KLA) will report YoY revenue decline in Q3 or Q4 2026.",
        threshold="Q3 or Q4 2026 quarterly revenue from any of ASML/AMAT/LRCX/KLAC strictly less than corresponding 2025 quarter, per 10-Q filings.",
        base_rate="All major vendors showed growth through Q3 2025. Base-rate probability for any single vendor to print a YoY decline within 2 quarters: ~25%.",
        made="2026-01-03",
        resolves="2027-02-28",
        analysis_file="semiconductor-cycle-2026-01",
        analysis_title="Semiconductor Cycle Analysis",
        tags=["semiconductors", "equipment"],
        probability=None,
    ),
    Prediction(
        id="SC-004",
        short_title="Foundry utilization divergence",
        headline="By Q4 2026, TSMC's trailing-edge node utilization will fall below 70% while leading-edge stays above 90%.",
        why_matters="A direct test of the desynchronized-cycle thesis: AI demand stays concentrated in leading-edge while non-AI segments stay weak.",
        claim="TSMC trailing-edge (<7nm) utilization will fall below 70% by Q4 2026 while leading-edge (3nm and below) remains above 90%.",
        threshold="Credible analyst-reported utilization data showing TSMC trailing-edge utilization <70% AND leading-edge >90% in Q4 2026.",
        base_rate="Current mix is mature 73% / advanced 100%. Continued divergence base-rate: ~40%.",
        made="2026-01-03",
        resolves="2027-01-31",
        analysis_file="semiconductor-cycle-2026-01",
        analysis_title="Semiconductor Cycle Analysis",
        tags=["semiconductors", "foundry"],
        probability=None,
    ),
    Prediction(
        id="SC-005",
        short_title="SOX 20%+ correction in 2027",
        headline="The SOX index will experience a peak-to-trough decline of at least 20% sometime in 2027.",
        why_matters="The cycle-correction thesis at index level. A 20% correction is well below historical norms (30–45%) but materially above noise.",
        claim="The SOX index will experience a peak-to-trough decline of at least 20% at some point during 2027.",
        threshold="Maximum drawdown of SOX index from any 2026/2027 peak to any 2027 trough ≥20%.",
        base_rate="Historical 3–4 year cycle pattern places a correction roughly in this window. Base-rate probability: ~55%.",
        made="2026-01-03",
        resolves="2027-12-31",
        analysis_file="semiconductor-cycle-2026-01",
        analysis_title="Semiconductor Cycle Analysis",
        tags=["semiconductors", "valuation"],
        probability=None,
    ),
    Prediction(
        id="SC-006",
        short_title="Auto semi growth > AI semi growth",
        headline="In at least one quarter of 2027, automotive semiconductor revenue growth will exceed AI/datacenter semiconductor revenue growth.",
        why_matters="A rotation signal: non-AI segments recover faster than AI decelerates. Would confirm desynchronized cycle thesis.",
        claim="Automotive semiconductor revenue growth will exceed AI/datacenter semiconductor revenue growth in at least one quarter of 2027.",
        threshold="In any 2027 calendar quarter, automotive segment YoY revenue growth (per WSTS or industry analyst aggregation) exceeds AI/datacenter segment YoY growth.",
        base_rate="Automotive has been in correction for 3 years; AI has been the sole growth driver. Base-rate probability of rotation within one quarter of 2027: ~25%.",
        made="2026-01-03",
        resolves="2027-12-31",
        analysis_file="semiconductor-cycle-2026-01",
        analysis_title="Semiconductor Cycle Analysis",
        tags=["semiconductors", "automotive"],
        probability=None,
    ),

    # ----- Open-Source Benchmarks (3) -----
    Prediction(
        id="OB-001",
        short_title="Open-weights stays within 2pt of frontier",
        headline="Open-weights AI models will stay within 2 MMLU points of proprietary frontier models through end of 2026.",
        why_matters="Tests whether the open-source-converges-with-proprietary thesis holds through a full year of frontier-lab investment.",
        claim="Open-weights models will maintain parity (within 2 points on MMLU) with proprietary frontier models through 2026.",
        threshold="At any benchmark snapshot in 2026, the gap between best proprietary MMLU and best open-weights MMLU must not exceed 2 points.",
        base_rate="Open-weights led on MMLU as of Jan 2026. Continuation base-rate: ~70%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="open-source-benchmarks-2026-01",
        analysis_title="Open-Source Benchmark Tracking",
        tags=["ai-infrastructure", "open-source"],
        probability=None,
    ),
    Prediction(
        id="OB-002",
        short_title="4B model matches Llama 2 70B on mobile",
        headline="By December 2026, a 4B-parameter or smaller open-weights model will match Llama 2 70B performance on a mobile device.",
        why_matters="The strongest possible test of the parameter-efficiency thesis: capability collapse onto consumer-mobile hardware.",
        claim="A 4B parameter or smaller open-weights model will match Llama 2 70B performance (MMLU ~69%) while running on mobile devices by end of 2026.",
        threshold="Open-weights model with ≤5B parameters achieving MMLU ≥68%, demonstrated running on a mobile chipset (Snapdragon-class or Apple Silicon mobile).",
        base_rate="Multiple sub-5B models near this threshold; Phi-4-mini and Qwen 3 small variants are candidates. Base-rate probability: ~50%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="open-source-benchmarks-2026-01",
        analysis_title="Open-Source Benchmark Tracking",
        tags=["ai-infrastructure", "open-source", "edge-compute"],
        probability=None,
    ),
    Prediction(
        id="OB-003",
        short_title="Frontier training <$1M",
        headline="By end of 2026, at least one lab will demonstrate frontier-class model training for under $1M total compute cost.",
        why_matters="If frontier capability can be reached for <$1M, the compute moat collapses and the AI infrastructure thesis breaks at the training-cost level.",
        claim="By end of 2026, at least one lab will demonstrate frontier-class model training (MMLU >85%) for under $1M total compute cost.",
        threshold="Documented training cost <$1M (with credible methodology, not promotional estimate) for a model achieving MMLU ≥85% by Dec 31, 2026.",
        base_rate="Multiple sub-$10M frontier runs reported; strict <$1M is much harder. Base-rate probability: ~30%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="open-source-benchmarks-2026-01",
        analysis_title="Open-Source Benchmark Tracking",
        tags=["ai-infrastructure", "open-source"],
        probability=None,
    ),

    # ----- Enterprise AI Adoption (3) -----
    Prediction(
        id="EA-001",
        short_title="2027 AI spend forecast <25%",
        headline="By June 30, 2026, at least one major analyst will forecast 2027 AI spending growth below 25%.",
        why_matters="A leading indicator of demand-side fatigue: analysts publicly downgrading multi-year AI spending forecasts.",
        claim="Enterprise AI spending growth will fall below 25% YoY in at least one major analyst forecast (IDC, Gartner, Forrester) for 2027 by Q2 2026.",
        threshold="Published forecast from IDC, Gartner, or Forrester showing <25% YoY enterprise AI spending growth for calendar 2027, by June 30, 2026.",
        base_rate="Gartner AI software 2027 forecast was 20.4% as of Jan 2026 (already below threshold). Base-rate probability: ~75%.",
        made="2026-01-03",
        resolves="2026-06-30",
        analysis_file="enterprise-ai-adoption-2026-01",
        analysis_title="Enterprise AI Adoption Metrics",
        tags=["enterprise-ai", "demand"],
        probability=None,
    ),
    Prediction(
        id="EA-002",
        short_title="Consulting firm publishes >80% failure rate",
        headline="By end of 2026, a major consulting firm will publish a report documenting AI project failure rates above 80%.",
        why_matters="Tier-1 consulting reports are the primary mechanism by which AI-ROI concerns enter CFO/CIO budget discussions.",
        claim="At least one major consulting firm (McKinsey, BCG, Bain, Deloitte) will publish a report documenting AI project failure rates above 80% by end of 2026.",
        threshold="Published report from McKinsey, BCG, Bain, or Deloitte showing >80% AI project failure rate, dated before Dec 31, 2026.",
        base_rate="Current published rates from these firms are in the 70–85% range. Base-rate probability of crossing 80% threshold in any single report within 12 months: ~50%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="enterprise-ai-adoption-2026-01",
        analysis_title="Enterprise AI Adoption Metrics",
        tags=["enterprise-ai", "media-narrative"],
        probability=None,
    ),
    Prediction(
        id="EA-003",
        short_title="3+ Fortune 500 disclose AI ROI",
        headline="By Q4 2026, at least 3 Fortune 500 companies will publicly disclose specific dollar AI ROI figures in earnings reports.",
        why_matters="The opposite-tail test: enterprises proving (not just claiming) AI ROI. If 3+ disclose specific numbers, the bear thesis loses its strongest argument.",
        claim="By Q4 2026, at least 3 Fortune 500 companies will publicly disclose quantified AI ROI metrics in earnings reports (specific dollar figures, not just percentages).",
        threshold="Specific, quantified AI ROI disclosure (with dollar amounts) in 3+ Fortune 500 earnings transcripts or releases by Feb 2027.",
        base_rate="As of Jan 2026, very few Fortune 500 disclose specific AI ROI dollars. Base-rate probability: ~30%.",
        made="2026-01-03",
        resolves="2027-02-28",
        analysis_file="enterprise-ai-adoption-2026-01",
        analysis_title="Enterprise AI Adoption Metrics",
        tags=["enterprise-ai", "disclosure"],
        probability=None,
    ),

    # ----- Energy & Climate (4) -----
    Prediction(
        id="EC-001",
        short_title="Solar remains cheapest electricity",
        headline="Solar will remain the cheapest new source of electricity globally through 2026.",
        why_matters="Confirms the renewables-efficiency thesis: cost-curve gains compound rather than reverse.",
        claim="Utility-scale solar LCOE will remain the cheapest source of new electricity generation globally through 2026.",
        threshold="No other generation source (gas, nuclear, wind) achieves lower unsubsidized LCOE than solar in any major market per Lazard or BNEF reports for 2026.",
        base_rate="Solar has been cheapest since ~2020. Base-rate probability of continuation: ~85%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="energy-climate-2026-01",
        analysis_title="Energy & Climate Analysis",
        tags=["energy", "renewables"],
        probability="0.85",
    ),
    Prediction(
        id="EC-002",
        short_title="EV battery <$100/kWh",
        headline="By end of 2026, lithium-ion EV battery pack prices will fall below $100/kWh.",
        why_matters="$100/kWh is the long-standing parity-with-ICE threshold; crossing it would mark a real industrial milestone.",
        claim="Lithium-ion battery pack prices will fall below $100/kWh for EV applications by end of 2026.",
        threshold="BloombergNEF or equivalent reports average EV pack price <$100/kWh in 2026 annual survey.",
        base_rate="EV pack at $108/kWh as of 2025; cost trajectory suggests this is tight but plausible. Base-rate probability: ~55%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="energy-climate-2026-01",
        analysis_title="Energy & Climate Analysis",
        tags=["energy", "batteries", "ev"],
        probability="0.60",
    ),
    Prediction(
        id="EC-003",
        short_title="$50B+ clean energy projects cancelled",
        headline="At least $50B in announced clean energy projects will be cancelled or indefinitely delayed due to U.S. policy uncertainty in 2026.",
        why_matters="The policy-risk tail of the clean-energy thesis: if cancellations cross $50B, the IRA rollback risk is materially binding.",
        claim="At least $50B in announced clean energy projects will be cancelled or indefinitely delayed due to U.S. policy uncertainty in 2026.",
        threshold="Documented project cancellations or indefinite delays citing IRA/policy uncertainty totaling ≥$50B in 2026.",
        base_rate="Q1 2025 saw early cancellations but at smaller scale. Base-rate probability: ~50%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="energy-climate-2026-01",
        analysis_title="Energy & Climate Analysis",
        tags=["energy", "policy", "renewables"],
        probability="0.50",
    ),
    Prediction(
        id="EC-004",
        short_title="3+ utilities cite AI data-center demand",
        headline="In 2026, at least 3 major utilities will explicitly cite AI data-center electricity demand as a growth driver in earnings calls.",
        why_matters="Tests whether AI compute is producing measurable spillovers into the electricity sector via grid utility revenue.",
        claim="AI data center electricity demand will be cited as a growth driver by at least 3 major utility companies in 2026 earnings calls.",
        threshold="Explicit mentions of AI/data center demand as a growth driver in earnings transcripts of 3+ major US utilities (e.g., NEE, DUK, SO, AEP) during 2026.",
        base_rate="Several utilities already cite AI data-center demand. Base-rate probability: ~80%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="energy-climate-2026-01",
        analysis_title="Energy & Climate Analysis",
        tags=["energy", "utilities", "ai-infrastructure"],
        probability="0.80",
    ),

    # ----- Biotech Development (4) -----
    Prediction(
        id="BT-001",
        short_title="First AI-discovered FDA approval",
        headline="By end of 2027, the first AI-discovered drug will receive FDA approval.",
        why_matters="The single most important test of whether AI is inflecting Eroom's Law in drug discovery.",
        claim="The first AI-discovered drug (where AI was used for target identification or molecular design) will receive FDA approval by December 31, 2027.",
        threshold="FDA approval of a drug where the discovering company explicitly claims AI was central to discovery, before Dec 31, 2027.",
        base_rate="No AI-discovered drug has yet been approved; multiple in late-stage trials. Base-rate probability: ~55%.",
        made="2026-01-03",
        resolves="2027-12-31",
        analysis_file="biotech-development-2026-01",
        analysis_title="Biotech Development Cost Analysis",
        tags=["biotech", "ai-applications"],
        probability="0.60",
    ),
    Prediction(
        id="BT-002",
        short_title="3+ AI drugs complete Phase III with >55% success",
        headline="By end of 2027, at least 3 AI-discovered drugs will have completed Phase III with combined success rate above 55%.",
        why_matters="The early-validation test of whether AI's Phase I 80–90% success rates translate into late-stage performance.",
        claim="At least 3 AI-discovered drugs will have completed Phase III trials with a combined success rate above 55% by end of 2027.",
        threshold="Documented Phase III outcomes for 3+ AI-discovered molecules, combined success rate >55%, before Dec 31, 2027.",
        base_rate="Phase III pipeline is thin (~5 candidates). Base-rate probability: ~35%.",
        made="2026-01-03",
        resolves="2027-12-31",
        analysis_file="biotech-development-2026-01",
        analysis_title="Biotech Development Cost Analysis",
        tags=["biotech", "ai-applications"],
        probability="0.40",
    ),
    Prediction(
        id="BT-003",
        short_title="Biopharma M&A >$100B in 2026",
        headline="Total biopharma M&A deal value in 2026 will exceed $100 billion.",
        why_matters="Patent cliff pressure (2026–2028) creates structural M&A demand; this tests whether it materializes at scale.",
        claim="Total biopharma M&A deal value in 2026 will exceed $100 billion, driven by patent cliff pressure.",
        threshold="Reported aggregate biopharma M&A deal value in calendar 2026 ≥$100B per M&A database aggregation.",
        base_rate="2024 was $77B; 2023 was $153.5B. Base-rate probability: ~65%.",
        made="2026-01-03",
        resolves="2027-02-28",
        analysis_file="biotech-development-2026-01",
        analysis_title="Biotech Development Cost Analysis",
        tags=["biotech", "m-and-a"],
        probability="0.65",
    ),
    Prediction(
        id="BT-004",
        short_title="XBI 20% drawdown if no AI approval",
        headline="If no AI-discovered drug receives FDA approval by end of 2026, XBI will have a 20% drawdown during 2026.",
        why_matters="The market-pricing-of-disappointment test: tests whether AI-biotech valuations require an approval to hold up.",
        claim="XBI will experience at least one 20% drawdown from any 2026 peak if no AI-discovered drug receives FDA approval by end of 2026.",
        threshold="Conditional: if no AI-discovered drug approval by Dec 31, 2026, XBI must show ≥20% peak-to-trough decline within 2026.",
        base_rate="XBI volatility historically supports 20% drawdowns in ~40% of years. Base-rate probability (conditional): ~50%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="biotech-development-2026-01",
        analysis_title="Biotech Development Cost Analysis",
        tags=["biotech", "valuation"],
        probability="0.35",
    ),

    # ----- Commercial Real Estate (4) -----
    Prediction(
        id="CRE-001",
        short_title="National office vacancy <18% by Q4 2026",
        headline="By Q4 2026, national U.S. office vacancy will decline below 18%.",
        why_matters="The headline test of the office-market-has-bottomed thesis.",
        claim="National office vacancy rate will decline below 18% by Q4 2026.",
        threshold="Reported Q4 2026 national US office vacancy <18% per Yardi Matrix or CBRE.",
        base_rate="Q3 2025 at 18.6%, peak was 19.6%. Base-rate probability: ~55%.",
        made="2026-01-03",
        resolves="2027-02-28",
        analysis_file="commercial-real-estate-2026-01",
        analysis_title="Commercial Real Estate Analysis",
        tags=["real-estate", "office"],
        probability="0.55",
    ),
    Prediction(
        id="CRE-002",
        short_title="Class A REITs outperform B/C by 15%+",
        headline="Class A office REITs will outperform Class B/C-focused REITs by at least 15 percentage points in 2026.",
        why_matters="The price-level test of the bifurcation thesis: quality holds, lower-tier obsolesces.",
        claim="Class A office REITs will outperform Class B/C-focused REITs by at least 15 percentage points in 2026 total return.",
        threshold="Documented performance differential of ≥15pp between Class A and Class B/C office REIT baskets for calendar 2026.",
        base_rate="Bifurcation already underway; 15pp is meaningful but not extreme. Base-rate probability: ~60%.",
        made="2026-01-03",
        resolves="2027-01-31",
        analysis_file="commercial-real-estate-2026-01",
        analysis_title="Commercial Real Estate Analysis",
        tags=["real-estate", "office", "valuation"],
        probability="0.60",
    ),
    Prediction(
        id="CRE-003",
        short_title="50M+ sq ft office conversion announced",
        headline="At least 50 million square feet of office space will be announced for conversion or demolition in 2026.",
        why_matters="The supply-side adjustment mechanism — if announcements cross 50M sq ft, the office overhang is actively being unwound.",
        claim="At least 50 million square feet of office space will be announced for conversion or demolition in 2026.",
        threshold="Documented announcements totaling ≥50M sq ft of office conversion or demolition in calendar 2026.",
        base_rate="Conversion pace accelerating but historically below this level. Base-rate probability: ~50%.",
        made="2026-01-03",
        resolves="2026-12-31",
        analysis_file="commercial-real-estate-2026-01",
        analysis_title="Commercial Real Estate Analysis",
        tags=["real-estate", "office"],
        probability="0.50",
    ),
    Prediction(
        id="CRE-004",
        short_title="San Francisco vacancy stays >25%",
        headline="San Francisco office vacancy will remain above 25% through 2026.",
        why_matters="The persistent-weak-tail test: even as national vacancy normalizes, the worst-hit markets stay structurally damaged.",
        claim="San Francisco office vacancy will remain above 25% through 2026.",
        threshold="Q4 2026 San Francisco office vacancy >25% per CoStar or CBRE.",
        base_rate="Currently 32.5%; would need 7+pp improvement to fall below 25%. Base-rate probability: ~75%.",
        made="2026-01-03",
        resolves="2027-02-28",
        analysis_file="commercial-real-estate-2026-01",
        analysis_title="Commercial Real Estate Analysis",
        tags=["real-estate", "office"],
        probability="0.75",
    ),

    # ----- Labor Market & AI (4) -----
    Prediction(
        id="LM-001",
        short_title="Unemployment 3.8–4.5%, no AI attribution",
        headline="US unemployment will stay between 3.8% and 4.5% through 2026, with no AI attribution in official reports.",
        why_matters="The aggregate-disruption-thesis-fails test: AI labor disruption is real but invisible at the macro headline level.",
        claim="US unemployment stays in the 3.8–4.5% band through 2026, and no Fed/CBO/BLS official report attributes meaningful labor disruption to AI.",
        threshold="Monthly BLS unemployment readings all between 3.8% and 4.5% in 2026, AND no major Fed/BLS/CBO release explicitly attributes labor disruption to AI.",
        base_rate="Base-rate probability of unemployment staying in any 70bps band: ~50%. Conjunction with no-attribution: ~65%.",
        made="2026-04-18",
        resolves="2027-02-28",
        analysis_file="labor-market-ai-2026-04",
        analysis_title="Labor Market & AI Impact Analysis",
        tags=["labor", "ai-applications"],
        probability="0.65",
    ),
    Prediction(
        id="LM-002",
        short_title="New-grad tech hiring ≥15% down YoY",
        headline="New-graduate tech hiring will be at least 15% lower in 2026 than 2024.",
        why_matters="The concentrated-disruption thesis at its sharpest point: entry-level SWE is the canary in the coal mine.",
        claim="New-grad tech hiring will be at least 15% down YoY (2026 vs 2024).",
        threshold="LinkedIn Workforce Insights or BLS data shows 2026 new-graduate tech hiring volume ≥15% below 2024 baseline.",
        base_rate="New-grad tech hiring already weak in 2024; a further 15% decline is meaningful. Base-rate probability: ~60%.",
        made="2026-04-18",
        resolves="2027-06-30",
        analysis_file="labor-market-ai-2026-04",
        analysis_title="Labor Market & AI Impact Analysis",
        tags=["labor", "ai-applications"],
        probability="0.60",
    ),
    Prediction(
        id="LM-003",
        short_title="CSR (BLS 43-4051) ≥5% decline 2024→2026",
        headline="Customer service representative headcount (BLS 43-4051) will decline at least 5% from 2024 to 2026.",
        why_matters="The occupational-specificity test: AI is replacing job categories visible in BLS OES data, not the aggregate labor force.",
        claim="BLS Customer Service Representative (43-4051) headcount declines ≥5% from 2024 to 2026.",
        threshold="BLS Occupational Employment Statistics (OES) 43-4051 headcount in 2026 is at least 5% lower than 2024 OES headcount.",
        base_rate="CSR occupation already shrinking pre-AI. Base-rate probability of ≥5% decline over 2 years: ~55%.",
        made="2026-04-18",
        resolves="2027-05-31",
        analysis_file="labor-market-ai-2026-04",
        analysis_title="Labor Market & AI Impact Analysis",
        tags=["labor", "ai-applications"],
        probability="0.55",
    ),
    Prediction(
        id="LM-004",
        short_title="No consulting AI-unemployment wave",
        headline="No Tier-1 consulting firm will declare an aggregate AI-unemployment wave through 2026.",
        why_matters="Consulting firms typically frame employment disruption narratives. Their silence is itself a signal that disruption stays concentrated.",
        claim="No Tier-1 consulting firm (McKinsey, BCG, Bain, Deloitte) declares an aggregate AI-driven unemployment wave through 2026.",
        threshold="No publication from McKinsey/BCG/Bain/Deloitte during 2026 explicitly characterizes a broad-based AI-driven unemployment wave.",
        base_rate="Consulting narrative has so far been productivity-positive. Base-rate probability of continuation: ~75%.",
        made="2026-04-18",
        resolves="2026-12-31",
        analysis_file="labor-market-ai-2026-04",
        analysis_title="Labor Market & AI Impact Analysis",
        tags=["labor", "media-narrative"],
        probability="0.75",
    ),

    # ----- Digital Assets Cycle (5) -----
    Prediction(
        id="DA-001",
        short_title="BTC ≥40% drawdown Apr 2026 – Dec 2027",
        headline="Between April 2026 and December 2027, Bitcoin will experience at least a 40% peak-to-trough drawdown.",
        why_matters="The four-year-cycle test in the post-ETF era. A 40% drawdown is the soft form of the cycle persisting.",
        claim="BTC will experience ≥40% peak-to-trough drawdown between April 2026 and December 2027.",
        threshold="Max drawdown from any peak in [Apr 2026, Dec 2027] to any subsequent trough in same window ≥40%.",
        base_rate="BTC historically has 40%+ drawdowns in roughly 70% of any 18-month window. Base-rate probability: ~65%.",
        made="2026-04-18",
        resolves="2027-12-31",
        analysis_file="digital-assets-2026-04",
        analysis_title="Digital Assets Cycle Analysis",
        tags=["crypto", "valuation"],
        probability="0.65",
    ),
    Prediction(
        id="DA-002",
        short_title="BTC ETF flow/price correlation >0.5",
        headline="The correlation between spot BTC ETF flows and BTC price will stay above 0.5 through 2026.",
        why_matters="Tests whether ETF flows are the primary marginal-buyer mechanism in the post-spot-ETF crypto cycle.",
        claim="Spot BTC ETF flow/price correlation stays above 0.5 through 2026.",
        threshold="Rolling 90-day correlation between aggregate spot BTC ETF net flows and BTC price stays >0.5 throughout 2026.",
        base_rate="Correlation has been elevated since ETF approval. Base-rate probability: ~60%.",
        made="2026-04-18",
        resolves="2027-01-31",
        analysis_file="digital-assets-2026-04",
        analysis_title="Digital Assets Cycle Analysis",
        tags=["crypto", "etf"],
        probability="0.60",
    ),
    Prediction(
        id="DA-003",
        short_title="USDT+USDC combined supply >$300B",
        headline="At some point in 2026, combined USDT and USDC supply will exceed $300B.",
        why_matters="Stablecoin supply is the de facto crypto monetary base; $300B would mark a structural-growth threshold.",
        claim="Combined USDT+USDC supply exceeds $300B at some point in 2026.",
        threshold="Per DeFiLlama or aggregator data, combined USDT + USDC supply ≥$300B on any day in 2026.",
        base_rate="Combined supply has been growing strongly. Base-rate probability: ~60%.",
        made="2026-04-18",
        resolves="2026-12-31",
        analysis_file="digital-assets-2026-04",
        analysis_title="Digital Assets Cycle Analysis",
        tags=["crypto", "stablecoins"],
        probability="0.60",
    ),
    Prediction(
        id="DA-004",
        short_title="No US-regulated stablecoin peg break",
        headline="No US-regulated stablecoin will break its peg by more than 2% for more than 24 hours in 2026.",
        why_matters="Tests whether the post-SVB regulatory environment has actually stabilized fiat-backed stablecoins.",
        claim="No US-regulated stablecoin (USDC, PYUSD, etc.) breaks peg by >2% for >24 hours during 2026.",
        threshold="No US-regulated stablecoin trades >2% below $1 for a continuous 24-hour window during 2026.",
        base_rate="Strong regulatory framework + Treasury-backed reserves. Base-rate probability: ~80%.",
        made="2026-04-18",
        resolves="2026-12-31",
        analysis_file="digital-assets-2026-04",
        analysis_title="Digital Assets Cycle Analysis",
        tags=["crypto", "stablecoins"],
        probability="0.80",
    ),
    Prediction(
        id="DA-005",
        short_title="2026 BTC drawdown smaller than 77%",
        headline="If Bitcoin has a drawdown in 2026, it will be smaller than 77% (the 2022 cycle benchmark).",
        why_matters="The amplitude-dampening test: post-ETF cycle keeps the four-year rhythm but with smaller swings.",
        claim="2026 BTC drawdown (if any) is smaller than 77% (the 2022 analogue).",
        threshold="Maximum BTC peak-to-trough drawdown within 2026 calendar year is <77%.",
        base_rate="Post-spot-ETF context suggests amplitude dampening. Base-rate probability: ~60%.",
        made="2026-04-18",
        resolves="2026-12-31",
        analysis_file="digital-assets-2026-04",
        analysis_title="Digital Assets Cycle Analysis",
        tags=["crypto", "valuation"],
        probability="0.60",
    ),

    # ----- Consumer Spending (5) -----
    Prediction(
        id="CS-001",
        short_title="Subprime auto 60+ DPD >6% in 2026",
        headline="Subprime auto loan 60+ day delinquencies will stay above 6% in at least three of four 2026 quarters.",
        why_matters="The cleanest signal of K-shape consumer distress: subprime delinquencies at multi-decade records while prime stays clean.",
        claim="US subprime auto loan 60+ DPD delinquency rate stays above 6.0% in at least 3 of 4 quarterly NY Fed Household Debt and Credit reports covering 2026.",
        threshold="≥3 of 4 quarterly NY Fed Household Debt and Credit Reports for 2026 show subprime 60+ DPD >6.0%.",
        base_rate="January 2026 record at ~6.5%; historical persistence of stress conditions. Base-rate probability: ~70%.",
        made="2026-05-08",
        resolves="2027-02-28",
        analysis_file="consumer-spending-2026-05",
        analysis_title="Consumer Spending & Retail Cycle Analysis",
        tags=["consumer-cycle", "credit"],
        probability="0.70",
    ),
    Prediction(
        id="CS-002",
        short_title="Discount basket beats mid-tier mall by 10pp",
        headline="A discount-retailer basket (DG, DLTR, FIVE) will beat a mid-tier mall basket (M, KSS, GPS) by 10+ percentage points over the next year.",
        why_matters="The K-shape thesis at sector-rotation level: lower-income trade-down beneficiaries vs. squeezed mid-tier.",
        claim="Equal-weighted basket of (DG, DLTR, FIVE) total return beats equal-weighted basket of (M, KSS, GPS) by ≥10pp over May 8, 2026 → April 30, 2027.",
        threshold="Discount basket total return − mid-tier basket total return ≥10pp over the specified period.",
        base_rate="Sector-rotation persistence base-rate: ~50%. K-shape tailwind: ~55%.",
        made="2026-05-08",
        resolves="2027-05-07",
        analysis_file="consumer-spending-2026-05",
        analysis_title="Consumer Spending & Retail Cycle Analysis",
        tags=["consumer-cycle", "retail"],
        probability="0.55",
    ),
    Prediction(
        id="CS-003",
        short_title="Credit card 90+ DPD ≥4%",
        headline="Credit card 90+ day delinquencies will reach or exceed 4% in at least one 2026 quarter.",
        why_matters="The K-shape thesis breaking out of subprime auto into the broader card portfolio — a contagion signal.",
        claim="Aggregate credit card 90+ DPD delinquency rate (NY Fed series) reaches ≥4.0% in any 2026 quarter.",
        threshold="Any quarterly NY Fed Household Debt and Credit Report for 2026 shows credit card 90+ DPD ≥4.0%.",
        base_rate="Currently rising but below 4%. Base-rate probability: ~45%.",
        made="2026-05-08",
        resolves="2027-02-28",
        analysis_file="consumer-spending-2026-05",
        analysis_title="Consumer Spending & Retail Cycle Analysis",
        tags=["consumer-cycle", "credit"],
        probability="0.45",
    ),
    Prediction(
        id="CS-004",
        short_title="2026 retail sales < NRF 4.4% forecast",
        headline="2026 US retail sales growth will come in below the NRF's 4.4% forecast.",
        why_matters="Direct test of whether headline retail strength assumed by NRF and consensus actually holds up against K-shape distributional risk.",
        claim="Calendar-year 2026 actual US retail sales growth (per Census Bureau Monthly Retail Trade) below NRF +4.4% YoY forecast.",
        threshold="Census 2026 retail sales annual growth <4.4%.",
        base_rate="NRF forecasts have been roughly accurate historically. Base-rate probability of undershooting: ~50%.",
        made="2026-05-08",
        resolves="2027-02-17",
        analysis_file="consumer-spending-2026-05",
        analysis_title="Consumer Spending & Retail Cycle Analysis",
        tags=["consumer-cycle", "retail"],
        probability="0.55",
    ),
    Prediction(
        id="CS-005",
        short_title="Fed governor cites K-shape",
        headline="At least one Federal Reserve governor or Reserve Bank president will explicitly reference the K-shape consumer in 2026.",
        why_matters="When a Fed governor cites K-shape, the narrative is consensus rather than fringe — and rate decisions begin reflecting it.",
        claim="At least one Fed Board governor or Reserve Bank president explicitly references K-shape consumer dynamics or income bifurcation in a 2026 speech or testimony.",
        threshold="Documented mention in any Fed speech transcript or congressional testimony during calendar 2026.",
        base_rate="Fed has cited K-shape before in prior cycles. Base-rate probability: ~75%.",
        made="2026-05-08",
        resolves="2027-01-31",
        analysis_file="consumer-spending-2026-05",
        analysis_title="Consumer Spending & Retail Cycle Analysis",
        tags=["consumer-cycle", "policy"],
        probability="0.75",
    ),

    # ----- Private Credit & BDC (5) -----
    Prediction(
        id="PC-001",
        short_title="BDC median non-accruals ≥4%",
        headline="The KBRA-universe median BDC non-accrual rate will reach 4% or higher in at least one 2026 quarter.",
        why_matters="The mark-to-model-breakdown test: as defaults migrate from idiosyncratic to systemic, the industry median moves materially.",
        claim="Median non-accrual rate at cost across rated BDCs (KBRA universe) reaches ≥4.0% in any 2026 quarterly compendium.",
        threshold="Any 2026 quarterly KBRA BDC Compendium shows median non-accruals ≥4.0% at cost.",
        base_rate="Q3 2025 median was 2.5%; trajectory suggests this is tight but plausible. Base-rate probability: ~55%.",
        made="2026-05-08",
        resolves="2027-02-28",
        analysis_file="private-credit-2026-05",
        analysis_title="Private Credit & BDC Sector Analysis",
        tags=["credit-cycle", "private-credit"],
        probability="0.55",
    ),
    Prediction(
        id="PC-002",
        short_title="5+ BDC dividend cuts of ≥10%",
        headline="At least 5 publicly traded BDCs will cut their base dividend by 10% or more in 2026.",
        why_matters="Dividend cuts are the most concrete signal that NII compression has reached the level where it can't be smoothed away.",
        claim="At least 5 publicly traded BDCs with market cap >$500M cut quarterly base dividend by ≥10% in calendar 2026.",
        threshold="5 distinct public BDCs (with market cap >$500M at May 8, 2026) reduce base dividend by ≥10% before Dec 31, 2026.",
        base_rate="FS KKR cut by 25% in Q1 2026; one cut so far. Base-rate probability of additional 4: ~70%.",
        made="2026-05-08",
        resolves="2027-01-31",
        analysis_file="private-credit-2026-05",
        analysis_title="Private Credit & BDC Sector Analysis",
        tags=["credit-cycle", "private-credit"],
        probability="0.70",
    ),
    Prediction(
        id="PC-003",
        short_title="Major non-traded BDC gating event",
        headline="At least one major non-traded BDC will invoke its redemption gate or suspend share repurchases in 2026.",
        why_matters="Gating is the visible failure mode of the mark-to-model architecture when redemption pressure exceeds the smoothed-NAV math.",
        claim="At least one major non-traded perpetual BDC (>$10B AUM at start of 2026) invokes redemption gate or formally suspends share repurchases in 2026.",
        threshold="Documented gate invocation or repurchase suspension in any non-traded BDC SEC filing, press release, or investor letter during 2026.",
        base_rate="BCRED record redemptions ($3.8B / 7.9% AUM) in Q1 2026 was already gating-adjacent. Base-rate probability: ~50%.",
        made="2026-05-08",
        resolves="2027-01-31",
        analysis_file="private-credit-2026-05",
        analysis_title="Private Credit & BDC Sector Analysis",
        tags=["credit-cycle", "private-credit"],
        probability="0.50",
    ),
    Prediction(
        id="PC-004",
        short_title="BIZD underperforms HYG by 10pp+",
        headline="The BDC ETF (BIZD) will underperform the high-yield bond ETF (HYG) by 10+ percentage points May–December 2026.",
        why_matters="The cleanest market-level test of whether BDC repricing keeps pace with broader credit, or whether the asset class is structurally cracking.",
        claim="BIZD total return underperforms HYG total return by ≥10pp between May 8, 2026 and Dec 31, 2026.",
        threshold="BIZD total return − HYG total return ≤ -10pp over specified window.",
        base_rate="BIZD has already underperformed YTD. Continuation base-rate: ~55%.",
        made="2026-05-08",
        resolves="2027-01-01",
        analysis_file="private-credit-2026-05",
        analysis_title="Private Credit & BDC Sector Analysis",
        tags=["credit-cycle", "private-credit", "valuation"],
        probability="0.55",
    ),
    Prediction(
        id="PC-005",
        short_title="BDC sponsor strategic transaction",
        headline="At least one major BDC sponsor will announce a strategic sale, merger, or wind-down of a credit business in 2026.",
        why_matters="The industry-consolidation test: when sponsor equity is down 40–66% and a credit business sale or wind-down is publicly announced, the cycle has been admitted to.",
        claim="At least one major BDC sponsor (Apollo, Blackstone, Ares, KKR, Blue Owl, FS Investments) announces strategic transaction (sale/merger/wind-down) of a private credit business unit in 2026.",
        threshold="Documented announcement (SEC 8-K, press release, WSJ/FT/Bloomberg coverage) of sale, merger, or wind-down of a credit-related fund family in 2026.",
        base_rate="Sponsor equity drawdowns are at cycle-deep levels but strategic transactions still rare. Base-rate probability: ~40%.",
        made="2026-05-08",
        resolves="2027-01-31",
        analysis_file="private-credit-2026-05",
        analysis_title="Private Credit & BDC Sector Analysis",
        tags=["credit-cycle", "private-credit", "m-and-a"],
        probability="0.40",
    ),
]


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------


def render(p: Prediction) -> str:
    """Render one prediction file."""

    front_matter_lines = [
        "---",
        f"id: {p.id}",
        f'title: "{p.id}: {p.short_title}"',
        f"short_title: \"{p.short_title}\"",
        f"made: {p.made}",
        f"resolves: {p.resolves}",
        f"status: {p.status}",
    ]
    if p.verdict:
        front_matter_lines.append(f"verdict: {p.verdict}")
    if p.resolved_date:
        front_matter_lines.append(f"resolved_date: {p.resolved_date}")
    front_matter_lines.append(f"analysis_file: {p.analysis_file}")
    front_matter_lines.append(f'analysis_title: "{p.analysis_title}"')
    front_matter_lines.append(f"tags: [{', '.join(p.tags)}]")
    if p.probability:
        front_matter_lines.append(f"probability: {p.probability}")
    front_matter_lines.append("---")

    # Status emoji for visual indicator
    if p.status == "Resolved":
        status_emoji = "✅ CORRECT" if p.verdict == "CORRECT" else "❌ INCORRECT"
    else:
        status_emoji = "🟡 Pending"

    body = textwrap.dedent(f"""
        # {p.id}: {p.short_title}

        **Status:** {status_emoji}

        **Headline:** {p.headline}

        **Why this matters:** {p.why_matters}

        ---

        ## Full claim

        {p.claim}

        ## Threshold

        {p.threshold}

        ## Base rate

        {p.base_rate}

        ## Key facts

        | Field | Value |
        |-------|-------|
        | Made | {p.made} |
        | Resolves | {p.resolves} |
        | Source analysis | [{p.analysis_title}](/analysis/{p.analysis_file}/) |
        | Tags | {', '.join(p.tags) if p.tags else '—'} |
        | Ex-ante probability | {p.probability if p.probability else '*not pre-registered*'} |
    """).strip()

    if p.status == "Resolved":
        body += "\n\n---\n\n## Verdict\n\n"
        body += f"**Outcome:** {p.verdict}\n\n"
        body += f"**Resolved:** {p.resolved_date}\n\n"
        body += f"**One-line summary:** {p.resolution_one_liner}\n\n"
        if p.primary_source:
            body += f"**Primary source:** {p.primary_source}\n\n"
        body += "**Full resolution analysis:** see [tracker resolution log](/predictions/#resolution-log).\n"
    else:
        body += "\n\n---\n\n## Tracking assessment\n\n"
        body += "*Interim assessments are added quarterly.*\n"

    return "\n".join(front_matter_lines) + "\n" + body + "\n"


def main() -> None:
    COLLECTION_DIR.mkdir(parents=True, exist_ok=True)

    # Write each prediction
    for p in PREDICTIONS:
        path = COLLECTION_DIR / f"{p.id}.md"
        path.write_text(render(p))

    print(f"Wrote {len(PREDICTIONS)} prediction files to {COLLECTION_DIR}")

    # Sanity checks
    seen_ids = set()
    for p in PREDICTIONS:
        if p.id in seen_ids:
            raise SystemExit(f"Duplicate prediction id: {p.id}")
        seen_ids.add(p.id)

    resolved = sum(1 for p in PREDICTIONS if p.status == "Resolved")
    print(f"  Total: {len(PREDICTIONS)}")
    print(f"  Resolved: {resolved}")
    print(f"  Pending: {len(PREDICTIONS) - resolved}")


if __name__ == "__main__":
    main()
