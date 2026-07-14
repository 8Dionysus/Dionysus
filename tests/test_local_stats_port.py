from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = REPO_ROOT / "seed-registry.yaml"
PORT_PATH = REPO_ROOT / "stats" / "port.manifest.json"
PACKET_PATH = (
    REPO_ROOT
    / "stats"
    / "packets"
    / "seed-registry-landed-post-wave-ratio.reference.json"
)


def load_registry() -> dict[str, object]:
    payload = yaml.safe_load(EVIDENCE_PATH.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


def load_packet() -> dict[str, object]:
    return json.loads(PACKET_PATH.read_text(encoding="utf-8"))


def load_port() -> dict[str, object]:
    return json.loads(PORT_PATH.read_text(encoding="utf-8"))


def derive_landed_post_wave_ratio(payload: dict[str, object]) -> dict[str, object]:
    if payload.get("registry_version") != 2:
        return {"status": "unknown", "reason": "unsupported_registry"}

    records = payload.get("seed_index")
    if not isinstance(records, list) or not records:
        return {"status": "unknown", "reason": "malformed_population"}

    registry_ids: list[str] = []
    for record in records:
        if not isinstance(record, dict):
            return {"status": "unknown", "reason": "malformed_population"}
        registry_id = record.get("registry_id")
        registry_status = record.get("registry_status")
        if (
            not isinstance(registry_id, str)
            or not registry_id
            or not isinstance(registry_status, str)
            or not registry_status
        ):
            return {"status": "unknown", "reason": "malformed_population"}
        registry_ids.append(registry_id)

    if len(registry_ids) != len(set(registry_ids)):
        return {"status": "unknown", "reason": "duplicate_registry_identity"}

    numerator = sum(
        record["registry_status"] == "landed_post_wave" for record in records
    )
    denominator = len(records)
    return {
        "status": "observed",
        "reason": "complete",
        "numerator": numerator,
        "denominator": denominator,
        "ratio": numerator / denominator,
    }


def test_reference_packet_matches_current_registry_v2() -> None:
    packet = load_packet()
    derived = derive_landed_post_wave_ratio(load_registry())

    assert derived["status"] == "observed"
    assert packet["population"]["size"] == derived["denominator"]
    assert packet["sample"]["size"] == derived["denominator"]
    assert packet["value"]["numerator"] == derived["numerator"]
    assert packet["value"]["denominator"] == derived["denominator"]
    assert packet["value"]["number"] == derived["ratio"]
    assert packet["progress"] == {"state": "terminal", "completed": 89, "total": 89}


def test_complete_population_without_landed_post_wave_is_observed_zero() -> None:
    payload = deepcopy(load_registry())
    for record in payload["seed_index"]:
        record["registry_status"] = "archived_canonical"

    derived = derive_landed_post_wave_ratio(payload)

    assert derived["status"] == "observed"
    assert derived["numerator"] == 0
    assert derived["denominator"] == 89
    assert derived["ratio"] == 0.0


def test_wave_and_origin_surfaces_do_not_enter_the_population() -> None:
    payload = deepcopy(load_registry())
    derived = derive_landed_post_wave_ratio(payload)

    assert derived["denominator"] == len(payload["seed_index"])
    assert derived["denominator"] != len(payload["wave_index"])
    assert derived["denominator"] != len(payload["origin_notes"])


def test_measurement_stays_reference_only_and_below_owner_truth() -> None:
    measurement = load_port()["measurements"][0]
    ceiling = measurement["authority_ceiling"]

    assert measurement["live_state"] == {"capability": "reference_only"}
    assert measurement["dimensions"]["allowed"] == []
    assert "target-repository merge" in ceiling
    assert "canonical meaning" in ceiling
    assert "what should be planted next" in ceiling


def test_duplicate_malformed_empty_and_unsupported_populations_are_unknown() -> None:
    valid = load_registry()
    duplicate = deepcopy(valid)
    duplicate["seed_index"].append(deepcopy(duplicate["seed_index"][0]))
    malformed = deepcopy(valid)
    del malformed["seed_index"][0]["registry_status"]
    empty = deepcopy(valid)
    empty["seed_index"] = []
    unsupported = deepcopy(valid)
    unsupported["registry_version"] = 3

    for payload in (duplicate, malformed, empty, unsupported):
        assert derive_landed_post_wave_ratio(payload)["status"] == "unknown"
