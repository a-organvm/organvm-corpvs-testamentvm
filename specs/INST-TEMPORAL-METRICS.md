# INST-TEMPORAL-METRICS: Temporal Metrics

```
Document ID:      INST-TEMPORAL-METRICS
Title:            Temporal Metrics
Version:          1.0
Status:           RATIFIED
Layer:            L4A — Sensing & Observation
Authoritative:    Observation-Based Metric Architecture
Parent Specs:     SPEC-000 (System Manifesto), SPEC-003 (Invariant Register)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/temporal-metrics/grounding.md
Risk Register:    post-flood/specs/temporal-metrics/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. Purpose

A metric observed once is a number. A metric observed repeatedly over time is a signal. ORGANVM's constitutional governance requires signals, not numbers: not merely "what is the test coverage now?" but "what is the test coverage trajectory, and what feedback dynamics produce it?"

The temporal metrics architecture records, classifies, and interprets metrics using the formalism of system dynamics. Forrester's (1961) stocks-and-flows framework provides the modeling primitives. Sterman's (2000) reference modes provide the diagnostic vocabulary for classifying trends. Meadows' (2008) leverage point hierarchy structures the intervention strategy.

AX-000-002 (Organizational Closure) requires that constitutive processes -- including metric observation -- be specified within the system. INV-000-005 (Observability) mandates that the system accurately report its own state. The temporal metrics architecture is the mechanism that satisfies both: it defines how the system observes itself and how those observations are stored, aggregated, and interpreted.

**Risk profile: 80% GROUNDED, 20% ADAPTED.**

---

## 2. Metric Types

### MET-001: Stocks (Gauges)

A stock is an accumulation -- the state of the system at a point in time. Stocks persist between observations and have meaning independent of when they are observed.

| Stock Metric | Description | Observation Cadence |
|-------------|-------------|-------------------|
| `repos_with_tests` | Count of repos with at least one test file | Per CI run |
| `repos_with_ci` | Count of repos with CI workflow | Per governance audit |
| `promotion_state_distribution` | Count of repos per promotion state | Per promotion event |
| `seed_coverage` | Fraction of repos with seed.yaml | Per seed discovery |
| `omega_criteria_met` | Count of satisfied omega criteria | Per organism snapshot |
| `entity_count` | Total entities in ontologia | Per entity creation |

Gauges are recorded as point-in-time values. The latest observation is the current value. Historical observations enable trend analysis.

### MET-002: Flows (Counters)

A flow is a rate -- change over a time interval. Flows have meaning only over their observation interval, not at a single point.

| Flow Metric | Description | Observation Interval |
|------------|-------------|---------------------|
| `tests_added` | Number of tests added in the interval | Per sprint |
| `promotions_completed` | Number of promotions in the interval | Per sprint |
| `events_emitted` | Number of events on the spine in the interval | Per heartbeat |
| `ci_runs_completed` | Number of CI runs in the interval | Per day |
| `governance_audits_run` | Number of governance audits in the interval | Per sprint |

Counters are recorded as interval sums. Summing across intervals yields cumulative totals. Dividing by interval length yields rates.

### MET-003: Rates (Deltas)

A delta is the rate of change of a stock -- the derivative. Deltas detect acceleration and deceleration in system dynamics.

| Delta Metric | Derived From | Significance |
|-------------|-------------|-------------|
| `test_growth_rate` | d(repos_with_tests)/dt | Positive = improving coverage; negative = regression |
| `promotion_velocity` | d(graduated_count)/dt | Rate of maturation across the system |
| `entity_creation_rate` | d(entity_count)/dt | Rate of ontological expansion |
| `ci_health_trend` | d(repos_with_ci)/dt | Direction of CI infrastructure adoption |

Deltas are computed from consecutive stock observations: `delta = (stock_t2 - stock_t1) / (t2 - t1)`.

---

## 3. Feedback Classification

### MET-004: Balancing Loops

Balancing loops are goal-seeking: they resist change and push the system toward a target. Metrics participating in balancing loops converge toward equilibrium.

| Loop | Mechanism | Governance Implication |
|------|-----------|----------------------|
| Promotion pipeline | Quality gates constrain promotion rate; repos that fail criteria remain at current state | Tune gate criteria to achieve desired promotion velocity |
| Soak test | 30-day stability window prevents premature promotion | Adjust window length based on false-positive/false-negative rates |
| Dependency validation | DAG check prevents structural degradation | Binary: either acyclic or violated; no tuning |

### MET-005: Reinforcing Loops

Reinforcing loops are amplifying: they accelerate change in whatever direction the system is already moving. Unchecked reinforcing loops produce exponential growth or collapse.

| Loop | Mechanism | Governance Implication |
|------|-----------|----------------------|
| Seed graph density | More inter-repo edges create more integration pressure, which creates more edges | Monitor edge density for runaway amplification |
| Flagship attention | Flagship repos receive more attention, improving their metrics, attracting more attention | Detect success-to-the-successful archetype; redistribute attention |
| Documentation debt | Undocumented repos are harder to work on, producing less documentation | Detect eroding-goals archetype; intervene early |

### MET-006: Loop Dominance

System behavior is determined by which loops dominate at any given time. The promotion pipeline during PROPULSIO MAXIMA was a reinforcing loop (each promotion enabled the next); post-sprint, governance gates (balancing loops) dominate, slowing the rate.

Detecting loop dominance shifts is a diagnostic priority: when a metric's reference mode changes from exponential to S-shaped, a reinforcing-to-balancing transition has occurred.

---

## 4. Reference Modes

### MET-007: Expected Reference Modes

Each metric carries an expected reference mode -- the qualitative time-series pattern expected under healthy system dynamics (Sterman 2000):

| Reference Mode | Pattern | Example |
|---------------|---------|---------|
| **Monotonic growth** | Steady increase, no regression | `repos_with_ci` (CI adoption should never decrease) |
| **S-shaped growth** | Rapid initial growth, then plateau | `promotions_completed` (rapid sprint, then governance-constrained tail) |
| **Oscillation** | Periodic fluctuation around a mean | `ci_runs_completed` (weekly cadence) |
| **Goal-seeking** | Convergence toward a target | `omega_criteria_met` (converging toward 17/17) |
| **Overshoot-and-collapse** | Rapid growth beyond carrying capacity, then crash | (pathological -- should not occur in healthy system) |

### MET-008: Reference Mode Deviation

When an observed trajectory deviates from its expected reference mode, the deviation is a diagnostic signal:

| Expected | Observed | Diagnosis |
|----------|----------|-----------|
| Monotonic growth | Plateau | Balancing loop has become dominant; investigate constraint |
| Monotonic growth | Oscillation | Delay-induced instability; shorten feedback loop |
| S-shaped growth | Overshoot | Reinforcing loop exceeded carrying capacity; reduce growth rate |
| Goal-seeking | Divergence | Target may be miscalibrated; reassess constitutional goal |
| Any | Collapse | Structural failure; emergency diagnostic via SPEC-009 |

Reference mode deviations at paradigm-level metrics (Meadows level 3+) trigger escalation per SPEC-015.

---

## 5. Rollup Rules

### MET-009: Organ-Level Aggregation

Repo-level observations are aggregated at organ level using declared aggregation functions. The function is part of the metric definition, not chosen at query time.

| Aggregation Type | Function | Applicable To |
|-----------------|----------|---------------|
| **Central tendency** | Mean, median | Numeric gauges (test count, CI health %) |
| **Coverage** | Count-true / count-total | Boolean properties (has_ci, has_seed) |
| **Distribution** | Frequency histogram | Enum properties (promotion_state) |
| **Extremes** | Min, max | Identifies outliers requiring attention |

Stock metrics are aggregated by current-value statistics. Flow metrics are aggregated by interval-sum statistics. The distinction is structural, not optional.

### MET-010: System-Level Composition

Organ-level aggregates are composed into system-level indicators. Composition may be:

- **Simple:** Mean of organ means (unweighted cross-organ comparison)
- **Weighted by repo count:** Organs with more repos contribute proportionally more
- **Weighted by tier:** Flagship repos contribute more than infrastructure repos
- **Weighted by promotion state:** GRADUATED repos contribute more than LOCAL repos

The composition function is declared per metric and must be consistent with the metric's governance purpose.

### MET-011: Trend Classification

Trend classification operates on the time-series of a metric's observations:

| Classification | Definition | Threshold |
|---------------|-----------|-----------|
| **Improving** | Positive slope, within expected reference mode | slope > 0, p < 0.05 |
| **Stable** | Near-zero slope, within expected range | |slope| < epsilon |
| **Declining** | Negative slope, deviating from expected mode | slope < 0, p < 0.05 |
| **Volatile** | High variance, no clear trend | CV > threshold |

Trend classifications feed into the heartbeat's gestalt computation (INST-HEARTBEAT).

---

## 6. Leverage Level Annotation

### MET-012: Meadows Hierarchy Mapping

Each metric carries a leverage-level annotation (Meadows 2008) indicating its position in the intervention hierarchy:

| Level | Category | Example | Governance Response |
|-------|----------|---------|-------------------|
| 12-10 | **Parameter** | Soak-test duration, staleness threshold | Tune; low systemic impact |
| 9-7 | **Structure** | Promotion gate criteria, dependency rules | Redesign; moderate systemic impact |
| 6-4 | **Information** | What metrics are visible, to whom, when | Restructure feedback; high systemic impact |
| 3-1 | **Paradigm** | Eight-organ model, constitutional axioms | Constitutional revision; system-defining impact |

Alerts on paradigm-level metrics (omega scorecard, constitutional coverage) carry higher urgency than alerts on parameter-level metrics (individual repo CI status).

---

## 7. Implementation Status

| Component | Status | Location |
|-----------|--------|----------|
| Observation store (timeseries.py) | ALIGNED | `organvm-engine/src/organvm_engine/metrics/timeseries.py` |
| Gauge/counter/delta classification | ALIGNED | Observation records carry type field |
| Organ-level aggregation | PARTIAL | `metrics/variables.py` performs resolution but aggregation functions are implicit |
| Reference mode classification | MISSING | Target: `organvm-engine/src/organvm_engine/metrics/trends.py` |
| Feedback loop classification metadata | MISSING | Target: metric definition schema extension |
| Leverage level annotations | MISSING | Target: metric definition schema extension |
| Trend classification | MISSING | Target: `organvm-engine/src/organvm_engine/metrics/trends.py` |

---

## 8. Failure Modes

| Failure | Violated Element | Detection |
|---------|-----------------|-----------|
| Stale observation (metric not refreshed within cadence) | MET-001/002, INV-000-005 | Freshness check: `last_observed > now - cadence` |
| Wrong aggregation function (flow aggregated as stock) | MET-009 | Schema validation: declared type matches aggregation |
| Reference mode misclassification | MET-007 | Periodic review: actual trajectory vs. expected mode |
| Missing leverage annotation | MET-012 | Schema completeness check |
| Loop dominance shift undetected | MET-006 | Automated trend-break detection |

---

## 9. Evolution Constraints

INST-TEMPORAL-METRICS may be amended through the governed process defined in SPEC-000 Section 9. New metric types may be added (constrained extension). Existing metric types may not be removed -- deprecated metrics remain in historical record. The stock/flow/delta classification is constitutive and may not be weakened.

---

## 10. Traceability

```
SPEC-000 AX-000-002 (Organizational Closure) → MET-001/002/003 (metric observation is a constitutive process)
SPEC-000 INV-000-005 (Observability) → MET-009/010 (rollup rules enable accurate state reporting)
SPEC-003 (Invariant Register) → MET-008 (reference mode deviations may signal invariant violations)
INST-EVENT-SPINE → MET-001/002 (observations are recorded as events on the spine)
INST-HEARTBEAT → MET-011 (trend classifications feed gestalt computation)
INST-VARIABLE-RESOLUTION → MET-009/010 (rollup rules implement scope cascade)
```

Full grounding narrative: `post-flood/specs/temporal-metrics/grounding.md` (3,073 words)
Full risk register: `post-flood/specs/temporal-metrics/risk-register.md` (5 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
