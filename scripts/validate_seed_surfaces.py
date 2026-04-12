#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATORS = (
    ROOT / 'scripts' / 'validate_manifest.py',
    ROOT / 'scripts' / 'validate_seed_registry.py',
    ROOT / 'scripts' / 'validate_seed_route_map.py',
    ROOT / 'scripts' / 'validate_prep_packs.py',
    ROOT / 'scripts' / 'validate_seed_lineage_examples.py',
    ROOT / 'scripts' / 'validate_seed_owner_landing_trace.py',
    ROOT / 'scripts' / 'validate_checkpoint_notes.py',
    ROOT / 'scripts' / 'validate_seed_note_lifecycle.py',
    ROOT / 'scripts' / 'validate_owner_repo_reality.py',
    ROOT / 'scripts' / 'validate_questbook_surface.py',
    ROOT / 'scripts' / 'validate_nested_agents.py',
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
