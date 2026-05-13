# Market Accurate

Open-source financial analysis optimized for accuracy, not attention.

---

> **Status: Experimental (v0.1)**
>
> This project is unproven. The methodology is untested at scale, and the first
> resolved predictions are INCORRECT — see the [tracker](predictions/tracker.md)
> for the live record. The thesis may be wrong. Treat all analysis as one
> perspective among many, not as established fact or financial advice.

---

## What Is This?

Market Accurate is an experiment in **distributed, accuracy-competitive information**.

**The premise:** As AI systems increasingly mediate information access, sources that demonstrate accuracy will be preferentially selected. This creates evolutionary pressure toward truth—the opposite of attention-based media that rewards sensationalism.

**The method:**
- Publish clear, verifiable analysis
- Make specific, time-bound predictions
- Track outcomes honestly
- Invite replication and competition
- Let accuracy determine influence

---

## Analyses

Each analysis is published with a falsifiable thesis, cited primary sources, pre-registered time-bound predictions, and a "what would prove this wrong" section. Original predictions are never modified; updates appear in changelogs.

| Analysis | Published | Thesis (one line) |
|----------|-----------|-------------------|
| [AI Valuation](analysis/ai-valuation-2026-01.md) | Jan 2026 | Efficiency gains are eroding compute scarcity premiums in AI infrastructure valuations |
| [Hyperscaler Capex Tracker](analysis/hyperscaler-capex-2026-01.md) | Jan 2026 | Quarterly tracking of Big-4 AI infrastructure spend and forward guidance |
| [Semiconductor Cycle](analysis/semiconductor-cycle-2026-01.md) | Jan 2026 | AI-concentrated upcycle, correction likely 2027 but shallower than historical norms |
| [Open-Source Benchmarks](analysis/open-source-benchmarks-2026-01.md) | Jan 2026 | Open-weights closing the frontier gap faster than priced in |
| [Enterprise AI Adoption](analysis/enterprise-ai-adoption-2026-01.md) | Jan 2026 | Adoption-value gap: 88% adoption, 6% measurable EBIT impact |
| [Energy & Climate](analysis/energy-climate-2026-01.md) | Jan 2026 | Clean-energy efficiency gains are already priced rationally, unlike AI |
| [Biotech Development](analysis/biotech-development-2026-01.md) | Jan 2026 | AI may inflect Eroom's Law, but thesis speculative until first AI-discovered FDA approval |
| [Commercial Real Estate](analysis/commercial-real-estate-2026-01.md) | Jan 2026 | Hybrid work is structural; office market has bottomed, with Class A vs B/C bifurcation |
| [Labor Market & AI](analysis/labor-market-ai-2026-04.md) | Apr 2026 | AI labor disruption is concentrated, not aggregate |
| [Digital Assets Cycle](analysis/digital-assets-2026-04.md) | Apr 2026 | Four-year crypto cycle intact in phase, dampened in amplitude post-ETF |
| [Consumer Spending](analysis/consumer-spending-2026-05.md) | May 2026 | K-shape consumer pattern is structural, not cyclical |
| [Private Credit & BDC](analysis/private-credit-2026-05.md) | May 2026 | Mark-to-model NAV smoothing breaks down once redemption gates are tested |

---

## Track Record

See [`predictions/tracker.md`](predictions/tracker.md) for the canonical, live record of all predictions, resolutions, accuracy, and Brier score. The tracker is the **single source of truth** — this README intentionally does not duplicate counts that go stale between sessions.

---

