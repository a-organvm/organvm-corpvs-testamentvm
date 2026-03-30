# IRF Institutional Reform — From Flat File to Proper Institution

**Date:** 2026-03-30
**Authority:** Functional Institutional Set (genesis doc) — the IRF must satisfy all 10 institutional requirements
**Relates:** IRF-SYS-023 (DONE-ID collision), IRF-MON-008 (DONE-ID collision, earlier report)
**Status:** SPEC — ready for implementation

---

## Problem Statement

The IRF (Index Rerum Faciendarum) is a flat markdown file acting as a universal work registry. It fails the Functional Institutional Set requirements:

| Institutional Requirement | Current State | Failure |
|--------------------------|---------------|---------|
| Authority (who may write) | Anyone, no protocol | Race conditions between parallel sessions |
| Memory (what gets recorded) | One-liner descriptions | Insufficient spec — items lack criteria, context, acceptance definition |
| Enforcement (rules are binding) | None | Agents ignore, duplicate, or contradict entries |
| Interfaces (how it connects) | Manual 10-index checklist | No automation, no bidirectional links |
| Persistence (survives iterations) | Markdown on disk | DONE-IDs collide, history unreliable |

Specific failures:
1. **ID collision**: DONE-186 appears 7x, DONE-184 5x, DONE-185 4x — parallel sessions independently increment
2. **Multi-agent confusion**: No protocol for how Claude, Gemini, OpenCode should read/write the IRF
3. **Items too shallow**: A one-line description is not a spec — no acceptance criteria, no GitHub issue, no project board placement

## Architecture: GitHub Issues as Source of Truth

**Core insight:** GitHub Issues already solve every problem the IRF has:
- Atomic IDs (issue numbers are auto-incremented, no collision possible)
- Multi-agent write support (API handles concurrency)
- Rich spec format (markdown body with templates)
- Project board integration (GitHub Projects v2)
- State tracking (open/closed, labels, milestones)
- Cross-referencing (mention any issue from any repo)
- Searchable, filterable, API-accessible

**The IRF.md becomes a summary view, not the source of truth.** The source of truth moves to GitHub Issues on `meta-organvm/organvm-corpvs-testamentvm`.

### Issue Template (per IRF item)

```yaml
name: IRF Work Item
description: Universal work registry item — every IRF entry must be a fully-specced issue
title: "IRF-{PREFIX}-{NNN}: {title}"
labels: ["irf"]
body:
  - type: input
    id: irf-id
    attributes:
      label: IRF ID
      description: "Unique identifier (e.g., IRF-SYS-024)"
    validations:
      required: true
  - type: dropdown
    id: priority
    attributes:
      label: Priority
      options:
        - P0 — NOW (human-gated or zero-cost)
        - P1 — SOON (next session, clear path)
        - P2 — GROWTH (extends capability)
        - P3 — HORIZON (future, needs design)
    validations:
      required: true
  - type: dropdown
    id: organ
    attributes:
      label: Target Organ
      options:
        - SYSTEM (cross-organ)
        - ORGAN-I (Theoria)
        - ORGAN-II (Poiesis)
        - ORGAN-III (Ergon)
        - ORGAN-IV (Taxis)
        - ORGAN-V (Logos)
        - ORGAN-VI (Koinonia)
        - ORGAN-VII (Kerygma)
        - META-ORGANVM
    validations:
      required: true
  - type: textarea
    id: telos
    attributes:
      label: Telos (per AX-7)
      description: "Why does this work need to exist? What ideal does it serve?"
    validations:
      required: true
  - type: textarea
    id: specification
    attributes:
      label: Specification
      description: "Full spec: what needs to be done, acceptance criteria, constraints"
    validations:
      required: true
  - type: textarea
    id: done-criteria
    attributes:
      label: Done Criteria
      description: "Checkboxes — what must be true for this to be DONE?"
      value: |
        - [ ] criterion 1
        - [ ] criterion 2
        - [ ] criterion 3
    validations:
      required: true
  - type: input
    id: owner
    attributes:
      label: Owner
      description: "Agent | Human | Human+Agent"
    validations:
      required: true
  - type: input
    id: source
    attributes:
      label: Source
      description: "What discovered this work? (session ID, audit, vacuum fill, etc.)"
    validations:
      required: true
  - type: input
    id: blocker
    attributes:
      label: Blocker
      description: "What blocks this? (None, or reference to blocking item)"
  - type: textarea
    id: growth-trajectory
    attributes:
      label: Growth Trajectory
      description: "Where does this fit in the larger arc? What does it unlock? What signal closure edges does it fulfill?"
```

