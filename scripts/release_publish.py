#!/usr/bin/env python3
"""Publish and audit the exact Dionysus prerelease through the owner route."""

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from pathlib import Path

import release_check


ROOT = release_check.ROOT
RELEASE_TAG = release_check.RELEASE_TAG
SLUG = "8Dionysus/Dionysus"


def fail(message: str) -> None:
    raise SystemExit(f"release_publish: FAIL: {message}")


def command_output(command: list[str], *, input_text: str | None = None) -> str:
    result = release_check.run(command, input_text=input_text)
    if result.returncode != 0:
        fail(f"{' '.join(command)}\n{release_check.command_detail(result)}")
    return result.stdout.strip()


def remote_ref(ref: str) -> str | None:
    result = release_check.run(["git", "ls-remote", "origin", ref])
    if result.returncode != 0:
        fail(f"remote inspection failed for {ref}: {release_check.command_detail(result)}")
    for line in result.stdout.splitlines():
        fields = line.split()
        if len(fields) >= 2 and fields[1] == ref:
            return fields[0]
    return None


def github_api(path: str) -> dict | list | None:
    result = release_check.run(["gh", "api", path])
    if result.returncode != 0:
        if "HTTP 404" in result.stderr or "Not Found" in result.stderr:
            return None
        fail(f"GitHub API lookup failed for {path}: {release_check.command_detail(result)}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        fail(f"GitHub API returned invalid JSON for {path}: {exc}")


def release_section() -> release_check.ReleaseSection:
    return release_check.extract_release_section((ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))


def canonical_body(section: release_check.ReleaseSection) -> str:
    return release_check.build_release_body(section)


def local_tag_commit() -> str | None:
    result = release_check.run(["git", "show-ref", "--tags", "--verify", f"refs/tags/{RELEASE_TAG}"])
    if result.returncode != 0:
        return None
    return command_output(["git", "rev-list", "-n", "1", RELEASE_TAG])


def assert_tag_state(head: str, *, allow_absent: bool) -> dict[str, str | None]:
    tag_object = remote_ref(f"refs/tags/{RELEASE_TAG}")
    peeled = remote_ref(f"refs/tags/{RELEASE_TAG}^{{}}")
    local = local_tag_commit()
    if allow_absent and (tag_object or peeled or local):
        if peeled != head or local != head:
            fail(
                "approved tag already exists with mismatched identity; refusing to move it: "
                f"tag_object={tag_object}, peeled={peeled}, local={local}, expected={head}"
            )
    return {"tag_object": tag_object, "peeled_commit": peeled, "local_commit": local}


def ensure_latest_marker(release: dict) -> dict:
    release_id = release.get("id")
    if not release_id:
        return release
    result = release_check.run(
        ["gh", "api", "--method", "PATCH", f"repos/{SLUG}/releases/{release_id}", "-F", "make_latest=true"]
    )
    if result.returncode != 0:
        fail(f"could not set the approved prerelease as latest: {release_check.command_detail(result)}")
    refreshed = github_api(f"repos/{SLUG}/releases/tags/{RELEASE_TAG}")
    if not isinstance(refreshed, dict):
        fail("GitHub Release disappeared while setting latest marker")
    return refreshed


def latest_release_tag() -> str | None:
    result = release_check.run(
        [
            "gh",
            "release",
            "list",
            "--repo",
            SLUG,
            "--limit",
            "100",
            "--json",
            "tagName,isLatest,isPrerelease,isDraft,publishedAt",
        ]
    )
    if result.returncode != 0:
        fail(f"latest marker lookup failed: {release_check.command_detail(result)}")
    try:
        rows = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        fail(f"latest marker response was not JSON: {exc}")
    return next((row.get("tagName") for row in rows if row.get("isLatest")), None)


def postpublish(expected_head: str | None = None) -> dict:
    gate = release_check.run_release_gate()
    head = str(gate["head"])
    if expected_head is not None and head != expected_head:
        fail(f"HEAD changed during postpublish audit: {head} != {expected_head}")
    section = release_section()
    body = canonical_body(section)
    identity = assert_tag_state(head, allow_absent=False)
    if identity["peeled_commit"] != head or identity["local_commit"] != head:
        fail(f"tag does not point at exact landed main: {identity}, expected={head}")
    local_type = command_output(["git", "cat-file", "-t", f"refs/tags/{RELEASE_TAG}"])
    if local_type != "tag":
        fail(f"approved tag is not annotated: {local_type}")

    release = github_api(f"repos/{SLUG}/releases/tags/{RELEASE_TAG}")
    if not isinstance(release, dict):
        fail(f"GitHub Release is missing for {RELEASE_TAG}")
    latest = latest_release_tag()
    if latest != RELEASE_TAG:
        release = ensure_latest_marker(release)
        latest = latest_release_tag()
    checks = {
        "tag_name": release.get("tag_name") == RELEASE_TAG,
        "published": bool(release.get("published_at")) and release.get("draft") is False,
        "prerelease": release.get("prerelease") is True,
        "latest_marker": latest == RELEASE_TAG,
        "body_matches_canonical": release.get("body") == body,
        "assets_empty": release.get("assets") == [],
    }
    if not all(checks.values()):
        fail(
            json.dumps(
                {
                    "checks": checks,
                    "release_url": release.get("html_url"),
                    "latest": latest,
                    "body_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
                    "assets": release.get("assets"),
                },
                sort_keys=True,
            )
        )
    return {
        "schema_version": "dionysus_postpublish_v1",
        "repo": "Dionysus",
        "version": release_check.RELEASE_VERSION,
        "tag": RELEASE_TAG,
        "head": head,
        "tag_identity": identity | {"local_type": local_type},
        "release_url": release.get("html_url"),
        "published_at": release.get("published_at"),
        "latest_marker": latest,
        "body_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "assets": [],
        "attestation": {
            "status": "not_applicable",
            "reason": "source-only GitHub prerelease; no package artifact is published",
        },
        "checks": checks,
        "runtime_health": False,
        "proof": False,
        "acceptance": False,
        "passed": True,
    }


def publish() -> dict:
    gate = release_check.run_release_gate()
    head = str(gate["head"])
    section = release_section()
    body = canonical_body(section)
    identity = assert_tag_state(head, allow_absent=True)
    if identity["peeled_commit"] is None:
        tag_result = release_check.run(["git", "tag", "-a", RELEASE_TAG, "-m", f"Dionysus {RELEASE_TAG}", head])
        if tag_result.returncode != 0:
            fail(f"annotated tag creation failed: {release_check.command_detail(tag_result)}")
        push_result = release_check.run(["git", "push", "origin", f"refs/tags/{RELEASE_TAG}"])
        if push_result.returncode != 0:
            fail(f"tag push failed after local tag creation; preserve the tag and retry: {release_check.command_detail(push_result)}")
        identity = assert_tag_state(head, allow_absent=False)

    existing = github_api(f"repos/{SLUG}/releases/tags/{RELEASE_TAG}")
    if existing is None:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as handle:
            handle.write(body)
            notes_path = Path(handle.name)
        try:
            release_result = release_check.run(
                [
                    "gh",
                    "release",
                    "create",
                    RELEASE_TAG,
                    "--repo",
                    SLUG,
                    "--verify-tag",
                    "--title",
                    RELEASE_TAG,
                    "--notes-file",
                    str(notes_path),
                    "--prerelease",
                    "--latest",
                ]
            )
        finally:
            notes_path.unlink(missing_ok=True)
        if release_result.returncode != 0:
            fail(
                "GitHub Release publication failed after the tag was pushed; "
                f"preserve the tag and retry postpublish: {release_check.command_detail(release_result)}"
            )
    else:
        if existing.get("body") != body or existing.get("prerelease") is not True:
            fail("an existing target GitHub Release does not match the canonical prerelease; refusing to overwrite it")
    return postpublish(head)


def dry_run() -> dict:
    gate = release_check.run_release_gate()
    head = str(gate["head"])
    section = release_section()
    identity = assert_tag_state(head, allow_absent=True)
    existing_release = github_api(f"repos/{SLUG}/releases/tags/{RELEASE_TAG}")
    return {
        "schema_version": "dionysus_release_publish_plan_v1",
        "repo": "Dionysus",
        "version": release_check.RELEASE_VERSION,
        "tag": RELEASE_TAG,
        "head": head,
        "baseline_tag": release_check.BASELINE_TAG,
        "body_sha256": hashlib.sha256(canonical_body(section).encode("utf-8")).hexdigest(),
        "source_only": True,
        "uploaded_assets": [],
        "artifact_trust": {
            "status": "not_applicable",
            "reason": "no package, binary, runtime, model, media, or release bundle is produced",
        },
        "existing_tag": identity,
        "existing_release": bool(existing_release),
        "actions": [
            "create or reuse only an annotated tag with the exact landed main commit",
            "create a prerelease GitHub Release from the canonical changelog body",
            "set and verify the GitHub latest marker",
            "verify empty assets and postpublish tag/body identity",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--confirm", action="store_true")
    mode.add_argument("--postpublish", action="store_true")
    args = parser.parse_args()
    try:
        result = postpublish() if args.postpublish else publish() if args.confirm else dry_run()
        print(json.dumps(result, sort_keys=True))
        return 0
    except SystemExit:
        raise
    except Exception as exc:
        fail(str(exc))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
