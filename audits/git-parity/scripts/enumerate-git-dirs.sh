#!/usr/bin/env bash
# enumerate-git-dirs.sh — emit one .git path per line for every user git directory.
#
# Includes: regular repos (.git/ dirs) and worktrees (.git files pointing to
# <parent>/.git/worktrees/<name>/). Excludes: nvm install, Trash, node_modules,
# Library, and submodule pointers (.git files pointing into .git/modules/).
#
# Stdout: one absolute path per line.
# Stderr: a one-line count for human eyes.
set -euo pipefail

ROOTS=(
  "$HOME/Workspace"
  "$HOME/Code"
  "$HOME/Documents"
)
STRAYS=(
  "$HOME/.openclaw/workspace/.git"
)
MAXDEPTH=6

emit_candidates() {
  for root in "${ROOTS[@]}"; do
    [[ -d "$root" ]] || continue
    find "$root" -maxdepth "$MAXDEPTH" -name ".git" -prune -print 2>/dev/null
  done
  for stray in "${STRAYS[@]}"; do
    [[ -e "$stray" ]] && echo "$stray"
  done
}

filter_excluded() {
  grep -vE '/\.local/share/nvm/|/\.Trash/|/node_modules/|/Library/' || true
}

drop_submodule_pointers() {
  while IFS= read -r p; do
    if [[ -f "$p" ]]; then
      # Worktree pointer or submodule pointer. Read first line.
      first=$(head -1 "$p" 2>/dev/null || echo "")
      target="${first#gitdir: }"
      # Submodule pointers contain ".git/modules/" in target. Drop them.
      if [[ "$target" == *"/.git/modules/"* ]]; then
        continue
      fi
    fi
    echo "$p"
  done
}

total=0
emit_candidates | filter_excluded | drop_submodule_pointers | sort -u | while IFS= read -r p; do
  echo "$p"
  total=$((total + 1))
done

# (the subshell loses `total` — recompute for stderr report)
count=$(emit_candidates | filter_excluded | drop_submodule_pointers | sort -u | wc -l | tr -d ' ')
echo "enumerate-git-dirs: $count entities" >&2
