from __future__ import annotations

import json
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from seed_route_map_common import (  # noqa: E402
    ROUTE_SPECS,
    SEED_ROUTE_MAP_PATH,
    SURFACE_PAYLOAD,
    build_payload,
)


def test_build_payload_stays_seed_only() -> None:
    payload = build_payload()

    assert payload["schema_version"] == "dionysus_seed_route_map_v1"
    assert payload["owner_repo"] == "Dionysus"
    assert payload["surface_kind"] == "seed"
    assert [route["route_id"] for route in payload["routes"]] == [
        "next-live-seed",
        "registry-validation",
        "questbook-follow-through",
    ]


def test_generated_surface_matches_canonical_build() -> None:
    current = json.loads(SEED_ROUTE_MAP_PATH.read_text(encoding="utf-8"))

    assert current == build_payload()


def test_surface_keeps_expected_refs() -> None:
    payload = build_payload()

    assert payload["authority_ref"] == SURFACE_PAYLOAD["authority_ref"]
    assert payload["routes"][1]["surface_ref"] == ROUTE_SPECS[1]["surface_ref"]
    assert payload["routes"][2]["surface_ref"] == ROUTE_SPECS[2]["surface_ref"]
