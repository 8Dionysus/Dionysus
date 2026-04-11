from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

ROOT_MARKERS = (
    "seed-registry.yaml",
    "generated/seed_route_map.min.json",
    "docs/codex/planting-protocol.md",
)

ALLOWED_ROOT_FILES = {
    "AGENTS.md",
    "README.md",
    "QUESTBOOK.md",
    "seed-registry.yaml",
}

ALLOWED_PREFIXES = (
    "archive/",
    "docs/",
    "generated/",
    "reports/",
    "schema/",
    "schemas/",
    "seed_expansion/",
    "seed_staging/",
    "templates/",
    "quests/",
)

MANIFEST_NAME = re.compile(r"^[a-z0-9_]+_wave\.manifest\.json$")


class RepoStateError(RuntimeError):
    """Raised when the repo state is invalid or the requested surface is unsafe."""


@dataclass(slots=True)
class TextSurface:
    ref: str
    path: str
    anchor: str | None
    anchor_found: bool
    mode: str
    excerpt: str
    line_count: int

    def as_dict(self) -> dict[str, Any]:
        return {
            "ref": self.ref,
            "path": self.path,
            "anchor": self.anchor,
            "anchor_found": self.anchor_found,
            "mode": self.mode,
            "excerpt": self.excerpt,
            "line_count": self.line_count,
        }


