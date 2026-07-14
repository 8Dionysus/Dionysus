# Dionysus local stats port

This directory exposes statistical questions whose domain meaning belongs to
the seed garden. It uses the shared `aoa-stats` grammar without moving seed
lifecycle meaning or planting authority into the central stats organ.

## Current reference measurement

| Measurement | Question | Reference value |
| --- | --- | --- |
| `Dionysus/seed-registry-landed-post-wave-ratio` | What fraction of entries in the current validated seed registry v2 carry the owner-authored lifecycle label `landed_post_wave`? | `56 / 89` at evidence revision `e00762d05b6eb37c19c80bbe85432ff7c1a8b7c7` |

The population is a census of unique records in `seed-registry.yaml` under
`seed_index`. Wave records, origin notes, source files, staging packs, archives,
planting reports, and target-repository state are excluded. A complete registry
with no `landed_post_wave` rows is an observed zero; an unsupported version or
a malformed, empty, or duplicate population is unknown.

## Evidence posture

The packet is a public reference snapshot of the owner-validated registry at a
named source revision. It is not a live inspection of target repositories, and
its terminal progress field means only that the declared census was processed.

## Authority

The ratio describes one literal navigation label in the seed registry. It does
not prove a target-repository merge, current owner acceptance, landing quality,
completeness, canonical meaning, release readiness, or what should be planted
next.

## Surfaces

- `port.manifest.json` declares the owner-local question and measurement.
- `packets/seed-registry-landed-post-wave-ratio.reference.json` records the
  evidence-linked reference observation.
- `seed-registry.yaml` owns the lifecycle labels used by the measurement.
- `scripts/validate_seed_registry.py` remains the owner validator.
- `aoa-stats` owns shared validation and cross-owner composition.
