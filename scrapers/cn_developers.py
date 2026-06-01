"""
Scrape all apps from major Chinese developers on Google Play.

Uses google-play-scraper to search for apps by developer name (both Chinese
and English names to maximise coverage), then writes metadata to the shared
AppDatabase.

Usage::

    from database import AppDatabase
    from scrapers.cn_developers import scrape

    db = AppDatabase("apps.db")
    new = scrape(db, delay=0.5)
    print(f"Added {new} new apps")
    db.close()
"""

import sys
import os
import time

import google_play_scraper as gps

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import AppDatabase

# ---------------------------------------------------------------------------
# Developer name list — both Chinese and English names to maximise coverage
# ---------------------------------------------------------------------------
CN_DEVELOPERS: list[str] = [
    # Tencent ecosystem
    "Tencent",
    "腾讯",
    # Alibaba ecosystem
    "Alibaba",
    "阿里巴巴",
    "Alibaba.com",
    # ByteDance
    "ByteDance",
    "字节跳动",
    # Baidu
    "Baidu",
    "百度",
    # NetEase
    "NetEase",
    "网易",
    "网易游戏",
    # JD.com
    "JD.com",
    "京东",
    # Meituan
    "Meituan",
    "美团",
    # Pinduoduo
    "Pinduoduo",
    "拼多多",
    # Xiaomi
    "Xiaomi",
    "小米",
    # Huawei
    "Huawei",
    "华为",
    # OPPO
    "OPPO",
    # vivo
    "vivo",
    "VIVO",
    # Sina / Weibo
    "Sina",
    "新浪",
    "Weibo",
    "微博",
    # Bilibili
    "Bilibili",
    "哔哩哔哩",
    "bilibili",
    # Kuaishou
    "Kuaishou",
    "快手",
    # Ctrip / Trip.com
    "Ctrip",
    "携程",
    "Trip.com",
    # Didi
    "Didi",
    "滴滴",
    # 58.com / Ganji
    "58.com",
    "赶集",
    # Zhihu
    "Zhihu",
    "知乎",
    # Xiaohongshu (RED)
    "Xiaohongshu",
    "小红书",
    # Douyin / TikTok
    "Douyin",
    "抖音",
    # Alipay
    "Alipay",
    "支付宝",
    # iQiyi
    "iQiyi",
    "爱奇艺",
    # Youku
    "Youku",
    "优酷",
    # Tencent Video
    "Tencent Video",
    "腾讯视频",
    # Sohu
    "Sohu",
    "搜狐",
    # 360
    "Qihoo 360",
    "360",
    # Meizu
    "Meizu",
    "魅族",
    # Lenovo
    "Lenovo",
    "联想",
    # ZTE
    "ZTE",
    "中兴",
    # OnePlus
    "OnePlus",
    "一加",
    # Douban
    "Douban",
    "豆瓣",
    # Xunlei / Thunder
    "Xunlei",
    "迅雷",
    # Kugou / Kuwo / QQ Music
    "Kugou",
    "酷狗",
    "Tencent Music",
    "QQ Music",
    # Momo / Tantan
    "Momo",
    "陌陌",
    "Tantan",
    "探探",
    # Banks & finance
    "中国工商银行",
    "中国建设银行",
    "中国银行",
    "中国农业银行",
    "招商银行",
    "交通银行",
    "中国邮政储蓄银行",
    # Telecom carriers
    "中国移动",
    "中国联通",
    "中国电信",
]

# Maximum number of hits per search call.
SEARCH_N_HITS = 200

# Number of apps to accumulate before flushing to the database.
BATCH_SIZE = 50

# Maximum retries per API call.
MAX_RETRIES = 2


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _call_with_retry(fn, desc: str, delay: float, max_retries: int = MAX_RETRIES):
    """Call *fn* with retry logic.  Returns the result or an empty list on
    repeated failure.  *delay* is doubled on each retry."""
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except Exception as exc:
            if attempt < max_retries:
                print(f"  {desc} retry {attempt + 1}/{max_retries} after: {exc}")
                time.sleep(delay * (2 ** attempt))
            else:
                print(f"  {desc} failed after {max_retries} retries: {exc}")
    return []


