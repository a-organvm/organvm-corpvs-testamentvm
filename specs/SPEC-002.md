# SPEC-002: Primitive Register

```
Document ID:      SPEC-002
Title:            Primitive Register
Version:          1.1
Status:           RATIFIED (G3 review incorporated)
Layer:            L1 — Metaphysical Identity
Authoritative:    Entire System
Parent Specs:     SPEC-000 (System Manifesto), SPEC-001 (Entity Classification)
Date Ratified:    2026-03-18
Grounding:        post-flood/specs/SPEC-002/grounding.md
Risk Register:    post-flood/specs/SPEC-002/risk-register.md
Inventory:        post-flood/specs/SPEC-002/inventory.md
Bibliography:     post-flood/specs/bibliography.bib
```

---

## 1. The Seven Primitives

The ORGANVM system is constituted from exactly seven irreducible ontological categories. Every organ, repository, formation, signal, governance rule, metric, and agent is a composition of these primitives. No system object requires an eighth category; no primitive can be defined in terms of the remaining six.

Each primitive carries:

- **PRIM identifier** for cross-spec traceability
- **Formal definition** in Martin-Lof dependent type theory (Martin-Lof 1984)
- **OntoClean profile** (Guarino & Welty 2002): Rigidity (+R/−R/~R), Identity (+I/−I), Unity (+U/−U), Dependence (+D/−D)
- **BFO alignment** (Arp, Smith & Spear 2015) and **DOLCE alignment** (Masolo et al. 2003)
- **Formalization Status**: FORMAL (machine-checkable), FORMALIZABLE (specifiable but requires downstream definitions), or JUDGMENT (requires human assessment)

### PRIM-001: Entity

**A thing that exists with persistent identity.**

**Formal definition.** `Entity : Type_0`. Entity is the base type in the universe hierarchy — the identity-bearing substrate on which all other primitives depend. Every Entity carries a unique identifier (UID), persists through state changes, and satisfies a principled identity criterion: two Entities are identical if and only if they share a UID, regardless of their current Values, States, or Relations.

**OntoClean profile.** +R (rigid: necessarily an Entity once an Entity), +I (identity-carrying: UIDs provide individuation), +U (unity: every Entity has a boundary distinguishing parts from non-parts), −D (independent: Entities do not require other Entities for their existence).

**BFO alignment.** Independent Continuant — an identity-bearing persisting thing. **DOLCE alignment.** Endurant — wholly present at each time it exists.

**Reduction test.** Entity cannot be defined in terms of the other six primitives. Values require bearers. Relations require relata. Events require participants. States require subjects. Constraints require domains. Capabilities require possessors. Entity is the only primitive that is ontologically independent (−D). It is the irreducible substrate.

**Formalization Status: FORMAL.** The `EntityIdentity` class in `ontologia/entity/identity.py` implements ULID-based UIDs with entity_type enum, created_at, and lifecycle_status. Machine-checkable: every registered entity has a UID satisfying uniqueness.

**Risk Classification: GROUNDED.** Uncontested across all ontological traditions.

---

### PRIM-002: Value

**A datum attached to an entity.**

**Formal definition.** `Value : Entity -> Dimension -> Type_0`. A Value is dependent on both a bearer Entity and a dimension (the aspect being measured or assigned). The promotion_status "CANDIDATE" is a Value of dimension `promotion_status` inhering in a specific Repo Entity.

**OntoClean profile.** −R (non-rigid: Values change — a status shifts from LOCAL to CANDIDATE), −I (no independent identity: two instances of "PUBLIC_PROCESS" are indistinguishable), −U (no internal unity: Values are atomic data), +D (dependent: Values cannot exist without a bearer Entity).

**BFO alignment.** Quality — a Specifically Dependent Continuant. **DOLCE alignment.** Quality — inhering in an Endurant, with qualia providing comparison across entities.

**Reduction test.** Could Value be defined as "a State of an Entity restricted to a single dimension"? This creates circularity — State is defined as the composite of all Values (PRIM-005). Value is the atomic datum; State is the aggregate. Value is logically prior to State, not derivable from it.

**Formalization Status: FORMALIZABLE.** Variables are implemented (`organvm-engine/metrics/variables.py`) as key-value pairs with scope cascade but are not formally typed as Value primitives. Requires SPEC-001 entity classification for typed dimension declarations.

**Risk Classification: GROUNDED.** Both BFO and DOLCE recognize qualities as first-class ontological categories. The boundary between intrinsic qualities (code_files count, measured) and assigned labels (promotion_status, stipulated) suggests a possible future subdivision following BFO's Quality/Realizable distinction.

---

### PRIM-003: Relation

**A typed connection between entities.**

**Formal definition.** `Relation : Entity -> Entity -> RelType -> Type_0`. A Relation is dependent on two Entity relata and carries a type (depends-on, produces, consumes, hierarchy-parent-of). The dependency edge "engine depends-on schema-definitions" is a Relation of type `depends-on` connecting two Repo Entities.

