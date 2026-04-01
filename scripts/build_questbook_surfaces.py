#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print(
        "[error] PyYAML is required for questbook surface builds. Install it with: python -m pip install PyYAML",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc


ROOT = Path(__file__).resolve().parents[1]
QUEST_CATALOG_PATH = Path("generated") / "quest_catalog.min.json"
QUEST_DISPATCH_PATH = Path("generated") / "quest_dispatch.min.json"
QUEST_CATALOG_EXAMPLE_PATH = Path("generated") / "quest_catalog.min.example.json"
QUEST_DISPATCH_EXAMPLE_PATH = Path("generated") / "quest_dispatch.min.example.json"
QUEST_SURFACE_PATHS = (
    QUEST_CATALOG_PATH,
    QUEST_DISPATCH_PATH,
    QUEST_CATALOG_EXAMPLE_PATH,
    QUEST_DISPATCH_EXAMPLE_PATH,
)
QUEST_IDS = (
    "DION-SEED-Q-0001",
    "DION-SEED-Q-0002",
    "DION-SEED-Q-0003",
    "DION-SEED-Q-0004",
)
DISPATCH_ARTIFACTS = {
    "DION-SEED-Q-0001": ["bounded_plan", "work_result", "verification_result"],
    "DION-SEED-Q-0002": ["bounded_plan", "guardrail_check", "verification_result"],
    "DION-SEED-Q-0003": ["bounded_plan", "guardrail_check", "verification_result"],
    "DION-SEED-Q-0004": ["bounded_plan", "work_result"],
}


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Dionysus questbook derived surfaces.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether live and example questbook projections match quests/*.yaml.",
    )
    return parser.parse_args(argv)


def relative_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_yaml_payload(path: Path, root: Path) -> dict[str, Any]:
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing required file: {relative_path(path, root)}") from exc
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML in {relative_path(path, root)}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{relative_path(path, root)} must be a YAML object")
    return payload


def collect_quest_payloads(root: Path) -> dict[str, dict[str, Any]]:
    payloads: dict[str, dict[str, Any]] = {}
    for quest_id in QUEST_IDS:
        quest_path = root / "quests" / f"{quest_id}.yaml"
        payload = read_yaml_payload(quest_path, root)
        if payload.get("schema_version") != "work_quest_v1":
            raise ValueError(f"{quest_id} schema_version must equal 'work_quest_v1'")
        if payload.get("id") != quest_id:
            raise ValueError(f"{relative_path(quest_path, root)} id must equal '{quest_id}'")
        if payload.get("repo") != "Dionysus":
            raise ValueError(f"{quest_id} repo must equal 'Dionysus'")
        if payload.get("public_safe") is not True:
            raise ValueError(f"{quest_id} public_safe must be true")
        payloads[quest_id] = payload
    return payloads


def build_quest_catalog_payload(root: Path = ROOT) -> list[dict[str, Any]]:
    payloads = collect_quest_payloads(root)
    return [
        {
            "id": quest_id,
            "title": payloads[quest_id]["title"],
            "repo": payloads[quest_id]["repo"],
            "theme_ref": payloads[quest_id].get("theme_ref", ""),
            "milestone_ref": payloads[quest_id].get("milestone_ref", ""),
            "state": payloads[quest_id]["state"],
            "band": payloads[quest_id]["band"],
            "kind": payloads[quest_id]["kind"],
            "difficulty": payloads[quest_id]["difficulty"],
            "risk": payloads[quest_id]["risk"],
            "owner_surface": payloads[quest_id]["owner_surface"],
            "source_path": f"quests/{quest_id}.yaml",
            "public_safe": payloads[quest_id]["public_safe"],
        }
        for quest_id in QUEST_IDS
    ]


def build_quest_dispatch_payload(root: Path = ROOT) -> list[dict[str, Any]]:
    payloads = collect_quest_payloads(root)
    return [
        {
            "schema_version": "quest_dispatch_v1",
            "id": quest_id,
            "repo": payloads[quest_id]["repo"],
            "state": payloads[quest_id]["state"],
            "band": payloads[quest_id]["band"],
            "difficulty": payloads[quest_id]["difficulty"],
            "risk": payloads[quest_id]["risk"],
            "control_mode": payloads[quest_id]["control_mode"],
            "delegate_tier": payloads[quest_id]["delegate_tier"],
            "split_required": payloads[quest_id]["split_required"],
            "write_scope": payloads[quest_id]["write_scope"],
            "requires_artifacts": DISPATCH_ARTIFACTS[quest_id],
            "activation_mode": payloads[quest_id]["activation"]["mode"],
            "source_path": f"quests/{quest_id}.yaml",
            "public_safe": payloads[quest_id]["public_safe"],
            "fallback_tier": payloads[quest_id]["fallback_tier"],
            "wrapper_class": payloads[quest_id]["wrapper_class"],
        }
        for quest_id in QUEST_IDS
    ]


def build_questbook_surface_payloads(root: Path = ROOT) -> dict[Path, Any]:
    catalog_payload = build_quest_catalog_payload(root)
    dispatch_payload = build_quest_dispatch_payload(root)
    return {
        QUEST_CATALOG_PATH: catalog_payload,
        QUEST_DISPATCH_PATH: dispatch_payload,
        QUEST_CATALOG_EXAMPLE_PATH: catalog_payload,
        QUEST_DISPATCH_EXAMPLE_PATH: dispatch_payload,
    }


def write_json_file(path: Path, payload: Any, *, compact: bool) -> None:
    if compact:
        encoded = json.dumps(payload, ensure_ascii=True, separators=(",", ":"))
    else:
        encoded = json.dumps(payload, ensure_ascii=True, indent=2)
    path.write_text(encoded + "\n", encoding="utf-8")


def write_questbook_surfaces(root: Path = ROOT) -> tuple[Path, ...]:
    generated_dir = root / "generated"
    generated_dir.mkdir(exist_ok=True)
    payloads = build_questbook_surface_payloads(root)
    outputs: list[Path] = []
    for relative_path in QUEST_SURFACE_PATHS:
        output_path = root / relative_path
        write_json_file(
            output_path,
            payloads[relative_path],
            compact=relative_path in {QUEST_CATALOG_PATH, QUEST_DISPATCH_PATH},
        )
        outputs.append(output_path)
    return tuple(outputs)


def check_questbook_surfaces(root: Path = ROOT) -> list[str]:
    payloads = build_questbook_surface_payloads(root)
    problems: list[str] = []
    for relative in QUEST_SURFACE_PATHS:
        path = root / relative
        if not path.is_file():
            problems.append(f"missing {relative.as_posix()}")
            continue
        expected_text = json.dumps(
            payloads[relative],
            ensure_ascii=True,
            separators=(",", ":") if relative in {QUEST_CATALOG_PATH, QUEST_DISPATCH_PATH} else None,
            indent=None if relative in {QUEST_CATALOG_PATH, QUEST_DISPATCH_PATH} else 2,
        ) + "\n"
        if path.read_text(encoding="utf-8") != expected_text:
            problems.append(f"stale {relative.as_posix()}")
    return problems


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.check:
            problems = check_questbook_surfaces(ROOT)
            if problems:
                print("Questbook surface check failed.")
                for problem in problems:
                    print(f"- {problem}")
                return 1
            print("Questbook surface check passed.")
            return 0
        outputs = write_questbook_surfaces(ROOT)
    except ValueError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    for output in outputs:
        print(f"[ok] wrote {relative_path(output, ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
