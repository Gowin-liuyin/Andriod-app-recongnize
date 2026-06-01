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

from google_play_scraper import search as gp_search
from google_play_scraper.exceptions import NotFoundError, ExtraHTTPError


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BATCH_SIZE = 100          # flush to DB every N unique apps
MAX_RETRIES = 3           # retry count for transient failures
RETRY_BASE_DELAY = 1.0    # seconds — multiplied by 2**attempt on retry
N_HITS = 250              # max results per query

# ---- Chinese search terms (lang=zh, country=cn) ----

_ZH_TERMS: list[str] = [
    # Category / domain keywords
    "社交", "通讯", "工具", "摄影", "相机", "视频", "音乐", "娱乐", "新闻",
    "购物", "旅行", "旅游", "健康", "健身", "教育", "学习", "金融", "理财",
    "阅读", "小说", "漫画", "动画", "地图", "导航", "天气", "美食", "外卖",
    "支付", "直播", "短视频", "修图", "清理", "安全", "输入法",
    "VPN", "翻墙", "加密", "钱包", "币", "挖矿",
    "AI", "人工智能", "聊天", "约会", "交友", "租房", "买房",
    "快递", "打车", "共享", "二手", "招聘", "求职",
    "股票", "基金", "保险", "医疗", "医院",
    "游戏", "学习", "英语", "翻译", "笔记", "日历", "闹钟",
    "备份", "加速", "省电", "壁纸", "主题", "桌面", "文件管理",
    "浏览器", "录音", "扫描", "打印", "投影", "遥控", "监控", "安防",
    "智能家居", "车联网", "自动驾驶",
    # Popular Chinese apps / brands
    "微信", "支付宝", "抖音", "快手", "小红书", "拼多多", "美团", "饿了么",
    "京东", "淘宝", "天猫", "百度", "高德", "滴滴", "携程", "去哪儿",
    "飞猪", "知乎", "豆瓣", "微博", "QQ", "网易", "搜狐", "优酷",
    "爱奇艺", "腾讯", "B站", "哔哩哔哩", "虎牙", "斗鱼",
    "陌陌", "探探", "闲鱼", "转转", "贝壳", "链家",
    "今日头条", "西瓜视频", "火山", "美图", "美颜", "轻颜",
    "Keep", "咕咚", "悦跑", "薄荷", "下厨房", "豆果",
    "得到", "樊登", "喜马拉雅", "蜻蜓", "酷狗", "QQ音乐",
    "网易云", "虾米", "咪咕", "沃", "天翼", "和",
    "工商银行", "建设银行", "农业银行", "中国银行", "招商银行", "交通银行",
    "浦发银行", "中信银行", "民生银行", "光大银行", "平安银行",
    "华夏", "华泰", "中信建投", "国泰君安", "海通", "广发", "申万",
    "同花顺", "东方财富", "雪球", "富途", "老虎", "币安",
    "华为", "小米", "OPPO", "vivo", "三星", "锤子", "一加", "魅族",
    "携程旅行", "艺龙", "同程", "途牛", "穷游", "马蜂窝",
    "房天下", "安居客", "58同城", "赶集", "智联", "前程无忧", "BOSS直聘",
    "滴滴出行", "曹操出行", "首汽", "神州", "顺丰", "圆通", "中通",
    "申通", "韵达", "百世", "德邦", "菜鸟",
    # Short/auto-complete terms
    "",  # empty query — default results
    "微", "小", "快", "新", "大", "爱", "美", "好", "安", "网",
    "智", "云", "乐", "宝", "通", "易", "联", "优", "酷",
    "免费", "付费", "热门", "推荐", "排行", "最新", "必备",
    "实用", "好玩", "神器", "助手", "管家", "大师",
    "专业版", "高级版", "极速版", "轻量版",
    "万能", "遥控器", "计算器", "手电筒", "指南针", "二维码",
    "条形码", "名片", "身份证", "驾照", "签证", "护照",
    "机票", "火车票", "酒店", "民宿", "景点", "攻略",
    "汇率", "单位换算", "尺子", "水平仪", "分贝仪", "测速",
    "恋爱", "结婚", "婚礼", "宝宝", "育儿", "孕期",
    "宠物", "狗", "猫", "鱼", "鸟",
    "汽车", "摩托车", "电动车", "自行车", "公交", "地铁",
    "停车", "充电", "加油", "洗车", "保养",
    "足球", "篮球", "NBA", "世界杯", "电竞", "棋牌",
    "斗地主", "麻将", "象棋", "围棋", "德州", "炸金花",
]

