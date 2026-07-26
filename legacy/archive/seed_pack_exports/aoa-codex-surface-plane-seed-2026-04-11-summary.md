# AoA Codex Surface Plane Seed Summary

## Purpose

This derived transport bundle preserves one multi-file Codex upgrade drop as a
single replayable seed surface inside `Dionysus`.

It is transport and staging only. It does not become canonical owner-repo
meaning.

## Bundle

- bundle: `archive/seed_pack_exports/aoa-codex-surface-plane-seed-2026-04-11.zip`
- assembled_at: `2026-04-11`
- assembly_root: `/home/dionysus/Загрузки`

## Source files copied into the bundle

- `aoa_codex_seed_pack.zip`
- `aoa_codex_hooks_doctor_pack.zip`
- `aoa_codex_convergence_pack.zip`
- `aoa_subagent_projection_pack.zip`
- `aoa_local_plugin_pack.zip`
- `aoa_skill_mcp_wiring_pack.zip`
- `aoa_project_mcp_pack.zip`
- `dionysus_mcp_server_pack.zip`
- `aoa_stats_mcp_server_pack.zip`
- `aoa_codex_bridge_pack.zip`
- `aoa_codex_surface_crosswalk.md`
- `aoa_wave1_change_map.md`

## Working reading

- `aoa_codex_seed_pack.zip` is the landing brain and sequence note
- `aoa_codex_bridge_pack.zip` is reference-only and already superseded by the
  later packs
- `aoa_project_mcp_pack.zip` is the workspace-level MCP seed, but it must be
  adapted to `aoa-sdk` workspace discovery
- `aoa_stats_mcp_server_pack.zip` and `dionysus_mcp_server_pack.zip` are the
  repo-local MCP seeds
- `aoa_skill_mcp_wiring_pack.zip` is the skill-to-MCP dependency and validator
  seed
- `aoa_local_plugin_pack.zip` is the launcher-plugin seed
- `aoa_subagent_projection_pack.zip` is the subagent projection seed
- `aoa_codex_convergence_pack.zip` is the later doctor and convergence seed
- `aoa_codex_hooks_doctor_pack.zip` is the experimental hooks seed
- `aoa_codex_surface_crosswalk.md` is the surface-boundary matrix
- `aoa_wave1_change_map.md` is the candidate-lineage rollout note

## Current workspace reality at capture time

As of `2026-04-11`:

- the project-level `/srv/.codex` layer exists
- workspace-level `aoa_workspace` MCP is already landed in `aoa-sdk` and wired
  from `/srv/.codex/config.toml`
- end-to-end `codex exec` successfully resolved `abyss-stack` through the MCP
  to `/home/dionysus/src/abyss-stack`
- repo-local `aoa_stats` and `dionysus` MCP surfaces are not landed yet
- skill/MCP wiring, local plugin launchers, subagent projection, and
  convergence remain staged
- hooks are still experimental because manual script smoke passed, but
  automatic runtime hook invocation is not yet a proved stable surface

## Adaptation rules to preserve

- do not unzip-merge these packs into live repos unchanged
- respect `aoa-sdk` as the topology and control-plane owner
- keep AGENTS, skills, MCP, subagents, and plugins as distinct Codex surfaces
- keep derived layers derived and review-backed
- regenerate repo-native builders and tests from live owner repos
- do not copy `__pycache__`, `.pytest_cache`, personal sandbox/approval
  settings, or unsupported hooks assumptions into live repos

## Recommended planting order

1. `Agents-of-Abyss` concept anchor and doctrine note
2. `aoa-sdk` workspace MCP plus project-level `/srv/.codex` glue
3. `aoa-stats` repo-local MCP
4. `Dionysus` repo-local MCP
5. `aoa-skills` skill-to-MCP wiring and launcher-skill posture
6. local plugin launcher layer
7. `aoa-agents` profile projection into subagent config
8. convergence doctor
9. hooks only after runtime proof

## Lineage companion

Keep the bundled `aoa_wave1_change_map.md` as the companion note for the
parallel lineage route:

`Agents-of-Abyss` -> `aoa-sdk` -> `aoa-skills` -> `Dionysus` -> `aoa-stats` -> `aoa-evals`
