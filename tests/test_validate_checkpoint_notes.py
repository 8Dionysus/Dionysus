from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts import validate_checkpoint_notes


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_checkpoint_note_validator_accepts_lightweight_pair_without_session_harvest() -> None:
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        json_path = root / "reports" / "ecosystem-audits" / "2026-04-07.aoa-sdk.checkpoint-note.json"
        md_path = root / "reports" / "ecosystem-audits" / "2026-04-07.aoa-sdk.checkpoint-note.md"
        write_text(
            json_path,
            json.dumps(
                {
                    "schema_version": 1,
                    "note_type": "checkpoint_note",
                    "session_ref": "session:2026-04-07-aoa-sdk-checkpoint-growth",
                    "promotion_reason": "reviewed checkpoint note promoted from aoa-sdk local session-growth storage",
                    "promotion_target": "dionysus_note",
                    "source_note_ref": "repo:aoa-sdk/.aoa/session-growth/current/aoa-sdk/checkpoint-note.json",
                    "candidate_clusters": [
                        {
                            "candidate_id": "candidate:route:cross-repo-seed-wave-landing",
                            "display_name": "Cross-repo seed-wave landing lane"
                        }
                    ],
                    "evidence_refs": [
                        "repo:aoa-sdk/.aoa/session-growth/current/aoa-sdk/checkpoint-note.json"
                    ],
                    "owner_hints": ["aoa-playbooks"],
                    "next_owner_moves": ["keep full harvest explicit"],
                    "review_status": "reviewed",
                },
                indent=2,
            )
            + "\n",
        )
        write_text(
            md_path,
            "# Checkpoint Note Promotion\n\nSession ref: `session:2026-04-07-aoa-sdk-checkpoint-growth`\n",
        )

        assert validate_checkpoint_notes.run_validation(root) == []


def test_checkpoint_note_validator_rejects_raw_jsonl_reference() -> None:
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        json_path = root / "reports" / "ecosystem-audits" / "2026-04-07.aoa-sdk.checkpoint-note.json"
        md_path = root / "reports" / "ecosystem-audits" / "2026-04-07.aoa-sdk.checkpoint-note.md"
        write_text(
            json_path,
            json.dumps(
                {
                    "schema_version": 1,
                    "note_type": "checkpoint_note",
                    "session_ref": "session:2026-04-07-aoa-sdk-checkpoint-growth",
                    "promotion_reason": "reviewed checkpoint note promoted from aoa-sdk local session-growth storage",
                    "promotion_target": "dionysus_note",
                    "source_note_ref": "repo:aoa-sdk/.aoa/session-growth/current/aoa-sdk/checkpoint-note.jsonl",
                    "candidate_clusters": [{"candidate_id": "candidate:route:test"}],
                    "evidence_refs": ["repo:aoa-sdk/.aoa/session-growth/current/aoa-sdk/checkpoint-note.jsonl"],
                },
                indent=2,
            )
            + "\n",
        )
        write_text(
            md_path,
            "# Checkpoint Note Promotion\n\nSession ref: `session:2026-04-07-aoa-sdk-checkpoint-growth`\n",
        )

        errors = validate_checkpoint_notes.run_validation(root)

    assert any("must not point at raw checkpoint-note.jsonl history" in error for error in errors)


def test_checkpoint_note_validator_requires_matching_pair() -> None:
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        md_path = root / "reports" / "ecosystem-audits" / "2026-04-07.aoa-sdk.checkpoint-note.md"
        write_text(md_path, "# Checkpoint Note Promotion\n\nSession ref: `session:test`\n")

        errors = validate_checkpoint_notes.run_validation(root)

    assert len(errors) == 1
    assert "missing matching JSON note" in errors[0]


def test_checkpoint_note_validator_rejects_raw_jsonl_in_evidence_refs_even_with_clean_source_note_ref() -> None:
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        json_path = root / "reports" / "ecosystem-audits" / "2026-04-07.aoa-sdk.checkpoint-note.json"
        md_path = root / "reports" / "ecosystem-audits" / "2026-04-07.aoa-sdk.checkpoint-note.md"
        write_text(
            json_path,
            json.dumps(
                {
                    "schema_version": 1,
                    "note_type": "checkpoint_note",
                    "session_ref": "session:2026-04-07-aoa-sdk-checkpoint-growth",
                    "promotion_reason": "reviewed checkpoint note promoted from aoa-sdk local session-growth storage",
                    "promotion_target": "dionysus_note",
                    "source_note_ref": "repo:aoa-sdk/.aoa/session-growth/current/aoa-sdk/checkpoint-note.json",
                    "candidate_clusters": [{"candidate_id": "candidate:route:test"}],
                    "evidence_refs": ["repo:aoa-sdk/.aoa/session-growth/current/aoa-sdk/checkpoint-note.jsonl"],
                },
                indent=2,
            )
            + "\n",
        )
        write_text(
            md_path,
            "# Checkpoint Note Promotion\n\nSession ref: `session:2026-04-07-aoa-sdk-checkpoint-growth`\n",
        )

        errors = validate_checkpoint_notes.run_validation(root)

    assert any("evidence_refs must not include raw checkpoint-note.jsonl history" in error for error in errors)
