#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REL = Path("schemas") / "seed_owner_landing_trace.schema.json"
EXAMPLE_REL = Path("examples") / "seed_owner_landing_trace.example.json"
LINEAGE_EXAMPLE_REL = Path("examples") / "seed_lineage_entry.example.json"
SCHEMA_PATH = ROOT / SCHEMA_REL
EXAMPLE_PATH = ROOT / EXAMPLE_REL
LINEAGE_EXAMPLE_PATH = ROOT / LINEAGE_EXAMPLE_REL
REQUIRED_SCHEMA_FIELDS = (
    "schema_version",
    "candidate_ref",
    "seed_ref",
    "owner_repo",
    "owner_shape",
    "outcome",
    "owner_status_ref",
    "object_ref",
    "merged_into",
    "superseded_by",
    "drop_reason",
    "observed_at",
    "evidence_refs",
)


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def display_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_json(path: Path, root: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        fail(f"missing required file: {display_path(path, root)}")
        raise AssertionError("unreachable") from exc
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {display_path(path, root)}: {exc}")
        raise AssertionError("unreachable") from exc


def validate_schema_contract(schema: object, *, root: Path) -> None:
    if not isinstance(schema, dict):
        fail(f"{display_path(root / SCHEMA_REL, root)} must be a JSON object")
    if schema.get("title") != "Dionysus seed_owner_landing_trace_v1":
        fail(
            f"{display_path(root / SCHEMA_REL, root)} title must equal "
            "'Dionysus seed_owner_landing_trace_v1'"
        )
    if schema.get("type") != "object":
        fail(f"{display_path(root / SCHEMA_REL, root)} type must equal 'object'")
    if schema.get("additionalProperties") is not False:
        fail(f"{display_path(root / SCHEMA_REL, root)} must set additionalProperties to false")
    required = schema.get("required")
    if required != list(REQUIRED_SCHEMA_FIELDS):
        fail(f"{display_path(root / SCHEMA_REL, root)} required fields must stay aligned with the local contract")
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        fail(f"{display_path(root / SCHEMA_REL, root)} properties must be an object")
    version_payload = properties.get("schema_version")
    if (
        not isinstance(version_payload, dict)
        or version_payload.get("const") != "dionysus_seed_owner_landing_trace_v1"
    ):
        fail(
            f"{display_path(root / SCHEMA_REL, root)} schema_version.const must equal "
            "'dionysus_seed_owner_landing_trace_v1'"
        )


def validate_example_payload(
    payload: object,
    schema: object,
    lineage_payload: object,
    *,
    root: Path,
) -> None:
    if not isinstance(payload, dict):
        fail(f"{display_path(root / EXAMPLE_REL, root)} must be a JSON object")
    if not isinstance(lineage_payload, dict):
        fail(f"{display_path(root / LINEAGE_EXAMPLE_REL, root)} must be a JSON object")

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda error: list(error.absolute_path))
    if errors:
        error = errors[0]
        path = ".".join(str(item) for item in error.absolute_path)
        if path:
            fail(f"{display_path(root / EXAMPLE_REL, root)} schema violation at '{path}': {error.message}")
        fail(f"{display_path(root / EXAMPLE_REL, root)} schema violation: {error.message}")

    if payload["candidate_ref"] != lineage_payload["candidate_ref"]:
        fail(f"{display_path(root / EXAMPLE_REL, root)} candidate_ref must stay aligned with seed_lineage_entry.example.json")
    if payload["seed_ref"] != lineage_payload["seed_ref"]:
        fail(f"{display_path(root / EXAMPLE_REL, root)} seed_ref must stay aligned with seed_lineage_entry.example.json")
    if payload.get("cluster_ref") is not None and payload["cluster_ref"] != lineage_payload["cluster_ref"]:
        fail(f"{display_path(root / EXAMPLE_REL, root)} cluster_ref must stay aligned with seed_lineage_entry.example.json when present")
    if payload["seed_ref"] == payload["candidate_ref"]:
        fail(f"{display_path(root / EXAMPLE_REL, root)} seed_ref must stay distinct from candidate_ref")

    outcome = payload["outcome"]
    owner_status_ref = payload["owner_status_ref"]
    object_ref = payload["object_ref"]
    merged_into = payload["merged_into"]
    drop_reason = payload["drop_reason"]

    if outcome == "landed_owner_status" and owner_status_ref is None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} outcome 'landed_owner_status' requires owner_status_ref")
    if outcome != "landed_owner_status" and owner_status_ref is not None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} owner_status_ref requires outcome 'landed_owner_status'")
    if outcome == "landed_owner_status" and object_ref is not None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} landed_owner_status must keep object_ref null")
    if outcome == "landed_owner_object" and object_ref is None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} outcome 'landed_owner_object' requires object_ref")
    if outcome in {"reanchored", "merged", "deferred", "dropped"} and object_ref is not None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} object_ref is only allowed for outcome 'landed_owner_object'")
    if outcome == "merged" and merged_into is None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} outcome 'merged' requires merged_into")
    if outcome != "merged" and merged_into is not None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} merged_into requires outcome 'merged'")
    if outcome == "dropped" and drop_reason is None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} outcome 'dropped' requires drop_reason")
    if outcome != "dropped" and drop_reason is not None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} drop_reason requires outcome 'dropped'")


def validate_seed_owner_landing_trace(root: Path = ROOT) -> None:
    schema = read_json(root / SCHEMA_REL, root)
    validate_schema_contract(schema, root=root)
    payload = read_json(root / EXAMPLE_REL, root)
    lineage_payload = read_json(root / LINEAGE_EXAMPLE_REL, root)
    validate_example_payload(payload, schema, lineage_payload, root=root)


def run_validation(root: Path = ROOT) -> list[str]:
    try:
        validate_seed_owner_landing_trace(root)
    except ValidationError as exc:
        return [str(exc)]
    return []


def main() -> int:
    errors = run_validation(ROOT)
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print("[ok] validated seed owner landing trace")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
