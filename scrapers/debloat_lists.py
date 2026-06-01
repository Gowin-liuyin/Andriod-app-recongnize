"""
Parse community-maintained Android debloat lists to discover package names and
their corresponding human-readable app names.

Data sources
------------
* UAD-NG (Universal Android Debloater Next Generation)
  Manufacturer-specific JSON lists hosted on GitHub.  Each file is an array of
  ``{id, label, description, removal, ...}`` objects.

* MuntashirAkon/android-debloat-list
  A single aggregated JSON list in the same format.

Every entry that has a non-empty *label* (or *name*) is collected, deduplicated
by package name, and written into the database with ``source='debloat'``.
"""

import sys
import os
import re

import requests

# Allow the module to be run directly while still importing the database
# module that lives in the parent directory.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import AppDatabase

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

UAD_RAW_BASE = (
    "https://raw.githubusercontent.com/MuntashirAkon/"
    "android-debloat-list/master/"
)

# UAD-NG organises entries by list type rather than by manufacturer.
UAD_MANUFACTURERS = [
    "oem", "aosp", "google", "carrier", "misc",
]

MUNTASHIR_URL = (
    "https://raw.githubusercontent.com/MuntashirAkon/"
    "android-debloat-list/master/list.json"
)

REQUEST_TIMEOUT = 30  # seconds


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _fetch_json(url: str, timeout: int = REQUEST_TIMEOUT) -> list | dict | None:
    """Fetch *url* and parse its body as JSON.

    Returns the parsed object on success or ``None`` on any HTTP / parse error
    (the error is printed to stderr so the caller doesn't need to guess).
    """
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        print(f"  [debloat] ERROR fetching {url}: {exc}", file=sys.stderr)
        return None
    except ValueError as exc:
        print(f"  [debloat] ERROR parsing JSON from {url}: {exc}", file=sys.stderr)
        return None


def _extract_entries(
    data: list | dict,
    source_name: str,
    default_category: str | None = None,
) -> list[dict]:
    """Pull package-name / app-name records from a parsed JSON blob.

    *data* may be a top-level list of entry objects, or a dict containing an
    array under one of its keys.  Each entry object is expected to have:

    * ``id``    — package name (e.g. ``com.samsung.android.bixby.wakeup``)
    * ``label`` — human-readable app name (falls back to ``name``)
    * ``removal`` — optional; used as a coarse *category* hint if the
      manufacturer-level category is not set

    Returns a list of dicts suitable for :meth:`AppDatabase.upsert_batch`.
    """
    # Unwrap if the JSON is a dict that wraps one or more arrays.
    if isinstance(data, dict):
        for key in ("packages", "apps", "entries", "list"):
            if isinstance(data.get(key), list):
                data = data[key]
                break
        else:
            # Pick the first list value we find.
            for val in data.values():
                if isinstance(val, list):
                    data = val
                    break

    if not isinstance(data, list):
        print(
            f"  [debloat] WARNING: {source_name} JSON is not an array, skipping",
            file=sys.stderr,
        )
        return []

    records: list[dict] = []
    for entry in data:
        if not isinstance(entry, dict):
            continue

        pkg = entry.get("id")
        if not pkg or not isinstance(pkg, str):
            continue

        # Prefer `label` or `name` — clean one-line names.
        label = entry.get("label") or entry.get("name")
        if not label or not isinstance(label, str) or not label.strip():
            # Fall back to the first sentence of `description`.
            desc = entry.get("description")
            if isinstance(desc, str) and desc.strip():
                # Take text up to the first period, newline, paren, colon, or URL.
                first = desc.strip().split("\n")[0].strip()
                first = re.split(r'[.。:：()（）\[\]]', first)[0].strip()
                # Remove URLs
                first = re.sub(r'https?://\S+', '', first).strip()
                if 3 <= len(first) <= 60:
                    label = first
        if not label or not isinstance(label, str) or not label.strip():
            continue
        label = label.strip()
        if len(label) > 60:
            continue

        # Derive a category — most specific first.
        category = default_category
        if not category:
            removal = entry.get("removal")
            if isinstance(removal, str) and removal.strip():
                category = removal.strip().title()

        records.append(
            {
                "package_name": pkg,
                "app_name": label,
                "category": category,
                "source": "debloat",
            }
        )

    return records


def _parse_uad_manufacturer(name: str) -> list[dict]:
    """Download and parse a single UAD-NG manufacturer JSON file."""
    url = f"{UAD_RAW_BASE}{name}.json"
    data = _fetch_json(url)
    if data is None:
        return []
    return _extract_entries(data, source_name=f"uad/{name}", default_category=name.title())


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def scrape(db: AppDatabase) -> int:
    """Download and parse debloat lists.  Returns count of new apps added.

    Parameters
    ----------
    db : AppDatabase
        An open database instance that will be populated via
        :meth:`~AppDatabase.upsert_batch`.

    Returns
    -------
    int
        Number of *new* applications added (existing apps that were only
        updated are **not** counted).
    """
    # Record the starting row count so we can report how many *new* apps
    # were inserted.
    before_count = db.count()
    all_records: dict[str, dict] = {}  # dedup by package_name

    # ------------------------------------------------------------------
    # Source 1 — UAD-NG manufacturer lists
    # ------------------------------------------------------------------
    for manufacturer in UAD_MANUFACTURERS:
        records = _parse_uad_manufacturer(manufacturer)
        if not records:
            continue

        # Dedup — later entries for the same package overwrite earlier ones.
        for rec in records:
            all_records[rec["package_name"]] = rec

        print(f"[debloat] uad/{manufacturer}: {len(records)} entries")

    # ------------------------------------------------------------------
    # Source 2 — MuntashirAkon/android-debloat-list
    # ------------------------------------------------------------------
    muntashir_data = _fetch_json(MUNTASHIR_URL)
    if muntashir_data is not None:
        records = _extract_entries(muntashir_data, source_name="muntashir")
        for rec in records:
            all_records[rec["package_name"]] = rec
        print(f"[debloat] muntashir: {len(records)} entries")
    else:
        print("[debloat] muntashir: skipped (fetch failed)", file=sys.stderr)

    # ------------------------------------------------------------------
    # Persist everything in a single batch transaction
    # ------------------------------------------------------------------
    if not all_records:
        print("[debloat] no entries to import", file=sys.stderr)
        return 0

    unique_records = list(all_records.values())
    db.upsert_batch(unique_records)

    after_count = db.count()
    new_apps = after_count - before_count

    print(
        f"[debloat] done: {len(unique_records)} unique entries, "
        f"{new_apps} new apps added"
    )
    return new_apps


# ---------------------------------------------------------------------------
# Standalone execution
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    db = AppDatabase()
    try:
        added = scrape(db)
        print(f"Total new apps: {added}")
    finally:
        db.close()