def _extract_record(result: dict) -> dict:
    """Convert a google-play-scraper result dict into a DB-ready record dict."""
    return {
        "package_name": result.get("appId", ""),
        "app_name": result.get("title", ""),
        "developer": result.get("developer", ""),
        "category": result.get("genreId", ""),
        "installs": result.get("installs", ""),
        "score": result.get("score"),
        "source": "play_store",
    }


def _app_detail(app_id: str, delay: float) -> dict | None:
    """Optionally fetch full app details for richer metadata.

    Called selectively (e.g. for apps missing installs or score) rather
    than for every app, to avoid excessive API calls.
    """
    for attempt in range(MAX_RETRIES + 1):
        try:
            return gps.app(app_id, lang="zh", country="cn")
        except Exception as exc:
            if attempt < MAX_RETRIES:
                time.sleep(delay)
            else:
                return None
    return None


# ---------------------------------------------------------------------------
# Main scraper
# ---------------------------------------------------------------------------


def scrape(db: AppDatabase, delay: float = 0.5) -> int:
    """Scrape all apps by major Chinese developers.  Returns count of new apps.

    Parameters
    ----------
    db : AppDatabase
        An open database instance (caller owns the lifecycle).
    delay : float
        Seconds to sleep between API calls (default 0.5).

    Returns
    -------
    int
        Number of **new** apps added to the database.
    """
    seen: set[str] = set()      # dedup by package_name
    pending: list[dict] = []    # accumulated records for batch write
    total_new = 0

    def _flush() -> None:
        """Write accumulated records to the database and clear the buffer."""
        nonlocal pending, total_new
        if not pending:
            return
        count = db.upsert_batch(pending)
        total_new += count
        print(f"  [batch] wrote {count} records ({total_new} total new so far)")
        pending.clear()

    def _process_result(r: dict) -> None:
        """Extract, dedup, and stage one result for batch write."""
        app_id = r.get("appId", "")
        if not app_id or app_id in seen:
            return
        seen.add(app_id)

        # If the search result is thin (missing installs / score), fetch
        # full details from the app endpoint.
        if not r.get("installs") or r.get("score") is None:
            detail = _app_detail(app_id, delay)
            if detail:
                r = detail
            time.sleep(delay)

        record = _extract_record(r)
        pending.append(record)

        if len(pending) >= BATCH_SIZE:
            _flush()

    for idx, dev_name in enumerate(CN_DEVELOPERS, start=1):
        print(f"[cn_dev {idx}/{len(CN_DEVELOPERS)}] Searching: {dev_name}")

        # ---- search endpoint ----
        results = _call_with_retry(
            lambda d=dev_name: gps.search(d, lang="zh", country="cn", n_hits=SEARCH_N_HITS),
            desc="search",
            delay=delay,
        )
        results = list(results) if results else []
        print(f"  -> {len(results)} results (search)")

        for r in results:
            _process_result(r)
        time.sleep(delay)

        # ---- developer endpoint (extra coverage) ----
        dev_results = _call_with_retry(
            lambda d=dev_name: gps.developer(d, lang="zh", country="cn"),
            desc="dev",
            delay=delay,
        )
        dev_results = list(dev_results) if dev_results else []

        if dev_results:
            print(f"  -> {len(dev_results)} results (developer endpoint)")
            for r in dev_results:
                _process_result(r)
            time.sleep(delay)

    # Flush any remaining records.
    _flush()

    return total_new


# ---------------------------------------------------------------------------
# Self-test / example
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Chinese Developer Scraper — self-test")
    print("=" * 60)

    db = AppDatabase()  # defaults to apps.db alongside database.py
    try:
        new_count = scrape(db, delay=1.0)
        print()
        print(f"Total new apps added: {new_count}")
        print(f"Total apps in database: {db.count()}")
    finally:
        db.close()
