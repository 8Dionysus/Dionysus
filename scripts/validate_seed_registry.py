#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from datetime import date
from functools import lru_cache
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print(
        "[error] PyYAML is required for seed-registry validation. Install it with: python -m pip install PyYAML",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "seed-registry.yaml"
CONTRACT_PATH = ROOT / "schema/seed-registry.contract.yaml"
REQUIRED_REGISTRY_VERSION = 2
REQUIRED_NAVIGATION_KEYS = (
    "canonical_order_source",
    "semantic_source",
    "manifest_validator",
    "registry_validator",
    "validation_entrypoint",
    "registry_contract",
    "planting_report_template",
    "provenance_policy",
    "donor_capture_template",
    "registry_role",
    "archived_root",
    "archived_pack",
    "next_live_seed",
)
ALLOWED_ORIGIN_MODES = {"native", "donor_derived", "mixed"}
ALLOWED_TRANSPLANT_POLICIES = {
    "native",
    "idea_only",
    "pattern_extract",
    "adapt_with_attribution",
    "vendor_verbatim",
    "read_only_donor",
}
PROVENANCE_KEYS = (
    "origin_mode",
    "donor_repo",
    "donor_ref",
    "donor_license_spdx",
    "donor_paths",
    "provenance_note",
)
REDISTRIBUTION_KEYS = (
    "license_spdx",
    "upstream_license_ref",
    "copy_license_required",
    "notice_required",
    "retain_attribution_required",
    "mark_modifications_required",
    "modified_from_upstream",
    "obligations_note",
)
TRANSPLANT_KEYS = (
    "policy",
    "what_survives",
    "what_stays_behind",
    "non_goals",
)
FRESHNESS_KEYS = (
    "last_revalidated_at",
    "revalidate_after_days",
    "superseded_by",
)
MANIFEST_SPECS = {
    "first_wave.manifest.json": {
        "order_key": "first_wave_order",
        "tail_keys": ("later_pilots", "origin_notes"),
    },
    "second_wave.manifest.json": {
        "order_key": "second_wave_order",
        "tail_keys": ("deferred_pilots", "held_later"),
    },
    "third_wave.manifest.json": {
        "order_key": "third_wave_order",
        "tail_keys": ("deferred_pilots", "held_later"),
    },
    "fourth_wave.manifest.json": {
        "order_key": "fourth_wave_order",
        "tail_keys": ("held_later",),
    },
    "fifth_wave.manifest.json": {
        "order_key": "fifth_wave_order",
        "tail_keys": ("held_later",),
    },
    "sixth_wave.manifest.json": {
        "order_key": "sixth_wave_order",
        "tail_keys": ("held_later",),
    },
    "seventh_wave.manifest.json": {
        "order_key": "seventh_wave_order",
        "tail_keys": ("held_later",),
    },
    "eighth_wave.manifest.json": {
        "order_key": "eighth_wave_order",
        "tail_keys": ("held_later",),
    },
    "ninth_wave.manifest.json": {
        "order_key": "ninth_wave_order",
        "tail_keys": ("supporting_notes",),
    },
    "tenth_wave.manifest.json": {
        "order_key": "tenth_wave_order",
        "tail_keys": ("supporting_notes",),
    },
    "eleventh_wave.manifest.json": {
        "order_key": "eleventh_wave_order",
        "tail_keys": (),
    },
    "twelfth_wave.manifest.json": {
        "order_key": "twelfth_wave_order",
        "tail_keys": (),
    },
    "thirteenth_wave.manifest.json": {
        "order_key": "thirteenth_wave_order",
        "tail_keys": (),
    },
    "fourteenth_wave.manifest.json": {
        "order_key": "fourteenth_wave_order",
        "tail_keys": (),
    },
    "fifteenth_wave.manifest.json": {
        "order_key": "fifteenth_wave_order",
        "tail_keys": ("supporting_notes",),
    },
}
MARKDOWN_HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
HTML_ID = re.compile(r'<a\s+id="([^"]+)"></a>', re.IGNORECASE)
CLOSURE_STATUS = re.compile(r"\bStatus:\s*([A-Za-z_-]+)\b", re.IGNORECASE)
ARCHIVED_SEED_PACK_DIR = re.compile(r"^seed_pack_\d{4}-\d{2}-\d{2}(?:$|[-_])")
RAW_GITHUB_CONTENT_URL = re.compile(
    r"https://raw\.githubusercontent\.com/[^/\s]+/[^/\s]+/(?P<revision>[^/\s]+)/[^\s)>\"]+",
    re.IGNORECASE,
)
IMMUTABLE_GIT_REVISION = re.compile(r"^[0-9a-f]{7,40}$", re.IGNORECASE)


class ValidationError(RuntimeError):
    """Raised when registry validation fails."""


def fail(message: str) -> None:
    raise ValidationError(message)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing file: {path.relative_to(ROOT).as_posix()}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path.relative_to(ROOT).as_posix()}: {exc}") from exc


