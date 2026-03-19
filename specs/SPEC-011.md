# SPEC-011: Meta-Evolution Architecture

```
Document ID:      SPEC-011
Title:            Meta-Evolution Architecture
Version:          1.0
Status:           RATIFIED
Layer:            L4B — Diagnosis & Meta-Evolution
Authoritative:    Self-Modifying Governance and Evolutionary Strata
Parent Specs:     SPEC-000 (System Manifesto), SPEC-003 (Invariant Register), SPEC-008 (Evolution & Migration Law)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/SPEC-011/grounding.md
Risk Register:    post-flood/specs/SPEC-011/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. The Meta-Evolution Problem

A system that cannot change its own rules is eventually governed by rules that no longer fit its reality. A system that can change its own rules without constraint is eventually governed by no rules at all. The meta-evolution problem is navigating between these two failure modes: enabling self-modification while preventing self-destruction.

ORGANVM's constitutional corpus defines the system through axioms, ontological categories, primitive types, invariants, behavioral rules, and architectural constraints. But the corpus itself must evolve as the system matures. The meta-evolution architecture formalises how this self-modification occurs: through which mechanisms, under which constraints, with which safety guarantees.

The architecture draws on Hofstadter's (1979) strange loops and Godel's incompleteness theorems for the structural model of self-referential governance, and von Foerster's (1981) second-order cybernetics for the identity-persistence formalism (eigenforms) and the safety constraint (ethical imperative).

**Risk profile: 60% GROUNDED, 40% ADAPTED.**

---

## 2. Four Evolutionary Strata

### META-001: Stratum 1 — State Evolution

**Scope:** Individual entity state changes within existing rules.
**Examples:** Promoting a repo from CANDIDATE to PUBLIC_PROCESS. Recording a new metric observation. Updating a registry field.
**Governing rules:** SPEC-004 (Logical Specification), SPEC-005 (Rulebook), governance-rules.json.
**Constraint:** All state transitions must satisfy the preconditions defined in the state machine and the invariants defined in SPEC-003.

State evolution is the most frequent and least impactful stratum. It operates entirely within the current constitutional framework. No rule changes; only state changes.

### META-002: Stratum 2 — Structural Evolution

**Scope:** Structural changes to the system's architecture within existing categories.
**Examples:** Adding a new repo to an existing organ. Modifying the dependency graph. Adding a new cross-organ signal edge. Creating a new entity in ontologia.
**Governing rules:** SPEC-006 (Architecture Document), SPEC-007 (Interface Contract Spec), SPEC-012 (Repo Fusion Protocol).
**Constraint:** Structural changes must preserve all invariants (SPEC-003) and respect the architectural constraints defined in SPEC-006.

Structural evolution modifies what exists without changing the categories of existence. A new repo is created as an instance of the existing entity classification. A new dependency edge is typed using existing edge types.

### META-003: Stratum 3 — Ontological Evolution

**Scope:** Changes to the categories, types, and classifications themselves.
**Examples:** Introducing a new entity type (beyond ORGAN, REPO, MODULE). Redefining an organ's functional domain. Adding a new relation type to the seed graph. Extending the promotion state machine with a new state.
**Governing rules:** SPEC-001 (Ontology Charter), SPEC-002 (Primitive Register), SPEC-008 (Evolution & Migration Law).
**Constraint:** Category changes must be compatible with the primitive composition framework (SPEC-002): new types must decompose into the seven primitives. Category changes must be governed by SPEC-008's change modes (conservative, constrained, breaking).

Ontological evolution is rare and high-impact. It modifies the conceptual vocabulary the system uses to describe itself. A new entity type changes what the system recognises as existing.

### META-004: Stratum 4 — Meta-Evolution

**Scope:** Changes to the evolutionary rules themselves -- the rules that govern how rules change.
**Examples:** Modifying the transition conditions in the state machine. Adding new invariants to SPEC-003. Revising axioms in SPEC-000. Changing the SPEC amendment process. Adding new strata to the meta-evolution hierarchy.
**Governing rules:** SPEC-000 Section 9 (Evolution Constraints), this specification (SPEC-011).
**Constraint:** Meta-evolutionary changes must preserve the system's eigenform (invariant set) and must not reduce the system's option space (ethical imperative). Human judgment is required as an escape hatch (Godel's incompleteness).

---

## 3. The Strange Loop

### META-005: Self-Referential Governance Hierarchy

The four strata form a strange loop (Hofstadter 1979): meta-evolutionary changes at Stratum 4 modify the state rules (Stratum 1), structural rules (Stratum 2), and ontological rules (Stratum 3) that generate the meta-evolutionary stratum. The output of the hierarchy feeds back to its input.

This is not paradoxical because the loop operates across time. The current meta-rules govern the next iteration of change. That iteration may produce new meta-rules that govern the iteration after that. At each moment, there is a definite set of rules in force. The loop manifests as the sequence of rule-sets across time.

### META-006: Tangled Hierarchy

In practice, the four strata are not cleanly separated. A structural change (adding a repo) can trigger an ontological change (new category needed for the repo's domain) that triggers a meta-evolutionary change (new promotion criteria for the new category) that modifies the state rules governing the original structural change.

The levels are tangled: clean separation is a design ideal, not an operational reality. The specification defines them separately for analytical clarity while acknowledging that actual evolutionary episodes cross stratum boundaries.

---

## 4. Identity as Eigenform

### META-007: The Eigenform Principle

ORGANVM's identity is not any particular configuration of repos, organs, or governance rules -- all of these change through evolution. Identity is the fixed point of the system's recursive self-transformation (von Foerster 1981): the invariant that persists as the system transforms itself.

The five system invariants (INV-000-001 through INV-000-005) are the formal approximation of this eigenform. They are the properties that must hold across all evolutionary transformations, including meta-evolutionary ones.

**Constitutive consequence:** A meta-evolutionary change that violates an invariant is not an evolution of ORGANVM but a dissolution of it. If dependency acyclicity (INV-000-001) is abandoned, the resulting system is not an evolved ORGANVM but a different system. The eigenform is what makes evolution continuous rather than replacement.

### META-008: Observer Inclusion

The constitutional corpus (this specification and its siblings) describes ORGANVM. But it is also part of ORGANVM: tracked in the registry, managed as a submodule, and its content influences agent behaviour through CLAUDE.md injection. The corpus observes the system from within the system. There is no external vantage point from which ORGANVM's evolution can be specified.

This circularity is not a defect but a structural necessity (von Foerster 1981). Systems achieving stability through eigenforms must include the observer: the fixed point of self-observation is precisely identity.

---

## 5. Safety Mechanisms

### META-009: Governance Hierarchy

The strata are ordered by impact and by the governance rigor required for change:

| Stratum | Impact | Required Governance |
|---------|--------|-------------------|
| 1 (State) | Low | Automated validation (state machine + invariant check) |
| 2 (Structure) | Moderate | Automated validation + adversarial review |
| 3 (Ontology) | High | SPEC-008 change mode classification + adversarial review + creator sign-off |
| 4 (Meta) | System-defining | Full SPEC-000 Section 9 amendment process + human judgment |

Lower strata may not override higher strata. A state change (Stratum 1) may not violate a structural constraint (Stratum 2). An ontological change (Stratum 3) may not violate an invariant (anchored at Stratum 4). Violations are blocked by the governance hierarchy.

### META-010: Simulation Sandbox

Meta-evolutionary changes should be tested in simulation before deployment. The sandbox loads the current system state, applies the proposed meta-evolutionary change, and evaluates all invariants in the modified state. If any invariant is violated in simulation, the change is rejected before it reaches the production system.

The sandbox does not guarantee correctness -- it checks invariant preservation in the current state but cannot exhaustively explore all future states that the modified rules would produce. It is a safety net, not a proof of safety.

### META-011: Evolutionary Throttling

The rate of meta-evolutionary change is constrained to prevent runaway self-modification. At each stratum:

| Stratum | Rate Limit | Rationale |
|---------|-----------|-----------|
| 1 (State) | Unlimited | State changes are routine governance operations |
| 2 (Structure) | Multiple per sprint | Structural changes need integration time |
| 3 (Ontology) | One per sprint | Category changes require system-wide propagation |
| 4 (Meta) | One per era | Meta-evolutionary changes define the era |

These limits are themselves meta-evolutionary parameters -- subject to governed revision at Stratum 4.

### META-012: Incompleteness Escape Hatch

Godel's incompleteness theorems guarantee that ORGANVM's governance framework -- being a sufficiently powerful formal system -- contains valid evolutionary paths that cannot be proven valid by the current rules. These paths require human judgment.

INV-000-004 (Constitutional Supremacy) provides the escape hatch: when the formal governance system reaches its limits, the human operator may authorise a meta-evolutionary change based on constitutional intent rather than formal proof. This authorisation is the Godel sentence of the system: a statement (the change is warranted) that is true but unprovable within the formal framework.

Every use of the escape hatch is recorded as an EvolutionRecord with `justification_mode: human_judgment` and the operator's reasoning.

---

## 6. Meta-Evolution Entities

### META-013: PolicyObject

A governance rule that can be modified by Stratum 4. Each PolicyObject carries:

| Field | Type | Description |
|-------|------|-------------|
| `policy_id` | ULID | Stable identity across modifications |
| `version` | SemVer | Current version |
| `authority` | SpecRef | The SPEC that declares this policy |
| `content` | Rule | The evaluable governance rule |
| `modification_history` | List[EvolutionRecord] | Full amendment chain |

### META-014: InferenceRule

A rule that derives governance conclusions from observed state. InferenceRules implement the sensing cycle's infer phase:

| Field | Type | Description |
|-------|------|-------------|
| `rule_id` | ULID | Stable identity |
| `inputs` | List[MetricRef] | What observations feed the rule |
| `output` | GovernanceConclusion | What conclusion the rule produces |
| `confidence` | Float | Degree of confidence in the conclusion |

### META-015: SensorDefinition

A specification of what the system observes and how:

| Field | Type | Description |
|-------|------|-------------|
| `sensor_id` | ULID | Stable identity |
| `target` | EntityRef | What entity or property is observed |
| `cadence` | CadenceRef | How often (INST-HEARTBEAT cadences) |
| `threshold` | Value | When to escalate |

### META-016: MetricDefinition

A specification of how observations are aggregated and interpreted:

| Field | Type | Description |
|-------|------|-------------|
| `metric_id` | ULID | Stable identity |
| `type` | Enum | gauge, counter, delta (INST-TEMPORAL-METRICS) |
| `aggregation` | Enum | Scope-cascade function (INST-VARIABLE-RESOLUTION) |
| `leverage_level` | Int (1-12) | Meadows hierarchy position |
| `reference_mode` | Enum | Expected temporal pattern |

### META-017: EvolutionRecord

An immutable record of every meta-evolutionary change:

| Field | Type | Description |
|-------|------|-------------|
| `record_id` | ULID | Stable identity |
| `stratum` | Int (1-4) | Which stratum the change affects |
| `change_mode` | Enum | conservative, constrained, breaking (SPEC-008) |
| `justification_mode` | Enum | formal_proof, adversarial_review, human_judgment |
| `affected_entities` | List[ULID] | What was changed |
| `invariants_checked` | List[InvariantRef] | Which invariants were verified |
| `timestamp` | ISO 8601 | When the change was recorded |
| `operator_reasoning` | String | null | Human justification (for human_judgment mode) |

No EvolutionRecord may be deleted (INV-000-003 applied to the meta-level).

---

## 7. The Ethical Imperative as Safety Constraint

### META-018: Option Space Preservation

Von Foerster's (1981) ethical imperative -- "Act always so as to increase the number of choices" -- provides the safety constraint for meta-evolution.

For ORGANVM, "choices" maps to the set of valid future states: configurations reachable through legitimate governance operations without violating invariants. A meta-evolutionary change is evaluated by its effect on this set:

| Effect on Option Space | Classification | Governance Response |
|----------------------|---------------|-------------------|
| Expands (new states become reachable) | Healthy | Proceed through normal governance |
| Preserves (same states remain reachable) | Neutral | Proceed with justification for necessity |
| Contracts (previously reachable states become unreachable) | Pathological | Requires breaking revision process (SPEC-000 Section 9) |

**Operationalisation:** Full computation of the reachable state space is intractable (5^112 promotion configurations). Practical evaluation uses heuristic proxies: Does the proposed change add or remove promotion paths? Does it enable or block governance operations? Does it increase or decrease the system's expressiveness?

---

## 8. Implementation Status

| Component | Status | Location |
|-----------|--------|----------|
| State evolution (Stratum 1) | ALIGNED | `governance/state_machine.py`, `registry/` |
| Structural evolution (Stratum 2) | ALIGNED | `governance/`, `ontologia/`, `seed/` |
| Ontological evolution (Stratum 3) | PARTIAL | Ontologia supports entity creation; category extension not governed |
| Meta-evolution (Stratum 4) | MISSING | No programmatic support for rule modification |
| PolicyObject data model | MISSING | Target: `organvm-engine/src/organvm_engine/meta/` |
| EvolutionRecord store | MISSING | Target: append-only JSONL in ontologia store |
| Simulation sandbox | MISSING | Target: governance test framework with snapshot + invariant check |
| Evolutionary throttling | MISSING | Target: rate limiter in meta-evolution API |
| Option space heuristic evaluation | MISSING | Target: governance impact assessment |

---

## 9. Failure Modes

| Failure | Violated Element | Detection |
|---------|-----------------|-----------|
| Stratum violation (lower stratum overrides higher) | META-009 | Governance hierarchy enforcement |
| Invariant-violating meta-evolution (eigenform dissolution) | META-007 | Simulation sandbox + invariant check |
| Unrecorded meta-evolution (change without EvolutionRecord) | META-017, AX-000-008 | Audit: compare current rules against last recorded rule set |
| Runaway self-modification (throttle exceeded) | META-011 | Rate limiter enforcement |
| Option space contraction without breaking revision process | META-018 | Heuristic option space evaluation |

---

## 10. Evolution Constraints

SPEC-011 may be amended through the governed process defined in SPEC-000 Section 9. This specification is self-referential: it defines the rules for changing rules, including the rules for changing this specification. Amendment of SPEC-011 is therefore a Stratum 4 meta-evolutionary change requiring the full breaking revision process.

The four-stratum hierarchy may be extended (additional strata added) but may not be contracted. The eigenform principle (META-007) and the ethical imperative (META-018) are constitutive and may not be weakened.

---

## 11. Traceability

```
SPEC-000 AX-000-005 (Evolutionary Recursivity) → META-001/002/003/004 (four strata implement three orders of change)
SPEC-000 AX-000-006 (Topological Plasticity) → META-003 (ontological evolution enables topology change)
SPEC-000 INV-000-004 (Constitutional Supremacy) → META-012 (incompleteness escape hatch via human judgment)
SPEC-003 (Invariant Register) → META-007 (invariants are the eigenform)
SPEC-008 (Evolution & Migration Law) → META-001/002/003 (change modes govern first three strata)
INST-EVENT-SPINE → META-017 (EvolutionRecords are events on the spine)
INST-HEARTBEAT → META-011 (throttling cadence aligned with heartbeat cadence)
SPEC-010 (Alpha-Omega Phase Map) → META-004 (meta-evolution is an Omega-phase capability)
```

Full grounding narrative: `post-flood/specs/SPEC-011/grounding.md` (3,329 words)
Full risk register: `post-flood/specs/SPEC-011/risk-register.md` (5 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
