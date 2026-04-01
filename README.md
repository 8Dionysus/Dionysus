# Dionysus Seed Garden

`Dionysus` is the seed garden and dispatch layer for the current AoA / ToS ecosystem.

It stores seed sources, wave manifests, archived planting surfaces, and the minimal protocol needed to move seeds into owning repositories. It is not the final owning home of AoA meaning, ToS meaning, or repo-local implementation detail.

## What belongs here

- seed sources before or between plantings
- wave manifests that define order
- archived canonical seed surfaces kept for lineage
- live gated future-work seeds that are not yet open waves
- named prep packs for flexible future-work staging when a new numbered wave would be premature
- planting protocol, registry overlays, and validation surfaces
- planting trace only when the trace would otherwise be lost

## What does not belong here

- runtime services
- final repo-owned doctrine that should live in a target repo
- derived graph/export/UI inflation
- silent AoA ↔ ToS collapse
- repo-local backlog disguised as seed canon

## Current state

- `first_wave.manifest.json` through `ninth_wave.manifest.json` define the planting waves.
- `scripts/validate_manifest.py` validates manifest refs.
- `scripts/validate_seed_registry.py` validates `seed-registry.yaml`, required v3 provenance/redistribution/transplant shape, wave linkage, and closure-note status alignment.
- `scripts/validate_nested_agents.py` validates the required root and local `AGENTS.md` coverage for the wave 1.3 operating surfaces.
- `scripts/validate_seed_surfaces.py` runs all five validators as one entrypoint.
- `archive/` is the canonical archive root.
- `archive/seed_pack_exports/` keeps derived convenience zip bundles for review, handoff, or transport; these exports are not authoritative seed surfaces.
- `archive/seed_pack_2026-03-22/` is the archived canonical source pack for the closed ninth wave.
- `archive/seed_post_wave/seed.aoa.agents-runtime-pack.v0.md#aoa-seed-r1-agents-runtime-seam` is the archived source pack for the landed post-wave runtime slice.
- `seed_expansion/seed.tos.zarathustra-trilingual-entry.v0.md#tos-expansion-zarathustra-trilingual-entry` landed in `Tree-of-Sophia` and remains live in the registry until a later archival pass.
- `seed_expansion/seed.tos.wider-world-thought-expansion.v0.md#tos-expansion-wider-world-thought-expansion` is the next live gated seed surface, now synced to the bounded Zarathustra-route review gate in `Tree-of-Sophia`.
- `seed-registry.yaml` is the navigation overlay for humans and Codex.
- `seed_clawrouter_donor_graft.md` and `seed_clawrouter_donor_graft.map.yaml` stage a donor-origin prep slice for later bounded ClawRouter plantings without changing the current next-live seed.
- `seed_wave1_codex_audit_spine.md` and `seed_wave1_codex_audit_spine.map.yaml` stage a future cross-repo Codex audit wave without planting into the owning repos yet.
- `seed_wave2_codex_skill_proof_audit_bridge.md` and `seed_wave2_codex_skill_proof_audit_bridge.map.yaml` stage the later skill/proof audit seam wave without planting into the owning repos yet.
- `seed_architecture_fit_pack.md`, `seed_dialogue_memory_pack.md`, `seed_federation_conductor_pack.md`, `seed_memory_evals_skills_docs_pack.md`, `seed_future_agent_systems_prep_pack.md`, and their `.map.yaml` files stage additional future prep packs and candidate lineage without changing the current next-live seed.
- `seed_wave3_codex_repo_local_skills_trace_harness.md` and `seed_wave3_codex_repo_local_skills_trace_harness.map.yaml` stage the later repo-local Codex skills and trace-harness audit wave without downstream planting yet.
- `seed_questbook_foundation_pack.md`, `seed_questbook_source_proof_pack.md`, `seed_questbook_boundary_runtime_pack.md`, and `seed_questbook_seedgarden_profile_pack.md`, with matching `.map.yaml` files, stage a need-driven questbook rollout as named prep packs without opening a tenth numbered wave.
- `QUESTBOOK.md`, `docs/QUESTBOOK_SEED_GARDEN_INTEGRATION.md`, `quests/*.yaml`, `schemas/quest*.json`, and `generated/*.example.json` now hold the repo-local questbook reflection layer for seed-garden follow-through inside `Dionysus`; profile-level reflection in `8Dionysus` remains deferred to a later public-entry refresh contour.
- The current questbook contour explicitly leaves `ATM10-Agent` outside this planting line and defers `aoa-sdk` to the next separate named seed after the four-pack rollout lands.
- `archive/seed_pack_exports/questbook_first_wave_seed.zip` and `archive/seed_pack_exports/questbook_second_wave_seed.zip` are transport-provenance bundles for the staged questbook prep packs; they are not authoritative seed surfaces.
- `schema/seed-registry.contract.yaml` defines the registry field contract, including v3 provenance and transplant maps.
- `docs/codex/planting-protocol.md` defines the planting discipline.
- `docs/codex/seed-provenance-policy.md` and `docs/codex/seed-registry-v3-migration.md` define donor-shaped intake rules and the staged v3 migration path.
- `templates/donor-capture.template.md` is the local donor-intake note shape for donor-derived or mixed seeds.
- `templates/planting-report.template.md` and `reports/planting/` define how planting trace should be stored when Dionysus keeps the report.
- `scripts/check_seed_registry_v3_readiness.py` provides an advisory v3 readiness check plus report/stub generation.
- `scripts/validate_prep_packs.py` validates the named questbook prep-pack notes, priority metadata, exclusions, and source bundle placement.
- `reports/seed-registry-v3-readiness.md` records the current advisory v3 readiness snapshot for the live registry.

