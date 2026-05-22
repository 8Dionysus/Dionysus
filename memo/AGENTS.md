# AGENTS.md

## Applies to

This card applies to `memo/`.

## Role

`memo/` is the Dionysus local memory port. It holds seed-garden memory
candidates, receipts, exports, and local notes before reviewed landing in
`aoa-memo`.

## Read before editing

1. Root `AGENTS.md`
2. `seed-registry.yaml`
3. `ROADMAP.md`
4. `docs/SEED_SURFACE_MAP.md`
5. This `README.md`
6. `PORT.yaml`
7. `aoa-memo` memory operation contracts when a candidate should move centrally

## Boundaries

Use this port for `write_candidate_only` work. Keep seed truth, planting trace,
and staging records in Dionysus source surfaces; use this port for recall,
candidate memory, receipts, and reviewed handoff.

Use `PORT.yaml` for the local port contract and `INDEX.md` / `index.min.json`
as generated read models. Use `candidates/` for proposed memory, `receipts/`
for review or handoff traces, `exports/` for packets meant for `aoa-memo`, and
`local/` for seed-garden memory that stays local for now.

## Candidate Route

Create seed-garden candidates through the stack MCP helper:

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli create-candidate \
  --repo Dionysus \
  --evidence-ref README.md \
  --claim "Dionysus memory should move through reviewed local candidates before aoa-memo landing."
```

Then validate the emitted candidate path:

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli validate-candidate path/to/candidate.json
```

## Reviewed Landing Route

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli pending-exports --repo Dionysus
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli landing-plan --repo Dionysus --export-ref exports/path.reviewed-intake.json --run-dry-run
```

`landing-plan` is an access-plane check. Durable memory lands only in
`aoa-memo` through reviewed intake, generated read models, validators, and
review.

## Validation

```bash
python /srv/AbyssOS/aoa-memo/scripts/memory/validate_local_memo_port.py --path memo
python /srv/AbyssOS/aoa-memo/scripts/memory/build_local_memo_port_index.py --path memo --check
```

For repo-wide release posture, use the root `AGENTS.md` validation route.

## Closeout

Report candidate path, evidence refs, validation result, and whether the item
stayed local, was exported for reviewed intake, or was landed in `aoa-memo`.
