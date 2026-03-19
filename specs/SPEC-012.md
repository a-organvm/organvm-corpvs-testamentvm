# SPEC-012: Repo Fusion Protocol

```
Document ID:      SPEC-012
Title:            Repo Fusion Protocol
Version:          1.0
Status:           RATIFIED
Layer:            L3B — Governance Instruments
Authoritative:    Structural Transformation
Parent Specs:     SPEC-000 (System Manifesto), SPEC-001 (Ontology Charter), SPEC-008 (Evolution & Migration Law)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/SPEC-012/grounding.md
Risk Register:    post-flood/specs/SPEC-012/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. Fusion Methodology

Repo fusion is the governed process by which two or more repositories are synthesized into a single entity through a third-location fusion chamber. Fusion is not merging git histories, not copying files, and not absorbing one repo into another. It is the ontological alignment and structural synthesis of two organizational identities into a third that preserves the lineage of both while producing emergent capability that neither possessed alone.

The fusion chamber protocol proceeds in four phases, each producing auditable governance artifacts. Every phase requires human authorization before advancing.

### FUSE-001: Inventory

**Statement:** Enumerate all modules, interfaces, data models, event types, dependency edges, and signal contracts in both source repos.

The inventory produces two structural manifests -- one per source repo -- each listing: module names and locations, public interfaces, data model schemas, event types declared in `seed.yaml`, dependency edges (upstream and downstream), signal contracts (produces/consumes), and test coverage boundaries.

The inventory must be exhaustive. Modules omitted from the inventory are invisible to the alignment phase and will be silently dropped from the fused result -- a violation of AX-000-007 (Alchemical Inheritance).

### FUSE-002: Alignment

**Statement:** Compute multi-layer similarity across the inventories to produce a candidate correspondence map.

Following Ehrig and Staab's QOM algorithm (2004), alignment computes similarity across four feature layers:

| Layer | Source Repo Artifact | Similarity Metric |
|-------|---------------------|-------------------|
| **Lexical** | Module names, function names, class names, configuration keys | String similarity (Levenshtein, Jaccard on tokens) |
| **Structural** | Directory hierarchies, package structures, import graphs | Graph isomorphism distance |
| **Extensional** | Test files, documentation, generated outputs per module | Overlap coefficient on produced artifacts |
| **Semantic** | Dependency edges, event types, signal contracts in seed.yaml | Edge-set comparison on typed graph |

The alignment process is iterative: each round's confirmed correspondences constrain subsequent rounds. Convergence occurs when no round produces new correspondences above the similarity threshold. The threshold is a governance parameter, not a hardcoded constant -- set conservatively (high similarity required) to minimize false correspondences.

The output is a correspondence map: for each pair of modules (one from each source repo), a composite similarity score classifying them as identical (retain from either), corresponding (candidates for synthesis), or unique (retain from originating repo).

### FUSE-003: Classification

**Statement:** For each correspondence in the alignment map, classify the resolution strategy.

Following Noy and Musen's PROMPT conflict taxonomy (2003), each correspondence falls into one of four conflict categories, each resolved by a specific fusion classification:

| Conflict Category | Definition | Fusion Classification |
|-------------------|-----------|----------------------|
| **Synonymy** | Same concept, different names across repos | **Retain from A** or **Retain from B** -- choose one naming convention |
| **Homonymy** | Different concepts, same name across repos | **Invent anew** -- rename at least one to eliminate ambiguity |
| **Structural mismatch** | Same domain, different granularity or hierarchy depth | **Synthesize from both** -- produce a new organization accommodating both |
| **Constraint violation** | Conflicting governance rules, incompatible schemas, contradictory dependency declarations | **Invent anew** -- create new modules satisfying both repos' requirements |

Every classification decision requires human authorization. The classification record preserves: the two modules being classified, the conflict category, the chosen resolution, the rationale, and the authorizing principal. Classification decisions are governance evidence (SPEC-002, Evidence type) and are never deleted.

### FUSE-004: Synthesis

**Statement:** Construct the fused entity in the third location according to the classification decisions.

The third-location principle (the "fusion chamber") is constitutionally mandated. Neither source repo's directory structure, naming conventions, or organizational assumptions are inherited automatically. Every element in the fused result must be explicitly placed through a FUSE-003 classification decision.

The rationale: merging repo B into repo A privileges A's structure. Third-location synthesis eliminates this bias by forcing every element to justify its inclusion on its own merits. This is grounded in ontology merging methodology -- the "merge into" approach creates structural bias where the receiving ontology's categories dominate (Noy & Musen 2003).

Synthesis produces: (a) the fused codebase in the third-location directory, (b) a new `seed.yaml` declaring the fused entity's organ membership, tier, produces/consumes edges, and event subscriptions, (c) updated dependency edges reflecting the fused entity's position in the system graph, and (d) the fusion record (see Section 2).

---

## 2. Lineage Preservation

AX-000-007 (Alchemical Inheritance) imposes a constitutional constraint: the system's prior structural states are not waste but prima materia, and no era may discard the memory of prior eras. Applied to fusion, this means both source repos' identities must survive the synthesis.

### FUSE-005: Lineage Record

**Statement:** Every fusion must produce a structured lineage record in ontologia.

The fused entity's ontologia record must contain:

| Field | Content |
|-------|---------|
| `successor_uid` | The fused entity's ULID |
| `predecessor_uids` | The UIDs of both source repos |
| `dissolution_reason` | `FUSION` with reference to the fusion protocol record |
| `dissolution_date` | Date the fusion was executed |
| `lineage_type` | `MERGE` |
| `classification_record` | Reference to the FUSE-003 classification decisions |
| `alignment_map` | Reference to the FUSE-002 correspondence map |

The source repos' UIDs are never destroyed (INV-000-003, Identity Persistence). They transition to `lifecycle_status = DISSOLVED` with lineage edges pointing to the successor. The fused entity inherits the combined lineage of both sources -- every predecessor relationship, every historical name record, every archived metric observation.

### FUSE-006: De-Fusion Provision

**Statement:** The fusion protocol must support governed splitting of a fused entity back into components.

If a fusion fails the cognitive load test in practice (the maintainer finds the fused domain unmanageable) or if the expected emergent capability fails to materialize, de-fusion produces two new UIDs with lineage edges back to the fused entity's UID. The fused entity's UID persists (INV-000-003) with `lifecycle_status = DISSOLVED` and `dissolution_reason = DEFUSION`. De-fusion is a fusion in reverse: it requires the same four-phase protocol (FUSE-001 through FUSE-004) applied to the splitting problem.

---

## 3. Cognitive Load Feasibility

Following Skelton and Pais (2019), cognitive load is the primary feasibility criterion for repo fusion. A proposed fusion may produce a perfect alignment map with all conflicts cleanly resolved, yet still be infeasible if the fused entity's cognitive load exceeds what the maintainer can sustain.

### FUSE-007: Cognitive Load Assessment

**Statement:** Every fusion proposal must include a cognitive load assessment across three dimensions before classification begins.

| Load Type | Definition | Proxy Metric |
|-----------|-----------|-------------|
| **Intrinsic** | Irreducible domain complexity of the fused entity | Combined module count, number of distinct domain concepts |
| **Extraneous** | Environmental friction from tooling, governance, context switching | Number of distinct technology stacks, build tool count, CI configuration complexity |
| **Germane** | Learning investment required to reason about the fused domain | Number of cross-domain concepts requiring simultaneous comprehension |

In ORGANVM's single-person context, there is no team to distribute load across, no specialist to absorb a complicated subsystem, no platform team to abstract away infrastructure concerns. The human must hold the fused domain in working memory as a single coherent unit. The cognitive load assessment is mandatory, not advisory.

### FUSE-008: Elevation versus Consolidation

**Statement:** A fusion is justified only if it produces elevation -- emergent capability exceeding the sum of parts. Consolidation -- reducing repo count without emergent gain -- does not justify the increased cognitive load.

The elevation threshold is: does the fused entity enable at least one operation, reasoning chain, or architectural pattern that was structurally impossible when the repos were separate? If yes, the increased cognitive load has a return. If no, the fusion is consolidation and should be reconsidered.

A stronger criterion applies for load-bearing components: the emergent capability must be load-bearing for the system as a whole, not merely convenient for the maintainer.

Elevation examples: fusing two data pipeline stages enables end-to-end type checking that was impossible across the repo boundary. Fusing a schema validator and the schema registry enables co-evolution guarantees.

Consolidation examples: fusing two repos that happen to share a programming language but serve independent domains. Fusing repos purely to reduce the total count in the registry.

Conway's Law (1968) provides the structural invariant: the "communication structure" in single-person context is the human's attention topology. A fusion that merges code without merging the corresponding cognitive workspace will decompose along the old boundary, reproducing the original split.

---

## 4. Conflict Resolution

### FUSE-009: Interaction Mode Evolution

**Statement:** Fusion is appropriate when two repos are in sustained collaboration mode; it is inappropriate when they interact only through stable service boundaries.

Following Skelton and Pais's interaction mode evolution (2019): during fusion, the two repos are in collaboration mode (high-bandwidth bidirectional communication, frequent co-changes, reciprocal signal exchange). After fusion completes and interfaces stabilize, the fused entity provides X-as-a-service to its consumers.

If two repos already interact only through stable service boundaries (well-defined APIs, no co-change coupling, no reciprocal signal exchange), the interface has already crystallized and fusion would dissolve a valuable abstraction. In such cases, fusion is structurally contraindicated regardless of the elevation assessment.

### FUSE-010: Schema and Governance Reconciliation

**Statement:** When source repos declare conflicting governance rules, incompatible schema versions, or contradictory dependency edges, resolution follows the constitutional hierarchy.

| Conflict Type | Resolution |
|---------------|-----------|
| Incompatible schema versions | The fused entity adopts the more recent schema version; backward-compatibility migration is required for the older source |
| Contradictory dependency declarations | The constitutional dependency direction (AX-000-008, INV-000-001) prevails; any edge that would create a cycle is removed |
| Conflicting governance rules | The higher-authority rule prevails per INV-000-004 (Constitutional Supremacy) |
| Incompatible promotion statuses | The fused entity enters at the lower of the two source statuses; promotion criteria must be re-satisfied |

---

## 5. Contestation Disclosures

### 5.1 Ontology Alignment Adapted to Software Repos

**Status:** ADAPTED (risk register claims #1, #2)

Ehrig and Staab's QOM and Noy and Musen's PROMPT were designed for ontology alignment in semantic web and knowledge engineering contexts, not software repository merging. The feature layers transfer structurally (labels = module names, structural position = directory hierarchy, semantic relations = event types) but the similarity metrics require domain-specific calibration. The iterative convergence model grounds the fusion chamber protocol; the specific similarity functions must be adapted from ontology concepts to software artifacts.

### 5.2 Cognitive Load in Single-Operator Context

**Status:** ADAPTED (risk register claim #3)

Skelton and Pais's cognitive load framework was designed for multi-person teams. In ORGANVM's single-operator context, "team cognitive load" reduces to "individual cognitive capacity." The three load components transfer directly. The measurement challenge is that individual cognitive load is subjective and context-dependent, while team cognitive load can be approximated by headcount and skill distribution.

### 5.3 Elevation versus Consolidation Is Novel

**Status:** NOVEL (risk register claim #5)

The distinction between elevation (emergent capability) and consolidation (count reduction) has no direct academic precedent. Baldwin and Clark's option value framework (2000) suggests the distinction implicitly but does not formalize it as a threshold. Without measurable criteria for "emergent gain," the distinction risks degenerating into post-hoc rationalization. SPEC-012 mitigates this by requiring that the emergent capability be named, described, and assessed for load-bearing status before fusion proceeds.

---

## 6. Evolution Constraints

SPEC-012 may be amended through the following governed process only.

### 6.1 Amendment Types

| Type | Definition | Requirements |
|------|-----------|-------------|
| **Conservative Refinement** | Refines existing FUSE definitions, adjusts proxy metrics, or adds detail to the classification taxonomy. Does not add new FUSE identifiers. | Adversarial review + creator sign-off |
| **Constrained Extension** | Adds new FUSE identifiers or new conflict categories. Must preserve all existing lineage requirements and cognitive load constraints. | Adversarial review + impact assessment on SPEC-008 (Evolution & Migration Law) + creator sign-off |
| **Breaking Revision** | Changes the third-location principle, modifies the lineage preservation requirements, or alters the elevation/consolidation threshold. | New grounding narrative + adversarial review + human spot-check + review of all downstream specs + creator sign-off |

### 6.2 Permanent Identifiers

FUSE identifiers (FUSE-001 through FUSE-010) are permanent. Removed items have their identifiers retired, not reassigned.

### 6.3 Versioning

The original SPEC-012 is never overwritten. Amendments are versioned: SPEC-012-v1.1, v1.2, etc.

---

## 7. Traceability

### 7.1 Upward Traceability (to SPEC-000)

| SPEC-000 Element | SPEC-012 Grounding |
|------------------|--------------------|
| AX-000-003 (Individual Primacy) | FUSE-007 -- cognitive load assessment ensures fusion does not overwhelm the individual practitioner |
| AX-000-004 (Constitutional Governance) | FUSE-001 through FUSE-004 -- every fusion step requires human authorization |
| AX-000-005 (Evolutionary Recursivity) | Section 6 -- the fusion protocol itself evolves through governed revision |
| AX-000-006 (Topological Plasticity) | FUSE-008 -- fusion is a governed topological operation; elevation justifies structural change |
| AX-000-007 (Alchemical Inheritance) | FUSE-005 -- lineage preservation is constitutionally mandated; prior structures are prima materia |
| AX-000-008 (Multiplex Flow Governance) | FUSE-010 -- dependency direction and DAG acyclicity constrain conflict resolution |
| INV-000-001 (Dependency Acyclicity) | FUSE-010 -- any edge creating a cycle is removed during reconciliation |
| INV-000-003 (Identity Persistence) | FUSE-005, FUSE-006 -- source UIDs are never destroyed; de-fusion preserves fused UID |
| INV-000-004 (Constitutional Supremacy) | FUSE-010 -- higher-authority rules prevail in governance conflicts |

### 7.2 Lateral Traceability

| Peer Spec | Connection |
|-----------|-----------|
| SPEC-001 (Ontology Charter) | Fused entities are Continuant entities (ONT-001) with ULID-based identity; lineage records are Occurrent events |
| SPEC-002 (Primitive Register) | Fusion classification decisions are Constraints (PRIM-006) over the State (PRIM-005) of two repos |
| SPEC-003 (Invariant Register) | INV-000-003 (Identity Persistence) constrains FUSE-005; INV-000-001 (DAG Acyclicity) constrains FUSE-010 |
| SPEC-004 (Logical Specification) | Fusion changes promotion status (LOG-004 archive for source repos, LOG-003 LOCAL entry for fused entity) |
| SPEC-005 (Rulebook) | RULE-001 (DAG Invariant) enforced during FUSE-010 reconciliation |
| SPEC-008 (Evolution & Migration Law) | Fusion is a Breaking Revision requiring migration records per SPEC-008 |
| INST-ERA (Era Model) | Fusion that triggers organ-level restructuring may constitute an era transition trigger |

### 7.3 Downward Traceability (to implementation)

| SPEC-012 Element | Current Code Location | Alignment |
|------------------|-----------------------|-----------|
| Fusion protocol (Sections 1-2) | Not implemented | MISSING -- no fusion tooling exists |
| Lineage records (FUSE-005) | `ontologia/store.py` lineage edges | PARTIAL -- lineage system exists but not wired to fusion operations |
| Cognitive load assessment (FUSE-007) | Not implemented | MISSING -- no cognitive load metrics |
| Elevation threshold (FUSE-008) | Not implemented | MISSING -- no automated assessment |
| Classification taxonomy (FUSE-003) | Not implemented | MISSING -- no classification tooling |

### 7.4 Academic Lineage

| SPEC-012 Element | Traditions | Key Sources |
|------------------|-----------|-------------|
| Multi-layer alignment | Ontology mapping | Ehrig & Staab 2004 |
| Conflict taxonomy and interactive merging | Knowledge engineering | Noy & Musen 2003 |
| Cognitive load feasibility | Organizational design | Skelton & Pais 2019 |
| Structural invariant (communication topology) | Systems design | Conway 1968 |
| Elevation vs. consolidation | (Novel) | Informed by Baldwin & Clark 2000 |

Full grounding narrative: `post-flood/specs/SPEC-012/grounding.md` (3,037 words)
Full risk register: `post-flood/specs/SPEC-012/risk-register.md` (6 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