## Source-of-truth order

When there is tension between files, read in this order:

1. wave manifest
2. canonical source seed file
3. closure note for the same wave
4. `seed-registry.yaml`
5. planting protocol and contract files
6. target repository structure and ownership
7. `README.md`

The manifest defines order. The seed file defines meaning. The closure note defines the finished state of a closed wave. The registry makes navigation legible. The README should explain, not overrule.

When work is still staged as a named prep pack with no manifest, read the pack
note and matching `.map.yaml` from `origin_notes` after checking the stronger
live surfaces above. Named prep packs are flexible staging notes; they do not
overrule an opened wave or the current live seed.

## Repository map

- `archive/`
  - historical canonical seed sources
  - previous bundles, rootlines, witness seeds, templates, branch pilots, soil-prep files, archived packs, and archived post-wave seed-packs
- `archive/seed_pack_exports/`
  - derived zip exports for review, transport, or bounded handoff; not authoritative seed canon
- `seed_expansion/`
  - live gated future-work surfaces after the archived ninth wave
- `*_wave.manifest.json`
  - machine-readable planting order by wave
- `ninth_wave.closure.md`
  - closure state and landed surfaces for wave nine
- `seed-registry.yaml`
  - human/Codex navigation overlay
- `seed_clawrouter_donor_graft.md` and `seed_clawrouter_donor_graft.map.yaml`
  - donor-origin prep note and machine-readable transplant map for later bounded ClawRouter planting
- `seed_wave1_codex_audit_spine.md` and `seed_wave1_codex_audit_spine.map.yaml`
  - audit-wave prep note and machine-readable transplant map for later bounded Codex audit planting
- `seed_wave2_codex_skill_proof_audit_bridge.md` and `seed_wave2_codex_skill_proof_audit_bridge.map.yaml`
  - skill/proof seam prep note and machine-readable transplant map for later bounded wave 2 audit planting
- `seed_architecture_fit_pack.md`, `seed_dialogue_memory_pack.md`, `seed_federation_conductor_pack.md`, `seed_memory_evals_skills_docs_pack.md`, `seed_future_agent_systems_prep_pack.md`, and their `.map.yaml` files
  - staged future prep packs and candidate lineage preserved in Dionysus without changing the current next-live seed
- `seed_wave3_codex_repo_local_skills_trace_harness.md` and `seed_wave3_codex_repo_local_skills_trace_harness.map.yaml`
  - later repo-local Codex skills and trace-harness audit prep note and machine-readable transplant map
- `seed_questbook_foundation_pack.md`, `seed_questbook_source_proof_pack.md`, `seed_questbook_boundary_runtime_pack.md`, `seed_questbook_seedgarden_profile_pack.md`, and their `.map.yaml` files
  - named questbook prep packs and machine-readable selection maps for flexible staging outside the numbered wave line
- `schema/seed-registry.contract.yaml`
  - registry field contract and cross-link expectations
- `AGENTS.md` and local `AGENTS.md` files
  - repo and directory-level operating guidance for Codex and maintainers
- `docs/codex/planting-protocol.md`
  - planting rules for Codex and maintainers
- `docs/codex/seed-provenance-policy.md` and `docs/codex/seed-registry-v3-migration.md`
  - donor provenance policy and staged v3 migration guidance
- `templates/donor-capture.template.md`
  - reusable donor capture note template
- `templates/seed-entry.v3.native.example.yaml` and `templates/seed-entry.v3.donor.example.yaml`
  - worked native and donor-shaped v3 registry examples
- `templates/planting-report.template.md`
  - reusable planting report template
- `reports/seed-registry-v3-readiness.md`
  - advisory migration report for the current live registry shape
- `reports/planting/`
  - durable planting trace when Dionysus is the right place to hold the report
