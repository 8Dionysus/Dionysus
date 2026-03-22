#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "first_wave.manifest.json"
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


def validate_ref(ref: str, label: str) -> None:
    if not isinstance(ref, str) or not ref:
        fail(f"{label}: ref must be a non-empty string")
    path_text, _, anchor = ref.partition("#")
    target = ROOT / path_text
    if not target.exists():
        fail(f"{label}: referenced path does not exist: {ref}")
    if anchor and target.suffix.lower() == ".md" and anchor not in anchors_for(target):
        fail(f"{label}: referenced markdown anchor does not exist: {ref}")


def main() -> int:
    try:
        payload = load_json(MANIFEST_PATH)
        if not isinstance(payload, dict):
            fail("manifest must be a JSON object")

        for key in ("canonical_sources", "first_wave_order", "later_pilots", "origin_notes"):
            if key not in payload:
                fail(f"manifest is missing required key '{key}'")

        for index, ref in enumerate(payload["canonical_sources"]):
            validate_ref(ref, f"canonical_sources[{index}]")
        for index, item in enumerate(payload["first_wave_order"]):
            if not isinstance(item, dict):
                fail(f"first_wave_order[{index}] must be an object")
            if "source" not in item:
                fail(f"first_wave_order[{index}] is missing required key 'source'")
            validate_ref(item["source"], f"first_wave_order[{index}].source")
        for index, ref in enumerate(payload["later_pilots"]):
            validate_ref(ref, f"later_pilots[{index}]")
        for index, ref in enumerate(payload["origin_notes"]):
            validate_ref(ref, f"origin_notes[{index}]")
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    print("[ok] validated first_wave.manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
