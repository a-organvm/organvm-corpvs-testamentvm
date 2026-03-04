# ADR-016: Post-Construction Operational Shift

## Status

Accepted

## Date

2026-03-04

## Context

The system transitioned from construction to operation on 2026-02-11 (launch). For 22 days post-launch, the system continued operating under construction-era governance rules:
- Promotion rules designed for building out organs (promote-to-art, promote-to-commerce)
- Schema version at 0.5 despite 15+ days of stable production use
- Constitution unamended since ratification
- Governance rules JSON containing unenforced construction-era gates

The CONSTITUTIO, SCHEMA-EVOLUTIO, and REGULA sprints were designed to formalize the post-construction reality.

## Decision

1. **Schema v1.0.0**: Formalize all 6 JSON schemas from 0.1.0 to 1.0.0. Constrain `schema_version` enum in registry schema. Update all references.
2. **Constitutional Amendment E**: Acknowledge construction-era articles (III, IV) and amendments (A, C) as SATISFIED/COMPLETED. Add first post-launch review record.
3. **Governance rules update**: Mark construction-era promotion rules as archival context. Update audit thresholds for operational reality.
4. **ADR series 015-016**: Document the tracking and operational decisions made during this transition.

## Alternatives Considered

- **Leave governance unchanged**: Rejected — construction-era rules create confusion when they don't match operational reality.
- **Major version bump (v2.0)**: Rejected — no breaking changes, just formalization of stable contracts.
- **Delete construction-era rules**: Rejected — they have archival value documenting the build methodology.

## Consequences

- Schema-definitions package at v1.0.0 with frozen enum for schema_version
- Constitution at v1.1.0 with Amendment E and first review record
- Clear separation between "construction complete" items and "ongoing operational" requirements
- Post-launch review cadence established (next review: after stranger test or 60-day mark)
