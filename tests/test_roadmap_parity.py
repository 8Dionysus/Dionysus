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
    payload = load_json("generated/seed_route_map.min.json")
    next_live_seed_ref = " ".join(payload["next_live_seed_ref"].split())

    assert payload["schema_version"] == "dionysus_seed_route_map_v2"
    assert "post-wave seed-garden stewardship" in roadmap
    assert next_live_seed_ref in roadmap_normalized
    assert "opened numbered wave" in roadmap
    assert "`seed-registry.yaml`" in roadmap
    assert "`generated/seed_route_map.min.json`" in roadmap
