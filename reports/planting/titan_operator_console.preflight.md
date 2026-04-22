# Titan Operator Console Preflight

Date: 2026-04-22
Wave: `twelfth_wave.manifest.json`

Preconditions: Titan names are known; runtime harness has receipt and gate vocabulary; Codex subagents remain explicit, not autospawned.

Risk gates: app-server bridge remains seed-only until installed runtime is verified; console must not silently spawn subagents; console must not silently mutate workspace files.
