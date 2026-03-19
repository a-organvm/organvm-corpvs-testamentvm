<!-- NOTE: Signal classes defined here are the canonical behavioral-contract view. See INST-FORMATION FORM-010 for the interdependence-type view of the same signal alphabet. Both views are complementary, not competing. Reconciliation target: SPEC-007 v1.1 -->
# SPEC-007: Interface Contract Spec

```
Document ID:      SPEC-007
Title:            Interface Contract Spec
Version:          1.0
Status:           RATIFIED
Layer:            L3A — Structural Architecture
Authoritative:    Inter-Organ Communication
Parent Specs:     SPEC-000 (System Manifesto), SPEC-002 (Primitive Register), SPEC-005 (Rulebook)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/SPEC-007/grounding.md
Risk Register:    post-flood/specs/SPEC-007/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. The 14 Canonical Signal Classes

ORGANVM's inter-organ communication operates through 14 canonical signal classes. Each signal class is not merely a type label but a behavioral contract: a commitment about what the signal contains, what preconditions the producer must satisfy, what postconditions the consumer may rely upon, and what invariants the signal preserves. The signal classes are the alphabet of the system's communication channel (Shannon 1948, structurally adapted).

Each signal class record carries:

| Field | Description |
|-------|-------------|
| **ID** | `SIG-NNN` permanent identifier |
| **Class Name** | The canonical signal type name |
| **Producer Precondition** | What must be true before emission |
| **Signal Postcondition** | What the consumer may assume about content |
| **Channel Constraints** | Co-occurrence rules and attenuation policies |
| **Invariants Preserved** | Which system invariants the signal must not violate |

### SIG-001: ONT_FRAGMENT

**Definition:** An ontological construct — a new or revised entity type, category, relation, or classification.

**Producer Precondition:** The producing formation has ontological authority (formation type is GENERATOR or LABORATORY, not ROUTER or RESERVOIR). Producer is at promotion status >= CANDIDATE.

**Signal Postcondition:** Content conforms to the ontologia entity schema. Fragment is well-typed against the SPEC-001 stratified taxonomy. Fragment carries provenance (source formation, derivation chain).

**Channel Constraints:** ONT_FRAGMENT and GOVERNANCE_DIRECTIVE may not be combined in a single formation output without explicit routing through the conductor. Silent ontology mutation is a prohibited coupling.

**Invariants Preserved:** INV-000-003 (Identity Persistence — no UID destruction), INV-001-001 (Ontological Categorization — fragment must classify into exactly one category).

### SIG-002: RULE_PROPOSAL

**Definition:** A proposed governance rule, dictum amendment, or constraint revision.

**Producer Precondition:** The producing formation has governance authority — it is the conductor, a META-ORGANVM component, or an authorized agent in a SHAPE or BUILD phase.

**Signal Postcondition:** Content includes the proposed rule text, ADICO decomposition (Attribute, Deontic, aIm, Condition, Or-else per Crawford & Ostrom 1995), affected scope (organ, repo, or system-wide), and justification with evidence citation. Conforms to SPEC-005 rule structure.

**Channel Constraints:** RULE_PROPOSAL requires acknowledgment from the conductor before propagation to affected organs. Proposals without acknowledgment are buffered, not broadcast.

**Invariants Preserved:** INV-000-004 (Constitutional Supremacy — proposals may not override higher-level constraints without constitutional revision process).

### SIG-003: STATE_MODEL

**Definition:** A behavioral specification — statechart fragment, transition table, guard condition, or temporal property.

**Producer Precondition:** Producer has architectural or governance authority. STATE_MODEL signals from application-layer repos (ARCH-006) are scoped to their own behavioral specification; system-wide state models require META authority.

**Signal Postcondition:** Content conforms to the Harel statechart notation established in SPEC-004. Transition entries carry LOG-NNN identifiers. Guard conditions reference RULE-NNN or TEMP-NNN identifiers.

**Channel Constraints:** STATE_MODEL signals affecting the promotion statechart (SPEC-004 Section 1) require constitutional-level review before integration.

**Invariants Preserved:** INV-000-001 (Dependency Acyclicity — state models must not create circular behavioral dependencies).

### SIG-004: HEALTH_PULSE

**Definition:** A timestamped status report from a component or formation.

**Producer Precondition:** Any active component may emit HEALTH_PULSE. No authority constraint — observability is universal.

**Signal Postcondition:** Content is a timestamped, machine-parseable status report containing at minimum: entity UID, promotion status, CI status (if applicable), last-validated timestamp, and organism gate evaluation. Content conforms to the system-metrics schema.

**Channel Constraints:** HEALTH_PULSE has high routing priority. Attenuation policy: never attenuated — health signals are always delivered.

**Invariants Preserved:** INV-000-005 (Observability — health pulses are the primary mechanism for maintaining system-wide observability).

### SIG-005: MERGE_REQUEST

**Definition:** A proposal to merge, split, or fuse structural entities.

**Producer Precondition:** Producer has governance authority for the affected entities. Merge requests involving cross-organ entities require conductor mediation.

**Signal Postcondition:** Content includes source entity UIDs, proposed disposition (merge, split, fuse), lineage plan (which UIDs are preserved, which are created, which enter LIMINAL), and impact assessment on downstream dependencies.

**Channel Constraints:** MERGE_REQUEST must not bypass the dependency graph validator. The request is evaluated against INV-000-001 before execution.

**Invariants Preserved:** INV-000-003 (Identity Persistence — merged entities retain UIDs in lineage), INV-000-001 (Dependency Acyclicity — the resulting graph must remain a DAG).

### SIG-006: FORMATION_DECLARATION

**Definition:** A declaration of formation type, signal inputs/outputs, cadence, and attenuation policy.

**Producer Precondition:** Producer is a component asserting its formation identity. Formation declarations are self-descriptions, not external assignments.

**Signal Postcondition:** Content conforms to the formation.yaml schema. Declaration includes formation type (GENERATOR, TRANSFORMER, ROUTER, RESERVOIR, INTERFACE, LABORATORY, SYNTHESIZER), signal inputs, signal outputs, and exit conditions.

**Channel Constraints:** FORMATION_DECLARATION is consumed by the orchestration layer (ARCH-005) for routing configuration. It does not trigger governance evaluation unless the declared formation type conflicts with the entity's organ placement.

**Invariants Preserved:** INV-000-002 (Governance Reachability — formations must be reachable from the constitutional root).

### SIG-007: AESTHETIC_MODULATION

**Definition:** A signal that shapes processing behavior through aesthetic parameters — palette, typography, tone, layout patterns.

**Producer Precondition:** Producer has aesthetic authority for its organ (governed by `organ-aesthetic.yaml` in the organ's `.github/` directory).

**Signal Postcondition:** Content conforms to the organ-aesthetic schema. Modulation parameters are namespaced by organ to prevent cross-organ aesthetic collision.

**Channel Constraints:** AESTHETIC_MODULATION has low routing priority. Attenuation policy: attenuated under channel congestion — aesthetic signals are deferred when governance or health signals require bandwidth.

**Invariants Preserved:** No structural invariants directly affected. Aesthetic modulation is a modulation signal (AX-000-009), not a dependency or governance signal.

### SIG-008: CAPABILITY_OFFER

**Definition:** An announcement that an entity can perform a specific operation or provide a specific service.

**Producer Precondition:** Producer has the capability it is offering (PRIM-007 Capability). Capabilities must be grounded in implementation — declaring a capability that cannot be exercised violates the signal postcondition.

**Signal Postcondition:** Content includes entity UID, capability type, preconditions for invocation, and expected output type. The offered capability must be exercisable at the entity's current promotion status.

**Channel Constraints:** CAPABILITY_OFFER is consumed by the orchestration layer for routing decisions. Offers from ARCHIVED entities are rejected.

**Invariants Preserved:** INV-000-005 (Observability — capabilities must be observable and verifiable).

### SIG-009: RESOURCE_CLAIM

**Definition:** A claim on shared system resources — agent sessions, tool checkout slots, compute budget, context-window capacity.

**Producer Precondition:** Producer is an active agent or formation with a valid coordination handle.

**Signal Postcondition:** Content includes claim type (punch-in/out, tool checkout, budget request), resource identifier, requested duration, and weight category (light/medium/heavy per `coordination/tool_lock.py`). Claims conform to the resource capacity model (6 units for 16GB M3).

**Channel Constraints:** RESOURCE_CLAIM has medium routing priority. Claims that exceed the capacity budget are queued, not rejected.

**Invariants Preserved:** No structural invariants directly affected. Resource claims are operational, not constitutional.

### SIG-010: GOVERNANCE_DIRECTIVE

**Definition:** An authoritative instruction from the constitutional or orchestration layer.

**Producer Precondition:** Producer has governance authority — the conductor, META-ORGANVM engine, or a constitutional-level process. Application-layer repos may not emit GOVERNANCE_DIRECTIVE.

**Signal Postcondition:** Content includes directive type (promote, demote, archive, audit, freeze), target entity UIDs, authorization chain (which RULE-NNN or SPEC-NNN authorizes the directive), and expected effect.

**Channel Constraints:** GOVERNANCE_DIRECTIVE has highest routing priority. Never attenuated. Overrides all lower-priority signals in the routing queue.

**Invariants Preserved:** INV-000-004 (Constitutional Supremacy — directives must be consistent with constitutional constraints), INV-000-002 (Governance Reachability — directives must flow from constitutional roots).

### SIG-011: METRIC_OBSERVATION

**Definition:** A measured quality with timestamp, value, and bearer entity.

**Producer Precondition:** Producer has measurement authority for the observed entity — typically the engine's metrics subsystem or a CI pipeline.

**Signal Postcondition:** Content conforms to the system-metrics schema. Observation includes entity UID, metric name, measured value, timestamp, and measurement method. Values are empirical (measured from actual system state), not fabricated.

**Channel Constraints:** METRIC_OBSERVATION has medium routing priority. Observations are buffered and batched for efficiency during metric refresh cycles.

**Invariants Preserved:** INV-000-005 (Observability — metrics are the diagnostic instruments; fabricated metrics violate observability).

### SIG-012: EVENT_DISPATCH

**Definition:** A structured event payload dispatched through the event spine.

**Producer Precondition:** Producer declares the event type in its seed.yaml `produces` field. Undeclared event production violates RULE-002 (Epistemic Membranes).

**Signal Postcondition:** Content conforms to the dispatch-payload JSON Schema. Event carries source entity UID, event type, timestamp, and typed payload. Event type matches a declared `produces` edge.

**Channel Constraints:** EVENT_DISPATCH routing follows the `produces`/`consumes` edges in seed.yaml. Events are delivered only to declared consumers.

**Invariants Preserved:** INV-000-001 (Dependency Acyclicity — event routing must not create circular dependencies).

### SIG-013: CONTEXT_UPDATE

**Definition:** An update to the cross-organ context injected into agent sessions.

**Producer Precondition:** Producer is the context-sync mechanism (`contextmd/generator.py`) or an authorized META-ORGANVM process.

**Signal Postcondition:** Content is a valid CLAUDE.md, GEMINI.md, or AGENTS.md fragment. Update carries the target repo UID, the section being updated, and the new content. Content length respects the capacity budget for the target context channel (see Section 3).

**Channel Constraints:** CONTEXT_UPDATE has low routing priority. Attenuation policy: context updates are deferred under congestion. The channel capacity problem (Section 3) applies: context content must have entropy below channel capacity for reliable communication.

**Invariants Preserved:** INV-000-005 (Observability — context documents are diagnostic instruments; stale context violates observability).

### SIG-014: LINEAGE_TRACE

**Definition:** A record of structural ancestry — predecessor/successor UIDs, dissolution reason, lineage type.

**Producer Precondition:** Producer is the ontologia store or a governance process executing a merge, split, dissolution, or archival.

**Signal Postcondition:** Content conforms to the ontologia event schema. Trace includes source UIDs, target UIDs, lineage type (predecessor, successor, derived-from, merged-into), and timestamp. Every dissolved or archived entity must have at least one LINEAGE_TRACE.

**Channel Constraints:** LINEAGE_TRACE is consumed by the identity layer (ARCH-004). Traces are append-only — a lineage record, once emitted, is never revoked.

**Invariants Preserved:** INV-000-003 (Identity Persistence — lineage traces are the mechanism for preserving identity through structural change), AX-000-007 (Alchemical Inheritance — prior structural artifacts inform new constructions).

---

## 2. Produces/Consumes as Behavioral Contracts

The seed.yaml `produces`/`consumes` edges currently serve three functions: they declare signal types a repo emits and expects, they define the wiring of the communication graph, and they enable dependency graph validation. SPEC-007 adds a fourth function: they are behavioral contracts between producers and consumers, carrying the full weight of Liskov and Wing's (1994) substitutability requirement and Meyer's (1997) contract reciprocity.

### INTF-001: Producer Obligations

A repo that declares `produces: [product.release]` commits to three things:

1. **Structural postcondition:** `product.release` events will conform to the dispatch-payload schema.
2. **Behavioral postcondition:** The repo will actually emit `product.release` events when triggering conditions are met — not merely that it *can* but that it *will*.
3. **History constraint:** The repo will not unilaterally stop producing `product.release` events without a migration protocol (SPEC-008). Removing a produces edge is a postcondition weakening — a violation of Liskov's behavioral subtyping contract.

**Traces to:** Liskov & Wing 1994 (behavioral subtyping), Meyer 1997 (supplier obligations).

### INTF-002: Consumer Entitlements

A repo that declares `consumes: [product.release]` is entitled to three things:

1. **Schema conformance:** Events received conform to the dispatch-payload schema.
2. **Behavioral guarantees:** Events carry the behavioral guarantees specified in the signal class contract (SIG-012 for EVENT_DISPATCH).
3. **Contract stability:** No producer will unilaterally weaken the contract without notification through a migration protocol.

**Traces to:** Liskov & Wing 1994 (caller entitlements), Meyer 1997 (caller benefits).

### INTF-003: Contract Evolution Across Promotion

When a repo is promoted, its interface contracts evolve monotonically following Meyer's inheritance contract rule:

| Promotion Direction | Preconditions | Postconditions |
|---------------------|---------------|----------------|
| **Promotion** (CANDIDATE to PUBLIC_PROCESS) | May only be weakened (accept broader inputs) | May only be strengthened (guarantee more) |
| **Demotion** (PUBLIC_PROCESS to CANDIDATE) | May be strengthened (require more) | May be weakened (guarantee less) |

Promotion is behavioral subtyping: the promoted repo is a more reliable producer and a more tolerant consumer. Demotion reverses the direction and requires notification to all dependents whose relied-upon guarantees have been reduced.

The formal rule: promotion = `(pre_old OR pre_new)` for preconditions, `(post_old AND post_new)` for postconditions. This is Liskov-Wing covariance/contravariance expressed in Meyer's contract algebra.

**Traces to:** SPEC-004 LOG-005 through LOG-011 (promotion transitions), SPEC-003 Section 2.2 (promotion as Liskov-constrained refinement).

### INTF-004: Transitive Contract Composition

When repo A produces signal S consumed by repo B, and repo B produces signal T consumed by repo C, the transitive contract chain is:

```
A's postconditions for S  -->  ground B's preconditions for consuming S
B's postconditions for T  -->  ground C's preconditions for consuming T
```

The system-level guarantee (C can rely on T having certain properties) is derived from component-level contracts. The DAG invariant (INV-000-001) ensures this composition is well-founded: there are no circular contract dependencies, so contracts can always be satisfied in topological order.

**Traces to:** Meyer 1997 (contract composition), INV-000-001 (Dependency Acyclicity).

### INTF-005: Proposed seed.yaml Extension

The following `contracts` section transforms seed.yaml from a wiring diagram into a behavioral specification. This is the target schema extension; implementation is a Layer 3B concern.

```yaml
contracts:
  produces:
    - signal: product.release
      precondition: "promotion_status >= PUBLIC_PROCESS"
      postcondition: "event conforms to dispatch-payload.schema.json AND contains version field"
      invariant: "repo CI status remains GREEN after emission"
  consumes:
    - signal: product.release
      precondition: "consumer has active subscription in seed.yaml"
      postcondition: "consumer acknowledges receipt within timeout"
