# AOA-TITAN-SEED-03: Summon Ritual

## Purpose

Create the explicit invocation surface for the first Titan appearance.

## Contract

The first summon uses an initial Codex prompt. It asks Codex to spawn Atlas, Sentinel, and Mneme as the default read-only service cohort. It forbids Forge without mutation intent and Delta without judgment intent.

## First landing

Target repos: `8Dionysus`, `aoa-sdk`

Required surfaces:

```text
8Dionysus/.codex/prompts/titan-summon.service-cohort.v0.md
8Dionysus/docs/TITAN_FIRST_APPEARANCE_RUNBOOK.md
aoa-sdk/docs/TITAN_SESSION_INGRESS.md
aoa-sdk/schemas/titan_session_ingress.schema.json
```

## First command

```bash
codex --cd /srv "$(cat /srv/8Dionysus/.codex/prompts/titan-summon.service-cohort.v0.md)"
```

## Acceptance

1. The prompt names all five Titans.
2. The default active roster is Atlas, Sentinel, Mneme.
3. The response must report roster, route frame, risk gates, memory posture, and suggested next move.
4. The prompt must preserve no hidden arena, no silent closure, and no unapproved mutation.

## Non-goals

This seed does not make hooks silently spawn agents. Hooks may add developer context and warnings, but the summon remains explicit.
