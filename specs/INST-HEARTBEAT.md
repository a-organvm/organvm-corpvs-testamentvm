# INST-HEARTBEAT: Cadences and Affective State

```
Document ID:      INST-HEARTBEAT
Title:            Cadences and Affective State
Version:          1.0
Status:           RATIFIED
Layer:            L4A — Sensing & Observation
Authoritative:    System Vitality Sensing and Gestalt Computation
Parent Specs:     SPEC-000 (System Manifesto)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/heartbeat-affect/grounding.md
Risk Register:    post-flood/specs/heartbeat-affect/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. Purpose

Individual metrics tell you about individual components. No single metric -- not test coverage, not CI status, not promotion state -- captures the system's position on the order-chaos spectrum. The heartbeat and affect architecture provides the integrative assessment: a periodic sensing mechanism that detects systemic drift toward rigidity or chaos (Kauffman 1993), combined with an affective signal layer that compresses high-dimensional metric state into actionable governance signals (Damasio 1999).

The heartbeat answers: "where is the system on the order-chaos spectrum?" Affect answers: "how should this position feel to the operator?" Together they ground the SystemOrganism's compressed density representation and its consumer projections.

AX-000-002 (Organizational Closure) requires that the system's self-sensing be a constitutive process. INV-000-005 (Observability) mandates accurate self-reporting. The heartbeat is the mechanism that produces the observations; affect is the mechanism that renders them into governance-actionable form.

**Risk profile: 20% GROUNDED, 80% ADAPTED.**

### Phenomenological Constraint

The affect is in the operator, not the system. ORGANVM does not feel. It computes signals designed to produce appropriate feelings in the human operator. The system provides the stimulus; the operator provides the experience. This distinction is constitutive: any specification or implementation that attributes phenomenal experience to the system violates this constraint.

---

## 2. Cadences

### BEAT-001: Fast Cadence (Per-Session)

The fast cadence fires on every agent session start and completion. It captures the most volatile system properties -- those that change within the timescale of a single work session.

| Reading | Source | Purpose |
|---------|--------|---------|
| Session context freshness | CLAUDE.md modification date | Is the agent working with stale context? |
| Active claims | Claims registry (coordination/claims.py) | How many agents are currently operating? |
| Last CI status | CI workflow results | Has anything broken since the last session? |
| Organism density text | SystemOrganism snapshot | Quick gestalt for session planning |

**Trigger:** `conductor_session_start` or `organvm session` invocation.
**Consumer:** Agent session context, operator session planning.
**Event:** `organism.heartbeat` with `cadence: fast`.

### BEAT-002: Medium Cadence (Per-Day)

The medium cadence fires once per calendar day. It captures properties that change at the daily timescale -- CI run results, metric freshness, promotion pipeline movement.

| Reading | Source | Purpose |
|---------|--------|---------|
| CI health across all organs | CI workflow aggregation | Catch regressions before they compound |
| Metric freshness audit | Timestamp comparison per metric | Flag stale metrics before they become governance blind spots |
| Promotion pipeline velocity | Count of promotions in last 24h | Detect blockage or acceleration |
| Consumer lag | Event spine cursor positions | Detect read models falling behind |
| Dependency graph mutations | Edge diff since last heartbeat | Detect structural changes requiring review |

**Trigger:** Scheduled (cron or LaunchAgent) or manual `organvm organism`.
**Consumer:** Dashboard daily view, operator morning review.
**Event:** `organism.heartbeat` with `cadence: medium`.

### BEAT-003: Slow Cadence (Per-Sprint)

The slow cadence fires at sprint boundaries (configurable, default: 2 weeks). It captures properties that change at the strategic timescale -- trend analysis, reference mode classification, omega progress, structural interrogation results.

| Reading | Source | Purpose |
|---------|--------|---------|
| Trend classification per metric | Temporal metrics timeseries analysis | Detect trajectory changes requiring governance response |
| Reference mode deviation | Observed vs. expected reference modes | Flag structural instability |
| Omega scorecard snapshot | omega/scorecard.py evaluation | Track maturation progress |
| Graph index computation | CCI, DDI, FVI, CRI, ECI (INST-GRAPH-INDICES) | Structural health assessment |
| Cross-organ coherence | Assortative mixing analysis | Detect evolutionary divergence between organs |
| Consistent snapshot | Event spine snapshot | Archival-quality system state record |

**Trigger:** Sprint boundary or manual `organvm organism snapshot --write`.
**Consumer:** Governance review, strategic planning, omega tracking.
**Event:** `organism.heartbeat` with `cadence: slow`.

---

## 3. Vital Parameters

### BEAT-004: Vital Parameter Classes

The heartbeat reads vital parameters across four diagnostic dimensions:

| Dimension | Parameters | Healthy Range | Frozen Signal | Chaotic Signal |
|-----------|-----------|---------------|---------------|----------------|
| **Metric freshness** | Last observation timestamp per metric | Within cadence window | All metrics stale (system not observing itself) | Metric values oscillating wildly |
| **Governance compliance** | Fraction of repos satisfying current promotion criteria | > 70% | 100% (all repos identical, no diversity) | < 30% (governance disconnected from reality) |
| **Structural health** | Dependency DAG validity, seed coverage, edge density | DAG valid, seed > 90%, density in target range | Minimal edges (isolated repos) | Dense edges (excessive coupling) |
| **Activity signals** | Commit recency, CI run frequency, session count | Regular activity across organs | No activity (system dormant) | Activity concentrated in one organ (imbalanced) |

### BEAT-005: Edge-of-Chaos Detection

The heartbeat detects drift toward rigidity (frozen regime) or chaos using Kauffman's (1993) qualitative framework:

**Frozen regime signals:**
- Decreasing variety (fewer distinct promotion states in active use)
- Fewer active organs (activity concentrating in subset)
- More uniform metric values (all repos converging to identical profiles)
- No structural changes (no new repos, edges, or formations)

**Chaotic regime signals:**
- Increasing unlinked components (repos without seed.yaml, orphaned entities)
- Invariant violations accumulating (dependency cycles, governance gaps)
- Metric volatility exceeding reference mode expectations
- Agent operations without session scoping (uncoordinated changes)

**Target regime:** Intermediate -- enough governance order for constitutional coherence, enough organ autonomy for creative adaptability. The precise target connectivity is empirically determined, not derived from Kauffman's NK model K ~ 2 parameter.

---

## 4. Derived Gestalt

### BEAT-006: Gestalt States

The heartbeat compresses vital parameter readings into a four-state gestalt that provides the operator's affective signal:

| Gestalt | Definition | Vital Parameter Profile |
|---------|-----------|------------------------|
| **THRIVING** | All dimensions healthy; system in target regime; positive trends | Freshness: all current. Compliance: > 80%. Structure: DAG valid, seed > 95%. Activity: balanced across organs. Trends: improving or stable. |
| **COHERENT** | Most dimensions healthy; minor concerns; stable or improving | Freshness: mostly current. Compliance: 60-80%. Structure: DAG valid, seed > 80%. Activity: some imbalance. Trends: stable, no declining. |
| **STRAINED** | One or more dimensions degraded; declining trends; intervention needed | Freshness: some stale. Compliance: 40-60%. Structure: DAG valid but edge density outside range. Activity: concentrated. Trends: one or more declining. |
| **BRITTLE** | Multiple dimensions degraded; structural risk; urgent intervention | Freshness: multiple stale. Compliance: < 40%. Structure: invariant violations detected. Activity: sparse or chaotic. Trends: multiple declining or collapsing. |

### BEAT-007: Gestalt Computation

The gestalt is computed as the minimum health level across all four vital parameter dimensions. A single BRITTLE dimension forces the overall gestalt to BRITTLE, regardless of other dimensions. This conservative rule prevents masking: a system that is thriving on three dimensions but brittle on one is brittle, not thriving.

```
gestalt = min(
  freshness_health,
  compliance_health,
  structural_health,
  activity_health
)
```

Each dimension maps to a health level based on the thresholds defined in BEAT-004.

### BEAT-008: Gestalt Trajectory

The gestalt is not only a point-in-time assessment but a trajectory. The heartbeat records gestalt state at each cadence, enabling trend analysis:

| Trajectory | Pattern | Governance Implication |
|-----------|---------|----------------------|
| Improving | STRAINED -> COHERENT -> THRIVING | Interventions are working; maintain course |
| Stable | Same state across multiple heartbeats | System in equilibrium; watch for plateau |
| Declining | COHERENT -> STRAINED | Drift detected; investigate before reaching BRITTLE |
| Oscillating | Alternating between states | Feedback loop instability; adjust cadence or thresholds |

---

## 5. Somatic Marker Function

### BEAT-009: Attention Biasing

The attention-direction function (Damasio 1999, functional analogue) compresses heartbeat readings into governance-actionable signals that bias the operator's attention. The compression operates through three mechanisms:

**Traffic-light classification:** Each vital parameter is classified as green (within expected range), yellow (approaching threshold), or red (threshold exceeded or trend deteriorating). This reduces 112+ repo metrics to a small number of attention signals.

**Density compression:** The full metric state is rendered as the SystemOrganism's density text -- a single line summarizing organ count, repo count, module count, omega progress, and CI health. Example: `"8o/113r/58m, 4/17 omega met, 62% CI green — COHERENT"`. This is the affective signal: not raw data but a pre-processed, attention-directing summary.

**Priority surfacing:** Organs and repos with red or yellow signals are surfaced first in dashboard views and MCP queries. The operator's limited attention is directed to the highest-priority concerns before encountering healthy components.

### BEAT-010: Background Feeling Production

The heartbeat produces the system equivalent of Damasio's background feelings: a continuous, low-level sense of system health that colors all governance decisions. This is not a single dramatic alert but an ongoing perception assembled from periodic heartbeat readings, dashboard checks, organism snapshots, and MCP queries.

The background feeling is healthy when the operator does not notice it. If the system is THRIVING, the density text confirms expectations without demanding attention. The feeling becomes salient when something is wrong -- when the gestalt shifts to STRAINED or BRITTLE, the operator notices because the background signal has changed.

---

## 6. Implementation Status

| Component | Status | Location |
|-----------|--------|----------|
| SystemOrganism snapshot | ALIGNED | `organvm-engine/src/organvm_engine/metrics/organism.py` |
| Compressed density text | ALIGNED | `SystemOrganism.compressed_text()` |
| Gate evaluation (partial vital parameters) | ALIGNED | `metrics/gates.py` |
| Gestalt computation | MISSING | Target: `metrics/organism.py` extension |
| Cadence scheduling | MISSING | Target: cron/LaunchAgent + CLI flag |
| Edge-of-chaos detection | MISSING | Target: `metrics/vitality.py` |
| Traffic-light classification | PARTIAL | Dashboard uses color coding; not formalized as classification |
| Gestalt trajectory tracking | MISSING | Target: timeseries observation of gestalt state |

---

## 7. Failure Modes

| Failure | Violated Element | Detection |
|---------|-----------------|-----------|
| Heartbeat cadence missed (no observation at expected time) | BEAT-001/002/003 | Timestamp gap detection in heartbeat timeseries |
| Gestalt masking (healthy aggregate hiding sick dimension) | BEAT-007 | Min-function prevents this structurally |
| Somatic marker fatigue (operator ignoring persistent yellow/red) | BEAT-009 | Alert escalation: persistent yellow upgrades to red after threshold |
| Edge-of-chaos drift undetected | BEAT-005 | Slow-cadence structural review catches drift over sprint timescale |
| Affect misattribution (system claims phenomenal experience) | Section 1 constraint | Code review: no anthropomorphic language in system output |

---

## 8. Evolution Constraints

INST-HEARTBEAT may be amended through the governed process defined in SPEC-000 Section 9. Cadence definitions may be refined (adjusted timing, added readings). New cadences may be added between existing ones. The four-state gestalt taxonomy may be extended but existing states may not be removed. The phenomenological constraint (Section 1) is constitutive and may not be weakened.

---

## 9. Traceability

```
SPEC-000 AX-000-002 (Organizational Closure) → BEAT-001/002/003 (heartbeat is a constitutive sensing process)
SPEC-000 INV-000-005 (Observability) → BEAT-004 (vital parameters enable accurate self-reporting)
INST-EVENT-SPINE → BEAT-001/002/003 (heartbeat readings recorded as events)
INST-TEMPORAL-METRICS → BEAT-004 (vital parameters are temporal metrics with reference modes)
INST-VARIABLE-RESOLUTION → BEAT-006 (gestalt consumes GLOBAL-scope variables)
SPEC-009 (Structural Interrogation) → BEAT-005 (edge-of-chaos detection feeds diagnostic inquiry)
SPEC-015 (Escalation & Attention Policy) → BEAT-009 (somatic markers trigger escalation)
```

Full grounding narrative: `post-flood/specs/heartbeat-affect/grounding.md` (2,968 words)
Full risk register: `post-flood/specs/heartbeat-affect/risk-register.md` (5 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
