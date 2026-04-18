"""Shared helpers for Market Accurate data-pipeline scripts.

Kept deliberately small. No framework, no ORM, no cache: just a few
functions that the fetcher scripts can reuse.
"""
from __future__ import annotations

import json
import pathlib
from datetime import date, datetime
from typing import Any

SNAPSHOT_DIR = pathlib.Path(__file__).parent / "snapshot"

USER_AGENT = (
    "market-accurate-data-pipeline "
    "(https://github.com/JKershaw/market-accurate; research use; CC0)"
)


def snapshot_path(source: str, when: date | None = None) -> pathlib.Path:
    """Return a timestamped snapshot path for a given source name."""
    when = when or date.today()
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    return SNAPSHOT_DIR / f"{source}-{when.isoformat()}.json"


def write_snapshot(source: str, data: dict[str, Any]) -> pathlib.Path:
    """Write a JSON snapshot for a fetch run. Append-only: refuses to overwrite."""
    path = snapshot_path(source)
    if path.exists():
        raise FileExistsError(
            f"Snapshot already exists for {source} on {date.today()}: {path}. "
            "Snapshots are append-only; delete by hand if you really mean it."
        )
    payload = {
        "source": source,
        "fetched_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "data": data,
    }
    path.write_text(json.dumps(payload, indent=2, default=str))
    return path


def requests_headers() -> dict[str, str]:
    """HTTP headers to use for polite scraping. Always set a UA."""
    return {"User-Agent": USER_AGENT, "Accept": "application/json, text/html"}
