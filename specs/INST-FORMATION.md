# INST-FORMATION: Formation Protocol

```
Document ID:      INST-FORMATION
Title:            Formation Protocol
Version:          1.0
Status:           RATIFIED
Layer:            L3B — Governance Instruments
Authoritative:    Formation Classification and Signal Architecture
Parent Specs:     SPEC-000 (System Manifesto), SPEC-001 (Ontology Charter), SPEC-005 (Rulebook)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/formation-protocol/grounding.md
Risk Register:    post-flood/specs/formation-protocol/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. Formation Types

A formation type classifies a repository by its operational character -- what it does in the system's signal architecture -- orthogonally to organ membership (where it sits) and promotion status (how mature it is). Each formation type corresponds to a structural configuration in Mintzberg's organizational theory (1979): a pattern of internal organization determined by which function dominates, which coordination mechanism prevails, and what contingency factors apply.

Formation type must be derived from a repo's actual contingency factors (position in the dependency graph, environmental stability, technical complexity, output cadence), not assigned by fiat. Misassignment -- declaring a formation type that does not match the repo's operational reality -- produces structural misfit (Mintzberg 1979) and is detectable through governance audit.

Each formation carries a `formation.yaml` declaration specifying: formation type, signal inputs/outputs, cadence, attenuation policy, feedback/feedfront paths, and exit conditions.

### FORM-001: GENERATOR

**Mintzberg analogue:** Adhocracy.
**Dominant function:** Novel artifact production.
**Coordination mechanism:** Mutual adjustment among creative processes.
**Contingency profile:** High environmental complexity, low predictability, creative technical system.
**Signal profile:** Irregular output cadence, high-variety output types, low-volume high-value signals.

GENERATOR formations produce novel artifacts through open-ended exploration. Their outputs carry maximum variety and must be attenuated before entering downstream TRANSFORMER or ROUTER formations, because raw creative output carries too much variety for standardized processing.

**ORGANVM examples:** Theoretical research repos (ORGAN-I), generative art engines (ORGAN-II).

### FORM-002: TRANSFORMER

**Mintzberg analogue:** Professional bureaucracy.
**Dominant function:** Input-to-output conversion via specialized process.
**Coordination mechanism:** Standardization of skills (the transformation algorithm).
**Contingency profile:** Moderate complexity, stable transformation logic, variable input.
**Signal profile:** Regular cadence, type-preserving or type-converting signals.

TRANSFORMER formations apply a specialized process to their inputs and produce transformed outputs. They may apply feedback to their own transformation logic based on output quality metrics -- a self-modifying professional bureaucracy that Mintzberg's static model does not anticipate.

**ORGANVM examples:** Data pipeline stages (alchemia-ingestvm), schema validators (schema-definitions).

### FORM-003: ROUTER

**Mintzberg analogue:** Machine bureaucracy.
**Dominant function:** Signal dispatch and distribution.
**Coordination mechanism:** Standardization of work processes (routing rules).
**Contingency profile:** High throughput, low domain complexity, stable routing topology.
**Signal profile:** High-volume, type-preserving, predictable cadence.

ROUTER formations dispatch signals according to declared rules. They are constitutionally prohibited from inventing theory or generating novel content -- they may only route signals, never modify signal content. This prohibition is constitutive, not regulative: a ROUTER that generates content has ceased to be a ROUTER and requires reclassification.

**ORGANVM examples:** Event dispatchers, ORGAN-IV orchestration components.

### FORM-004: RESERVOIR

**Mintzberg analogue:** Divisionalized form.
**Dominant function:** Accumulation and stable provision of artifacts.
**Coordination mechanism:** Standardization of outputs (data products with stable interfaces).
**Contingency profile:** Low volatility, high consumer count, storage orientation.
**Signal profile:** Demand-driven output cadence, stable interface contracts.

RESERVOIR formations buffer the productive core from demand volatility (Thompson 1967). They absorb irregular production schedules and provide stable, on-demand access to accumulated artifacts. Their interfaces are stable service boundaries: downstream consumers treat the RESERVOIR as an X-as-a-service provider.

**ORGANVM examples:** Registry corpus (organvm-corpvs-testamentvm), schema-definitions, knowledge bases.

### FORM-005: INTERFACE

**Mintzberg analogue:** Boundary-spanning unit.
**Dominant function:** Translation between internal and external signal vocabularies.
**Coordination mechanism:** Standardization of skills (protocol expertise).
**Contingency profile:** External environment interface, translation complexity, protocol diversity.
**Signal profile:** Bidirectional, protocol-converting.

INTERFACE formations manage the system's relationship with its environment, translating between internal signal classes and external protocols. They must attenuate external signals to prevent environmental volatility from propagating into the system's productive core. Without INTERFACE buffering, external perturbations propagate directly into GENERATOR and LABORATORY formations, disrupting the mutual adjustment processes they depend on.

**ORGANVM examples:** MCP server (organvm-mcp-server), stakeholder portal, distribution endpoints (ORGAN-VII).

### FORM-006: LABORATORY

**Mintzberg analogue:** Adhocracy (experimental variant).
**Dominant function:** Hypothesis testing and provisional artifact production.
**Coordination mechanism:** Mutual adjustment with explicit provisionality constraints.
**Contingency profile:** High uncertainty, low stakes (outputs not yet load-bearing), exploratory scope.
**Signal profile:** Irregular cadence, provisional output type, explicit exit conditions.

LABORATORY formations are constitutionally distinct from GENERATOR formations in one respect: their outputs are provisional. LABORATORY outputs must not bypass migration review when promoted to production status (SPEC-008), preventing untested provisional artifacts from becoming load-bearing without governance authorization. Exit conditions in `formation.yaml` govern the transition: when specified conditions are met (or violated), the formation's type must be reassessed against its actual contingency factors.

**ORGANVM examples:** Experimental repos in INCUBATOR or LOCAL status.

### FORM-007: SYNTHESIZER

**Mintzberg analogue:** No single analogue (composite configuration).
**Dominant function:** Integrative production combining inputs from multiple formations.
**Coordination mechanism:** Mutual adjustment (internal) combined with standardized interfaces (external).
**Contingency profile:** Cross-domain scope, integrative complexity, multiple upstream dependencies.
**Signal profile:** Multiple input types, synthesized output type, variable cadence.

SYNTHESIZER formations are inherently cross-configurational -- they combine elements of adhocracy (creative integration), professional bureaucracy (domain-specific processing), and divisionalized form (stable output interfaces). The SYNTHESIZER is the formation protocol's genuinely NOVEL contribution: no single Mintzberg configuration accommodates integrative functions that cross configuration boundaries.

**ORGANVM examples:** system-dashboard (synthesizes registry, metrics, ontologia data), organvm-engine (synthesizes across all governance domains).

---

## 2. Signal Coupling Rules

Inter-formation communication is governed by Thompson's interdependence typology (1967). The coupling rules classify how tightly formations must be coordinated based on the character of their signal exchange.

### FORM-008: Interdependence Classification

| Interdependence Type | Coordination Mechanism | Signal Character | Coupling Cost |
|---------------------|----------------------|-----------------|---------------|
| **Pooled** | Standardization (shared rules, common formats) | Context-setting: formations share organ membership and governance rules without direct signal exchange | Low |
| **Sequential** | Plan or schedule (produces/consumes edges in seed.yaml) | Unidirectional: output of formation A is input of formation B, with no feedback | Medium |
| **Reciprocal** | Mutual adjustment (frequent bidirectional communication) | Bidirectional: formations exchange outputs mutually, each modifying the other's processing | High |

Thompson's clustering principle determines organ boundaries: formations with reciprocal interdependence should share the same organ. Formations with only sequential interdependence can be in different organs connected by explicit edges. Formations with only pooled interdependence can be in different organs without operational consequence.

The dependency DAG constraint (AX-000-008, INV-000-001) prohibits cross-organ reciprocal interdependence by design: the unidirectional dependency rule makes cross-organ bidirectional signal exchange architecturally impossible.

### FORM-009: Prohibited Couplings

The following couplings are constitutionally prohibited. Each represents reciprocal interdependence that exceeds the system's coordination capacity -- the Thompson boundary beyond which coordination cost exceeds coordination capacity.

| Prohibition | Rationale | Violated Principle |
|------------|-----------|-------------------|
| **Unbounded mutual recursion** | Reciprocal interdependence without convergence: each round of exchange generates more exchange, with no stable state. Coordination cost is unbounded. | Thompson: coordination must converge |
| **Silent ontology mutation** | A formation changing ontological categories without governance notification. Violates the standardization mechanism that pooled interdependence requires. | Thompson: pooled interdependence requires standardization |
| **Archives as hidden design authority** | A RESERVOIR covertly influencing design decisions without declaring the dependency edge. Converts pooled interdependence into covert sequential interdependence. | Thompson: interdependence must be declared |
| **Routers inventing theory** | A ROUTER generating novel content, converting its standardized work process into an adhocratic creative process. Violates the formation's constitutional role. | Mintzberg: configuration must match contingency |
| **Laboratories bypassing migration review** | A LABORATORY promoting outputs directly to production without SPEC-008 migration governance. | AX-000-004: no operation without constitutional authorization |

---

## 3. The 14 Canonical Signal Classes

Every inter-formation signal must belong to one of 14 canonical signal classes. Each class carries an implicit interdependence type (Section 2) that determines its coupling cost and coordination requirements.

### FORM-010: Signal Class Register

**Unidirectional classes (sequential interdependence):**

| Signal Class | Producer | Consumer | Content |
|-------------|----------|----------|---------|
| `METRIC_OBSERVATION` | Any formation with metrics | Dashboard, organism, audit | Quantitative measurement at a point in time |
| `EVENT_DISPATCH` | Any formation emitting events | Event subscribers declared in seed.yaml | State change notification |
| `AUDIT_FINDING` | Governance audit | Formation under audit | Compliance assessment result |
| `ERA_MARKER` | Constitutional authority (META) | All formations | Era transition boundary signal |
| `LINEAGE_RECORD` | Ontologia, fusion protocol | Any formation tracing history | Identity continuity record |

**Bidirectional classes (reciprocal interdependence):**

| Signal Class | Initiator | Responder | Content |
|-------------|-----------|-----------|---------|
| `RULE_PROPOSAL` | Any formation | Governance authority | Proposed governance change (requires accept/reject) |
| `PROMOTION_REQUEST` | Repository owner | Governance authority | State transition request (requires authorize/deny) |
| `PATCH_INSTRUCTION` | Taxis (ORGAN-IV) | Target formation | Routing change directive (requires confirm/fail) |

**Context-setting classes (pooled interdependence):**

| Signal Class | Source | Audience | Content |
|-------------|--------|----------|---------|
| `CONTEXT_PAYLOAD` | Context sync (contextmd) | All formations in scope | Generated CLAUDE.md / AGENTS.md content |
| `SCHEMA_ARTIFACT` | Schema-definitions | All formations consuming schemas | JSON Schema definition or update |
| `FORMATION_DECLARATION` | Any formation | System-wide registry | formation.yaml content declaring type, signals, cadence |

**Generative classes (formation-specific):**

| Signal Class | Typical Producer | Content |
|-------------|-----------------|---------|
| `ONT_FRAGMENT` | GENERATOR, LABORATORY | Novel ontological concept or theoretical artifact |
| `STATE_MODEL` | Any formation tracking state | Complete state snapshot of an entity or subsystem |
| `SIGNAL_ATTENUATION` | INTERFACE, ROUTER | Attenuation policy declaration (what fraction of signal variety is preserved) |

### FORM-011: Signal Class Extensibility

The 14 canonical signal classes are an open set, not a closed enumeration. New signal classes may be added through a Constrained Extension amendment (Section 7) when operational use reveals communication needs that no existing class accommodates. The hospitality principle (Ranganathan 1967) applies: adding a new signal class must not require reclassifying signals already assigned to existing classes.

Completeness is demonstrable only empirically: every actual inter-formation data flow should map to at least one signal class. Governance audits should flag unclassifiable signals as evidence of taxonomic strain.

---

## 4. Formation Lifecycle

### FORM-012: Lifecycle States

Every formation traverses a three-stage lifecycle:

**Spawn.** A formation is spawned when a new repository is created with a `formation.yaml` declaring its type, signal inputs/outputs, cadence, attenuation policy, and exit conditions. Spawning is governed by the standard promotion pipeline (SPEC-004): the formation enters at INCUBATOR or LOCAL status.

**Operate.** The formation performs its declared function, producing and consuming signals according to its type classification and coupling rules. During operation, the formation's contingency factors may drift from its declared type -- a LABORATORY may accumulate production dependencies, a GENERATOR may settle into predictable cadence. Exit conditions in `formation.yaml` detect this drift.

**Crystallize or Dissolve.** When exit conditions are triggered:
- **Reclassification:** The formation's type is reassessed against its actual contingency factors (Conway 1968, flexibility principle). A LABORATORY that has matured into a production dependency is reclassified as GENERATOR or TRANSFORMER.
- **Dissolution:** The formation is archived per the promotion pipeline (SPEC-004 LOG-004, LOG-007, LOG-013, LOG-014). Its lineage is preserved per AX-000-007.
- **Crystallization:** In rare cases, a formation's outputs become so structurally irreducible that it qualifies for organ crystallization (Section 5).

### FORM-013: Exit Conditions

Each `formation.yaml` must declare exit conditions -- the circumstances under which the formation's current type must be reassessed. Exit conditions are Constraints (SPEC-002 PRIM-006) over the formation's operational State (SPEC-002 PRIM-005).

Exit condition examples:
- A LABORATORY producing outputs consumed by more than 3 downstream formations triggers reclassification review
- A GENERATOR whose output cadence has been regular for 90+ consecutive days triggers assessment of TRANSFORMER reclassification
- A ROUTER accumulating more than 100 lines of domain logic triggers TRANSFORMER reclassification review
- A RESERVOIR with zero consumers for 90+ days triggers dissolution review

---

## 5. Formation-to-Organ Crystallization

AX-000-006 (Topological Plasticity) declares that ORGANVM's organ topology is a governed variable. The formation protocol specifies the mechanism by which topological change occurs: crystallization from formation activity.

### FORM-014: Crystallization Conditions

All three conditions must be satisfied simultaneously:

**Structural irreducibility.** The formation's outputs are consumed by formations across multiple existing organs, and no existing organ's domain subsumes the formation's function. The formation occupies a structural position that is not reducible to an existing organ's scope.

**Load-bearing dependency.** Other formations depend on the candidate formation so heavily that its failure would cascade across organ boundaries. Measured by dependency fan-out and signal consumption frequency. A formation consumed by a single organ is part of that organ; a formation consumed across three or more organs is a candidate for independence.

**Cognitive distinctness.** The formation's domain requires sufficiently specialized attention that treating it as a sub-unit of an existing organ imposes unsustainable cognitive load (Skelton & Pais 2019). The maintainer experiences the formation as a separate domain, not as a sub-function of its current organ.

### FORM-015: Crystallization Governance

Organ crystallization -- promotion from formation-within-an-organ to organ-in-its-own-right -- is a constitutional act. It requires:

1. Evidence of structural irreducibility, load-bearing dependency, and cognitive distinctness (FORM-014)
2. Classification as a Constrained Extension under SPEC-000 Section 9 (adds a new organ while preserving all existing invariants)
3. Adversarial review by a different agent or model
4. Impact assessment on all downstream specs
5. Human principal authorization

Crystallization does not constitute an era transition in itself -- it is a within-era topological adjustment, provided it does not alter the system's deep structure (authority stack, dependency direction, identity system). If crystallization triggers a cascade requiring restructuring of the authority stack or reversal of dependency direction, it becomes a trigger for era transition, handled by INST-ERA.

---

## 6. Contestation Disclosures

### 6.1 Mintzberg Configurations Adapted to Software Repos

**Status:** ADAPTED (risk register claims #1, #4)

Mintzberg's five structural configurations emerge from contingency factors in human organizations. ORGANVM's seven formation types are declared in `formation.yaml` by the human operator, not emergent from organizational dynamics. The contingency principle transfers (formation type should match the repo's position, stability, and complexity), but the mechanism differs: Mintzberg's configurations emerge organically; ORGANVM's are constitutionally declared. This creates a misassignment risk if the declared type drifts from contingency reality. Exit conditions (FORM-013) mitigate this by detecting drift.

### 6.2 The SYNTHESIZER Has No Clean Analogue

**Status:** NOVEL (risk register)

The SYNTHESIZER formation type crosses configuration boundaries deliberately. Its theoretical justification rests on the empirical observation that integrative functions exist (organvm-engine is a fact, not a hypothesis) and require a formation type acknowledging their cross-configurational character. No single Mintzberg configuration accommodates this role.

### 6.3 Signal Class Completeness Is Empirical

**Status:** NOVEL (risk register claim #3)

The 14 signal classes are a domain-specific vocabulary without external validation. Their completeness is an empirical question: do they cover all actual inter-formation communication needs? Completeness can be demonstrated operationally (no unclassifiable signals exist in practice) but cannot be proven theoretically (new communication needs may emerge). The signal alphabet must be extensible (FORM-011).

### 6.4 Conway's Law as Cognitive Ergonomics

**Status:** ADAPTED (risk register claim #4)

Conway's Law was formulated for multi-person organizations where communication structure is observable. For a single operator, "communication structure" is internal cognitive allocation, which is subjective and hard to measure. The risk is that formation type becomes aspirational rather than descriptive, producing formations that are structurally well-defined but operationally inert.

---

## 7. Evolution Constraints

INST-FORMATION may be amended through the following governed process only.

### 7.1 Amendment Types

| Type | Definition | Requirements |
|------|-----------|-------------|
| **Conservative Refinement** | Refines existing FORM definitions, adds detail to formation types, adjusts exit condition examples. Does not add new FORM identifiers. | Adversarial review + creator sign-off |
| **Constrained Extension** | Adds new FORM identifiers, new formation types, or new signal classes. Must preserve all existing signal coupling rules and prohibited couplings. | Adversarial review + impact assessment on SPEC-007 (Interface Contract Spec) and INST-TAXONOMY + creator sign-off |
| **Breaking Revision** | Changes the formation type set, modifies prohibited couplings, or alters the crystallization conditions. | New grounding narrative + adversarial review + human spot-check + review of all downstream specs + creator sign-off |

### 7.2 Permanent Identifiers

FORM identifiers (FORM-001 through FORM-015) are permanent. Removed items have their identifiers retired, not reassigned.

### 7.3 Versioning

The original INST-FORMATION is never overwritten. Amendments are versioned: INST-FORMATION-v1.1, v1.2, etc.

---

## 8. Traceability

### 8.1 Upward Traceability (to SPEC-000)

| SPEC-000 Element | INST-FORMATION Grounding |
|------------------|--------------------------|
| AX-000-003 (Individual Primacy) | FORM-014 cognitive distinctness -- formation boundaries must respect the individual's cognitive capacity |
| AX-000-004 (Constitutional Governance) | FORM-009 -- prohibited couplings are constitutive constraints, not optional guidelines |
| AX-000-005 (Evolutionary Recursivity) | Section 7 -- the formation protocol itself evolves through governed revision; FORM-012 lifecycle includes reclassification |
| AX-000-006 (Topological Plasticity) | FORM-014, FORM-015 -- crystallization pathway is the mechanism for governed topological evolution |
| AX-000-007 (Alchemical Inheritance) | FORM-012 -- dissolved formations preserve lineage |
| AX-000-008 (Multiplex Flow Governance) | FORM-008, FORM-010 -- signal classes are typed edges in the multiplex graph; coupling rules govern each flow type independently |
| AX-000-009 (Modular Alchemical Synthesis) | FORM-010 -- signal classes are the signal vocabulary; coupling rules govern compatibility; attenuation is a first-class operation |
| INV-000-001 (Dependency Acyclicity) | FORM-008 -- cross-organ reciprocal interdependence is architecturally impossible under the DAG constraint |
| INV-000-005 (Observability) | FORM-010 -- every signal flow must be observable through the event spine and temporal metric fabric |

### 8.2 Lateral Traceability

| Peer Spec | Connection |
|-----------|-----------|
| SPEC-001 (Ontology Charter) | Formations are Continuant entities (ONT-001); signal flows are Occurrent events |
| SPEC-002 (Primitive Register) | Formation types are Constraints (PRIM-006) over signal Capabilities (PRIM-007); exit conditions are Constraints over States (PRIM-005) |
| SPEC-003 (Invariant Register) | INV-000-001 (DAG) constrains cross-organ coupling; INV-000-009 (Signal Observability) requires signal flow recording |
| SPEC-004 (Logical Specification) | Formation lifecycle maps to promotion statechart; crystallization governance invokes SPEC-000 Section 9 |
| SPEC-005 (Rulebook) | Prohibited couplings decomposable into ADICO rules with explicit Or-else chains |
| SPEC-007 (Interface Contract Spec) | Signal classes define the typed edges that SPEC-007 formalizes as interface contracts |
| SPEC-012 (Repo Fusion Protocol) | Fusing two formations requires reconciling their formation types and signal architectures |
| INST-TAXONOMY (Functional Taxonomy) | Formation type is orthogonal to functional class; a GENERATOR may be classified as ENGINE, FRAMEWORK, or EXPERIMENT |
| INST-ERA (Era Model) | Crystallization may trigger era transition if it alters deep structure |

### 8.3 Downward Traceability (to implementation)

| INST-FORMATION Element | Current Code Location | Alignment |
|------------------------|-----------------------|-----------|
| Formation types (Section 1) | Not implemented | MISSING -- no `formation.yaml` schema, no type classification |
| Signal coupling rules (Section 2) | `seed.yaml` produces/consumes edges | PARTIAL -- edges declared but not typed by interdependence category |
| Signal classes (Section 3) | Not implemented | MISSING -- no signal class vocabulary in seed.yaml schema |
| Prohibited couplings (FORM-009) | Partially enforced by `governance/dependency_graph.py` (DAG acyclicity) | DRIFT -- only acyclicity enforced; other prohibitions not checked |
| Formation lifecycle (Section 4) | Promotion pipeline (`governance/state_machine.py`) | PARTIAL -- promotion exists but not linked to formation type |
| Crystallization (Section 5) | Not implemented | MISSING -- no automated detection of crystallization conditions |
| Exit conditions (FORM-013) | Not implemented | MISSING -- no formation.yaml exit condition schema |

### 8.4 Academic Lineage

| INST-FORMATION Element | Traditions | Key Sources |
|------------------------|-----------|-------------|
| Formation types as structural configurations | Organizational theory | Mintzberg 1979 |
| Signal coupling rules | Interdependence typology | Thompson 1967 |
| Communication topology constraint | Systems design | Conway 1968 |
| Cognitive load in crystallization | Organizational design | Skelton & Pais 2019 |
| Signal class extensibility | Classification theory | Ranganathan 1967 |

Full grounding narrative: `post-flood/specs/formation-protocol/grounding.md` (3,571 words)
Full risk register: `post-flood/specs/formation-protocol/risk-register.md` (6 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
