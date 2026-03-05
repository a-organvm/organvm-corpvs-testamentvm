# Concordance Quick Reference

> Single-page cheat sheet. Full definitions: [`concordance.md`](./concordance.md)

## Prefixes & Namespaces

| Prefix | Namespace | Source |
|--------|-----------|--------|
| `X1`--`X4` | P0 TODO: hermetic seal breakers | rolling-todo.md |
| `E1`--`E5` | P1 TODO: external engagement | rolling-todo.md |
| `M1-II`--`M6-II` | P2 TODO: system quality | rolling-todo.md |
| `S1-II`--`S6-II` | P3 TODO: strategic | rolling-todo.md |
| `G1`--`G3` | TODO: setup/infrastructure | rolling-todo.md |
| `#1`--`#17` | Omega criteria (graduation gate) | there+back-again.md |
| `H1`--`H5` | Horizons (parallel timelines) | there+back-again.md |
| `AP-1`--`AP-7` | Anti-patterns (construction traps) | operational-cadence.md |
| `W/SP/BS/LC/BL/ET/LO`+`-II` | E2G-II audit findings | e2g-ii-action-items.md |
| `01`--`33` | Completed sprint numbers | docs/specs/sprints/ |

## Top 10 Most-Referenced IDs

| ID | Meaning | Status |
|----|---------|--------|
| `#8` | >= 1 ORGAN-III product live | MET |
| `#5` | >= 1 application submitted | MET |
| `#6` | AI-conductor essay published | MET |
| `#1` | 30-day soak test passes | IN PROGRESS |
| `#17` | 30+ days autonomous operation | IN PROGRESS |
| `X1` | Submit Google Creative Lab Five | OPEN |
| `AP-1` | Don't start another named sprint | Anti-pattern |
| `AP-7` | Don't confuse motion with progress | Anti-pattern |
| `H1` | Horizon: Prove It Works (days 1--30) | Active |
| `H3` | Horizon: Generate Revenue (days 30--180) | Active |

## CLI Lookup

```bash
python3 scripts/invoke.py X1              # single ID
python3 scripts/invoke.py --namespace omega   # all omega criteria
python3 scripts/invoke.py --tag INCOME        # filter by constraint
python3 scripts/invoke.py --search "stranger" # full-text search
```

## Key Cross-References

- **Omega <-> TODO:** concordance.md "Cross-Reference: Omega <- TODO"
- **Findings -> Actions:** e2g-ii-action-items.md cross-ref table
- **Sprint history:** concordance.md "Sprints" table (33 completed)

---
*Derived from concordance.md. Updated 2026-03-04.*
