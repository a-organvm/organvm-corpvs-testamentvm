#!/usr/bin/env python3
"""Extract signal flow edges from all seed.yaml files and build the coverage matrix."""

import yaml
import json
import os
from pathlib import Path
from collections import defaultdict

# ─── Repo → Ideal Form mapping (from 2026-04-07-ideal-form-classification.md) ───

FORM_NAMES = {
    "I": "Self-Reading System",
    "II": "Alchemical Transformation",
    "III": "Narrative as Computation",
    "IV": "Knowledge Atomization",
    "V": "Behavioral Architecture",
    "VI": "Live Performance",
    "VII": "Identity as OS",
    "VIII": "Governance as Art",
    "IX": "Multi-Agent Orchestration",
    "X": "Communal Knowledge",
    "XI": "Amplification & Distribution",
    "XII": "Commercial Products",
    "XIII": "World-Building",
    "XIV": "Computational Substrate",
    "XV": "Contribution as Practice",
}

REPO_TO_FORM = {
    # I. Self-Reading
    "recursive-engine--generative-entity": "I",
    "auto-revision-epistemic-engine": "I",
    "organon-noumenon--ontogenetic-morphe": "I",
    "a-recursive-root": "I",
    "radix-recursiva-solve-coagula-redi": "I",
    "cog-init-1-0-": "I",
    "call-function--ontological": "I",
    "hierarchia-mundi": "I",
    "reverse-engine-recursive-run": "I",
    "a-organvm": "I",
    "system-system--system": "I",
    # II. Alchemical
    "sema-metra--alchemica-mundi": "II",
    "alchemical-synthesizer": "II",
    "alchemia-ingestvm": "II",
    "materia-collider": "II",
    # III. Narrative
    "narratological-algorithmic-lenses": "III",
    "nexus--babel-alexandria": "III",
    "linguistic-atomization-framework": "III",
    "chthon-oneiros": "III",
    "krypto-velamen": "III",
    "vigiles-aeternae--corpus-mythicum": "III",
    # IV. Knowledge
    "my-knowledge-base": "IV",
    "conversation-corpus-engine": "IV",
    "scalable-lore-expert": "IV",
    "meta-source--ledger-output": "IV",
    "cognitive-archaelogy-tribunal": "IV",
    "organvm-corpvs-testamentvm": "IV",
    # V. Behavioral / Styx
    "styx-behavioral-economics-theory": "V",
    "peer-audited--behavioral-blockchain": "V",
    "styx-behavioral-commerce": "V",
    "styx-behavioral-art": "V",
    # VI. Performance
    "metasystem-master": "VI",
    "core-engine": "VI",
    "performance-sdk": "VI",
    "audio-synthesis-bridge": "VI",
    "universal-waveform-explorer": "VI",
    # VII. Identity
    "a-mavs-olevm": "VII",
    "ivi374ivi027-05": "VII",
    "life-my--midst--in": "VII",
    "4-ivi374-f0rivi4": "VII",
    # VIII. Governance
    "orchestration-start-here": "VIII",
    "petasum-super-petasum": "VIII",
    "system-governance-framework": "VIII",
    "collective-persona-operations": "VIII",
    "cvrsvs-honorvm": "VIII",
    "tool-interaction-design": "VIII",
    "organvm-ontologia": "VIII",
    # IX. Multi-Agent
    "agentic-titan": "IX",
    "agent--claude-smith": "IX",
    "a-i--skills": "IX",
    # X. Communal Knowledge
    "community-hub": "X",
    "salon-archive": "X",
    "reading-group-curriculum": "X",
    "adaptive-personal-syllabus": "X",
    "koinonia-db": "X",
    "studium-generale": "X",
    # XI. Amplification
    "public-process": "XI",
    "social-automation": "XI",
    "distribution-strategy": "XI",
    "announcement-templates": "XI",
    "content-engine--asset-amplifier": "XI",
    "hokage-chess": "XI",
    # XII. Commercial
    "public-record-data-scrapper": "XII",
    "classroom-rpg-aetheria": "XII",
    "the-actual-news": "XII",
    "sovereign-systems--elevate-align": "XII",
    "tab-bookmark-manager": "XII",
    "card-trade-social": "XII",
    # XIII. World-Building
    "vigiles-aeternae--theatrum-mundi": "XIII",
    "vigiles-aeternae--agon-cosmogonicum": "XIII",
    "a-i-council--coliseum": "XIII",
    "life-betterment-simulation": "XIII",
    "shared-remembrance-gateway": "XIII",
    "my-block-warfare": "XIII",
    # XIV. Substrate
    "organvm-engine": "XIV",
    "schema-definitions": "XIV",
    "organvm-mcp-server": "XIV",
    "system-dashboard": "XIV",
    "stakeholder-portal": "XIV",
    "praxis-perpetua": "XIV",
    # XV. Contribution
    "contrib--adenhq-hive": "XV",
    "contrib--temporal-sdk-python": "XV",
    "contrib--dbt-mcp": "XV",
    "contrib--langchain-langgraph": "XV",
    "contrib--anthropic-skills": "XV",
    "contrib--ipqwery-ipapi-py": "XV",
    "contrib--primeinc-github-stars": "XV",
}

