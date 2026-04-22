# AOA-TITAN-SEED-04: Mutation Gate

## Purpose

Prevent the service cohort from silently mutating project state.

## Contract

Forge is the only first-wave Titan with workspace-write posture. Forge appears only after explicit mutation intent, a named target surface, and a rollback or validation posture.

## First landing

Target repos: `aoa-skills`, `aoa-playbooks`, `aoa-sdk`

Required surfaces:

```text
aoa-skills/skills/titan-mutation-gate/SKILL.md
aoa-playbooks/docs/TITAN_SERVICE_COHORT_PLAYBOOK.md
aoa-sdk/docs/TITAN_SESSION_INGRESS.md
```

## Mutation gate packet

```text
intent: what must change
targets: repo paths or owner surfaces
allowed_actor: Forge
precheck: Atlas route + Sentinel risk + Mneme provenance
validation: command or manual review note
rollback: revert path or stop condition
```

## Acceptance

1. Forge cannot appear during default summon.
2. Forge cannot edit without target surfaces.
3. Atlas, Sentinel, and Mneme remain read-only companions.
4. Every Forge action must leave a receipt.

## Non-goals

This seed does not implement destructive automation or permission bypass.
