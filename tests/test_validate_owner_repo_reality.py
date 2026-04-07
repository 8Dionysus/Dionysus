from __future__ import annotations

import textwrap
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from scripts import validate_owner_repo_reality


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_owner_repo_reality_canary_accepts_current_anchor_set() -> None:
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        target = root / "owner" / "surface.txt"
        spec = root / "canary.yaml"
        write_text(target, "token-a\ntoken-b\n")
        write_text(
            spec,
            textwrap.dedent(
                f"""
                canary_version: 1
                checks:
                  - id: sample
                    path: {target.as_posix()}
                    contains:
                      - token-a
                    not_contains:
                      - stale-token
                """
            ).strip()
            + "\n",
        )

        assert validate_owner_repo_reality.run_validation(root, spec) == []


def test_owner_repo_reality_canary_rejects_stale_anchor() -> None:
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        target = root / "owner" / "surface.txt"
        spec = root / "canary.yaml"
        write_text(target, "old-token\n")
        write_text(
            spec,
            textwrap.dedent(
                f"""
                canary_version: 1
                checks:
                  - id: stale
                    path: {target.as_posix()}
                    not_contains:
                      - old-token
                """
            ).strip()
            + "\n",
        )

        errors = validate_owner_repo_reality.run_validation(root, spec)
        assert len(errors) == 1
        assert "stale token 'old-token'" in errors[0]


def test_owner_repo_reality_canary_accepts_remote_anchor(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeResponse:
        def __enter__(self) -> "FakeResponse":
            return self

        def __exit__(self, exc_type, exc, tb) -> None:
            return None

        def read(self) -> bytes:
            return b"remote-token\n"

    def fake_urlopen(url: str) -> FakeResponse:
        assert url == "https://example.invalid/surface.txt"
        return FakeResponse()

    monkeypatch.setattr(validate_owner_repo_reality.urllib_request, "urlopen", fake_urlopen)

    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        spec = root / "canary.yaml"
        write_text(
            spec,
            textwrap.dedent(
                """
                canary_version: 1
                checks:
                  - id: remote
                    path: https://example.invalid/surface.txt
                    contains:
                      - remote-token
                """
            ).strip()
            + "\n",
        )

        assert validate_owner_repo_reality.run_validation(root, spec) == []
