# Ecosystem Audits

This folder stores durable human+AI-readable cross-repo audits when Dionysus is
the right place to preserve a system-level review that spans multiple owning
repositories and the runtime body.

Use it for:

- ecosystem-wide maturity reviews
- source-vs-runtime drift audits
- cross-repo closure snapshots
- controlled-autonomy readiness assessments
- closeout digests for audit-driven remediation waves
- lightweight promoted `checkpoint-note` snapshots when a reviewed local
  session-growth note should survive outside `.aoa/` but a full
  `session-harvest.*` family would be premature

Do not use it for:

- repo-local doctrine that belongs in the owning repository
- raw runtime truth packets
- private host artifacts
- hidden machine-readable scoreboards that replace source-owned meaning
- raw append history from local checkpoint-note JSONL logs

Keep reports compact, evidence-backed, and explicit about scope.
These audits are durable review surfaces, not new sovereign sources.
The lightweight `checkpoint-note` family is a reviewed snapshot layer.
It does not make the heavier `session-harvest.*` family mandatory for every
mid-session promotion.
