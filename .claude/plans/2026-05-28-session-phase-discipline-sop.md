# Plan — Session-Phase Discipline SOP

**Date:** 2026-05-28
**Status:** ACTIVE
**Scope:** corpvs (`a-organvm/organvm-corpvs-testamentvm`)
**Walking-through-protocol-itself**: this plan + the SOP it produces is a dogfood demonstration of the ceremony the SOP codifies.

---

## Context

Conductor observation 2026-05-28 (this session): "where are the PRs & the protocols following best practices? walk it through the full process."

Surfaces real gap: session-phase ceremony (s-NN-* lifecycle commands + canonical schema) was shipped 2026-05-27..28 but never codified as a docs/standards/ SOP. Future sessions consult either the YAML schema directly or the command files individually — no narrative document explains the DISCIPLINE behind the mechanism.

Exploration corrected an assumption error: standards/19 is taken (`19-two-org-consolidation-architecture.md`); next available is standards/25.

## Goal

Author `docs/standards/25-session-phase-discipline.md` in corpvs. Document:

1. The 10-phase lifecycle (explore → plan → branch → code → verify → push → wait → review → amend → merge → closeout → archive)
2. When to apply the discipline (substantive work vs. one-off edits)
3. The dogfood principle (every substantive change goes through ceremony, including doc edits)
4. Cross-references to the implementing artifacts (session-phases.yaml, command files, hook configs)
5. Closure: this very document was authored via the discipline it codifies

Walk all 10 phases properly:
- /s-explore: ✓ done (this turn)
- /s-plan: ← this file
- /s-branch: `feature/session-phase-discipline-sop` on corpvs
- /s-code: atomic commit(s) authoring the SOP
- /verify: read-through, lint check
- /s-push: open PR with proper title/body
- /s-wait: observe CI status
- /review: self-review via /code-review skill
- /s-amend: (if review surfaces changes)
- /s-merge: squash + delete-branch
- /closeout: end-of-session ritual
- /s-archive: gate-check + archive

## Approach

1. **Branch creation** (`/s-branch`): `feature/session-phase-discipline-sop` off corpvs main, push -u
2. **Document authoring** (`/s-code`):
   - Use standards/17 + 18 as format template (same header structure)
   - Sections: Purpose & Scope, The Ceremony (10 phases), When to Apply, Dogfood Principle, Cross-references, Closure provenance
   - Atomic commit: `feat: docs/standards/25 — session-phase discipline SOP`
3. **Push + PR** (`/s-push`):
   - `gh pr create` with title `docs: codify session-phase discipline SOP (standards/25)`
   - Body: motivation, scope, dogfood note, cross-references
4. **CI wait** (`/s-wait`): observe ci.yml results
5. **Self-review** (`/review`): inline review for completeness, accuracy, cross-ref correctness
6. **Merge** (`/s-merge`): squash + delete-branch via `gh pr merge --squash --delete-branch`
7. **Closeout** (`/closeout`): file closeout summary
8. **Archive** (`/s-archive`): gate check; archive if all green

## Premortem (Rule #24 triadic review)

**Sympathetic — where this succeeds:**
- The work IS small (one markdown doc, ~150 lines)
- Format precedent is clear (standards/17, 18)
- The recursive dogfood gives the demonstration weight
- No external dependencies — pure additive doc
- Branch unprotected so no merge-gate friction

**Adversarial — three failure modes:**
1. **CI fails** on the PR because of a yamllint/markdownlint rule I haven't seen → mitigation: read CI workflow before pushing; budget time for amend cycle
2. **PR title/body lint fails** at PR-create time (corpvs may enforce conventional-commits in title) → mitigation: prepare title in conventional-commits format upfront
3. **Self-review at scale of one author is hollow** — no second pair of eyes to catch errors → mitigation: use `/code-review` skill which applies an external perspective; also be willing to /s-amend if any signal warrants

**Orthogonal — false assumption to test:**
*Assumption*: corpvs's main branch allows direct merge after squash. *Counter*: maybe main requires X reviews. *Verification*: I checked `gh api .../branches/main/protection` → 404 (unprotected). So squash-merge will work mechanically. The discipline is best-practice, not enforced.

## Validation

1. PR opens with conventional-commits title
2. CI passes (or surfaces concrete failures to amend)
3. Squash-merge commit lands on corpvs main with DONE-NNN closure noted
4. Branch auto-deleted post-merge
5. New doc visible at `docs/standards/25-session-phase-discipline.md`
6. canonical-surfaces.md / IRF row referencing it (Phase 2 — may or may not be in scope this turn)

## Rollback

Each phase is independently rollback-safe:
- Branch creation: `git switch main && git branch -D feature/session-phase-discipline-sop`
- Commit: `git reset --hard HEAD~1` (only before push)
- PR: close without merging
- Merge: revert via PR after the fact
- Doc itself: `git revert <sha>`

## Cross-references

- `session-phases.yaml` (canonical schema being codified)
- `user-command-namespaces.yaml` (prefix conventions)
- `~/.claude/commands/s-NN-*.md` (implementing commands)
- `~/.config/ai-context/scripts/` (canonical script substrate)
- `docs/standards/17-branch-governance.md` (format precedent + cross-ref target)
- `docs/standards/18-scheduled-process-contract.md` (format precedent)
- Universal Rules #5, #11, #24
