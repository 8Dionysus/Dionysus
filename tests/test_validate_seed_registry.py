from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts import validate_seed_registry


class ValidateSeedRegistryTests(unittest.TestCase):
    def test_archived_seed_pack_traceability_rejects_unlinked_pack(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pack_dir = root / "archive" / "seed_pack_2026-03-24_kag-frontier"
            pack_dir.mkdir(parents=True)
            (pack_dir / "README.md").write_text("# Archived pack\n", encoding="utf-8")

            with self.assertRaises(validate_seed_registry.ValidationError) as exc:
                validate_seed_registry.validate_archived_seed_pack_traceability(
                    {"origin_notes": [], "wave_index": [], "seed_index": []},
                    root,
                )

        self.assertIn("archive/seed_pack_2026-03-24_kag-frontier/", str(exc.exception))

    def test_archived_seed_pack_traceability_accepts_source_linkage(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pack_dir = root / "archive" / "seed_pack_2026-03-24_kag-frontier"
            pack_dir.mkdir(parents=True)
            readme = pack_dir / "README.md"
            readme.write_text("# Archived pack\n", encoding="utf-8")

            validate_seed_registry.validate_archived_seed_pack_traceability(
                {
                    "origin_notes": [],
                    "wave_index": [],
                    "seed_index": [
                        {
                            "source_ref": "archive/seed_pack_2026-03-24_kag-frontier/README.md",
                            "provenance": {"provenance_note": None},
                        }
                    ],
                },
                root,
            )

    def test_archived_seed_pack_immutable_sources_rejects_branch_links(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pack_dir = root / "archive" / "seed_pack_2026-03-24_kag-frontier"
            pack_dir.mkdir(parents=True)
            (pack_dir / "seed_small_kag2.md").write_text(
                "[1]: https://raw.githubusercontent.com/8Dionysus/Tree-of-Sophia/main/README.md\n",
                encoding="utf-8",
            )

            with self.assertRaises(validate_seed_registry.ValidationError) as exc:
                validate_seed_registry.validate_archived_seed_pack_immutable_sources(root)

        self.assertIn("seed_small_kag2.md", str(exc.exception))
        self.assertIn("main", str(exc.exception))

    def test_archived_seed_pack_immutable_sources_accepts_commit_pins(self) -> None:
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pack_dir = root / "archive" / "seed_pack_2026-03-24_kag-frontier"
            pack_dir.mkdir(parents=True)
            (pack_dir / "seed_small_kag2.md").write_text(
                "[1]: https://raw.githubusercontent.com/8Dionysus/Tree-of-Sophia/"
                "0123456789abcdef0123456789abcdef01234567/README.md\n",
                encoding="utf-8",
            )

            validate_seed_registry.validate_archived_seed_pack_immutable_sources(root)


if __name__ == "__main__":
    unittest.main()