**OntoClean profile.** +R (rigid: necessarily a Relation once a Relation), −I (no intrinsic identity: identified by relata + type, not by independent UID), +U (unity: a Relation is a unified whole of its relata, direction, and type), +D (dependent: Relations depend on their relata — if Entity A is destroyed, its Relations cease to exist).

**BFO alignment.** Relational Quality — a Specifically Dependent Continuant depending on multiple bearers. **DOLCE alignment.** Abstract — lacking spatial or temporal qualities of its own.

**Reduction test.** Relations cannot be reduced to co-occurring Values on two Entities. The dependency "A depends-on B" carries directionality (A depends on B, not vice versa) and type (depends-on, not produces) that no combination of Values on A and B can express. Directionality and type are constitutive of Relation, not reducible to monadic properties of the relata.

**Formalization Status: FORMALIZABLE.** Three separate relation implementations exist (ontologia lineage, seed graph edges, governance dependency graph) but are not unified under a single Relation primitive. Requires consolidation under SPEC-001 entity classification.

**Risk Classification: GROUNDED.** All ontological traditions recognize relations as first-class, though they disagree on categorization (BFO: dependent continuant; DOLCE: abstract). The disagreement concerns classification, not primitive status.

---

### PRIM-004: Event

**A state change with timestamp and causation.**

**Formal definition.** `Event : Entity -> State -> State -> Type_0`. An Event is a transition from one State to another for a specific Entity, carrying a timestamp and causal provenance. The promotion of repo X from CANDIDATE to PUBLIC_PROCESS is an Event: Entity = X, State_before = {promotion_status: CANDIDATE, ...}, State_after = {promotion_status: PUBLIC_PROCESS, ...}.

**OntoClean profile.** +R (rigid: necessarily an Event once an Event), +I (identity-carrying: Events have identity criteria — timestamp, causation, affected Entity, type — making each individually identifiable), −U (no persistent unity: Events are temporally bounded), +D (dependent: Events depend on Entities and States).

**BFO alignment.** Process or Process Boundary (Occurrent). **DOLCE alignment.** Perdurant — specifically Achievement (instantaneous) or Accomplishment (extended).

**Reduction test.** An Event is not merely a pair of States (before, after). It carries causation (what triggered the transition), timestamp (when it occurred), and type (what kind of transition) — none of which can be expressed as a State or pair of States. The causal and temporal dimensions are constitutive.

**Formalization Status: FORMALIZABLE.** Events exist as observation signals (`ontologia/sensing/signals.py` — RawSignal) and edge activity tracking (`pulse/flow.py` — EdgeActivity) but are not reified as the constitutional primitive described here. The append-only event log is a Layer 4A implementation target.

**Risk Classification: GROUNDED.** Universal across all ontological traditions. BFO and DOLCE differ on subclassification but agree on the irreducibility of temporal occurrences.

---

### PRIM-005: State

**The current configuration of an entity's values.**

**Formal definition.** `State : (e : Entity) -> Pi(d : Dim(e)) -> Value(e, d) -> Type_0`. A State is a dependent product over all of an Entity's dimensions — the complete assignment of Values to an Entity at a point in time. Equivalently, it is the Sigma-type `Sigma(v : ValueDimension) x Value(v)` for a given Entity.

**OntoClean profile.** ~R (anti-rigid: States are contingent — an Entity can change State while remaining the same Entity), −I (no independent identity: States are identified by their Entity + complete Value assignment at a time), +U (unity: a State is a unified snapshot — the complete configuration, not a loose collection), +D (dependent: States depend on both Entities and Values).

**BFO alignment.** No direct equivalent — BFO treats the totality of an entity's Qualities at a time as derivative, not a separate category. **DOLCE alignment.** State — a homeomeric Perdurant (every temporal part of sitting is itself sitting).

**Reduction test.** Can State be defined as "the set of all Values of an Entity at a time"? Yes — but this definition is itself a primitive operation. The reification of "current configuration" as a first-class concept is what makes State primitive. Without State, there is no way to express "the system was in configuration X at time T" — only individual value assertions, losing the holistic snapshot. The dependent product formalization (Pi-type over all dimensions) captures precisely this: a State is not a set of Values but the *complete assignment function* from dimensions to Values.

**The decisive argument for State's primitive status is functional**: State is the domain of Constraints. Constraints restrict States (complete configurations), not individual Values. The governance rule "promotion requires CI workflow AND platinum status AND implementation_status=ACTIVE" is a predicate over the *joint* configuration of three dimensions — it cannot be decomposed into three independent predicates over individual Values without losing the conjunctive structure. Without State as a primitive, Constraint has no well-typed domain.

**Formalization Status: FORMALIZABLE.** States are implicit in the codebase — the current values of an entity's fields in `registry/query.py` and promotion states in `governance/state_machine.py`. Not reified as first-class State objects with snapshot semantics.

