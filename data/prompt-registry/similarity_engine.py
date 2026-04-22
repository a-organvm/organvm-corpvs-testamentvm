#!/usr/bin/env python3
"""Similarity Engine for ORGANVM prompt-atoms.

Performs three analyses:
  1. CLUSTER — groups near-duplicate atoms by content similarity
  2. DELTA — extracts differences between cluster members (the signal)
  3. REPETITION — counts topic frequency as incompleteness indicator

Repetition principle: if the user said it twice, the first instance
wasn't handled. If they said it five times, it's critical. Repetition
frequency directly elevates priority.

Copy-paste detection: near-identical content across atoms = the user
pasted the same thing again because it wasn't addressed. This is
a system failure signal, not noise.

Usage:
    python3 similarity_engine.py [--threshold 0.40] [--dry-run]
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ATOMS_PATH = SCRIPT_DIR / "prompt-atoms.json"
CLUSTERS_PATH = SCRIPT_DIR / "similarity-clusters.json"
REPORT_PATH = SCRIPT_DIR / "SIMILARITY-REPORT.md"

# Minimum Jaccard similarity to consider atoms as near-duplicates
DEFAULT_THRESHOLD = 0.40

# Minimum keyword length
MIN_KEYWORD_LEN = 4

# Stop words (same as prioritize_atoms.py)
STOP_WORDS = frozenset({
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "it", "this", "that", "are", "was",
    "were", "be", "been", "being", "have", "has", "had", "do", "does",
    "did", "will", "would", "shall", "should", "may", "might", "must",
    "can", "could", "not", "no", "all", "each", "every", "both", "few",
    "more", "most", "other", "some", "such", "than", "too", "very",
    "just", "also", "now", "then", "when", "where", "how", "what",
    "which", "who", "whom", "why", "here", "there", "about", "above",
    "after", "again", "against", "below", "between", "into", "through",
    "during", "before", "until", "while", "use", "used", "using",
    "make", "made", "need", "needs", "new", "get", "set", "add", "run",
    "file", "files", "see", "like", "only", "over", "same", "work",
    "if", "so", "up", "out", "any", "its", "they", "them", "their",
    "you", "your", "we", "our", "my", "me", "he", "she", "his", "her",
    "one", "two", "first", "last", "next", "well", "way", "even",
})

DOMAIN_STOP_WORDS = frozenset({
    "agent", "completed", "done", "session", "audit", "commit", "vacuum",
    "claude", "none", "resolved", "added", "yaml", "created", "json",
    "seed", "tests", "repo", "human", "github", "repos", "meta-organvm",
    "docs", "organvm", "governance", "registry", "entry", "data", "closed",
    "across", "entries", "organ", "system", "update", "status", "build",
    "deploy", "spec", "sprint", "phase", "check", "pass", "rule", "rules",
    "implement", "implemented", "implementation", "config", "configure",
    "configured", "ensure", "verified", "fixed", "test", "merged",
    "pushed", "remaining", "advanced", "partially", "further",
    "chore", "feat", "sync", "context", "submodule", "auto-generated",
    "refresh", "dependabot", "remove", "checkpoint", "workflow",
    "pointers", "changes", "readme", "updates", "local", "bump",
    "standards", "plans", "version", "deps", "initial", "merge",
    "branch", "revert", "release", "moved", "rename", "renamed",
    "refactor", "cleanup", "minor", "style", "format",
    "create", "review", "these", "output", "start", "proceed",
    "write", "clean", "users", "project", "state", "source",
    "should", "given", "based", "using", "every", "follow",
    "apply", "point", "define", "include", "current", "specific",
    "existing", "running", "right", "within", "keep", "thing",
    "things", "type", "types", "must", "want", "back", "full",
    "takes", "look", "show", "move", "step", "ensure", "require",
})

ALL_STOP = STOP_WORDS | DOMAIN_STOP_WORDS


def extract_keywords(text: str) -> set[str]:
    """Extract meaningful lowercase keywords from text."""
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9_-]+", text.lower())
    return {w for w in words if len(w) >= MIN_KEYWORD_LEN and w not in ALL_STOP}


def jaccard(a: set, b: set) -> float:
    """Jaccard similarity: |intersection| / |union|."""
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union > 0 else 0.0


def normalized_content(text: str) -> str:
    """Normalize content for exact-match dedup."""
    return re.sub(r"\s+", " ", text.lower().strip())[:200]


# ---------------------------------------------------------------------------
# Phase 1: Exact and near-exact copy detection
# ---------------------------------------------------------------------------

def detect_copies(atoms: list[dict]) -> dict[str, list[str]]:
    """Find atoms with identical or near-identical content (>90% match).

    These are copy-paste instances — the user repeated themselves.
    """
    # Group by normalized first-200-chars
    content_groups: dict[str, list[str]] = defaultdict(list)
    for atom in atoms:
        content = atom.get("content", "")
        if len(content) < 30:
            continue
        key = normalized_content(content)
        content_groups[key].append(atom["atom_id"])

    # Filter to groups with >1 member (actual duplicates)
    copies = {k: v for k, v in content_groups.items() if len(v) > 1}
    return copies


# ---------------------------------------------------------------------------
# Phase 2: Similarity clustering via inverted index
# ---------------------------------------------------------------------------

def build_similarity_clusters(
    atoms: list[dict],
    threshold: float,
) -> list[dict]:
    """Find clusters of similar atoms using inverted keyword index.

    Efficient O(n*k*m) where m = avg index size per keyword.
    Avoids O(n^2) full pairwise comparison.
    """
    print("  Extracting keywords...")
    atom_kws: dict[str, set[str]] = {}
    inverted: dict[str, set[int]] = defaultdict(set)
    id_to_idx: dict[str, int] = {}

    for i, atom in enumerate(atoms):
        aid = atom["atom_id"]
        content = atom.get("content", "")
        if len(content) < 30:
            continue
        kws = extract_keywords(content)
        if len(kws) < 3:
            continue
        atom_kws[aid] = kws
        id_to_idx[aid] = i
        for kw in kws:
            inverted[kw].add(i)

    print(f"  {len(atom_kws)} atoms with keywords, {len(inverted)} unique keywords")

    # Find candidate pairs via inverted index
    print("  Finding candidate pairs...")
    candidate_pairs: dict[tuple[int, int], int] = Counter()
    for kw, indices in inverted.items():
        idx_list = list(indices)
        # Only consider keywords appearing in <500 atoms (high-frequency = noise)
        if len(idx_list) > 500:
            continue
        for i in range(len(idx_list)):
            for j in range(i + 1, len(idx_list)):
                pair = (min(idx_list[i], idx_list[j]), max(idx_list[i], idx_list[j]))
                candidate_pairs[pair] += 1

    # Filter to pairs with at least 3 shared keywords
    strong_candidates = {pair for pair, count in candidate_pairs.items() if count >= 3}
    print(f"  {len(strong_candidates)} candidate pairs (≥3 shared keywords)")

    # Compute Jaccard for strong candidates
    print("  Computing similarity...")
    idx_to_aid = {v: k for k, v in id_to_idx.items()}
    similar_pairs: list[tuple[str, str, float]] = []

    for i, j in strong_candidates:
        aid_i = idx_to_aid.get(i)
        aid_j = idx_to_aid.get(j)
        if aid_i is None or aid_j is None:
            continue
        kws_i = atom_kws.get(aid_i, set())
        kws_j = atom_kws.get(aid_j, set())
        sim = jaccard(kws_i, kws_j)
        if sim >= threshold:
            similar_pairs.append((aid_i, aid_j, sim))

    print(f"  {len(similar_pairs)} similar pairs (Jaccard ≥ {threshold})")

    # Build clusters via union-find
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        while parent.get(x, x) != x:
            parent[x] = parent.get(parent[x], parent[x])
            x = parent[x]
        return x

    def union(x: str, y: str) -> None:
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    for aid_i, aid_j, sim in similar_pairs:
        union(aid_i, aid_j)

    # Collect clusters
    cluster_map: dict[str, list[str]] = defaultdict(list)
    all_aids = set()
    for aid_i, aid_j, _ in similar_pairs:
        all_aids.add(aid_i)
        all_aids.add(aid_j)
    for aid in all_aids:
        root = find(aid)
        cluster_map[root].append(aid)

    # Build cluster objects with delta analysis
    atom_lookup = {a["atom_id"]: a for a in atoms}
    clusters = []

    for root, members in cluster_map.items():
        if len(members) < 2:
            continue
        member_atoms = [atom_lookup[aid] for aid in members if aid in atom_lookup]
        member_atoms.sort(key=lambda a: a.get("date", ""))

        # Find the canonical version (latest, most complete)
        canonical = max(member_atoms, key=lambda a: len(a.get("content", "")))

        # Extract deltas: keywords in canonical but not in earlier versions
        canonical_kws = extract_keywords(canonical.get("content", ""))
        deltas = []
        for m in member_atoms:
            if m["atom_id"] == canonical["atom_id"]:
                continue
            m_kws = extract_keywords(m.get("content", ""))
            added = canonical_kws - m_kws  # what canonical has that this version doesn't
            removed = m_kws - canonical_kws  # what this version has that canonical doesn't
            if added or removed:
                deltas.append({
                    "atom_id": m["atom_id"],
                    "date": m.get("date", ""),
                    "added_in_canonical": sorted(added)[:20],
                    "unique_to_this": sorted(removed)[:20],
                })

        clusters.append({
            "cluster_id": f"CLU-{len(clusters)+1:04d}",
            "size": len(members),
            "canonical": canonical["atom_id"],
            "members": [m["atom_id"] for m in member_atoms],
            "dates": [m.get("date", "") for m in member_atoms],
            "statuses": [m.get("status", "") for m in member_atoms],
            "similarity_range": "high",
            "deltas": deltas,
            "repetition_count": len(members),
        })

    clusters.sort(key=lambda c: -c["size"])
    return clusters


# ---------------------------------------------------------------------------
# Phase 3: Repetition frequency → priority boost
# ---------------------------------------------------------------------------

def compute_repetition_boost(
    atoms: list[dict],
    copies: dict[str, list[str]],
    clusters: list[dict],
) -> dict[str, float]:
    """Compute priority boost based on repetition frequency.

    Repetition = the user said it again because it wasn't handled.
    More repetitions = higher urgency = bigger priority boost.
    """
    # Count appearances of each atom in copy groups and clusters
    atom_repetitions: Counter[str] = Counter()

    for key, aids in copies.items():
        for aid in aids:
            atom_repetitions[aid] += len(aids) - 1  # times repeated

    for cluster in clusters:
        for aid in cluster["members"]:
            atom_repetitions[aid] += cluster["size"] - 1

    # Normalize: repetition boost = min(repetitions / 5, 0.3)
    # 5+ repetitions = max boost of 0.3
    boosts = {}
    for aid, count in atom_repetitions.items():
        boosts[aid] = min(count / 5.0, 0.3)

    return boosts


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    dry_run = "--dry-run" in sys.argv
    threshold = DEFAULT_THRESHOLD
    if "--threshold" in sys.argv:
        idx = sys.argv.index("--threshold")
        if idx + 1 < len(sys.argv):
            threshold = float(sys.argv[idx + 1])

    if not ATOMS_PATH.exists():
        print(f"ERROR: {ATOMS_PATH} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Loading {ATOMS_PATH}...")
    with open(ATOMS_PATH) as f:
        atoms = json.load(f)
    print(f"Loaded {len(atoms)} atoms")

    # Phase 1: Exact copy detection
    print("\n=== Phase 1: Copy-paste detection ===")
    copies = detect_copies(atoms)
    total_copy_atoms = sum(len(v) for v in copies.values())
    print(f"Found {len(copies)} copy groups ({total_copy_atoms} atoms)")

    # Top copy groups
    top_copies = sorted(copies.items(), key=lambda x: -len(x[1]))[:10]
    for content_key, aids in top_copies:
        print(f"  {len(aids)}x: {content_key[:80]}...")

    # Phase 2: Similarity clustering
    print("\n=== Phase 2: Similarity clustering ===")
    clusters = build_similarity_clusters(atoms, threshold)
    print(f"Found {len(clusters)} clusters")

    # Top clusters
    for c in clusters[:10]:
        print(f"  CLU {c['cluster_id']}: {c['size']} members, canonical={c['canonical']}")

    # Phase 3: Repetition → priority boost
    print("\n=== Phase 3: Repetition priority boost ===")
    boosts = compute_repetition_boost(atoms, copies, clusters)
    boosted_count = sum(1 for b in boosts.values() if b > 0)
    print(f"Atoms with repetition boost: {boosted_count}")
    high_boost = {aid: b for aid, b in boosts.items() if b >= 0.2}
    print(f"High-repetition atoms (boost ≥ 0.2): {len(high_boost)}")

    # Apply boosts to priority_score
    if not dry_run:
        atom_lookup = {a["atom_id"]: a for a in atoms}
        modified = 0
        for aid, boost in boosts.items():
            if aid in atom_lookup:
                atom = atom_lookup[aid]
                old_score = atom.get("priority_score", 0.0)
                new_score = min(1.0, old_score + boost)
                if new_score != old_score:
                    atom["priority_score"] = round(new_score, 4)
                    # Recalculate P-level
                    if new_score >= 0.70:
                        atom["priority"] = 0
                    elif new_score >= 0.50:
                        atom["priority"] = 1
                    elif new_score >= 0.30:
                        atom["priority"] = 2
                    else:
                        atom["priority"] = 3
                    modified += 1
        print(f"Modified priority for {modified} atoms")

    # Write clusters file
    print(f"\nWriting {CLUSTERS_PATH}...")
    with open(CLUSTERS_PATH, "w") as f:
        json.dump({
            "generated": datetime.now().isoformat(),
            "threshold": threshold,
            "copy_groups": len(copies),
            "copy_atoms": total_copy_atoms,
            "clusters": len(clusters),
            "boosted_atoms": boosted_count,
            "cluster_data": clusters[:200],  # Top 200 clusters
        }, f, indent=1)

    # Write report
    print(f"Writing {REPORT_PATH}...")
    lines = [
        "# Similarity & Repetition Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Threshold:** {threshold}",
        f"**Total atoms:** {len(atoms)}",
        "",
        "## Copy-Paste Detection",
        "",
        f"**Exact/near-exact duplicates:** {len(copies)} groups, {total_copy_atoms} atoms",
        "",
        "Each copy group represents content the user repeated — a signal that the",
        "original instance wasn't properly handled.",
        "",
        "### Top Copy Groups",
        "",
    ]

    for content_key, aids in top_copies[:15]:
        lines.append(f"- **{len(aids)}x repeated:** `{aids[0]}` — {content_key[:100]}...")

    lines.extend([
        "",
        "## Similarity Clusters",
        "",
        f"**Clusters found:** {len(clusters)}",
        "",
        "Each cluster contains atoms that discuss the same topic across sessions.",
        "The DELTA between members reveals evolution and incompleteness.",
        "",
        "### Top Clusters by Size",
        "",
    ])

    for c in clusters[:20]:
        lines.append(f"### {c['cluster_id']} ({c['size']} members)")
        lines.append(f"Canonical: `{c['canonical']}`")
        lines.append(f"Dates: {', '.join(c['dates'][:5])}")
        lines.append(f"Statuses: {', '.join(set(c['statuses']))}")
        if c["deltas"]:
            lines.append("Deltas:")
            for d in c["deltas"][:3]:
                if d["added_in_canonical"]:
                    lines.append(f"  - `{d['atom_id']}` missing: {', '.join(d['added_in_canonical'][:8])}")
                if d["unique_to_this"]:
                    lines.append(f"  - `{d['atom_id']}` unique: {', '.join(d['unique_to_this'][:8])}")
        lines.append("")

    lines.extend([
        "## Repetition Priority Boost",
        "",
        f"**Atoms boosted:** {boosted_count}",
        f"**High-repetition (boost ≥ 0.2):** {len(high_boost)}",
        "",
        "Repetition frequency directly elevates priority score.",
        "5+ repetitions = maximum boost of +0.30.",
        "",
    ])

    if high_boost:
        lines.append("### Highest Repetition Atoms")
        lines.append("")
        atom_lookup = {a["atom_id"]: a for a in atoms}
        for aid in sorted(high_boost, key=high_boost.get, reverse=True)[:15]:
            atom = atom_lookup.get(aid, {})
            content = atom.get("content", "")[:80].replace("\n", " ")
            lines.append(f"- `{aid}` (boost +{high_boost[aid]:.2f}) — {content}")

    lines.append(f"\n*Engine: similarity_engine.py | Run: {datetime.now().isoformat()}*")

    REPORT_PATH.write_text("\n".join(lines))

    # Write atoms if modified
    if not dry_run and boosts:
        print(f"\nWriting {ATOMS_PATH}...")
        with open(ATOMS_PATH, "w") as f:
            json.dump(atoms, f, indent=1)
        print("Done.")
    elif dry_run:
        print("\n[DRY RUN] No changes written to atoms.")


if __name__ == "__main__":
    main()