def load_yaml(path: Path) -> object:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing file: {path.relative_to(ROOT).as_posix()}") from exc
    except yaml.YAMLError as exc:
        raise ValidationError(f"invalid YAML in {path.relative_to(ROOT).as_posix()}: {exc}") from exc


@lru_cache(maxsize=None)
def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        for html_match in HTML_ID.finditer(line):
            anchors.add(html_match.group(1))
        match = MARKDOWN_HEADING.match(line)
        if not match:
            continue
        base = markdown_anchor(match.group(2))
        if not base:
            continue
        suffix = seen.get(base, 0)
        seen[base] = suffix + 1
        anchors.add(base if suffix == 0 else f"{base}-{suffix}")
    return anchors


def markdown_anchor(text: str) -> str:
    anchor = text.strip().lower()
    anchor = re.sub(r"[^\w\s-]", "", anchor)
    anchor = re.sub(r"\s+", "-", anchor)
    anchor = re.sub(r"-+", "-", anchor)
    return anchor.strip("-")


def seed_like_ref_requires_anchor(ref: object) -> bool:
    return isinstance(ref, str) and (
        ref.startswith("seed_bundle/seeds_")
        or ref.startswith("seed_templates/")
        or ref.startswith("seed_branches/")
        or ref.startswith("seed_soil/")
        or ref.startswith("seed_expansion/")
        or ref.startswith("archive/seed_bundle/seeds_")
        or ref.startswith("archive/seed_templates/")
        or ref.startswith("archive/seed_branches/")
        or ref.startswith("archive/seed_soil/")
        or ref.startswith("archive/seed_expansion/")
    )


def validate_ref(ref: str, label: str, *, require_anchor: bool = False, allow_directory: bool = False) -> None:
    if not isinstance(ref, str) or not ref:
        fail(f"{label}: ref must be a non-empty string")
    path_text, _, anchor = ref.partition("#")
    normalized_path = path_text.rstrip("/")
    target = ROOT / normalized_path
    if not target.exists():
        fail(f"{label}: referenced path does not exist: {ref}")
    if target.is_dir():
        if anchor:
            fail(f"{label}: directory refs cannot include anchors: {ref}")
        if not allow_directory:
            fail(f"{label}: directory refs are not allowed here: {ref}")
        return
    if anchor and target.suffix.lower() != ".md":
        fail(f"{label}: non-markdown refs cannot include anchors: {ref}")
    if require_anchor and target.suffix.lower() == ".md" and not anchor:
        fail(f"{label}: referenced markdown ref must include an explicit anchor: {ref}")
    if anchor and target.suffix.lower() == ".md" and anchor not in anchors_for(target):
        fail(f"{label}: referenced markdown anchor does not exist: {ref}")


def normalize_closure_status(raw_status: str) -> str:
    status = raw_status.strip().lower().replace("-", "_")
    aliases = {
        "archived": "archived_canonical",
    }
    return aliases.get(status, status)


def extract_closure_status(path: Path) -> str | None:
    match = CLOSURE_STATUS.search(path.read_text(encoding="utf-8"))
    if not match:
        return None
    return normalize_closure_status(match.group(1))


def require_mapping(value: object, label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or not value:
        fail(f"{label}: must be a non-empty mapping")
    return value


def require_nonempty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label}: must be a non-empty string")
    return value


def require_optional_string(value: object, label: str) -> str | None:
    if value is None:
        return None
    return require_nonempty_string(value, label)


def require_string_map(mapping: object, label: str) -> dict[str, str]:
    raw_mapping = require_mapping(mapping, label)
    normalized: dict[str, str] = {}
    for key, value in raw_mapping.items():
        if not isinstance(key, str) or not key:
            fail(f"{label}: keys must be non-empty strings")
        normalized[key] = require_nonempty_string(value, f"{label}.{key}")
    return normalized


