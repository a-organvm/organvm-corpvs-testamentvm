# INST-TAXONOMY: Functional Taxonomy

```
Document ID:      INST-TAXONOMY
Title:            Functional Taxonomy
Version:          1.0
Status:           RATIFIED
Layer:            L3B — Governance Instruments
Authoritative:    Repository Classification
Parent Specs:     SPEC-000 (System Manifesto), SPEC-001 (Ontology Charter), SPEC-005 (Rulebook)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/functional-taxonomy/grounding.md
Risk Register:    post-flood/specs/functional-taxonomy/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. The 10-Class System

The functional taxonomy classifies every repository by its operational role in the system's architecture -- what it *does* -- orthogonally to organ membership (where it sits) and promotion status (how mature it is). Each class names a distinct function in the system's constitutional architecture. Assignment of a functional class carries governance consequences: which CI requirements apply, what documentation is expected, what promotion criteria are checked, and how the repo appears in system-level reporting.

This taxonomy is not a neutral description but active governance infrastructure (Bowker & Star 1999). Assigning a repo as INFRASTRUCTURE rather than APPLICATION changes how that repo is governed, what is expected of it, and how visible it is in system views. Every classification decision distributes obligations and expectations.

### TAXON-001: CHARTER

**Function:** Establishes constitutional foundations, axioms, invariants, and system identity.
**Governance character:** Highest authority -- changes propagate system-wide. Conservative Refinement and adversarial review required for all modifications.
**Canonical instances:** SPEC corpus (organvm-corpvs-testamentvm), post-flood constitutional corpus.
**Distinguishing criterion:** The repo defines what the system *is*, not what it *does* or *produces*.

### TAXON-002: CORPUS

**Function:** Accumulates, organizes, and provides structured access to knowledge, documents, or records.
**Governance character:** Referential integrity, completeness metrics, cross-referencing discipline.
**Canonical instances:** Knowledge bases (ORGAN-I), research archives, curated source collections.
**Distinguishing criterion:** The repo's primary value is its accumulated content, not its processing capability.

### TAXON-003: FRAMEWORK

**Function:** Provides reusable abstractions, libraries, or scaffolding that other repos build upon.
**Governance character:** API stability, backward compatibility, dependency management -- downstream consumers depend on the framework's interface contracts.
**Canonical instances:** Schema-definitions, reusable library packages, shared utility modules.
**Distinguishing criterion:** Other repos import from or extend this repo. Changing its interface has downstream consequences.

### TAXON-004: ENGINE

**Function:** Performs computation, transformation, or orchestration as the system's active processing core.
**Governance character:** Test coverage, performance monitoring, correctness verification.
**Canonical instances:** organvm-engine, generative processing engines, pipeline processors.
**Distinguishing criterion:** The repo computes, transforms, or orchestrates -- it is the system doing work.

### TAXON-005: APPLICATION

**Function:** Provides user-facing interfaces, tools, or products designed for direct interaction.
**Governance character:** Usability, accessibility, deployment requirements, user documentation.
**Canonical instances:** Stakeholder portal, public-facing web applications, CLI tools intended for external users.
**Distinguishing criterion:** The repo has end users beyond the system operator. Its quality criteria include user experience.

### TAXON-006: INFRASTRUCTURE

**Function:** Provides foundational services that the system depends on but users do not interact with directly.
**Governance character:** Reliability, availability, observability -- failure has cascading consequences.
**Canonical instances:** CI configurations, MCP servers, deployment pipelines, monitoring tooling.
**Distinguishing criterion:** The repo is load-bearing for system operations. Its failure disrupts other repos.

### TAXON-007: ASSURANCE

**Function:** Provides verification, validation, testing, or quality assurance services.
**Governance character:** Coverage metrics, false-positive/negative rates, verification methodology.
**Canonical instances:** Test frameworks, soak-test infrastructure, governance audit tooling.
**Distinguishing criterion:** The repo's purpose is to verify that other repos meet their obligations.

### TAXON-008: ARCHIVE

**Function:** Preserves historical records, dissolved entities, and prior-era artifacts.
**Governance character:** Immutability (ARCHIVE contents are read-only), referential integrity of lineage records, accessibility for future consultation.
**Canonical instances:** materia-collider (dissolved repo content), archived data collections.
**Distinguishing criterion:** The repo's content is historical. It is consulted, not modified. Per AX-000-007, it carries prima materia for future transformations.

### TAXON-009: EXPERIMENT

**Function:** Tests hypotheses, explores possibilities, and produces provisional outputs not yet committed to production.
**Governance character:** Time-bounded (exit conditions required), provisional status clearly marked, migration review required before any output becomes load-bearing.
**Canonical instances:** Repos in INCUBATOR or early LOCAL status, proof-of-concept implementations.
**Distinguishing criterion:** The repo's outputs are explicitly provisional. It explores, not produces.

### TAXON-010: OPERATIONS

**Function:** Manages runtime operational concerns: deployment, monitoring, incident response, environment configuration.
**Governance character:** Operational reliability, runbook completeness, environment consistency.
**Canonical instances:** Deployment scripts, environment configurations, operational runbooks.
**Distinguishing criterion:** The repo exists to operate the system, not to build or define it.

---

## 2. Faceted Extension (Ranganathan)

### TAXON-011: The Enumerative Limitation

The current taxonomy is enumerative: 10 classes are listed, and each repo is assigned to exactly one. Ranganathan (1967) identifies the structural limitation: enumerative classification cannot accommodate multi-role entities without either proliferating compound classes (CHARTER-CORPUS-ARCHIVE) or accepting information loss (assigning only the dominant class).

Evidence of limitation in the current system:
- `organvm-engine` is simultaneously ENGINE (it computes), FRAMEWORK (other tools build on it), and INFRASTRUCTURE (the system depends on it)
- `organvm-corpvs-testamentvm` is simultaneously CHARTER (it establishes constitutional foundations), CORPUS (it accumulates knowledge), and ARCHIVE (it preserves historical records)
- `system-dashboard` is simultaneously APPLICATION (it provides a user interface) and INFRASTRUCTURE (system observability depends on it)

These repos are not misclassified -- they are **boundary objects** (Bowker & Star 1999) whose multi-world membership is a structural feature, not a classification failure.

### TAXON-012: Multi-Facet Extension Pathway

Ranganathan's analytico-synthetic method prescribes decomposing classification into independent facets and recombining them via a facet formula. Mapped to ORGANVM's existing classification dimensions using Ranganathan's PMEST categories:

| PMEST Category | Current Coverage | Extension |
|---------------|-----------------|-----------|
| **Personality** (focal function) | Functional class (10 values) | Primary + secondary class assignment |
| **Matter** (substrate) | Not classified | Implementation substrate: Python, TypeScript, Docs-only, Schema, Mixed |
| **Energy** (operational mode) | Not classified | Operational mode: batch, real-time, event-driven, on-demand, continuous, dormant |
| **Space** (location) | Organ membership (8+META) | Already implemented |
| **Time** (lifecycle) | Promotion status (5 states) | Already implemented |

The extension adds two new facet dimensions (Matter and Energy) and enriches the existing Personality facet (primary + secondary class). Each facet is independently governed: Matter determines build tooling and linting configuration, Energy determines performance and monitoring requirements, Space determines organ-specific governance, Time determines promotion-gated obligations, and Personality determines functional-class-specific governance.

### TAXON-013: Staged Migration

The migration from enumerative to analytico-synthetic classification is staged, not immediate:

**Era 1 (current):** The taxonomy operates enumeratively. Each repo receives a single primary functional class. The `tier` field (flagship, standard, infrastructure, archive) provides a rough second facet. A `secondary_class` field may be added to the registry schema to accommodate the most acute boundary-object cases without restructuring the entire classification system.

**Triggered by torque accumulation:** When classification torque (Section 3) becomes a measurable governance problem -- repos systematically receiving governance inappropriate to their actual function -- the taxonomy migrates to full analytico-synthetic classification with independent facets for function, mode, substrate, and scope.

This staged approach respects both Ranganathan's theoretical prescription (multi-facet classification is structurally superior) and Bowker and Star's practical caution (premature restructuring of infrastructure creates its own disruption).

---

## 3. Boundary Objects and Classification Torque

### TAXON-014: Boundary Object Recognition

Three categories of boundary objects appear in ORGANVM's registry:

**Cross-functional boundary objects.** Repos whose primary function spans two or more functional classes. These repos serve different functions for different consumers: `organvm-engine` is an ENGINE when invoked as a CLI tool, a FRAMEWORK when imported as a library, and INFRASTRUCTURE when its health determines system viability.

**Cross-organ boundary objects.** Repos whose function is defined by their relationship to multiple organs rather than to one. The MCP server has META organ membership but functionally serves all organs as an INTERFACE. Schema-definitions has META organ membership but is consumed by every organ as a FRAMEWORK. These repos' functional classification depends on which organ's perspective is adopted.

**Temporal boundary objects.** Repos whose functional class changes over time as they mature. A repo that begins as EXPERIMENT, proves its concept, and becomes load-bearing INFRASTRUCTURE without ever being formally reclassified. The repo's classification at any moment may be accurate, but its trajectory across classes creates a temporal boundary-object status.

For each category, the appropriate response differs. Cross-functional boundary objects need multi-facet classification (TAXON-012). Cross-organ boundary objects need organ-relative classification. Temporal boundary objects need classification review triggers (governance events that prompt reclassification assessment when operational character diverges from declared class).

### TAXON-015: Classification Torque

Torque (Bowker & Star 1999) is the strain experienced by entities classified in ways that conflict with their actual function.

A repo classified as EXPERIMENT that has become load-bearing INFRASTRUCTURE experiences classification torque: its governance treatment (experimental, provisional, low-stakes) conflicts with its operational reality (critical, depended-upon, high-stakes). Torque has practical consequences -- the repo may not receive the CI requirements, test coverage expectations, or documentation standards that its actual role demands.

Torque detection signals:
- Repos frequently reclassified (more than once per era)
- Repos whose governance audit findings systematically mismatch their declared class
- Functional classes growing asymmetrically (one class accumulating repos while others stagnate)
- Repos whose `tier` field conflicts with their functional class (infrastructure-tier repo classified as EXPERIMENT)

Classification torque is a governance diagnostic, not merely an intellectual concern. When torque accumulates, the taxonomy is failing to serve its governance function.

---

## 4. Naturalization Risks

### TAXON-016: Naturalization Vectors

When a classification system becomes so embedded in practice that its categories feel inevitable rather than constructed, it has been *naturalized* (Bowker & Star 1999). Naturalization is simultaneously the mark of successful infrastructure (the classification works so well that no one notices it) and a danger (the classification's biases become invisible).

Three naturalization vectors are currently active:

**Governance coupling.** As more governance rules reference functional class (promotion criteria varying by class, CI requirements conditioned on class, documentation expectations keyed to class), the taxonomy becomes load-bearing infrastructure. Changing a class definition requires updating every governance rule that references it -- creating path-dependent resistance to taxonomic evolution.

**Tooling reification.** CLI commands, dashboard views, and reporting templates embed functional class as a filter or grouping dimension. `organvm registry list --class ENGINE` creates an expectation that ENGINE is a permanent, stable category. The tooling becomes a constituency for the status quo.

**Cognitive habituation.** As the operator internalizes the 10-class vocabulary, it becomes the default frame for thinking about new repos. "Is this an ENGINE or a FRAMEWORK?" becomes the instinctive question, foreclosing alternatives outside the taxonomy's vocabulary.

### TAXON-017: Denaturalization Practice

Mitigation requires deliberate denaturalization -- periodic exercises in questioning the taxonomy's categories, testing its boundaries, and examining its consequences.

Governance audits should include a classification strain assessment:
- Which repos have been reclassified most frequently?
- Which classifications are most frequently contested during promotion review?
- Which functional classes are growing fastest relative to others?
- Do any repos resist classification into any of the 10 classes?

These are Bowker and Star's residual-category signals adapted to ORGANVM's context. The era model (INST-ERA) provides the natural intervention point: era transitions, as moments of constitutional revision, are the appropriate occasions for taxonomic reassessment. A new era may bring a new taxonomy -- or may confirm the existing one with the renewed authority of explicit review rather than passive inheritance.

---

## 5. Hospitable Notation

### TAXON-018: Extension Protocol

Following Ranganathan's canon of hospitality (1967), the notation system must accommodate new functional classes without restructuring existing notation.

Adding an 11th functional class requires:
1. Demonstrating that the proposed class is not a compound of existing classes (it names a genuinely irreducible function)
2. Demonstrating that existing repos are experiencing classification torque that the new class would resolve
3. Assigning a new TAXON-0NN identifier without renumbering existing identifiers
4. Reviewing all governance rules that reference functional class for impact
5. Filing as a Constrained Extension amendment (Section 7)

Adding a new facet dimension (e.g., Matter or Energy from TAXON-012) requires:
1. Demonstrating that the facet captures governance-relevant variation not captured by existing facets
2. Defining the facet's value set as an open list with its own extension protocol
3. Specifying which governance obligations the new facet triggers
4. Filing as a Constrained Extension amendment (Section 7)

---

## 6. Contestation Disclosures

### 6.1 Enumerative Classification Is a Reasonable Starting Point

**Status:** GROUNDED (risk register claims #1, #4, #5)

Ranganathan's critique of enumerative classification is well-validated: single-assignment systems lose information for multi-role entities. However, enumerative classification has practical advantages (simplicity, decisiveness, precedent) that justify its use as a first-era starting point. The staged migration pathway (TAXON-013) resolves the tension by accepting the current limitation while providing a governed evolution path.

### 6.2 Classification as Active Infrastructure

**Status:** GROUNDED (risk register claim #2)

Bowker and Star's finding that classification systems shape the world they purport to describe applies without adaptation to ORGANVM's taxonomy. The taxonomy is literally a classification system governing institutional behavior. The governance consequences attached to each class (CI requirements, documentation expectations, promotion criteria) are exactly the kind of constitutive effects Bowker and Star analyze.

### 6.3 Naturalization Risk in Single-Operator Context

**Status:** ADAPTED (risk register claim #6)

Bowker and Star's naturalization concept was developed for large-scale institutional classification systems (ICD, racial categories, nursing classifications). ORGANVM's taxonomy is small-scale and single-operator, which reduces the social consequences of naturalization but does not eliminate the cognitive risk: the operator may stop questioning whether the categories still serve the system's mission. Periodic denaturalization (TAXON-017) mitigates this.

### 6.4 PMEST Applied to Software Repos

**Status:** ADAPTED (risk register claim #7)

PMEST was designed for library classification of knowledge subjects, not software repositories. The mapping (Personality = domain function, Matter = implementation substrate, Energy = operational mode, Space = organ location, Time = lifecycle phase) is structural analogy, not direct application. Whether all five dimensions are necessary for ORGANVM is an empirical question. The Energy facet (batch vs. real-time vs. event-driven) is the most promising independent addition.

---

## 7. Evolution Constraints

INST-TAXONOMY may be amended through the following governed process only.

### 7.1 Amendment Types

| Type | Definition | Requirements |
|------|-----------|-------------|
| **Conservative Refinement** | Refines existing TAXON definitions, adjusts distinguishing criteria, or adds torque detection signals. Does not add new TAXON identifiers. | Adversarial review + creator sign-off |
| **Constrained Extension** | Adds new functional classes (new TAXON identifiers) or new facet dimensions. Must demonstrate that the extension resolves measurable classification torque. Must preserve hospitality (TAXON-018). | Adversarial review + impact assessment on SPEC-005 (Rulebook) and registry schema + creator sign-off |
| **Breaking Revision** | Changes the class set (removing, merging, or splitting classes), changes the assignment model (enumerative to faceted), or modifies the governance consequences of class membership. | New grounding narrative + adversarial review + human spot-check + review of all downstream specs + creator sign-off |

### 7.2 Permanent Identifiers

TAXON identifiers (TAXON-001 through TAXON-018) are permanent. Removed items have their identifiers retired, not reassigned.

### 7.3 Versioning

The original INST-TAXONOMY is never overwritten. Amendments are versioned: INST-TAXONOMY-v1.1, v1.2, etc.

---

## 8. Traceability

### 8.1 Upward Traceability (to SPEC-000)

| SPEC-000 Element | INST-TAXONOMY Grounding |
|------------------|-------------------------|
| AX-000-003 (Individual Primacy) | TAXON-015 -- classification torque that imposes inappropriate governance burdens violates individual primacy |
| AX-000-004 (Constitutional Governance) | TAXON-001 through TAXON-010 -- functional class determines governance obligations; classification is constitutive, not decorative |
| AX-000-005 (Evolutionary Recursivity) | Section 7 -- the taxonomy itself evolves through governed revision; TAXON-013 defines the staged migration pathway |
| AX-000-006 (Topological Plasticity) | TAXON-016 -- naturalization risk: if the taxonomy constrains what kinds of repos can exist, it constrains topological evolution |
| AX-000-007 (Alchemical Inheritance) | TAXON-008 (ARCHIVE) -- prior-era artifacts are preserved, not discarded; ARCHIVE is a constitutionally mandated class |
| INV-000-004 (Constitutional Supremacy) | TAXON-001 (CHARTER) -- CHARTER-class repos carry highest constitutional authority |
| INV-000-005 (Observability) | TAXON-015, TAXON-017 -- classification torque and denaturalization are observability requirements for the taxonomy itself |

### 8.2 Lateral Traceability

| Peer Spec | Connection |
|-----------|-----------|
| SPEC-001 (Ontology Charter) | Functional class is a Value (PRIM-002) attached to Repo entities (ONT-006) |
| SPEC-002 (Primitive Register) | Classification decisions are Constraints (PRIM-006) over the State (PRIM-005) of repos |
| SPEC-003 (Invariant Register) | Functional class is a governed property; invalid classifications violate governance reachability (INV-000-002) |
| SPEC-005 (Rulebook) | Governance obligations vary by functional class; RULE-008 (Factory Gate) is class-conditional |
| INST-FORMATION (Formation Protocol) | Formation type is orthogonal to functional class: a GENERATOR formation may be ENGINE, FRAMEWORK, or EXPERIMENT class |
| INST-ERA (Era Model) | Era transitions are the governed occasions for taxonomic denaturalization (TAXON-017) |

### 8.3 Downward Traceability (to implementation)

| INST-TAXONOMY Element | Current Code Location | Alignment |
|-----------------------|-----------------------|-----------|
| 10-class system (Section 1) | Not implemented as registry field | MISSING -- `tier` field provides rough approximation but is not the functional taxonomy |
| Boundary object recognition (TAXON-014) | Not implemented | MISSING -- no multi-class assignment support |
| Torque detection (TAXON-015) | Not implemented | MISSING -- no reclassification tracking or torque metrics |
| Faceted extension (TAXON-012) | Not implemented | MISSING -- registry schema has no facet fields beyond organ and tier |
| Denaturalization (TAXON-017) | Not implemented | MISSING -- no classification strain assessment in governance audit |
| Hospitable notation (TAXON-018) | Not implemented | MISSING -- no extension protocol in governance tooling |

### 8.4 Academic Lineage

| INST-TAXONOMY Element | Traditions | Key Sources |
|-----------------------|-----------|-------------|
| Enumerative vs. analytico-synthetic classification | Library classification theory | Ranganathan 1967 |
| PMEST facet categories | Classification science | Ranganathan 1967 |
| Canon of hospitality | Notation design | Ranganathan 1967 |
| Classification as infrastructure | Science and technology studies | Bowker & Star 1999 |
| Boundary objects | Infrastructure studies | Bowker & Star 1999 |
| Torque and naturalization | Critical classification studies | Bowker & Star 1999 |

Full grounding narrative: `post-flood/specs/functional-taxonomy/grounding.md` (3,524 words)
Full risk register: `post-flood/specs/functional-taxonomy/risk-register.md` (7 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
