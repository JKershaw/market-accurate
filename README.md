# Market Accurate

Open-source financial analysis optimized for accuracy, not attention.

---

> **Status: Experimental (v0.1)**
>
> This project is unproven. Track record is empty. Methodology is untested at scale.
> The thesis may be wrong. Treat all analysis as one perspective among many, not as
> established fact or financial advice.

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

## Current Analysis

### [AI Valuation Analysis (January 2026)](analysis/ai-valuation-2026-01.md)

**Thesis:** AI infrastructure valuations embed assumptions about persistent compute scarcity that efficiency gains are actively eroding.

**Key findings:**
- Inference costs fell **280x** from Nov 2022 to Oct 2024
- Parameter efficiency improved **20x** (Llama 3 8B matches GPT-3 175B)
- Open-source closed **98%** of the frontier gap
- **$800B gap** between required AI revenue and projections
- **74%** of enterprises struggle to scale AI value

**Assessment:** 20-40% correction in AI infrastructure valuations likely within 18-36 months.

[Read full analysis →](analysis/ai-valuation-2026-01.md)

### [Hyperscaler Capex Tracker (January 2026)](analysis/hyperscaler-capex-2026-01.md)

**Focus:** Quarterly tracking of AI infrastructure spending by Microsoft, Google, Amazon, and Meta.

**Key metrics:**
- Combined 2025 capex: **$380-400B** (up ~60% YoY)
- 2026 projected: **~$600B** (up ~36% YoY)
- Q3 2025 record: **$106-113B** single quarter
- Capex intensity: **23.3%** of revenue (vs 13.9% historical median)

[Read full tracker →](analysis/hyperscaler-capex-2026-01.md)

### [Open-Source Benchmark Tracking (January 2026)](analysis/open-source-benchmarks-2026-01.md)

**Focus:** Tracking performance gap between proprietary and open-weights AI models.

**Key metrics:**
- MMLU gap to frontier: **-2.1 points** (open-source leads)
- Frontier capability lag: **12-18 months** and shrinking
- DeepSeek-R1 matched GPT-4 at **~5% of training cost**
- Consumer GPU viable: **8B-70B parameter** models

[Read full tracker →](analysis/open-source-benchmarks-2026-01.md)

### [Enterprise AI Adoption Metrics (January 2026)](analysis/enterprise-ai-adoption-2026-01.md)

**Focus:** Aggregating enterprise AI adoption surveys to track value realization.

**Key metrics:**
- Enterprise adoption rate: **88%**
- AI initiatives delivering expected ROI: **25%**
- Companies achieving measurable EBIT impact: **6%**
- AI projects that fail: **70-85%**

[Read full analysis →](analysis/enterprise-ai-adoption-2026-01.md)

---

## Track Record

| Predictions Made | Resolved | Correct | Accuracy |
|-----------------|----------|---------|----------|
| 21 | 0 | - | - |

[View detailed tracker →](predictions/tracker.md)

*Track record will populate as predictions resolve.*

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
├── analysis/
│   ├── ai-valuation-2026-01.md           # AI efficiency thesis
│   ├── hyperscaler-capex-2026-01.md      # Capex tracking
│   ├── semiconductor-cycle-2026-01.md    # Silicon cycle analysis
│   ├── open-source-benchmarks-2026-01.md # Open-source model tracking
│   └── enterprise-ai-adoption-2026-01.md # Enterprise adoption metrics
├── predictions/
│   └── tracker.md            # Prediction outcomes
├── docs/
│   ├── agent-infrastructure.md  # Agent system documentation
│   └── prediction-calendar.md   # Upcoming resolution dates
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
