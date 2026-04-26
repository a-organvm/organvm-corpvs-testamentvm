# ADR-018: Portfolio Lockfile + CI Honesty (npm ci on Astro v5)

## Status

Accepted

## Date

2026-04-26

## Context

The `portfolio-site/` Astro project entered a state where its dependency declaration was unverifiable:

- `package.json` pinned `astro: ^5.0.0` (downgraded from `^6.1.6` during a prior triage)
- `package-lock.json` was absent from the repository
- `.github/workflows/ci.yml` had been changed to `npm install` (commit `2937991`, "fix(CI): use npm install instead of npm ci") so the validation job would stay green without a lockfile
- `.github/workflows/pages-deploy.yml` still used `npm ci` (line 39) and **failed on every run from 2026-04-26 00:23 UTC onward** (4 consecutive failures across Dependabot bumps and the v5 pin commit) because `npm ci` cannot run without a lockfile

The two-workflow split produced a dishonest signal: validation CI was green while production deploys were broken. The user-facing Pages site was running on its last-known-good build from 2026-03-30 while every commit since produced a red Pages workflow no one was watching.

This ADR closes that gap by completing — not reverting — the prior pragmatic fix that swapped `npm ci` for `npm install`.

## Decision

1. **Generate and commit `portfolio-site/package-lock.json`** against the current `astro: ^5.0.0` declaration, using npm 11 (lockfileVersion 3, readable by npm 10 in CI Node 20/22).
2. **Restore `npm ci` in `.github/workflows/ci.yml`** so validation CI fails honestly when dependencies drift.
3. **Leave `pages-deploy.yml` alone** — it already uses `npm ci`; the new lockfile makes it succeed.
4. **Pin Astro at v5.x for now.** The original v6 → v5 downgrade was undocumented; rather than re-attempt v6 without the original failure context, we accept v5 as the currently-shipped state. A future ADR can revisit v6 if and when the original break is diagnosed.

## Consequences

**Positive:**

- Pages deploys resume working immediately on the next push.
- Validation CI failures now correlate with real dependency drift, not lockfile absence.
- Dependabot PRs will surface real conflicts in CI instead of merging green and breaking Pages.
- Contributor experience improves: `git clone && cd portfolio-site && npm ci` works.

**Negative:**

- We are pinned at Astro v5.x without a recorded reason for the v6 downgrade. Any future v6 attempt will need to rediscover the failure that prompted the downgrade.
- The lockfile is generated under Node 25 (local dev) and consumed under Node 20 (`pages-deploy`) and Node 22 (`ci`). lockfileVersion 3 supports this fan-out, but a Node-version split between workflows is its own latent inconsistency that should be revisited.

**Follow-ups (not in scope here):**

- Align `pages-deploy.yml` and `ci.yml` to a single Node version.
- Diagnose what broke Astro v6 originally and decide whether to re-upgrade.

## References

- Sister-session relay (2026-04-25 22:00 ~ EDT) flagged the dishonesty pattern after Achilles Session B's pragmatic `npm install` fix.
- `INST-INDEX-RERUM-FACIENDARUM.md` row DONE-478 (Achilles Session B: AG-04 corpvs CI fix) — this ADR completes that work item.
- `data/done-id-counter.json` — DONE-479 claimed for this completion.
