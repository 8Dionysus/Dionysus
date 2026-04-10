# Releasing `Dionysus`

`Dionysus` is released as the seed garden and staging surface of the AoA federation.

See also:

- [README](../README.md)
- [CHANGELOG](../CHANGELOG.md)

## Recommended release flow

1. Keep the release bounded to seed and staging surfaces.
2. Update `CHANGELOG.md` in the `Summary / Validation / Notes` shape.
3. Run the repo-level verifier:
   - `python scripts/release_check.py`
4. Run federation preflight:
   - `aoa release audit /srv --phase preflight --repo Dionysus --strict --json`
5. Publish only through `aoa release publish`.
