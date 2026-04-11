from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from dionysus_mcp.repo_state import DionysusRepoState, RepoStateError  # noqa: E402


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _build_fixture_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "Dionysus"
    _write(repo / "AGENTS.md", "# AGENTS\nroot guidance\n")
    _write(repo / "README.md", "# README\nseed garden\n")
    _write(repo / "QUESTBOOK.md", "# QUESTBOOK\nquest follow-through\n")
    _write(repo / "docs/SEED_SURFACE_MAP.md", "# map\nread order\n")
    _write(repo / "docs/codex/planting-protocol.md", "# protocol\nmanifest first\n")
    _write(repo / "docs/codex/owner-repo-reality-check.md", "# reality\nowner repo wins\n")
    _write(repo / "docs/codex/AGENTS.md", "# codex guidance\n")
    _write(repo / "reports/planting/README.md", "# reports\ndurable trace\n")
    _write(repo / "reports/planting/AGENTS.md", "# planting guidance\n")
    _write(repo / "seed_expansion/AGENTS.md", "# expansion guidance\n")
    _write(repo / "archive/AGENTS.md", "# archive guidance\n")
    _write(
        repo / "seed_expansion/seed.live.md",
        "# Live Seed\n\n## Wider World Thought Expansion\nOpen the next live seed.\n",
    )
    _write(
        repo / "seed_staging/future/pack.md",
        "---\nlifecycle_status: staged\nlifecycle_note: owner repo still pending\nreality_checked_at: 2026-04-10\n---\n\n# future pack\n",
    )
    _write(
        repo / "ninth_wave.manifest.json",
        json.dumps(
            {
                "version": 1,
                "mode": "contract_growth",
                "canonical_sources": ["archive/seed_rootline/seed.example.md"],
                "ninth_wave_order": [
                    {
                        "id": "seed-example",
                        "label": "Seed Example",
                        "source": "archive/seed_rootline/seed.example.md",
                    }
                ],
                "supporting_notes": ["ninth_wave.closure.md"],
            }
        ),
    )
    _write(repo / "ninth_wave.closure.md", "# Closure\nwave closed\n")
    _write(repo / "archive/seed_rootline/seed.example.md", "# Seed Example\nsource text\n")
    registry = {
        "registry_version": 2,
        "updated_at": "2026-04-10",
        "navigation": {
            "canonical_order_source": "wave manifests",
            "semantic_source": "source seed files",
            "validation_entrypoint": "scripts/validate_seed_surfaces.py",
            "registry_contract": "schema/seed-registry.contract.yaml",
            "next_live_seed": "seed_expansion/seed.live.md#wider-world-thought-expansion",
            "archived_root": "archive/",
            "archived_pack": "archive/seed_pack_2026-03-22/",
        },
        "lifecycle_states": {
            "archived_canonical": "historical source kept for lineage and replay",
            "gated_next": "acknowledged next seed surface",
        },
        "origin_notes": ["seed_notes/exploratory/origin.md"],
        "wave_index": [
            {
                "wave": "ninth_wave",
                "file": "ninth_wave.manifest.json",
                "mode": "contract_growth",
                "registry_status": "archived_canonical",
                "summary": "example wave",
                "closure_note": "ninth_wave.closure.md",
            }
        ],
        "seed_index": [
            {
                "registry_id": "live-seed",
                "label": "Live Seed",
                "source_ref": "seed_expansion/seed.live.md#wider-world-thought-expansion",
                "wave": None,
                "projects": ["ToS"],
                "kind": "knowledge-seed",
                "registry_status": "gated_next",
                "parent_seed": None,
                "repo_homes": ["Tree-of-Sophia"],
                "first_artifact_hint": "one note",
                "notes": "example",
                "provenance": {
                    "origin_mode": "native",
                    "donor_repo": None,
                    "donor_ref": None,
                    "donor_license_spdx": None,
                    "donor_paths": [],
                    "provenance_note": None,
                },
                "redistribution": {
                    "license_spdx": None,
                    "upstream_license_ref": None,
                    "copy_license_required": False,
                    "notice_required": False,
                    "retain_attribution_required": False,
                    "mark_modifications_required": False,
                    "modified_from_upstream": False,
                    "obligations_note": None,
                },
                "transplant": {
                    "policy": "native",
                    "what_survives": ["the seed"],
                    "what_stays_behind": ["nothing external"],
                    "non_goals": ["no runtime"],
                },
            },
            {
                "registry_id": "seed-example",
                "label": "Seed Example",
                "source_ref": "archive/seed_rootline/seed.example.md",
                "wave": "ninth_wave",
                "projects": ["AoA"],
                "kind": "architectural-seed",
                "registry_status": "archived_canonical",
                "parent_seed": None,
                "repo_homes": ["Agents-of-Abyss"],
                "first_artifact_hint": "one structural file",
                "notes": "example",
                "provenance": {
                    "origin_mode": "native",
                    "donor_repo": None,
                    "donor_ref": None,
                    "donor_license_spdx": None,
                    "donor_paths": [],
                    "provenance_note": None,
                },
                "redistribution": {
                    "license_spdx": None,
                    "upstream_license_ref": None,
                    "copy_license_required": False,
                    "notice_required": False,
                    "retain_attribution_required": False,
                    "mark_modifications_required": False,
                    "modified_from_upstream": False,
                    "obligations_note": None,
                },
                "transplant": {
                    "policy": "native",
                    "what_survives": ["the pattern"],
                    "what_stays_behind": ["none"],
                    "non_goals": ["no runtime"],
                },
            },
        ],
    }
    _write(repo / "seed-registry.yaml", yaml.safe_dump(registry, sort_keys=False))
    _write(
        repo / "generated/seed_route_map.min.json",
        json.dumps(
            {
                "schema_version": "dionysus_seed_route_map_v2",
                "next_live_seed_ref": "seed_expansion/seed.live.md#wider-world-thought-expansion",
                "routes": [
                    {
                        "route_id": "next-live-seed",
                        "need": "locate current live seed",
                        "surface_ref": "seed_expansion/seed.live.md#wider-world-thought-expansion",
                        "verification_refs": [
                            "seed-registry.yaml",
                            "docs/codex/planting-protocol.md",
                        ],
                    }
                ],
            }
        ),
    )
    _write(
        repo / "generated/quest_catalog.min.json",
        json.dumps(
            [
                {"id": "DION-SEED-Q-0001", "state": "done"},
                {"id": "DION-SEED-Q-0003", "state": "captured"},
            ]
        ),
    )
    _write(
        repo / "generated/quest_dispatch.min.json",
        json.dumps([{"id": "DION-SEED-Q-0001", "delegate_tier": "executor"}]),
    )
    return repo


