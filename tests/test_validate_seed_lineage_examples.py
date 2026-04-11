from __future__ import annotations

import json
import shutil
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts import validate_seed_lineage_examples


REPO_ROOT = Path(__file__).resolve().parents[1]
SURFACE_PATHS = (
    "schemas/seed_lineage_entry.schema.json",
    "examples/seed_lineage_entry.example.json",
)


def copy_surface(target_root: Path) -> None:
    for relative_path in SURFACE_PATHS:
        source = REPO_ROOT / relative_path
        destination = target_root / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


class ValidateSeedLineageExamplesTests(unittest.TestCase):
    def test_repo_surface_validates(self) -> None:
        self.assertEqual([], validate_seed_lineage_examples.run_validation(REPO_ROOT))

    def test_preplant_entry_rejects_object_ref(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "examples/seed_lineage_entry.example.json"
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            payload["object_ref"] = "docs/reviewed-growth-refinery.md"
            example_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

            errors = validate_seed_lineage_examples.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("must keep object_ref null before planting", errors[0])

    def test_merged_into_requires_superseded_state(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "examples/seed_lineage_entry.example.json"
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            payload["merged_into"] = "seed:aoa:session-growth:reviewed-donor-harvest:v2"
            example_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

            errors = validate_seed_lineage_examples.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("merged_into requires lifecycle_status 'superseded'", errors[0])


if __name__ == "__main__":
    unittest.main()
