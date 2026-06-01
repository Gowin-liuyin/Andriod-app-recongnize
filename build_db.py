#!/usr/bin/env python3
"""
Master database build script — orchestrates all scrapers to populate the
offline SQLite database.

Run this once with an internet connection::

    python build_db.py

Or with options::

    python build_db.py --db /custom/path/apps.db   # custom DB path
    python build_db.py --skip-play-store            # skip the slowest step
    python build_db.py --help                       # show usage

The produced ``apps.db`` is a self-contained SQLite file.  Once built, the
GUI works completely offline — no network calls needed.
"""

import sys
import os
import time

# Ensure the project root is on sys.path so imports work when the script
# is invoked from any directory.
_project_root = os.path.dirname(os.path.abspath(__file__))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from database import AppDatabase
from scrapers.play_store import scrape as scrape_play_store
from scrapers.cn_developers import scrape as scrape_cn_devs
from scrapers.debloat_lists import scrape as scrape_debloat
from scrapers.fdroid import scrape as scrape_fdroid
from scrapers.cn_manual import scrape as scrape_cn_manual

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _fmt_seconds(seconds: float) -> str:
    """Return a human-readable duration string (e.g. ``12.3s`` or ``2m 5s``)."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes = int(seconds // 60)
    secs = seconds % 60
    if secs < 0.5:
        return f"{minutes}m"
    return f"{minutes}m {secs:.0f}s"


def _fmt_size(path: str) -> str:
    """Return a human-readable file size (e.g. ``4.2 MB``)."""
    try:
        size_bytes = os.path.getsize(path)
    except OSError:
        return "unknown"
    for unit in ("B", "KB", "MB", "GB"):
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def _print_usage():
    """Print CLI usage and exit."""
    print(
        "Usage: python build_db.py [OPTIONS]\n"
        "\n"
        "Build the offline SQLite package-name lookup database.\n"
        "\n"
        "Options:\n"
        "  --db PATH           Use PATH as the database file instead of the default\n"
        "                      (default: <project-root>/apps.db)\n"
        "\n"
        "  --skip-play-store   Omit the Google Play Store scraper (the slowest step).\n"
        "                      Useful for quick testing or when rate-limited.\n"
        "\n"
        "  --help              Show this help message and exit.\n"
        "\n"
        "Examples:\n"
        "  python build_db.py\n"
        "  python build_db.py --db /tmp/test.db\n"
        "  python build_db.py --skip-play-store --db /data/apps.db\n"
    )


# ---------------------------------------------------------------------------
# Core build logic
# ---------------------------------------------------------------------------

def build_all(db_path: str = None, skip_play_store: bool = False) -> int:
    """Run every scraper in order and return the total record count.

    Parameters
    ----------
    db_path : str or None
        Filesystem path for the SQLite database.  ``None`` uses the default
        from :class:`AppDatabase` (``<project-root>/apps.db``).
    skip_play_store : bool
        When ``True``, the Play Store scraper (typically the slowest step) is
        skipped entirely.

    Returns
    -------
    int
        Total number of records in the database after all scrapers finish.
    """
    # ------------------------------------------------------------------
    # 1. Open database
    # ------------------------------------------------------------------
    db = AppDatabase(db_path)
    target_path = db.db_path

    print("=" * 60)
    print("  Package-Lookup Database Builder")
    print("=" * 60)
    print(f"  Database: {target_path}")
    print("=" * 60)
    print()

    # Define the pipeline: (display_name, function, kwargs, is_skippable)
    steps = [
        ("Chinese Manual Data",  scrape_cn_manual, {}),
        ("Debloat Lists",        scrape_debloat,   {}),
        ("F-Droid Index",        scrape_fdroid,    {}),
        ("Chinese Developers",   scrape_cn_devs,   {"delay": 0.5}),
        ("Google Play Store",    scrape_play_store, {"delay": 0.3}),
    ]

    if skip_play_store:
        # Remove the last step (Play Store) but keep the pipeline clean.
        steps = [s for s in steps if s[0] != "Google Play Store"]

    total_steps = len(steps)
    step_records = []

    # ------------------------------------------------------------------
    # 2. Run each scraper in sequence
    # ------------------------------------------------------------------
    for i, (name, func, kwargs) in enumerate(steps, 1):
        print(f"===== Step {i}/{total_steps}: {name} =====")
        start = time.time()

        try:
            count = func(db, **kwargs)
            elapsed = time.time() - start
            print(f"  Records: {count}")
            print(f"  Time:    {_fmt_seconds(elapsed)}")
            step_records.append(count)
        except Exception as exc:
            elapsed = time.time() - start
            print(f"  [ERROR] {name} failed after {_fmt_seconds(elapsed)}")
            print(f"  [ERROR] {exc.__class__.__name__}: {exc}")
            step_records.append(0)

        print()

    # ------------------------------------------------------------------
    # 3. Summary
    # ------------------------------------------------------------------
    total = db.count()

    print("=" * 60)
    print("  Build Complete")
    print("=" * 60)
    print(f"  Total records:  {total:,}")
    print(f"  Database:       {target_path}")
    print(f"  Size:           {_fmt_size(target_path)}")
    print("=" * 60)

    db.close()
    return total


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Parse sys.argv directly — no argparse dependency.
    args = sys.argv[1:]

    db_path = None
    skip_play_store = False

    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ("--help", "-h"):
            _print_usage()
            sys.exit(0)
        elif arg == "--skip-play-store":
            skip_play_store = True
            i += 1
        elif arg == "--db":
            if i + 1 >= len(args):
                print("Error: --db requires a path argument")
                print("Run 'python build_db.py --help' for usage.")
                sys.exit(1)
            db_path = args[i + 1]
            i += 2
        else:
            print(f"Error: unknown option '{arg}'")
            print("Run 'python build_db.py --help' for usage.")
            sys.exit(1)

    total = build_all(db_path=db_path, skip_play_store=skip_play_store)
    print(f"\nDone. {total:,} records ready for offline lookup.")
