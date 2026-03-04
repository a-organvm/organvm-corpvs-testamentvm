#!/usr/bin/env bash
set -euo pipefail

# PRAESIDIUM — Backup & Disaster Recovery
# Mirror-clones all repos across all 9 GitHub organizations.
# Usage: ./scripts/backup-all-orgs.sh [backup-dir]
#
# Requires: gh CLI authenticated with access to all orgs.

BACKUP_DIR="${1:-$HOME/Backups/organvm-$(date +%Y%m%d)}"
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

ORGS=(
  ivviiviivvi           # ORGAN-I  (Theoria)
  omni-dromenon-machina # ORGAN-II (Poiesis)
  labores-profani-crux  # ORGAN-III (Ergon)
  organvm-iv-taxis      # ORGAN-IV (Taxis)
  organvm-v-logos       # ORGAN-V  (Logos)
  organvm-vi-koinonia   # ORGAN-VI (Koinonia)
  organvm-vii-kerygma   # ORGAN-VII (Kerygma)
  meta-organvm          # META-ORGANVM
  4444j99               # Personal / LIMINAL
)

echo "PRAESIDIUM — Backup started at $TIMESTAMP"
echo "Destination: $BACKUP_DIR"
echo "Organizations: ${#ORGS[@]}"
echo "────────────────────────────────────────"

mkdir -p "$BACKUP_DIR"

total=0
failed=0
skipped=0

for org in "${ORGS[@]}"; do
  org_dir="$BACKUP_DIR/$org"
  mkdir -p "$org_dir"
  echo ""
  echo "[$org]"

  repos=$(gh repo list "$org" --json nameWithOwner --jq '.[].nameWithOwner' 2>/dev/null || true)
  if [[ -z "$repos" ]]; then
    echo "  (no repos or access denied)"
    continue
  fi

  while IFS= read -r repo; do
    repo_name="${repo#*/}"
    mirror_path="$org_dir/$repo_name.git"

    if [[ -d "$mirror_path" ]]; then
      echo "  ↻ $repo_name (updating existing mirror)"
      if git -C "$mirror_path" remote update --prune 2>/dev/null; then
        ((total++))
      else
        echo "    ✗ update failed"
        ((failed++))
      fi
    else
      echo "  ↓ $repo_name (new mirror clone)"
      if git clone --mirror "https://github.com/$repo.git" "$mirror_path" 2>/dev/null; then
        ((total++))
      else
        echo "    ✗ clone failed"
        ((failed++))
      fi
    fi
  done <<< "$repos"
done

echo ""
echo "────────────────────────────────────────"
echo "PRAESIDIUM complete: $total mirrored, $failed failed"
echo "Backup location: $BACKUP_DIR"
echo "Timestamp: $TIMESTAMP"

# Write manifest
cat > "$BACKUP_DIR/manifest.json" << MANIFEST
{
  "timestamp": "$TIMESTAMP",
  "total_repos": $total,
  "failed": $failed,
  "organizations": $(printf '%s\n' "${ORGS[@]}" | jq -R . | jq -s .),
  "backup_dir": "$BACKUP_DIR"
}
MANIFEST

echo "Manifest: $BACKUP_DIR/manifest.json"

if [[ "$failed" -gt 0 ]]; then
  exit 1
fi
