# INST-VARIABLE-RESOLUTION: Variable Resolution Engine

```
Document ID:      INST-VARIABLE-RESOLUTION
Title:            Variable Resolution Engine
Version:          1.0
Status:           RATIFIED
Layer:            L4A — Sensing & Observation
Authoritative:    Scope Cascade and Variable Inheritance
Parent Specs:     SPEC-000 (System Manifesto), SPEC-002 (Primitive Register)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/variable-resolution/grounding.md
Risk Register:    post-flood/specs/variable-resolution/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. Purpose

A variable observed at one scope is a measurement. The same variable resolved across multiple scopes is knowledge. Test coverage of 85% at repo level is a data point. That metric resolved at organ level to reveal a 62% aggregate, at system level to show a three-month trajectory from 45% to 62%, and at global level to benchmark against comparable standards -- this is knowledge.

The variable resolution engine implements this scope cascade computationally. Variables declared in seed.yaml at repo level are resolved through a six-scope hierarchy, each scope adding contextual meaning through aggregation and comparison. The architecture implements the Combination phase of Nonaka and Takeuchi's (1995) SECI model -- explicit-to-explicit knowledge reconfiguration -- while participating in the broader knowledge creation cycle through session contexts (Socialization/Externalization) and dashboard-driven behavior change (Internalization).

**Risk profile: 20% GROUNDED, 60% ADAPTED, 20% NOVEL.**

---

## 2. Scope Hierarchy

### VAR-001: Six Resolution Scopes

Variables are resolved through six scopes, ordered from most specific to most general:

| Scope | Level | Description | Resolution Source |
|-------|-------|-------------|------------------|
| `COMPUTED` | 0 | Derived from other variables by formula | Expression evaluation over resolved inputs |
| `SESSION` | 1 | Valid for the current agent session only | Session context, CLAUDE.md injection |
| `MODULE` | 2 | Scoped to a sub-package within a repo | Module-level seed.yaml or excavation data |
| `REPO` | 3 | Scoped to a single repository | seed.yaml, CI results, filesystem inspection |
| `ORGAN` | 4 | Scoped to all repos in an organ | Aggregation over repo-level values |
| `GLOBAL` | 5 | Scoped to the entire system or external benchmarks | Cross-organ composition, external references |

The scope numbers establish the resolution order: narrower scopes are checked first. If a variable is defined at `REPO` scope and also at `ORGAN` scope, the `REPO` value takes precedence for that specific repo; the `ORGAN` value serves as the aggregate for repos that do not declare their own.

### VAR-002: Scope Inheritance

Variables cascade downward through the scope hierarchy. A variable declared at `ORGAN` scope but not at `REPO` scope is inherited by all repos in that organ. A variable declared at `GLOBAL` scope but not at `ORGAN` scope is inherited by all organs.

**Inheritance rules:**

1. **Override:** A variable declared at a narrower scope overrides the inherited value from a wider scope for that entity only.
2. **Inherit:** An entity that does not declare a variable inherits the value from the nearest enclosing scope that declares it.
3. **Undefined:** If no scope in the hierarchy declares the variable, it is undefined. Undefined variables produce a resolution error, not a silent default.
4. **Computed variables** (`COMPUTED` scope) may reference variables at any scope. Their resolution is lazy: inputs are resolved first, then the expression is evaluated.

---

## 3. Resolution Algorithm

### VAR-003: Resolution Procedure

Given a variable name `V` and an entity `E` (repo, organ, module, or system), the resolution algorithm proceeds:

```
resolve(V, E):
  1. If E has a COMPUTED definition for V:
       resolve all inputs, evaluate expression, return result
  2. If the current session defines V for E:
       return session value
  3. If E is a module and E's module scope defines V:
       return module value
  4. If E is a repo (or E's enclosing repo) and E's seed.yaml defines V:
       return repo value
  5. If E's organ defines V at organ scope:
       return organ value
  6. If V is defined at global scope:
       return global value
  7. Resolution error: V is undefined for E
```

### VAR-004: Aggregation at Scope Boundaries

When resolving a variable at organ scope, the engine computes an aggregate over all repos in the organ that have repo-level values. The aggregation function is declared in the variable definition:

| Variable Type | Aggregation Function | Example |
|---------------|---------------------|---------|
| Numeric gauge | Mean, median, min, max | `test_count`: mean across repos |
| Boolean property | Count-true / count-total | `has_ci`: fraction of repos with CI |
| Enum value | Frequency distribution | `promotion_status`: histogram |
| Rate (delta) | Weighted sum | `test_growth_rate`: sum of repo-level growth rates |

The aggregation function is part of the variable's schema definition, not chosen at query time. This ensures consistency: the same variable resolved at the same scope always uses the same aggregation.

### VAR-005: Cross-Scope Composition

System-level variables are composed from organ-level aggregates:

| Composition Mode | Formula | Use Case |
|-----------------|---------|----------|
| **Unweighted mean** | mean(organ_values) | Cross-organ comparison (equal weight per organ) |
| **Repo-weighted mean** | sum(organ_value * organ_repo_count) / total_repos | System-wide average respecting organ size |
| **Tier-weighted mean** | sum(organ_value * tier_weight) / sum(tier_weights) | Governance-weighted: flagships count more |
| **Min/max** | min(organ_values), max(organ_values) | Identify weakest/strongest organ |

---

## 4. Variable Declaration

### VAR-006: Variable Definition Schema

Each variable is defined with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `name` | String | Canonical variable name (snake_case) |
| `type` | Enum | `gauge`, `counter`, `delta`, `boolean`, `enum` |
| `scope` | Enum | `GLOBAL`, `ORGAN`, `REPO`, `MODULE`, `SESSION`, `COMPUTED` |
| `aggregation` | Enum | `mean`, `median`, `min`, `max`, `count_ratio`, `frequency`, `sum`, `weighted_mean` |
| `composition` | Enum | `unweighted_mean`, `repo_weighted`, `tier_weighted`, `min`, `max` |
| `leverage_level` | Int (1-12) | Meadows leverage hierarchy position (see INST-TEMPORAL-METRICS) |
| `reference_mode` | Enum | Expected temporal pattern: `monotonic`, `s_shaped`, `oscillating`, `goal_seeking` |
| `source` | String | Where the raw value is obtained (filesystem, CI API, registry field, formula) |
| `expression` | String | null | For COMPUTED variables: formula referencing other variables |

### VAR-007: Variable Registry

All declared variables are maintained in a variable registry. The registry is a governed artifact: variables may be added (constrained extension) but never removed. Deprecated variables remain in the registry with `deprecated: true` and a deprecation date. The registry enables:

- Discovery: what variables exist and at what scopes
- Schema validation: incoming observations match declared types
- Audit: tracing variable resolution chains for governance review

---

## 5. Consumer Projections

### VAR-008: Scope-Appropriate Consumers

Different consumers need variables resolved at different scopes:

| Consumer | Primary Scope | Purpose |
|----------|--------------|---------|
| Developer working on a repo | REPO, MODULE | Local context for implementation decisions |
| CLAUDE.md context injection | REPO, SESSION | Agent context for session-scoped work |
| Organ governance review | ORGAN | Cross-repo comparison within domain |
| Dashboard health view | ORGAN, GLOBAL | System overview with organ-level drill-down |
| MCP server queries | All scopes | Flexible resolution for diverse agent queries |
| Omega scorecard | GLOBAL | System-wide maturity assessment |
| Heartbeat gestalt | GLOBAL | Compressed system health signal |

### VAR-009: Resolution Caching

Resolved values are cached at each scope boundary with a freshness window. The cache is invalidated when:

1. A new observation is recorded for any input variable
2. The freshness window expires (configurable per variable, default: same as observation cadence)
3. A governance operation modifies the aggregation or composition function

Cache invalidation propagates upward: a new repo-level observation invalidates the organ-level cache for that organ, which invalidates the system-level cache.

---

## 6. Implementation Status

| Component | Status | Location |
|-----------|--------|----------|
| Variable resolution engine | PARTIAL | `organvm-engine/src/organvm_engine/metrics/variables.py` |
| Scope cascade (REPO -> ORGAN -> GLOBAL) | PARTIAL | Three-level resolution implemented; MODULE and SESSION scopes not yet |
| COMPUTED variables | MISSING | Expression evaluation not implemented |
| Variable registry schema | MISSING | Target: `schema-definitions/schemas/variable-definition.schema.json` |
| Aggregation functions | PARTIAL | Implicit in `variables.py`; not declared per-variable |
| Cross-scope composition | PARTIAL | System-level composition exists but composition modes not configurable |

---

## 7. Failure Modes

| Failure | Violated Element | Detection |
|---------|-----------------|-----------|
| Undefined variable (no scope provides a value) | VAR-003 step 7 | Resolution error returned; surfaced in dashboard |
| Scope conflict (same variable at same scope for same entity with different values) | VAR-001 | Schema validation: uniqueness constraint on (variable, scope, entity) |
| Aggregation mismatch (flow variable aggregated as stock) | VAR-004, MET-001/002 | Type check: variable type must match aggregation function |
| Stale cache serving outdated values | VAR-009, INV-000-005 | Freshness check: cache timestamp vs. latest observation |
| Circular COMPUTED variable reference | VAR-003 step 1 | Cycle detection in COMPUTED expression dependency graph |

---

## 8. Evolution Constraints

INST-VARIABLE-RESOLUTION may be amended through the governed process defined in SPEC-000 Section 9. New scopes may be added between existing scopes (constrained extension) but the relative ordering of existing scopes must be preserved. The six-scope hierarchy may be extended but not contracted. Variable definitions may be refined but not weakened.

---

## 9. Traceability

```
SPEC-000 AX-000-002 (Organizational Closure) → VAR-003 (resolution algorithm is a constitutive process)
SPEC-002 PRIM-002 (Value) → VAR-006 (variables are typed values with declared semantics)
SPEC-003 INV-000-005 (Observability) → VAR-008 (consumer projections enable accurate reporting)
INST-TEMPORAL-METRICS → VAR-006 (variable types align with metric types: gauge/counter/delta)
INST-TEMPORAL-METRICS MET-009/010 → VAR-004/005 (rollup rules implement scope cascade)
INST-HEARTBEAT → VAR-008 (heartbeat gestalt consumes GLOBAL-scope variables)
```

Full grounding narrative: `post-flood/specs/variable-resolution/grounding.md` (3,156 words)
Full risk register: `post-flood/specs/variable-resolution/risk-register.md` (5 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
