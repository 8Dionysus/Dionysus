# Private vault boundary

This directory is the local placeholder for future private Dionysus artifacts.
Everything under `vault/` except this file is ignored by Git.

Do not treat the ignore rule as encryption. Until a reviewed storage design
exists, do not put real interviews here on a shared or untrusted machine.

A future vault may separate:

```text
raw/
transcripts/
evidence/
claims/
projections/
consent/
```

No such storage contract is implemented by the current skeleton.