# Organ name normalization
ORGAN_NORMALIZE = {
    "I": "I", "THEORIA": "I", "1": "I", "ORGAN-I": "I",
    "II": "II", "POIESIS": "II", "ART": "II", "2": "II", "ORGAN-II": "II",
    "III": "III", "ERGON": "III", "COMMERCE": "III", "3": "III", "ORGAN-III": "III",
    "IV": "IV", "TAXIS": "IV", "ORCHESTRATION": "IV", "4": "IV", "ORGAN-IV": "IV",
    "V": "V", "LOGOS": "V", "PUBLIC PROCESS": "V", "5": "V", "ORGAN-V": "V",
    "VI": "VI", "KOINONIA": "VI", "COMMUNITY": "VI", "6": "VI", "ORGAN-VI": "VI",
    "VII": "VII", "KERYGMA": "VII", "DISTRIBUTION": "VII", "7": "VII", "ORGAN-VII": "VII",
    "META": "META", "META-ORGANVM": "META",
}

ORGAN_NAMES = {
    "I": "Theoria", "II": "Poiesis", "III": "Ergon", "IV": "Taxis",
    "V": "Logos", "VI": "Koinonia", "VII": "Kerygma", "META": "Meta",
}

# ─── Search paths ───

SEARCH_ROOTS = [
    Path.home() / "Workspace" / "organvm-i-theoria",
    Path.home() / "Workspace" / "organvm-ii-poiesis",
    Path.home() / "Workspace" / "organvm-iii-ergon",
    Path.home() / "Workspace" / "organvm-iv-taxis",
    Path.home() / "Workspace" / "organvm-v-logos",
    Path.home() / "Workspace" / "organvm-vi-koinonia",
    Path.home() / "Workspace" / "organvm-vii-kerygma",
    Path.home() / "Workspace" / "meta-organvm",
    Path.home() / "Workspace" / "4444J99",
]


def find_seed_yamls():
    """Find all seed.yaml files."""
    results = []
    for root in SEARCH_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("seed.yaml"):
            # Skip node_modules, .venv, etc.
            parts = path.parts
            if any(p in ('.venv', 'node_modules', '.git', '__pycache__', '.tox') for p in parts):
                continue
            results.append(path)
    return sorted(results)


def normalize_organ(raw):
    """Normalize organ field to standard Roman numeral."""
    if raw is None:
        return "UNKNOWN"
    s = str(raw).strip().upper()
    return ORGAN_NORMALIZE.get(s, "UNKNOWN")


def extract_repo_name(seed_data, filepath):
    """Extract repo name from seed data or filepath."""
    if "repo" in seed_data:
        return seed_data["repo"]
    if "name" in seed_data:
        return seed_data["name"]
    # Infer from path: the parent of seed.yaml is typically the repo dir
    return filepath.parent.name


