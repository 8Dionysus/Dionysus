#!/usr/bin/env python3
"""Run a loopback-only static smoke for the Dionysus workbook."""

from __future__ import annotations

import json
import re
import threading
import urllib.request
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEB_ROOT = ROOT / "web"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, _format: str, *_args: object) -> None:
        return


def fetch(base_url: str, path: str) -> tuple[int, str]:
    with urllib.request.urlopen(f"{base_url}/{path}", timeout=5) as response:
        return response.status, response.read().decode("utf-8")


def main() -> int:
    handler = partial(QuietHandler, directory=str(WEB_ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        base_url = f"http://127.0.0.1:{server.server_port}"
        index_status, index_body = fetch(base_url, "index.html")
        app_status, app_body = fetch(base_url, "app.js")
        if index_status != 200 or app_status != 200:
            raise RuntimeError(f"unexpected HTTP status: index={index_status}, app={app_status}")
        if "Dionysus" not in index_body or "localStorage" not in app_body:
            raise RuntimeError("workbook response is missing its expected static surface")
        if re.search(r"(?:fetch|XMLHttpRequest|sendBeacon|WebSocket)\s*\(", app_body):
            raise RuntimeError("workbook contains an unexpected network-capable browser call")
        print(
            json.dumps(
                {
                    "schema_version": "dionysus_workbook_static_smoke_v1",
                    "base": "loopback",
                    "index_status": index_status,
                    "app_status": app_status,
                    "network_calls": False,
                    "passed": True,
                },
                sort_keys=True,
            )
        )
        return 0
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())