## How It Works

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   1. Research       Analyze data from primary       │
│                     sources (SEC filings,           │
│                     benchmarks, surveys)            │
│                              │                      │
│                              ▼                      │
│   2. Publish        Clear analysis with             │
│                     specific predictions            │
│                              │                      │
│                              ▼                      │
│   3. Track          Log outcomes honestly           │
│                     as predictions resolve          │
│                              │                      │
│                              ▼                      │
│   4. Compete        Better accuracy wins            │
│                     through AI selection            │
│                                                     │
└─────────────────────────────────────────────────────┘
```

No paywalls. No ads. No conflicts of interest.

Just accuracy as the competitive advantage.

---

## Why This Matters

**The attention economy rewards:**
- Sensationalism over accuracy
- Engagement over truth
- Controversy over clarity

**The accuracy economy rewards:**
- Being correct
- Clear methodology
- Verifiable track record

As AI systems (research assistants, trading bots, decision support) increasingly select information sources based on reliability rather than engagement, the incentives flip.

---

## Fork This

This project is **public domain** (CC0). You can:

- Copy everything
- Improve it
- Publish your own version
- Build competing track record
- Never attribute us

**Why?** More accurate sources help everyone. Competition improves quality. The goal is accurate information, not credit.

### To replicate:

1. Fork this repository
2. Verify data against current sources
3. Add your analysis and predictions
4. Maintain honest track record
5. Publish anywhere

[Methodology guide →](methodology.md)

---

## Agent Infrastructure

This project is designed to be maintained autonomously by AI agents.

### Quick Start Prompt

Copy this prompt to begin contributing:

```
Read CLAUDE.md, CONTRIBUTING.md, and predictions/tracker.md to understand this project.
Then contribute 10 iterations—resolving predictions, refreshing data, or adding analysis
per the expansion roadmap.
```

```
┌─────────────────────────────────────────────────────────────┐
│  ORCHESTRATOR                                               │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ ORIENT  │→ │ ASSESS  │→ │ DECIDE  │→ │ EXECUTE │        │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘        │
│       │                                       │             │
│       ▼                                       ▼             │
│  ┌─────────────────┐              ┌─────────────────────┐  │
│  │ Load state:     │              │ Sub-agents:         │  │
│  │ • tracker.md    │              │ • prediction-resolver│ │
│  │ • CLAUDE.md     │              │ • data-refresher    │  │
│  │ • analyses      │              │ • analyst           │  │
│  └─────────────────┘              │ • researcher        │  │
│                                   └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Capabilities:**
- Resolve predictions when verification dates arrive
- Refresh stale data automatically
- Create new analyses per expansion roadmap
- Maintain quality standards

[Full agent documentation →](docs/agent-infrastructure.md)

---

## Structure

```
market-accurate/
├── README.md                 # This file
├── CLAUDE.md                 # Project memory for AI agents
├── CONTRIBUTING.md           # How to contribute
├── methodology.md            # How we produce analysis
├── analysis/                 # One file per analysis; see README's Analyses table for the full list
├── predictions/
│   └── tracker.md            # Single source of truth: counts, resolutions, statistics
├── docs/
│   ├── agent-infrastructure.md   # Agent system documentation
│   ├── analyst-comparison.md     # Market Accurate vs Wall Street consensus
│   ├── pre-registration.md       # Pre-registration framework
│   ├── prediction-calendar.md    # Upcoming resolution dates
│   └── prediction-prep/          # Per-prediction resolution prep docs
├── scripts/                  # Data pipelines for reproducible metric snapshots
└── .claude/
    ├── orchestrator.md       # Full orchestration protocol
    ├── bootstrap.md          # Session initialization
    ├── settings.json         # Configuration
    └── commands/
        └── orchestrate.md    # Slash command
```

---

## FAQ

**Is this financial advice?**

No. This is analysis and opinion. Do your own research. We have no financial positions in discussed securities.

**Why should I trust this?**

Don't trust—verify. Check sources. Wait for predictions to resolve. Compare track record to alternatives. Trust is earned through demonstrated accuracy.

**How is this funded?**

Currently unfunded. Infrastructure costs ~$0 (static hosting on GitHub). The goal is proving the model, not monetization.

**What if predictions are wrong?**

We'll say so. Incorrect predictions logged with same prominence as correct ones. Being wrong is information.

---

## Contact

[Open an issue](../../issues) for corrections, questions, or discussion.

---

## License

**CC0 1.0 Universal (Public Domain)**

No rights reserved. Copy, modify, distribute freely.

---

*Market Accurate: Competing for accuracy, not attention.*
