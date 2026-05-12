#!/usr/bin/env bash
# classify-repo.sh — classify one local git repo against the parity rubric.
#
# Argument: $1 = path to the .git directory or .git file (worktree pointer).
# Stdout: one TSV row.
#
# TSV columns (no header — caller writes header):
#   path  git_type  worktree_of  remotes  ahead  behind  detached
#   uncommitted  untracked  stash_count  branch_drift  submodule_drift
#   classification
#
# Severity order (highest wins): NO_REMOTE, DETACHED_HEAD, DIRTY_UNCOMMITTED,
# STASH_PRESENT, DIVERGED, LOCAL_AHEAD, BRANCH_DRIFT, SUBMODULE_DRIFT,
# DIRTY_UNTRACKED, LOCAL_BEHIND, BARE, PARITY_OK, ERROR.
#
# No network calls. No state modifications.

set -uo pipefail  # NOT -e; per-check failures must not abort the script.

GIT_PATH="${1:-}"
if [[ -z "$GIT_PATH" ]]; then
  echo "usage: $0 <path-to-.git>" >&2
  exit 2
fi

# Resolve repo working directory and type
if [[ -d "$GIT_PATH" ]]; then
  git_type="regular"
  repo_dir="$(dirname "$GIT_PATH")"
  worktree_of=""
elif [[ -f "$GIT_PATH" ]]; then
  git_type="worktree"
  repo_dir="$(dirname "$GIT_PATH")"
  first=$(head -1 "$GIT_PATH" 2>/dev/null || echo "")
  worktree_of="${first#gitdir: }"
else
  printf '%s\t%s\t\t\t\t\t\t\t\t\t\t\t%s\n' "$GIT_PATH" "missing" "ERROR"
  exit 0
fi

# Bare-repo detection (after resolving repo_dir for regular case)
is_bare=$(git -C "$repo_dir" rev-parse --is-bare-repository 2>/dev/null || echo "false")
if [[ "$is_bare" == "true" ]]; then
  git_type="bare"
fi

# Remote presence
remotes=$(git -C "$repo_dir" remote 2>/dev/null | tr '\n' ',' | sed 's/,$//')

# Defaults
ahead=0; behind=0; detached="false"
uncommitted=0; untracked=0; stash_count=0
branch_drift=""; submodule_drift="false"
class=""

# HEAD state
head_branch=$(git -C "$repo_dir" symbolic-ref --short -q HEAD 2>/dev/null || echo "")
if [[ -z "$head_branch" ]]; then
  if git -C "$repo_dir" rev-parse --verify HEAD &>/dev/null; then
    detached="true"
  fi
fi

# Ahead/behind vs upstream — only if HEAD is on a branch with an upstream
if [[ -n "$head_branch" ]]; then
  upstream=$(git -C "$repo_dir" rev-parse --abbrev-ref "@{u}" 2>/dev/null || echo "")
  if [[ -n "$upstream" ]]; then
    ahead=$(git -C "$repo_dir" rev-list --count "@{u}..HEAD" 2>/dev/null || echo 0)
    behind=$(git -C "$repo_dir" rev-list --count "HEAD..@{u}" 2>/dev/null || echo 0)
  fi
fi

# Working-tree state (skip for bare repos)
# Note: grep -c outputs the count AND exits 1 on zero matches. We must NOT
# use `|| echo 0` — that would append a second "0", producing "0\n0" in the
# captured variable and corrupting TSV with embedded newlines. Use `|| true`
# only to suppress non-zero exit propagation; the count itself is already correct.
if [[ "$git_type" != "bare" ]]; then
  status_output=$(git -C "$repo_dir" status --porcelain=v1 2>/dev/null || true)
  if [[ -n "$status_output" ]]; then
    untracked=$(printf '%s\n' "$status_output" | grep -c '^??' || true)
    uncommitted=$(printf '%s\n' "$status_output" | grep -cE '^[^?]' || true)
  fi
fi

# Stashes — wc -l returns 0 with exit 0 on empty input, but be defensive.
stash_count=$(git -C "$repo_dir" stash list 2>/dev/null | wc -l | tr -d ' \n' || true)
stash_count="${stash_count:-0}"

# Branch drift (non-HEAD branches with [ahead, [behind, or [gone)
if [[ "$git_type" != "bare" ]]; then
  branch_drift=$(git -C "$repo_dir" for-each-ref \
      --format='%(refname:short)|%(upstream:track)' refs/heads/ 2>/dev/null \
    | awk -F'|' '$2 ~ /\[ahead|\[behind|\[gone/ { gsub(/[][]/, "", $2); print $1 ":" $2 }' \
    | tr '\n' ';' | sed 's/;$//')
fi

# Submodule drift (only if .gitmodules present)
if [[ -f "$repo_dir/.gitmodules" ]]; then
  if git -C "$repo_dir" submodule status 2>/dev/null | grep -qE '^[+-]'; then
    submodule_drift="true"
  fi
fi

# Classification — highest severity wins
if [[ -z "$remotes" ]]; then
  class="NO_REMOTE"
elif [[ "$detached" == "true" ]]; then
  class="DETACHED_HEAD"
elif [[ "$uncommitted" -gt 0 ]] 2>/dev/null; then
  class="DIRTY_UNCOMMITTED"
elif [[ "$stash_count" -gt 0 ]] 2>/dev/null; then
  class="STASH_PRESENT"
elif [[ "$ahead" -gt 0 && "$behind" -gt 0 ]] 2>/dev/null; then
  class="DIVERGED"
elif [[ "$ahead" -gt 0 ]] 2>/dev/null; then
  class="LOCAL_AHEAD"
elif [[ -n "$branch_drift" ]]; then
  class="BRANCH_DRIFT"
elif [[ "$submodule_drift" == "true" ]]; then
  class="SUBMODULE_DRIFT"
elif [[ "$untracked" -gt 0 ]] 2>/dev/null; then
  class="DIRTY_UNTRACKED"
elif [[ "$behind" -gt 0 ]] 2>/dev/null; then
  class="LOCAL_BEHIND"
elif [[ "$git_type" == "bare" ]]; then
  class="BARE"
else
  class="PARITY_OK"
fi

printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
  "$repo_dir" "$git_type" "$worktree_of" "$remotes" "$ahead" "$behind" \
  "$detached" "$uncommitted" "$untracked" "$stash_count" \
  "$branch_drift" "$submodule_drift" "$class"
