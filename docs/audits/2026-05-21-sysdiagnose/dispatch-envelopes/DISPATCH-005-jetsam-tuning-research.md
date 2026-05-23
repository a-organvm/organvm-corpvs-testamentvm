# DISPATCH-005: Research — macOS 26.5 jetsam tuning on memory-constrained hosts

**Target agent:** Perplexity (web research)
**Source repo:** N/A (research output)

**Work scope:**
Research and summarize, with citations, the following questions:

1. What user-tunable jetsam parameters exist on macOS 26 (Tahoe)? Specifically:
   - `memorystatus_critical_pages` and adjacent kernel parameters
   - `sysctl vm.compressor_*` knobs and what they do
   - Whether `sudo memory_pressure` can be used proactively to inform jetsam decisions
2. Are there documented best-practices for running multiple Electron-based AI apps on 16 GB hosts?
3. What are the trade-offs of `sudo purge` invocations? Is there a non-destructive equivalent?
4. Does the macOS resource-class system (`launchctl print-class`) allow demoting specific processes (e.g., Antigravity, ChatGPT Atlas) to lower memory priority so jetsam picks them first?
5. Are there community-validated `defaults write` recipes for reducing Electron app memory footprint (e.g., Spotlight indexing exclusions for `~/Library/Application Support/Claude/`)?

**Acceptance criteria:**
- One markdown file with answers to each question, each answer backed by at least one citation (Apple developer docs, well-regarded blog, or HN/Stack Overflow with high-reputation responders).
- Explicit "I don't know" entries where the research did not find authoritative answers — do not fabricate.
- Concrete `defaults write` / `sysctl` / `launchctl` commands listed verbatim, not paraphrased.

**Out of scope:**
- Actually executing any of the recommended commands. This is research-only; the audit will receive the report and Claude decides what to test.
- Speculative future-macOS guidance.

**Verification on return:**
Claude reviews the research output against:
1. Apple's public documentation (sanity check citations).
2. The audit's FIND-005 to confirm research findings actually help with the observed pattern.
3. Files the report at `findings/RESEARCH-005-jetsam-tuning.md` and adds a Findings link to REPORT.md if research yielded actionable knobs.