def require_string_list(values: object, label: str, *, non_empty: bool = True) -> list[str]:
    if not isinstance(values, list):
        fail(f"{label}: must be a list")
    if non_empty and not values:
        fail(f"{label}: must not be empty")
    normalized: list[str] = []
    for index, value in enumerate(values):
        normalized.append(require_nonempty_string(value, f"{label}[{index}]"))
    return normalized


def require_bool(value: object, label: str) -> bool:
    if not isinstance(value, bool):
        fail(f"{label}: must be a boolean")
    return value


def require_optional_iso_date(value: object, label: str) -> str | None:
    if value is None:
        return None
    value = require_nonempty_string(value, label)
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(f"{label}: must be null or an ISO date string") from exc
    return value


def require_keys(mapping: dict[str, Any], label: str, keys: tuple[str, ...]) -> None:
    for key in keys:
        if key not in mapping:
            fail(f"{label}: missing required key '{key}'")


def iter_archived_seed_pack_dirs(root: Path) -> tuple[Path, ...]:
    archive_root = root / "archive"
    if not archive_root.exists():
        return ()
    return tuple(
        sorted(
            path
            for path in archive_root.iterdir()
            if path.is_dir() and ARCHIVED_SEED_PACK_DIR.match(path.name)
        )
    )


def collect_registry_trace_refs(payload: dict[str, Any]) -> set[str]:
    refs: set[str] = set()

    for ref in payload.get("origin_notes", ()):
        if isinstance(ref, str) and ref:
            refs.add(ref)

    for entry in payload.get("wave_index", ()):
        if not isinstance(entry, dict):
            continue
        supporting_notes = entry.get("supporting_notes")
        if isinstance(supporting_notes, list):
            for ref in supporting_notes:
                if isinstance(ref, str) and ref:
                    refs.add(ref)

    for entry in payload.get("seed_index", ()):
        if not isinstance(entry, dict):
            continue
        source_ref = entry.get("source_ref")
        if isinstance(source_ref, str) and source_ref:
            refs.add(source_ref)
        provenance = entry.get("provenance")
        if isinstance(provenance, dict):
            provenance_note = provenance.get("provenance_note")
            if isinstance(provenance_note, str) and provenance_note:
                refs.add(provenance_note)

    return refs


def validate_archived_seed_pack_traceability(payload: dict[str, Any], root: Path) -> None:
    trace_refs = collect_registry_trace_refs(payload)
    for pack_dir in iter_archived_seed_pack_dirs(root):
        pack_prefix = f"{pack_dir.relative_to(root).as_posix().rstrip('/')}/"
        if any(ref == pack_prefix.rstrip("/") or ref.startswith(pack_prefix) for ref in trace_refs):
            continue
        fail(
            f"{pack_prefix}: archived seed pack must be traceable from seed-registry.yaml "
            "via source_ref, provenance_note, origin_notes, or wave supporting_notes"
        )


def validate_archived_seed_pack_immutable_sources(root: Path) -> None:
    for pack_dir in iter_archived_seed_pack_dirs(root):
        for markdown_path in sorted(pack_dir.rglob("*.md")):
            for match in RAW_GITHUB_CONTENT_URL.finditer(markdown_path.read_text(encoding="utf-8")):
                revision = match.group("revision")
                if IMMUTABLE_GIT_REVISION.fullmatch(revision):
                    continue
                fail(
                    f"{markdown_path.relative_to(root).as_posix()}: archive seed packs must pin raw "
                    f"GitHub sources to immutable commit revisions, not '{revision}': {match.group(0)}"
                )


def collect_manifest_refs(manifest_path: Path) -> tuple[dict[str, Any], set[str], set[str]]:
    payload = load_json(manifest_path)
    if not isinstance(payload, dict):
        fail(f"{manifest_path.name}: manifest must be a JSON object")
    spec = MANIFEST_SPECS.get(manifest_path.name)
    if spec is None:
        fail(f"{manifest_path.name}: unsupported manifest surface")
    order_key = spec["order_key"]
    tail_keys = spec["tail_keys"]
    for key in ("canonical_sources", order_key, *tail_keys):
        if key not in payload:
            fail(f"{manifest_path.name}: missing required key '{key}'")

    refs: set[str] = set()
    order_refs: set[str] = set()

    refs.update(require_string_list(payload["canonical_sources"], f"{manifest_path.name}: canonical_sources"))
    order_items = payload[order_key]
    if not isinstance(order_items, list) or not order_items:
        fail(f"{manifest_path.name}: {order_key} must be a non-empty list")
    for index, item in enumerate(order_items):
        if not isinstance(item, dict):
            fail(f"{manifest_path.name}: {order_key}[{index}] must be an object")
        source_ref = item.get("source")
        if not isinstance(source_ref, str) or not source_ref:
            fail(f"{manifest_path.name}: {order_key}[{index}].source must be a non-empty string")
        refs.add(source_ref)
        order_refs.add(source_ref)
    for tail_key in tail_keys:
        refs.update(require_string_list(payload[tail_key], f"{manifest_path.name}: {tail_key}", non_empty=False))
    return payload, refs, order_refs


