from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "validate_seed_note_lifecycle.py"
SPEC = importlib.util.spec_from_file_location("validate_seed_note_lifecycle", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"unable to load validator module from {MODULE_PATH}")
validate_seed_note_lifecycle = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_seed_note_lifecycle)


def copy_text_file(root: Path, relative_path: str) -> None:
    source = REPO_ROOT / relative_path
    destination = root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def test_via_negativa_pack_companion_map_stays_in_landed_lineage_state() -> None:
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        note_path = "seed_staging/future/seed_aoa_antifragility_wave_4_5_via_negativa_pack.md"
        map_path = "seed_staging/future/seed_aoa_antifragility_wave_4_5_via_negativa_pack.map.yaml"
        copy_text_file(root, note_path)
        copy_text_file(root, map_path)

        with patch.object(
            validate_seed_note_lifecycle,
            "EXPECTED_NOTES",
            {
                note_path: {
                    "kind": "prep-pack-note",
                    "lifecycle_status": "landed_upstream_retained_for_lineage",
                }
            },
        ):
            with patch.object(
                validate_seed_note_lifecycle,
                "EXPECTED_COMPANION_MAPS",
                {
                    note_path: {
                        "path": map_path,
                        "updated_at": "2026-04-08",
                        "required_lineage_tokens": (
                            "owner-repo landings were verified",
                            "lineage-only replay",
                        ),
                        "forbidden_lineage_tokens": (
                            "no via-negativa owner-repo landings are yet verified in the current workspace",
                        ),
                    }
                },
            ):
                assert validate_seed_note_lifecycle.run_validation(root) == []


def test_via_negativa_pack_companion_map_rejects_stale_premerge_signal() -> None:
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        note_path = "seed_staging/future/seed_aoa_antifragility_wave_4_5_via_negativa_pack.md"
        map_path = "seed_staging/future/seed_aoa_antifragility_wave_4_5_via_negativa_pack.map.yaml"
        copy_text_file(root, note_path)
        copy_text_file(root, map_path)
        target_map = root / map_path
        target_map.write_text(
            target_map.read_text(encoding="utf-8").replace(
                "via-negativa owner-repo landings were verified in the 2026-04-08 workspace and this pack now survives as lineage-only replay rather than as live staging",
                "no via-negativa owner-repo landings are yet verified in the current workspace",
                1,
            ),
            encoding="utf-8",
        )

        with patch.object(
            validate_seed_note_lifecycle,
            "EXPECTED_NOTES",
            {
                note_path: {
                    "kind": "prep-pack-note",
                    "lifecycle_status": "landed_upstream_retained_for_lineage",
                }
            },
        ):
            with patch.object(
                validate_seed_note_lifecycle,
                "EXPECTED_COMPANION_MAPS",
                {
                    note_path: {
                        "path": map_path,
                        "updated_at": "2026-04-08",
                        "required_lineage_tokens": (
                            "owner-repo landings were verified",
                            "lineage-only replay",
                        ),
                        "forbidden_lineage_tokens": (
                            "no via-negativa owner-repo landings are yet verified in the current workspace",
                        ),
                    }
                },
            ):
                errors = validate_seed_note_lifecycle.run_validation(root)

    assert len(errors) == 1
    assert "must mention" in errors[0] or "must not mention" in errors[0]
