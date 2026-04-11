seed_id: seed.aoa.codex-surface-plane-pack.v0
title: AoA Codex Surface Plane and Lineage Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: partially_landed_retained_for_lineage
lifecycle_note: The workspace-level aoa_workspace MCP, the /srv project-level Codex glue, the repo-local aoa_stats and dionysus MCPs, the first aoa-skills skill-to-MCP wiring slice, the aoa-agents subagent projection plus workspace install slice, the first workspace launcher plugin slice, the workspace-local convergence seam, and the hooked-doctor seam are now landed, while the wider lineage rollout remains staged in Dionysus.
reality_checked_at: '2026-04-11'
status: pending_archive
priority: medium
parent_seed: null
tags:
  - codex
  - workspace
  - mcp
  - plugin
  - subagents
  - convergence
  - hooks
  - lineage
  - aoa-sdk
  - aoa-stats
  - dionysus

# Seed Note: AoA Codex Surface Plane and Lineage Prep Pack

## Purpose

Prepare one bounded Codex access-plane and lineage prep pack inside
`Dionysus`.

This pack preserves a multi-surface Codex rollout across workspace config,
project MCP, repo-local MCP, skill/MCP wiring, launcher plugin, subagent
projection, convergence doctor, hooks, and candidate-lineage follow-through
without pretending the archive bundle can be planted into owner repos
unchanged.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the source drop spans several owner repositories and one workspace-root layer
- the first workspace-MCP slice and the first two repo-local MCP slices are
  landed, the first skill-to-MCP wiring slice is now landed too, while the
  rest still needs adaptation and bounded sequencing
- the pack mixes doctrine notes, transport zips, generated overlays, and
  runtime-facing glue that should not be treated as one owner-repo patch
- the bundle carries reference-only and experimental surfaces that need honest
  staging status before any further planting
- the bundled lineage note names a parallel cross-repo route that should stay
  explicit instead of hiding behind the access-plane rollout

## Bundle contents to preserve

The source artifact is
`archive/seed_pack_exports/aoa-codex-surface-plane-seed-2026-04-11.zip`.

The archived ingress summary is
`archive/seed_pack_exports/aoa-codex-surface-plane-seed-2026-04-11-summary.md`.

The package carries:

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

## Boundary posture to preserve

Read this pack under these boundaries:

- keep AGENTS, skills, MCP, subagents, and plugins as distinct Codex surfaces
- keep `aoa-sdk` on the topology and control plane rather than as a semantic
  owner for sibling repos
- keep `Agents-of-Abyss` as the doctrine and constitutional center
- keep the `aoa-stats` MCP derived-only, and keep the `Dionysus` MCP
  route-first, read-only, and weaker than owner-repo planting truth
- keep hooks deterministic, narrow, and experimental until runtime support is
  proved in the active Codex environment
- keep bridge and generated overlays as transport context, not owner truth
- keep candidate-lineage rollout explicit as a parallel route rather than
  smuggling it into the MCP glue

## Ownership posture

Read later landings under these owner boundaries:

- `Agents-of-Abyss` is the first owner for the concept anchor and lineage
  doctrine note
- `aoa-sdk` is the first owner for workspace discovery, project-level
  orientation, and the `aoa_workspace` MCP server
- the sibling workspace root `/srv` is the honest home for project-level
  `.codex` glue such as MCP server declarations and hooks config
- `aoa-stats` is the first owner for the derived observability MCP slice
- `Dionysus` is the first owner for the read-only seed-garden MCP slice and
  seed-lineage carry
- `aoa-skills` is the first owner for skill-to-MCP wiring and launcher-skill
  posture
- `aoa-agents` is the first owner for profile-driven subagent projection
- `aoa-evals` is the later owner for lineage-integrity and owner-fit proof
  bundles
- `aoa-routing` and `aoa-kag` remain derivative consumers, not first-authoring
  homes for this pack
- `Dionysus` keeps the pack and its planting posture, not the final owner
  truth of the landed repos

## Application posture

Treat this pack as a partially landed lineage pack.

The honest first planting is already live as:

1. one workspace-level `aoa_workspace` MCP server in `aoa-sdk`
2. one project-level `/srv/.codex` layer with `aoa_workspace` wiring
3. one runtime-proved resolution path that correctly prefers
   `/home/dionysus/src/abyss-stack`
