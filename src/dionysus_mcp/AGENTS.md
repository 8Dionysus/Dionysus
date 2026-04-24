# AGENTS.md
Local guidance for `src/dionysus_mcp/`.

Read the root `AGENTS.md` and `docs/CODEX_MCP.md` first. This package exposes a
repo-local MCP slice for seed-garden orientation.

## Local role
Keep the MCP surface route-first, read-only, and weaker than manifests,
closure notes, registry state, planting reports, and owner-repo reality.

## Editing posture
Return compact, source-linked context. Prefer previews and route maps over large
context dumps. Do not add write actions, hidden queue mutation, or owner-repo
side effects.

## Hard no
Do not let MCP convenience become seed authority or a live orchestration layer.

## Validation
Run:

```bash
python -m pytest -q tests/test_dionysus_mcp_state.py
python scripts/dionysus_mcp_server.py
```
