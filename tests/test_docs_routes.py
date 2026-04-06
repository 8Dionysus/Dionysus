from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_readme_start_here_surfaces_closure_note_and_owner_repo_before_agents() -> None:
    readme = read_text("README.md")

    closure_step = "3. the matching closure note for that wave when one exists"
    registry_step = "4. `seed-registry.yaml`"
    owner_step = "6. the target repository structure and ownership"
    agents_step = "7. `AGENTS.md` and the nearest nested `AGENTS.md`"

    assert closure_step in readme
    assert registry_step in readme
    assert owner_step in readme
    assert agents_step in readme
    assert readme.index(closure_step) < readme.index(registry_step)
    assert readme.index(owner_step) < readme.index(agents_step)


def test_readme_lists_current_validation_and_lineage_routes() -> None:
    readme = read_text("README.md")

    assert "python scripts/validate_seed_surfaces.py" in readme
    assert "python -m pytest -q tests" in readme
    assert "`archive/seed_pack_exports/` holds derived ingress and transport bundles only" in readme
    assert "`reports/planting/README.md` explains when Dionysus should keep durable planting trace" in readme


def test_agents_mentions_pytest_reinforcement() -> None:
    agents = read_text("AGENTS.md")

    assert "python scripts/validate_seed_surfaces.py" in agents
    assert "python -m pytest -q tests" in agents


def test_seed_surface_map_softens_root_wording_and_marks_seed_pack_exports_derived() -> None:
    surface_map = read_text("docs/SEED_SURFACE_MAP.md")

    assert "canonical navigation and live lifecycle surfaces" in surface_map
    assert "live control surfaces" not in surface_map
    assert "Within `archive/`, treat `archive/seed_pack_exports/` as derived ingress and" in surface_map
    assert "transport only, not as canonical seed meaning." in surface_map
