from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def load_json(relative_path: str) -> object:
    return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


def test_roadmap_names_current_next_live_seed_posture() -> None:
    roadmap = read_text("ROADMAP.md")
    roadmap_normalized = " ".join(roadmap.split())
    readme = read_text("README.md")
    changelog = read_text("CHANGELOG.md")
    payload = load_json("generated/seed_route_map.min.json")
    next_live_seed_ref = " ".join(payload["next_live_seed_ref"].split())

    assert "> Current release: `v0.1.3`" in readme
    assert "## [0.1.3] - 2026-04-23" in changelog
    assert "`v0.1.3`" in roadmap
    assert "Current release contour" in roadmap
    assert "seed-garden stewardship for release-line staging" in roadmap
    assert "Prep packs remain weaker than opened waves" in roadmap
    assert payload["schema_version"] == "dionysus_seed_route_map_v2"
    assert payload["authority_ref"] == "docs/codex/planting-protocol.md"
    assert "post-wave seed-garden stewardship" in roadmap
    assert next_live_seed_ref in roadmap_normalized
    assert "opened numbered wave" in roadmap
    assert "`seed-registry.yaml`" in roadmap
    assert "`generated/seed_route_map.min.json`" in roadmap

    current_release_surfaces = [
        "seed-registry.yaml",
        "generated/seed_route_map.min.json",
        "seed_expansion/seed.tos.wider-world-thought-expansion.v0.md",
        "docs/SEED_SURFACE_MAP.md",
        "docs/codex/planting-protocol.md",
        "docs/CODEX_MCP.md",
        "scripts/dionysus_mcp_server.py",
        "src/dionysus_mcp/server.py",
        "src/dionysus_mcp/repo_state.py",
        "tests/test_dionysus_mcp_state.py",
        "requirements-mcp.txt",
        "docs/CANDIDATE_SEED_IDENTITY.md",
        "docs/SEED_OWNER_LANDING_TRACE.md",
        "schemas/seed_lineage_entry.schema.json",
        "examples/seed_lineage_entry.example.json",
        "schemas/seed_owner_landing_trace.schema.json",
        "examples/seed_owner_landing_trace.example.json",
        "scripts/validate_seed_lineage_examples.py",
        "scripts/validate_seed_owner_landing_trace.py",
        "seed_staging/future/seed_aoa_wave3_owner_landing_followthrough_pack.md",
        "seed_staging/future/seed_aoa_wave8_campaign_cadence_pack.md",
        "seed_staging/future/seed_aoa_wave9_self_agency_continuity_pack.md",
        "seed_staging/future/seed_aoa_federation_kag_factory_upgrade_pack.md",
        "scripts/validate_seed_surfaces.py",
        "scripts/build_seed_route_map.py",
        "scripts/validate_seed_route_map.py",
        "scripts/release_check.py",
    ]
    for surface in current_release_surfaces:
        assert (REPO_ROOT / surface).exists(), surface
        assert surface in roadmap
