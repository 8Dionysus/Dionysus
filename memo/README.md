# Dionysus Memo Port

This is the seed-garden local memory port for `Dionysus`.

Use it for candidates, receipts, exports, and local notes that should be visible
to future agents without making `Dionysus` the central memory authority.

| Path | Use |
|---|---|
| `PORT.yaml` | seed-garden port contract |
| `INDEX.md` / `index.min.json` | generated local read model over packets |
| `candidates/` | proposed memory claims with evidence refs |
| `receipts/` | accept, reject, validate, or forward traces |
| `exports/` | reviewed-intake packets for `aoa-memo` |
| `local/` | seed-garden memory notes that should remain local |

Default write mode: `write_candidate_only`.
