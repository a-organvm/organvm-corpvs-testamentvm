# 14: Logos Documentation Layer

**Date:** 2026-04-02
**Status:** ACTIVE — applies to all non-archived repositories
**Derived from:** Amendment K (Lex Umbrae Naturae)
**Complements:** `10-repository-standards.md`, `11-specification-driven-development.md`

---

## 1. Purpose & Scope

The **Logos Documentation Layer** enforces the **Required Relationship** between implementation (Nature) and record (Counterpart). It ensures that every repository in the ORGANVM ecosystem maintains a narrative expression of its existence, facilitating system-wide coherence and public discourse.

This standard mandates the creation and maintenance of the `docs/logos/` directory in every repository.

---

## 2. The Logos Directory Structure

Every repository must contain a `docs/logos/` directory with the following mandatory files:

| File | Purpose | Content Requirement |
|------|---------|---------------------|
| `telos.md` | The Idealized Form | The dream, the theory, and the idealized functionalities. Why does this exist? |
| `pragma.md` | The Concrete Realization | The honest account of what has been built. How far is it from the telos? |
| `praxis.md` | The Remediation Plan | Attack vectors for closing the gap between telos and pragma. |
| `receptio.md` | The Account of Reception | How has this been received by the world or the constructed polis? |
| `alchemical-io.md` | Signal Transformations | Narrative of the formation's metabolic inputs, processes, and outputs. |

### Relationship to `seed.yaml`

The fields `telos`, `pragma`, `praxis`, and `receptio` in `seed.yaml` (schema v1.2) are **summaries**. The corresponding `.md` files in `docs/logos/` are **narratives**. 

- `seed.yaml`: Machine-readable summary (1-2 paragraphs each).
- `docs/logos/*.md`: Human-readable depth (full essays/records).

---

## 3. Alchemical I/O Narrative

The `alchemical-io.md` file is a unique requirement of the Logos Layer. It describes the "Nature" of the repository using the system's alchemical/metabolic vocabulary.

**Required Sections:**
1. **Source (Inputs):** What raw materials or signals does this formation consume?
2. **Transmutation (Process):** What is the core alchemical operation performed? (e.g., distillation, coagulation, calcination).
3. **Return (Outputs):** What refined signals or artifacts are returned to the system?
4. **Future Self:** How does this implementation feed the formation's evolution?

---

## 4. Enforcement (Ghosts & Dreams)

The system enforces symmetry via the following classifications:

- **Ghost:** A repository with high implementation mass (code) but missing or empty `docs/logos/`.
- **Dream:** A repository with a lush `docs/logos/` but zero implementation (empty `src/` or equivalent).

### Compliance Gates

| Status | Logos Layer Requirement |
|--------|--------------------------|
| **INCUBATOR** | Not required. |
| **LOCAL** | Scaffolding required (`docs/logos/` exists). |
| **CANDIDATE** | Drafts of all 5 files required. |
| **PUBLIC_PROCESS** | Complete, peer-reviewed narratives required. |
| **GRADUATED** | Fully verified symmetry required. |

---

## 5. Integration with ORGAN-V (Public Process)

The Logos Layer serves as the source material for the `public-process` repository in ORGAN-V.

1. **Extraction:** Significant updates to a formation's `docs/logos/` are extracted as essays.
2. **Linking:** The `CLAUDE.md` and `GEMINI.md` files for the repository will automatically link to the corresponding Logos narratives.
3. **Feed:** The `alchemical-io.md` updates should be broadcast to the system-wide activity feed.

---

## Appendix: Scaffolding Command

Use the `organvm` CLI to scaffold the Logos Layer:

```bash
organvm context logos --scaffold
```

This command creates the directory and populates the files with standard prompts.
