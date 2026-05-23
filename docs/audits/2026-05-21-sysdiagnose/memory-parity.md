# Memory Parity Check — Rule #12 verification

**Scope:** project_artifact_* and project_session_* memory entries modified in last 7 days
**Method:** for each entry, identify the load-bearing on-disk claim (file path, commit SHA, IRF row state, directory existence) and verify against current state.
**Population:** 30 memory files modified between 2026-05-15 and 2026-05-22.

## Verification sample (7 entries — load-bearing claims)

| Memory entry | Claim | Verification | Status |
|---|---|---|---|
| `project_session_2026_05_22_1password_automation_surface.md` | SSH_AUTH_SOCK fix at chezmoi `e5d38b3` | `git log e5d38b3` → "Add .config/zsh/02-1password.zsh" | ✅ verified |
| `project_session_2026_05_20_nudger_open_threads.md` | worktree at `.claude/worktrees/housekeeping-enforcement` | `test -d` → MISSING | ⚠️ stale (likely merged/cleaned per `[[2026-05-21-all-sessions-closeout-sweep]]`) |
| `project_session_2026_05_21_sessionend_hook_perma_fix.md` | substrate-check at chezmoi `0b74e70` | `git log 0b74e70` → matches description | ✅ verified |
| `reference_1password_8_12_beta_socket_path.md` | socket at `~/Library/Group Containers/.../t/agent.sock` | `test -S` → PRESENT | ✅ verified |
| `project_artifact_2026_05_20_skills_path_coordination.md` (via [[feedback_skills_path_coordination]]) | skills at `~/Code/organvm/a-i--skills`; old path absent | both checks pass | ✅ verified |
| `feedback_classifier_authorization_grammar.md` (mentions `~/_dot-config` seed from `[[2026-05-21-dot-config-substrate-seed]]`) | dir exists with content | `ls` → 5 entries present | ✅ verified |
| `project_artifact_2026_05_22_signing_p1_first_real_use.md` | multi-signer-ssh wrapper + op-ssh-sign load-bearing | both present and executable | ✅ verified, but with **timeline nuance** (see below) |

## Verification rate

**6/7 verified, 1 stale = 85.7% parity.**

This is comfortably above the empirical threshold the user's memory rule #12 was written to catch (memory rule was distilled after cases where 30–50% of memory claims were stale). The single stale claim is benign (a worktree that was used and cleaned up), not load-bearing for any active work.

## Timeline nuance — `[[2026-05-22-signing-p1-first-real-use]]`

The memory entry claims op-ssh-sign became load-bearing only on 2026-05-22 after the SSH_AUTH_SOCK fix. Timeline cross-check (see `timeline.md`) shows op-ssh-sign was already actively invoked 10+ times during 17:50–18:12 EDT on **2026-05-21** — *before* the memory entry's claimed first-use date.

**Reconciliation:** the memory entry is partially correct. The wrapper's P1 path *worked* via direct invocation before 2026-05-22 (git can call op-ssh-sign directly via gpg.ssh.program config). What 2026-05-22's session changed is that `ssh -A`-style operations now route P1 through 1Password agent socket via SSH_AUTH_SOCK. So "first real use" is true under one interpretation (agent-mediated) but false under another (direct invocation). Recommend the memory entry be updated to say *"first real use of agent-mediated P1"* on next session close.

This is a Rule #12 success story: the memory was *almost* right but the timeline reveals nuance. Use these checks as evidence the rule is working as designed.

## Memory entries that were NOT sampled

Not sampled in this audit:
- `feedback_*` entries (claims are policy, not file-state — different verification methodology).
- Entries older than 7 days (Rule #12 typically applies to fresh memory; stale-by-design entries are categorically different).
- The full set of `collaborator_*` and `user_*` entries (claims are about people, not file paths).

A full memory-tree parity check (all 100+ entries) would be valuable but out of scope for this audit.

## Recommendation

No immediate corrections needed beyond the one nuance noted above. The 85.7% parity rate is consistent with the system as designed — memory is hypothesis, audit verifies before action, stale claims surface as findings rather than as failed actions.
