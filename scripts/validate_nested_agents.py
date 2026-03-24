#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_AGENTS = (
    ROOT / 'AGENTS.md',
    ROOT / 'archive' / 'AGENTS.md',
    ROOT / 'docs' / 'codex' / 'AGENTS.md',
    ROOT / 'reports' / 'planting' / 'AGENTS.md',
    ROOT / 'seed_expansion' / 'AGENTS.md',
)


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def validate_agents_docs() -> None:
    for path in REQUIRED_AGENTS:
        rel = path.relative_to(ROOT).as_posix()
        if not path.is_file():
            fail(f'missing required AGENTS.md: {rel}')
        try:
            text = path.read_text(encoding='utf-8').strip()
        except OSError as exc:
            fail(f'unable to read {rel}: {exc}')
        if not text:
            fail(f'empty AGENTS.md: {rel}')


def main() -> int:
    try:
        validate_agents_docs()
    except ValidationError as exc:
        print(f'[error] {exc}', file=sys.stderr)
        return 1

    for path in REQUIRED_AGENTS:
        print(f"[ok] validated {path.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