@dataclass(slots=True)
class DionysusRepoState:
    repo_root: Path

    @classmethod
    def discover(cls, start_path: str | Path | None = None) -> "DionysusRepoState":
        env_root = os.getenv("DIONYSUS_REPO_ROOT")
        if env_root:
            candidate = Path(env_root).expanduser().resolve()
            cls._validate_repo_root(candidate)
            return cls(repo_root=candidate)

        start = Path(start_path or Path.cwd()).resolve()
        candidates = [start, *start.parents]
        for candidate in candidates:
            try:
                cls._validate_repo_root(candidate)
            except RepoStateError:
                continue
            return cls(repo_root=candidate)
        joined = ", ".join(ROOT_MARKERS)
        raise RepoStateError(
            f"Could not discover Dionysus repo root from {start}. Missing markers: {joined}"
        )

    @staticmethod
    def _validate_repo_root(candidate: Path) -> None:
        missing = [marker for marker in ROOT_MARKERS if not (candidate / marker).exists()]
        if missing:
            raise RepoStateError(
                f"{candidate} does not look like Dionysus; missing required files: {', '.join(missing)}"
            )

    def load_route_map(self) -> dict[str, Any]:
        return self._load_json("generated/seed_route_map.min.json")

    def load_registry(self) -> dict[str, Any]:
        raw = self._read_text_file("seed-registry.yaml")
        data = yaml.safe_load(raw) or {}
        if not isinstance(data, dict):
            raise RepoStateError("seed-registry.yaml did not parse into a mapping")
        return data

    def build_registry_navigation(self) -> dict[str, Any]:
        registry = self.load_registry()
        navigation = registry.get("navigation", {})
        wave_index = registry.get("wave_index", [])
        lifecycle_states = registry.get("lifecycle_states", {})
        return {
            "registry_version": registry.get("registry_version"),
            "updated_at": registry.get("updated_at"),
            "navigation": {
                "canonical_order_source": navigation.get("canonical_order_source"),
                "semantic_source": navigation.get("semantic_source"),
                "validation_entrypoint": navigation.get("validation_entrypoint"),
                "registry_contract": navigation.get("registry_contract"),
                "next_live_seed": navigation.get("next_live_seed"),
                "archived_root": navigation.get("archived_root"),
                "archived_pack": navigation.get("archived_pack"),
            },
            "lifecycle_states": lifecycle_states,
            "wave_index": wave_index,
            "counts": {
                "origin_notes": len(registry.get("origin_notes", [])),
                "waves": len(wave_index),
                "seed_entries": len(registry.get("seed_index", [])),
            },
        }

    def load_next_live_seed(self, mode: str = "preview", limit: int = 40) -> dict[str, Any]:
        registry = self.load_registry()
        route_map = self.load_route_map()
        next_ref = registry.get("navigation", {}).get("next_live_seed")
        if not isinstance(next_ref, str) or not next_ref:
            raise RepoStateError("seed-registry.yaml is missing navigation.next_live_seed")

        route_hint = None
        for route in route_map.get("routes", []):
            if route.get("route_id") == "next-live-seed":
                route_hint = route
                break

        registry_entry = None
        for entry in registry.get("seed_index", []):
            if entry.get("source_ref") == next_ref or entry.get("registry_status") == "gated_next":
                registry_entry = entry
                if entry.get("source_ref") == next_ref:
                    break

        surface = self.read_text_ref(next_ref, mode=mode, limit=limit)
        return {
            "next_live_seed_ref": next_ref,
            "route_hint": route_hint,
            "registry_entry": registry_entry,
            "surface": surface.as_dict(),
            "warning": (
                "Start from the live seed and the owner repo before reading staging notes. "
                "Dionysus keeps lineage and dispatch, not final target-repo doctrine."
            ),
        }

    def load_wave_context(self, wave: str) -> dict[str, Any]:
        registry = self.load_registry()
        wave_key = self._normalize_wave(wave)
        wave_entry = next(
            (entry for entry in registry.get("wave_index", []) if entry.get("wave") == wave_key),
            None,
        )
        if wave_entry is None:
            raise RepoStateError(f"Unknown wave: {wave}")

        manifest_file = wave_entry.get("file")
        if not isinstance(manifest_file, str):
            raise RepoStateError(f"Wave {wave_key} is missing its manifest file")
        manifest = self._load_json(manifest_file)

        ordered_lists: dict[str, list[dict[str, Any]]] = {}
        for key, value in manifest.items():
            if key.endswith("_order") and isinstance(value, list):
                ordered_lists[key] = value

        closure_preview = None
        closure_note = wave_entry.get("closure_note")
        if isinstance(closure_note, str) and closure_note:
            closure_preview = self.read_text_ref(closure_note, mode="preview", limit=24).as_dict()

        return {
            "wave": wave_key,
            "wave_entry": wave_entry,
            "manifest_file": manifest_file,
            "manifest": manifest,
            "ordered_lists": ordered_lists,
            "closure_preview": closure_preview,
            "supporting_notes": manifest.get("supporting_notes", []),
        }

    def load_registry_entry(
        self,
        registry_id: str,
        mode: str = "preview",
        limit: int = 32,
    ) -> dict[str, Any]:
        registry = self.load_registry()
        entry = next(
            (item for item in registry.get("seed_index", []) if item.get("registry_id") == registry_id),
            None,
        )
        if entry is None:
            raise RepoStateError(f"Unknown registry id: {registry_id}")

        source_ref = entry.get("source_ref")
        source_preview = None
        if isinstance(source_ref, str) and source_ref:
            source_preview = self.read_text_ref(source_ref, mode=mode, limit=limit).as_dict()
        return {
            "registry_entry": entry,
            "source_preview": source_preview,
        }

    def load_staging_note(
        self,
        note_path: str,
        mode: str = "preview",
        limit: int = 40,
    ) -> dict[str, Any]:
        normalized = self._normalize_ref(note_path)
        if not normalized.startswith("seed_staging/"):
            raise RepoStateError("seed_staging notes must stay under seed_staging/")

        text = self._read_text_file(normalized)
        frontmatter, _body = self._extract_frontmatter(text)
        surface = self.read_text_ref(normalized, mode=mode, limit=limit)
        lifecycle_markers = {
            key: frontmatter.get(key)
            for key in ("lifecycle_status", "lifecycle_note", "reality_checked_at")
            if key in frontmatter
        }
        return {
            "note_path": normalized,
            "lifecycle_markers": lifecycle_markers,
            "surface": surface.as_dict(),
            "warning": (
                "Staging truth is weaker than owner-repo planting truth. "
                "Use this note as lineage or staging guidance, then verify the owner repo directly."
            ),
        }

    def build_planting_rules_bundle(self) -> dict[str, Any]:
        refs = [
            "AGENTS.md",
            "docs/SEED_SURFACE_MAP.md",
            "docs/codex/planting-protocol.md",
            "docs/codex/owner-repo-reality-check.md",
            "docs/codex/AGENTS.md",
            "reports/planting/README.md",
            "reports/planting/AGENTS.md",
            "seed_expansion/AGENTS.md",
            "archive/AGENTS.md",
        ]
        previews = [self.read_text_ref(ref, mode="preview", limit=28).as_dict() for ref in refs]
        return {
            "source_refs": refs,
            "read_order": [
                "relevant *_wave.manifest.json or the current live seed",
                "exact source seed named by that surface",
                "closure note when one exists",
                "seed-registry.yaml",
                "docs/codex/planting-protocol.md",
                "owner repo structure and ownership",
                "seed_staging/... only when staging or lineage replay is still the real task",
            ],
            "stop_rule": (
                "Stop at docs, schemas, contracts, and notes when planting would touch secrets, "
                "destructive writes, silent policy shifts, hidden side effects, or vendor-locked canon."
            ),
            "bundle": previews,
        }

    def load_quest_followthrough(self) -> dict[str, Any]:
        catalog = self._load_json("generated/quest_catalog.min.json")
        dispatch = self._load_json("generated/quest_dispatch.min.json")
        questbook = self.read_text_ref("QUESTBOOK.md", mode="preview", limit=24).as_dict()
        return {
            "questbook": questbook,
            "quest_catalog": catalog,
            "quest_dispatch": dispatch,
            "warning": (
                "Quest surfaces here are seed-garden follow-through. "
                "They must not outrank manifests, closure notes, registry state, or owner-repo reality."
            ),
        }

    def read_text_ref(self, ref: str, mode: str = "preview", limit: int = 40) -> TextSurface:
        if mode not in {"preview", "full"}:
            raise RepoStateError("mode must be 'preview' or 'full'")

        path_ref, anchor = self._split_ref(ref)
        normalized = self._normalize_ref(path_ref)
        text = self._read_text_file(normalized)
        lines = text.splitlines()
        anchor_found = False
        excerpt = text

        if mode == "preview":
            if anchor:
                anchor_line = self._find_anchor_line(lines, anchor)
                if anchor_line is not None:
                    anchor_found = True
                    excerpt_lines = lines[anchor_line : anchor_line + max(limit, 1)]
                else:
                    excerpt_lines = lines[: max(limit, 1)]
            else:
                excerpt_lines = lines[: max(limit, 1)]
            excerpt = "\n".join(excerpt_lines)
        elif anchor:
            anchor_found = self._find_anchor_line(lines, anchor) is not None

        return TextSurface(
            ref=ref,
            path=normalized,
            anchor=anchor,
            anchor_found=anchor_found,
            mode=mode,
            excerpt=excerpt,
            line_count=len(lines),
        )

    def _load_json(self, ref: str) -> Any:
        text = self._read_text_file(ref)
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise RepoStateError(f"Invalid JSON at {ref}: {exc}") from exc

    def _read_text_file(self, ref: str) -> str:
        path = self.repo_root / self._normalize_ref(ref)
        if not path.exists():
            raise RepoStateError(f"Missing surface: {ref}")
        return path.read_text(encoding="utf-8")

    def _normalize_wave(self, wave: str) -> str:
        normalized = wave.strip()
        if not normalized:
            raise RepoStateError("wave cannot be empty")
        if normalized.endswith(".manifest.json"):
            normalized = normalized[: -len(".manifest.json")]
        if normalized.endswith("_wave"):
            return normalized
        if normalized.isidentifier() or re.match(r"^[a-z0-9_]+$", normalized):
            return f"{normalized}_wave"
        return normalized

    def _normalize_ref(self, ref: str) -> str:
        candidate = ref.strip()
        if not candidate:
            raise RepoStateError("surface ref cannot be empty")
        if candidate.startswith("/"):
            raise RepoStateError("absolute paths are not allowed")
        if ".." in Path(candidate).parts:
            raise RepoStateError("parent path traversal is not allowed")
        if candidate in ALLOWED_ROOT_FILES:
            return candidate
        if MANIFEST_NAME.match(Path(candidate).name):
            return candidate
        if candidate.endswith(".closure.md"):
            return candidate
        if candidate.startswith(ALLOWED_PREFIXES):
            return candidate
        raise RepoStateError(f"Ref is outside the allowed Dionysus surface set: {ref}")

    def _split_ref(self, ref: str) -> tuple[str, str | None]:
        if "#" in ref:
            path_ref, anchor = ref.split("#", 1)
            return path_ref, anchor or None
        return ref, None

    def _extract_frontmatter(self, text: str) -> tuple[dict[str, Any], str]:
        if not text.startswith("---\n"):
            return {}, text
        end = text.find("\n---\n", 4)
        if end == -1:
            return {}, text
        raw = text[4:end]
        body = text[end + 5 :]
        data = yaml.safe_load(raw) or {}
        if not isinstance(data, dict):
            return {}, text
        return data, body

    def _find_anchor_line(self, lines: list[str], anchor: str) -> int | None:
        if not anchor:
            return None
        canonical = self._slugify(anchor)
        for idx, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("#"):
                heading = stripped.lstrip("#").strip()
                if self._slugify(heading) == canonical:
                    return idx
            if canonical and canonical in self._slugify(stripped):
                return idx
        return None

    def _slugify(self, value: str) -> str:
        lowered = value.strip().lower()
        lowered = re.sub(r"[`*_{}\[\]()#+.!?<>:;'/\\|\"]", "", lowered)
        lowered = re.sub(r"\s+", "-", lowered)
        lowered = re.sub(r"-+", "-", lowered)
        return lowered.strip("-")
