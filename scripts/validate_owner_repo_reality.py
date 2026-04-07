#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any
from urllib import error as urllib_error
from urllib import request as urllib_request

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print(
        "[error] PyYAML is required for owner-repo reality validation. Install it with: python -m pip install PyYAML",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc

ROOT = Path(__file__).resolve().parents[1]
CANARY_SPEC_PATH = (
    ROOT / "reports" / "ecosystem-audits" / "federated-audit-remediation.reality-canary.yaml"
)


class ValidationError(RuntimeError):
    """Raised when the owner-repo reality canary detects stale or missing anchors."""


def fail(message: str) -> None:
    raise ValidationError(message)


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        fail(f"missing required file: {path}")
    if not isinstance(payload, dict) or not payload:
        fail(f"{path}: YAML payload must be a non-empty mapping")
    return payload


def require_string_list(value: object, label: str) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        fail(f"{label}: must be a string or a list of non-empty strings")
    return list(value)


def resolve_path(root: Path, raw_path: str) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    return root / path


def read_target_text(root: Path, raw_path: str) -> tuple[str, str]:
    if raw_path.startswith(("http://", "https://")):
        try:
            with urllib_request.urlopen(raw_path) as response:
                payload = response.read()
        except (urllib_error.URLError, OSError) as exc:
            fail(f"missing owner-repo surface {raw_path}: {exc}")
        try:
            return payload.decode("utf-8"), raw_path
        except UnicodeDecodeError as exc:
            fail(f"{raw_path}: remote owner-repo surface must be UTF-8 text ({exc})")

    target_path = resolve_path(root, raw_path)
    if not target_path.is_file():
        fail(f"missing owner-repo surface {target_path}")
    return target_path.read_text(encoding="utf-8"), str(target_path)


def validate_canary_spec(root: Path = ROOT, spec_path: Path = CANARY_SPEC_PATH) -> None:
    payload = load_yaml(spec_path)
    checks = payload.get("checks")
    if not isinstance(checks, list) or not checks:
        fail(f"{spec_path}: must define a non-empty 'checks' list")

    for index, check in enumerate(checks):
        location = f"{spec_path}:checks[{index}]"
        if not isinstance(check, dict):
            fail(f"{location}: each check must be a mapping")
        check_id = check.get("id")
        raw_path = check.get("path")
        if not isinstance(check_id, str) or not check_id:
            fail(f"{location}: missing non-empty 'id'")
        if not isinstance(raw_path, str) or not raw_path:
            fail(f"{location}: missing non-empty 'path'")

        text, target_label = read_target_text(root, raw_path)
        for token in require_string_list(check.get("contains"), f"{location}.contains"):
            if token not in text:
                fail(f"{check_id}: expected token {token!r} in {target_label}")
        for token in require_string_list(check.get("not_contains"), f"{location}.not_contains"):
            if token in text:
                fail(f"{check_id}: stale token {token!r} still present in {target_label}")


def run_validation(root: Path = ROOT, spec_path: Path = CANARY_SPEC_PATH) -> list[str]:
    try:
        validate_canary_spec(root=root, spec_path=spec_path)
    except ValidationError as exc:
        return [str(exc)]
    return []


def main() -> int:
    errors = run_validation(ROOT, CANARY_SPEC_PATH)
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print("[ok] validated owner-repo reality canary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
