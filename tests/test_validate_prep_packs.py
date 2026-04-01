from __future__ import annotations

import shutil
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts import validate_prep_packs


REPO_ROOT = Path(__file__).resolve().parents[1]
SURFACE_PATHS = (
    "archive/seed_pack_exports",
    "seed-registry.yaml",
    "seed_questbook_foundation_pack.md",
    "seed_questbook_foundation_pack.map.yaml",
    "seed_questbook_source_proof_pack.md",
    "seed_questbook_source_proof_pack.map.yaml",
    "seed_questbook_boundary_runtime_pack.md",
    "seed_questbook_boundary_runtime_pack.map.yaml",
    "seed_questbook_seedgarden_profile_pack.md",
    "seed_questbook_seedgarden_profile_pack.map.yaml",
    "seed_rpg_first_wave_pack.md",
    "seed_rpg_first_wave_pack.map.yaml",
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


class ValidatePrepPacksTests(unittest.TestCase):
    def test_repo_surface_validates(self) -> None:
        self.assertEqual([], validate_prep_packs.run_validation(REPO_ROOT))

    def test_rpg_pack_rejects_next_live_seed_drift(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            map_path = root / "seed_rpg_first_wave_pack.map.yaml"
            map_path.write_text(
                map_path.read_text(encoding="utf-8").replace(
                    "seed_expansion/seed.tos.wider-world-thought-expansion.v0.md#tos-expansion-wider-world-thought-expansion",
                    "seed_expansion/seed.fake.next.v0.md#fake-next",
                    1,
                ),
                encoding="utf-8",
            )

            errors = validate_prep_packs.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("keep_next_live_seed must match seed-registry navigation.next_live_seed", errors[0])

    def test_rpg_pack_rejects_seed_index_registration(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            registry_path = root / "seed-registry.yaml"
            registry_path.write_text(
                registry_path.read_text(encoding="utf-8").replace(
                    "seed_index:\n",
                    "seed_index:\n- source_ref: seed_rpg_first_wave_pack.md#seed-note\n",
                    1,
                ),
                encoding="utf-8",
            )

            errors = validate_prep_packs.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("seed-registry.yaml.seed_index must not register prep-pack note 'seed_rpg_first_wave_pack.md' yet", errors[0])

    def test_rpg_pack_rejects_out_of_archive_source_bundle(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            map_path = root / "seed_rpg_first_wave_pack.map.yaml"
            map_path.write_text(
                map_path.read_text(encoding="utf-8").replace(
                    "archive/seed_pack_exports/rpg_first_wave_seed.zip",
                    "rpg_first_wave_seed.zip",
                    1,
                ),
                encoding="utf-8",
            )

            errors = validate_prep_packs.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("source_bundle.path must be 'archive/seed_pack_exports/rpg_first_wave_seed.zip'", errors[0])


if __name__ == "__main__":
    unittest.main()
