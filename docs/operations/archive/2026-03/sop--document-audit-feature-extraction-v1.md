# SOP: Document Audit & Feature Extraction

**Created:** 2026-03-04
**Author:** @4444j99 (AI-conductor model: human directs, AI generates, human reviews)
**Status:** ACTIVE — Living document, updated as process evolves
**Companions:** [`key-workflows.md`](./key-workflows.md) (procedures), [`operational-cadence.md`](./operational-cadence.md) (rhythm), [`minimum-viable-operations.md`](./minimum-viable-operations.md) (maintenance)
**Constitution:** [`docs/memory/constitution.md`](../memory/constitution.md) — Articles I-VI govern all specifications

---

> *Every project accumulates documentation that contains product ideas nobody has tracked. This SOP turns that latent value into actionable GitHub issues, systematically and repeatably.*

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Prerequisites](#2-prerequisites)
3. [Phase 1 — Inventory & Triage](#3-phase-1--inventory--triage)
4. [Phase 2 — Exhaustive Read & Extraction](#4-phase-2--exhaustive-read--extraction)
5. [Phase 3 — Deduplication](#5-phase-3--deduplication)
6. [Phase 4 — Issue Creation](#6-phase-4--issue-creation)
7. [Phase 5 — Post-Audit Artifacts](#7-phase-5--post-audit-artifacts)
8. [Appendices](#8-appendices)

---

## 1. Purpose & Scope

### What this SOP does

This procedure takes a repository's `docs/` directory (or equivalent documentation corpus) and produces a complete set of GitHub issues — one for every product idea, feature concept, architectural suggestion, or behavioral insight buried in the documentation. The audit is **exhaustive**: every document is read word-for-word, not skimmed or summarized.

### When to run it

| Trigger | Description |
|---------|-------------|
| **New repo onboarding** | When a repo first enters the system with existing documentation |
| **Major doc additions** | When a bulk import of research, brainstorm transcripts, or external references lands in a repo |
| **Quarterly review** | Part of the Week 4 monthly review cycle (see [`operational-cadence.md`](./operational-cadence.md), Part II, Week 4) |
| **Pre-beta audit** | Before a product enters private or public beta, to ensure nothing in the docs was forgotten |
| **Post-mortem** | After a failed launch or missed deadline, to capture lessons from planning docs |

### What it applies to

Any repo in any organ with documentation that may contain untracked product or feature ideas. This includes:
- Standard `docs/` directories (research, brainstorm, legal, architecture, planning)
- `specs/` directories (RFCs, ADRs, technical specifications)
- `design/` directories (design documents, wireframes with annotations)
- Root-level markdown files (README, CONTRIBUTING, ARCHITECTURE)
- External reference libraries (books, papers, articles in `docs/research/reference-library/`)

The procedure is organ-agnostic. It works identically for ORGAN-I theory repos, ORGAN-II creative repos, ORGAN-III products, and ORGAN-V editorial repos. Adapt the issue labels and terminology to the organ's domain.

---

## 2. Prerequisites

### Required artifacts

| Artifact | Required? | Purpose |
|----------|-----------|---------|
| `FEATURE-BACKLOG.md` (or equivalent) | Recommended | Deduplication target — avoids creating issues for already-tracked features. If it doesn't exist, the audit will create one as an output artifact. |
| `MANIFEST.md` (or equivalent) | Recommended | Document index with stable IDs. If it doesn't exist, Phase 1 builds one. |
| `seed.yaml` | Required | Confirms organ membership, tier, and promotion status. Determines label taxonomy. |
| Project `CLAUDE.md` | Required | Provides project context, architecture, conventions. Read before starting. |

### Required tools

| Tool | Purpose | Install |
|------|---------|---------|
| `gh` CLI | GitHub issue creation, label management, issue listing | `brew install gh` + `gh auth login` |
| Claude Code (or manual) | Exhaustive document reading and extraction | Already available in this context |
| `pandoc` | Format conversion (epub → plain text, docx → markdown) | `brew install pandoc` |
| Calibre (optional) | AZW3/MOBI → EPUB conversion (Amazon DRM-free only) | `brew install --cask calibre` |

### Required access

- GitHub repo write access (push to default branch)
- GitHub issue creation permissions
- Read access to all files in the documentation corpus

### Pre-audit checklist

Before starting the audit, complete these steps in order:

- [ ] Read the project's `CLAUDE.md` (root level and `docs/CLAUDE.md` if it exists)
- [ ] Read `seed.yaml` — note organ, tier, promotion status
- [ ] Inventory all open GitHub issues: `gh issue list --repo <org>/<repo> --state open --limit 500`
- [ ] Read `FEATURE-BACKLOG.md` if it exists — note all `F-*` IDs and their statuses
- [ ] Read `MANIFEST.md` if it exists — note all `DOC-*` IDs
- [ ] Confirm label taxonomy exists on the repo (create labels if needed — see [Phase 4](#6-phase-4--issue-creation))

---

## 3. Phase 1 — Inventory & Triage

**Goal:** Build a complete map of every document in the corpus before reading anything.

### Step 1: List all documentation files

```bash
cd <repo-root>
find docs/ -type f | sort
```

Or with Claude Code:
```
Glob: docs/**/*
```

### Step 2: Classify by format

Create a working inventory. For each file, record:

| Field | Description |
|-------|-------------|
| **Path** | Relative path from repo root |
| **Format** | `markdown`, `pdf`, `epub`, `azw3`, `txt`, `docx`, `pptx`, `binary`, `asset` |
| **Readable?** | Yes / Needs conversion / Unreadable |
| **Category** | `research`, `brainstorm`, `legal`, `architecture`, `planning`, `pitch`, `reference`, `governance`, `asset` |
| **Size** | Approximate word count or page count |

### Step 3: Convert unreadable formats

For each file that needs conversion:

```bash
# EPUB → plain text
pandoc -f epub -t plain "docs/research/reference-library/author--title.epub" \
  -o "/tmp/author--title.txt"

# DOCX → markdown
pandoc -f docx -t markdown "docs/planning/roadmap.docx" \
  -o "/tmp/roadmap.md"

# PDF → plain text (pandoc, best-effort)
pandoc -f pdf -t plain "docs/pitch/deck.pdf" \
  -o "/tmp/deck.txt"

# AZW3 → EPUB → plain text (requires Calibre)
ebook-convert "docs/research/reference-library/author--title.azw3" \
  "/tmp/author--title.epub"
pandoc -f epub -t plain "/tmp/author--title.epub" \
  -o "/tmp/author--title.txt"
```

**Note conversion failures.** Some formats (DRM-protected files, scanned PDFs without OCR, proprietary binary formats) cannot be converted. Record these as gaps in the audit summary.

### Step 4: Build the document manifest

If no `MANIFEST.md` exists, create one using this structure (adapted from the Styx project):

```markdown
# Project Manifest: Annotated Document Index

**Version**: 1.0.0
**Project**: <project-name>
**Document Count**: <N> entries
**Generated**: <YYYY-MM-DD>

---

## Category: Research

| ID | File | Tags | Annotation |
|----|------|------|------------|
| DOC-RES-01 | `docs/research/topic-name.md` | #research #domain | Brief description |

## Category: Architecture
...
```

Assign stable `DOC-*` IDs using the pattern `DOC-{CATEGORY}-{NN}`:
- `DOC-RES-*` — Research
- `DOC-BRN-*` — Brainstorm
- `DOC-LEG-*` — Legal
- `DOC-ARC-*` — Architecture
- `DOC-PLN-*` — Planning
- `DOC-PIT-*` — Pitch
- `DOC-REF-*` — Reference library (external sources)
- `DOC-GOV-*` — Governance

### Phase 1 output

A complete inventory document (or updated `MANIFEST.md`) showing every file, its format, readability status, and category. This is the roadmap for Phase 2.

---

## 4. Phase 2 — Exhaustive Read & Extraction

**Goal:** Read every document word-for-word and extract every actionable idea.

### The cardinal rule

**Read every word.** Do not skim. Do not summarize from headings. Do not skip sections that "look like boilerplate." The most valuable feature ideas are often buried in parenthetical remarks, footnotes, section transitions, or "future work" paragraphs that a skimmer would miss.

### Reading order

Process documents **by folder**, not alphabetically. This preserves thematic context:

1. **Brainstorm** first — raw ideas, unfiltered. Highest density of novel concepts.
2. **Research** second — theoretical frameworks, competitor analysis, behavioral science. Ideas here are grounded in evidence.
3. **Legal** third — compliance constraints often imply required features (age gates, geofencing, dispute resolution).
4. **Architecture** fourth — technical decisions often imply features that were planned but never tracked.
5. **Planning** fifth — roadmaps, implementation status docs, ship reports. Cross-reference against what was actually built.
6. **Reference library** last — external books and papers. Read in full; extract actionable product implications from theoretical frameworks.

### Extraction format

For each idea extracted, record:

```markdown
### [EXT-NNN] Extraction Title

- **Source**: `docs/research/filename.md`, Section "Section Name" (or page N for books)
- **Quote/Paraphrase**: Verbatim quote or close paraphrase of the relevant passage
- **Idea**: What product feature, behavioral mechanism, or architectural change this implies
- **Category**: `core-mechanics` | `ux` | `compliance` | `behavioral-science` | `infrastructure` | `business-model` | `security` | `social` | `mobile` | `b2b` | etc.
```

### Extraction heuristics

Look for these signals in every document:

| Signal | Example | Likely extraction |
|--------|---------|-------------------|
| "We could..." / "We should..." / "Consider..." | "We could add a spectator mode" | Feature idea |
| "The research shows..." / "Studies indicate..." | "Loss aversion coefficient is 1.955" | Behavioral constant or algorithm parameter |
| "Legal requirement" / "Must comply with..." | "Must verify age 18+ before staking" | Compliance feature |
| "Not yet implemented" / "Future work" / "Phase 2+" | "Phase 2: PvP lobbies" | Backlog item |
| Architectural diagrams with unbuilt components | "Oracle Network (planned)" | Infrastructure feature |
| Competitor analysis gaps | "Competitor X doesn't offer Y" | Differentiator feature |
| User journey steps without code | "User receives push notification" | Missing implementation |
| "Risk: ..." / "Mitigation: ..." | "Risk: users fabricate proofs" | Security feature |

### Parallelization (Claude Code)

For large corpora (20+ documents), parallelize reads using Claude Code agents:

```
- Agent 1: docs/brainstorm/ (all files)
- Agent 2: docs/research/ (markdown files)
- Agent 3: docs/research/reference-library/ (converted text files)
- Agent 4: docs/legal/ + docs/architecture/
- Agent 5: docs/planning/
```

**Constraint:** On 16GB RAM systems, limit to 5 concurrent agents. Each agent produces its own extraction list; merge in Phase 3.

### Phase 2 output

A consolidated extraction list organized by source folder. Each extraction has a unique `EXT-NNN` ID, source citation, verbatim quote, and categorized idea.

---

## 5. Phase 3 — Deduplication

**Goal:** Eliminate duplicates and classify each extraction as skip, enhance, or create.

### Cross-reference targets

Every extraction must be checked against three sources:

#### 1. Feature backlog (`FEATURE-BACKLOG.md`)

If the project has an existing feature backlog with `F-*` IDs:
- Search for each extraction's keywords in the backlog
- If an `F-*` entry covers the same idea: **SKIP** (already tracked)
- If an `F-*` entry partially covers it: **ENHANCE** (note the `F-*` ID for cross-reference in the issue)

#### 2. Open GitHub issues

```bash
# List all open issues with titles
gh issue list --repo <org>/<repo> --state open --limit 500 --json number,title

# Search for a specific keyword
gh issue list --repo <org>/<repo> --search "keyword" --state open
```

- If an open issue covers the same idea: **SKIP**
- If an open issue partially overlaps: **ENHANCE** (reference the issue number)

#### 3. Codebase (implemented but untracked)

```bash
# Search for feature keywords in source code
grep -r "keyword" src/ --include="*.ts" --include="*.tsx" -l
```

Or with Claude Code:
```
Grep: pattern="keyword" path="src/"
```

- If the feature is already implemented with tests: **SKIP** (optionally create a documentation issue)
- If partially implemented: **ENHANCE** (note the existing code paths)

### Merge overlapping extractions

Multiple documents often describe the same idea from different angles. When two or more extractions from different documents describe the same feature:

1. Merge them into a single candidate
2. List all source documents in the merged entry
3. Choose the most specific/detailed description as the primary
4. Retain unique details from each source as supplementary requirements

### Classification output

Each extraction gets one of three labels:

| Label | Action | Reason |
|-------|--------|--------|
| **SKIP** | Do nothing | Already tracked in backlog, open issue, or implemented code |
| **ENHANCE** | Update existing issue or backlog entry | Partially tracked — new details from this extraction add value |
| **CREATE** | New GitHub issue | Genuinely new idea not tracked anywhere |

### Phase 3 output

A deduplicated candidate list where each entry is classified as SKIP, ENHANCE, or CREATE, with cross-references to existing tracking (issue numbers, `F-*` IDs, code paths).

---

## 6. Phase 4 — Issue Creation

**Goal:** Create one GitHub issue per CREATE candidate, update existing issues for ENHANCE candidates.

### Label taxonomy

Before creating issues, ensure the repo has these labels (create any that are missing):

```bash
# Core labels (every repo)
gh label create "enhancement" --description "New feature or request" --color "a2eeef" --repo <org>/<repo>
gh label create "documentation" --description "Documentation improvements" --color "0075ca" --repo <org>/<repo>

# Domain labels (adapt to project)
gh label create "behavioral-science" --description "Behavioral economics and psychology" --color "d4c5f9" --repo <org>/<repo>
gh label create "compliance" --description "Legal and regulatory requirements" --color "e4e669" --repo <org>/<repo>
gh label create "ux" --description "User experience and interface" --color "7057ff" --repo <org>/<repo>
gh label create "infrastructure" --description "Backend, DevOps, architecture" --color "f9d0c4" --repo <org>/<repo>
gh label create "security" --description "Security features and hardening" --color "b60205" --repo <org>/<repo>
gh label create "mobile" --description "Mobile app features" --color "0e8a16" --repo <org>/<repo>
gh label create "business-model" --description "Revenue, pricing, partnerships" --color "fbca04" --repo <org>/<repo>
```

### Issue title format

```
feat: {descriptive title in lowercase}
```

Examples:
- `feat: add spectator mode for public contract viewing`
- `feat: implement pod-based cohorts (max 5 members)`
- `feat: integrate Whoop webhook for sleep score verification`

### Issue body template

Every issue must use this structured template:

````markdown
## Source

- **Document(s)**: `docs/research/filename.md` (Section "X"), `docs/brainstorm/filename.md`
- **Author(s)**: Original document author(s) if known
- **Extraction ID(s)**: EXT-042, EXT-067 (merged)

## Problem

What gap, opportunity, or user need does this address? 2-3 sentences max.

## Proposed Feature

1. **Requirement 1**: Description
2. **Requirement 2**: Description
3. **Requirement 3**: Description

### Design sketch (if applicable)

Brief architectural notes, API shape, or UI behavior.

## Cross-References

- **Backlog**: F-CATEGORY-NN (if partially tracked)
- **Related issues**: #42, #67 (if related but not duplicate)
- **Code paths**: `src/api/services/module/file.ts` (if partially implemented)
- **External**: Link to research paper, competitor, or standard (if applicable)

## Labels

`enhancement`, `domain-label`
````

### Batch creation strategy

Create issues in **thematic groups**, not in document order. This produces coherent issue clusters:

1. Group all CREATE candidates by category (ux, compliance, behavioral-science, etc.)
2. Within each group, sort by priority (P0 before P1, P1 before P2)
3. Create all issues in one group before moving to the next
4. Between groups, update the running tally

### Running tally

Maintain a running count during creation:

```
Folder: brainstorm/     — 12 issues created (#46-#57)
Folder: research/       — 28 issues created (#58-#85)
Folder: legal/          — 8 issues created (#86-#93)
Folder: architecture/   — 6 issues created (#94-#99)
Folder: planning/       — 4 issues created (#100-#103)
Folder: reference-lib/  — 16 issues created (#104-#119)
─────────────────────────────────────────────
Total: 74 issues created (#46-#119)
```

### Batch `gh` commands

For efficiency, create issues from the command line:

```bash
gh issue create \
  --repo <org>/<repo> \
  --title "feat: descriptive title" \
  --body "$(cat <<'EOF'
## Source
...issue body here...
EOF
)" \
  --label "enhancement" \
  --label "behavioral-science"
```

### ENHANCE workflow

For ENHANCE candidates (existing issues that need supplementary detail):

```bash
gh issue comment <issue-number> \
  --repo <org>/<repo> \
  --body "$(cat <<'EOF'
## Additional Context from Document Audit

**Source**: `docs/research/filename.md`, Section "X"
**New detail**: Description of what this extraction adds to the existing issue.
EOF
)"
```

### Phase 4 output

All CREATE candidates have been filed as GitHub issues. All ENHANCE candidates have been commented on existing issues. The running tally is complete.

---

## 7. Phase 5 — Post-Audit Artifacts

**Goal:** Update project metadata and leave a clean audit trail.

### Step 1: Update FEATURE-BACKLOG.md

If the project uses a feature backlog with `F-*` IDs:

1. Add new `F-*` entries for each created issue
2. Set status to `NOT_STARTED`
3. Add source citations (backreferencing doc filenames)
4. Update the executive summary counts
5. Update the source-to-feature reverse mapping table (if one exists)

If the project does not have a feature backlog, create one using the template from the Styx project (`docs/FEATURE-BACKLOG.md`) as reference. At minimum, include:
- Feature ID (`F-{CATEGORY}-{NN}`)
- Title
- Status (`IMPLEMENTED`, `PARTIAL`, `STUB`, `NOT_STARTED`)
- Priority (`P0`, `P1`, `P2`, `P3`)
- Source document(s)
- GitHub issue number

### Step 2: Update MANIFEST.md

If new documents were discovered or created during the audit:

1. Assign `DOC-*` IDs to any new files
2. Add entries to the appropriate category table
3. Update the document count in the header
4. Update the version number

### Step 3: Create a reference syllabus (if reference library was audited)

When the audit included external books, papers, or articles, produce a structured reading list:

```markdown
# Reference Syllabus: <Project Name>

## Core Reading (directly informs product design)
1. **Author — Title** (format). Key takeaway: ...
2. ...

## Supplementary Reading (broader context)
1. ...

## Recommended Further Reading (not yet in library)
1. ...
```

Place in `docs/research/reference-library/SYLLABUS.md` (or equivalent).

### Step 4: Write the audit summary

Create a summary file or section documenting what was done:

```markdown
# Document Audit Summary

**Date**: YYYY-MM-DD
**Repo**: <org>/<repo>
**Auditor**: @username (with Claude Code)

## Scope
- Folders audited: brainstorm/, research/, legal/, architecture/, planning/, research/reference-library/
- Documents read: N (of M total files)
- Formats converted: epub (N), pdf (N), azw3 (N)
- Conversion failures: <list any>

## Results
- Extractions identified: N
- After deduplication: N candidates
  - SKIP (already tracked): N
  - ENHANCE (updated existing): N
  - CREATE (new issues): N

## Issues Created
- Range: #<first> – #<last>
- By folder:
  - brainstorm/: N issues
  - research/: N issues
  - ...
- By category:
  - behavioral-science: N
  - ux: N
  - ...

## Gaps
- Unreadable files: <list>
- Documents with no actionable extractions: <list>
- Areas needing further research: <list>

## Artifacts Updated
- [ ] FEATURE-BACKLOG.md — N new entries added
- [ ] MANIFEST.md — N new documents indexed
- [ ] SYLLABUS.md — created/updated
- [ ] This summary committed
```

Place this summary in `docs/planning/` or as a comment on a tracking issue.

### Step 5: Commit and push

```bash
git add docs/FEATURE-BACKLOG.md docs/MANIFEST.md docs/research/reference-library/SYLLABUS.md
git add docs/planning/audit-summary--YYYY-MM-DD.md  # if created
git commit -m "docs: complete document audit — N issues created (#first-#last)"
git push origin <branch>
```

---

## 8. Appendices

### Appendix A: Format Conversion Reference

| Source Format | Target | Command | Notes |
|---------------|--------|---------|-------|
| EPUB | Plain text | `pandoc -f epub -t plain input.epub -o output.txt` | Best for prose books. Preserves chapter structure. |
| EPUB | Markdown | `pandoc -f epub -t markdown input.epub -o output.md` | Preserves formatting, headers, emphasis. |
| PDF | Plain text | `pandoc -f pdf -t plain input.pdf -o output.txt` | Works for text-based PDFs. Fails on scanned/image PDFs. |
| PDF (scanned) | Plain text | `tesseract input.pdf output -l eng pdf` | Requires `brew install tesseract`. Quality varies. |
| DOCX | Markdown | `pandoc -f docx -t markdown input.docx -o output.md` | Excellent conversion quality. |
| AZW3 | EPUB | `ebook-convert input.azw3 output.epub` | Requires Calibre. DRM-free only. |
| PPTX | Markdown | `pandoc -f pptx -t markdown input.pptx -o output.md` | Extracts text from slides; loses layout. |
| HTML | Markdown | `pandoc -f html -t markdown input.html -o output.md` | Good for saved web pages. |

**When conversion fails:**
1. Note the file in the audit summary under "Gaps"
2. Record what format it is and why conversion failed (DRM, scanned image, corrupted)
3. If the content is important, consider manual transcription or OCR alternatives
4. Do not skip the file silently — every gap must be documented

### Appendix B: Issue Body Template (Copy-Paste)

````markdown
## Source

- **Document(s)**: `docs/category/filename.md` (Section "X")
- **Author(s)**:
- **Extraction ID(s)**: EXT-NNN

## Problem

[What gap or opportunity this addresses]

## Proposed Feature

1. **Requirement**: [Description]
2. **Requirement**: [Description]

## Cross-References

- **Backlog**: F-CATEGORY-NN
- **Related issues**: #N
- **Code paths**: `src/path/to/file.ts`
````

### Appendix C: Claude Code Parallelization Guide

For corpora with 20+ documents, use parallel Claude Code agents to read documents simultaneously. This is the recommended approach for large audits.

**Setup:**

```
Agent 1 (brainstorm):
  "Read every file in docs/brainstorm/ word-for-word. For each product idea,
   feature concept, or architectural suggestion, extract it with: source file,
   section, verbatim quote, and categorized idea. Output as a numbered list."

Agent 2 (research - markdown):
  "Read every .md file in docs/research/ word-for-word. [same instructions]"

Agent 3 (reference library):
  "Read every .txt and .md file in docs/research/reference-library/ word-for-word.
   For each book/paper, note the theoretical framework and extract every
   actionable product implication. [same format]"

Agent 4 (legal + architecture):
  "Read every file in docs/legal/ and docs/architecture/ word-for-word.
   [same instructions]"

Agent 5 (planning):
  "Read every file in docs/planning/ word-for-word. Pay special attention to
   'future work' sections, planned-but-unbuilt features, and roadmap items
   that haven't been implemented. [same format]"
```

**Constraints:**
- Maximum 5 concurrent agents on 16GB RAM systems
- Each agent should output a structured extraction list, not prose
- Merge agent outputs in Phase 3 (deduplication) — expect 10-30% overlap between agents reading related docs
- If an agent's output is truncated, split its folder assignment across two agents

**Timing estimates:**
- 10-document corpus: 1 agent, ~30 minutes
- 30-document corpus: 3-4 agents, ~45 minutes
- 60+ document corpus: 5 agents, ~90 minutes
- Reference library (full books): 1 dedicated agent per 2-3 books, ~60 minutes per agent

### Appendix D: Adapting for Non-`docs/` Repos

Not all repos organize documentation under `docs/`. Here's how to apply this SOP to alternative structures:

| Structure | Where to look | Adaptation |
|-----------|---------------|------------|
| **RFC directory** (`rfcs/` or `rfc/`) | Each RFC is a self-contained proposal. Treat each RFC as a brainstorm document. | Extract unimplemented proposals, rejected alternatives worth revisiting, and open questions. |
| **ADR directory** (`adr/` or `docs/adr/`) | Architecture Decision Records. | Focus on "Consequences" and "Alternatives Considered" sections — rejected alternatives often contain feature ideas. |
| **Design docs** (`design/` or `docs/design/`) | Detailed feature specifications. | Cross-reference each design against codebase to find unimplemented sections. |
| **Wiki** (GitHub Wiki) | Clone locally: `git clone <repo>.wiki.git` | Treat wiki pages as brainstorm documents. Wikis often contain undocumented feature discussions. |
| **Issue comments** | `gh api repos/<org>/<repo>/issues/<n>/comments` | For repos where design happens in issues, audit closed issue threads for unextracted ideas. |
| **PR descriptions** | `gh pr list --state merged --limit 100 --json title,body` | Large PRs sometimes describe features that were partially implemented or deferred. |
| **README sections** | Root `README.md`, "Roadmap" or "Future" sections | Often contains aspirational feature lists that were never tracked as issues. |

### Appendix E: Cross-Reference to Governance

This SOP exists within the governance framework of the eight-organ system. Key connections:

| Document | Relationship |
|----------|-------------|
| [`docs/memory/constitution.md`](../memory/constitution.md) | Articles I-VI govern all specifications including this SOP. Article III (dependency flow) constrains which organs can produce features for which. |
| [`governance-rules.json`](../../governance-rules.json) | Defines promotion state machine and dependency edges. When creating issues, respect the organ's tier and promotion status from `seed.yaml`. |
| [`key-workflows.md`](./key-workflows.md) | Workflow #7 references this SOP. After completing an audit, use Workflow #1 (Update the Registry) if repo metadata changed. |
| [`operational-cadence.md`](./operational-cadence.md) | Document audits fit into the Week 4 (Review + Maintenance) cycle of the monthly cadence. Audits for ORGAN-III products align with Tuesday/Thursday product days. |
| [`minimum-viable-operations.md`](./minimum-viable-operations.md) | If the audit reveals system maintenance issues (broken links, missing CI, stale configs), log them through MVO procedures rather than creating feature issues. |
| [`concordance.md`](./concordance.md) | Use the concordance for ID format lookups (DOC-*, F-*, EXT-*) and cross-organ reference resolution. |

---

## Quick Reference Card

```
╔══════════════════════════════════════════════════════════════╗
║      DOCUMENT AUDIT & FEATURE EXTRACTION — QUICK REF        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  PHASE 1: INVENTORY                                          ║
║  □ List all docs/  files (Glob or find)                      ║
║  □ Classify format + readability                             ║
║  □ Convert unreadable formats (pandoc/calibre)               ║
║  □ Build or update MANIFEST.md                               ║
║                                                              ║
║  PHASE 2: READ & EXTRACT                                     ║
║  □ Read EVERY document word-for-word                         ║
║  □ Order: brainstorm → research → legal → arch → planning    ║
║  □ Extract: source, quote, idea, category                    ║
║  □ Parallelize with 5 agents if 20+ docs                    ║
║                                                              ║
║  PHASE 3: DEDUPLICATE                                        ║
║  □ Cross-ref: FEATURE-BACKLOG.md                             ║
║  □ Cross-ref: open GitHub issues                             ║
║  □ Cross-ref: codebase (grep for implemented)                ║
║  □ Label each: SKIP / ENHANCE / CREATE                       ║
║                                                              ║
║  PHASE 4: CREATE ISSUES                                      ║
║  □ Title: "feat: lowercase description"                      ║
║  □ Body: Source → Problem → Proposed Feature → Cross-Refs    ║
║  □ Labels: enhancement + domain labels                       ║
║  □ Batch by theme, not document order                        ║
║  □ Maintain running tally by folder                          ║
║                                                              ║
║  PHASE 5: POST-AUDIT                                         ║
║  □ Update FEATURE-BACKLOG.md                                 ║
║  □ Update MANIFEST.md                                        ║
║  □ Create SYLLABUS.md (if reference library audited)         ║
║  □ Write audit summary                                       ║
║  □ Commit + push                                             ║
║                                                              ║
║  COMMANDS                                                    ║
║  gh issue list --repo O/R --state open --limit 500           ║
║  gh issue create --repo O/R --title "feat: ..." --body "..." ║
║  gh issue comment N --repo O/R --body "..."                  ║
║  pandoc -f epub -t plain in.epub -o out.txt                  ║
║  pandoc -f pdf -t plain in.pdf -o out.txt                    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

*This SOP was derived from the first execution of this procedure on the Styx project (`peer-audited--behavioral-blockchain`), which audited 37+ documents across 6 folders and produced 74 GitHub issues (#46–#119) on 2026-03-04. The procedure is now codified for reuse across all ~111 repos in the eight-organ system.*
