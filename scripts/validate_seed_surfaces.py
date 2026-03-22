#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATORS = (
    ROOT / 'scripts' / 'validate_manifest.py',
    ROOT / 'scripts' / 'validate_seed_registry.py',
)


def main() -> int:
    for validator in VALIDATORS:
        result = subprocess.run([sys.executable, str(validator)], cwd=ROOT, check=False)
        if result.returncode != 0:
            return result.returncode
    print('[ok] validated seed surfaces')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
