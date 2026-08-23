#!/usr/bin/env python3
"""Owner-local release gate for the Dionysus source-only alpha."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE_VERSION = "0.4.0-alpha.1"
RELEASE_TAG = f"v{RELEASE_VERSION}"
BASELINE_TAG = "v0.3.0"
BASELINE_COMMIT = "72031c63ffc296550777ff7db1a86e29f94f6768"
PRODUCT_FIRST_PARENT = (
    "8529c00c731ce560c0d8d2719fabbaf9dcbe222e",
    "209cc4888be3896d5da6db1d25ca0ac42bb45786",
    "6c463f6b89a11e85b37e2606525afc7d45005fbd",
    "8c5c8ec960c507e097b37472e9e8353c369919bf",
    "b2ed9208e5712e45be4eb08d65ed60826c745170",
)
REQUIRED_HEADINGS = (
    "Summary",
    "Added",
    "Changed",
    "Fixed",
    "Deprecated",
    "Removed",
    "Security",
    "Compatibility and Migration",
    "Deployment, Observability, Recovery, and Rollback",
    "Artifacts, Attestation, and Admission",
    "Validation",
    "First-Parent Reconciliation (5/5)",
    "Notes",
)
MEDIA_SUFFIXES = {".aac", ".flac", ".m4a", ".mp3", ".mp4", ".ogg", ".opus", ".wav", ".webm"}


class ReleaseGateError(RuntimeError):
    """A fail-closed owner release gate error."""


@dataclass(frozen=True)
class ReleaseSection:
    version: str
    tag: str
    date: str
    body: str
    summary_bullets: tuple[str, ...]


def run(command: list[str], *, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.setdefault("PYTHONDONTWRITEBYTECODE", "1")
    return subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        input=input_text,
        capture_output=True,
        text=True,
    )


def command_detail(result: subprocess.CompletedProcess[str]) -> str:
    return result.stderr.strip() or result.stdout.strip() or "no command output"


def output(command: list[str]) -> str:
    result = run(command)
    if result.returncode != 0:
        raise ReleaseGateError(f"{' '.join(command)}\n{command_detail(result)}")
    return result.stdout.strip()


def fail(message: str) -> None:
    raise ReleaseGateError(message)


def _section_body(body: str, heading: str) -> str | None:
    match = re.search(rf"^### {re.escape(heading)}\s*$", body, re.M)
    if match is None:
        return None
    next_heading = re.search(r"^### ", body[match.end() :], re.M)
    end = match.end() + next_heading.start() if next_heading else len(body)
    return body[match.end() : end].strip()


def _bullets(section: str | None) -> tuple[str, ...]:
    if not section:
        return ()
    values: list[str] = []
    current: str | None = None
    for raw_line in section.splitlines():
        line = raw_line.rstrip()
        if line.startswith("- "):
            if current is not None:
                values.append(current)
            current = line[2:].strip()
        elif current is not None and line.strip():
            current = f"{current} {line.strip()}"
    if current is not None:
        values.append(current)
    return tuple(values)


def extract_release_section(changelog: str, version: str = RELEASE_VERSION) -> ReleaseSection:
    pattern = re.compile(rf"^## \[{re.escape(version)}\] - (?P<date>\d{{4}}-\d{{2}}-\d{{2}})\s*$", re.M)
    match = pattern.search(changelog)
    if match is None:
        fail(f"CHANGELOG.md is missing a dated [{version}] section")
    next_heading = re.search(r"^## \[", changelog[match.end() :], re.M)
    end = match.end() + next_heading.start() if next_heading else len(changelog)
    body = changelog[match.end() : end].strip()
    summary = _bullets(_section_body(body, "Summary"))
    return ReleaseSection(
        version=version,
        tag=f"v{version}",
        date=match.group("date"),
        body=body,
        summary_bullets=summary,
    )


def build_release_body(section: ReleaseSection) -> str:
    highlights = "\n".join(f"- {item}" for item in section.summary_bullets)
    return (
        f"Released: {section.date}\n\n"
        "Canonical changelog: [CHANGELOG.md](https://github.com/8Dionysus/Dionysus/blob/main/CHANGELOG.md)\n\n"
        f"## Highlights\n{highlights}\n\n"
        f"## Full Release Notes\n{section.body}\n"
    )


def _clean_status() -> str:
    return output(["git", "status", "--porcelain", "--untracked-files=all"])


def verify_release_surfaces() -> ReleaseSection:
    changelog_path = ROOT / "CHANGELOG.md"
    if not changelog_path.is_file():
        fail("CHANGELOG.md is missing")
    changelog = changelog_path.read_text(encoding="utf-8")
    if "## [Unreleased]" not in changelog:
        fail("CHANGELOG.md must retain [Unreleased]")
    section = extract_release_section(changelog)
    if not section.summary_bullets:
        fail("release section must contain Summary bullets")
    for heading in REQUIRED_HEADINGS:
        if _section_body(section.body, heading) is None:
            fail(f"release section is missing ### {heading}")

    banner = f"> Current release: `{RELEASE_TAG}`. See [CHANGELOG](CHANGELOG.md) for release notes."
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if banner not in readme:
        fail("README.md is missing the exact current-release banner")
    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    if f"Current release line: `{RELEASE_TAG}`" not in roadmap:
        fail("ROADMAP.md is missing the current release line")
    releasing = (ROOT / "docs" / "RELEASING.md").read_text(encoding="utf-8")
    for phrase in ("source-only prerelease", "scripts/release_publish.py", "aoa release"):
        if phrase not in releasing:
            fail(f"docs/RELEASING.md is missing {phrase!r}")

    actual_product_commits = tuple(
        output(["git", "rev-list", "--first-parent", "--reverse", f"{BASELINE_TAG}..HEAD^"]).splitlines()
    )
    if actual_product_commits != PRODUCT_FIRST_PARENT:
        fail(
            "first-parent product range drifted: "
            f"expected {list(PRODUCT_FIRST_PARENT)}, got {list(actual_product_commits)}"
        )
    if output(["git", "rev-parse", BASELINE_COMMIT]) != BASELINE_COMMIT:
        fail("release baseline commit is not present")

    release_commit_paths = output(["git", "diff", "--name-only", "HEAD^", "HEAD"]).splitlines()
    if any(path.startswith("legacy/") for path in release_commit_paths):
        fail("release-preparation commit must not rewrite legacy/")
    if any(path.startswith("aoa-session-memory") for path in release_commit_paths):
        fail("release-preparation commit must not touch protected session-memory paths")

    tracked_vault = set(output(["git", "ls-files", "vault"]).splitlines())
    if tracked_vault - {"vault/README.md"}:
        fail(f"private vault contains tracked material: {sorted(tracked_vault)}")
    tracked_media = sorted(
        path for path in output(["git", "ls-files"]).splitlines() if Path(path).suffix.lower() in MEDIA_SUFFIXES
    )
    if tracked_media:
        fail(f"personal media is tracked: {tracked_media}")
    secret_pattern = r"sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|BEGIN (RSA|OPENSSH|PRIVATE) KEY"
    secret_scan = run(["git", "grep", "-n", "-I", "-E", secret_pattern, "--", "."])
    if secret_scan.returncode not in (0, 1):
        fail(f"secret scan failed: {command_detail(secret_scan)}")
    public_hits = [line for line in secret_scan.stdout.splitlines() if not line.startswith("legacy/")]
    if public_hits:
        fail(f"possible credential or private-key material found: {public_hits[:4]}")

    return section


def verify_clean_synced_main() -> str:
    status = _clean_status()
    if status:
        fail(f"tracked or untracked worktree changes remain:\n{status}")
    branch = output(["git", "branch", "--show-current"])
    if branch != "main":
        fail(f"release gate must run on main, found {branch!r}")
    fetched = run(["git", "fetch", "--tags", "origin"])
    if fetched.returncode != 0:
        fail(f"origin fetch failed\n{command_detail(fetched)}")
    head = output(["git", "rev-parse", "HEAD"])
    origin_main = output(["git", "rev-parse", "refs/remotes/origin/main"])
    if head != origin_main:
        fail(f"main is not synchronized with origin/main: {head} != {origin_main}")
    return head


def run_owner_validators() -> None:
    commands = [
        [sys.executable, "-B", "scripts/validate_skeleton.py"],
        ["node", "--check", "web/app.js"],
        [sys.executable, "-B", "scripts/smoke_workbook.py"],
        ["git", "diff", "--check", f"{BASELINE_TAG}..HEAD"],
    ]
    for command in commands:
        result = run(command)
        if result.returncode != 0:
            fail(f"{' '.join(command)}\n{command_detail(result)}")


def run_release_gate() -> dict[str, object]:
    section = verify_release_surfaces()
    head = verify_clean_synced_main()
    run_owner_validators()
    final_status = _clean_status()
    if final_status:
        fail(f"owner validators left worktree drift:\n{final_status}")
    return {
        "schema_version": "dionysus_release_check_v1",
        "repo": "Dionysus",
        "version": RELEASE_VERSION,
        "tag": RELEASE_TAG,
        "head": head,
        "baseline_tag": BASELINE_TAG,
        "baseline_commit": BASELINE_COMMIT,
        "product_first_parent_count": len(PRODUCT_FIRST_PARENT),
        "changelog_section_sha256": hashlib.sha256(section.body.encode("utf-8")).hexdigest(),
        "source_only": True,
        "artifact_registry_promotion": False,
        "runtime_health": False,
        "proof": False,
        "acceptance": False,
        "passed": True,
    }


def main() -> int:
    try:
        print(json.dumps(run_release_gate(), sort_keys=True))
        return 0
    except ReleaseGateError as exc:
        print(f"release_check: FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
