# Changelog

All notable changes to `Dionysus` will be documented in this file.

The format is intentionally simple and human-first.
Tracking starts with the community-docs baseline for this repository.

## [Unreleased]

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