### Project Board Structure

One GitHub Projects v2 board: **"Index Rerum Faciendarum"** on `meta-organvm`

Columns (status field):
- **VACUUM** — discovered gap, not yet specced
- **SPECCED** — fully specified with done criteria
- **IN PROGRESS** — actively being worked
- **REVIEW** — work done, needs verification
- **DONE** — closed with evidence
- **ARCHIVED** — superseded or no longer relevant

Views:
- **By Priority** — P0/P1/P2/P3 swimlanes
- **By Organ** — organ-grouped kanban
- **By Agent** — who's working what (prevents collision)

### Multi-Agent Protocol

```
WRITE PROTOCOL (for any agent — Claude, Gemini, OpenCode):

1. BEFORE creating an IRF item:
   - Search existing issues: `gh search issues "IRF-" --repo meta-organvm/organvm-corpvs-testamentvm`
   - Check if the work is already tracked (prevent duplicates)

2. TO CREATE an IRF item:
   - Create GitHub issue using the template
   - All required fields must be populated (telos, spec, done criteria, owner, source)
   - Label with `irf` + priority label + organ label

3. TO CLAIM an IRF item (start work):
   - Assign yourself (agent name in comment)
   - Move to IN PROGRESS on project board
   - No two agents may work the same item simultaneously

4. TO COMPLETE an IRF item:
   - Check ALL done-criteria boxes
   - Add completion comment with: commit SHA, session ID, evidence
   - Close the issue
   - The 10-index propagation checklist runs as part of closure

5. DONE-IDs:
   - ABOLISHED. Issue numbers are the IDs.
   - Historical DONE-NNN entries in IRF.md are frozen — no new DONE-NNNs ever.
   - Completion is tracked by GitHub issue closure, not by markdown entry.
```

### Migration Plan

1. **Phase 0: Template** — Create `.github/ISSUE_TEMPLATE/irf-work-item.yml` in organvm-corpvs-testamentvm
2. **Phase 1: Project Board** — Create GitHub Projects v2 board (requires `read:project` + `project` token scope — human action)
3. **Phase 2: Forward migration** — All NEW IRF items go to GitHub Issues only
4. **Phase 3: Back-migration** — Existing P0/P1 items in IRF.md get created as issues
5. **Phase 4: IRF.md becomes generated** — `organvm irf sync` reads GitHub Issues and regenerates IRF.md as a summary view
6. **Phase 5: CLI integration** — `organvm irf create`, `organvm irf claim`, `organvm irf done` wrappers around `gh issue`

### What This Fixes

| Problem | Solution |
|---------|----------|
| DONE-ID collision | GitHub issue numbers (atomic, auto-increment) |
| Multi-agent race conditions | GitHub API handles concurrency; claim protocol prevents double-work |
| Items too shallow | Issue template enforces telos, spec, done criteria |
| No project board | GitHub Projects v2 with priority/organ/agent views |
| No growth trajectory | Template field linking item to cascade plan and signal closure |
| 10-index propagation forgotten | Issue closure template includes checklist |
| IRF.md grows forever | Becomes a generated summary view, not the source |

### Token Scope Requirement

Current `GITHUB_TOKEN` lacks `read:project` scope. To create/manage GitHub Projects v2:
- Add `read:project` and `project` scopes at https://github.com/settings/tokens
- Or re-authenticate: `gh auth refresh -s project`

### Blocking Requirement

Phase 1 (Project Board creation) requires human action for token scope. Phases 0, 2, 3 can proceed with current token.
