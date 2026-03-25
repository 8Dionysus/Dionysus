#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

TOP_LEVEL_KEYS = {
    "registry_version",
    "updated_at",
    "navigation",
    "lifecycle_states",
    "origin_notes",
    "wave_index",
    "seed_index",
}

NAV_KEYS = {
    "canonical_order_source",
    "semantic_source",
    "manifest_validator",
    "registry_validator",
    "validation_entrypoint",
    "registry_contract",
    "planting_report_template",
    "provenance_policy",
    "donor_capture_template",
    "registry_role",
    "archived_root",
    "archived_pack",
    "next_live_seed",
}

SEED_KEYS = {
    "registry_id",
    "label",
    "source_ref",
    "wave",
    "projects",
    "kind",
    "registry_status",
    "parent_seed",
    "repo_homes",
    "first_artifact_hint",
    "notes",
    "provenance",
    "redistribution",
    "transplant",
}

PROVENANCE_KEYS = {
    "origin_mode",
    "donor_repo",
    "donor_ref",
    "donor_license_spdx",
    "donor_paths",
    "provenance_note",
}

REDISTRIBUTION_KEYS = {
    "license_spdx",
    "upstream_license_ref",
    "copy_license_required",
    "notice_required",
    "retain_attribution_required",
    "mark_modifications_required",
    "modified_from_upstream",
    "obligations_note",
}

TRANSPLANT_KEYS = {
    "policy",
    "what_survives",
    "what_stays_behind",
    "non_goals",
}

