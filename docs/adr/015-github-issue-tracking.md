# ADR-015: GitHub Issue Tracking for Omega Criteria and Sprint Catalog

## Status

Accepted

## Date

2026-03-04

## Context

The system has 17 omega completion criteria tracked in `there+back-again.md` and 48 unexecuted sprints in `sprint-catalog.md`. Prior to this decision, all tracking was purely document-based — markdown tables, revision logs, and cross-references. There was no machine-queryable work-tracking system and no way to assign, label, or filter work items.

The governance quadrilateral (roadmap + cadence + catalog + rolling TODO) provided strategic planning but lacked operational work management.

## Decision

Create GitHub issues for all non-MET omega criteria and all unexecuted sprint catalog items on `meta-organvm/organvm-corpvs-testamentvm`. Use a structured label taxonomy:

- **Omega issues** (9): One issue per horizon grouping, labeled `omega` + `horizon-N` + blocker type (`blocked:external`, `blocked:time`, `blocked:income`)
- **Sprint issues** (48): One issue per catalog item, labeled `sprint` + `cat:{category}` + relevant horizon labels
- **Code issues** on `meta-organvm/organvm-engine`: Scorecard/tooling bugs (1 initial)

All issues contain bidirectional links: issue body links to documentation, documentation links back to issue URL.

## Alternatives Considered

- **GitHub Projects board**: Rejected — adds complexity without proportional value for a solo-operated system. Issues alone provide filtering, labeling, and milestone tracking.
- **Linear/Jira**: Rejected — external tool adds vendor dependency and fragmentation. GitHub issues colocate with code.
- **Keep everything in markdown**: Rejected — no machine-queryable filtering, no assignee/label/milestone support, no notification integration.

## Consequences

- 58 issues created (57 on corpus repo, 1 on engine repo)
- 13 labels on corpus: omega, horizon-1 through horizon-5, blocked:{external,time,income}, sprint, cat:{12 categories}
- Bidirectional tracking links added to omega-evidence-map.md, there+back-again.md, sprint-catalog.md (+132 lines)
- `gh issue list` now provides operational work queue alongside `rolling-todo.md`
- Blocker labels make external dependencies visible at a glance