# Single letters a-z and digits 0-9 (trigger auto-complete for zh locale)
_ZH_TERMS.extend(chr(c) for c in range(ord("a"), ord("z") + 1))
_ZH_TERMS.extend(str(d) for d in range(10))

# Common Chinese characters (one-char queries surface alphabetically adjacent apps)
_ZH_COMMON_CHARS: list[str] = [
    "的", "一", "是", "在", "不", "了", "有", "和", "人", "这",
    "中", "大", "为", "上", "个", "国", "我", "以", "要", "他",
    "时", "来", "用", "们", "生", "到", "作", "地", "于", "出",
    "就", "分", "对", "成", "会", "可", "主", "发", "年", "动",
    "同", "工", "也", "能", "下", "过", "子", "说", "产", "种",
    "面", "而", "方", "后", "多", "定", "行", "学", "法", "所",
    "民", "得", "经", "十", "三", "之", "进", "着", "等", "部",
    "度", "家", "电", "力", "里", "如", "水", "化", "高", "自",
    "二", "理", "起", "物", "现", "实", "加", "量", "都", "两",
    "体", "制", "机", "当", "使", "点", "从", "业", "本", "去",
    "把", "性", "应", "开", "它", "合", "因", "只", "头", "长",
    "文", "无", "明", "问", "其", "公", "已", "天", "正", "想",
    "心", "看", "知", "又", "关", "比", "但", "重", "那", "此",
    "意", "第", "道", "还", "样", "前", "些", "与", "将", "被",
    "外", "最", "给", "情", "向", "间", "几", "数", "内", "老",
]
_ZH_TERMS.extend(_ZH_COMMON_CHARS)

# ---- English search terms (lang=en, country=us) ----