def validate_navigation(navigation: object) -> dict[str, Any]:
    mapping = require_mapping(navigation, "seed-registry.yaml: navigation")
    require_keys(mapping, "seed-registry.yaml: navigation", REQUIRED_NAVIGATION_KEYS)
    for key in ("canonical_order_source", "semantic_source", "registry_role"):
        require_nonempty_string(mapping[key], f"seed-registry.yaml: navigation.{key}")

    validate_ref(mapping["manifest_validator"], "seed-registry.yaml: navigation.manifest_validator")
    validate_ref(mapping["registry_validator"], "seed-registry.yaml: navigation.registry_validator")
    validate_ref(mapping["validation_entrypoint"], "seed-registry.yaml: navigation.validation_entrypoint")
    validate_ref(mapping["registry_contract"], "seed-registry.yaml: navigation.registry_contract")
    validate_ref(mapping["planting_report_template"], "seed-registry.yaml: navigation.planting_report_template")
    validate_ref(mapping["provenance_policy"], "seed-registry.yaml: navigation.provenance_policy")
    validate_ref(mapping["donor_capture_template"], "seed-registry.yaml: navigation.donor_capture_template")
    validate_ref(mapping["archived_root"], "seed-registry.yaml: navigation.archived_root", allow_directory=True)
    validate_ref(mapping["archived_pack"], "seed-registry.yaml: navigation.archived_pack", allow_directory=True)
    validate_ref(
        mapping["next_live_seed"],
        "seed-registry.yaml: navigation.next_live_seed",
        require_anchor=seed_like_ref_requires_anchor(mapping["next_live_seed"]),
    )
    return mapping


def validate_provenance(entry: dict[str, Any], index: int) -> str:
    label = f"seed-registry.yaml: seed_index[{index}].provenance"
    provenance = require_mapping(entry["provenance"], label)
    require_keys(provenance, label, PROVENANCE_KEYS)

    origin_mode = require_nonempty_string(provenance["origin_mode"], f"{label}.origin_mode")
    if origin_mode not in ALLOWED_ORIGIN_MODES:
        fail(f"{label}.origin_mode: must be one of {sorted(ALLOWED_ORIGIN_MODES)}")

    donor_repo = require_optional_string(provenance["donor_repo"], f"{label}.donor_repo")
    donor_ref = require_optional_string(provenance["donor_ref"], f"{label}.donor_ref")
    donor_license_spdx = require_optional_string(provenance["donor_license_spdx"], f"{label}.donor_license_spdx")
    donor_paths = require_string_list(provenance["donor_paths"], f"{label}.donor_paths", non_empty=False)
    provenance_note = require_optional_string(provenance["provenance_note"], f"{label}.provenance_note")

    if origin_mode == "native":
        if any(value is not None for value in (donor_repo, donor_ref, donor_license_spdx, provenance_note)):
            fail(f"{label}: native entries must keep donor repo/ref/license/note null")
        if donor_paths:
            fail(f"{label}: native entries must keep donor_paths empty")
    else:
        if donor_repo is None or donor_ref is None:
            fail(f"{label}: donor_derived and mixed entries must set donor_repo and donor_ref")
        if not donor_paths:
            fail(f"{label}: donor_derived and mixed entries must list at least one donor path")
        if provenance_note is None:
            fail(f"{label}: donor_derived and mixed entries must set provenance_note")
        validate_ref(provenance_note, f"{label}.provenance_note")

    return origin_mode


