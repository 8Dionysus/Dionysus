#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Sequence

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print(
        "[error] PyYAML is required for questbook validation. Install it with: python -m pip install PyYAML",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc

ROOT = Path(__file__).resolve().parents[1]
QUESTBOOK_PATH = Path("QUESTBOOK.md")
QUESTBOOK_INTEGRATION_PATH = Path("docs") / "QUESTBOOK_SEED_GARDEN_INTEGRATION.md"
QUEST_SCHEMA_PATH = Path("schemas") / "quest.schema.json"
QUEST_DISPATCH_SCHEMA_PATH = Path("schemas") / "quest_dispatch.schema.json"
QUEST_CATALOG_EXAMPLE_PATH = Path("generated") / "quest_catalog.min.example.json"
QUEST_DISPATCH_EXAMPLE_PATH = Path("generated") / "quest_dispatch.min.example.json"
QUEST_IDS = (
    "DION-SEED-Q-0001",
    "DION-SEED-Q-0002",
    "DION-SEED-Q-0003",
    "DION-SEED-Q-0004",
)
QUESTBOOK_REQUIRED_TOKENS = (
    "deferred seed-garden obligations that belong to `Dionysus`",
    "repo-local backlog disguised as seed canon",
    "generated/quest_catalog.min.example.json",
    "generated/quest_dispatch.min.example.json",
    "versioned examples for review and validator alignment",
)
QUESTBOOK_INTEGRATION_REQUIRED_TOKENS = (
    "public tracked surface for seed-garden obligations",
    "wave manifests define planting order when a wave exists",
    "named prep-pack notes and maps stage need-driven work before a fresh wave is justified",
    "`seed-registry.yaml` remains the navigation overlay",
    "`README.md` still explains the source-of-truth order",
    "`docs/codex/planting-protocol.md`",
    "`archive/seed_pack_exports/` for derived transport surfaces only",
    "target repositories remain the owners of their own quest meaning",
    "`8Dionysus` remains deferred until a later public-profile refresh contour",
)
FORBIDDEN_TOKENS = ("ATM10-Agent", "aoa-sdk")
CLOSED_QUEST_STATES = {"done", "dropped"}
QUEST_SCHEMA_REQUIRED_FIELDS = (
    "schema_version",
    "id",
    "title",
    "repo",
    "owner_surface",
    "kind",
    "state",
    "band",
    "difficulty",
    "risk",
    "control_mode",
    "delegate_tier",
    "write_scope",
    "activation",
    "anchor_ref",
    "evidence",
    "opened_at",
    "touched_at",
    "public_safe",
)
QUEST_DISPATCH_REQUIRED_FIELDS = (
    "schema_version",
    "id",
    "repo",
    "state",
    "band",
    "difficulty",
    "risk",
    "control_mode",
    "delegate_tier",
    "split_required",
    "write_scope",
    "activation_mode",
    "public_safe",
)
DISPATCH_ARTIFACTS = {
    "DION-SEED-Q-0001": ["bounded_plan", "work_result", "verification_result"],
    "DION-SEED-Q-0002": ["bounded_plan", "guardrail_check", "verification_result"],
    "DION-SEED-Q-0003": ["bounded_plan", "guardrail_check", "verification_result"],
    "DION-SEED-Q-0004": ["bounded_plan", "work_result"],
}


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def display_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_json(path: Path, root: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {display_path(path, root)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {display_path(path, root)}: {exc}")


def read_text(path: Path, root: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required file: {display_path(path, root)}")


def read_yaml(path: Path, root: Path) -> object:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {display_path(path, root)}")
    except yaml.YAMLError as exc:
        fail(f"invalid YAML in {display_path(path, root)}: {exc}")


def validate_schema_envelope(
    payload: object,
    *,
    title: str,
    schema_version: str,
    required_fields: Sequence[str],
    label: str,
) -> None:
    if not isinstance(payload, dict):
        fail(f"{label} must be a JSON object")
    if payload.get("title") != title:
        fail(f"{label} title must equal '{title}'")
    if payload.get("type") != "object":
        fail(f"{label} type must equal 'object'")
    if payload.get("additionalProperties") is not False:
        fail(f"{label} must set additionalProperties to false")
    required = payload.get("required")
    if required != list(required_fields):
        fail(f"{label} required fields must stay aligned with the local quest contract")
    properties = payload.get("properties")
    if not isinstance(properties, dict):
        fail(f"{label} properties must be an object")
    version_payload = properties.get("schema_version")
    if not isinstance(version_payload, dict) or version_payload.get("const") != schema_version:
        fail(f"{label} schema_version.const must equal '{schema_version}'")


def build_expected_quest_catalog_entry(quest_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": quest_id,
        "title": payload["title"],
        "repo": payload["repo"],
        "theme_ref": payload.get("theme_ref", ""),
        "milestone_ref": payload.get("milestone_ref", ""),
        "state": payload["state"],
        "band": payload["band"],
        "kind": payload["kind"],
        "difficulty": payload["difficulty"],
        "risk": payload["risk"],
        "owner_surface": payload["owner_surface"],
        "source_path": f"quests/{quest_id}.yaml",
        "public_safe": payload["public_safe"],
    }


def build_expected_quest_dispatch_entry(quest_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    activation = payload.get("activation")
    if not isinstance(activation, dict):
        fail(f"{quest_id} activation must be an object")

    return {
        "schema_version": "quest_dispatch_v1",
        "id": quest_id,
        "repo": payload["repo"],
        "state": payload["state"],
        "band": payload["band"],
        "difficulty": payload["difficulty"],
        "risk": payload["risk"],
        "control_mode": payload["control_mode"],
        "delegate_tier": payload["delegate_tier"],
        "split_required": payload["split_required"],
        "write_scope": payload["write_scope"],
        "requires_artifacts": DISPATCH_ARTIFACTS[quest_id],
        "activation_mode": activation["mode"],
        "source_path": f"quests/{quest_id}.yaml",
        "public_safe": payload["public_safe"],
        "fallback_tier": payload["fallback_tier"],
        "wrapper_class": payload["wrapper_class"],
    }


def validate_reference_path(path_text: str, *, label: str, root: Path) -> None:
    if not isinstance(path_text, str) or not path_text:
        fail(f"{label} must be a non-empty string")
    target = root / path_text.rstrip("/")
    if not target.exists():
        fail(f"{label} must point to an existing local path: {path_text}")


def validate_questbook_surface(root: Path = ROOT) -> None:
    required_paths = (
        QUESTBOOK_PATH,
        QUESTBOOK_INTEGRATION_PATH,
        QUEST_SCHEMA_PATH,
        QUEST_DISPATCH_SCHEMA_PATH,
        QUEST_CATALOG_EXAMPLE_PATH,
        QUEST_DISPATCH_EXAMPLE_PATH,
    ) + tuple(Path("quests") / f"{quest_id}.yaml" for quest_id in QUEST_IDS)

    for relative_path in required_paths:
        path = root / relative_path
        if not path.exists():
            fail(f"missing required file: {relative_path.as_posix()}")

    questbook_text = read_text(root / QUESTBOOK_PATH, root)
    for token in QUESTBOOK_REQUIRED_TOKENS:
        if token not in questbook_text:
            fail(f"QUESTBOOK.md must contain '{token}'")
    for token in FORBIDDEN_TOKENS:
        if token in questbook_text:
            fail(f"QUESTBOOK.md must not mention '{token}'")

    integration_text = read_text(root / QUESTBOOK_INTEGRATION_PATH, root)
    for token in QUESTBOOK_INTEGRATION_REQUIRED_TOKENS:
        if token not in integration_text:
            fail(f"{QUESTBOOK_INTEGRATION_PATH.as_posix()} must contain '{token}'")
    for token in FORBIDDEN_TOKENS:
        if token in integration_text:
            fail(f"{QUESTBOOK_INTEGRATION_PATH.as_posix()} must not mention '{token}'")

    quest_schema_payload = read_json(root / QUEST_SCHEMA_PATH, root)
    validate_schema_envelope(
        quest_schema_payload,
        title="Dionysus work_quest_v1",
        schema_version="work_quest_v1",
        required_fields=QUEST_SCHEMA_REQUIRED_FIELDS,
        label=QUEST_SCHEMA_PATH.as_posix(),
    )

    dispatch_schema_payload = read_json(root / QUEST_DISPATCH_SCHEMA_PATH, root)
    validate_schema_envelope(
        dispatch_schema_payload,
        title="Dionysus quest_dispatch_v1",
        schema_version="quest_dispatch_v1",
        required_fields=QUEST_DISPATCH_REQUIRED_FIELDS,
        label=QUEST_DISPATCH_SCHEMA_PATH.as_posix(),
    )

    expected_catalog = []
    expected_dispatch = []
    active_quest_ids: list[str] = []
    closed_quest_ids: list[str] = []
    for quest_id in QUEST_IDS:
        quest_path = root / "quests" / f"{quest_id}.yaml"
        quest_payload = read_yaml(quest_path, root)
        if not isinstance(quest_payload, dict):
            fail(f"{quest_path.relative_to(root).as_posix()} must be a YAML object")
        if quest_payload.get("schema_version") != "work_quest_v1":
            fail(f"{quest_id} schema_version must equal 'work_quest_v1'")
        if quest_payload.get("id") != quest_id:
            fail(f"{quest_path.relative_to(root).as_posix()} id must equal '{quest_id}'")
        if quest_payload.get("repo") != "Dionysus":
            fail(f"{quest_id} repo must equal 'Dionysus'")
        if quest_payload.get("public_safe") is not True:
            fail(f"{quest_id} public_safe must be true")
        if quest_payload.get("state") in CLOSED_QUEST_STATES:
            closed_quest_ids.append(quest_id)
        else:
            active_quest_ids.append(quest_id)

        notes = quest_payload.get("notes", "")
        if not isinstance(notes, str):
            fail(f"{quest_id} notes must be a string")
        for token in FORBIDDEN_TOKENS:
            if token in notes:
                fail(f"{quest_id} notes must stay in scope for the current contour")

        anchor_ref = quest_payload.get("anchor_ref")
        if not isinstance(anchor_ref, dict):
            fail(f"{quest_id} anchor_ref must be an object")
        validate_reference_path(anchor_ref.get("ref"), label=f"{quest_id} anchor_ref.ref", root=root)

        activation = quest_payload.get("activation")
        if not isinstance(activation, dict):
            fail(f"{quest_id} activation must be an object")
        activation_ref = activation.get("ref")
        if activation_ref is not None:
            validate_reference_path(activation_ref, label=f"{quest_id} activation.ref", root=root)

        expected_catalog.append(build_expected_quest_catalog_entry(quest_id, quest_payload))
        expected_dispatch.append(build_expected_quest_dispatch_entry(quest_id, quest_payload))

    for quest_id in active_quest_ids:
        if quest_id not in questbook_text:
            fail(f"QUESTBOOK.md must reference active quest id '{quest_id}'")
    for quest_id in closed_quest_ids:
        if quest_id in questbook_text:
            fail(f"QUESTBOOK.md must not list closed quest id '{quest_id}'")

    catalog_payload = read_json(root / QUEST_CATALOG_EXAMPLE_PATH, root)
    if catalog_payload != expected_catalog:
        fail("generated/quest_catalog.min.example.json must stay aligned with quests/*.yaml")

    dispatch_payload = read_json(root / QUEST_DISPATCH_EXAMPLE_PATH, root)
    if dispatch_payload != expected_dispatch:
        fail("generated/quest_dispatch.min.example.json must stay aligned with quests/*.yaml")


def run_validation(root: Path = ROOT) -> list[str]:
    try:
        validate_questbook_surface(root)
    except ValidationError as exc:
        return [str(exc)]
    return []


def main() -> int:
    errors = run_validation(ROOT)
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print("[ok] validated Dionysus questbook surface")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
