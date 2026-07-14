# Changelog

All notable changes to `Dionysus` will be documented in this file.

The format is intentionally simple and human-first.
Tracking starts with the community-docs baseline for this repository.

## [Unreleased]

## [0.3.0] - 2026-07-14

### Summary

- This release adds a bounded owner-local statistics port over the public seed
  registry v2 lifecycle labels while preserving seed, wave, registry, closure,
  and target-repository authority.
- Validation and documentation routes now fail closed on the central stats
  contract and return runnable commands to executable owners or the nearest
  `AGENTS.md` instead of duplicating them across explanatory Markdown.
- The release was reconstructed from the complete post-`v0.2.0` Git range:
  its single first-parent commit changed 37 paths with 1,068 additions and 516
  deletions, and that 1/1 commit is accounted for below rather than inferred
  only from the previous `[Unreleased]` prose.

### Added

- A root `stats/` port now exposes the public reference ratio of seed registry
  v2 entries carrying the literal `landed_post_wave` lifecycle label, with the
  exact population, missingness, provenance, and authority ceiling declared
  through the shared `aoa-stats` contract.
- Added the owner-delegating stats validator, reference packet, regression
  coverage, CODEOWNERS route, and CI checkout of the pinned `aoa-stats` owner.

### Changed

- Active explanatory Markdown now routes validation and runnable commands to
  executable owners or the nearest `AGENTS.md` instead of repeating command
  blocks across README, decision, protocol, lineage, and staging surfaces.
- The repository release gate now fails closed when the compatible central
  stats validator is unavailable.
- Refreshed root, seed/staging, protocol, decision, Spark, and script route
  cards so operational commands remain with executable owners.
- Regenerated all seven repository-local KAG indexes after the authored,
  validation, and stats surfaces changed.

### First-Parent Reconciliation (1/1)

