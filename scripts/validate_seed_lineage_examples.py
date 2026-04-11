#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REL = Path("schemas") / "seed_lineage_entry.schema.json"
EXAMPLE_REL = Path("examples") / "seed_lineage_entry.example.json"
SCHEMA_PATH = ROOT / SCHEMA_REL
EXAMPLE_PATH = ROOT / EXAMPLE_REL
REQUIRED_SCHEMA_FIELDS = (
    "schema_version",
    "seed_ref",
    "candidate_ref",
    "cluster_ref",
    "owner_hypothesis",
    "owner_shape",
    "lifecycle_status",
    "status_posture",
    "evidence_refs",
    "supersedes",
    "merged_into",
    "drop_reason",
    "object_ref",
)
PRE_PLANT_STATES = {"staged", "open-wave", "planting-in-progress"}


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
    if schema.get("title") != "Dionysus seed_lineage_entry_v1":
        fail(f"{display_path(root / SCHEMA_REL, root)} title must equal 'Dionysus seed_lineage_entry_v1'")
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
    if not isinstance(version_payload, dict) or version_payload.get("const") != "dionysus_seed_lineage_entry_v1":
        fail(
            f"{display_path(root / SCHEMA_REL, root)} schema_version.const must equal "
            "'dionysus_seed_lineage_entry_v1'"
        )


def validate_example_payload(payload: object, schema: object, *, root: Path) -> None:
    if not isinstance(payload, dict):
        fail(f"{display_path(root / EXAMPLE_REL, root)} must be a JSON object")
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda error: list(error.absolute_path))
    if errors:
        error = errors[0]
        path = ".".join(str(item) for item in error.absolute_path)
        if path:
            fail(f"{display_path(root / EXAMPLE_REL, root)} schema violation at '{path}': {error.message}")
        fail(f"{display_path(root / EXAMPLE_REL, root)} schema violation: {error.message}")

    lifecycle_status = payload["lifecycle_status"]
    object_ref = payload["object_ref"]
    merged_into = payload["merged_into"]
    drop_reason = payload["drop_reason"]
    supersedes = payload["supersedes"]

    if lifecycle_status in PRE_PLANT_STATES and object_ref is not None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} must keep object_ref null before planting")
    if lifecycle_status == "planted" and object_ref is None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} must carry object_ref once lifecycle_status is 'planted'")
    if merged_into is not None and lifecycle_status != "superseded":
        fail(f"{display_path(root / EXAMPLE_REL, root)} merged_into requires lifecycle_status 'superseded'")
    if lifecycle_status == "superseded" and merged_into is None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} lifecycle_status 'superseded' requires merged_into")
    if drop_reason is not None and lifecycle_status != "dropped":
        fail(f"{display_path(root / EXAMPLE_REL, root)} drop_reason requires lifecycle_status 'dropped'")
    if lifecycle_status == "dropped" and drop_reason is None:
        fail(f"{display_path(root / EXAMPLE_REL, root)} lifecycle_status 'dropped' requires drop_reason")
    if payload["seed_ref"] == payload["candidate_ref"]:
        fail(f"{display_path(root / EXAMPLE_REL, root)} seed_ref must stay distinct from candidate_ref")
    if payload["seed_ref"] in supersedes:
        fail(f"{display_path(root / EXAMPLE_REL, root)} supersedes must not include the current seed_ref")


def validate_seed_lineage_examples(root: Path = ROOT) -> None:
    schema = read_json(root / SCHEMA_REL, root)
    validate_schema_contract(schema, root=root)
    payload = read_json(root / EXAMPLE_REL, root)
    validate_example_payload(payload, schema, root=root)


def run_validation(root: Path = ROOT) -> list[str]:
    try:
        validate_seed_lineage_examples(root)
    except ValidationError as exc:
        return [str(exc)]
    return []


def main() -> int:
    errors = run_validation(ROOT)
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print("[ok] validated seed lineage examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