def validate_redistribution(entry: dict[str, Any], index: int, origin_mode: str) -> None:
    label = f"seed-registry.yaml: seed_index[{index}].redistribution"
    redistribution = require_mapping(entry["redistribution"], label)
    require_keys(redistribution, label, REDISTRIBUTION_KEYS)

    license_spdx = require_optional_string(redistribution["license_spdx"], f"{label}.license_spdx")
    upstream_license_ref = require_optional_string(
        redistribution["upstream_license_ref"],
        f"{label}.upstream_license_ref",
    )
    copy_license_required = require_bool(redistribution["copy_license_required"], f"{label}.copy_license_required")
    notice_required = require_bool(redistribution["notice_required"], f"{label}.notice_required")
    retain_attribution_required = require_bool(
        redistribution["retain_attribution_required"],
        f"{label}.retain_attribution_required",
    )
    mark_modifications_required = require_bool(
        redistribution["mark_modifications_required"],
        f"{label}.mark_modifications_required",
    )
    modified_from_upstream = require_bool(redistribution["modified_from_upstream"], f"{label}.modified_from_upstream")
    require_nonempty_string(redistribution["obligations_note"], f"{label}.obligations_note")

    if origin_mode == "native":
        if license_spdx is not None or upstream_license_ref is not None:
            fail(f"{label}: native entries must keep license_spdx and upstream_license_ref null")
        if any(
            (
                copy_license_required,
                notice_required,
                retain_attribution_required,
                mark_modifications_required,
                modified_from_upstream,
            )
        ):
            fail(f"{label}: native entries must keep redistribution booleans false")


def validate_transplant(entry: dict[str, Any], index: int, origin_mode: str) -> None:
    label = f"seed-registry.yaml: seed_index[{index}].transplant"
    transplant = require_mapping(entry["transplant"], label)
    require_keys(transplant, label, TRANSPLANT_KEYS)

    policy = require_nonempty_string(transplant["policy"], f"{label}.policy")
    if policy not in ALLOWED_TRANSPLANT_POLICIES:
        fail(f"{label}.policy: must be one of {sorted(ALLOWED_TRANSPLANT_POLICIES)}")

    require_string_list(transplant["what_survives"], f"{label}.what_survives")
    require_string_list(transplant["what_stays_behind"], f"{label}.what_stays_behind")
    require_string_list(transplant["non_goals"], f"{label}.non_goals")

    if origin_mode == "native" and policy != "native":
        fail(f"{label}: native entries must use transplant.policy='native'")
    if origin_mode != "native" and policy == "native":
        fail(f"{label}: donor-shaped entries must use a non-native transplant policy")


def validate_freshness(entry: dict[str, Any], index: int) -> str | None:
    freshness = entry.get("freshness")
    if freshness is None:
        return None

    label = f"seed-registry.yaml: seed_index[{index}].freshness"
    freshness_map = require_mapping(freshness, label)
    require_keys(freshness_map, label, FRESHNESS_KEYS)

    require_optional_iso_date(freshness_map["last_revalidated_at"], f"{label}.last_revalidated_at")
    revalidate_after_days = freshness_map["revalidate_after_days"]
    if revalidate_after_days is not None:
        if not isinstance(revalidate_after_days, int) or revalidate_after_days <= 0:
            fail(f"{label}.revalidate_after_days: must be null or a positive integer")

    return require_optional_string(freshness_map["superseded_by"], f"{label}.superseded_by")


