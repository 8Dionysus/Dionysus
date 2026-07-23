# AoA Wave 5 Portability Regeneration Pack Summary

## Purpose

This derived transport bundle preserves the next Codex-plane portability and
regeneration wave as a source-owned install hardening route.

It is transport and staging only. It does not replace live owner-repo truth,
and it does not move MCP implementation ownership, agent meaning, or workspace
discovery authority out of their current owner repositories.

## Bundle

- bundle: `archive/seed_pack_exports/aoa-wave5-portability-regeneration-pack-2026-04-11.zip`
- assembled_at: `2026-04-11`
- assembly_root: `/home/dionysus/Загрузки`

## Source files copied into the bundle

- `aoa_wave5_portability_regeneration_pack/README.md`
- `aoa_wave5_portability_regeneration_pack/IMPLEMENTATION_DOCKET.md`
- `aoa_wave5_portability_regeneration_pack/PR_SLICES.md`
- `aoa_wave5_portability_regeneration_pack/CODEX_EXECUTION_PROMPT.md`
- `aoa_wave5_portability_regeneration_pack/ACCEPTANCE_MATRIX.md`
- `aoa_wave5_portability_regeneration_pack/contracts/codex_plane_regeneration_contract_v1.md`
- `aoa_wave5_portability_regeneration_pack/proposed-targets/8Dionysus/*`
- `aoa_wave5_portability_regeneration_pack/proposed-targets/aoa-sdk/*`
- `aoa_wave5_portability_regeneration_pack/tools/validate_wave5_portability_regeneration.py`

## Working reading

- this wave is about source-owned regeneration of the checked-in Codex-plane
  deploy surfaces for a chosen workspace root
- `8Dionysus` owns the regeneration doctrine, manifest/profile tree, renderer,
  validator, and the checked-in generated `.codex` deploy files
- `aoa-sdk` stays on workspace discovery and compatibility, with only a narrow
  boundary note for Codex-plane portability
- portability comes from regeneration, not from hand-editing path-bound files
  or pretending project config can become root-relative truth everywhere
- raw `__pycache__` and `.pyc` payloads in the uploaded bundle are transport
  noise, not planting material

## Current workspace reality at capture time

As of `2026-04-11`:

- the shared-root `.codex/config.toml` and `.codex/hooks.json` are already
  present in `/srv` and reflected in `8Dionysus`, but they are still
  deployment-shaped and path-bound to the current workspace root
- `8Dionysus/docs/WORKSPACE_INSTALL.md` already warns that path-bound shared
  install surfaces need adaptation when the public workspace root changes
- what is still missing is the source-owned regeneration substrate:
  doctrine, manifest/profile inputs, renderer, and drift validator
- `aoa-sdk` already owns workspace discovery and compatibility posture; it
  should not be patched into a second config renderer

## Adaptation rules to preserve

- keep MCP server names stable: `aoa_workspace`, `aoa_stats`, and `dionysus`
- keep project-root markers stable and explicit
- keep `.codex/config.toml` and `.codex/hooks.json` as generated deploy
  surfaces rather than the primary authoring surface
- keep regeneration source-owned in `8Dionysus`
- keep workspace discovery owned by `aoa-sdk`
- ignore `__pycache__` and `.pyc` payloads from the uploaded bundle
- do not patch owner repos to chase path drift that belongs in the renderer

## Recommended planting order

1. `8Dionysus` doctrine note plus manifest/profile tree
2. `8Dionysus` renderer, validator, and regenerated checked-in `.codex/`
3. `aoa-sdk` portability boundary note

## Lineage center

Keep this bundle as regeneration evidence for the route:

`8Dionysus manifest/profile -> rendered shared-root .codex deploy surfaces -> aoa-sdk boundary note`

That route stays subordinate to the existing owner split between shared-root
install doctrine and repo-owned runtime implementations.
