"""
F-Droid index scraper.

Downloads the F-Droid repository index (index-v2.json or fallback index-v1.jar)
and extracts package_name → app_name mappings into the AppDatabase.
"""

import sys
import os
import json
import zipfile
import io
import xml.etree.ElementTree as ET

import requests

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import AppDatabase

INDEX_V2_URL = "https://f-droid.org/repo/index-v2.json"
INDEX_V1_URL = "https://f-droid.org/repo/index-v1.jar"


def _resolve_name(metadata: dict) -> tuple[str, str | None]:
    """Extract the best display name and English name from *metadata.name*.

    Returns
    -------
    (app_name, app_name_en)
        *app_name* is a non-empty string (the best available locale).
        *app_name_en* is the ``"en-US"`` entry, or ``None``.
    """
    names: dict | None = metadata.get("name")
    if not isinstance(names, dict) or not names:
        return ("", None)

    app_name_en = names.get("en-US") or names.get("en") or None

    # Pick the best display name: try preferred locales in order, then first
    for locale in ("en-US", "zh-CN", "zh", "en"):
        val = names.get(locale)
        if val:
            return (val, app_name_en)

    # Fallback: first available value
    first = next(iter(names.values()), "")
    return (first, app_name_en)


def _parse_v2(db: AppDatabase, text: str) -> int:
    """Parse index-v2.json *text* and insert records.  Returns count of new apps."""
    data = json.loads(text)
    packages: dict = data.get("packages", {})
    print(f"[fdroid] Downloaded index, {len(packages)} packages")

    before_count = db.count()
    batch: list[dict] = []

    for package_name, pkg in packages.items():
        metadata: dict = pkg.get("metadata", {})
        if not isinstance(metadata, dict):
            continue

        app_name, app_name_en = _resolve_name(metadata)
        if not app_name:
            continue

        categories: list = metadata.get("categories")
        category = categories[0] if categories else None
        developer = metadata.get("authorName")

        batch.append({
            "package_name": package_name,
            "app_name": app_name,
            "app_name_en": app_name_en,
            "developer": developer,
            "category": category,
            "source": "fdroid",
        })

        if len(batch) >= 500:
            db.upsert_batch(batch)
            batch.clear()

    # Final partial chunk
    if batch:
        db.upsert_batch(batch)

    after_count = db.count()
    return after_count - before_count


def _parse_v1(db: AppDatabase, content: bytes) -> int:
    """Parse index-v1.jar *content* (ZIP bytes) and insert records."""
    with zipfile.ZipFile(io.BytesIO(content)) as zf:
        with zf.open("index.xml") as f:
            xml_bytes = f.read()

    root = ET.fromstring(xml_bytes)

    before_count = db.count()
    batch: list[dict] = []

    for app_elem in root.iter("application"):
        package_name = app_elem.get("id")
        if not package_name:
            continue

        name_elem = app_elem.find("name")
        app_name = name_elem.text.strip() if name_elem is not None and name_elem.text else ""
        if not app_name:
            continue

        batch.append({
            "package_name": package_name,
            "app_name": app_name,
            "app_name_en": None,
            "developer": None,
            "category": None,
            "source": "fdroid",
        })

        if len(batch) >= 500:
            db.upsert_batch(batch)
            batch.clear()

    if batch:
        db.upsert_batch(batch)

    after_count = db.count()
    return after_count - before_count


def scrape(db: AppDatabase, timeout: int = 60) -> int:
    """Download and parse F-Droid index. Returns count of new apps added."""
    # ---- attempt index-v2.json -----------------------------------------------
    try:
        resp = requests.get(INDEX_V2_URL, timeout=timeout)
        resp.raise_for_status()
        return _parse_v2(db, resp.text)
    except (requests.RequestException, json.JSONDecodeError) as e:
        print(f"[fdroid] index-v2 failed: {e}")

    # ---- fallback: index-v1.jar ----------------------------------------------
    try:
        resp = requests.get(INDEX_V1_URL, timeout=timeout)
        resp.raise_for_status()
        return _parse_v1(db, resp.content)
    except requests.RequestException as e:
        print(f"[fdroid] index-v1 failed: {e}")

    print("[fdroid] Both index sources failed — no data added.")
    return 0


# ---------------------------------------------------------------------------
# Quick run
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    db = AppDatabase()
    try:
        added = scrape(db)
        print(f"[fdroid] Done — {added} new apps added, {db.count()} total in DB.")
    finally:
        db.close()