FRESHNESS_KEYS = {
    "last_revalidated_at",
    "revalidate_after_days",
    "superseded_by",
}


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def ensure_mapping(value: Any, label: str, problems: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        problems.append(f"{label} must be a mapping")
        return {}
    return value


def guess_native_stub(entry: dict[str, Any]) -> dict[str, Any]:
    notes = entry.get("notes") or "TODO: summarize the bounded surviving form"
    return {
        "registry_id": entry.get("registry_id"),
        "provenance": {
            "origin_mode": "native",
            "donor_repo": None,
            "donor_ref": None,
            "donor_license_spdx": None,
            "donor_paths": [],
            "provenance_note": None,
        },
        "redistribution": {
            "license_spdx": None,
            "upstream_license_ref": None,
            "copy_license_required": False,
            "notice_required": False,
            "retain_attribution_required": False,
            "mark_modifications_required": False,
            "modified_from_upstream": False,
            "obligations_note": "TODO: keep this explicit even when there are no third-party obligations.",
        },
        "transplant": {
            "policy": "native",
            "what_survives": [str(notes)],
            "what_stays_behind": ["TODO: name donor doctrine excluded, or say none at this seed surface."],
            "non_goals": ["TODO: copy explicit skipped zones from planting reports or seed notes."],
        },
        "freshness": {
            "last_revalidated_at": None,
            "revalidate_after_days": None,
            "superseded_by": None,
        },
    }


def write_stub(stub_dir: Path, entry: dict[str, Any]) -> None:
    stub_dir.mkdir(parents=True, exist_ok=True)
    registry_id = entry.get("registry_id", "unknown-entry")
    stub_path = stub_dir / f"{registry_id}.v3.stub.yaml"
    stub = guess_native_stub(entry)
    with stub_path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(stub, handle, sort_keys=False, allow_unicode=True)


def report_markdown(
    payload: dict[str, Any],
    navigation_missing: set[str],
    entry_problems: list[tuple[str, list[str]]],
    freshness_missing: list[str],
) -> str:
    lines: list[str] = []
    lines.append("# Seed Registry v3 readiness report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- registry_version: `{payload.get('registry_version')}`")
    lines.append(f"- seed entries inspected: `{len(payload.get('seed_index', []) or [])}`")
    lines.append(f"- missing navigation keys: `{len(navigation_missing)}`")
    lines.append(f"- entries missing required v3 maps or nested keys: `{len(entry_problems)}`")
    lines.append(f"- entries missing optional freshness map: `{len(freshness_missing)}`")
    lines.append("")
    if navigation_missing:
        lines.append("## Missing navigation keys")
        lines.append("")
        for key in sorted(navigation_missing):
            lines.append(f"- `{key}`")
        lines.append("")
    if entry_problems:
        lines.append("## Entries requiring backfill")
        lines.append("")
        for registry_id, problems in entry_problems:
            lines.append(f"### `{registry_id}`")
            for problem in problems:
                lines.append(f"- {problem}")
            lines.append("")
    if freshness_missing:
        lines.append("## Entries without optional freshness map")
        lines.append("")
        for registry_id in freshness_missing:
            lines.append(f"- `{registry_id}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Advisory checker for seed-registry v3 readiness.")
    parser.add_argument("registry", nargs="?", default="seed-registry.yaml", help="Path to seed-registry.yaml")
    parser.add_argument("--emit-stub-dir", help="Write one v3 stub YAML file per seed entry")
    parser.add_argument("--write-report", help="Write a markdown readiness report")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when v3 gaps are found")
    args = parser.parse_args()

    registry_path = Path(args.registry)
    payload = load_yaml(registry_path)

    problems: list[str] = []
    payload = ensure_mapping(payload, str(registry_path), problems)
    if problems:
        for problem in problems:
            print(f"[error] {problem}", file=sys.stderr)
        return 1

    missing_top = TOP_LEVEL_KEYS - set(payload.keys())
    if missing_top:
        for key in sorted(missing_top):
            print(f"[error] missing top-level key: {key}", file=sys.stderr)
        return 1

    navigation = ensure_mapping(payload.get("navigation"), "navigation", problems)
    navigation_missing = NAV_KEYS - set(navigation.keys())

    seed_index = payload.get("seed_index")
    if not isinstance(seed_index, list):
        print("[error] seed_index must be a list", file=sys.stderr)
        return 1

    entry_problems: list[tuple[str, list[str]]] = []
    freshness_missing: list[str] = []

    stub_dir = Path(args.emit_stub_dir) if args.emit_stub_dir else None

    for entry in seed_index:
        registry_id = entry.get("registry_id", "<missing-registry-id>")
        if stub_dir is not None:
            write_stub(stub_dir, entry)

        local_problems: list[str] = []
        missing_seed = SEED_KEYS - set(entry.keys())
        if missing_seed:
            local_problems.extend([f"missing seed key `{key}`" for key in sorted(missing_seed)])

        provenance = entry.get("provenance")
        if isinstance(provenance, dict):
            missing = PROVENANCE_KEYS - set(provenance.keys())
            local_problems.extend([f"missing provenance key `{key}`" for key in sorted(missing)])
        else:
            local_problems.append("missing provenance mapping")

        redistribution = entry.get("redistribution")
        if isinstance(redistribution, dict):
            missing = REDISTRIBUTION_KEYS - set(redistribution.keys())
            local_problems.extend([f"missing redistribution key `{key}`" for key in sorted(missing)])
        else:
            local_problems.append("missing redistribution mapping")

        transplant = entry.get("transplant")
        if isinstance(transplant, dict):
            missing = TRANSPLANT_KEYS - set(transplant.keys())
            local_problems.extend([f"missing transplant key `{key}`" for key in sorted(missing)])
        else:
            local_problems.append("missing transplant mapping")

        freshness = entry.get("freshness")
        if freshness is None:
            freshness_missing.append(registry_id)
        elif isinstance(freshness, dict):
            missing = FRESHNESS_KEYS - set(freshness.keys())
            local_problems.extend([f"missing freshness key `{key}`" for key in sorted(missing)])
        else:
            local_problems.append("freshness must be a mapping when present")

        if local_problems:
            entry_problems.append((registry_id, local_problems))

    print(f"[info] navigation missing keys: {', '.join(sorted(navigation_missing)) or 'none'}")
    print(f"[info] entries with required v3 gaps: {len(entry_problems)} / {len(seed_index)}")
    print(f"[info] entries missing optional freshness: {len(freshness_missing)} / {len(seed_index)}")

    if args.write_report:
        report_path = Path(args.write_report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            report_markdown(payload, navigation_missing, entry_problems, freshness_missing),
            encoding="utf-8",
        )
        print(f"[info] wrote report: {report_path}")

    if args.strict and (navigation_missing or entry_problems):
        print("[error] v3 readiness gaps found", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
