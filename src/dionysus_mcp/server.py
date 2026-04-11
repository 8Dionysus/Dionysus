from __future__ import annotations

import json
import logging
from typing import Any

from dionysus_mcp.repo_state import DionysusRepoState

LOGGER = logging.getLogger(__name__)


def build_server() -> Any:
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency 'mcp'. Install with: python -m pip install -r requirements-mcp.txt"
        ) from exc

    state = DionysusRepoState.discover()
    mcp = FastMCP("dionysus", json_response=True)

    @mcp.tool()
    def seed_route_catalog() -> dict[str, Any]:
        """Return the compact Dionysus route-entry capsule."""
        return state.load_route_map()

    @mcp.tool()
    def seed_registry_navigation() -> dict[str, Any]:
        """Return the compact navigation view from seed-registry.yaml."""
        return state.build_registry_navigation()

    @mcp.tool()
    def seed_next_live(mode: str = "preview", limit: int = 40) -> dict[str, Any]:
        """Return the current next live seed with route hints and a text preview."""
        return state.load_next_live_seed(mode=mode, limit=limit)

    @mcp.tool()
    def seed_wave_context(wave: str) -> dict[str, Any]:
        """Return one wave context by wave name."""
        return state.load_wave_context(wave=wave)

    @mcp.tool()
    def seed_registry_entry(
        registry_id: str,
        mode: str = "preview",
        limit: int = 32,
    ) -> dict[str, Any]:
        """Return one registry entry and a small preview of its source seed."""
        return state.load_registry_entry(registry_id=registry_id, mode=mode, limit=limit)

    @mcp.tool()
    def seed_staging_note(
        note_path: str,
        mode: str = "preview",
        limit: int = 40,
    ) -> dict[str, Any]:
        """Return one staging note with lifecycle markers and a reality-check warning."""
        return state.load_staging_note(note_path=note_path, mode=mode, limit=limit)

    @mcp.tool()
    def seed_planting_rules() -> dict[str, Any]:
        """Return the compact planting-rule bundle for Dionysus."""
        return state.build_planting_rules_bundle()

    @mcp.tool()
    def seed_quest_followthrough() -> dict[str, Any]:
        """Return the compact quest follow-through bundle for Dionysus."""
        return state.load_quest_followthrough()

    @mcp.resource("dionysus://route-map")
    def route_map_resource() -> str:
        return json.dumps(state.load_route_map(), ensure_ascii=False, indent=2)

    @mcp.resource("dionysus://registry/navigation")
    def registry_navigation_resource() -> str:
        return json.dumps(state.build_registry_navigation(), ensure_ascii=False, indent=2)

    @mcp.resource("dionysus://next-live-seed")
    def next_live_seed_resource() -> str:
        return json.dumps(
            state.load_next_live_seed(mode="preview", limit=40),
            ensure_ascii=False,
            indent=2,
        )

    @mcp.resource("dionysus://wave/{wave}")
    def wave_resource(wave: str) -> str:
        return json.dumps(state.load_wave_context(wave=wave), ensure_ascii=False, indent=2)

    @mcp.resource("dionysus://registry/{registry_id}")
    def registry_entry_resource(registry_id: str) -> str:
        return json.dumps(
            state.load_registry_entry(registry_id=registry_id),
            ensure_ascii=False,
            indent=2,
        )

    @mcp.resource("dionysus://planting-rules")
    def planting_rules_resource() -> str:
        return json.dumps(state.build_planting_rules_bundle(), ensure_ascii=False, indent=2)

    @mcp.resource("dionysus://questbook")
    def questbook_resource() -> str:
        return json.dumps(state.load_quest_followthrough(), ensure_ascii=False, indent=2)

    @mcp.prompt()
    def open_next_live_seed(target_repo: str = "") -> str:
        """Prompt recipe for opening the live seed without collapsing staging and ownership."""
        target_tail = (
            f" After reading it, verify the owner repo directly: {target_repo}."
            if target_repo
            else " After reading it, verify the owner repo directly before doing staging work."
        )
        return (
            "Use seed_route_catalog, then seed_registry_navigation, then seed_next_live. "
            "Treat the live seed and its owner repo as stronger than staging notes." + target_tail
        )

    @mcp.prompt()
    def reality_check_staging_note(note_path: str, target_repo: str = "") -> str:
        """Prompt recipe for staging-note reality checks."""
        target_tail = (
            f" Verify the owner repo directly: {target_repo}."
            if target_repo
            else " Verify the owner repo directly afterward."
        )
        return (
            f"Use seed_staging_note(note_path='{note_path}'), then seed_planting_rules. "
            "Treat lifecycle markers as guidance only, not as sovereignty." + target_tail
        )

    @mcp.prompt()
    def prepare_seed_planting(target_repo: str, registry_id: str) -> str:
        """Prompt recipe for preparing one planting slice."""
        return (
            f"Use seed_registry_entry(registry_id='{registry_id}'), then seed_planting_rules. "
            f"Verify the target repo directly: {target_repo}. "
            "Name the smallest coherent landing slice, one structural artifact, the validation surface, and the explicit non-goals."
        )

    LOGGER.info("Dionysus MCP server ready at repo root: %s", state.repo_root)
    return mcp


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    server = build_server()
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
