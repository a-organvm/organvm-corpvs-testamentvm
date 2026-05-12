#!/usr/bin/env bash
# run-audit.sh — orchestrate enumerate + classify and emit dated TSV + summary.
#
# Usage: run-audit.sh [date-stamp]
#   Date stamp defaults to today (YYYY-MM-DD).
#
# Writes:
#   results/<date>.tsv          (one row per repo, TSV with header)
#   results/<date>-summary.md   (counts by classification + sanity checks)
#
# Read-only against every repo it inspects. No fetch, no commit, no modify.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESULTS_DIR="$(cd "$SCRIPT_DIR/../results" && pwd)"
STAMP="${1:-$(date +%Y-%m-%d)}"
TSV="$RESULTS_DIR/$STAMP.tsv"
SUMMARY="$RESULTS_DIR/$STAMP-summary.md"

ENUMERATE="$SCRIPT_DIR/enumerate-git-dirs.sh"
CLASSIFY="$SCRIPT_DIR/classify-repo.sh"

[[ -x "$ENUMERATE" ]] || chmod +x "$ENUMERATE"
[[ -x "$CLASSIFY" ]] || chmod +x "$CLASSIFY"

echo "audit start: $(date -Iseconds)" >&2

# Header
printf 'path\tgit_type\tworktree_of\tremotes\tahead\tbehind\tdetached\tuncommitted\tuntracked\tstash_count\tbranch_drift\tsubmodule_drift\tclassification\n' > "$TSV"

# Enumerate, then classify each entity
mapfile -t paths < <("$ENUMERATE" 2>/dev/null)
total=${#paths[@]}
echo "audit: classifying $total entities" >&2

i=0
for p in "${paths[@]}"; do
  i=$((i + 1))
  if (( i % 25 == 0 )); then
    echo "audit: progress $i / $total" >&2
  fi
  "$CLASSIFY" "$p" >> "$TSV" || echo "audit-warn: classify failed for $p" >&2
done

echo "audit: done classification ($total entities) at $(date -Iseconds)" >&2

# Summary
{
  echo "# Git-parity audit — $STAMP"
  echo ""
  echo "**Source data:** \`$TSV\`"
  echo "**Total entities:** $total"
  echo "**Audit scope:** read-only; no fetch, no state modification."
  echo ""
  echo "## Counts by classification"
  echo ""
  echo "| Class | Count |"
  echo "|---|---|"
  awk -F'\t' 'NR>1 { c[$13]++ } END { for (k in c) printf "| %s | %d |\n", k, c[k] }' "$TSV" | sort
  echo ""
  echo "## Counts by git_type"
  echo ""
  echo "| Type | Count |"
  echo "|---|---|"
  awk -F'\t' 'NR>1 { c[$2]++ } END { for (k in c) printf "| %s | %d |\n", k, c[k] }' "$TSV" | sort
  echo ""
  echo "## Sanity-check witnesses"
  echo ""
  echo "Critical anchors that MUST appear with sensible classifications:"
  echo ""
  for anchor in \
    "$HOME/Workspace/4444J99/domus-semper-palingenesis" \
    "$HOME/Code/organvm/organvm-corpvs-testamentvm" \
    "$HOME/.openclaw/workspace"; do
    row=$(awk -F'\t' -v a="$anchor" '$1 == a { print }' "$TSV")
    if [[ -n "$row" ]]; then
      cls=$(echo "$row" | awk -F'\t' '{ print $13 }')
      echo "- \`$anchor\` → **$cls** ✓"
    else
      echo "- \`$anchor\` → **MISSING from TSV** ✗"
    fi
  done
  echo ""
  echo "Exclusion check — these MUST be absent:"
  echo ""
  for excluded in "$HOME/.local/share/nvm"; do
    row=$(awk -F'\t' -v a="$excluded" '$1 == a { print }' "$TSV")
    if [[ -z "$row" ]]; then
      echo "- \`$excluded\` → **absent** ✓"
    else
      echo "- \`$excluded\` → **PRESENT (exclusion failed)** ✗"
    fi
  done
  echo ""
  echo "## Method"
  echo ""
  echo "- Parity definition: per \`~/.claude/plans/2026-05-01-three-gates-design.md\` lines 48–59."
  echo "- Enumeration: \`~/Workspace ~/Code ~/Documents\` maxdepth 6, plus \`~/.openclaw/workspace/.git\` stray."
  echo "- Exclusions: nvm install, Trash, node_modules, Library, submodule pointers (.git files into \`.git/modules/\`)."
  echo "- No \`git fetch\`: ahead/behind computed against cached upstream refs. Re-run with \`--with-network\` (future) for fresh accuracy."
  echo ""
  echo "## After the audit (out of scope for this artifact)"
  echo ""
  echo "Classifications produce *proposals*, never *actions* — only the human decides removal (memory rule #8, "Atoms are permanent")."
  echo ""
} > "$SUMMARY"

echo "audit complete: TSV=$TSV summary=$SUMMARY" >&2
