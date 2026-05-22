# IRF P0 surface — snapshot

**Last check:** 2026-05-22T11:13:00Z
**Count:** 37 open P0 items

## Delta since prior snapshot
- Closed: none (bootstrap — no prior snapshot)
- Opened: none (bootstrap — no prior snapshot)
- Status-changed: none (bootstrap — no prior snapshot)

## Domain rollup
| Domain | Count |
|--------|-------|
| APP | 1 |
| III | 4 |
| INST | 3 |
| OPS | 4 |
| PRT | 4 |
| RES | 11 |
| SEC | 2 |
| SYS | 5 |
| TAX-VAC | 1 |
| THE-VAC | 1 |
| VAC | 1 |
| **Total** | **37** |

## Items
| ID | Domain | Status | Description |
|----|--------|--------|-------------|
| IRF-APP-087 | APP | OPEN | 39 outreach messages prepared but 0 sent — pipeline warm-path unactivated. Triage complete — 9 target dead (rejected/expired), live targets remain uncontacted. |
| IRF-III-026 | III | OPEN | VACUUM: public-record-data-scrapper has no payment flow. 526 tests, deployed on Netlify+Render, UCC-MCA lead generation. 17 deployed URLs, zero revenue. Required: Stripe integration, 3-tier pricing, sign-up flow. |
| IRF-III-027 | III | OPEN | VACUUM: content-engine--asset-amplifier (Cronus) has no payment flow. CF Pages + Cloudflare Workers + Neon PostgreSQL, 7 AI providers, zero marginal cost on Ollama. Required: Stripe integration, freemium gate, pricing page. |
| IRF-III-035 | III | OPEN | VACUUM: sovereign-systems hub `quizFormUrl` is empty. `src/data/hub.config.ts:268` has `quizFormUrl: ''`. `QuizEmbed.astro` falls back to local `/quiz` route — Maddie intended a GHL form URL. GH#58. |
| IRF-III-047 | III | OPEN | Styx revenue gap — premortem completed. 20 failure modes identified on "extract sellable artifact + get paid in 30 days" plan. Hidden assumption: internal complexity invisible to buyers. |
| IRF-INST-001 | INST | OPEN | Apply to NLnet NGI0 Commons Fund — EUR 37,080 for Cvrsvs Honorvm governance engine extraction. Web form at nlnet.nl/propose/. Draft complete (S38). All sections filled. Deadline approaching. |
| IRF-INST-015 | INST | OPEN | Human review pass on NLnet draft — Read aloud, verify all claims, check scoring criteria alignment. Then submit web form at nlnet.nl/propose/ selecting "NGI Zero Commons Fund." |
| IRF-INST-016 | INST | OPEN | Register ORCID — Persistent researcher identifier. Takes 5 minutes at orcid.org/register. Required for academic funders (Sloan, NSF). Referenced in "Becoming the Subject." |
| IRF-OPS-014 | OPS | OPEN | Overreach Incident remediation — Stream D 17-commit push to hokage-chess origin/main without acolyte authorization. Push range `0a31116..7d29278` live on main. Decision: accept or rollback via force-with-lease. |
| IRF-OPS-021 | OPS | OPEN | README.md merge-conflict markers on main — `meta-organvm/organvm-corpvs-testamentvm/README.md`. Lines 14–23 and 312–318 contain unresolved diff3-style conflict markers. All three sides carry identical content. Corruption is live on main. |
| IRF-OPS-028 | OPS | OPEN | Word-count metric generator regression cascading into 87+ files across 3 repos. `total_words_short` reported as `~6K+` where previously `~404K+`/`~739K+`/`~766K+`. Blocks all generator-cascaded commits. |
| IRF-OPS-061 | OPS | OPEN | `organvm atoms pipeline --write` cadence has slipped — atom registry at `~/Code/organvm/organvm-corpvs-testamentvm/data/prompt-registry/prompt-atoms.json` was last updated prior to this session. |
| IRF-PRT-027 | PRT | OPEN | hokagechess.com domain registration (Cloudflare Registrar). Verified available 2026-04-25 via Verisign. Register through Cloudflare Registrar (at-cost, no markup). Required for hokage-chess landing page deploy. |
| IRF-PRT-028 | PRT | OPEN | hokage-chess landing page deploy to Vercel. Repo `4444J99/hokage-chess` is private; Next.js 16 build ready. Deploy to Vercel, configure custom domain `hokagechess.com`. Depends on IRF-PRT-027. |
| IRF-PRT-060 | PRT | OPEN | Kit API key (PRT-030) gates Hokage L2 deploy. 60s user action; without it, email funnel L2 cannot ship. Escalate if delayed >7d (currently silent since Apr 25). |
| IRF-PRT-061 | PRT | OPEN | hokagechess.com domain registration — verified AVAILABLE 2026-04-25. Time-decay risk: domain may be taken by squatter. No owner assigned. Register today (~$15/yr). Duplicate P0 signal with IRF-PRT-027. |
| IRF-RES-003 | RES | OPEN | Define "readiness" construct independently of its operationalization — convene expert panel to define full domain of "repository readiness" independently of metrics that measure it. GH#343. |
| IRF-RES-004 | RES | OPEN | Conduct factor analysis on the omega scorecard — perform EFA on all indicators across repo population; determine single vs. multiple latent factors. GH#340 (commission INQ-2026-013, Wave 1). |
| IRF-RES-006 | RES | OPEN | Build a controlled vocabulary registry for domain terms — machine-readable mapping of canonical terms to synonyms; validate new names against vocabulary in CI. GH#345 (commission INQ-2026-013). |
| IRF-RES-007 | RES | OPEN | Make incompleteness visible in all governance verdicts — every automated verdict must include explicit scope statement listing unverified semantic properties. GH#346 (commission INQ-2026-013). |
| IRF-RES-008 | RES | OPEN | Formalize the IRA panel protocol — strengthen IRA panel as Tarskian escape; provide explicit guidance on semantic properties that automated checks cannot assess. GH#347 (commission INQ-2026-013). |
| IRF-RES-009 | RES | OPEN | Implement seed.yaml semantic accuracy tracking — maintain machine-readable registry of properties not covered by seed.yaml validation; track gap between declared and verified. GH#348. |
| IRF-RES-010 | RES | OPEN | Separate self-maintenance from self-improvement in governance — build two distinct operational modes with architectural enforcement of the boundary. GH#348 (commission INQ-2026-013). |
| IRF-RES-011 | RES | OPEN | Establish the hybrid topology principle as architectural law — codify inter-organ hierarchical flow and intra-organ rhizomatic connectivity as compression/search architectural constraint. GH#349. |
| IRF-RES-012 | RES | OPEN | Design governance artifacts as boundary objects — redesign seed.yaml, CLAUDE.md, and governance-rules.json as boundary objects accommodating human, machine, and institutional readers. |
| IRF-RES-013 | RES | OPEN | Implement temporal staging for governance validation — ensure governance always validates previous state using current state, never current state using itself. |
| IRF-RES-014 | RES | OPEN | Implement context-specific governance norms — differentiate thresholds by organ, programming language, and project type; use expert-determined context-specific norms. |
| IRF-SEC-002 | SEC | OPEN | OpenAI API key exposed in public Docker image. Key found in `cetaceang/openai-king` (92MB, 507 pulls, live since Aug 2025). Responsible disclosure received 2026-04-10. Action: rotate at platform.openai.com, audit usage logs. |
| IRF-SEC-005 | SEC | OPEN | Gmail app password not revoked in Google Account. Label `gmail-app-pw-033526` (created 2026-03-25) grants IMAP/SMTP to `padavano.anthony@gmail.com`. No active consumers. 27+ days without revocation. |
| IRF-SYS-009 | SYS | OPEN | Gmail notification hygiene — filter designed in S36: `from:notifications@github.com ("dependabot[bot]" OR "github-actions[bot]")` → Skip Inbox, Apply label `github/bots`, Mark as Read. HUMAN ACTION NEEDED. |
| IRF-SYS-011 | SYS | OPEN | GoDaddy domain `met4vers.io` EXPIRED — cancellation notice received. Domain expired Mar 29. Grace period active — renewal or intentional abandonment decision required. |
| IRF-SYS-087 | SYS | OPEN | UMFAS birth — compress the corpus into the space. REFRAMED 2026-04-06: Birth is COMPRESSION: inventory all origin documents → atomize → the atomized corpus IS the space. GH#310. |
| IRF-SYS-137 | SYS | OPEN | Gemini Takeout export still pending — HUMAN ACTION NEEDED. Google Takeout requested for Gemini conversation history but export not yet delivered/downloaded. Blocks full Gemini corpus ingestion. |
| IRF-SYS-156 | SYS | OPEN | GitHub notification backlog — 4,115 total / 1,448 unread / 12 explicit-attention items at high risk of being lost in CI noise. The 12 humans-waiting items risk being missed. |
| IRF-TAX-VAC-001 | TAX-VAC | OPEN | Execute cold-reading Stranger Test on personalized-storefront-render SKILL.md. Verification gate to graduate substrate from "self-attested" to "verified." |
| IRF-THE-VAC-004 | THE-VAC | OPEN | Implement corpus persona-extract in conversation-corpus-engine. Highest compounding move: extract vocabulary/yearnings from session JSONLs. |
| IRF-VAC-001a | VAC | OPEN | Create tracking issue for SGO research programme on corpvs-testamentvm (13 papers, 74 tasks, 3 arXiv packages, 4 governance declarations). PARTIAL — 3 arXiv submissions complete. |
