> **Canonical location:** `praxis-perpetua/standards/SOP--stranger-test-protocol.md`. This file is a reference copy retained for local context.

# Stranger Test Protocol

**Purpose:** Validate that the eight-organ system is navigable by someone encountering it for the first time.
**Reference:** Constitution Article V — "A stranger should be able to understand the system by reading public documentation alone."
**Last updated:** 2026-02-16

---

## Overview

The Stranger Test measures whether the ORGANVM system's public documentation is sufficient for a competent developer to understand the system's purpose, structure, and key artifacts without guidance from the system's creator.

This is the first external validation exercise for the system. Results feed into grant applications (addressing the "single-operator" critique) and inform documentation improvements.

---

## Participant Profile

### Required
- Professional software developer or technically fluent graduate student
- Comfortable navigating GitHub (repos, orgs, README files, Actions)
- Familiar with basic concepts: CI/CD, dependency graphs, JSON, Markdown
- No prior exposure to the ORGANVM system, its creator, or this corpus

### Preferred (not required)
- Experience with multi-repo or monorepo architectures
- Familiarity with creative coding, generative art, or institutional governance
- Has evaluated or reviewed open-source projects before

### Disqualifying
- Has previously read any ORGANVM documentation or essays
- Personal relationship with the system creator (social bias)
- Currently collaborating on any repo in the system

---

## Test Environment

The participant receives:
1. The URL of one starting point: `https://github.com/meta-organvm` (the meta-org)
2. A laptop with a browser and terminal (with `gh` CLI authenticated, or just browser-only)
3. This task sheet (Tasks 1–5 below)
4. A timer (administered by the test facilitator)

The participant does **not** receive:
- This protocol document (facilitator-only)
- Any verbal explanation of the system
- Access to private repos, CLAUDE.md, MEMORY.md, or this corpus's `docs/` directory
- Hints or guidance during the test (facilitator observes silently)

---

## Tasks

### Task 1: Identify the System's Purpose (10 minutes)

**Prompt given to participant:**
> Starting from https://github.com/meta-organvm, figure out what this system is and what it's for. Write 2-3 sentences describing it.

**Success criteria:**
- [ ] Identifies that it's a multi-organ/multi-repo creative system (mentions "organs" or "coordinated repos")
- [ ] Identifies that it spans multiple domains (theory, art, commerce — at least 2 of 3)
- [ ] Does NOT confuse it with a single application or library
- [ ] Completed within 10 minutes

**Partial credit:** Identifies it as a multi-repo system but misses the organ metaphor or domain structure.

**What we learn:** Whether the org-level README and repo descriptions communicate the system's nature.

---

### Task 2: Find the Flagship Repo for ORGAN-III (8 minutes)

**Prompt given to participant:**
> ORGAN-III is the "commerce" organ. Find its flagship repository — the most important repo in that organ. Name it and explain what it does.

**Success criteria:**
- [ ] Navigates to the `organvm-iii-ergon` organization
- [ ] Identifies `public-record-data-scrapper` as the flagship (or the repo with highest portfolio_relevance)
- [ ] Provides a roughly accurate description of what the repo does
- [ ] Completed within 8 minutes

**Partial credit:** Finds the org but picks a different repo; or finds the right repo but can't explain what it does.

**What we learn:** Whether the org structure and repo descriptions make it clear which repos are most important.

---

### Task 3: Explain the Dependency Rules (10 minutes)

**Prompt given to participant:**
> The system has rules about which organs can depend on which other organs. Find these rules and explain the key constraint in one sentence.

**Success criteria:**
- [ ] Finds the governance rules (either in `governance-rules.json`, a README, or the orchestration system docs)
- [ ] Correctly states the no-back-edge rule: data flows I -> II -> III, not backwards
- [ ] Understands that ORGAN-IV through Meta are not restricted the same way
- [ ] Completed within 10 minutes

**Partial credit:** Finds that dependencies exist but can't articulate the directional constraint; or states the rule but gets the direction wrong.

**What we learn:** Whether the governance model is discoverable and understandable from public docs.

---

### Task 4: Locate the Essay About AI Transparency (6 minutes)

**Prompt given to participant:**
> The system includes essays published on a public blog. Find the essay that discusses AI transparency or honesty in how the system was built. Provide its title or URL.

**Success criteria:**
- [ ] Navigates to `organvm-v-logos/public-process` (the essays repo)
- [ ] Finds the `_posts/` directory
- [ ] Identifies the honesty/transparency essay (published during VERITAS sprint)
- [ ] Completed within 6 minutes

**Partial credit:** Finds the essays repo but can't locate the specific essay; or finds a different essay and explains why they think it's about transparency.