**Risk Classification: ADAPTED.** BFO's subsumption of State into Quality aggregates is the primary challenge. ORGANVM retains State because it occupies a unique structural role as the domain of Constraints — a role that requires the holistic snapshot, not merely the collection of individual Values. The departure from BFO is explicitly acknowledged.

### Contestation Disclosure (PRIM-005)

BFO does not recognize State as a separate category. ORGANVM retains it because of the system's governance architecture, not because of a dispute about general ontology. State is primitive *for ORGANVM* because Constraints require a well-typed domain over complete configurations. A purely descriptive ontology could eliminate State without loss; a governed ontology cannot.

---

### PRIM-006: Constraint

**A rule limiting what states or transitions are lawful.**

**Formal definition.** `Constraint : State -> Deontic -> Prop` where `Deontic = MUST | SHOULD | MAY`. A Constraint is a deontic predicate over States — it classifies States as obligatory (MUST be reached), permissible (MAY be occupied), or prohibited (MUST NOT be entered) relative to a governance context. Via Martin-Lof's propositions-as-types correspondence, a Constraint is a type; a proof that a State satisfies the Constraint is a term inhabiting that type. An uninhabited Constraint type = an unsatisfiable rule. The deontic parameter preserves the normative force that distinguishes Constraints from mere Boolean predicates: `MUST` corresponds to obligation (von Wright's O), `MAY` to permission (P), and the negation of `MAY` to prohibition (F). The promotion_criteria in `governance-rules.json` — requiring ci_workflow AND platinum_status AND implementation_status=ACTIVE — is a Constraint with deontic mode MUST: the system is obligated to enforce this predicate on promotion transitions. Full ADICO-structured formalization (Crawford & Ostrom 1995) is deferred to SPEC-003 (Invariant Register) and SPEC-005 (Rulebook).

**OntoClean profile.** +R (rigid: necessarily a Constraint once a Constraint), −I (no intrinsic identity: identified by content, not by independent UID), +U (unity: a Constraint is a unified rule — condition + deontic force + consequence), +D (dependent: Constraints depend on the States and Entities they constrain).

**BFO alignment.** No equivalent. BFO describes what IS, not what OUGHT. **DOLCE alignment.** No equivalent. DOLCE categorizes descriptive ontological kinds, not normative rules.

**Reduction test.** Can Constraint be defined as "a predicate over States that returns true/false"? Partially — but this loses deontic force. A Constraint carries normativity: it declares what MUST, SHOULD, or MAY be the case (von Wright 1951). A pure predicate merely classifies; it does not prescribe, prohibit, or permit. Can Constraint be defined as "a Relation between actual States and permitted States"? This loses the constitutive asymmetry: Constraints are imposed on States by governance, not symmetric connections between equals.

**Grounding in deontic logic and institutional ontology.** Constraint imports concepts from three traditions that standard descriptive ontologies do not draw on:

- **Von Wright (1951):** Deontic logic — obligation (O), permission (P), prohibition (F) as modal operators over propositions
- **Crawford & Ostrom (1995):** ADICO institutional grammar — Attribute-Deontic-aIm-Condition-Or-else
- **Ostrom (2005):** Rules-in-use vs. rules-in-form — the distinction between Constraints as declared (governance-rules.json) and Constraints as enforced (engine validators)

**Formalization Status: FORMALIZABLE.** Governance rules exist as JSON config (`governance-rules.json`) and are evaluated procedurally (`governance/rules.py`), but are not first-class ontological objects with their own identity, deontic classification, or traceability to this primitive register.

**Risk Classification: NOVEL.** Constraint has no counterpart in BFO, DOLCE, Armstrong, or Johansson — a 0/2 alignment score against the two foundational ontologies.

### Contestation Disclosure (PRIM-006)

Constraint is ORGANVM's most distinctive contribution to the primitive register. Ontologists in the BFO or DOLCE traditions may reject it as a category error — importing normative content into an ontological register that should be purely descriptive. ORGANVM's response: the descriptive/normative boundary is itself a theoretical commitment, not a fact. A system whose identity is constituted by governance rules requires normative categories in its primitive register. Gruber's minimal commitment principle supports this: the ontology should make only those commitments required by its application domain — and ORGANVM's domain is governance.

---

### PRIM-007: Capability

**An operation an entity may perform.**

**Formal definition.** `Capability : Entity -> EventType -> Type_0`. A Capability is a dispositional property: Entity e has Capability c if e CAN produce Events of type c. A repo's "deploy" capability means the repo can produce deployment Events — whether or not any deployment has actually occurred.

**OntoClean profile.** ~R (anti-rigid: Capabilities are contingent — an Entity can gain or lose Capabilities), −I (no intrinsic identity: identified by type and bearer), −U (no internal unity: Capabilities are atomic), +D (dependent: Capabilities depend on their bearer Entity and on enabling States/Constraints).

**BFO alignment.** Disposition or Function — a Realizable Entity (Specifically Dependent Continuant). BFO's trichotomy (Disposition/Role/Function) suggests Capability may conflate three distinct concepts. **DOLCE alignment.** No direct equivalent.

