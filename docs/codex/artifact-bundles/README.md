# Dionysus Artifact Bundles

This directory holds repo-local manifests for OS Abyss artifact verification.

These manifests describe what Dionysus publishes for verifier consumption; they
do not own seed meaning. Seed meaning remains in manifests, exact seed sources,
closure notes, `seed-registry.yaml`, and the planting protocol.

## Seed Route Readmodel

`manifests/seed_route_readmodel.bundle.json` verifies
`generated/seed_route_map.min.json` as a `dionysus_seed_route_readmodel_bundle`.
The active controls are ABI-only:

```bash
python scripts/validate_abyss_machine_seed_route_bundle.py
```

The validator also writes a temporary OS Abyss bundle registry read-model,
requires a `release-ready` latest record only after successful ABI verification,
and rehearses rejection of corrupted ABI sidecars, private markers, unverified
latest promotion, terminal revocation, consumer trust-gate selection, and
isolated subject-store materialization.

C2PA is not claimed here. Public seed packs, PDFs, media, docs, or content
credentials need a real C2PA-capable artifact class and generator before they
can be treated as credentialed public exports.