```

Each contract element maps to a Meyer DbC component. The composition rules (weaken preconditions, strengthen postconditions) provide the formal constraint on how contracts evolve across promotion levels.

**Traces to:** Meyer 1997 (Design by Contract), Szyperski 2002 (contractually specified interfaces).

---

## 3. Channel Capacity Model

Shannon's (1948) information theory provides the structural vocabulary for reasoning about ORGANVM's communication capacity. The application is ADAPTED: ORGANVM borrows Shannon's structural vocabulary (signal, channel, capacity, noise, redundancy) without claiming that Shannon's mathematical results apply quantitatively.

### INTF-010: Conductor Routing Bandwidth

The conductor's routing mechanism has finite capacity: a bounded number of signals can be processed per session. Signal priority determines which signals are processed first when demand exceeds capacity.

| Priority | Signal Classes | Attenuation |
|----------|---------------|-------------|
| **Critical** | SIG-010 (GOVERNANCE_DIRECTIVE), SIG-004 (HEALTH_PULSE) | Never attenuated |
| **High** | SIG-005 (MERGE_REQUEST), SIG-012 (EVENT_DISPATCH) | Attenuated only under severe congestion |
| **Medium** | SIG-002 (RULE_PROPOSAL), SIG-003 (STATE_MODEL), SIG-009 (RESOURCE_CLAIM), SIG-011 (METRIC_OBSERVATION), SIG-008 (CAPABILITY_OFFER) | Attenuated under moderate congestion |
| **Low** | SIG-001 (ONT_FRAGMENT), SIG-006 (FORMATION_DECLARATION), SIG-007 (AESTHETIC_MODULATION), SIG-013 (CONTEXT_UPDATE), SIG-014 (LINEAGE_TRACE) | Deferred under any congestion |

### INTF-011: Context Channel Capacity

The context-sync mechanism generates CLAUDE.md/GEMINI.md files that inject cross-organ awareness into agent sessions. These context documents are a communication channel with finite capacity: agent context windows have bounded length, and every word of context injected consumes capacity.

The channel capacity problem: context content has entropy H; the receiving agent's context window has capacity C. Reliable communication requires H < C. When context exceeds capacity, the agent loses information — distant context is degraded by positional decay characteristics of the receiving model.

**Implementation requirement:** Context documents should be generated with explicit length budgets. Signal-class prioritization determines what information is included when the budget is constrained: governance state and dependency structure before aesthetic parameters and lineage history.

### INTF-012: Redundancy and Efficiency

Shannon's insight that redundancy enables error correction has a governance analog: multiple repos producing similar signals provides resilience against single-repo failure, but at the cost of reduced efficiency and increased coordination complexity.

The entropy lens identifies over-redundant organs: organs where many repos produce the same signal class, suggesting consolidation opportunities. Under-redundant organs (single points of failure for a signal class) represent resilience risks.

---

## 4. Compatibility Rules

### INTF-020: Signal Type Compatibility

A consumer may receive a signal only if the signal's class matches a declared `consumes` entry or subscription in the consumer's seed.yaml. Undeclared signal reception violates RULE-002 (Epistemic Membranes).

### INTF-021: Promotion-Level Compatibility

A consumer at promotion level N may consume signals from producers at any promotion level >= N. A CANDIDATE consumer may consume from CANDIDATE, PUBLIC_PROCESS, or GRADUATED producers. This follows from the Liskov subtyping chain (SPEC-003 Section 2.2): higher promotion levels provide strictly stronger guarantees.

A consumer SHOULD NOT consume from producers at promotion levels below its own — the producer's weaker guarantees may not satisfy the consumer's preconditions. This is a SHOULD (norm), not a MUST (rule): legitimate exceptions exist (consuming from LOCAL development repos during testing).

### INTF-022: Cross-Organ Flow Governance

All cross-organ signal flows must satisfy:

1. **Declaration:** Both producer and consumer declare the signal type in seed.yaml.
2. **DAG compliance:** The signal flow does not create a dependency cycle in G^dep.
3. **Directionality:** Dependency-type flows follow the unidirectional rule (I to II to III). Information-type flows may be recursive (AX-000-008).
4. **Type compatibility:** The signal class matches on both sides of the edge.

Violations trigger VIOL-004 (Epistemic Membrane Violation) with the obligation chain defined in SPEC-005 Section 3.

### INTF-023: Formation Protocol Prohibited Couplings

The following signal combinations are constitutionally prohibited:

| Prohibited Coupling | Reason | Violated Principle |
|---------------------|--------|-------------------|
| Unbounded mutual recursion between formations | Deadlock risk; no convergence guarantee | INV-000-001 (acyclicity) |
| Silent ontology mutation (ONT_FRAGMENT without conductor routing) | Ontological authority bypass | AX-000-001 (Ontological Primacy) |
| Archives as hidden design authority (LINEAGE_TRACE used as governance input) | Conflates history with authority | INV-000-004 (Constitutional Supremacy) |
| Routers inventing theory (ROUTER emitting ONT_FRAGMENT) | Formation type violation | SIG-001 producer precondition |
| Laboratories bypassing migration review (LABORATORY emitting GOVERNANCE_DIRECTIVE) | Governance authority bypass | SIG-010 producer precondition |

---

## 5. Contestation Disclosures

### 5.1 Shannon's Information Theory Is Structurally Adapted

**Status:** ADAPTED (risk register).

Shannon's theory explicitly excludes semantic content — "the semantic aspects of communication are irrelevant to the engineering problem." ORGANVM's signals carry semantic content where meaning is essential. The mapping is structural and analogical: signal classes as alphabet, formation protocol as coding scheme, conductor as channel with finite capacity. ORGANVM does not compute channel capacity in Shannon's sense (bits per second); it has a bounded attention budget measured in context-window tokens and human review hours. The Shannon vocabulary names the phenomenon; the specific capacity analysis must use ORGANVM-native units.

### 5.2 Design by Contract in Distributed Governance

**Status:** ADAPTED (risk register).

Meyer's Design by Contract was designed for object-oriented software with compile-time checking. ORGANVM's contracts span independent repos communicating via events — a distributed, loosely-coupled context where contract checking is necessarily runtime and asynchronous. The DbC structure transfers (preconditions, postconditions, invariants); the enforcement mechanism requires adaptation from compile-time to governance-time verification.

### 5.3 Three Missing Contract Elements (NOVEL)

**Status:** NOVEL (risk register).

The finding that ORGANVM's current seed.yaml interfaces are structural declarations rather than behavioral contracts — lacking per-signal preconditions, behavioral postconditions, and per-repo invariants — is an empirical observation about the current schema, not a contested theoretical claim. The finding parallels SPEC-005's discovery that most governance dictums are norms (ADIC) rather than rules (ADICO). Both gaps have the same character: the system specifies *what* but not *under what conditions* and *with what guarantees*.

---

## 6. Evolution Constraints

SPEC-007 may be amended through the following governed process only.

### 6.1 Amendment Types

| Type | Definition | Requirements |
|------|-----------|-------------|
| **Conservative Refinement** | Refines an existing signal class contract (adds preconditions, strengthens postconditions, clarifies invariants). Does not add new SIG or INTF identifiers. | Adversarial review + creator sign-off |
| **Constrained Extension** | Adds new signal classes (new SIG-NNN identifiers), new interface contract elements (new INTF-NNN identifiers), or new compatibility rules. Must preserve all existing signal contracts. | Adversarial review + impact assessment on SPEC-005 (Rulebook) and SPEC-006 (Architecture Document) + creator sign-off |
| **Signal Retraction** | Removes a signal class by demonstrating it is redundant with remaining classes or no longer used. | Adversarial review + migration plan for all producers and consumers of the signal class + creator sign-off |
| **Breaking Revision** | Changes the behavioral contract of an existing signal class in ways that weaken postconditions or strengthen preconditions, violating the Liskov monotonicity principle. | New grounding narrative + adversarial review + human spot-check + review of all downstream specs + creator sign-off |

### 6.2 Permanent Identifiers

SIG identifiers (SIG-001 through SIG-014) and INTF identifiers (INTF-001 through INTF-023) are permanent. Removed items have their identifiers retired, not reassigned.

### 6.3 Versioning

The original SPEC-007 is never overwritten. Amendments are versioned: SPEC-007-v1.1, v1.2, etc.

---

## 7. Traceability

### 7.1 Upward Traceability (to SPEC-000)

| SPEC-000 Element | SPEC-007 Grounding |
|------------------|--------------------|
| AX-000-001 (Ontological Primacy) | SIG-001 — ONT_FRAGMENT requires ontological authority and conforms to SPEC-001 taxonomy |
| AX-000-004 (Constitutional Governance) | INTF-001 — producer obligations are constitutional commitments; INTF-022 — cross-organ flows require declaration |
| AX-000-005 (Evolutionary Recursivity) | Section 6 — the interface contract spec itself evolves through governed revision |
| AX-000-007 (Alchemical Inheritance) | SIG-014 — LINEAGE_TRACE preserves structural history; INTF-001 — removing a produces edge requires migration |
| AX-000-008 (Multiplex Flow Governance) | SIG-001 through SIG-014 — the 14 signal classes span all five graph layers; INTF-022 — compatibility rules differ by flow type |
| AX-000-009 (Modular Alchemical Synthesis) | SIG-006 — FORMATION_DECLARATION; SIG-007 — AESTHETIC_MODULATION as first-class constitutional operation |
| INV-000-001 (Dependency Acyclicity) | INTF-004 — transitive contract composition requires DAG; INTF-022 — cross-organ flows validated against DAG |
| INV-000-003 (Identity Persistence) | SIG-014 — lineage traces are append-only; SIG-005 — merge requests preserve UIDs |
| INV-000-004 (Constitutional Supremacy) | SIG-010 — GOVERNANCE_DIRECTIVE requires constitutional authority; INTF-023 — prohibited couplings enforce authority hierarchy |
| INV-000-005 (Observability) | SIG-004 — HEALTH_PULSE never attenuated; SIG-011 — METRIC_OBSERVATION provides diagnostic data |

### 7.2 Lateral Traceability

| Peer Spec | Connection |
|-----------|-----------|
| SPEC-001 (Ontology Charter) | ONT-019 (SignalDispatch) is the entity type for signal delivery events; ONT-034 (Data Flow) and ONT-035 (Subscription) formalize produces/consumes edges |
| SPEC-002 (Primitive Register) | Signals are PRIM-004 (Event) + PRIM-002 (Value) + PRIM-003 (Relation) compositions (Section 3.3) |
| SPEC-003 (Invariant Register) | Section 2 (Contract Model) — seed.yaml as Design by Contract; SPEC-007 extends with per-signal behavioral contracts |
| SPEC-004 (Logical Specification) | Section 1.6 (Broadcast Events) — statechart transitions generate the signals defined here |
| SPEC-005 (Rulebook) | RULE-002 (Epistemic Membranes) — undeclared cross-organ flows trigger violation handling; RULE-016 (Event Handshake) — event edges must reference cataloged types |
| SPEC-006 (Architecture Document) | ARCH-032 (Interoperability) — quality attribute scenario for cross-organ signal flow; ARCH-005 (Orchestration Layer) — routing infrastructure |

### 7.3 Downward Traceability (to implementation)

| SPEC-007 Element | Current Code Location | Alignment |
|------------------|-----------------------|-----------|
| 14 signal classes (Section 1) | Formation protocol (post-flood corpus) — taxonomy only | DRIFT — listed as types, not as behavioral contracts |
| Producer obligations (INTF-001) | `seed.yaml` produces field | DRIFT — structural declaration, no preconditions/postconditions |
| Consumer entitlements (INTF-002) | `seed.yaml` consumes field | DRIFT — structural declaration, no behavioral guarantees |
| Contract evolution (INTF-003) | `governance/state_machine.py` | PARTIAL — promotion monotonicity exists but not formalized as contract evolution |
| Transitive composition (INTF-004) | `seed/graph.py` | DRIFT — graph built but contracts not composed |
| seed.yaml contracts extension (INTF-005) | Not implemented | MISSING — target: Layer 3B schema extension |
| Channel capacity model (Section 3) | `contextmd/generator.py` | DRIFT — generates context without capacity budgeting |
| Compatibility rules (Section 4) | `governance/dependency_graph.py`, `seed/graph.py` | PARTIAL — DAG and edge validation exist; promotion-level compatibility not checked |
| Prohibited couplings (INTF-023) | Not implemented | MISSING — formation protocol not yet enforced by engine |

### 7.4 Academic Lineage

| SPEC-007 Element | Traditions | Key Sources |
|------------------|-----------|-------------|
| Promotion as behavioral subtyping | Type theory | Liskov & Wing 1994 |
| Produces/consumes as DbC | Software engineering | Meyer 1997 |
| Component model correspondence | Component-based SE | Szyperski 2002 |
| Channel capacity model | Information theory (adapted) | Shannon 1948 |
| Signal class formalization | Novel (grounded in formation protocol) | — |

Full grounding narrative: `post-flood/specs/SPEC-007/grounding.md` (4,416 words)
Full risk register: `post-flood/specs/SPEC-007/risk-register.md` (6 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
