#!/usr/bin/env python3
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print(
        "[error] PyYAML is required for seed note lifecycle validation. Install it with: python -m pip install PyYAML",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_LIFECYCLE_STATUS = {
    "landed_upstream_retained_for_lineage",
    "partially_landed_retained_for_lineage",
    "staged_only_not_landed",
    "donor_only_not_planted",
}
EXPECTED_NOTES = {
    "seed_staging/donor/seed_clawrouter_donor_graft.md": {
        "kind": "donor-note",
        "lifecycle_status": "donor_only_not_planted",
    },
    "seed_staging/donor/seed_aoa_session_donor_harvest.md": {
        "kind": "donor-note",
        "lifecycle_status": "donor_only_not_planted",
    },
    "seed_staging/audit/seed_wave1_codex_audit_spine.md": {
        "kind": "audit-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/audit/seed_wave2_codex_skill_proof_audit_bridge.md": {
        "kind": "audit-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/audit/seed_federated_audit_remediation_pack.md": {
        "kind": "audit-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/future/seed_architecture_fit_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "staged_only_not_landed",
    },
    "seed_staging/future/seed_dialogue_memory_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "staged_only_not_landed",
    },
    "seed_staging/future/seed_federation_conductor_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "staged_only_not_landed",
    },
    "seed_staging/future/seed_memory_evals_skills_docs_pack.md": {
        "kind": "candidate-pack-note",
        "lifecycle_status": "staged_only_not_landed",
    },
    "seed_staging/future/seed_future_agent_systems_prep_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "staged_only_not_landed",
    },
    "seed_staging/future/seed_aoa_session_harvest_family_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/future/seed_aoa_automation_opportunity_scan_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "staged_only_not_landed",
    },
    "seed_staging/future/seed_aoa_wave2_refinery_convergence_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "staged_only_not_landed",
    },
    "seed_staging/future/seed_aoa_wave7_trusted_rollout_ops_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "staged_only_not_landed",
    },
    "seed_staging/future/seed_aoa_wave3_owner_landing_followthrough_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/future/seed_aoa_codex_surface_plane_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "partially_landed_retained_for_lineage",
    },
    "seed_staging/future/seed_aoa_rag_skeleton_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "partially_landed_retained_for_lineage",
    },
    "seed_staging/future/seed_aoa_stats_telemetry_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "partially_landed_retained_for_lineage",
    },
    "seed_staging/future/seed_aoa_first_wave_candidate_lineage_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/future/seed_aoa_remaining_seeds_execution_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/future/seed_aoa_antifragility_wave_4_5_via_negativa_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/audit/seed_wave3_codex_repo_local_skills_trace_harness.md": {
        "kind": "audit-pack-note",
        "lifecycle_status": "staged_only_not_landed",
    },
    "seed_staging/root_docs/seed_wave1_root_docs_refresh.md": {
        "kind": "docs-refresh-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/root_docs/seed_wave2_root_docs_refresh.md": {
        "kind": "docs-refresh-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/root_docs/seed_wave3_root_docs_refresh.md": {
        "kind": "docs-refresh-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/questbook/seed_questbook_foundation_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/questbook/seed_questbook_source_proof_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/questbook/seed_questbook_boundary_runtime_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/questbook/seed_questbook_seedgarden_profile_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "partially_landed_retained_for_lineage",
    },
    "seed_staging/rpg/seed_rpg_first_wave_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/rpg/seed_rpg_second_wave_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/rpg/seed_rpg_architecture_rfc_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/rpg/seed_rpg_bridge_wave_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/rpg/seed_rpg_sdk_addendum_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
    "seed_staging/rpg/seed_rpg_runtime_projection_pack.md": {
        "kind": "prep-pack-note",
        "lifecycle_status": "landed_upstream_retained_for_lineage",
    },
}
REQUIRED_KEYS = (
    "seed_id",
    "kind",
    "lifecycle_status",
    "lifecycle_note",
    "reality_checked_at",
)
EXPECTED_COMPANION_MAPS = {
    "seed_staging/future/seed_aoa_antifragility_wave_4_5_via_negativa_pack.md": {
        "path": "seed_staging/future/seed_aoa_antifragility_wave_4_5_via_negativa_pack.map.yaml",
        "updated_at": "2026-04-08",
        "required_lineage_tokens": (
            "owner-repo landings were verified",
            "lineage-only replay",
        ),
        "forbidden_lineage_tokens": (
            "no via-negativa owner-repo landings are yet verified in the current workspace",
        ),
    }
}


class ValidationError(RuntimeError):
    """Raised when a structured seed note lifecycle check fails."""


def fail(message: str) -> None:
    raise ValidationError(message)


def load_note_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    frontmatter, separator, _ = text.partition("\n\n")
    if not separator:
        fail(f"{path.name}: missing frontmatter/body separator")
    data = yaml.safe_load(frontmatter)
    if not isinstance(data, dict) or not data:
        fail(f"{path.name}: frontmatter must be a non-empty mapping")
    return data


def require_mapping(value: object, label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or not value:
        fail(f"{label}: must be a non-empty mapping")
    return value


def require_nonempty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label}: must be a non-empty string")
    return value


def require_iso_date(value: object, label: str) -> str:
    date_string = require_nonempty_string(value, label)
    try:
        date.fromisoformat(date_string)
    except ValueError as exc:
        fail(f"{label}: must be an ISO date in YYYY-MM-DD form")
    return date_string


def display_path(path: Path, *, root: Path = ROOT) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def load_yaml(path: Path, *, root: Path = ROOT) -> dict[str, Any]:
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        fail(f"missing file: {display_path(path, root=root)}")
    if not isinstance(payload, dict) or not payload:
        fail(f"{display_path(path, root=root)}: YAML payload must be a non-empty mapping")
    return payload


def require_string_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
        fail(f"{label}: must be a non-empty list of non-empty strings")
    return list(value)


def validate_seed_note_lifecycle(root: Path = ROOT) -> None:
    for note_name, expected in EXPECTED_NOTES.items():
        note_path = root / note_name
        if not note_path.exists():
            fail(f"missing lifecycle-tracked note: {note_name}")

        frontmatter = require_mapping(load_note_frontmatter(note_path), note_name)
        for key in REQUIRED_KEYS:
            if key not in frontmatter:
                fail(f"{note_name}: missing frontmatter key '{key}'")

        if require_nonempty_string(frontmatter["kind"], f"{note_name}.kind") != expected["kind"]:
            fail(f"{note_name}.kind must be '{expected['kind']}'")

        lifecycle_status = require_nonempty_string(
            frontmatter["lifecycle_status"], f"{note_name}.lifecycle_status"
        )
        if lifecycle_status not in ALLOWED_LIFECYCLE_STATUS:
            fail(
                f"{note_name}.lifecycle_status must be one of "
                f"{sorted(ALLOWED_LIFECYCLE_STATUS)}"
            )
        if lifecycle_status != expected["lifecycle_status"]:
            fail(f"{note_name}.lifecycle_status must be '{expected['lifecycle_status']}'")

        require_nonempty_string(frontmatter["seed_id"], f"{note_name}.seed_id")
        require_nonempty_string(frontmatter["lifecycle_note"], f"{note_name}.lifecycle_note")
        require_iso_date(frontmatter["reality_checked_at"], f"{note_name}.reality_checked_at")

        companion_map = EXPECTED_COMPANION_MAPS.get(note_name)
        if companion_map is not None:
            map_path = root / companion_map["path"]
            payload = load_yaml(map_path, root=root)
            updated_at = require_iso_date(payload.get("updated_at"), f"{companion_map['path']}.updated_at")
            if updated_at != companion_map["updated_at"]:
                fail(f"{companion_map['path']}.updated_at must be '{companion_map['updated_at']}'")

            selection_policy = require_mapping(
                payload.get("selection_policy"),
                f"{companion_map['path']}.selection_policy",
            )
            lineage_precondition = require_string_list(
                selection_policy.get("lineage_precondition"),
                f"{companion_map['path']}.selection_policy.lineage_precondition",
            )
            combined = "\n".join(lineage_precondition)
            for token in companion_map["required_lineage_tokens"]:
                if token not in combined:
                    fail(
                        f"{companion_map['path']}.selection_policy.lineage_precondition must mention {token!r}"
                    )
            for token in companion_map["forbidden_lineage_tokens"]:
                if token in combined:
                    fail(
                        f"{companion_map['path']}.selection_policy.lineage_precondition must not mention {token!r}"
                    )


def run_validation(root: Path = ROOT) -> list[str]:
    try:
        validate_seed_note_lifecycle(root)
    except ValidationError as exc:
        return [str(exc)]
    return []


def main() -> int:
    errors = run_validation(ROOT)
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print("[ok] validated structured seed note lifecycle")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
