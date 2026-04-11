# Codex MCP

## Purpose

`Dionysus` now ships a narrow repo-local MCP server so Codex can orient inside
the seed garden without turning staging, route maps, or planting reports into
hidden owner-repo sovereignty.

This surface is intentionally:

- read-only
- route-first
- registry-aware
- planting-protocol-aware
- repo-local
- non-sovereign

## Start posture

When using this MCP:

1. call `seed_route_catalog`
2. call `seed_registry_navigation`
3. use `seed_next_live` or `seed_wave_context` before touching staging notes
4. call `seed_planting_rules` before proposing a planting slice
5. use `seed_staging_note` only when the task truly starts from staging or lineage replay

The hard rule stays the same: staging truth is weaker than owner-repo planting
truth.

## Tools

- `seed_route_catalog`: read `generated/seed_route_map.min.json`
- `seed_registry_navigation`: inspect the compact navigation view derived from `seed-registry.yaml`
- `seed_next_live`: open the current `navigation.next_live_seed` with route hints and preview
- `seed_wave_context`: inspect one wave manifest, its registry entry, and closure preview
- `seed_registry_entry`: inspect one registry seed entry with a source preview
- `seed_staging_note`: inspect one `seed_staging/...` note with lifecycle markers and warning posture
- `seed_planting_rules`: reground on `AGENTS.md`, `docs/SEED_SURFACE_MAP.md`, planting protocol, reality-check docs, and planting reports guidance
- `seed_quest_followthrough`: inspect the seed-garden quest adjunct without turning it into a second sovereignty layer

## Resources

- `dionysus://route-map`
- `dionysus://registry/navigation`
- `dionysus://next-live-seed`
- `dionysus://wave/{wave}`
- `dionysus://registry/{registry_id}`
- `dionysus://planting-rules`
- `dionysus://questbook`

## Local run

Install the optional MCP dependency:

```bash
python -m pip install -r requirements-mcp.txt
```

Run the focused MCP tests:

```bash
python -m pytest -q tests/test_dionysus_mcp_state.py
```

Start the STDIO server from the repo root:

```bash
python scripts/dionysus_mcp_server.py
```

## Project-level Codex wiring

The AoA workspace-level Codex config can wire this repo-local server with:

```toml
[mcp_servers.dionysus]
command = "python3"
args = ["scripts/dionysus_mcp_server.py"]
cwd = "/srv/Dionysus"
```

Keep the wiring project-scoped. Do not mirror personal sandbox or model
defaults into the project layer.