**Reduction test.** Can Capability be defined as "a Constraint that permits rather than prohibits"? No — Constraints are rules; Capabilities are powers. The distinction is between normative rule and dispositional power — deontic modality vs. dynamic modality. Can Capability be defined as "a function type Entity -> Event"? This captures the operational meaning but loses the dispositional aspect: a Capability can exist without being exercised. Johansson (2004, Ch. 11) argues that tendencies are irreducible to their manifestations — a sugar cube's solubility exists even when it is not dissolving. Similarly, a repo's deploy-capability exists even when no deployment is occurring.

**BFO's refinement.** BFO's Disposition/Role/Function trichotomy raises a legitimate concern:

| BFO Category | ORGANVM Example | Distinction |
|-------------|----------------|-------------|
| Disposition | Module's extraction potential | Latent, may never manifest |
| Role | Entity's "flagship" status | Contextual, assigned by governance |
| Function | Repo's "deploy" capability | Internally grounded in CI configuration |

ORGANVM's single Capability primitive conflates these. The conflation is acknowledged as a simplification — future versions may subdivide following BFO, but SPEC-002 v1.0 retains the unified primitive to avoid premature refinement.

**Formalization Status: FORMALIZABLE.** No explicit capability tracking exists. Repos have `ci_workflow` and `platinum_status` as implicit capability indicators. Formal declaration of what entities CAN do is a gap.

**Risk Classification: CONTESTED.** BFO recognizes dispositions as first-class (1/2 alignment). Johansson independently validates tendencies as irreducible. DOLCE does not recognize a Capability equivalent.

### Contestation Disclosure (PRIM-007)

Capability is contested. BFO's Disposition/Role/Function trichotomy provides a more refined analysis. ORGANVM retains the unified primitive following Johansson's irreducibility thesis and for functional necessity — without Capability, there is no way to express what an Entity CAN do as opposed to what it IS or what it HAS. The acknowledged need for future subdivision is a refinement trajectory, not a retraction.

---

### Summary: Primitive Register

| ID | Primitive | Type Signature | OntoClean | BFO | DOLCE | Risk | Formalization |
|----|-----------|---------------|-----------|-----|-------|------|---------------|
| PRIM-001 | Entity | `Type_0` | +R +I +U −D | 1/1 | 1/1 | GROUNDED | FORMAL |
| PRIM-002 | Value | `Entity -> Dimension -> Type_0` | −R −I −U +D | 1/1 | 1/1 | GROUNDED | FORMALIZABLE |
| PRIM-003 | Relation | `Entity -> Entity -> RelType -> Type_0` | +R −I +U +D | 1/1 | 1/1 | GROUNDED | FORMALIZABLE |
| PRIM-004 | Event | `Entity -> State -> State -> Type_0` | +R +I −U +D | 1/1 | 1/1 | GROUNDED | FORMALIZABLE |
| PRIM-005 | State | `(e : Entity) -> Pi(d : Dim(e)) -> Value(e,d) -> Type_0` | ~R −I +U +D | 0/1 | 0.5/1 | ADAPTED | FORMALIZABLE |
| PRIM-006 | Constraint | `State -> Prop` | +R −I +U +D | 0/1 | 0/1 | NOVEL | FORMALIZABLE |
| PRIM-007 | Capability | `Entity -> EventType -> Type_0` | ~R −I −U +D | 0.5/1 | 0/1 | CONTESTED | FORMALIZABLE |

---

## 2. Composition Framework

### 2.1 Non-Extensional Mereology

The seven primitives are atoms, not the system. The system consists of composite objects — organs, repos, modules, governance structures, promotion pipelines — each composed from primitives. The composition framework must answer: how do primitives combine into wholes, and what determines the identity of the resulting composite?

Classical extensional mereology (CEM) cannot serve this purpose. Under CEM's extensionality axiom, two composites with identical parts are identical. But ORGANVM requires non-extensional composition: two organs with identical repos can differ if they have different governance rules (Constraints), different aesthetic identities (Values), or different dependency structures (Relations). The organ's identity is not exhausted by its repositories.

Simons' Minimal Mereology (MM) (Simons 1987) provides the alternative. MM retains the core mereological axioms while dropping extensionality and unrestricted composition:

| Axiom | Statement | Status |
|-------|----------|--------|
| Reflexivity | Every object is part of itself | Retained |
| Antisymmetry | If x is part of y and y is part of x, then x = y | Retained |
| Transitivity | If x is part of y and y is part of z, then x is part of z | Retained |
| Weak Supplementation | If x is a proper part of y, then y has another proper part z disjoint from x | Retained |
| Extensionality | Two composites with identical parts are identical | **Dropped** |
| Unrestricted Composition | Any arbitrary collection forms a composite | **Dropped** |

Under MM, a composite's identity depends on the *structure-determining relations* among its parts, not merely the parts' existence. An organ is what Simons calls an *integral whole*: a composite whose parts stand in relations that are essential to its identity.

### 2.2 Dependent Record Types