def validate_registry() -> None:
    payload = load_yaml(REGISTRY_PATH)
    if not isinstance(payload, dict):
        fail("seed-registry.yaml: top level must be a mapping")
    validate_ref(CONTRACT_PATH.relative_to(ROOT).as_posix(), "seed-registry contract")

    for key in (
        "registry_version",
        "updated_at",
        "navigation",
        "lifecycle_states",
        "origin_notes",
        "wave_index",
        "seed_index",
    ):
        if key not in payload:
            fail(f"seed-registry.yaml: missing required key '{key}'")

    if payload["registry_version"] != REQUIRED_REGISTRY_VERSION:
        fail(f"seed-registry.yaml: registry_version must be {REQUIRED_REGISTRY_VERSION}")

    updated_at = payload["updated_at"]
    if not isinstance(updated_at, str):
        fail("seed-registry.yaml: updated_at must be an ISO date string")
    try:
        date.fromisoformat(updated_at)
    except ValueError as exc:
        raise ValidationError("seed-registry.yaml: updated_at must be an ISO date string") from exc

    navigation = validate_navigation(payload["navigation"])

    lifecycle_states = require_string_map(payload["lifecycle_states"], "seed-registry.yaml: lifecycle_states")
    for key in ("archived_canonical", "pending_archive", "gated_next", "landed_post_wave"):
        if key not in lifecycle_states:
            fail(f"seed-registry.yaml: lifecycle_states is missing required key '{key}'")

    for index, ref in enumerate(require_string_list(payload["origin_notes"], "seed-registry.yaml: origin_notes", non_empty=False)):
        validate_ref(ref, f"seed-registry.yaml: origin_notes[{index}]")

    wave_index = payload["wave_index"]
    if not isinstance(wave_index, list) or not wave_index:
        fail("seed-registry.yaml: wave_index must be a non-empty list")

    wave_status_by_name: dict[str, str] = {}
    manifest_refs_by_wave: dict[str, set[str]] = {}
    manifest_order_refs_by_wave: dict[str, set[str]] = {}

    for index, entry in enumerate(wave_index):
        if not isinstance(entry, dict):
            fail(f"seed-registry.yaml: wave_index[{index}] must be an object")
        for key in ("wave", "file", "mode", "registry_status", "summary"):
            if key not in entry:
                fail(f"seed-registry.yaml: wave_index[{index}] is missing required key '{key}'")
        wave_name = entry["wave"]
        if not isinstance(wave_name, str) or not wave_name:
            fail(f"seed-registry.yaml: wave_index[{index}].wave must be a non-empty string")
        if wave_name in wave_status_by_name:
            fail(f"seed-registry.yaml: duplicate wave entry '{wave_name}'")
        manifest_ref = entry["file"]
        validate_ref(manifest_ref, f"seed-registry.yaml: wave_index[{index}].file")
        expected_wave_name = Path(manifest_ref).name.removesuffix(".manifest.json")
        if wave_name != expected_wave_name:
            fail(
                f"seed-registry.yaml: wave_index[{index}].wave '{wave_name}' does not match manifest filename '{manifest_ref}'"
            )
        if entry["registry_status"] not in lifecycle_states:
            fail(
                f"seed-registry.yaml: wave_index[{index}].registry_status '{entry['registry_status']}' is not defined in lifecycle_states"
            )
        manifest_payload, manifest_refs, order_refs = collect_manifest_refs(ROOT / manifest_ref)
        manifest_mode = manifest_payload.get("mode")
        if manifest_mode != entry["mode"]:
            fail(
                f"seed-registry.yaml: wave_index[{index}].mode '{entry['mode']}' does not match {manifest_ref} mode '{manifest_mode}'"
            )
        if "closure_note" in entry:
            validate_ref(entry["closure_note"], f"seed-registry.yaml: wave_index[{index}].closure_note")
            closure_status = extract_closure_status(ROOT / entry["closure_note"])
            if closure_status and closure_status != entry["registry_status"]:
                fail(
                    f"seed-registry.yaml: wave_index[{index}].registry_status '{entry['registry_status']}' conflicts with closure note status '{closure_status}'"
                )
        if "supporting_notes" in entry:
            notes = require_string_list(
                entry["supporting_notes"],
                f"seed-registry.yaml: wave_index[{index}].supporting_notes",
                non_empty=False,
            )
            for note_index, note_ref in enumerate(notes):
                validate_ref(note_ref, f"seed-registry.yaml: wave_index[{index}].supporting_notes[{note_index}]")
        if "landed_to" in entry:
            require_string_list(entry["landed_to"], f"seed-registry.yaml: wave_index[{index}].landed_to")
        require_nonempty_string(entry["summary"], f"seed-registry.yaml: wave_index[{index}].summary")
        wave_status_by_name[wave_name] = entry["registry_status"]
        manifest_refs_by_wave[wave_name] = manifest_refs
        manifest_order_refs_by_wave[wave_name] = order_refs

    seed_index = payload["seed_index"]
    if not isinstance(seed_index, list) or not seed_index:
        fail("seed-registry.yaml: seed_index must be a non-empty list")

    seen_seed_ids: set[str] = set()
    seen_gated_next_refs: set[str] = set()
    registry_order_refs_by_wave: dict[str, set[str]] = {wave: set() for wave in wave_status_by_name}
    freshness_supersessions: list[tuple[str, str]] = []
    allowed_null_wave_statuses = {"gated_next", "landed_post_wave"}

    for index, entry in enumerate(seed_index):
        if not isinstance(entry, dict):
            fail(f"seed-registry.yaml: seed_index[{index}] must be an object")
        for key in (
            "registry_id",
            "label",
            "source_ref",
            "wave",
            "projects",
            "kind",
            "registry_status",
            "parent_seed",
            "repo_homes",
            "first_artifact_hint",
            "notes",
            "provenance",
            "redistribution",
            "transplant",
        ):
            if key not in entry:
                fail(f"seed-registry.yaml: seed_index[{index}] is missing required key '{key}'")
        registry_id = require_nonempty_string(entry["registry_id"], f"seed-registry.yaml: seed_index[{index}].registry_id")
        if registry_id in seen_seed_ids:
            fail(f"seed-registry.yaml: duplicate registry_id '{registry_id}'")
        seen_seed_ids.add(registry_id)

        for key in ("label", "kind", "first_artifact_hint", "notes"):
            require_nonempty_string(entry[key], f"seed-registry.yaml: seed_index[{index}].{key}")
        if entry["registry_status"] not in lifecycle_states:
            fail(
                f"seed-registry.yaml: seed_index[{index}].registry_status '{entry['registry_status']}' is not defined in lifecycle_states"
            )

        if entry["parent_seed"] is not None:
            require_nonempty_string(entry["parent_seed"], f"seed-registry.yaml: seed_index[{index}].parent_seed")

        require_string_list(entry["projects"], f"seed-registry.yaml: seed_index[{index}].projects")
        require_string_list(entry["repo_homes"], f"seed-registry.yaml: seed_index[{index}].repo_homes")

        source_ref = entry["source_ref"]
        validate_ref(
            source_ref,
            f"seed-registry.yaml: seed_index[{index}].source_ref",
            require_anchor=seed_like_ref_requires_anchor(source_ref),
        )

        wave_name = entry["wave"]
        if wave_name is None:
            if entry["registry_status"] not in allowed_null_wave_statuses:
                fail(
                    "seed-registry.yaml: "
                    f"seed_index[{index}] has wave=null but registry_status '{entry['registry_status']}' "
                    "instead of one of: gated_next, landed_post_wave"
                )
            if entry["registry_status"] == "gated_next":
                seen_gated_next_refs.add(source_ref)
        else:
            require_nonempty_string(wave_name, f"seed-registry.yaml: seed_index[{index}].wave")
            if wave_name not in wave_status_by_name:
                fail(f"seed-registry.yaml: seed_index[{index}].wave '{wave_name}' is not present in wave_index")
            if source_ref not in manifest_refs_by_wave[wave_name]:
                fail(
                    f"seed-registry.yaml: seed_index[{index}].source_ref '{source_ref}' is not traceable to {wave_name}.manifest.json"
                )
            if entry["registry_status"] != wave_status_by_name[wave_name]:
                fail(
                    f"seed-registry.yaml: seed_index[{index}].registry_status '{entry['registry_status']}' does not match wave_index status '{wave_status_by_name[wave_name]}' for wave '{wave_name}'"
                )
            registry_order_refs_by_wave[wave_name].add(source_ref)

        origin_mode = validate_provenance(entry, index)
        validate_redistribution(entry, index, origin_mode)
        validate_transplant(entry, index, origin_mode)
        superseded_by = validate_freshness(entry, index)
        if superseded_by is not None:
            if superseded_by == registry_id:
                fail(f"seed-registry.yaml: seed_index[{index}].freshness.superseded_by must not point to itself")
            freshness_supersessions.append((registry_id, superseded_by))

    next_live_seed = navigation["next_live_seed"]
    if next_live_seed not in seen_gated_next_refs:
        fail(
            "seed-registry.yaml: navigation.next_live_seed must match a seed_index entry with registry_status 'gated_next'"
        )

    for current_id, superseded_by in freshness_supersessions:
        if superseded_by not in seen_seed_ids:
            fail(
                f"seed-registry.yaml: entry '{current_id}' points freshness.superseded_by to unknown registry_id '{superseded_by}'"
            )

    validate_archived_seed_pack_traceability(payload, ROOT)
    validate_archived_seed_pack_immutable_sources(ROOT)

    for wave_name, order_refs in manifest_order_refs_by_wave.items():
        missing = sorted(order_refs - registry_order_refs_by_wave[wave_name])
        if missing:
            joined = ", ".join(missing)
            fail(f"seed-registry.yaml: wave '{wave_name}' is missing registry coverage for order refs: {joined}")


def main() -> int:
    try:
        validate_registry()
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    print("[ok] validated seed-registry.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
