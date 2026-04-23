#!/usr/bin/env python3
"""
Form Gap Analysis: Top 10 ideal forms vs materialized evidence.
Scans ~/Workspace/ for repos, files, configs, and git activity matching each form's concepts.
Writes form-gap-analysis.jsonl and prints human-readable summary.
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

WORKSPACE = Path(os.path.expanduser("~/Workspace"))
IDEAL_FORMS_PATH = WORKSPACE / "organvm/organvm-corpvs-testamentvm/data/atoms/ideal-forms.jsonl"
OUTPUT_PATH = WORKSPACE / "organvm/organvm-corpvs-testamentvm/data/atoms/form-gap-analysis.jsonl"

# ---------------------------------------------------------------------------
# Search strategies per form -- derived from label, core_concepts, domains,
# angle_distribution, and facet sample text
# ---------------------------------------------------------------------------

FORM_SEARCH_CONFIG = {
    "traj-deep-90d6761e8b4a": {
        # revise / thread / project -- general project revision, editing, iteration
        "search_terms": ["revise", "revision", "rewrite", "edit", "thread", "iterate"],
        "repo_patterns": [
            "auto-revision*", "essay-pipeline", "editorial-standards",
            "content-engine*", "kerygma-pipeline", "conversation-corpus*",
        ],
        "file_patterns": ["*revis*", "*thread*", "*edit*", "*draft*"],
        "domain": "general (revision/editing workflows)",
        "expected_artifacts": [
            "Revision pipeline (automated rewrite engine)",
            "Thread management system",
            "Project iteration tracking",
            "Edit history / diff tooling",
            "Style guide enforcement",
        ],
    },
    "traj-deep-9dd66d2f5a09": {
        # thread / project / system -- system-level project orchestration
        "search_terms": ["project", "system", "orchestrat", "pipeline", "workflow"],
        "repo_patterns": [
            "orchestration*", "system-system*", "organvm-engine",
            "system-governance*", "system-dashboard", "metasystem*",
        ],
        "file_patterns": ["*orchestrat*", "*pipeline*", "*workflow*", "*system*"],
        "domain": "general (system orchestration)",
        "expected_artifacts": [
            "Multi-project orchestration engine",
            "System state dashboard",
            "Pipeline execution framework",
            "Thread-to-system promotion logic",
            "Cross-project dependency graph",
        ],
    },
    "traj-f2a1c18c7cd9": {
        # class -- pedagogy, education, curriculum, classroom
        "search_terms": ["class", "curriculum", "syllabus", "assignment", "student", "rubric", "pedagog"],
        "repo_patterns": [
            "classroom-rpg*", "adaptive-personal-syllabus", "reading-group*",
            "studium-generale", "reading-observatory",
        ],
        "file_patterns": ["*syllabus*", "*curriculum*", "*rubric*", "*assignment*", "*class*"],
        "domain": "code/pedagogy (classroom + education)",
        "expected_artifacts": [
            "Curriculum builder / syllabus generator",
            "Assignment scaffolding templates",
            "Student feedback automation",
            "Rubric engine",
            "Pedagogical content delivery system",
            "Class session management",
        ],
    },
    "traj-67a416ac51dd": {
        # capitalize keywords / digital marketing / details resume
        "search_terms": ["resume", "cover letter", "keyword", "marketing", "portfolio", "application", "job"],
        "repo_patterns": [
            "application-pipeline", "portfolio", "cvrsvs-honorvm",
            "kerygma-profiles", "padavano",
        ],
        "file_patterns": ["*resume*", "*cv*", "*cover*letter*", "*portfolio*", "*application*"],
        "domain": "architecture (career/professional materials)",
        "expected_artifacts": [
            "Resume builder with keyword optimization",
            "Cover letter generator",
            "Digital marketing portfolio",
            "Application tracking pipeline",
            "Job search automation",
            "Professional profile sync across platforms",
        ],
    },
    "traj-deep-d68a59f93ad3": {
        # revise / thread / system -- system-level revision and maintenance
        "search_terms": ["revise", "maintain", "refactor", "system", "audit", "lint"],
        "repo_patterns": [
            "auto-revision*", "domus-semper*", "growth-auditor",
            "vigiles-aeternae*", "system-governance*",
        ],
        "file_patterns": ["*audit*", "*maintain*", "*lint*", "*refactor*", "*health*"],
        "domain": "general (system revision/maintenance)",
        "expected_artifacts": [
            "System-wide revision engine",
            "Automated maintenance pipelines",
            "Audit framework (code, governance, security)",
            "Refactoring toolchain",
            "Health check infrastructure",
        ],
    },
    "traj-deep-5abf62d1815c": {
        # draft / rewrite / story -- creative writing, storytelling
        "search_terms": ["draft", "rewrite", "story", "essay", "narrative", "creative writing"],
        "repo_patterns": [
            "essay-pipeline", "editorial-standards", "salon-archive",
            "content-engine*", "narratological*", "carrier-wave*",
            "public-process", "kerygma-pipeline",
        ],
        "file_patterns": ["*story*", "*draft*", "*essay*", "*narrative*", "*rewrite*"],
        "domain": "content (creative writing/storytelling)",
        "expected_artifacts": [
            "Essay drafting pipeline",
            "Story structure templates",
            "Rewrite/revision workflow",
            "Narrative analysis tools",
            "Publishing pipeline (draft -> edit -> publish)",
            "Creative writing portfolio",
        ],
    },
    "traj-deep-f9b5cfb52530": {
        # visual / thread / generative -- generative art, visual creation
        "search_terms": ["visual", "generative", "art", "image", "render", "blender", "three.js", "canvas"],
        "repo_patterns": [
            "blender-mcp", "gemini-cli-blender*", "styx-behavioral-art",
            "sign-signal*", "chthon-oneiros",
        ],
        "file_patterns": ["*generat*art*", "*visual*", "*render*", "*canvas*", "*shader*"],
        "domain": "creative (generative art/visual)",
        "expected_artifacts": [
            "Generative art engine / gallery",
            "Blender automation pipeline",
            "Visual asset creation workflow",
            "Three.js interactive scenes",
            "Canvas/shader experimentation framework",
            "Art deployment pipeline",
        ],
    },
    "traj-471075722596": {
        # cover letter / anthony padavano -- professional identity, career docs
        "search_terms": ["cover letter", "padavano", "resume", "portfolio", "application", "professional"],
        "repo_patterns": [
            "application-pipeline", "padavano", "portfolio",
            "cvrsvs-honorvm", "kerygma-profiles",
        ],
        "file_patterns": ["*cover*", "*letter*", "*padavano*", "*portfolio*", "*bio*"],
        "domain": "content (professional identity/career)",
        "expected_artifacts": [
            "Cover letter generator (role-adaptive)",
            "Professional bio/narrative",
            "Portfolio site deployment",
            "Application materials pipeline",
            "Identity documents (CV, resume, teaching philosophy)",
            "LinkedIn/professional profile automation",
        ],
    },
    "form-merged-2149a80aa514": {
        # protocols + protocol -- governance protocols, SOPs
        "search_terms": ["protocol", "SOP", "governance", "policy", "rule", "standard"],
        "repo_patterns": [
            "system-governance*", "rules-system*", "praxis-perpetua",
            "vigiles-aeternae*", "sovereign*", "custodia*",
        ],
        "file_patterns": ["*protocol*", "*sop*", "*governance*", "*policy*", "*rule*"],
        "domain": "governance (protocols/SOPs)",
        "expected_artifacts": [
            "Protocol registry (searchable, versioned)",
            "SOP lifecycle engine",
            "Governance enforcement hooks",
            "Policy compliance checks",
            "Protocol-to-implementation bridge",
            "Cross-system protocol sync",
        ],
    },
    "traj-deep-765a0f60d268": {
        # building / system / thread -- system building, construction, architecture
        "search_terms": ["build", "system", "architect", "scaffold", "infra", "construct"],
        "repo_patterns": [
            "system-system*", "organvm-engine", "metasystem*",
            "schema-definitions", "orchestration*", "atomic-substrata",
        ],
        "file_patterns": ["*architect*", "*scaffold*", "*build*", "*infra*", "*construct*"],
        "domain": "creative/functional (system building)",
        "expected_artifacts": [
            "System architecture documentation",
            "Scaffolding / boilerplate generator",
            "Infrastructure-as-code templates",
            "Build pipeline automation",
            "Cross-repo dependency management",
            "System composition engine",
        ],
    },
}


def find_repos(patterns: list[str]) -> list[str]:
    """Find repos matching glob patterns under WORKSPACE."""
    found = []
    # Check direct children and one-level-deep org dirs
    search_dirs = [WORKSPACE]
    for d in WORKSPACE.iterdir():
        if d.is_dir() and not d.name.startswith("."):
            search_dirs.append(d)

    for pattern in patterns:
        for sd in search_dirs:
            for item in sd.glob(pattern):
                if item.is_dir():
                    rel = str(item.relative_to(WORKSPACE))
                    if rel not in found:
                        found.append(rel)
    return found


def find_files(patterns: list[str], limit: int = 20) -> list[str]:
    """Find files matching patterns across workspace (shallow, fast)."""
    found = []
    for pattern in patterns:
        try:
            result = subprocess.run(
                ["find", str(WORKSPACE), "-maxdepth", "4", "-name", pattern,
                 "-not", "-path", "*/node_modules/*", "-not", "-path", "*/.git/*",
                 "-not", "-path", "*/venv/*", "-not", "-path", "*/__pycache__/*"],
                capture_output=True, text=True, timeout=10,
            )
            for line in result.stdout.strip().split("\n"):
                if line and len(found) < limit:
                    rel = line.replace(str(WORKSPACE) + "/", "")
                    if rel not in found:
                        found.append(rel)
        except (subprocess.TimeoutExpired, Exception):
            pass
    return found


def check_git_activity(repo_path: str) -> dict:
    """Check recent git activity in a repo."""
    full = WORKSPACE / repo_path
    if not (full / ".git").exists():
        return {"has_git": False, "last_commit": None, "commit_count_30d": 0}
    try:
        result = subprocess.run(
            ["git", "-C", str(full), "log", "--oneline", "-1", "--format=%ci %s"],
            capture_output=True, text=True, timeout=5,
        )
        last = result.stdout.strip() if result.returncode == 0 else None

        result2 = subprocess.run(
            ["git", "-C", str(full), "log", "--oneline", "--since=30 days ago"],
            capture_output=True, text=True, timeout=5,
        )
        count = len(result2.stdout.strip().split("\n")) if result2.stdout.strip() else 0

        return {"has_git": True, "last_commit": last, "commit_count_30d": count}
    except (subprocess.TimeoutExpired, Exception):
        return {"has_git": True, "last_commit": "error", "commit_count_30d": 0}


def grep_workspace(terms: list[str], limit: int = 15) -> list[str]:
    """Grep for terms across workspace (fast, shallow)."""
    found = []
    for term in terms[:3]:  # limit to avoid slowness
        try:
            result = subprocess.run(
                ["grep", "-rl", "--include=*.md", "--include=*.py", "--include=*.sh",
                 "--include=*.toml", "--include=*.yaml", "--include=*.json",
                 "--include=*.zsh", "--include=*.ts",
                 "-m", "1", term, str(WORKSPACE)],
                capture_output=True, text=True, timeout=15,
            )
            for line in result.stdout.strip().split("\n"):
                if line and len(found) < limit:
                    rel = line.replace(str(WORKSPACE) + "/", "")
                    if rel not in found:
                        found.append(rel)
        except (subprocess.TimeoutExpired, Exception):
            pass
    return found


def compute_materialization(repos_found, files_found, git_data, expected_count) -> float:
    """Estimate materialization percentage."""
    score = 0.0
    total_weight = 0.0

    # Repo existence (40%)
    active_repos = sum(1 for r in repos_found if git_data.get(r, {}).get("has_git", False))
    if repos_found:
        repo_score = min(active_repos / max(len(repos_found), 1), 1.0)
    else:
        repo_score = 0.0
    score += 0.4 * repo_score
    total_weight += 0.4

    # Recent activity (30%)
    active_recent = sum(1 for r in repos_found if git_data.get(r, {}).get("commit_count_30d", 0) > 0)
    if repos_found:
        activity_score = min(active_recent / max(len(repos_found), 1), 1.0)
    else:
        activity_score = 0.0
    score += 0.3 * activity_score
    total_weight += 0.3

    # File/artifact density (30%)
    if expected_count > 0:
        artifact_score = min(len(files_found) / (expected_count * 3), 1.0)
    else:
        artifact_score = 0.0
    score += 0.3 * artifact_score
    total_weight += 0.3

    return round(score / total_weight, 2) if total_weight > 0 else 0.0


def derive_gaps(expected_artifacts, repos_found, files_found, git_data) -> list[str]:
    """Determine what is missing."""
    gaps = []
    all_evidence = " ".join(repos_found + files_found).lower()

    for artifact in expected_artifacts:
        # Extract keywords from expected artifact
        keywords = [w.lower() for w in artifact.split() if len(w) > 3]
        matched = any(kw in all_evidence for kw in keywords[:3])
        if not matched:
            gaps.append(artifact)

    # Check for inactive repos
    for repo in repos_found:
        gd = git_data.get(repo, {})
        if gd.get("has_git") and gd.get("commit_count_30d", 0) == 0:
            gaps.append(f"Repo '{repo}' exists but has no activity in 30 days")

    return gaps


def derive_next_actions(gaps, form_label, repos_found) -> list[str]:
    """Generate concrete next actions from gaps."""
    actions = []
    for gap in gaps[:3]:
        if "exists but has no activity" in gap:
            repo_name = gap.split("'")[1]
            actions.append(f"Revive {repo_name}: assess scope, create first issue, push initial commit")
        elif "pipeline" in gap.lower():
            actions.append(f"Build {gap.lower()}: define stages, write CLI entry point, add to justfile")
        elif "template" in gap.lower() or "scaffold" in gap.lower():
            actions.append(f"Create {gap.lower()} in relevant repo with test coverage")
        elif "automation" in gap.lower() or "engine" in gap.lower():
            actions.append(f"Design {gap.lower()}: spec inputs/outputs, build MVP, wire to existing pipeline")
        else:
            actions.append(f"Implement: {gap}")

    if not repos_found:
        actions.insert(0, f"Create seed repo for '{form_label}' domain with README + initial structure")

    return actions[:5]


def main():
    # Load forms
    forms = []
    with open(IDEAL_FORMS_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            forms.append(json.loads(line))

    top10 = sorted(forms, key=lambda x: x.get("facet_count", 0), reverse=True)[:10]
    results = []

    print("=" * 80)
    print("FORM GAP ANALYSIS — Top 10 Ideal Forms by Facet Count")
    print(f"Generated: {datetime.now().isoformat()}")
    print("=" * 80)

    for i, fm in enumerate(top10):
        fid = fm["form_id"]
        label = fm["label"]
        facets = fm["facet_count"]
        config = FORM_SEARCH_CONFIG.get(fid, {})

        print(f"\n{'─' * 70}")
        print(f"  #{i+1}  {label.upper()}")
        print(f"  form_id: {fid}")
        print(f"  facets: {facets} | domain: {config.get('domain', fm.get('domains', {}))}")
        print(f"{'─' * 70}")

        # Search
        repos = find_repos(config.get("repo_patterns", []))
        files = find_files(config.get("file_patterns", []))
        grep_hits = grep_workspace(config.get("search_terms", []))

        # Git activity
        git_data = {}
        for repo in repos:
            git_data[repo] = check_git_activity(repo)

        # Merge evidence
        all_evidence = sorted(set(repos + files + grep_hits))

        # Compute
        expected = config.get("expected_artifacts", [])
        mat_pct = compute_materialization(repos, files + grep_hits, git_data, len(expected))
        gaps = derive_gaps(expected, repos, files + grep_hits, git_data)
        next_actions = derive_next_actions(gaps, label, repos)

        # Print
        print(f"\n  MATERIALIZATION: {int(mat_pct * 100)}%")
        print(f"  Evidence ({len(all_evidence)} items):")
        for ev in all_evidence[:10]:
            gd = git_data.get(ev, {})
            status = ""
            if gd.get("has_git"):
                c30 = gd.get("commit_count_30d", 0)
                status = f" [git: {c30} commits/30d]"
                if gd.get("last_commit"):
                    status += f" last: {gd['last_commit'][:40]}"
            print(f"    + {ev}{status}")
        if len(all_evidence) > 10:
            print(f"    ... and {len(all_evidence) - 10} more")

        if gaps:
            print(f"\n  GAPS ({len(gaps)}):")
            for g in gaps[:6]:
                print(f"    - {g}")
            if len(gaps) > 6:
                print(f"    ... and {len(gaps) - 6} more")

        if next_actions:
            print(f"\n  NEXT ACTIONS:")
            for a in next_actions:
                print(f"    > {a}")

        # Record
        results.append({
            "form_id": fid,
            "label": label,
            "facets": facets,
            "materialized_evidence": all_evidence[:30],
            "gaps": gaps,
            "materialization_pct": mat_pct,
            "next_actions": next_actions,
        })

    # Write output
    with open(OUTPUT_PATH, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    print(f"\n{'=' * 80}")
    print(f"OUTPUT: {OUTPUT_PATH}")
    print(f"{'=' * 80}")

    # Summary table
    print("\n  SUMMARY TABLE")
    print(f"  {'#':<3} {'Label':<45} {'Facets':>6} {'Mat%':>5} {'Gaps':>5}")
    print(f"  {'─'*3} {'─'*45} {'─'*6} {'─'*5} {'─'*5}")
    for i, r in enumerate(results):
        lbl = r["label"][:44]
        print(f"  {i+1:<3} {lbl:<45} {r['facets']:>6} {int(r['materialization_pct']*100):>4}% {len(r['gaps']):>5}")

    total_mat = sum(r["materialization_pct"] for r in results) / len(results)
    total_gaps = sum(len(r["gaps"]) for r in results)
    print(f"\n  AVERAGE MATERIALIZATION: {int(total_mat * 100)}%")
    print(f"  TOTAL GAPS: {total_gaps}")


if __name__ == "__main__":
    main()