In the type-theoretic formalization, composition is expressed through dependent record types rather than mere Sigma-types (dependent pairs). A Sigma-type `Sigma(x : A) x B(x)` is an existential — it says "there exists an x of type A and a b of type B(x)." This captures loose aggregation but not structured wholes.

An organ is a *dependent record*: a structured collection where the types of later fields depend on the values of earlier fields, and where structural constraints restrict the space of valid records. The dependent record type captures Simons' integral whole: the record's identity depends on the structure among its fields, not just their existence.

```
CompositeObject = Record {
  entities     : List Entity
  values       : Pi(e : entities) -> List (Value e)
  relations    : List (Sigma(e1 e2 : entities) x RelType)
  states       : Pi(e : entities) -> State e
  constraints  : List (Constraint (states))
  capabilities : Pi(e : entities) -> List (Capability e)
}
```

This record is non-extensional: two records with identical entity lists can differ in their relations, constraints, or capabilities. It is also structured: the constraints field restricts the space of valid states, and the values field depends on the specific entities in the entities field.

### 2.3 Typed Composition Relations

The composition relation is typed: `contains(ORGAN, REPO)` and `contains(REPO, MODULE)` are different Relations with different structural implications. Simons' distinction between essential and non-essential parts (Ch. 8) applies:

- **Essential parts:** Removing one changes the composite's identity. The engine is an essential part of Meta — Meta without the engine is a different organ.
- **Generic dependence:** The composite needs *some* parts of a certain type but not any specific roster. An organ needs repos but not necessarily any particular repo.
- **Rigid dependence:** The composite necessarily has that exact part. The registry is rigidly depended upon by the governance system.

---

## 3. Domain Entity Compositions

The following domain entities from SPEC-001 are compositions of primitives from the register. None requires an additional primitive; none is itself a primitive.

### 3.1 Agent

An Agent is a composite that produces Events through Capabilities under Constraints:

```
Agent = Record {
  identity    : Entity                          -- PRIM-001: identity-bearing
  properties  : List (Value identity)           -- PRIM-002: agent type, handle, model
  roles       : List (Relation identity target) -- PRIM-003: claims, assignments
  actions     : List Event                      -- PRIM-004: tool calls, commits, reviews
  session     : State identity                  -- PRIM-005: active/completed, current context
  permissions : List (Constraint session)       -- PRIM-006: what the agent MAY do
  powers      : List (Capability identity)      -- PRIM-007: what the agent CAN do
}
```

### 3.2 Artifact

An Artifact is a composite that persists through state changes and carries measured Values:

```
Artifact = Record {
  identity    : Entity                          -- PRIM-001: repo, module, document
  properties  : List (Value identity)           -- PRIM-002: name, tier, code_files, test_count
  edges       : List (Relation identity target) -- PRIM-003: dependencies, produces/consumes
  status      : State identity                  -- PRIM-005: promotion status, health
  rules       : List (Constraint status)        -- PRIM-006: promotion criteria, quality gates
  powers      : List (Capability identity)      -- PRIM-007: CI, deploy, publish
}
```

### 3.3 Signal

A Signal is a composite that mediates inter-entity communication:

```
Signal = Record {
  identity    : Entity                          -- PRIM-001: signal instance
  payload     : List (Value identity)           -- PRIM-002: signal type, content, amplitude
  route       : Relation source target          -- PRIM-003: from producer to consumer
  emission    : Event source                    -- PRIM-004: the act of signal production
  attenuation : List (Constraint payload)       -- PRIM-006: type-compatibility, gain limits
}
```

### 3.4 Governance Object

A Governance Object (rule, dictum, axiom) is a composite whose Constraint is constitutive:

```
GovernanceObject = Record {
  identity    : Entity                          -- PRIM-001: the rule itself has identity
  properties  : List (Value identity)           -- PRIM-002: severity, enforcement mode, scope
  scope       : List (Relation identity target) -- PRIM-003: applies-to organs/repos
  enactment   : Event                           -- PRIM-004: when the rule was ratified
  rule        : Constraint domain               -- PRIM-006: the normative content
}
```

### 3.5 Evidence

Evidence was a candidate for the primitive register and is explicitly shown to be a composition:

```
Evidence = Record {
  identity    : Entity                          -- PRIM-001: test result, audit trace
  datum       : Value identity                  -- PRIM-002: pass/fail, coverage %, measured value
  observation : Event observer                  -- PRIM-004: the act of measurement at a time
}
```

Evidence is operationally important — test results, audit traces, and metrics drive governance decisions. But ontologically it is `Entity + Value + Event`: a thing that records a measurement at a time. Gruber's minimal commitment principle applies: do not elevate domain concepts to ontological primitives unless they are irreducible. Evidence is reducible.

### 3.6 Process

Process was a candidate for the primitive register and is explicitly shown to be a composition:

