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
    "docs/decisions/DION-D-0002-instrument-registry-boundary.md",
    "docs/decisions/DION-D-0003-local-reflection-workbook.md",
    "instruments/AGENTS.md",
    "instruments/README.md",
    "instruments/admission-contract.md",
    "instruments/registry.toml",
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
    "web/AGENTS.md",
    "web/README.md",
    "web/favicon.svg",
    "web/index.html",
    "web/styles.css",
    "web/app.js",
)

PUBLIC_TRACKED_PATHS = (
    ".github",
    ".gitignore",
    ".ignore",
    "AGENTS.md",
    "DESIGN.md",
    "LICENSE",
    "README.md",
    "ROADMAP.md",
    "docs",
    "examples",
    "instruments",
    "interviews",
    "portrait",
    "schemas",
    "scripts",
    "vault",
    "web",
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
INSTRUMENT_ADMISSION_STATES = {"admitted", "external-only", "pilot", "excluded"}
INSTRUMENT_VOICE_POSTURES = {
    "conversation-native",
    "unverified",
    "verbatim-pilot",
    "equivalent",
    "not-applicable",
}
INSTRUMENT_CONTENT_POSTURES = {
    "reference-and-adaptation-allowed",
    "dionysus-authored-elicitation-only",
    "reference-only",
    "open-source-items-no-vendored-form",
    "licensed-source-available",
    "do-not-vendor",
}
FORBIDDEN_INSTRUMENT_KEYS = {
    "items",
    "item_text",
    "norms",
    "responses",
    "scores",
    "scoring_key",
}


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


def validate_instrument_registry() -> None:
    registry_path = ROOT / "instruments/registry.toml"
    try:
        registry = tomllib.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise ValidationError(f"instruments/registry.toml: invalid TOML: {exc}") from exc

    require(
        registry.get("schema_version") == "0.1.0",
        "instrument registry: unsupported schema_version",
    )
    require(registry.get("reviewed_on"), "instrument registry: missing review date")
    require(registry.get("purpose"), "instrument registry: missing purpose")
    require(registry.get("authority"), "instrument registry: missing authority boundary")

    instruments = registry.get("instruments", [])
    require(instruments, "instrument registry: no entries")
    instrument_ids = [item.get("id") for item in instruments]
    require(
        len(instrument_ids) == len(set(instrument_ids)),
        "instrument registry: duplicate IDs",
    )
    observed_states = {item.get("admission") for item in instruments}
    require(
        "admitted" in observed_states,
        "instrument registry: at least one bounded method must be admitted",
    )
    require(
        observed_states & {"external-only", "pilot", "excluded"},
        "instrument registry: must preserve at least one explicit non-admission boundary",
    )

    required_strings = {
        "id",
        "name",
        "family",
        "kind",
        "role",
        "language_posture",
        "license_posture",
        "content_posture",
        "voice_posture",
        "interpretation_posture",
        "decision_note",
    }
    for instrument in instruments:
        location = f"instrument {instrument.get('id', '<missing>')}"
        forbidden = set(instrument) & FORBIDDEN_INSTRUMENT_KEYS
        require(not forbidden, f"{location}: protected or private content keys are forbidden: {sorted(forbidden)}")

        for field in required_strings:
            require(
                isinstance(instrument.get(field), str) and instrument[field].strip(),
                f"{location}: missing or empty {field}",
            )

        admission = instrument.get("admission")
        require(
            admission in INSTRUMENT_ADMISSION_STATES,
            f"{location}: invalid admission state",
        )
        require(
            instrument.get("voice_posture") in INSTRUMENT_VOICE_POSTURES,
            f"{location}: invalid voice posture",
        )
        require(
            instrument.get("content_posture") in INSTRUMENT_CONTENT_POSTURES,
            f"{location}: invalid content posture",
        )

        for field in ("source_urls", "evidence_urls"):
            urls = instrument.get(field)
            require(isinstance(urls, list) and urls, f"{location}: {field} must be non-empty")
            require(
                all(isinstance(url, str) and url.startswith("https://") for url in urls),
                f"{location}: {field} must contain only HTTPS URLs",
            )

        gaps = instrument.get("blocking_gaps")
        require(isinstance(gaps, list), f"{location}: blocking_gaps must be an array")
        require(
            all(isinstance(gap, str) and gap.strip() for gap in gaps),
            f"{location}: blocking_gaps contains an empty value",
        )
        if admission == "admitted":
            require(not gaps, f"{location}: admitted entry has blocking gaps")
            require(
                instrument.get("voice_posture") != "unverified",
                f"{location}: admitted entry cannot rely on unverified voice scoring",
            )
        else:
            require(gaps, f"{location}: non-admitted entry must explain its blocking gaps")
        if admission == "excluded":
            require(
                instrument.get("voice_posture") == "not-applicable",
                f"{location}: excluded entry must not expose an administration mode",
            )


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


def validate_instrument_session_links() -> None:
    registry_path = ROOT / "instruments/registry.toml"
    try:
        registry = tomllib.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise ValidationError(f"instruments/registry.toml: invalid TOML: {exc}") from exc

    dispositions = {
        item["id"]: item["admission"] for item in registry.get("instruments", [])
    }
    example = load_json("examples/interview-session.example.json")
    orientation_refs = example.get("orientation_refs", [])
    artifact_refs = example.get("artifact_refs", [])
    artifact_locators = {
        item["locator"]
        for item in artifact_refs
        if item.get("kind") == "instrument-result"
    }

    for orientation in orientation_refs:
        registry_id = orientation["registry_id"]
        location = f"interview orientation {registry_id}"
        require(registry_id in dispositions, f"{location}: unknown registry ID")
        require(
            dispositions[registry_id] == orientation["registry_admission"],
            f"{location}: stale admission disposition",
        )
        require(
            orientation["result_locator"] in artifact_locators,
            f"{location}: private result is not represented in artifact_refs",
        )

    if orientation_refs:
        retained = example["consent"]["retained_artifacts"]
        require(
            "instrument-results" in retained,
            "interview orientation: consent does not cover retained instrument results",
        )


def validate_reflection_ui() -> None:
    deploy_paths = ("web/index.html", "web/styles.css", "web/app.js")
    sources: dict[str, str] = {}
    for relative_path in deploy_paths:
        try:
            sources[relative_path] = (ROOT / relative_path).read_text(encoding="utf-8")
        except OSError as exc:
            raise ValidationError(f"{relative_path}: cannot read UI source: {exc}") from exc

    for relative_path, source in sources.items():
        require(
            "http://" not in source and "https://" not in source,
            f"{relative_path}: deployed UI must not reference remote assets or endpoints",
        )

    app_source = sources["web/app.js"]
    forbidden_network_primitives = (
        "fetch(",
        "XMLHttpRequest",
        "WebSocket(",
        "EventSource(",
        "sendBeacon(",
    )
    observed_network_primitives = [
        primitive for primitive in forbidden_network_primitives if primitive in app_source
    ]
    require(
        not observed_network_primitives,
        f"reflection UI: network primitives are forbidden: {observed_network_primitives}",
    )

    html_source = sources["web/index.html"]
    for marker in (
        "Только на этом устройстве",
        "Ответы не покидают браузер",
        "не зашифрованное хранилище",
    ):
        require(marker in html_source, f"reflection UI: missing privacy marker {marker!r}")

    for marker in (
        'id: "personal-strivings"',
        'id: "life-story-interview-ii"',
        'id: "counterportrait-v0"',
        "localStorage",
        "exportWorkbook",
        "resetWorkbook",
        "Вопросы, а не выводы",
    ):
        require(marker in app_source, f"reflection UI: missing contract marker {marker!r}")

    registry_path = ROOT / "instruments/registry.toml"
    try:
        registry = tomllib.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise ValidationError(f"instruments/registry.toml: invalid TOML: {exc}") from exc

    deployed_source = "\n".join(sources.values())
    embedded_non_admitted = [
        item["id"]
        for item in registry.get("instruments", [])
        if item.get("admission") != "admitted" and item["id"] in deployed_source
    ]
    require(
        not embedded_non_admitted,
        f"reflection UI: non-admitted instrument IDs are embedded: {embedded_non_admitted}",
    )


def validate_public_boundary() -> None:
    vault_entries = [
        path
        for path in (ROOT / "vault").rglob("*")
        if path.is_file() and path.relative_to(ROOT).as_posix() != "vault/README.md"
    ]
    require(not vault_entries, f"private vault contains unexpected files: {vault_entries}")

    tracked = subprocess.run(
        ["git", "ls-files", "-z", "--", *PUBLIC_TRACKED_PATHS],
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
        validate_instrument_registry,
        validate_schemas_and_examples,
        validate_instrument_session_links,
        validate_reflection_ui,
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
    print("OK: instrument registry preserves admission, rights, and mode boundaries")
    print("OK: fictional instrument orientation resolves to the current registry")
    print("OK: fictional examples satisfy the public schemas")
    print("OK: local reflection UI has no network or non-admitted instrument surface")
    print("OK: the private vault is empty")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
