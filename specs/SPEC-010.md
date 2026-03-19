# SPEC-010: Alpha-Omega Phase Map

```
Document ID:      SPEC-010
Title:            Alpha-Omega Phase Map
Version:          1.0
Status:           RATIFIED
Layer:            L4B — Diagnosis & Meta-Evolution
Authoritative:    System Maturation Lifecycle
Parent Specs:     SPEC-000 (System Manifesto), SPEC-004 (Logical Specification), SPEC-008 (Evolution & Migration Law)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/SPEC-010/grounding.md
Risk Register:    post-flood/specs/SPEC-010/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. The Operational Rule

The question "what should we do next?" is the wrong question for a constitutional system. The right question is: **"what transition condition between the current phase and the next phase has not yet been satisfied?"**

This reformulation replaces open-ended planning with condition checking. System development is not a narrative ("first we design, then we build, then we test") but a state machine where progression is governed by explicit transition predicates. The Alpha-Omega Phase Map defines ten phases organized into five regimes, with explicit transition conditions at each boundary.

The architecture is a quad-motor composite model (Van de Ven & Poole 1995): the life-cycle motor provides the phase sequence, the teleological motor provides the transition conditions, the dialectical motor operates during repo fusion events, and the evolutionary motor operates through the promotion pipeline. Greiner's (1972) evolution-revolution model grounds the crisis-resolution pattern at each regime boundary.

**Risk profile: 60% GROUNDED, 40% ADAPTED.**

---

## 2. Five Regimes

### PHASE-001: Alpha (Conceptual Emergence)

**Greiner analogue:** Phase 1 (Creativity).
**Character:** Rapid, informal exploration driven by creative energy. Repos proliferate without governance links. Theory is generative but unformalised.
**Crisis:** Unformalised theory. The flood -- rapid repo creation outpaces governance capacity, producing 52 repos that must later be dissolved.
**Resolution:** Create the constitutional corpus. Formalise theory into specifications.

**Phases within Alpha:**

| Phase | Name | Activity |
|-------|------|----------|
| A1 | Seed | Initial creative impulse. First repos created. No governance structure. |
| A2 | Proliferation | Rapid expansion. Multiple organs emerge informally. Registry created but sparse. |

### PHASE-002: Beta (Formal Design)

**Greiner analogue:** Phase 2 (Direction).
**Character:** Centralised formal specification through the SPEC ladder. Constitutional corpus produced. Schemas defined. Governance rules codified.
**Crisis:** Unimplemented specification. The constitutional corpus is comprehensive but the engine, dashboard, MCP server, and ontologia do not yet exist.
**Resolution:** Begin building the governance infrastructure.

**Phases within Beta:**

| Phase | Name | Activity |
|-------|------|----------|
| B1 | Specification | SPEC-000 through SPEC-017 authored. Post-flood corpus extracted and organised. |
| B2 | Schema | JSON schemas defined. Registry format stabilised. seed.yaml contract established. |

### PHASE-003: Gamma (Embodiment)

**Greiner analogue:** Phase 3 (Delegation).
**Character:** Distributed implementation with organ-scoped autonomy. Engine, dashboard, MCP server, ontologia built. CLI established. Individual organs develop independently.
**Crisis:** Uncoordinated implementation. Cross-organ integration is weak. Soak tests, CI pipelines, and metric propagation are immature.
**Resolution:** Build cross-organ coordination infrastructure.

**Phases within Gamma:**

| Phase | Name | Activity |
|-------|------|----------|
| G1 | Core Engine | organvm-engine implemented: registry, governance, seed, metrics, dispatch, git. |
| G2 | Infrastructure | Dashboard, MCP server, ontologia, schema-definitions, alchemia implemented. |
| G3 | Integration | Cross-organ wiring: seed graph edges, CI pipelines, metric propagation, soak tests. |

### PHASE-004: Delta (Stabilisation)

**Greiner analogue:** Phase 4 (Coordination).
**Character:** Formal planning, cross-organ alignment, standard operating procedures. SOPs codified in praxis-perpetua. Ecosystem profiles declared. Governance instruments mature.
**Crisis:** Rigid governance (red tape). Governance overhead threatens creative throughput. The governance infrastructure that enabled Gamma stability constrains Delta productivity.
**Resolution:** Develop adaptive governance: meta-evolution protocol, self-modifying developmental grammar.

**Phases within Delta:**

| Phase | Name | Activity |
|-------|------|----------|
| D1 | Coordination | Cross-organ metric alignment. SOPs, session protocols, handoff procedures formalised. |
| D2 | Stabilisation | Sustained soak-test passage. Documentation completeness. Cross-organ validation passing. |

### PHASE-005: Omega (Completion / Evolution)

**Greiner analogue:** Phase 5 (Collaboration).
**Character:** Self-governing system. The system manages its own evolution with minimal human intervention for routine operations. Human role shifts from implementation to phase architecture.
**Crisis:** The system outgrows its creator's capacity to govern. The number of repos, agents, and governance operations exceeds what a single operator can review.
**Resolution:** The system governs itself. Meta-evolution (SPEC-011) enables governed self-modification.

**Phases within Omega:**

| Phase | Name | Activity |
|-------|------|----------|
| O1 | Maturity | 17/17 omega criteria met. All organs self-sustaining. Governance is automatic for routine operations. |
| O2 | Evolution | System enters meta-evolutionary mode. Era transitions are governed. New organs may emerge from formation activity. |

---

## 3. Transition Conditions

### PHASE-006: Regime Boundary Conditions

Transition conditions are not tasks to complete but predicates to satisfy. The distinction matters: a task ("write SPEC-003") has a completion state; a predicate ("all invariants have machine-checkable validators") must be continuously true.

| Boundary | Conditions | Assessment |
|----------|-----------|------------|
| Alpha -> Beta | (1) Constitutional corpus exists (2) Registry tracks all repos (3) Axioms declared | Manual: corpus review |
| Beta -> Gamma | (1) SPEC-000 through SPEC-008 ratified (2) JSON schemas defined (3) seed.yaml contract operational | Manual: spec review + schema validation |
| Gamma -> Delta | (1) Engine, dashboard, MCP server operational (2) CI pipelines across 3+ organs (3) Soak test infrastructure running (4) Cross-organ metric propagation functional | Auto + Manual: CI health, soak-test status, metric freshness |
| Delta -> Omega | (1) 17/17 omega criteria met (2) All invariant validators implemented (3) Meta-evolution protocol operational (4) System sustains COHERENT gestalt for 90+ days | Auto: omega scorecard + gestalt trajectory |

### PHASE-007: The Omega Scorecard

The 17-criterion binary scorecard is the most fully specified transition condition set. Each criterion is a predicate, not a deliverable:

| # | Criterion | Assessment Mode | Current Status |
|---|-----------|----------------|---------------|
| 1 | Soak-test day count >= 30 | Auto | Evaluating |
| 2 | All invariant validators implemented | Manual | NOT MET |
| 3 | CI health above threshold system-wide | Auto | Evaluating |
| 4 | Test coverage above threshold per organ | Manual | NOT MET |
| 5 | Cross-organ dependency validation passing | Manual | MET |
| 6 | Seed.yaml coverage >= 95% | Manual | MET |
| 7 | Documentation completeness per flagship | Manual | NOT MET |
| 8 | Registry-v2.json fully validated | Manual | MET |
| 9 | Dashboard operational with all routes | Auto | Evaluating |
| 10 | MCP server operational with all tools | Manual | NOT MET |
| 11 | Ontologia bootstrapped with all entities | Manual | NOT MET |
| 12 | Schema definitions covering all data contracts | Manual | NOT MET |
| 13 | Governance rules complete and consistent | Manual | MET |
| 14 | Ecosystem profiles declared per product | Manual | NOT MET |
| 15 | SOPs covering all critical processes | Manual | NOT MET |
| 16 | Cross-organ event subscriptions operational | Manual | NOT MET |
| 17 | System sustains stable health for 30+ days | Auto | Evaluating |

The scorecard does not measure effort or progress; it measures readiness. A system that has done enormous work but fails one criterion has not satisfied the transition condition.

---

## 4. Phase-Driven Orchestration

### PHASE-008: Current Phase Diagnosis

ORGANVM's current position is diagnosable as **late Gamma (G3) / early Delta (D1)**:

- Alpha: COMPLETE. Constitutional corpus exists. Registry tracks 112+ repos.
- Beta boundary condition (SPEC-000 through SPEC-008 ratified) SATISFIED. Additionally, SPEC-009 through SPEC-017 and all INST-* documents ratified on 2026-03-19, exceeding original condition. Schemas defined. seed.yaml operational.
- Gamma: MOSTLY COMPLETE. Engine, dashboard, MCP server, ontologia operational. CI pipelines across multiple organs. Soak tests running. Cross-organ metric propagation functional but immature.
- Delta: BEGINNING. SOPs being codified (praxis-perpetua). Ecosystem profiles being declared. Cross-organ alignment in progress.

The crisis of uncoordinated implementation (Gamma -> Delta boundary) is partially resolved but not fully. This diagnosis drives the governance priority: coordination, standardisation, and sustained stability.

### PHASE-009: Phase-Appropriate Actions

Each phase constrains what kinds of work are appropriate. Working on Omega-phase concerns during Gamma is premature; working on Alpha-phase concerns during Delta is regressive.

| Current Phase | Appropriate Work | Inappropriate Work |
|--------------|-----------------|-------------------|
| Gamma (G3) | Cross-organ integration, CI pipeline completion, soak-test monitoring | New organ creation, meta-evolution protocol, era transitions |
| Delta (D1) | SOP codification, ecosystem profiling, metric alignment, documentation | Rapid repo proliferation, architectural redesign, topology changes |
| Delta (D2) | Sustained stability demonstration, documentation completion, governance hardening | New feature development, repo creation, dependency restructuring |
| Omega (O1) | Omega scorecard criteria satisfaction, governance automation | Manual workarounds for automated governance |

### PHASE-010: Solutions-Become-Problems

Per Greiner (1972), each phase's management solution becomes the next phase's management crisis. This pattern is structural, not avoidable:

| Phase | Solution | Subsequent Problem |
|-------|----------|-------------------|
| Alpha | Creative proliferation | Ungovernability (the flood) |
| Beta | Formal specification | Specification without implementation |
| Gamma | Delegated implementation | Uncoordinated cross-organ integration |
| Delta | Standardisation and coordination | Governance rigidity constraining creativity |
| Omega | Self-governance | System complexity exceeding operator comprehension |

Recognising the pattern prevents misdiagnosis: Delta's governance overhead is not a bug but the structural consequence of Gamma's delegation. The response is not to reduce governance (which would regress to Gamma's crisis) but to evolve governance toward self-modification (SPEC-011).

---

## 5. Implementation Status

| Component | Status | Location |
|-----------|--------|----------|
| Omega scorecard (17 criteria) | ALIGNED | `organvm-engine/src/organvm_engine/omega/scorecard.py` |
| Omega CLI | ALIGNED | `organvm omega status`, `organvm omega detail` |
| Omega MCP tool | ALIGNED | `organvm_omega_status` |
| Phase diagnosis | MANUAL | Based on scorecard + regime boundary analysis |
| Phase-appropriate action enforcement | MISSING | Conceptual; no automated enforcement |
| Regime transition detection | MISSING | Target: regime boundary predicate evaluation |

---

## 6. Evolution Constraints

SPEC-010 may be amended through the governed process defined in SPEC-000 Section 9. New phases may be added within existing regimes (constrained extension). Regime boundaries may be refined (additional conditions added). Regime sequence may not be reordered -- the developmental logic (conception -> design -> embodiment -> stabilisation -> maturity) is constitutive. The operational rule (condition checking, not open-ended planning) is constitutive and may not be weakened.

---

## 7. Traceability

```
SPEC-000 AX-000-005 (Evolutionary Recursivity) → PHASE-005 (Omega enables self-modifying evolution)
SPEC-000 AX-000-006 (Topological Plasticity) → PHASE-005/O2 (era transitions may mutate topology)
SPEC-004 (Logical Specification) → PHASE-006 (transition conditions as state machine predicates)
SPEC-008 (Evolution & Migration Law) → PHASE-006 (regime transitions follow governed change modes)
SPEC-011 (Meta-Evolution Architecture) → PHASE-005 (Omega requires operational meta-evolution)
INST-HEARTBEAT → PHASE-006/008 (gestalt trajectory informs phase diagnosis)
INST-ERA → PHASE-001 through PHASE-005 (eras and phases are complementary temporal models)
```

Full grounding narrative: `post-flood/specs/SPEC-010/grounding.md` (3,040 words)
Full risk register: `post-flood/specs/SPEC-010/risk-register.md` (5 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