```
Process = Record {
  identity    : Entity                          -- PRIM-001: the process has identity
  steps       : List Event                      -- PRIM-004: ordered sequence of state changes
  ordering    : List (Relation step_n step_n+1) -- PRIM-003: temporal/causal ordering
  governance  : List (Constraint steps)         -- PRIM-006: rules governing valid step sequences
  status      : State identity                  -- PRIM-005: active/completed/failed
}
```

A promotion process is an Entity (it has identity), a sequence of Events (governance audit, CI verification, state transition), and governing Constraints (promotion_criteria, required transitions). The ordering and governance come from Constraint and Relation, not from Process as a sui generis primitive.

---

## 4. Alignment with SPEC-000 Axioms

Every SPEC-000 axiom must be expressible in terms of the seven primitives without requiring additional ontological categories. This section demonstrates sufficiency.

### AX-000-001: Ontological Primacy

*Define what exists before defining how it behaves.*

**Expression in primitives:** Every Entity (PRIM-001) must be ontologically declared before Constraints (PRIM-006) are applied to it. This is a Constraint (PRIM-006) over Events (PRIM-004): for all Event e that applies a Constraint to Entity x, there must exist a prior Event creating Entity x.

**Primitives required:** PRIM-001 (Entity), PRIM-004 (Event), PRIM-006 (Constraint). No additional categories needed.

### AX-000-002: Organizational Closure

*Every constitutive process of the system is specified by processes within the system.*

**Expression in primitives:** The system's constitutive processes are compositions of Events (PRIM-004) under Constraints (PRIM-006). Closure means: for every Event in a constitutive process, its causal provenance traces to another constitutive Event or to the human principal (an Entity, PRIM-001). No external authority specifies the system's organization.

**Primitives required:** PRIM-001 (Entity), PRIM-004 (Event), PRIM-006 (Constraint). No additional categories needed.

### AX-000-003: Individual Primacy

*The system exists to amplify individual creative capacity, not to replace it.*

**Expression in primitives:** This is a Constraint (PRIM-006) over the space of all system Constraints: no Constraint may be justified solely by system-level optimization (a Value, PRIM-002) if it diminishes creative autonomy (a Value, PRIM-002) of the individual practitioner (an Entity, PRIM-001). The assessment requires JUDGMENT — it cannot be reduced to a machine-checkable predicate.

**Primitives required:** PRIM-001 (Entity), PRIM-002 (Value), PRIM-006 (Constraint). No additional categories needed.

### AX-000-004: Constitutional Governance

*No component may exist, operate, or evolve without constitutional authorization.*

**Expression in primitives:** Every Entity (PRIM-001) requires a seed.yaml declaring Relation (PRIM-003) to an organ, Value (PRIM-002) for tier and status, and State (PRIM-005) for promotion. Every State transition is governed by Constraints (PRIM-006) encoded in the state machine. Every dependency is a declared Relation (PRIM-003) validated against allowed_edges.

**Primitives required:** PRIM-001 through PRIM-006. No additional categories needed.

### AX-000-005: Evolutionary Recursivity

*The system must be capable of modifying its own rules, including the rules for rule-modification, through governed processes.*

**Expression in primitives:** First-order change: State (PRIM-005) evolves via Events (PRIM-004) within existing Constraints (PRIM-006). Second-order change: Constraints themselves are Entities (PRIM-001) with States, subject to their own Constraints (meta-rules). Third-order change: the meta-rules are Entities subject to meta-meta-rules. The recursive structure is enabled by the fact that Constraints are first-class composites with Entity identity — they can be governed by other Constraints.

**Primitives required:** PRIM-001 (Entity), PRIM-004 (Event), PRIM-005 (State), PRIM-006 (Constraint). No additional categories needed.

### Sufficiency Verdict

All five SPEC-000 axioms (plus AX-000-006 through AX-000-009) are expressible in the seven primitives. No axiom requires Process, Evidence, Agent, or any candidate excluded from the register. The register is sufficient for SPEC-000's governance architecture.

---

## 5. Contestation Disclosures

Honest ontological engineering requires disclosing where claims are contested, marginal, or novel. SPEC-002 makes five disclosures, ordered by theoretical significance.

### 5.1 State Is a Marginal Primitive

