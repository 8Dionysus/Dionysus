#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print(
        "[error] PyYAML is required for prep-pack validation. Install it with: python -m pip install PyYAML",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "seed-registry.yaml"
ALLOWED_PRIORITY = {"now", "next", "later", "hold"}
ALLOWED_PRIORITY_BANDS = {"now", "next", "later", "hold"}
ALLOWED_PLANTING_READINESS = {"ready", "needs_adaptation", "blocked"}

EXPECTED_PACKS = {
    "seed_questbook_foundation_pack.md": {
        "seed_id": "seed.questbook.foundation-pack.v0",
        "priority": "now",
        "priority_band": "now",
        "planting_readiness": "ready",
        "source_bundle": "archive/seed_pack_exports/questbook_first_wave_seed.zip",
        "targets": [
            "Agents-of-Abyss",
            "aoa-agents",
            "aoa-routing",
            "aoa-playbooks",
            "aoa-memo",
        ],
        "dependencies": [],
    },
    "seed_questbook_source_proof_pack.md": {
        "seed_id": "seed.questbook.source-proof-pack.v0",
        "priority": "next",
        "priority_band": "next",
        "planting_readiness": "ready",
        "source_bundle": "archive/seed_pack_exports/questbook_second_wave_seed.zip",
        "targets": [
            "aoa-techniques",
            "aoa-skills",
            "aoa-evals",
        ],
        "dependencies": [
            "seed.questbook.foundation-pack.v0",
        ],
    },
    "seed_questbook_boundary_runtime_pack.md": {
        "seed_id": "seed.questbook.boundary-runtime-pack.v0",
        "priority": "later",
        "priority_band": "later",
        "planting_readiness": "needs_adaptation",
        "source_bundle": "archive/seed_pack_exports/questbook_second_wave_seed.zip",
        "targets": [
            "aoa-kag",
            "Tree-of-Sophia",
            "abyss-stack",
        ],
        "dependencies": [
            "seed.questbook.source-proof-pack.v0",
        ],
    },
    "seed_questbook_seedgarden_profile_pack.md": {
        "seed_id": "seed.questbook.seedgarden-profile-pack.v0",
        "priority": "later",
        "priority_band": "later",
        "planting_readiness": "needs_adaptation",
        "source_bundle": "archive/seed_pack_exports/questbook_second_wave_seed.zip",
        "targets": [
            "Dionysus",
            "8Dionysus",
        ],
        "dependencies": [
            "seed.questbook.foundation-pack.v0",
            "seed.questbook.source-proof-pack.v0",
            "seed.questbook.boundary-runtime-pack.v0",
        ],
    },
}

NOTE_REQUIRED_KEYS = (
    "seed_id",
    "title",
    "profile_anchor",
    "projects",
    "kind",
    "status",
    "priority",
    "parent_seed",
    "tags",
)

MAP_REQUIRED_KEYS = (
    "map_version",
    "updated_at",
    "seed_note",
    "status",
    "source_bundle",
    "selection_policy",
    "navigation_constraints",
    "targets",
    "scope_exclusions",
)


class ValidationError(RuntimeError):
    """Raised when prep-pack validation fails."""


def fail(message: str) -> None:
    raise ValidationError(message)


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing file: {path.relative_to(ROOT).as_posix()}") from exc
    except yaml.YAMLError as exc:
        raise ValidationError(f"invalid YAML in {path.relative_to(ROOT).as_posix()}: {exc}") from exc


def require_mapping(value: object, label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or not value:
        fail(f"{label}: must be a non-empty mapping")
    return value


def require_nonempty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label}: must be a non-empty string")
    return value


def require_string_list(value: object, label: str, *, non_empty: bool = True) -> list[str]:
    if not isinstance(value, list):
        fail(f"{label}: must be a list")
    if non_empty and not value:
        fail(f"{label}: must not be empty")
    result: list[str] = []
    for index, item in enumerate(value):
        result.append(require_nonempty_string(item, f"{label}[{index}]"))
    return result