_EN_TERMS: list[str] = [
    # Communication / social
    "chat", "messaging", "message", "sms", "call", "video call", "contacts",
    "dialer", "phone", "social", "dating", "meet", "friends", "community",
    "forum", "group",
    # Privacy / security
    "vpn", "proxy", "encrypt", "password", "manager", "security", "privacy",
    "antivirus", "firewall", "authenticator", "2fa", "lock", "vault", "hide",
    # Crypto / finance
    "crypto", "wallet", "bitcoin", "ethereum", "exchange", "trading", "mining",
    "blockchain", "defi", "nft", "token", "stablecoin", "metamask",
    "stock", "forex", "gold", "invest", "trade", "bank", "credit", "loan",
    "mortgage", "insurance", "tax", "invoice", "receipt", "budget", "expense",
    "pay", "payment", "mobile pay", "banking",
    # AI / assistants
    "ai", "artificial intelligence", "chatgpt", "gpt", "assistant", "copilot",
    "chatbot", "ml", "deep learning", "image generator", "llm",
    # Productivity / office
    "notes", "todo", "task", "reminder", "alarm", "clock", "timer",
    "calendar", "planner", "journal", "diary", "habit", "goal",
    "office", "document", "spreadsheet", "presentation", "pdf",
    "word", "excel", "powerpoint", "slides", "form", "survey", "poll",
    "scan", "sign", "contract", "fax", "print",
    "resume", "cv", "job", "freelance", "gig", "project", "team",
    "workspace", "collaboration", "meeting", "webinar", "conference",
    "remote desktop", "vnc", "teamviewer", "anydesk", "screen share",
    # Tools / utilities
    "file", "transfer", "share", "cloud", "storage", "backup", "sync",
    "browser", "internet", "web", "search", "download", "upload",
    "calculator", "scanner", "qr", "barcode", "translate", "dictionary",
    "unit converter", "compass", "flashlight", "ruler", "level",
    "wifi", "bluetooth", "speed test", "data monitor", "cleaner",
    "booster", "battery", "cpu", "device info", "benchmark",
    # Media
    "photo", "camera", "selfie", "filter", "edit", "collage", "effect",
    "video", "player", "editor", "movie maker", "slideshow",
    "music", "audio", "mp3", "recorder", "equalizer", "dj", "mixer",
    "radio", "podcast", "streaming", "tv", "iptv", "movie", "cinema",
    # Games
    "game", "puzzle", "arcade", "action", "rpg", "strategy", "card",
    "casino", "bet", "lottery", "board", "chess", "sudoku", "word",
    "trivia", "quiz", "brain", "kids game",
    # Health / fitness
    "fitness", "workout", "gym", "running", "cycling", "yoga", "meditation",
    "sleep", "diet", "calorie", "fasting", "water", "pedometer",
    "health", "doctor", "pharmacy", "hospital", "clinic", "therapy",
    "mental health", "period", "pregnancy", "baby", "parent",
    # Lifestyle
    "food", "recipe", "cooking", "delivery", "restaurant", "grocery",
    "shopping", "deals", "coupon", "discount", "auction", "sell", "buy",
    "marketplace", "classifieds", "second hand", "thrift",
    "home", "house", "apartment", "real estate", "property", "rent",
    "roommate", "flat", "garden", "plant", "flower",
    "furniture", "decor", "interior design", "diy", "craft",
    "art", "draw", "paint", "sketch", "design", "logo", "poster",
    "invite", "card", "flyer", "collage", "frame",
    "fashion", "beauty", "makeup", "hair", "nails", "style", "outfit",
    # Education / learning
    "learn", "study", "course", "education", "tutor", "language",
    "english", "spanish", "french", "german", "chinese", "japanese",
    "korean", "coding", "programming", "math", "science", "history",
    # Books / reading
    "ebook", "reader", "book", "audiobook", "library", "comic", "manga",
    "news", "rss", "magazine", "newspaper", "blog",
    # Travel / navigation
    "travel", "flight", "hotel", "booking", "airbnb", "hostel",
    "map", "navigation", "gps", "compass", "speed", "traffic",
    "parking", "charge", "ev", "fuel", "gas", "car", "auto", "bike",
    "motorcycle", "truck", "bus", "train", "metro", "subway", "taxi",
    "ride share", "scooter", "rental", "car share",
    # Sports
    "sport", "score", "live score", "football", "soccer", "basketball",
    "baseball", "tennis", "golf", "hockey", "cricket", "rugby",
    "fantasy sports", "betting", "odds",
    # Weather / nature
    "weather", "forecast", "radar", "climate", "sunrise", "moon phase",
    "tide", "earthquake", "aurora",
    # Pets / animals
    "pet", "dog", "cat", "fish", "bird", "horse", "snake", "reptile",
    "vet", "animal",
    # Customization
    "wallpaper", "theme", "icon", "launcher", "keyboard", "ringtone",
    "notification", "widget", "lock screen", "home screen",
    # Certification / ID
    "certification", "license", "id", "passport", "visa", "immigration",
    "driver license", "test prep", "exam",
    # Miscellaneous
    "watch", "wear", "wearable", "smartwatch", "fitness band",
    "remote control", "smart home", "iot", "home automation",
    "vr", "virtual reality", "ar", "augmented reality",
    "kids", "family", "parental control", "elder", "senior",
    "religion", "bible", "quran", "prayer", "meditation app",
]

# Single letters a-z and digits 0-9 (trigger auto-complete for en locale)
_EN_TERMS.extend(chr(c) for c in range(ord("a"), ord("z") + 1))
_EN_TERMS.extend(str(d) for d in range(10))

# Additional short generic terms to round out coverage
_EN_TERMS.extend([
    "free", "pro", "lite", "premium", "hd", "plus", "best", "top",
    "fast", "easy", "simple", "smart", "app", "mobile", "android",
    "google", "play", "tool", "utility", "helper", "guide", "tutorial",
    "manual", "catalog", "finder", "tracker", "monitor", "control",
    "live", "offline", "online", "network", "social network",
])

# ---------------------------------------------------------------------------
# Build the flat search-configs list
# ---------------------------------------------------------------------------

SEARCH_CONFIGS: list[tuple[str, str, str, int]] = []
SEARCH_CONFIGS += [(t, "zh", "cn", N_HITS) for t in _ZH_TERMS]
SEARCH_CONFIGS += [(t, "en", "us", N_HITS) for t in _EN_TERMS]


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
    from google_play_scraper import app as gp_app

    resolved = 0
    for i, pkg in enumerate(sorted(packages_need_en)):
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
    """Scrape Google Play search results.  Returns number of **new** apps added.

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