**Status:** ADAPTED (risk register claim #5)

BFO does not recognize State as a separate category, treating it as the derivative totality of an entity's Qualities at a time. ORGANVM retains State because it serves a structural role that BFO does not need to fill: State is the domain of Constraints, and Constraints are essential to governance.

**The argument is functional, not ontological in BFO's realist sense.** State is primitive *for ORGANVM* because the system's governance architecture requires holistic configuration snapshots as first-class objects. A purely descriptive ontology could eliminate State without loss; a governed ontology cannot.

### 5.2 Constraint Is a Novel Primitive

**Status:** NOVEL (risk register claim #6)

Constraint has no counterpart in any standard foundational ontology — 0/2 alignment against BFO and DOLCE. This novelty is the primitive register's most significant theoretical risk.

**Mitigation:** Grounding in adjacent formal traditions — deontic logic (von Wright 1951), institutional grammar (Crawford & Ostrom 1995), rules-in-use theory (Ostrom 2005), constitutive rules (Searle 1995). These traditions have rigorous peer-reviewed foundations; they operate in a different intellectual space than descriptive ontology.

**Anticipated objection:** Ontologists in BFO/DOLCE traditions may reject Constraint as a category error — importing normative content into a register that should be purely descriptive. **Response:** The descriptive/normative boundary is itself a theoretical commitment, not a fact. A system whose identity is constituted by governance rules requires normative categories in its primitive register.

### 5.3 Capability Is a Contested Primitive

**Status:** CONTESTED (risk register claim #7)

BFO recognizes dispositions but subdivides them into Disposition (latent), Role (contextual), and Function (internally grounded) — a trichotomy that ORGANVM's unified Capability conflates. DOLCE does not recognize Capability as distinct.

**Retention argument:** Johansson's irreducibility thesis — tendencies cannot be reduced to their manifestations. **Acknowledged refinement:** Future subdivision into Disposition/Role/Function following BFO is a legitimate trajectory that SPEC-002 explicitly flags for later work without requiring register revision (the subdivision would be type refinement within PRIM-007, not a new primitive).

### 5.4 Process Is Not a Primitive

**Status:** NOVEL reconciliation (risk register claim #10)

The Stage-II corpus lists Process as a root class. SPEC-002 resolves this by demonstrating Process = Entity + ordered Events + governing Constraints (Section 3.6). BFO treats Process as an Occurrent subtype — a classification ORGANVM replicates by typing certain composite objects as "process-shaped" without elevating Process to primitive status.

### 5.5 Evidence Is Not a Primitive

**Status:** NOVEL reconciliation (risk register claim #11)

The Stage-II corpus lists Evidence as a root class. SPEC-002 resolves this by demonstrating Evidence = Entity + Value + Event (Section 3.5). Evidence is operationally important but ontologically reducible. Gruber's minimal commitment principle: do not elevate domain concepts to ontological primitives unless they are irreducible.

---

## 6. Evolution Constraints

SPEC-002 may be amended through the following governed process only. This process is self-contained — it does not depend on any downstream spec for its authority.

### 6.1 Amendment Types

| Type | Definition | Requirements |
|------|-----------|-------------|
| **Conservative Refinement** | Adds detail to an existing primitive (e.g., subdividing Value into intrinsic/assigned). Preserves primitive count and type signatures. | Adversarial review + creator sign-off |
| **Constrained Extension** | Adds a new primitive (PRIM-008+). Must pass the reduction test against all existing primitives. | Adversarial review + impact assessment on downstream specs + demonstration that no existing primitive or composition can serve the function + creator sign-off |
| **Primitive Retraction** | Removes a primitive by demonstrating it is reducible to the remaining primitives. | Adversarial review + migration plan for all downstream references + demonstration that all SPEC-000 axioms remain expressible + creator sign-off |
| **Breaking Revision** | Changes the type signature or OntoClean profile of an existing primitive. | New grounding narrative + adversarial review + human spot-check of cited sources + review of all downstream specs + creator sign-off |

### 6.2 Reduction Test Protocol

Any proposed 8th primitive (PRIM-008) must survive the following test:

1. **Attempted reduction:** Can PRIM-008 be expressed as a composition of existing primitives (PRIM-001 through PRIM-007) using the dependent record type framework from Section 2?
2. **Loss assessment:** If the reduction succeeds syntactically, does it lose constitutive properties (e.g., deontic force for Constraint, dispositional existence for Capability)?
3. **Cross-tradition validation:** Does at least one of BFO, DOLCE, Armstrong, or Johansson recognize the candidate as irreducible or first-class?
4. **Sufficiency impact:** Does the absence of PRIM-008 prevent the expression of any SPEC-000 axiom or SPEC-001 entity class?

A candidate passes only if: (1) reduction fails or loses constitutive properties, AND (2) at least one tradition recognizes it, AND (3) its absence creates an expressibility gap.

### 6.3 Versioning

The original SPEC-002 is never overwritten. Amendments are versioned: SPEC-002-v1.1, v1.2, etc. The primitive identifiers (PRIM-001 through PRIM-007) are permanent — a retracted primitive's identifier is retired, not reassigned.

---

## 7. Traceability

### 7.1 Upward Traceability (to SPEC-000)

| SPEC-000 Element | SPEC-002 Grounding |
|------------------|--------------------|
| AX-000-001 (Ontological Primacy) | PRIM-001 (Entity) + PRIM-004 (Event) + PRIM-006 (Constraint) — Section 4.1 |
| AX-000-002 (Organizational Closure) | PRIM-001 + PRIM-004 + PRIM-006 — Section 4.2 |
| AX-000-003 (Individual Primacy) | PRIM-001 + PRIM-002 (Value) + PRIM-006 — Section 4.3 |
| AX-000-004 (Constitutional Governance) | PRIM-001 through PRIM-006 — Section 4.4 |
| AX-000-005 (Evolutionary Recursivity) | PRIM-001 + PRIM-004 + PRIM-005 (State) + PRIM-006 — Section 4.5 |
| AX-000-006 (Topological Plasticity) | PRIM-001 + PRIM-003 (Relation) + PRIM-005 + PRIM-006 |
| AX-000-007 (Alchemical Inheritance) | PRIM-001 + PRIM-003 + PRIM-004 + PRIM-005 |
| AX-000-008 (Multiplex Flow Governance) | PRIM-003 + PRIM-006 (typed relations under typed constraints) |
| AX-000-009 (Modular Alchemical Synthesis) | PRIM-003 + PRIM-004 + PRIM-006 + PRIM-007 (Capability) |
| Section 6 Primitives declaration | PRIM-001 through PRIM-007 — Section 1 (this document) |
| INV-000-001 (Dependency Acyclicity) | PRIM-003 (Relation) + PRIM-006 (Constraint) |
| INV-000-002 (Governance Reachability) | PRIM-001 + PRIM-003 + PRIM-006 |
| INV-000-003 (Identity Persistence) | PRIM-001 (Entity: UID never destroyed) |
| INV-000-004 (Constitutional Supremacy) | PRIM-006 (Constraints are hierarchically ordered) |
| INV-000-005 (Observability) | PRIM-002 (Value) + PRIM-005 (State) + PRIM-007 (Capability) |

### 7.2 Lateral Traceability (to SPEC-001)

| SPEC-001 Entity Class | Primitive Composition |
|-----------------------|-----------------------|
| ORGAN | PRIM-001 + PRIM-002 + PRIM-003 + PRIM-005 + PRIM-006 |
| REPO | PRIM-001 + PRIM-002 + PRIM-003 + PRIM-005 + PRIM-006 + PRIM-007 |
| MODULE | PRIM-001 + PRIM-002 + PRIM-003 + PRIM-005 + PRIM-007 |
| DOCUMENT | PRIM-001 + PRIM-002 + PRIM-003 |
| SESSION | PRIM-001 + PRIM-002 + PRIM-004 + PRIM-005 |
| VARIABLE | PRIM-001 + PRIM-002 + PRIM-005 |
| METRIC | PRIM-001 + PRIM-002 + PRIM-006 |

### 7.3 Downward Traceability (to implementation)

| Primitive | Current Code Location | Alignment |
|-----------|-----------------------|-----------|
| PRIM-001 Entity | `ontologia/entity/identity.py` — EntityIdentity | ALIGNED |
| PRIM-002 Value | `organvm-engine/metrics/variables.py` — variable resolution | DRIFT |
| PRIM-003 Relation | `ontologia/entity/lineage.py`, `seed/graph.py`, `governance/dependency_graph.py` | DRIFT (3 disconnected systems) |
| PRIM-004 Event | `ontologia/sensing/signals.py` — RawSignal | DRIFT |
| PRIM-005 State | `registry/query.py`, `governance/state_machine.py` | DRIFT (implicit, not reified) |
| PRIM-006 Constraint | `governance/rules.py`, `governance-rules.json` | DRIFT (JSON config, not ontological objects) |
| PRIM-007 Capability | Not implemented | MISSING |

The five DRIFT items share a pattern: the concept exists in code under a domain-specific name (variable, edge, signal, status, rule) but is not formalized as an instance of the corresponding ontological primitive. The MISSING item (Capability) is the most significant gap. Implementation alignment is a downstream concern for Layer 2 and Layer 3 specs; SPEC-002 establishes the normative target.

### 7.4 Academic Lineage

| Primitive | Traditions | Key Sources |
|-----------|-----------|-------------|
| PRIM-001 Entity | Substance ontology, BFO, DOLCE | Simons 1987, Arp et al. 2015, Masolo et al. 2003 |
| PRIM-002 Value | Quality theory, BFO, DOLCE | Armstrong 1978, Arp et al. 2015, Masolo et al. 2003 |
| PRIM-003 Relation | Relational ontology, BFO | Simons 1987, Arp et al. 2015, Johansson 2004 |
| PRIM-004 Event | Process philosophy, BFO, DOLCE | Arp et al. 2015, Masolo et al. 2003 |
| PRIM-005 State | DOLCE, Armstrong | Masolo et al. 2003, Armstrong 1978 |
| PRIM-006 Constraint | Deontic logic, institutional design | von Wright 1951, Ostrom 2005, Crawford & Ostrom 1995, Searle 1995 |
| PRIM-007 Capability | Disposition theory, BFO | Johansson 2004, Arp et al. 2015 |
| Composition framework | Non-extensional mereology, type theory | Simons 1987, Martin-Lof 1984, Pierce 2002 |

Full grounding narrative: `post-flood/specs/SPEC-002/grounding.md` (6,874 words)
Full risk register: `post-flood/specs/SPEC-002/risk-register.md` (11 classified claims)
Current state inventory: `post-flood/specs/SPEC-002/inventory.md` (7 primitive-to-code mappings)
Full bibliography: `post-flood/specs/bibliography.bib`
