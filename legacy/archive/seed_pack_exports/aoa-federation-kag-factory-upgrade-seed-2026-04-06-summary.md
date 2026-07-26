# aoa-federation-kag-factory-upgrade seed summary

Artifacts:
- `aoa-federation-kag-factory-upgrade-seed-2026-04-06.zip`

Core idea:
- turn the current bounded two-donor federation spine into a manifest-driven federation ingress system
- separate donor publication, registry visibility, spine visibility, and routing visibility instead of treating them as one event
- keep source repos authoritative, `aoa-kag` derived, `aoa-routing` navigation-only, `aoa-sdk` control-plane-only, and `aoa-memo` below proof
- preserve the current live contour by keeping `aoa-techniques` and `Tree-of-Sophia` live while `aoa-memo` stays registry-visible only until explicit activation

Reality check on `2026-04-09`:
- the sibling workspace already contains the named primary targets `aoa-kag`, `aoa-routing`, `aoa-sdk`, and optional proof repo `aoa-evals`
- the package marks `aoa-kag` as the mandatory first owner and keeps `aoa-routing` and `aoa-sdk` as bounded follow-on phases
- no owner-repo landing is verified yet; this bundle should be read as Dionysus staging and lineage, not as current owner truth
