#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_SPECS = {
    "first_wave.manifest.json": {
        "order_key": "first_wave_order",
        "tail_keys": ("later_pilots", "origin_notes"),
    },
    "second_wave.manifest.json": {
        "order_key": "second_wave_order",
        "tail_keys": ("deferred_pilots", "held_later"),
    },
    "third_wave.manifest.json": {
        "order_key": "third_wave_order",
        "tail_keys": ("deferred_pilots", "held_later"),
    },
    "fourth_wave.manifest.json": {
        "order_key": "fourth_wave_order",
        "tail_keys": ("held_later",),
    },
    "fifth_wave.manifest.json": {
        "order_key": "fifth_wave_order",
        "tail_keys": ("held_later",),
    },
    "sixth_wave.manifest.json": {
        "order_key": "sixth_wave_order",
        "tail_keys": ("held_later",),
    },
    "seventh_wave.manifest.json": {
        "order_key": "seventh_wave_order",
        "tail_keys": ("held_later",),
    },
}
MANIFEST_PATHS = [ROOT / name for name in MANIFEST_SPECS]
MARKDOWN_HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
HTML_ID = re.compile(r"<a\s+id=\"([^\"]+)\"\s*>\s*</a>", re.IGNORECASE)


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing file: {path.relative_to(ROOT).as_posix()}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path.relative_to(ROOT).as_posix()}: {exc}") from exc


def markdown_anchor(text: str) -> str:
    anchor = text.strip().lower()
    anchor = re.sub(r"[^\w\s-]", "", anchor)
    anchor = re.sub(r"\s+", "-", anchor)
    anchor = re.sub(r"-+", "-", anchor)
    return anchor.strip("-")


def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        html_match = HTML_ID.search(line)
        if html_match:
            anchors.add(html_match.group(1))
        match = MARKDOWN_HEADING.match(line)
        if not match:
            continue
        base = markdown_anchor(match.group(2))
        if not base:
            continue
        suffix = seen.get(base, 0)
        seen[base] = suffix + 1
        anchors.add(base if suffix == 0 else f"{base}-{suffix}")
    return anchors


def validate_ref(ref: str, label: str, require_anchor: bool = False) -> None:
    if not isinstance(ref, str) or not ref:
        fail(f"{label}: ref must be a non-empty string")
    path_text, _, anchor = ref.partition("#")
    target = ROOT / path_text
    if not target.exists():
        fail(f"{label}: referenced path does not exist: {ref}")
    if require_anchor and target.suffix.lower() == ".md" and not anchor:
        fail(f"{label}: referenced markdown ref must include an explicit anchor: {ref}")
    if anchor and target.suffix.lower() == ".md" and anchor not in anchors_for(target):
        fail(f"{label}: referenced markdown anchor does not exist: {ref}")


def seed_bundle_ref_requires_anchor(ref: object) -> bool:
    return isinstance(ref, str) and (
        ref.startswith("seed_bundle/seeds_")
        or ref.startswith("seed_templates/")
        or ref.startswith("seed_branches/")
        or ref.startswith("0ld/seed_bundle/seeds_")
        or ref.startswith("0ld/seed_templates/")
        or ref.startswith("0ld/seed_branches/")
    )


def validate_manifest(manifest_path: Path) -> None:
    payload = load_json(manifest_path)
    if not isinstance(payload, dict):
        fail(f"{manifest_path.name}: manifest must be a JSON object")

    spec = MANIFEST_SPECS.get(manifest_path.name)
    if spec is None:
        fail(f"unsupported manifest surface: {manifest_path.name}")
    order_key = spec["order_key"]
    tail_keys = spec["tail_keys"]

    for key in ("canonical_sources", order_key, *tail_keys):
        if key not in payload:
            fail(f"{manifest_path.name}: manifest is missing required key '{key}'")

    for index, ref in enumerate(payload["canonical_sources"]):
        validate_ref(
            ref,
            f"{manifest_path.name}: canonical_sources[{index}]",
            require_anchor=seed_bundle_ref_requires_anchor(ref),
        )
    for index, item in enumerate(payload[order_key]):
        if not isinstance(item, dict):
            fail(f"{manifest_path.name}: {order_key}[{index}] must be an object")
        if "source" not in item:
            fail(f"{manifest_path.name}: {order_key}[{index}] is missing required key 'source'")
        source_ref = item["source"]
        require_anchor = seed_bundle_ref_requires_anchor(source_ref)
        validate_ref(source_ref, f"{manifest_path.name}: {order_key}[{index}].source", require_anchor=require_anchor)
    for tail_key in tail_keys:
        for index, ref in enumerate(payload[tail_key]):
            require_anchor = seed_bundle_ref_requires_anchor(ref)
            validate_ref(ref, f"{manifest_path.name}: {tail_key}[{index}]", require_anchor=require_anchor)


def main() -> int:
    try:
        for manifest_path in MANIFEST_PATHS:
            validate_manifest(manifest_path)
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    for manifest_path in MANIFEST_PATHS:
        print(f"[ok] validated {manifest_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