**What we learn:** Whether essay discoverability works — can someone find a specific piece of content?

---

### Task 5: Assess System Health (12 minutes)

**Prompt given to participant:**
> Look at the system and tell me: does it seem healthy and actively maintained, or does it seem abandoned? Give 3 specific pieces of evidence for your assessment.

**Success criteria:**
- [ ] Provides at least 3 concrete observations (e.g., recent commits, CI status, documentation quality, repo activity)
- [ ] Assessment is based on evidence, not impression
- [ ] Evidence is accurate (not misread dates, counts, or statuses)
- [ ] Completed within 12 minutes

**Partial credit:** Provides fewer than 3 observations; or provides observations but draws incorrect conclusions from them.

**What we learn:** Whether the system's health signals (CI badges, commit history, documentation quality) are visible and interpretable.

---

## Scoring

| Task | Max Points | Criteria |
|------|-----------|----------|
| Task 1 | 3 | 1 per success criterion met (excluding time) |
| Task 2 | 3 | 1 per success criterion met (excluding time) |
| Task 3 | 3 | 1 per success criterion met (excluding time) |
| Task 4 | 3 | 1 per success criterion met (excluding time) |
| Task 5 | 3 | 1 per success criterion met (excluding time) |
| **Time bonus** | 5 | 1 point per task completed within time limit |
| **Total** | **20** | |

### Thresholds

| Score | Interpretation |
|-------|---------------|
| 16-20 | **PASS** — System is navigable by strangers |
| 11-15 | **PASS WITH NOTES** — Mostly navigable, specific improvements needed |
| 6-10 | **MARGINAL** — Significant documentation gaps; prioritize fixes |
| 0-5 | **FAIL** — System is not externally navigable; major rework needed |

---

## Feedback Questions (Post-Test)

Administer these after all 5 tasks, regardless of completion.

### Structured Questions (1-5 scale)

1. **Clarity:** "How clear was the system's purpose?" (1 = completely unclear, 5 = immediately obvious)
2. **Navigation:** "How easy was it to find things?" (1 = lost the whole time, 5 = intuitive)
3. **Documentation quality:** "How well-written were the READMEs and docs you read?" (1 = confusing, 5 = excellent)
4. **Coherence:** "Did the system feel like one coordinated thing, or a collection of unrelated repos?" (1 = unrelated, 5 = clearly coordinated)
5. **Credibility:** "Does this system seem like a real, maintained project?" (1 = seems abandoned/fake, 5 = clearly real and active)

### Open-Ended Questions

6. "What was the single most confusing thing you encountered?"
7. "What would have helped you most in the first 5 minutes?"
8. "If you had to explain this system to a colleague in one sentence, what would you say?"
9. "Would you star, fork, or bookmark any of the repos you saw? Which ones and why?"
10. "Any other observations, frustrations, or suggestions?"

---

## Analysis Template

After running the test, complete this summary:

```markdown
## Stranger Test Results — [Participant Pseudonym]

**Date:** YYYY-MM-DD
**Participant profile:** [e.g., "Senior backend engineer, 6 years experience, no prior exposure"]
**Total score:** X / 20

### Per-Task Results

| Task | Score | Time | Notes |
|------|-------|------|-------|
| 1. System purpose | /3 | Xm | |
| 2. ORGAN-III flagship | /3 | Xm | |
| 3. Dependency rules | /3 | Xm | |
| 4. AI transparency essay | /3 | Xm | |
| 5. System health | /3 | Xm | |
| Time bonus | /5 | | |

### Structured Feedback

| Question | Score (1-5) |
|----------|-------------|
| Clarity | |
| Navigation | |
| Documentation quality | |
| Coherence | |
| Credibility | |

### Key Findings

1. **Biggest friction point:** [from Q6]
2. **First-5-minutes gap:** [from Q7]
3. **One-sentence summary:** [from Q8]
4. **Would bookmark:** [from Q9]

### Recommended Actions

1. [Specific documentation change based on findings]
2. [Specific documentation change based on findings]
3. [Specific documentation change based on findings]
```

---

## Logistics Notes

- **Recording:** Ask participant's permission to screen-record. If declined, the facilitator takes timestamped notes.
- **Think-aloud:** Encourage (but don't require) the participant to think aloud while working.
- **No help:** The facilitator does not answer questions about the system during the test. If the participant is stuck, note what they're stuck on — that's data.
- **Breaks:** The test takes ~46 minutes of task time plus ~15 minutes for feedback. Total: ~60 minutes. No breaks needed unless requested.
- **Compensation:** Budget for a thank-you (coffee, book, etc.). This is a favor, not a job.
