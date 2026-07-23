#!/usr/bin/env python3
"""Validate the public Dionysus skeleton without third-party dependencies."""

from __future__ import annotations

import json
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = (
    "README.md",
    "AGENTS.md",
    "DESIGN.md",
    "LICENSE",
    "ROADMAP.md",
    "docs/PRIVACY.md",
    "docs/decisions/DION-D-0001-conversational-self-portrait.md",
    "interviews/catalog.toml",
    "interviews/session-contract.md",
    "portrait/templates/KERNEL.md",
    "portrait/templates/NOW.md",
    "portrait/templates/COUNTERWEIGHTS.md",
    "schemas/interview-session.schema.json",
    "schemas/portrait-claim.schema.json",
    "examples/interview-session.example.json",
    "examples/portrait-claim.example.json",
    "vault/README.md",
    "legacy/seed-garden/README.md",
    "legacy/seed-garden/AGENTS.md",
    "legacy/seed-garden/seed-registry.yaml",
)

LEGACY_ROOT_PATHS = (
    "archive",
    "seed_expansion",
    "seed_notes",
    "seed_staging",
    "seed-registry.yaml",
)

MEDIA_SUFFIXES = {
    ".aac",
    ".flac",
    ".m4a",
    ".mp3",
    ".mp4",
    ".ogg",
    ".opus",
    ".wav",
    ".webm",
}

PROTOCOL_KINDS = {"baseline", "depth", "counterportrait", "refresh", "event"}
PROTOCOL_MODES = {"voice", "text", "hybrid"}
MATURITY_STATES = {"skeleton", "draft", "pilot", "validated"}


class ValidationError(Exception):
    """A reader-facing validation failure."""


def load_json(relative_path: str) -> Any:
    path = ROOT / relative_path
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"{relative_path}: invalid JSON: {exc}") from exc


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def matches_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    raise ValidationError(f"validator does not support JSON Schema type {expected!r}")


def validate_instance(value: Any, schema: dict[str, Any], location: str) -> None:
    if "const" in schema:
        require(value == schema["const"], f"{location}: expected {schema['const']!r}")

    expected = schema.get("type")
    if expected is not None:
        expected_types = [expected] if isinstance(expected, str) else expected
        require(
            any(matches_type(value, item) for item in expected_types),
            f"{location}: expected type {expected_types}, got {type(value).__name__}",
        )

    if "enum" in schema:
        require(value in schema["enum"], f"{location}: unsupported value {value!r}")

    if isinstance(value, str):
        require(
            len(value) >= schema.get("minLength", 0),
            f"{location}: string is shorter than minLength",
        )

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema:
            require(value >= schema["minimum"], f"{location}: below minimum")
        if "maximum" in schema:
            require(value <= schema["maximum"], f"{location}: above maximum")

    if isinstance(value, list):
        require(
            len(value) >= schema.get("minItems", 0),
            f"{location}: array is shorter than minItems",
        )
        if schema.get("uniqueItems"):
            serialized = [json.dumps(item, sort_keys=True) for item in value]
            require(len(serialized) == len(set(serialized)), f"{location}: duplicate items")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                validate_instance(item, item_schema, f"{location}[{index}]")

    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for name in schema.get("required", []):
            require(name in value, f"{location}: missing required property {name!r}")
        if schema.get("additionalProperties") is False:
            extras = set(value) - set(properties)
            require(not extras, f"{location}: unsupported properties {sorted(extras)}")
        for name, child in value.items():
            if name in properties:
                validate_instance(child, properties[name], f"{location}.{name}")


def validate_required_paths() -> None:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).is_file()]
    require(not missing, f"missing required files: {missing}")

    old_roots = [path for path in LEGACY_ROOT_PATHS if (ROOT / path).exists()]
    require(not old_roots, f"old seed-garden paths remain active at root: {old_roots}")

    legacy_count = sum(1 for path in (ROOT / "legacy/seed-garden").rglob("*") if path.is_file())
    require(legacy_count >= 400, f"legacy seed garden looks incomplete: {legacy_count} files")


def validate_catalog() -> None:
    catalog_path = ROOT / "interviews/catalog.toml"
    try:
        catalog = tomllib.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise ValidationError(f"interviews/catalog.toml: invalid TOML: {exc}") from exc

    require(catalog.get("schema_version") == "0.1.0", "catalog: unsupported schema_version")
    lenses = catalog.get("lenses", [])
    protocols = catalog.get("protocols", [])
    lens_ids = [lens.get("id") for lens in lenses]
    protocol_ids = [protocol.get("id") for protocol in protocols]
    require(len(lens_ids) == len(set(lens_ids)), "catalog: duplicate lens IDs")
    require(len(protocol_ids) == len(set(protocol_ids)), "catalog: duplicate protocol IDs")
    require(set(PROTOCOL_KINDS) == {item.get("kind") for item in protocols}, "catalog: initial protocol family is incomplete")

    for protocol in protocols:
        location = f"catalog protocol {protocol.get('id', '<missing>')}"
        require(protocol.get("id"), f"{location}: missing ID")
        require(protocol.get("kind") in PROTOCOL_KINDS, f"{location}: invalid kind")
        require(protocol.get("maturity") in MATURITY_STATES, f"{location}: invalid maturity")
        require(protocol.get("preferred_mode") in PROTOCOL_MODES, f"{location}: invalid mode")
        duration = protocol.get("duration_hint_minutes")
        require(
            isinstance(duration, list)
            and len(duration) == 2
            and all(isinstance(item, int) and item > 0 for item in duration)
            and duration[0] <= duration[1],
            f"{location}: invalid duration hint",
        )
        unknown = set(protocol.get("lenses", [])) - set(lens_ids)
        require(not unknown, f"{location}: unknown lenses {sorted(unknown)}")
        require(protocol.get("purpose"), f"{location}: missing purpose")


def validate_schemas_and_examples() -> None:
    pairs = (
        ("schemas/interview-session.schema.json", "examples/interview-session.example.json"),
        ("schemas/portrait-claim.schema.json", "examples/portrait-claim.example.json"),
    )
    for schema_path, example_path in pairs:
        schema = load_json(schema_path)
        example = load_json(example_path)
        require(schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", f"{schema_path}: unexpected JSON Schema dialect")
        require(schema.get("$id"), f"{schema_path}: missing $id")
        validate_instance(example, schema, example_path)


def validate_public_boundary() -> None:
    vault_entries = [
        path
        for path in (ROOT / "vault").rglob("*")
        if path.is_file() and path.relative_to(ROOT).as_posix() != "vault/README.md"
    ]
    require(not vault_entries, f"private vault contains unexpected files: {vault_entries}")

    tracked = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8").split("\0")
    tracked = [path for path in tracked if path]
    tracked_vault = [path for path in tracked if path.startswith("vault/")]
    require(
        set(tracked_vault).issubset({"vault/README.md"}),
        f"private vault files are tracked: {tracked_vault}",
    )
    media = [path for path in tracked if Path(path).suffix.lower() in MEDIA_SUFFIXES]
    require(not media, f"media files are tracked in the public repository: {media}")


def main() -> int:
    checks = (
        validate_required_paths,
        validate_catalog,
        validate_schemas_and_examples,
        validate_public_boundary,
    )
    try:
        for check in checks:
            check()
    except (ValidationError, subprocess.CalledProcessError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print("OK: Dionysus skeleton is structurally valid")
    print("OK: interview catalog contains five distinct skeleton protocols")
    print("OK: fictional examples satisfy the public schemas")
    print("OK: legacy seed garden is isolated and the private vault is empty")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
