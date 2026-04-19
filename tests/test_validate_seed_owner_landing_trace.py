from __future__ import annotations

import json
import shutil
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts import validate_seed_owner_landing_trace


REPO_ROOT = Path(__file__).resolve().parents[1]
SURFACE_PATHS = (
    "schemas/seed_owner_landing_trace.schema.json",
    "examples/seed_owner_landing_trace.example.json",
    "examples/seed_lineage_entry.example.json",
)


def copy_surface(target_root: Path) -> None:
    for relative_path in SURFACE_PATHS:
        source = REPO_ROOT / relative_path
        destination = target_root / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


class ValidateSeedOwnerLandingTraceTests(unittest.TestCase):
    def test_repo_surface_validates(self) -> None:
        self.assertEqual([], validate_seed_owner_landing_trace.run_validation(REPO_ROOT))

    def test_trace_requires_alignment_with_seed_lineage_entry(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "examples/seed_owner_landing_trace.example.json"
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            payload["candidate_ref"] = "candidate:session-growth:other"
            example_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

            errors = validate_seed_owner_landing_trace.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("candidate_ref must stay aligned", errors[0])

    def test_landed_owner_status_requires_owner_status_ref(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "examples/seed_owner_landing_trace.example.json"
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            payload["owner_status_ref"] = None
            example_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

            errors = validate_seed_owner_landing_trace.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("outcome 'landed_owner_status' requires owner_status_ref", errors[0])

    def test_merged_outcome_requires_merged_into(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "examples/seed_owner_landing_trace.example.json"
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            payload["outcome"] = "merged"
            payload["owner_status_ref"] = None
            example_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

            errors = validate_seed_owner_landing_trace.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("outcome 'merged' requires merged_into", errors[0])

    def test_observed_at_must_be_valid_datetime(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "examples/seed_owner_landing_trace.example.json"
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            payload["observed_at"] = "not-a-date"
            example_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

            errors = validate_seed_owner_landing_trace.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("schema violation at 'observed_at'", errors[0])

    def test_reanchored_outcome_requires_superseded_by(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "examples/seed_owner_landing_trace.example.json"
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            payload["outcome"] = "reanchored"
            payload["owner_status_ref"] = None
            payload["superseded_by"] = None
            example_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

            errors = validate_seed_owner_landing_trace.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("outcome 'reanchored' requires superseded_by", errors[0])

    def test_non_reanchored_outcome_forbids_superseded_by(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "examples/seed_owner_landing_trace.example.json"
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            payload["superseded_by"] = "seed:aoa:session-growth:reviewed-donor-harvest:v2"
            example_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

            errors = validate_seed_owner_landing_trace.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("superseded_by requires outcome 'reanchored'", errors[0])

    def test_dropped_outcome_requires_drop_reason(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            copy_surface(root)
            example_path = root / "examples/seed_owner_landing_trace.example.json"
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            payload["outcome"] = "dropped"
            payload["owner_status_ref"] = None
            example_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

            errors = validate_seed_owner_landing_trace.run_validation(root)

        self.assertEqual(1, len(errors))
        self.assertIn("outcome 'dropped' requires drop_reason", errors[0])


if __name__ == "__main__":
    unittest.main()