4. one repo-local `aoa_stats` MCP server in `aoa-stats`
5. one project-level `/srv/.codex` wiring for `aoa_stats`
6. one runtime-proved `stats_catalog` read through Codex
7. one repo-local `dionysus` MCP server in `Dionysus`
8. one project-level `/srv/.codex` wiring for `dionysus`
9. one runtime-proved `seed_route_catalog` and `seed_next_live` read through
   Codex
10. one repo-owned `aoa-skills` skill-to-MCP wiring layer with route-family
    examples, generator and validator scripts, and generated-export guidance
11. one workspace-level `/srv` route-discipline note plus stable-server naming
    guidance for the skill-to-MCP layer
12. one workspace-validated example pass proving the named route-family
    scaffolds align with `/srv/.codex/config.toml`
13. one repo-owned `aoa-agents` subagent projection layer with live profile
    wiring, generator and validator scripts, and generated Codex custom-agent
    surfaces
14. one project-level `/srv/.codex/agents/` install plus `/srv/.codex/config.toml`
    registration for the five active AoA role seeds
15. one workspace-level validation pass proving the installed custom-agent
    projection still matches live `aoa-agents` profiles and wiring
16. one workspace-local `aoa-shared-launchers` plugin install under
    `/srv/.codex/plugins/aoa-shared-launchers`
17. one workspace plugin discovery seam at
    `/srv/.agents/plugins/marketplace.json` pointing at the installed launcher
    plugin
18. one post-install validation pass proving the launcher plugin manifest,
    bundled skills, marketplace entry, and named MCP dependencies align with
    `/srv/.codex/config.toml`
19. one workspace-local convergence package under
    `/srv/.codex/tools/aoa_codex_converge/`, `/srv/.codex/scripts/`, and
    `/srv/.codex/bin/`
20. one convergence bootstrap plus doctor/status pass proving the live `/srv`
    control-plane seams converge cleanly and emitting reports under
    `/srv/.codex/generated/codex/`
21. one workspace-local hooks doctor package under
    `/srv/.codex/tools/aoa_codex_hooks/` and
    `/srv/.codex/scripts/aoa_codex_hooks_doctor.py`
22. one in-place upgrade of the existing `.codex/hooks/*.py` entrypoints so
    current hook names keep working while richer hook state and event logic now
    flow through the new package
23. one manual hooks doctor pass plus event-wrapper smoke path proving reports
    and event logs now write under `/srv/.codex/generated/codex/hooks/`
24. one explicit workspace-local adaptation rule keeping plugins, convergence,
    and hooks under `.codex/*` because `/srv` itself is not writable for
    top-level `plugins/` and `scripts/` install surfaces

The next bounded landings remain staged on purpose:

1. wider lineage rollout through `Agents-of-Abyss`, `aoa-sdk`, `aoa-skills`,
   `Dionysus`, `aoa-stats`, and `aoa-evals`
2. any later owner-fit or lineage-integrity proof bundle once the control plane
   stops moving

The bundled lineage note also stays active as a parallel route:

1. plant the concept anchor in `Agents-of-Abyss`
2. formalize `cluster_ref -> candidate_ref -> seed_ref -> object_ref`
3. route the rollout through `aoa-sdk`, `aoa-skills`, `Dionysus`,
   `aoa-stats`, and `aoa-evals`

When planted later, regenerate code, tests, and generated surfaces from live
owner repos rather than copying archive overlays unchanged.

## What this pack is not for

- no new numbered wave manifest
- no change to `navigation.next_live_seed`
- no blind unzip-merge into owner repos
- no treating `aoa_codex_bridge_pack.zip` as the current authority
- no import of `__pycache__`, `.pytest_cache`, or personal approval/sandbox
  defaults into live repos
- no hooks-first planting without runtime proof
- no second workspace-topology model separate from `aoa-sdk` discovery
- no first-authoring into `aoa-routing` or `aoa-kag`

## Final rule

Keep this pack because it names one real Codex access-plane rollout plus one
parallel lineage route, and only the first bounded workspace slice, the first
two repo-local MCP slices, the first skill-to-MCP wiring slice, the first
subagent projection slice, the first launcher plugin slice, the first
convergence slice, and the first hooked-doctor slice have landed so far.

But preserve the difference between:

- one landed workspace-MCP slice
- two landed repo-local MCP slices
- one landed skill-to-MCP wiring slice
- one landed subagent projection slice
- one landed launcher plugin slice
- one landed convergence slice
- one landed hooked-doctor slice
- later lineage and proof follow-through still staged
- one explicit lineage route
- and one staging pack in `Dionysus`
