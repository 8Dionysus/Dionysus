#!/usr/bin/env python3
"""Shared builder helpers for the Dionysus seed-route capsule."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SEED_REGISTRY_PATH = REPO_ROOT / "seed-registry.yaml"
SEED_ROUTE_MAP_PATH = REPO_ROOT / "generated" / "seed_route_map.min.json"

SURFACE_PAYLOAD = {
    "schema_version": "dionysus_seed_route_map_v1",
    "owner_repo": "Dionysus",
    "surface_kind": "seed",
    "authority_ref": "docs/codex/planting-protocol.md",
}

ROUTE_SPECS = (
    {
        "route_id": "next-live-seed",
        "need": "locate the current gated live seed before opening staging or owner-repo follow-through",
    },
    {
        "route_id": "registry-validation",
        "need": "validate registry and seed-surface coherence before trusting a seed route",
        "surface_ref": "scripts/validate_seed_surfaces.py",
        "verification_refs": [
            "scripts/validate_seed_registry.py",
            "schema/seed-registry.contract.yaml",
        ],
    },
    {
        "route_id": "questbook-follow-through",
        "need": "inspect seed-garden quest follow-through without mistaking it for owner sovereignty",
        "surface_ref": "generated/quest_catalog.min.json",
        "verification_refs": [
            "generated/quest_dispatch.min.json",
            "QUESTBOOK.md",
        ],
    },
)

MARKDOWN_HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
HTML_ID = re.compile(r'<a\s+id="([^"]+)"></a>', re.IGNORECASE)


def load_registry() -> dict[str, object]:
    payload = yaml.safe_load(SEED_REGISTRY_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("seed-registry.yaml must parse as an object")
    return payload


def markdown_anchor(text: str) -> str:
    anchor = text.strip().lower()
    anchor = re.sub(r"[^\w\s-]", "", anchor)
    anchor = re.sub(r"\s+", "-", anchor)
    anchor = re.sub(r"-+", "-", anchor)
    return anchor.strip("-")


@lru_cache(maxsize=None)
def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        for html_match in HTML_ID.finditer(line):
            anchors.add(html_match.group(1))
        match = MARKDOWN_HEADING.match(line)
        if not match:
            continue
        base = markdown_anchor(match.group(2))
        if not base:
            continue
        suffix = seen.get(base, 0)
        seen[base] = suffix + 1
        anchors.add(base if suffix == 0 else f"{base}-{suffix}")
    return anchors


def resolve_ref(value: str) -> Path:
    path_text, _, anchor = value.partition("#")
    target = REPO_ROOT / path_text
    if not target.exists():
        raise ValueError(f"missing ref target '{value}'")
    if anchor:
        if target.suffix.lower() != ".md":
            raise ValueError(f"only markdown refs may carry anchors: '{value}'")
        if anchor not in anchors_for(target):
            raise ValueError(f"missing markdown anchor in ref '{value}'")
    return target


def build_payload() -> dict[str, object]:
    registry = load_registry()
    navigation = registry.get("navigation")
    if not isinstance(navigation, dict):
        raise ValueError("seed-registry.yaml must define navigation")
    next_live_seed_ref = navigation.get("next_live_seed")
    if not isinstance(next_live_seed_ref, str) or not next_live_seed_ref.strip():
        raise ValueError("seed-registry.yaml navigation.next_live_seed must be a non-empty string")

    resolve_ref(SURFACE_PAYLOAD["authority_ref"])
    resolve_ref("seed-registry.yaml")
    resolve_ref(next_live_seed_ref)

    routes: list[dict[str, object]] = [
        {
            "route_id": ROUTE_SPECS[0]["route_id"],
            "need": ROUTE_SPECS[0]["need"],
            "surface_ref": next_live_seed_ref,
            "verification_refs": [
                "seed-registry.yaml",
                "docs/codex/planting-protocol.md",
            ],
        }
    ]
    for spec in ROUTE_SPECS[1:]:
        resolve_ref(spec["surface_ref"])
        for ref in spec["verification_refs"]:
            resolve_ref(ref)
        routes.append(
            {
                "route_id": spec["route_id"],
                "need": spec["need"],
                "surface_ref": spec["surface_ref"],
                "verification_refs": list(spec["verification_refs"]),
            }
        )

    return {
        **SURFACE_PAYLOAD,
        "next_live_seed_ref": next_live_seed_ref,
        "routes": routes,
    }


def render_payload(payload: dict[str, object]) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"
