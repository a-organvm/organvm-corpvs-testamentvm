#!/usr/bin/env python3
"""Triple-Verification Engine for DONE atoms.

Nothing gets closed without triple checking. The measurement engine
marked 8,330 atoms DONE on first-match evidence. This script verifies
each DONE atom against multiple independent evidence sources and
flags atoms where verification fails.

Verification sources:
  1. EVIDENCE — does the atom's 'produced' field cite evidence?
  2. CLUSTER — is this atom in a similarity cluster where siblings are OPEN?
  3. CONTENT — does the content actually describe completed work?

Consensus model:
  3/3 pass → HIGH CONFIDENCE (stays DONE)
  2/3 pass → MEDIUM CONFIDENCE (stays DONE, flagged for review)
  1/3 pass → LOW CONFIDENCE (reopened to OPEN)
  0/3 pass → INVALID (reopened to OPEN)

Usage:
    python3 verify_done.py [--dry-run] [--batch N]

    --dry-run    Show results without writing
    --batch N    Process only N atoms (default: all)
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ATOMS_PATH = SCRIPT_DIR / "prompt-atoms.json"
CLUSTERS_PATH = SCRIPT_DIR / "similarity-clusters.json"
REPORT_PATH = SCRIPT_DIR / "DONE-VERIFICATION-REPORT.md"

# Evidence sources that constitute real verification
VALID_EVIDENCE = {
    "git", "git-file", "irf-done", "github-closed", "github-merged",
    "hook-exists", "memory-coverage", "file-exists",
}

# Patterns indicating content describes COMPLETED work (past tense, results)
COMPLETION_PATTERNS = [
    re.compile(r"\b(completed|done|finished|deployed|merged|shipped|released|resolved)\b", re.I),
    re.compile(r"\b(implemented|built|created|added|fixed|repaired|configured)\b", re.I),
    re.compile(r"\bDONE-\d+\b"),
    re.compile(r"✓|✅|☑"),
]

# Patterns indicating content describes INCOMPLETE work (future tense, directives)
INCOMPLETION_PATTERNS = [
    re.compile(r"\b(need|must|should|todo|fixme|hack|broken|missing|required)\b", re.I),
    re.compile(r"\b(implement|create|build|add|fix|deploy|configure|write)\s", re.I),
    re.compile(r"\b(not yet|still|remaining|pending|blocked|waiting)\b", re.I),
    re.compile(r"\?\s*$", re.M),  # ends with question mark
]

# System output patterns (not user work — noise that got atomized)
SYSTEM_OUTPUT = re.compile(
    r"^(==>|🍺|Pouring|<task-|cd\s+['\"]|claude\s+--|❯\s*$|"
    r"Checking|Downloading|Installing|Updating|Cloning|"
    r"remote:|warning:|Already|HEAD is now|"
    r"\d+\s+file|---|\+\+\+|@@\s|diff\s--)",
    re.I | re.M,
)


def check_evidence(atom: dict) -> bool:
    """Check 1: Does the atom cite valid evidence sources?"""
    produced = atom.get("produced", [])
    if not produced:
        return False
    return any(
        p in VALID_EVIDENCE or any(ev in p for ev in VALID_EVIDENCE)
        for p in produced
    )


def check_cluster_consistency(
    atom_id: str,
    cluster_lookup: dict[str, dict],
) -> bool:
    """Check 2: Is this atom in a cluster where ALL siblings are DONE?

    If siblings are OPEN, this DONE status is suspicious.
    """
    cluster = cluster_lookup.get(atom_id)
    if cluster is None:
        # Not in any cluster — no cluster evidence to contradict
        return True

    statuses = cluster.get("statuses", [])
    if not statuses:
        return True

    # What fraction of the cluster is DONE?
    done_count = sum(1 for s in statuses if s == "DONE")
    total = len(statuses)

    # If less than 70% of cluster is DONE, this atom's DONE status is suspect
    return done_count / total >= 0.70


def check_content_completion(atom: dict) -> bool:
    """Check 3: Does the content describe completed vs incomplete work?"""
    content = atom.get("content", "")
    if not content:
        return False

    # System output is not real work — it's noise that got atomized
    if SYSTEM_OUTPUT.search(content[:200]):
        return False

    # Count completion vs incompletion signals
    completion_signals = sum(1 for p in COMPLETION_PATTERNS if p.search(content))
    incompletion_signals = sum(1 for p in INCOMPLETION_PATTERNS if p.search(content))

    # If more incompletion signals than completion signals → suspect
    if incompletion_signals > completion_signals:
        return False

    return True


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    batch = None
    if "--batch" in sys.argv:
        idx = sys.argv.index("--batch")
        if idx + 1 < len(sys.argv):
            batch = int(sys.argv[idx + 1])

    if not ATOMS_PATH.exists():
        print(f"ERROR: {ATOMS_PATH} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Loading {ATOMS_PATH}...")
    with open(ATOMS_PATH) as f:
        atoms = json.load(f)

    # Load clusters for cross-reference
    cluster_lookup: dict[str, dict] = {}
    if CLUSTERS_PATH.exists():
        with open(CLUSTERS_PATH) as f:
            cluster_data = json.load(f)
        for c in cluster_data.get("cluster_data", []):
            for member in c.get("members", []):
                cluster_lookup[member] = c
        print(f"Loaded {len(cluster_lookup)} cluster memberships")

    # Filter to DONE atoms
    done_atoms = [a for a in atoms if a.get("status") == "DONE"]
    print(f"DONE atoms to verify: {len(done_atoms)}")

    if batch:
        done_atoms = done_atoms[:batch]
        print(f"Batch mode: verifying {batch} atoms")

    # Verify each atom
    results = {
        "HIGH": [],     # 3/3 pass
        "MEDIUM": [],   # 2/3 pass
        "LOW": [],      # 1/3 pass
        "INVALID": [],  # 0/3 pass
    }
    check_counts = Counter()

    for atom in done_atoms:
        aid = atom["atom_id"]
        c1 = check_evidence(atom)
        c2 = check_cluster_consistency(aid, cluster_lookup)
        c3 = check_content_completion(atom)
        passes = sum([c1, c2, c3])

        if passes == 3:
            results["HIGH"].append(aid)
        elif passes == 2:
            results["MEDIUM"].append(aid)
        elif passes == 1:
            results["LOW"].append(aid)
        else:
            results["INVALID"].append(aid)

        check_counts[f"evidence_{'pass' if c1 else 'fail'}"] += 1
        check_counts[f"cluster_{'pass' if c2 else 'fail'}"] += 1
        check_counts[f"content_{'pass' if c3 else 'fail'}"] += 1

    # Report
    total = len(done_atoms)
    print(f"\n{'='*60}")
    print("DONE VERIFICATION RESULTS")
    print(f"{'='*60}")
    print(f"Total verified: {total}")
    print(f"  HIGH (3/3):    {len(results['HIGH']):>6}  ({len(results['HIGH'])/total*100:.1f}%)")
    print(f"  MEDIUM (2/3):  {len(results['MEDIUM']):>6}  ({len(results['MEDIUM'])/total*100:.1f}%)")
    print(f"  LOW (1/3):     {len(results['LOW']):>6}  ({len(results['LOW'])/total*100:.1f}%)")
    print(f"  INVALID (0/3): {len(results['INVALID']):>6}  ({len(results['INVALID'])/total*100:.1f}%)")

    print(f"\nCheck breakdown:")
    print(f"  Evidence pass:  {check_counts['evidence_pass']:>6}  fail: {check_counts['evidence_fail']:>6}")
    print(f"  Cluster pass:   {check_counts['cluster_pass']:>6}  fail: {check_counts['cluster_fail']:>6}")
    print(f"  Content pass:   {check_counts['content_pass']:>6}  fail: {check_counts['content_fail']:>6}")

    # Reopen LOW and INVALID atoms
    reopened = 0
    if not dry_run:
        atom_lookup = {a["atom_id"]: a for a in atoms}
        for aid in results["LOW"] + results["INVALID"]:
            if aid in atom_lookup:
                atom_lookup[aid]["status"] = "OPEN"
                atom_lookup[aid]["produced"] = atom_lookup[aid].get("produced", []) + [
                    "reopened-failed-verification"
                ]
                reopened += 1
        print(f"\nReopened {reopened} LOW/INVALID atoms")

        # Write atoms
        print(f"Writing {ATOMS_PATH}...")
        with open(ATOMS_PATH, "w") as f:
            json.dump(atoms, f, indent=1)

    # Write report
    lines = [
        "# DONE Verification Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Atoms verified:** {total}",
        "",
        "## Confidence Levels",
        "",
        f"| Level | Count | % | Action |",
        f"|-------|-------|---|--------|",
        f"| HIGH (3/3) | {len(results['HIGH'])} | {len(results['HIGH'])/total*100:.1f}% | Stays DONE |",
        f"| MEDIUM (2/3) | {len(results['MEDIUM'])} | {len(results['MEDIUM'])/total*100:.1f}% | Stays DONE, flagged |",
        f"| LOW (1/3) | {len(results['LOW'])} | {len(results['LOW'])/total*100:.1f}% | Reopened |",
        f"| INVALID (0/3) | {len(results['INVALID'])} | {len(results['INVALID'])/total*100:.1f}% | Reopened |",
        "",
        "## Checks",
        "",
        "| Check | Pass | Fail |",
        "|-------|------|------|",
        f"| Evidence cited | {check_counts['evidence_pass']} | {check_counts['evidence_fail']} |",
        f"| Cluster consistency | {check_counts['cluster_pass']} | {check_counts['cluster_fail']} |",
        f"| Content completion | {check_counts['content_pass']} | {check_counts['content_fail']} |",
        "",
    ]

    # Sample INVALID atoms
    if results["INVALID"]:
        atom_lookup = {a["atom_id"]: a for a in atoms}
        lines.append("## Sample INVALID (0/3) Atoms")
        lines.append("")
        for aid in results["INVALID"][:20]:
            a = atom_lookup.get(aid, {})
            content = a.get("content", "")[:100].replace("\n", " ")
            lines.append(f"- `{aid}` ({a.get('type', '?')}) — {content}")
        lines.append("")

    if results["LOW"]:
        lines.append("## Sample LOW (1/3) Atoms")
        lines.append("")
        atom_lookup = {a["atom_id"]: a for a in atoms}
        for aid in results["LOW"][:20]:
            a = atom_lookup.get(aid, {})
            content = a.get("content", "")[:100].replace("\n", " ")
            produced = a.get("produced", [])
            lines.append(f"- `{aid}` ({a.get('type', '?')}, evidence: {produced[:2]}) — {content}")
        lines.append("")

    lines.append(f"\n*Engine: verify_done.py | Run: {datetime.now().isoformat()}*")
    REPORT_PATH.write_text("\n".join(lines))
    print(f"Wrote {REPORT_PATH}")

    if dry_run:
        print(f"\n[DRY RUN] Would reopen {len(results['LOW']) + len(results['INVALID'])} atoms.")


if __name__ == "__main__":
    main()