def extract_edges(seed_data, repo_name, organ):
    """Extract all signal flow edges from a seed.yaml."""
    edges = []

    # Produces
    for p in seed_data.get("produces", []) or []:
        if isinstance(p, str):
            edges.append({
                "type": "produces",
                "signal": p,
                "source_repo": repo_name,
                "source_organ": organ,
                "target_repo": None,
                "target_organ": None,
            })
        elif isinstance(p, dict):
            signal_type = p.get("type", p.get("name", "unknown"))
            consumers = p.get("consumers", [])
            if isinstance(consumers, list):
                for c in consumers:
                    if isinstance(c, dict):
                        target_organ = normalize_organ(c.get("organ"))
                        target_repos = c.get("repos", [])
                        for tr in target_repos:
                            edges.append({
                                "type": "produces",
                                "signal": signal_type,
                                "source_repo": repo_name,
                                "source_organ": organ,
                                "target_repo": tr,
                                "target_organ": target_organ,
                                "relationship": c.get("relationship"),
                            })
                        if not target_repos:
                            edges.append({
                                "type": "produces",
                                "signal": signal_type,
                                "source_repo": repo_name,
                                "source_organ": organ,
                                "target_repo": None,
                                "target_organ": target_organ,
                            })
                    elif isinstance(c, str):
                        edges.append({
                            "type": "produces",
                            "signal": signal_type,
                            "source_repo": repo_name,
                            "source_organ": organ,
                            "target_repo": None,
                            "target_organ": None,
                            "target_audience": c,
                        })
            elif not consumers:
                edges.append({
                    "type": "produces",
                    "signal": signal_type,
                    "source_repo": repo_name,
                    "source_organ": organ,
                    "target_repo": None,
                    "target_organ": None,
                })

    # Consumes
    for c in seed_data.get("consumes", []) or []:
        if isinstance(c, str):
            edges.append({
                "type": "consumes",
                "signal": c,
                "source_repo": None,
                "source_organ": None,
                "target_repo": repo_name,
                "target_organ": organ,
            })
        elif isinstance(c, dict):
            signal_type = c.get("type", c.get("name", "unknown"))
            source = c.get("source", None)
            source_organ = None
            source_repo = None
            if isinstance(source, dict):
                source_organ = normalize_organ(source.get("organ"))
                source_repo = source.get("repo")
            elif isinstance(source, str):
                source_organ = normalize_organ(source)
            edges.append({
                "type": "consumes",
                "signal": signal_type,
                "source_repo": source_repo,
                "source_organ": source_organ,
                "target_repo": repo_name,
                "target_organ": organ,
            })

    # Subscriptions
    for s in seed_data.get("subscriptions", []) or []:
        if isinstance(s, dict):
            event = s.get("event", "unknown")
            source = s.get("source", None)
            source_organ = normalize_organ(source) if source else None
            edges.append({
                "type": "subscription",
                "signal": event,
                "source_repo": None,
                "source_organ": source_organ,
                "target_repo": repo_name,
                "target_organ": organ,
                "action": s.get("action"),
            })

    # Dependencies (legacy format)
    for d in seed_data.get("dependencies", []) or []:
        if isinstance(d, dict):
            dep_repo = d.get("repo", "unknown")
            edges.append({
                "type": "dependency",
                "signal": "dependency",
                "source_repo": dep_repo,
                "source_organ": None,
                "target_repo": repo_name,
                "target_organ": organ,
                "assets": d.get("assets"),
            })

    return edges


def get_form_for_repo(repo_name):
    """Look up ideal form for a repo."""
    # Try exact match
    key = repo_name.lower().strip()
    for r, f in REPO_TO_FORM.items():
        if r.lower() == key:
            return f
    # Try partial match (repo name contains the key or vice versa)
    for r, f in REPO_TO_FORM.items():
        if r.lower() in key or key in r.lower():
            return f
    return None


