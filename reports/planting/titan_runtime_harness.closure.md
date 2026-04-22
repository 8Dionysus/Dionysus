# Titan Runtime Harness Closure Draft

Date: 2026-04-22

## Closure condition

This closure may be marked complete when:

1. `titanctl.py roster --json` returns the five named Titans.
2. `titanctl.py summon` writes a valid receipt.
3. `titanctl.py gate --agent Forge --kind mutation` records mutation permission only for Forge.
4. `titanctl.py gate --agent Delta --kind judgment` records judgment permission only for Delta.
5. `titanctl.py closeout` closes a receipt without granting memory sovereignty.
6. eval canaries exist for hidden arena, ungated Forge, ungated Delta, and missing closeout.

## Closure sentence

The first Titans held the lanterns. The second wave teaches the lanterns to cast shadows on the ledger.
