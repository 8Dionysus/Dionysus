#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDITS_DIR = ROOT / "reports" / "ecosystem-audits"


def run_validation(root: Path) -> list[str]:
    errors: list[str] = []
    audits_dir = root / "reports" / "ecosystem-audits"
    if not audits_dir.exists():
        return errors

    for json_path in sorted(audits_dir.glob("*.checkpoint-note.json")):
        md_path = json_path.with_suffix(".md")
        if not md_path.exists():
            errors.append(f"{json_path.relative_to(root)} is missing matching markdown note {md_path.name}")
            continue
        try:
            payload = json.loads(json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{json_path.relative_to(root)} is not valid JSON: {exc}")
            continue

        if payload.get("schema_version") != 1:
            errors.append(f"{json_path.relative_to(root)} schema_version must equal 1")
        if payload.get("note_type") != "checkpoint_note":
            errors.append(f"{json_path.relative_to(root)} note_type must equal 'checkpoint_note'")
        if payload.get("promotion_target") != "dionysus_note":
            errors.append(f"{json_path.relative_to(root)} promotion_target must equal 'dionysus_note'")
        if not isinstance(payload.get("session_ref"), str) or not payload["session_ref"]:
            errors.append(f"{json_path.relative_to(root)} session_ref must be a non-empty string")
        if not isinstance(payload.get("promotion_reason"), str) or not payload["promotion_reason"]:
            errors.append(f"{json_path.relative_to(root)} promotion_reason must be a non-empty string")
        source_note_ref = payload.get("source_note_ref")
        if not isinstance(source_note_ref, str) or not source_note_ref:
            errors.append(f"{json_path.relative_to(root)} source_note_ref must be a non-empty string")
        elif "checkpoint-note.jsonl" in source_note_ref:
            errors.append(f"{json_path.relative_to(root)} must not point at raw checkpoint-note.jsonl history")

        candidate_clusters = payload.get("candidate_clusters")
        if not isinstance(candidate_clusters, list) or not candidate_clusters:
            errors.append(f"{json_path.relative_to(root)} candidate_clusters must be a non-empty list")

        evidence_refs = payload.get("evidence_refs")
        if not isinstance(evidence_refs, list) or not evidence_refs:
            errors.append(f"{json_path.relative_to(root)} evidence_refs must be a non-empty list")

        markdown = md_path.read_text(encoding="utf-8")
        if "Checkpoint Note Promotion" not in markdown:
            errors.append(f"{md_path.relative_to(root)} must keep the checkpoint-note heading")
        if isinstance(payload.get("session_ref"), str) and payload["session_ref"] not in markdown:
            errors.append(f"{md_path.relative_to(root)} must repeat session_ref '{payload['session_ref']}'")
        if "checkpoint-note.jsonl" in markdown:
            errors.append(f"{md_path.relative_to(root)} must not replay raw checkpoint-note.jsonl history")

    for md_path in sorted(audits_dir.glob("*.checkpoint-note.md")):
        json_path = md_path.with_suffix(".json")
        if not json_path.exists():
            errors.append(f"{md_path.relative_to(root)} is missing matching JSON note {json_path.name}")

    return errors


def main() -> int:
    errors = run_validation(ROOT)
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print("[ok] checkpoint notes validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
