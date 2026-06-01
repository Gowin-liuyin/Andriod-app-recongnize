"""
Google Play Store scraper — systematically collects Android app metadata.

Uses the ``google-play-scraper`` library to search the Play Store with
diverse queries, maximising coverage across categories and locales.
Results are written into the shared ``AppDatabase``.
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import AppDatabase

from google_play_scraper import search as gp_search, app as gp_app
from google_play_scraper import category, collection
from google_play_scraper.exceptions import NotFoundError, ExtraHTTPError


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BATCH_SIZE = 100          # flush to DB every N unique apps
MAX_RETRIES = 3           # retry count for transient failures
RETRY_BASE_DELAY = 1.0    # seconds — multiplied by 2**attempt on retry

# Every category known to google-play-scraper (for logging / future use).
ALL_CATEGORIES = [
    category.GAME, category.SOCIAL, category.TOOLS, category.COMMUNICATION,
    category.PRODUCTIVITY, category.PHOTOGRAPHY, category.VIDEO_PLAYERS,
    category.MUSIC_AND_AUDIO, category.ENTERTAINMENT, category.NEWS_AND_MAGAZINES,
    category.SHOPPING, category.TRAVEL_AND_LOCAL, category.LIFESTYLE,
    category.HEALTH_AND_FITNESS, category.EDUCATION, category.FINANCE,
    category.BUSINESS, category.MEDICAL, category.BOOKS_AND_REFERENCE,
    category.PERSONALIZATION, category.SPORTS, category.COMICS,
    category.AUTO_AND_VEHICLES, category.LIBRARIES_AND_DEMO, category.PARENTING,
    category.ART_AND_DESIGN, category.MAPS_AND_NAVIGATION, category.WEATHER,
    category.EVENTS, category.BEAUTY, category.FOOD_AND_DRINK,
    category.HOUSE_AND_HOME, category.DATING,
]

ALL_COLLECTIONS = [
    collection.TOP_FREE,
    collection.TOP_PAID,
    collection.TOP_GROSSING,
]
# TRENDING may not exist in all versions; include only if present.
if hasattr(collection, "TRENDING"):
    ALL_COLLECTIONS.append(collection.TRENDING)

# Search terms designed to surface a broad, diverse set of apps.
# Single letters trigger auto-complete and surface apps alphabetically.
# Chinese characters and category names target specific segments.
SEARCH_CONFIGS = [
    # ---- Chinese locale (zh / cn) ----
    ("", "zh", "cn", 200),
    *[(c, "zh", "cn", 100) for c in "abcdefghijklmnopqrstuvwxyz"],
    *[(t, "zh", "cn", 100) for t in [
        "微", "小", "快", "新", "大", "爱", "美", "好", "安", "网",
        "智", "云", "乐", "宝", "通", "易", "联", "优", "酷",
        "游戏", "社交", "工具", "通讯", "摄影", "相机", "视频",
        "音乐", "娱乐", "新闻", "购物", "旅行", "旅游", "健康",
        "健身", "教育", "学习", "金融", "理财", "阅读", "小说",
        "漫画", "地图", "导航", "天气", "美食", "外卖", "支付",
        "直播", "短视频", "修图", "清理", "安全", "输入法",
    ]],
    # ---- English locale (en / us) ----
    *[(c, "en", "us", 100) for c in "abcdefghijklmnopqrstuvwxyz"],
    *[(t, "en", "us", 100) for t in [
        "game", "chat", "social", "tool", "photo", "video", "music",
        "entertainment", "news", "shopping", "travel", "health",
        "fitness", "education", "finance", "reading", "map", "weather",
        "food", "dating", "sport", "design", "editor", "wallpaper",
        "launcher", "keyboard", "cleaner", "security", "vpn",
        "scanner", "player", "recorder", "calendar", "notes",
    ]],
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _search_safe(
    term: str,
    lang: str,
    country: str,
    n_hits: int,
    delay: float,
) -> list[dict]:
    """Call ``gp_search`` with retries & exponential backoff.

    Returns an empty list when the call fails after *MAX_RETRIES* attempts
    (the caller simply skips that query rather than aborting the whole run).
    """
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            results = gp_search(term, lang=lang, country=country, n_hits=n_hits)
            # guard: ensure we always have a list
            if not isinstance(results, list):
                results = []
            return results
        except NotFoundError:
            # Empty result set — not an error.
            return []
        except ExtraHTTPError as exc:
            if attempt < MAX_RETRIES:
                wait = RETRY_BASE_DELAY * (2 ** (attempt - 1))
                time.sleep(wait)
            else:
                print(f"  [warn] HTTP error for term={term!r} "
                      f"lang={lang}/{country}: {exc}")
                return []
        except Exception as exc:
            if attempt < MAX_RETRIES:
                wait = RETRY_BASE_DELAY * (2 ** (attempt - 1))
                time.sleep(wait)
            else:
                print(f"  [warn] Unexpected error for term={term!r} "
                      f"lang={lang}/{country}: {exc}")
                return []

    return []


def _build_record(result: dict, lang: str) -> dict:
    """Convert a raw search-result dict into a database-ready record.

    When *lang* is ``'zh'`` the result title is treated as the Chinese
    name; when *lang* is ``'en'`` it is stored as the English name and
    also used as a fallback for *app_name*.
    """
    package_name = result.get("appId", "").strip()
    title = (result.get("title") or "").strip()
    developer = (result.get("developer") or "").strip()
    category_val = (result.get("genre") or "").strip()
    installs = (result.get("installs") or "").strip()
    score = result.get("score")

    record: dict = {
        "package_name": package_name,
        "app_name": title,
        "developer": developer if developer else None,
        "category": category_val if category_val else None,
        "installs": installs if installs else None,
        "score": float(score) if score is not None else None,
        "source": "play_store",
    }

    if lang == "en":
        record["app_name_en"] = title if title else None
    else:
        record["app_name_en"] = None

    return record


def _resolve_english_names(
    db: AppDatabase,
    packages_need_en: set[str],
    delay: float,
) -> int:
    """Call ``gp_app()`` with ``lang='en'`` for packages missing an
    English name.  Returns the number of names successfully resolved.

    This is an **optional** second pass — if the network is slow or the
    list is large, we give up early rather than blocking the pipeline.
    """
    resolved = 0
    for i, pkg in enumerate(packages_need_en):
        try:
            detail = gp_app(pkg, lang="en", country="us")
            en_name = (detail.get("title") or "").strip()
            if en_name:
                db.upsert(package_name=pkg, app_name=None, app_name_en=en_name)
                resolved += 1
        except (NotFoundError, ExtraHTTPError, Exception):
            pass  # silently skip — English name is a nice-to-have

        if (i + 1) % 50 == 0:
            print(f"  [play_store] English names: {resolved}/{i + 1} resolved")
            time.sleep(delay * 2)  # extra breathing room

        time.sleep(delay)

    return resolved


# ---------------------------------------------------------------------------
# Main scraper entry-point
# ---------------------------------------------------------------------------

def scrape(db: AppDatabase, delay: float = 0.3) -> int:
    """Scrape Google Play top charts.  Returns number of **new** apps added.

    Parameters
    ----------
    db : AppDatabase
        An already-initialised database instance (caller owns its lifecycle).
    delay : float
        Seconds to sleep between API calls (rate-limiting).

    Returns
    -------
    int
        Number of package names that were **not** already in the database
        before this run.
    """
    seen: set[str] = set()          # appIds collected this run
    batch: list[dict] = []           # pending DB records
    new_count = 0                    # only genuinely new packages
    total_searches = len(SEARCH_CONFIGS)

    print(f"[play_store] Starting scrape — {total_searches} search queries")

    for idx, (term, lang, country, n_hits) in enumerate(SEARCH_CONFIGS, 1):
        results = _search_safe(term, lang, country, n_hits, delay)

        if not results:
            # Don't log empty — too noisy.  Just move on.
            pass

        for r in results:
            app_id = (r.get("appId") or "").strip()
            if not app_id:
                continue
            if app_id in seen:
                continue

            seen.add(app_id)
            record = _build_record(r, lang)
            batch.append(record)

            # Flush batch when it reaches BATCH_SIZE.
            if len(batch) >= BATCH_SIZE:
                # Count which records are genuinely new.
                existing_rows = db.search_batch(
                    [b["package_name"] for b in batch]
                )
                existing_ids = {row["package_name"] for row in existing_rows}
                batch_new = sum(
                    1 for b in batch if b["package_name"] not in existing_ids
                )
                new_count += batch_new

                db.upsert_batch(batch)
                print(
                    f"[play_store] batch {len(batch)} records, "
                    f"{batch_new} new (cumulative: {new_count})"
                )
                batch = []

        del results  # help GC on long runs

        # Progress every 10% or on the last query.
        if idx % max(1, total_searches // 10) == 0 or idx == total_searches:
            pct = idx * 100 // total_searches
            print(
                f"[play_store] progress {idx}/{total_searches} ({pct}%) — "
                f"{len(seen)} unique apps so far"
            )

        time.sleep(delay)

    # Flush remaining records.
    if batch:
        existing_rows = db.search_batch([b["package_name"] for b in batch])
        existing_ids = {row["package_name"] for row in existing_rows}
        batch_new = sum(
            1 for b in batch if b["package_name"] not in existing_ids
        )
        new_count += batch_new
        db.upsert_batch(batch)
        print(
            f"[play_store] final batch {len(batch)} records, "
            f"{batch_new} new (total: {new_count})"
        )
        batch = []

    print(
        f"[play_store] Done.  {len(seen)} unique apps encountered, "
        f"{new_count} new to the database."
    )
    return new_count


def scrape_with_english_names(
    db: AppDatabase,
    delay: float = 0.3,
    max_english: int = 500,
) -> int:
    """Run the full scrape **and** resolve English names for top apps.

    This is a convenience wrapper around :func:`scrape` that adds a second
    pass to call ``gp_app()`` (with ``lang='en'``) for up to *max_english*
    packages that are still missing an ``app_name_en`` value.

    Returns the total number of new apps added (same as :func:`scrape`).
    """
    new_count = scrape(db, delay=delay)

    # Find packages that need English names — top apps by score first.
    try:
        cursor = db.conn.execute(
            "SELECT package_name FROM apps "
            "WHERE app_name_en IS NULL "
            "ORDER BY score DESC NULLS LAST "
            "LIMIT ?",
            (max_english,),
        )
        need_en = {row["package_name"] for row in cursor.fetchall()}
    except Exception:
        need_en = set()

    if need_en:
        print(
            f"[play_store] Resolving English names for up to "
            f"{len(need_en)} packages …"
        )
        resolved = _resolve_english_names(db, need_en, delay)
        print(f"[play_store] English names resolved: {resolved}")
    else:
        print("[play_store] No packages need English name resolution.")

    return new_count


# ---------------------------------------------------------------------------
# __main__ — quick self-test / demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    db = AppDatabase()
    try:
        added = scrape(db, delay=0.3)
        print(f"\nTotal rows in database: {db.count()}")
        print(f"New apps added this run: {added}")
    finally:
        db.close()
