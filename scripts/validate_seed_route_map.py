#!/usr/bin/env python3
"""Validate the Dionysus seed-route capsule surface."""

from __future__ import annotations

import json

from seed_route_map_common import (
    ROUTE_SPECS,
    SEED_ROUTE_MAP_PATH,
    SURFACE_PAYLOAD,
    build_payload,
    resolve_ref,
)


def main() -> int:
    expected_payload = build_payload()
    current_payload = json.loads(SEED_ROUTE_MAP_PATH.read_text(encoding="utf-8"))
    if current_payload != expected_payload:
        raise SystemExit("generated/seed_route_map.min.json does not match the canonical rebuild")

    for key, expected in SURFACE_PAYLOAD.items():
        if current_payload.get(key) != expected:
            raise SystemExit(f"generated/seed_route_map.min.json must keep {key}={expected!r}")
        if key == "authority_ref":
            resolve_ref(expected)

    next_live_seed_ref = current_payload.get("next_live_seed_ref")
    if not isinstance(next_live_seed_ref, str) or not next_live_seed_ref.strip():
        raise SystemExit("generated/seed_route_map.min.json must publish next_live_seed_ref")
    resolve_ref(next_live_seed_ref)

    routes = current_payload.get("routes")
    if not isinstance(routes, list) or len(routes) != len(ROUTE_SPECS):
        raise SystemExit("generated/seed_route_map.min.json must publish exactly three seed routes")

    for route, spec in zip(routes, ROUTE_SPECS, strict=True):
        if not isinstance(route, dict):
            raise SystemExit("generated/seed_route_map.min.json routes must be objects")
        if route.get("route_id") != spec["route_id"] or route.get("need") != spec["need"]:
            raise SystemExit(f"generated/seed_route_map.min.json route '{spec['route_id']}' drifted")
        surface_ref = route.get("surface_ref")
        if not isinstance(surface_ref, str) or not surface_ref.strip():
            raise SystemExit("generated/seed_route_map.min.json routes must carry a non-empty surface_ref")
        resolve_ref(surface_ref)
        if spec["route_id"] == "next-live-seed" and surface_ref != next_live_seed_ref:
            raise SystemExit("generated/seed_route_map.min.json next-live-seed must follow navigation.next_live_seed")
        if spec["route_id"] != "next-live-seed" and surface_ref != spec["surface_ref"]:
            raise SystemExit(f"generated/seed_route_map.min.json route '{spec['route_id']}' must keep surface_ref")
        verification_refs = route.get("verification_refs")
        if not isinstance(verification_refs, list) or not verification_refs:
            raise SystemExit("generated/seed_route_map.min.json verification_refs must be a non-empty list")
        for ref in verification_refs:
            if not isinstance(ref, str) or not ref.strip():
                raise SystemExit("generated/seed_route_map.min.json verification_refs must contain strings")
            resolve_ref(ref)

    print("[ok] validated generated/seed_route_map.min.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