- `QUESTBOOK.md`, `docs/QUESTBOOK_SEED_GARDEN_INTEGRATION.md`, `quests/*.yaml`, `schemas/quest*.json`, `generated/*.example.json`
  - repo-local questbook reflection surfaces for planting follow-through, not a second sovereignty layer
- `scripts/check_seed_registry_v3_readiness.py`
  - advisory v3 readiness checker and stub/report generator
- `scripts/validate_manifest.py`
  - manifest reference validator
- `scripts/validate_seed_registry.py`
  - registry and closure-alignment validator
- `scripts/validate_nested_agents.py`
  - required `AGENTS.md` coverage validator
- `scripts/validate_prep_packs.py`
  - named prep-pack validator for questbook staging notes and maps
- `scripts/validate_questbook_surface.py`
  - repo-local questbook reflection validator for Dionysus seed-garden surfaces
- `scripts/validate_seed_surfaces.py`
  - single validation entrypoint for CI and local runs
- `seed_expat.md`, `seed_self-agent.md`, `seed_trio.md`, `seed_clawrouter_donor_graft.md`, `seed_wave1_codex_audit_spine.md`, `seed_wave2_codex_skill_proof_audit_bridge.md`, `seed_architecture_fit_pack.md`, `seed_dialogue_memory_pack.md`, `seed_federation_conductor_pack.md`, `seed_memory_evals_skills_docs_pack.md`, `seed_future_agent_systems_prep_pack.md`, `seed_wave3_codex_repo_local_skills_trace_harness.md`, `seed_questbook_foundation_pack.md`, `seed_questbook_source_proof_pack.md`, `seed_questbook_boundary_runtime_pack.md`, `seed_questbook_seedgarden_profile_pack.md`
  - origin notes and prep soil, not first-wave canon

## Seed lifecycle

- `archived_canonical`
  - historical seed source still needed for lineage and replay
- `pending_archive`
  - temporary source surface still live only until archive move
- `gated_next`
  - acknowledged next seed surface, not yet an opened wave
- `landed_post_wave`
  - planted and merged post-wave seed kept live in the registry even after archive cleanup, until a later lifecycle-model pass changes that status

## Wave map

- `first_wave`: trunk-first structure and parent axis
- `second_wave`: method spine
- `third_wave`: counterpart bridge
- `fourth_wave`: witness and compost pilot pair
- `fifth_wave`: ToS growth law trio
- `sixth_wave`: ToS corpus scaffold
- `seventh_wave`: bounded lineage pilot
- `eighth_wave`: soil prep before manual Zarathustra entry
- `ninth_wave`: AoA contract growth, now closed and archived on canonical terms

## Using Dionysus to plant with Codex

1. Pick the wave manifest.
2. Read the exact source seed referenced by the manifest.
3. Open the matching entry in `seed-registry.yaml`.
4. Read the target repository before writing anything.
5. Plant the smallest linked slice that leaves:
   - one human-readable explanation
   - one structural artifact
   - preserved seed vocabulary
   - explicit boundaries
6. Stop at contracts/docs when a seed would cross red-risk zones.
7. Leave trace in the PR, commit message, or a report based on `templates/planting-report.template.md`.

For donor-shaped or mixed seeds, also record donor repo/ref, transplant policy, redistribution obligations, and explicit `what survives` / `what stays behind` notes.

Operational editing guidance lives in `AGENTS.md` and the nearest nested `AGENTS.md`.

See `docs/codex/planting-protocol.md` for the detailed rules.

## Validation

```bash
python scripts/validate_seed_surfaces.py
```

This runs:

- `python scripts/validate_manifest.py`
- `python scripts/validate_seed_registry.py`
- `python scripts/validate_prep_packs.py`
- `python scripts/validate_questbook_surface.py`
- `python scripts/validate_nested_agents.py`

The registry validator checks field shape, path validity, anchor validity, wave linkage, next-live-seed coherence, and closure-note status alignment. The questbook validator checks that the repo-local seed-garden questbook stays aligned with its local YAML and example surfaces. The nested-agents validator checks that the required root and wave-local `AGENTS.md` files are present and non-empty.

For advisory v3 backfill status, also run:

```bash
python scripts/check_seed_registry_v3_readiness.py seed-registry.yaml --write-report reports/seed-registry-v3-readiness.md
```

This checker remains advisory and is useful for future donor-shaped additions or registry drift checks.

A GitHub Actions workflow lives at `.github/workflows/validate-seed-surfaces.yml`.

## Working rule

When in doubt:

- plant structure before expansion
- plant authored and source-linked surfaces before derived projections
- plant lineage before archive
- plant bridges as derived contracts, not identity collapse
- plant witness and compost as public contracts before heavier runtime instrumentation
- plant templates before branch multiplication
- use named prep packs when future work needs priority and dependency control without a fresh numbered wave
- plant one bounded pilot before plurality
- keep Dionysus small, legible, and transplant-focused