1. `77f2583` — Add Dionysus federated stats port (#148).

### Validation

- Release preparation reconciled the exact `v0.2.0..77f2583` first-parent
  history and all 37 changed paths, including the stats contract, seed/staging
  route cleanup, release-gate dependency law, and complete KAG index family.
- The repository release gate validates seed manifests, registry/lifecycle and
  decision contracts, generated route and KAG parity, artifact admission, the
  pinned central stats owner, and the full test suite.

### Notes

- The published ratio describes only the literal public registry population;
  it is not a seed-quality verdict and does not infer owner-repository landing
  truth beyond the recorded lifecycle label.
- `aoa-stats` retains shared grammar and cross-owner composition, while live
  seed meaning and landed owner truth remain with their stronger surfaces.
- Release-only version markers, changelog reconciliation, and regenerated
  companions follow the one reconciled product commit and are described here
  rather than misclassified as another product change.

## [0.2.0] - 2026-07-13

### Summary

- This release advances `Dionysus` from the `v0.1.3` release-line staging
  baseline into a guarded seed-garden surface with explicit agent routes,
  bounded memo and eval ports, durable decision rationale, artifact-trust
  verification, and a canonical local KAG provider.
- Titan sixteenth-wave lineage, current seed-route contracts, portable support
  skills, and host-consumable readmodel evidence are now checked without
  promoting the seed garden into owner-repo, runtime, proof, memory, or graph
  authority.
- The release was reconstructed from Git because the old `[Unreleased]`
  section was empty: all 37 first-parent commits from `v0.1.3` through
  `c3bb7db` are accounted for below, spanning 368 changed paths and 48,431
  additions / 342 deletions. None of those 37 commits had updated this
  changelog.

### Added

- The Titan sixteenth-wave swarm-ledger closeout seed, manifest, registry
  entries, preflight/closure lineage, and bounded supporting seed surfaces.
- Nested seed-surface `AGENTS.md` guardrails plus a compact root route card and
  preserved full root reference.
- A portable `.agents/skills/` foundation, session-growth and GitHub landing
  routes, shared skill refreshes, and hardened traceability, dry-run,
  self-diagnosis, and summon support.
- A local `memo/` port and canonical `aoa-memo` trigger/route vocabulary that
  keep durable reviewed memory outside the seed garden.
- A `DIONYSUS-SEED-D-####` decision rationale lane with generated lookup
  indexes and modeled-surface validation.
- A bounded local `evals/` port for seed-garden evaluation pressure without
  central verdict authority.
- Artifact identity for `generated/seed_route_map.min.json`, an OS Abyss seed
  route bundle gate, stronger artifact profiles, material evidence, trust
  roots, subject-store checks, and release-gate coverage.
- A local KAG provider and canonical seven-index family for source surfaces,
  entities, artifacts, anchors, events, assertions, and relations.

### Changed

- Seed routes, portable skill links, owner-reality canaries, staging maps, and
  MCP validation roots now use the current `/srv/AbyssOS` workspace contour.
- Seed lifecycle validation now handles the Experience wave4/wave5 map YAML
  shape correctly and closes bot-audit gaps in manifests, registry entries,
  dated lineage reports, and staging lifecycle markers.
- Decision generation rejects unmodeled surfaces, validates modeled entries,
  and requires explicit lists instead of accepting ambiguous shapes.
- Repo-local KAG publication is CI-enforced, pinned, deterministic, complete
  across all seven indexes, and compacted into canonical committed outputs.
- Seed-route artifact cleanup is fail-closed outside owned generated roots,
  revoked-record checks use the actual revoked identity, and the owner-reality
  verification contract points at the current host surface.

### Fixed

- Dry-run helpers preserve malformed preview data for explicit rejection
  instead of hiding the invalid shape.
- Experience seed maps use validator-compatible YAML quoting and carry a
  regression test for their lifecycle form.
- Stale single-index KAG output and the old dirty receipt snapshot are not
  carried forward over the newer canonical seven-index family.

### First-Parent Reconciliation (37/37)

The ordered pre-release history is recorded explicitly because all 37 commits
were absent from the old changelog:

1. `45811b9` — Plant Titan sixteenth wave seed.
2. `01e8990` — Add seed surface AGENTS guardrails (#112).
3. `6f691e6` — Slim root AGENTS route card (#113).
4. `ff881b8` — Retarget seed surfaces to AbyssOS.
5. `2f9e115` — Retarget Codex MCP validation root.
6. `5210604` — Install portable AoA skill foundation.
7. `ce39f68` — Roll out session-growth skills and GitHub landing (#116).
8. `c340574` — Harden portable skills and traceability (#117).
9. `3b0e04d` — Refresh session growth refs and readiness guard (#118).
10. `a24e1f0` — Guard dry run preview step shape (#119).
11. `520f47e` — Preserve dry run helper malformed shapes (#120).
12. `3f321b1` — Refresh shared AoA skill pack (#121).
13. `e27b008` — Refresh shared AoA skill pack (#122).
14. `1248796` — Close Dionysus bot audit gaps (#123).
15. `279f682` — Refresh self-diagnose skill export.
16. `0a12fb8` — Add memory route trigger law (#125).
17. `24e5669` — Use canonical aoa-memo route label (#126).
18. `1e1ed20` — Add local memo port (#127).
19. `2677bee` — Make memo validation route portable (#128).
20. `5e9b106` — Add seed decision rationale lane.
21. `f51c577` — Detect unmodeled decision lane surfaces (#130).
22. `a4d2f21` — Validate modeled decision surface contract entries (#131).
23. `5db52f9` — Require modeled surfaces to be explicit lists (#132).
24. `aec93c7` — Add local eval port skeleton.
25. `15c25e2` — Fix Experience seed map YAML validation (#134).
26. `0c15c97` — Add artifact identity to seed route map (#135).
27. `0165772` — Add OS Abyss seed route artifact gate (#136).
28. `fb8b198` — Strengthen seed route artifact trust profile (#137).
29. `c40b3a9` — Promote seed route evidence with trust roots (#138).
30. `888f8c9` — Add Dionysus KAG provider home.
31. `04e253d` — Align Dionysus KAG provider index with schema.
32. `a8a394d` — Add repo-local KAG indexes (#141).
33. `286ed81` — Enforce repo-local KAG index parity (#142).
34. `3a31578` — Pin deterministic repo-local KAG index gate (#143).
35. `f5c35a8` — Add repository KAG index family (#144).
36. `b22292b` — Publish canonical repository KAG indexes (#145).
37. `c3bb7db` — Refresh seed route verification contracts (#146).

### Validation

- Release preparation reconciled the exact `v0.1.3..c3bb7db` first-parent
  history, changed-path inventory, stale dirty-tree evidence, seed route and
  registry truth, decisions, local ports, artifact bundle/trust boundaries,
  and all seven KAG indexes instead of relying on `[Unreleased]`.
- The repo release gate validates seed manifests, registry and lifecycle
  contracts, nested guidance, decision indexes, generated route parity,
  artifact evidence/admission, KAG provider outputs, and the full test suite.

### Notes

- `Dionysus` remains a seed garden and lineage surface. Memo, eval, portable
  skill, artifact enforcement, runtime, KAG composition, and planted owner
  meaning remain with their stronger repositories.
- The stale canonical dirty tree was preserved as a local safety commit before
  cleanup. Its validator change is byte-identical to landed `c3bb7db`; its
  older single KAG index and receipt state are superseded by the canonical
  seven-index family and are intentionally not republished.
- Release-only banners, roadmap contour, parity test, changelog reconciliation,
  and regenerated derived indexes follow the 37 reconciled commits and are not
  hidden inside that count.

## [0.1.3] - 2026-04-23

### Summary

- this patch archives Agon Wave XV, downloaded zip, recurrence, Codex-plane,
  project-MCP, local-plugin, and seed-pack exports while deduplicating
  archived transport copies
- Titan seed waves, Titan incarnation planting traces, and Experience
  wave1-wave5 (external v0.1-v1.1) / v1.2-v2.0 lineage surfaces are
  registered, staged, dated, and closed out against owner-repo landings
- `Dionysus` remains the seed garden and staging surface: it preserves lineage
  without becoming live owner truth after planting

### Added

- archived Agon Wave XV, broader downloaded zip archives, recurrence seed
  packs, Codex-plane packs, project-MCP packs, local-plugin packs, and
  deduplicated seed-pack exports
- Titan seed-wave registration, Titan incarnation spine traces, bearer
  lineage preflights, appserver bridge, memory loom, operator console, runtime
  harness, and dated planting lineage reports
- Experience wave1-wave5 (external v0.1-v1.1) and v1.2-v2.0 intake,
  seed-staging, seed-expansion, planting-report, and lineage closeout surfaces

### Changed

- archived seed-pack exports were deduplicated, owner-repo reality canaries
  were kept as lineage checks, and Experience lineage closure was completed
  across the current staging line

### Validation

- `python scripts/release_check.py`

### Notes

- this patch preserves seed and planting lineage only; landed owner repos
  remain the stronger source of truth for live doctrine, runtime, proof,
  memory, routing, and role contracts

## [0.1.2] - 2026-04-19

### Summary

- this patch tightens landing-trace validation and stages the current
  Wave5/Wave10 seed packs for follow-through
- roadmap/current-direction docs, PR intake, and required-check plus Node24
  workflow refs are aligned with the active staging line
- `Dionysus` remains the seed garden and staging surface rather than live
  owner truth

### Added

- a Wave5 A2A Codex return checkpoint seed pack and Wave10 component refresh
  pack closeout staging surfaces

### Changed

- seed owner landing-trace validation, RFC3339 nanosecond precision handling,
  roadmap direction references, and CI/protection surfaces are tightened for
  the current staging wave

### Validation

- `python scripts/release_check.py`

### Notes

- this patch strengthens staging lineage and handoff posture without promoting
  staged seed material into live owner authority

## [0.1.1] - 2026-04-12

### Summary

- this patch adds repo-local Codex MCP disclosure and stages the current
  release-line seed packs through continuity and federation KAG follow-through
- seeded wave lifecycle audits are tightened for the live staging line
- `Dionysus` remains the seed garden and staging surface rather than live
  owner truth

### Added

- narrow repo-local `dionysus` MCP surface for Codex under
  `src/dionysus_mcp/` and `scripts/dionysus_mcp_server.py`, scoped to route
  maps, registry navigation, wave context, staging-note reality checks,
  planting rules, and quest follow-through
- focused MCP state tests under `tests/test_dionysus_mcp_state.py`
- optional MCP dependency surface in `requirements-mcp.txt`
- staged release-line seed packs for owner follow-through, rollout campaign
  cadence, self-agency continuity, and the federation KAG factory upgrade
  path

### Documentation

- repo-local MCP posture and launch guidance in `docs/CODEX_MCP.md`
- README and AGENTS routing updates so the MCP stays route-first and
  non-sovereign

### Changed

- seeded wave lifecycle audits and continuity closeout traces are tightened
  across the current release line.

### Validation

- `python scripts/release_check.py`

### Notes

- detailed Codex MCP, staged release-line seed-pack, and seeded lifecycle-audit changes for this patch remain enumerated below under `Added`, `Documentation`, and `Changed`

## [0.1.0] - 2026-04-10

### Summary

- first public baseline establishes `Dionysus` as the seed garden and staging surface of the federation
- the release centers on seed-route-map validation, checkpoint-aware lineage, and bounded staging posture
- release claims stay intentionally weaker than live owner-repo authority

### Added

- community-docs baseline established for this repository
- `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and `CONTRIBUTING.md`
- seed-route-map capsule plus jsonschema-backed validation for prep-pack and
  checkpoint-aware seed routing
- checkpoint-note validation surfaces, checkpoint-aware closeout lineage, and
  structured seed lifecycle checks
- staged and closed prep packs for via-negativa, ToS-graph curation, and
  aoa-rag-skeleton lineage work

### Changed

- tightened seed prep, owner-repo reality, and nested AGENTS guidance around
  the seed-garden versus live-owner split
- restored antifragility lineage surfaces and clarified current seed-garden
  posture for future staging

### Included in this release

- wave-manifest and archive foundations across `first_wave.manifest.json`,
  `second_wave.manifest.json`, `third_wave.manifest.json`,
  `fourth_wave.manifest.json`, `fifth_wave.manifest.json`,
  `sixth_wave.manifest.json`, `seventh_wave.manifest.json`,
  `eighth_wave.manifest.json`, `ninth_wave.manifest.json`,
  `ninth_wave.closure.md`, `archive/`, `reports/planting/`, and
  `seed-registry.yaml`, including seeded AoA and ToS waves, runtime-pack
  lineage, and archived planting traces
- seed-garden staging and prep-pack expansions across `seed_expansion/`,
  `seed_staging/`, `seed_notes/`, `generated/`, and `templates/`, including
  questbook rollout, RPG staging waves, federated audit remediation, stats
  telemetry, surface-detection bundles, via negativa, ToS-graph curation, and
  `aoa-rag-skeleton` lineage work
- repo-local operating and validation surfaces under `docs/`, `AGENTS.md`,
  nested `AGENTS.md`, `.agents/`, `.github/`, `README.md`, `QUESTBOOK.md`,
  `quests/`, `scripts/`, `schemas/`, `tests/`, and `Spark/`, including the
  seed-route-map capsule, owner-repo reality fixes, checkpoint-aware closeout
  lineage, CI validator runs, and project-foundation follow-through

### Validation

- `python scripts/validate_seed_surfaces.py`
- `python scripts/build_seed_route_map.py --check`
- `python scripts/validate_seed_route_map.py`
- `python -m pytest -q tests`

### Notes

- this remains a staging and seed-garden baseline, not a claim that `Dionysus` owns live owner-repo truth