def main():
    seed_files = find_seed_yamls()
    print(f"Found {len(seed_files)} seed.yaml files\n")

    all_edges = []
    repos_by_organ = defaultdict(list)
    repos_by_form = defaultdict(list)
    form_organ_matrix = defaultdict(set)  # (form, organ) → set of repo names
    unclassified = []

    for sf in seed_files:
        try:
            with open(sf) as f:
                data = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"ERROR reading {sf}: {e}")
            continue

        repo_name = extract_repo_name(data, sf)
        organ_raw = data.get("organ", data.get("org", ""))
        organ = normalize_organ(organ_raw)

        # Infer organ from directory path if not in file
        if organ == "UNKNOWN":
            path_str = str(sf)
            if "organvm-i-" in path_str: organ = "I"
            elif "organvm-ii-" in path_str: organ = "II"
            elif "organvm-iii-" in path_str: organ = "III"
            elif "organvm-iv-" in path_str: organ = "IV"
            elif "organvm-v-" in path_str: organ = "V"
            elif "organvm-vi-" in path_str: organ = "VI"
            elif "organvm-vii-" in path_str: organ = "VII"
            elif "meta-organvm" in path_str: organ = "META"
            elif "4444J99" in path_str: organ = "PERSONAL"

        repos_by_organ[organ].append(repo_name)

        # Classify by ideal form
        form = get_form_for_repo(repo_name)
        if form:
            repos_by_form[form].append(repo_name)
            form_organ_matrix[(form, organ)].add(repo_name)
        else:
            unclassified.append((repo_name, organ, str(sf)))

        # Extract edges
        edges = extract_edges(data, repo_name, organ)
        all_edges.extend(edges)

    # ─── Output: Edge Table ───
    print("=" * 80)
    print("EDGE TABLE — All Signal Flow Edges")
    print("=" * 80)

    produces_edges = [e for e in all_edges if e["type"] == "produces"]
    consumes_edges = [e for e in all_edges if e["type"] == "consumes"]
    subscription_edges = [e for e in all_edges if e["type"] == "subscription"]
    dependency_edges = [e for e in all_edges if e["type"] == "dependency"]

    print(f"\nTotal edges: {len(all_edges)}")
    print(f"  produces:      {len(produces_edges)}")
    print(f"  consumes:      {len(consumes_edges)}")
    print(f"  subscriptions: {len(subscription_edges)}")
    print(f"  dependencies:  {len(dependency_edges)}")

    # Cross-organ edges (the most interesting ones)
    cross_organ = [e for e in all_edges
                   if e.get("source_organ") and e.get("target_organ")
                   and e["source_organ"] != e["target_organ"]
                   and e["source_organ"] != "UNKNOWN"
                   and e["target_organ"] != "UNKNOWN"]

    print(f"\n  Cross-organ edges: {len(cross_organ)}")
    print("\n--- Cross-Organ Edges (the signal flow between organs) ---")
    for e in cross_organ:
        src = f"{e['source_organ']}"
        if e.get("source_repo"):
            src += f"/{e['source_repo']}"
        tgt = f"{e['target_organ']}"
        if e.get("target_repo"):
            tgt += f"/{e['target_repo']}"
        print(f"  {src} →({e['signal']})→ {tgt}  [{e['type']}]")

    # ─── Output: Organ Distribution ───
    print("\n" + "=" * 80)
    print("ORGAN DISTRIBUTION")
    print("=" * 80)
    for organ in ["I", "II", "III", "IV", "V", "VI", "VII", "META", "PERSONAL", "UNKNOWN"]:
        repos = repos_by_organ.get(organ, [])
        if repos:
            name = ORGAN_NAMES.get(organ, organ)
            print(f"\n  {organ} ({name}): {len(repos)} repos")
            for r in sorted(repos):
                form = get_form_for_repo(r)
                form_label = f" [Form {form}: {FORM_NAMES.get(form, '?')}]" if form else " [UNCLASSIFIED]"
                print(f"    - {r}{form_label}")

    # ─── Output: Coverage Matrix ───
    print("\n" + "=" * 80)
    print("COVERAGE MATRIX — 15 Ideal Forms × 8 Organs")
    print("=" * 80)

    organs = ["I", "II", "III", "IV", "V", "VI", "VII", "META"]
    forms = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV"]

    # Header
    print(f"\n{'Form':<6} {'Name':<28}", end="")
    for o in organs:
        print(f" {o:<5}", end="")
    print("  Total")
    print("-" * 90)

    populated = 0
    empty = 0
    for form in forms:
        print(f"{form:<6} {FORM_NAMES[form][:27]:<28}", end="")
        row_total = 0
        for organ in organs:
            repos = form_organ_matrix.get((form, organ), set())
            count = len(repos)
            row_total += count
            if count > 0:
                print(f" {count:<5}", end="")
                populated += 1
            else:
                print(f" {'·':<5}", end="")
                empty += 1
        print(f"  {row_total}")

    print("-" * 90)
    print(f"\nPopulated cells: {populated} / {populated + empty}")
    print(f"Empty cells:     {empty} / {populated + empty}")
    print(f"Coverage:        {populated / (populated + empty) * 100:.1f}%")

    # ─── Output: Unclassified repos ───
    if unclassified:
        print(f"\n{'=' * 80}")
        print(f"UNCLASSIFIED REPOS ({len(unclassified)} repos not mapped to any ideal form)")
        print("=" * 80)
        for repo, organ, path in unclassified:
            print(f"  {organ}/{repo}  ({path})")

    # ─── Output: Empty cells (unspoken sentences) ───
    print(f"\n{'=' * 80}")
    print("UNSPOKEN SENTENCES — Empty cells in the matrix")
    print("=" * 80)
    for form in forms:
        empties = []
        for organ in organs:
            if not form_organ_matrix.get((form, organ)):
                empties.append(organ)
        if empties:
            print(f"\n  Form {form} ({FORM_NAMES[form]}):")
            print(f"    Missing in organs: {', '.join(empties)}")
            populated_in = [o for o in organs if form_organ_matrix.get((form, o))]
            print(f"    Present in organs: {', '.join(populated_in) if populated_in else 'NONE'}")

    # ─── JSON output for further processing ───
    output = {
        "total_seed_files": len(seed_files),
        "total_edges": len(all_edges),
        "cross_organ_edges": len(cross_organ),
        "populated_cells": populated,
        "empty_cells": empty,
        "coverage_pct": round(populated / (populated + empty) * 100, 1),
        "edges": all_edges,
        "matrix": {f"{form},{organ}": list(repos)
                   for (form, organ), repos in form_organ_matrix.items()},
        "unclassified": [{"repo": r, "organ": o, "path": p} for r, o, p in unclassified],
    }
    with open("/tmp/organvm_edges.json", "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n\nJSON output written to /tmp/organvm_edges.json")


if __name__ == "__main__":
    main()
