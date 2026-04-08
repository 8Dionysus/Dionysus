from __future__ import annotations

import shutil
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts import validate_questbook_surface


REPO_ROOT = Path(__file__).resolve().parents[1]
SURFACE_PATHS = (
    "README.md",
    "QUESTBOOK.md",
    "docs/QUESTBOOK_SEED_GARDEN_INTEGRATION.md",
    "docs/codex",
    "schemas",
    "generated",
    "quests",
    "archive/seed_pack_exports",
    "seed-registry.yaml",
    "seed_staging/future/seed_tos_graph_curation_pack.md",
    "seed_staging/future/seed_tos_graph_curation_pack.map.yaml",
    "seed_staging/rpg/seed_rpg_first_wave_pack.md",
    "seed_staging/rpg/seed_rpg_first_wave_pack.map.yaml",
    "seed_staging/rpg/seed_rpg_second_wave_pack.md",
    "seed_staging/rpg/seed_rpg_second_wave_pack.map.yaml",
    "seed_staging/rpg/seed_rpg_architecture_rfc_pack.md",
    "seed_staging/rpg/seed_rpg_architecture_rfc_pack.map.yaml",
    "seed_staging/rpg/seed_rpg_bridge_wave_pack.md",
    "seed_staging/rpg/seed_rpg_bridge_wave_pack.map.yaml",
    "seed_staging/rpg/seed_rpg_sdk_addendum_pack.md",
    "seed_staging/rpg/seed_rpg_sdk_addendum_pack.map.yaml",
    "seed_staging/rpg/seed_rpg_runtime_projection_pack.md",
    "seed_staging/rpg/seed_rpg_runtime_projection_pack.map.yaml",
)


def copy_surface(target_root: Path) -> None:
    for relative_path in SURFACE_PATHS:
        source = REPO_ROOT / relative_path
        destination = target_root / relative_path
        if source.is_dir():
            shutil.copytree(source, destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)


class ValidateQuestbookSurfaceTests(unittest.TestCase):
    def test_repo_surface_validates(self) -> None:
        self.assertEqual([], validate_questbook_surface.run_validation(REPO_ROOT))

    def test_missing_tracked_id_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            questbook_path = root / "QUESTBOOK.md"
            questbook_path.write_text(
                questbook_path.read_text(encoding="utf-8").replace(
                    "DION-SEED-Q-0004", "DION-SEED-Q-9999", 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("QUESTBOOK.md must reference active quest id 'DION-SEED-Q-0004'", errors[0])

    def test_missing_rpg_tracked_id_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            questbook_path = root / "QUESTBOOK.md"
            questbook_path.write_text(
                questbook_path.read_text(encoding="utf-8").replace(
                    "DION-SEED-Q-0005", "DION-SEED-Q-9998", 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("QUESTBOOK.md must reference active quest id 'DION-SEED-Q-0005'", errors[0])

    def test_missing_second_wave_rpg_tracked_id_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            questbook_path = root / "QUESTBOOK.md"
            questbook_path.write_text(
                questbook_path.read_text(encoding="utf-8").replace(
                    "DION-SEED-Q-0006", "DION-SEED-Q-9997", 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("QUESTBOOK.md must reference active quest id 'DION-SEED-Q-0006'", errors[0])

    def test_missing_architecture_rpg_tracked_id_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            questbook_path = root / "QUESTBOOK.md"
            questbook_path.write_text(
                questbook_path.read_text(encoding="utf-8").replace(
                    "DION-SEED-Q-0007", "DION-SEED-Q-9996", 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("QUESTBOOK.md must reference active quest id 'DION-SEED-Q-0007'", errors[0])

    def test_missing_bridge_wave_rpg_tracked_id_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            questbook_path = root / "QUESTBOOK.md"
            questbook_path.write_text(
                questbook_path.read_text(encoding="utf-8").replace(
                    "DION-SEED-Q-0008", "DION-SEED-Q-9995", 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("QUESTBOOK.md must reference active quest id 'DION-SEED-Q-0008'", errors[0])

    def test_missing_runtime_projection_rpg_tracked_id_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            questbook_path = root / "QUESTBOOK.md"
            questbook_path.write_text(
                questbook_path.read_text(encoding="utf-8").replace(
                    "DION-SEED-Q-0009", "DION-SEED-Q-9994", 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("QUESTBOOK.md must reference active quest id 'DION-SEED-Q-0009'", errors[0])

    def test_missing_sdk_addendum_rpg_tracked_id_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            questbook_path = root / "QUESTBOOK.md"
            questbook_path.write_text(
                questbook_path.read_text(encoding="utf-8").replace(
                    "DION-SEED-Q-0010", "DION-SEED-Q-9993", 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("QUESTBOOK.md must reference active quest id 'DION-SEED-Q-0010'", errors[0])

    def test_closed_tracked_id_in_questbook_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            questbook_path = root / "QUESTBOOK.md"
            questbook_path.write_text(
                questbook_path.read_text(encoding="utf-8").replace(
                    "- `DION-SEED-Q-0007` — stage the RPG architecture RFC pack as a named seed-garden prep pack",
                    "- `DION-SEED-Q-0007` — stage the RPG architecture RFC pack as a named seed-garden prep pack\n- `DION-SEED-Q-0001` — closed rollout should not stay listed",
                    1,
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("QUESTBOOK.md must not list closed quest id 'DION-SEED-Q-0001'", errors[0])

    def test_wrong_repo_in_quest_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            quest_path = root / "quests" / "DION-SEED-Q-0001.yaml"
            quest_path.write_text(
                quest_path.read_text(encoding="utf-8").replace(
                    "repo: Dionysus", "repo: 8Dionysus", 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("DION-SEED-Q-0001 repo must equal 'Dionysus'", errors[0])

    def test_missing_live_catalog_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            (root / "generated" / "quest_catalog.min.json").unlink()

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("missing required file: generated/quest_catalog.min.json", errors[0])

    def test_live_dispatch_drift_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            dispatch_path = root / "generated" / "quest_dispatch.min.json"
            dispatch_path.write_text(
                dispatch_path.read_text(encoding="utf-8").replace(
                    '"state":"done"', '"state":"captured"', 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("generated/quest_dispatch.min.json must stay aligned with quests/*.yaml", errors[0])

    def test_catalog_fixture_live_drift_fails_validation(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "generated" / "quest_catalog.min.example.json"
            example_path.write_text(
                example_path.read_text(encoding="utf-8").replace(
                    '"state": "done"', '"state": "captured"', 1
                ),
                encoding="utf-8",
            )

            errors = validate_questbook_surface.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn(
            "generated/quest_catalog.min.example.json must match generated/quest_catalog.min.json",
            errors[0],
        )


if __name__ == "__main__":
    unittest.main()