def test_discover_and_registry_navigation(tmp_path: Path) -> None:
    repo = _build_fixture_repo(tmp_path)
    state = DionysusRepoState.discover(repo)

    navigation = state.build_registry_navigation()

    assert navigation["registry_version"] == 2
    assert navigation["navigation"]["next_live_seed"].startswith("seed_expansion/")
    assert navigation["counts"]["seed_entries"] == 2


def test_load_next_live_seed_reads_route_and_surface(tmp_path: Path) -> None:
    repo = _build_fixture_repo(tmp_path)
    state = DionysusRepoState.discover(repo)

    payload = state.load_next_live_seed(limit=5)

    assert payload["route_hint"]["route_id"] == "next-live-seed"
    assert payload["surface"]["path"] == "seed_expansion/seed.live.md"
    assert payload["surface"]["anchor_found"] is True
    assert "Wider World Thought Expansion" in payload["surface"]["excerpt"]


def test_load_wave_context_resolves_manifest_and_closure(tmp_path: Path) -> None:
    repo = _build_fixture_repo(tmp_path)
    state = DionysusRepoState.discover(repo)

    payload = state.load_wave_context("ninth")

    assert payload["wave"] == "ninth_wave"
    assert payload["wave_entry"]["closure_note"] == "ninth_wave.closure.md"
    assert payload["ordered_lists"]["ninth_wave_order"][0]["id"] == "seed-example"
    assert "Closure" in payload["closure_preview"]["excerpt"]


def test_load_registry_entry_includes_source_preview(tmp_path: Path) -> None:
    repo = _build_fixture_repo(tmp_path)
    state = DionysusRepoState.discover(repo)

    payload = state.load_registry_entry("seed-example")

    assert payload["registry_entry"]["registry_id"] == "seed-example"
    assert "Seed Example" in payload["source_preview"]["excerpt"]


def test_load_staging_note_extracts_frontmatter_and_warning(tmp_path: Path) -> None:
    repo = _build_fixture_repo(tmp_path)
    state = DionysusRepoState.discover(repo)

    payload = state.load_staging_note("seed_staging/future/pack.md")

    assert payload["lifecycle_markers"]["lifecycle_status"] == "staged"
    assert "owner-repo" in payload["warning"]


def test_build_planting_rules_bundle_contains_expected_refs(tmp_path: Path) -> None:
    repo = _build_fixture_repo(tmp_path)
    state = DionysusRepoState.discover(repo)

    payload = state.build_planting_rules_bundle()

    assert "docs/codex/planting-protocol.md" in payload["source_refs"]
    assert any(item["path"] == "reports/planting/README.md" for item in payload["bundle"])


def test_path_escape_is_blocked(tmp_path: Path) -> None:
    repo = _build_fixture_repo(tmp_path)
    state = DionysusRepoState.discover(repo)

    try:
        state.load_staging_note("../outside.md")
    except RepoStateError as exc:
        assert "seed_staging" in str(exc) or "allowed" in str(exc)
    else:
        raise AssertionError("Expected RepoStateError for path escape")