def require_bool(value: object, label: str) -> bool:
    if not isinstance(value, bool):
        fail(f"{label}: must be a boolean")
    return value


def load_note_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    frontmatter, separator, _ = text.partition("\n\n")
    if not separator:
        fail(f"{path.name}: missing frontmatter/body separator")
    data = yaml.safe_load(frontmatter)
    if not isinstance(data, dict) or not data:
        fail(f"{path.name}: frontmatter must be a non-empty mapping")
    return data


def main() -> int:
    registry = require_mapping(load_yaml(REGISTRY_PATH), "seed-registry.yaml")
    navigation = require_mapping(registry["navigation"], "seed-registry.yaml.navigation")
    next_live_seed = require_nonempty_string(
        navigation["next_live_seed"], "seed-registry.yaml.navigation.next_live_seed"
    )
    origin_notes = require_string_list(registry["origin_notes"], "seed-registry.yaml.origin_notes")
    seed_index = registry["seed_index"]
    if not isinstance(seed_index, list):
        fail("seed-registry.yaml.seed_index: must be a list")

    expected_names = set(EXPECTED_PACKS)
    found_names = {path.name for path in ROOT.glob("seed_questbook_*_pack.md")}
    if found_names != expected_names:
        missing = sorted(expected_names - found_names)
        extra = sorted(found_names - expected_names)
        if missing:
            fail(f"missing questbook prep-pack notes: {', '.join(missing)}")
        fail(f"unexpected questbook prep-pack notes: {', '.join(extra)}")

    for source_ref in (
        entry.get("source_ref")
        for entry in seed_index
        if isinstance(entry, dict)
    ):
        if not isinstance(source_ref, str):
            continue
        for note_name in expected_names:
            if source_ref.startswith(note_name):
                fail(f"seed-registry.yaml.seed_index must not register questbook prep-pack note '{note_name}' yet")

    for note_name, expected in EXPECTED_PACKS.items():
        note_path = ROOT / note_name
        map_path = note_path.with_suffix(".map.yaml")
        if not map_path.exists():
            fail(f"{note_name}: missing matching map file '{map_path.name}'")
        if note_name not in origin_notes:
            fail(f"{note_name}: must be listed in seed-registry.yaml origin_notes")

        frontmatter = require_mapping(load_note_frontmatter(note_path), note_name)
        for key in NOTE_REQUIRED_KEYS:
            if key not in frontmatter:
                fail(f"{note_name}: missing frontmatter key '{key}'")
        if require_nonempty_string(frontmatter["seed_id"], f"{note_name}.seed_id") != expected["seed_id"]:
            fail(f"{note_name}.seed_id must be '{expected['seed_id']}'")
        priority = require_nonempty_string(frontmatter["priority"], f"{note_name}.priority")
        if priority not in ALLOWED_PRIORITY:
            fail(f"{note_name}.priority must be one of {sorted(ALLOWED_PRIORITY)}")
        if priority != expected["priority"]:
            fail(f"{note_name}.priority must be '{expected['priority']}'")
        require_string_list(frontmatter["projects"], f"{note_name}.projects")
        require_string_list(frontmatter["tags"], f"{note_name}.tags")

        mapping = require_mapping(load_yaml(map_path), map_path.name)
        for key in MAP_REQUIRED_KEYS:
            if key not in mapping:
                fail(f"{map_path.name}: missing required key '{key}'")
        if require_nonempty_string(mapping["seed_note"], f"{map_path.name}.seed_note") != note_name:
            fail(f"{map_path.name}.seed_note must be '{note_name}'")

        source_bundle = require_mapping(mapping["source_bundle"], f"{map_path.name}.source_bundle")
        source_bundle_path = require_nonempty_string(
            source_bundle["path"], f"{map_path.name}.source_bundle.path"
        )
        if source_bundle_path != expected["source_bundle"]:
            fail(f"{map_path.name}.source_bundle.path must be '{expected['source_bundle']}'")
        if not source_bundle_path.startswith("archive/seed_pack_exports/"):
            fail(f"{map_path.name}.source_bundle.path must stay under archive/seed_pack_exports/")
        if not (ROOT / source_bundle_path).exists():
            fail(f"{map_path.name}.source_bundle.path does not exist: {source_bundle_path}")

        selection = require_mapping(mapping["selection_policy"], f"{map_path.name}.selection_policy")
        require_bool(selection["fixed_order_required"], f"{map_path.name}.selection_policy.fixed_order_required")
        default_order = require_string_list(
            selection["default_order"], f"{map_path.name}.selection_policy.default_order"
        )
        if default_order != expected["targets"]:
            fail(
                f"{map_path.name}.selection_policy.default_order must be "
                f"{expected['targets']}"
            )
        priority_band = require_nonempty_string(
            selection["priority_band"], f"{map_path.name}.selection_policy.priority_band"
        )
        if priority_band not in ALLOWED_PRIORITY_BANDS:
            fail(f"{map_path.name}.selection_policy.priority_band must be one of {sorted(ALLOWED_PRIORITY_BANDS)}")
        if priority_band != expected["priority_band"]:
            fail(f"{map_path.name}.selection_policy.priority_band must be '{expected['priority_band']}'")
        planting_readiness = require_nonempty_string(
            selection["planting_readiness"], f"{map_path.name}.selection_policy.planting_readiness"
        )
        if planting_readiness not in ALLOWED_PLANTING_READINESS:
            fail(
                f"{map_path.name}.selection_policy.planting_readiness must be one of "
                f"{sorted(ALLOWED_PLANTING_READINESS)}"
            )
        if planting_readiness != expected["planting_readiness"]:
            fail(
                f"{map_path.name}.selection_policy.planting_readiness must be "
                f"'{expected['planting_readiness']}'"
            )
        require_string_list(selection["why_now"], f"{map_path.name}.selection_policy.why_now")
        dependencies = require_string_list(
            selection["dependencies"], f"{map_path.name}.selection_policy.dependencies", non_empty=False
        )
        if dependencies != expected["dependencies"]:
            fail(f"{map_path.name}.selection_policy.dependencies must be {expected['dependencies']}")

        navigation_constraints = require_mapping(
            mapping["navigation_constraints"], f"{map_path.name}.navigation_constraints"
        )
        if (
            require_nonempty_string(
                navigation_constraints["keep_next_live_seed"],
                f"{map_path.name}.navigation_constraints.keep_next_live_seed",
            )
            != next_live_seed
        ):
            fail(f"{map_path.name}: keep_next_live_seed must match seed-registry navigation.next_live_seed")

        scope_exclusions = require_string_list(mapping["scope_exclusions"], f"{map_path.name}.scope_exclusions")
        for excluded in ("ATM10-Agent", "aoa-sdk"):
            if excluded not in scope_exclusions:
                fail(f"{map_path.name}.scope_exclusions must include '{excluded}'")

        targets = mapping["targets"]
        if not isinstance(targets, list) or not targets:
            fail(f"{map_path.name}.targets must be a non-empty list")
        target_repos: list[str] = []
        for index, target in enumerate(targets):
            target_map = require_mapping(target, f"{map_path.name}.targets[{index}]")
            repo = require_nonempty_string(target_map["repo"], f"{map_path.name}.targets[{index}].repo")
            files = require_string_list(target_map["files"], f"{map_path.name}.targets[{index}].files")
            target_repos.append(repo)
            if repo in {"ATM10-Agent", "aoa-sdk"}:
                fail(f"{map_path.name}.targets[{index}].repo must not include '{repo}' in the current rollout")
            if note_name == "seed_questbook_boundary_runtime_pack.md" and repo == "abyss-stack":
                for file_ref in files:
                    if not file_ref.startswith("Configs/"):
                        fail(
                            f"{map_path.name}: abyss-stack target files must be adapted to Configs/... paths, "
                            f"got '{file_ref}'"
                        )
        if target_repos != expected["targets"]:
            fail(f"{map_path.name}.targets repo order must be {expected['targets']}")

    print("[ok] validated named questbook prep packs")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
