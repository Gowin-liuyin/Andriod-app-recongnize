"""
Curated hard-coded list of Chinese Android app package names mapped to
their human-readable names, developers, and categories.

Provides a comprehensive, offline source of truth for popular Chinese apps
that may not be indexed on Google Play or are distributed through domestic
Chinese app stores (Huawei AppGallery, Xiaomi GetApps, Tencent MyApp, etc.).

Usage::

    from database import AppDatabase
    from scrapers.cn_manual import scrape

    db = AppDatabase("apps.db")
    new = scrape(db)
    print(f"Added {new} new apps")
    db.close()
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import AppDatabase

# ---------------------------------------------------------------------------
# Comprehensive Chinese app dictionary
#
# Format:
#   "package.name": {
#       "app_name": "中文名",
#       "app_name_en": "Optional English name",
#       "developer": "Developer",
#       "category": "Category",
#   }
# ---------------------------------------------------------------------------

CN_APP_DICT: dict[str, dict] = {
    "com.tencent.mm": {
        "app_name": "微信",
        "app_name_en": "WeChat",
        "developer": "腾讯",
        "category": "Social",
    },

    "com.tencent.mobileqq": {
        "app_name": "QQ",
        "app_name_en": "QQ",
        "developer": "腾讯",
        "category": "Social",
    },

    "com.tencent.tim": {
        "app_name": "TIM",
        "app_name_en": "TIM",
        "developer": "腾讯",
        "category": "Social",
    },

    "com.tencent.qqlite": {
        "app_name": "QQ轻聊版",
        "app_name_en": "QQ Lite",
        "developer": "腾讯",
        "category": "Social",
    },

    "com.tencent.qqinternational": {
        "app_name": "QQ国际版",
        "app_name_en": "QQ International",
        "developer": "腾讯",
        "category": "Social",
    },

    "com.tencent.wework": {
        "app_name": "企业微信",
        "app_name_en": "WeCom",
        "developer": "腾讯",
        "category": "Business",
    },

    "com.alibaba.android.rimet": {
        "app_name": "钉钉",
        "app_name_en": "DingTalk",
        "developer": "阿里巴巴",
        "category": "Business",
    },

    "com.ss.android.lark": {
        "app_name": "飞书",
        "app_name_en": "Lark / Feishu",
        "developer": "字节跳动",
        "category": "Business",
    },

    "com.ss.android.lark.kami": {
        "app_name": "飞书极速版",
        "app_name_en": "Lark Lite",
        "developer": "字节跳动",
        "category": "Business",
    },

    "com.sina.weibo": {
        "app_name": "微博",
        "app_name_en": "Weibo",
        "developer": "新浪",
        "category": "Social",
    },

    "com.zhihu.android": {
        "app_name": "知乎",
        "app_name_en": "Zhihu",
        "developer": "知乎",
        "category": "Social",
    },

    "com.douban.frodo": {
        "app_name": "豆瓣",
        "app_name_en": "Douban",
        "developer": "豆瓣",
        "category": "Social",
    },

    "com.xingin.xhs": {
        "app_name": "小红书",
        "app_name_en": "RED / Xiaohongshu",
        "developer": "行吟信息科技",
        "category": "Social",
    },

    "cn.soulapp.android": {
        "app_name": "Soul",
        "app_name_en": "Soul",
        "developer": "上海任意门科技",
        "category": "Social",
    },

    "com.immomo.momo": {
        "app_name": "陌陌",
        "app_name_en": "Momo",
        "developer": "挚文集团",
        "category": "Social",
    },

    "com.p1.mobile.putong": {
        "app_name": "探探",
        "app_name_en": "Tantan",
        "developer": "探探科技",
        "category": "Dating",
    },

    "com.tencent.qzone": {
        "app_name": "QQ空间",
        "app_name_en": "Qzone",
        "developer": "腾讯",
        "category": "Social",
    },

    "com.tencent.qqmusic": {
        "app_name": "QQ音乐",
        "app_name_en": "QQ Music",
        "developer": "腾讯",
        "category": "Music & Audio",
    },

    "com.tencent.qqsports": {
        "app_name": "腾讯体育",
        "app_name_en": "Tencent Sports",
        "developer": "腾讯",
        "category": "Sports",
    },

    "com.tencent.weread": {
        "app_name": "微信读书",
        "app_name_en": "WeRead",
        "developer": "腾讯",
        "category": "Books & Reference",
    },

    "com.tencent.androidqqmail": {
        "app_name": "QQ邮箱",
        "app_name_en": "QQ Mail",
        "developer": "腾讯",
        "category": "Productivity",
    },

    "com.tencent.qqpimsecure": {
        "app_name": "腾讯手机管家",
        "app_name_en": "Tencent Mobile Manager",
        "developer": "腾讯",
        "category": "Tools",
    },

    "com.tencent.qqpim": {
        "app_name": "QQ同步助手",
        "app_name_en": "QQ Sync",
        "developer": "腾讯",
        "category": "Tools",
    },

    "com.tencent.qqlive": {
        "app_name": "腾讯视频",
        "app_name_en": "Tencent Video",
        "developer": "腾讯",
        "category": "Entertainment",
    },

    "com.tencent.weishi": {
        "app_name": "微视",
        "app_name_en": "WeSee",
        "developer": "腾讯",
        "category": "Entertainment",
    },

    "com.tencent.news": {
        "app_name": "腾讯新闻",
        "app_name_en": "Tencent News",
        "developer": "腾讯",
        "category": "News & Magazines",
    },

    "com.tencent.ibg.joox": {
        "app_name": "JOOX音乐",
        "app_name_en": "JOOX Music",
        "developer": "腾讯",
        "category": "Music & Audio",
    },

    "com.tencent.karaoke": {
        "app_name": "全民K歌",
        "app_name_en": "WeSing",
        "developer": "腾讯",
        "category": "Music & Audio",
    },

    "com.tencent.qqgame": {
        "app_name": "QQ游戏",
        "app_name_en": "QQ Game Center",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.map": {
        "app_name": "腾讯地图",
        "app_name_en": "Tencent Maps",
        "developer": "腾讯",
        "category": "Maps & Navigation",
    },

    "com.tencent.filemanager": {
        "app_name": "腾讯文件",
        "app_name_en": "Tencent Files",
        "developer": "腾讯",
        "category": "Tools",
    },

    "com.tencent.wemeet.app": {
        "app_name": "腾讯会议",
        "app_name_en": "Tencent Meeting / VooV Meeting",
        "developer": "腾讯",
        "category": "Business",
    },

    "com.tencent.edu": {
        "app_name": "腾讯课堂",
        "app_name_en": "Tencent Classroom",
        "developer": "腾讯",
        "category": "Education",
    },

    "com.tencent.qt.qtl": {
        "app_name": "掌上英雄联盟",
        "app_name_en": "League of Legends Mobile",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.imangi.templerun": {
        "app_name": "神庙逃亡",
        "app_name_en": "Temple Run",
        "developer": "Imangi Studios",
        "category": "Game",
    },

    "com.imangi.templerun2": {
        "app_name": "神庙逃亡2",
        "app_name_en": "Temple Run 2",
        "developer": "Imangi Studios",
        "category": "Game",
    },

    "com.taobao.taobao": {
        "app_name": "手机淘宝",
        "app_name_en": "Taobao",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.taobao.litetao": {
        "app_name": "淘特",
        "app_name_en": "Taobao Deals / Tejia",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.taobao.idlefish": {
        "app_name": "闲鱼",
        "app_name_en": "Idle Fish / Xianyu",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.tmall.wireless": {
        "app_name": "天猫",
        "app_name_en": "Tmall",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.alibaba.wireless": {
        "app_name": "阿里巴巴",
        "app_name_en": "Alibaba.com",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.alibaba.icbu": {
        "app_name": "阿里国际站",
        "app_name_en": "Alibaba International",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.jingdong.app.mall": {
        "app_name": "京东",
        "app_name_en": "JD.com",
        "developer": "京东",
        "category": "Shopping",
    },

    "com.jd.jrapp": {
        "app_name": "京东金融",
        "app_name_en": "JD Finance",
        "developer": "京东",
        "category": "Finance",
    },

    "com.jd.jdlite": {
        "app_name": "京东极速版",
        "app_name_en": "JD Lite",
        "developer": "京东",
        "category": "Shopping",
    },

    "com.xunmeng.pinduoduo": {
        "app_name": "拼多多",
        "app_name_en": "Pinduoduo",
        "developer": "拼多多",
        "category": "Shopping",
    },

    "com.achievo.vipshop": {
        "app_name": "唯品会",
        "app_name_en": "Vipshop",
        "developer": "唯品会",
        "category": "Shopping",
    },

    "com.suning.mobile.ebuy": {
        "app_name": "苏宁易购",
        "app_name_en": "Suning",
        "developer": "苏宁",
        "category": "Shopping",
    },

    "com.shizhuang.duapp": {
        "app_name": "得物",
        "app_name_en": "Dewu / Poizon",
        "developer": "上海识装信息科技",
        "category": "Shopping",
    },

    "com.wuba.zhuanzhuan": {
        "app_name": "转转",
        "app_name_en": "Zhuanzhuan",
        "developer": "转转",
        "category": "Shopping",
    },

    "com.mogujie": {
        "app_name": "蘑菇街",
        "app_name_en": "Mogu Street",
        "developer": "蘑菇街",
        "category": "Shopping",
    },

    "com.netease.yanxuan": {
        "app_name": "网易严选",
        "app_name_en": "Yanxuan",
        "developer": "网易",
        "category": "Shopping",
    },

    "com.xiaomi.shop": {
        "app_name": "小米商城",
        "app_name_en": "Mi Store",
        "developer": "小米",
        "category": "Shopping",
    },

    "com.xiaomi.youpin": {
        "app_name": "小米有品",
        "app_name_en": "Xiaomi Youpin",
        "developer": "小米",
        "category": "Shopping",
    },

    "com.vmall.client": {
        "app_name": "华为商城",
        "app_name_en": "Vmall / Huawei Mall",
        "developer": "华为",
        "category": "Shopping",
    },

    "com.dangdang.bookphone": {
        "app_name": "当当",
        "app_name_en": "Dangdang",
        "developer": "当当网",
        "category": "Shopping",
    },

    "com.yhd.mobile": {
        "app_name": "1号店",
        "app_name_en": "YHD / Yihaodian",
        "developer": "一号店",
        "category": "Shopping",
    },

    "com.koubei.client.android": {
        "app_name": "口碑",
        "app_name_en": "Koubei",
        "developer": "阿里巴巴",
        "category": "Food & Drink",
    },

    "com.taobao.fleamarket": {
        "app_name": "闲鱼",
        "app_name_en": "Idle Fish",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.jumei.app": {
        "app_name": "聚美优品",
        "app_name_en": "Jumei",
        "developer": "聚美优品",
        "category": "Shopping",
    },

    "com.tencent.ecmall": {
        "app_name": "腾讯惠聚",
        "app_name_en": "Tencent Huiju",
        "developer": "腾讯",
        "category": "Shopping",
    },

    "com.meituan.grocery": {
        "app_name": "美团优选",
        "app_name_en": "Meituan Select",
        "developer": "美团",
        "category": "Shopping",
    },

    "com.dmall.app": {
        "app_name": "多点",
        "app_name_en": "Dmall",
        "developer": "多点生活",
        "category": "Shopping",
    },

    "com.yongche.android": {
        "app_name": "永辉生活",
        "app_name_en": "Yonghui Life",
        "developer": "永辉超市",
        "category": "Shopping",
    },

    "com.unionpay": {
        "app_name": "云闪付",
        "app_name_en": "UnionPay / QuickPass",
        "developer": "中国银联",
        "category": "Finance",
    },

    "cn.gov.pbc.dcep": {
        "app_name": "数字人民币",
        "app_name_en": "Digital RMB / e-CNY",
        "developer": "中国人民银行",
        "category": "Finance",
    },

    "com.chinamworld.boc": {
        "app_name": "中国银行",
        "app_name_en": "Bank of China",
        "developer": "中国银行",
        "category": "Finance",
    },

    "com.chinamworld.icbc": {
        "app_name": "中国工商银行",
        "app_name_en": "ICBC",
        "developer": "中国工商银行",
        "category": "Finance",
    },

    "com.chinamworld.ccb": {
        "app_name": "中国建设银行",
        "app_name_en": "CCB",
        "developer": "中国建设银行",
        "category": "Finance",
    },

    "com.chinamworld.abchina": {
        "app_name": "中国农业银行",
        "app_name_en": "ABC",
        "developer": "中国农业银行",
        "category": "Finance",
    },

    "com.chinamworld.bocmbci": {
        "app_name": "中国银行手机银行",
        "app_name_en": "Bank of China Mobile",
        "developer": "中国银行",
        "category": "Finance",
    },

    "com.bankcomm.maidanba": {
        "app_name": "交通银行",
        "app_name_en": "Bank of Communications",
        "developer": "交通银行",
        "category": "Finance",
    },

    "com.psbc.mobilebank": {
        "app_name": "邮政储蓄银行",
        "app_name_en": "PSBC",
        "developer": "中国邮政储蓄银行",
        "category": "Finance",
    },

    "com.cib.olc": {
        "app_name": "兴业银行",
        "app_name_en": "CIB / Industrial Bank",
        "developer": "兴业银行",
        "category": "Finance",
    },

    "com.spdb.mobilebank": {
        "app_name": "浦发银行",
        "app_name_en": "SPDB",
        "developer": "浦发银行",
        "category": "Finance",
    },

    "cmb.pb": {
        "app_name": "招商银行掌上生活",
        "app_name_en": "CMB Credit Card",
        "developer": "招商银行",
        "category": "Finance",
    },

    "com.cmbc.mbank": {
        "app_name": "民生银行",
        "app_name_en": "CMBC",
        "developer": "民生银行",
        "category": "Finance",
    },

    "com.pingan.papd": {
        "app_name": "平安口袋银行",
        "app_name_en": "Ping An Pocket Bank",
        "developer": "平安银行",
        "category": "Finance",
    },

    "com.pingan.lifeinsurance": {
        "app_name": "平安金管家",
        "app_name_en": "Ping An Life",
        "developer": "中国平安",
        "category": "Finance",
    },

    "com.tencent.tmgp.cf": {
        "app_name": "微信支付",
        "app_name_en": "WeChat Pay",
        "developer": "腾讯",
        "category": "Finance",
    },

    "com.chinamworld.bank": {
        "app_name": "中国银行缤纷生活",
        "app_name_en": "BOC Life",
        "developer": "中国银行",
        "category": "Finance",
    },

    "com.yitong.mbank": {
        "app_name": "中信银行",
        "app_name_en": "CITIC Bank",
        "developer": "中信银行",
        "category": "Finance",
    },

    "com.bochk.app.aos": {
        "app_name": "中银香港",
        "app_name_en": "BOCHK",
        "developer": "中银香港",
        "category": "Finance",
    },

    "com.paic.mobile.android.portal": {
        "app_name": "平安好车主",
        "app_name_en": "Ping An Car Owner",
        "developer": "中国平安",
        "category": "Finance",
    },

    "com.antfortune.wealth": {
        "app_name": "蚂蚁财富",
        "app_name_en": "Ant Fortune",
        "developer": "蚂蚁集团",
        "category": "Finance",
    },

    "com.ant.interview": {
        "app_name": "芝麻信用",
        "app_name_en": "Sesame Credit",
        "developer": "蚂蚁集团",
        "category": "Finance",
    },

    "com.tencent.fortuneplat": {
        "app_name": "理财通",
        "app_name_en": "Tencent Wealth",
        "developer": "腾讯",
        "category": "Finance",
    },

    "com.lu.com": {
        "app_name": "陆金所",
        "app_name_en": "Lufax",
        "developer": "陆金所",
        "category": "Finance",
    },

    "com.eastmoney.android.berlin": {
        "app_name": "东方财富",
        "app_name_en": "East Money",
        "developer": "东方财富",
        "category": "Finance",
    },

    "com.eastmoney.android.fund": {
        "app_name": "天天基金",
        "app_name_en": "Tiantian Fund",
        "developer": "东方财富",
        "category": "Finance",
    },

    "com.tonghuashun.app": {
        "app_name": "同花顺",
        "app_name_en": "THS / Flush",
        "developer": "同花顺",
        "category": "Finance",
    },

    "com.snowball.android": {
        "app_name": "雪球",
        "app_name_en": "Snowball",
        "developer": "雪球",
        "category": "Finance",
    },

    "com.xueqiu.android": {
        "app_name": "雪球",
        "app_name_en": "Snowball Finance",
        "developer": "雪球",
        "category": "Finance",
    },

    "com.wacai365": {
        "app_name": "挖财",
        "app_name_en": "Wacai",
        "developer": "挖财",
        "category": "Finance",
    },

    "cn.com.unionpay.qrcode": {
        "app_name": "云闪付商户通",
        "app_name_en": "UnionPay Merchant",
        "developer": "中国银联",
        "category": "Finance",
    },

    "com.ss.android.ugc.aweme": {
        "app_name": "抖音",
        "app_name_en": "Douyin / TikTok CN",
        "developer": "字节跳动",
        "category": "Entertainment",
    },

    "com.ss.android.ugc.aweme.lite": {
        "app_name": "抖音极速版",
        "app_name_en": "Douyin Lite",
        "developer": "字节跳动",
        "category": "Entertainment",
    },

    "com.ss.android.ugc.live": {
        "app_name": "抖音火山版",
        "app_name_en": "Douyin Volcano",
        "developer": "字节跳动",
        "category": "Entertainment",
    },

    "com.smile.gifmaker": {
        "app_name": "快手",
        "app_name_en": "Kuaishou",
        "developer": "快手",
        "category": "Entertainment",
    },

    "com.kuaishou.nebula": {
        "app_name": "快手极速版",
        "app_name_en": "Kuaishou Lite",
        "developer": "快手",
        "category": "Entertainment",
    },

    "tv.danmaku.bili": {
        "app_name": "哔哩哔哩",
        "app_name_en": "Bilibili",
        "developer": "哔哩哔哩",
        "category": "Entertainment",
    },

    "tv.danmaku.bilibilihd": {
        "app_name": "哔哩哔哩HD",
        "app_name_en": "Bilibili HD",
        "developer": "哔哩哔哩",
        "category": "Entertainment",
    },

    "com.bilibili.app.in": {
        "app_name": "哔哩哔哩国际版",
        "app_name_en": "Bilibili International",
        "developer": "哔哩哔哩",
        "category": "Entertainment",
    },

    "com.qiyi.video": {
        "app_name": "爱奇艺",
        "app_name_en": "iQiyi",
        "developer": "爱奇艺",
        "category": "Entertainment",
    },

    "com.qiyi.video.lite": {
        "app_name": "爱奇艺极速版",
        "app_name_en": "iQiyi Lite",
        "developer": "爱奇艺",
        "category": "Entertainment",
    },

    "com.qiyi.video.pad": {
        "app_name": "爱奇艺PAD版",
        "app_name_en": "iQiyi Pad",
        "developer": "爱奇艺",
        "category": "Entertainment",
    },

    "com.youku.phone": {
        "app_name": "优酷",
        "app_name_en": "Youku",
        "developer": "阿里巴巴",
        "category": "Entertainment",
    },

    "com.youku.tudou": {
        "app_name": "土豆视频",
        "app_name_en": "Tudou",
        "developer": "阿里巴巴",
        "category": "Entertainment",
    },

    "com.cctv.yangshipin.app.androidp": {
        "app_name": "央视频",
        "app_name_en": "CCTV Video / Yangshipin",
        "developer": "中央广播电视总台",
        "category": "Entertainment",
    },

    "com.sohuott.tv": {
        "app_name": "搜狐视频",
        "app_name_en": "Sohu Video",
        "developer": "搜狐",
        "category": "Entertainment",
    },

    "com.hunantv.imgo.activity": {
        "app_name": "芒果TV",
        "app_name_en": "Mango TV",
        "developer": "芒果TV",
        "category": "Entertainment",
    },

    "com.ss.android.article.video": {
        "app_name": "西瓜视频",
        "app_name_en": "Xigua Video",
        "developer": "字节跳动",
        "category": "Entertainment",
    },

    "com.le123.ysdq": {
        "app_name": "影视大全",
        "app_name_en": "Yingshi Daquan",
        "developer": "影视大全",
        "category": "Entertainment",
    },

    "com.douguo.recipe": {
        "app_name": "豆果美食",
        "app_name_en": "Douguo Recipes",
        "developer": "豆果",
        "category": "Food & Drink",
    },

    "com.yixia.videoeditor": {
        "app_name": "秒拍",
        "app_name_en": "Miaopai",
        "developer": "一下科技",
        "category": "Entertainment",
    },

    "com.meelive.ingame": {
        "app_name": "映客",
        "app_name_en": "Inke",
        "developer": "映客",
        "category": "Entertainment",
    },

    "com.yy.yymeeting": {
        "app_name": "YY",
        "app_name_en": "YY Live",
        "developer": "欢聚集团",
        "category": "Entertainment",
    },

    "com.huajiao": {
        "app_name": "花椒直播",
        "app_name_en": "Huajiao Live",
        "developer": "花椒",
        "category": "Entertainment",
    },

    "air.tv.douyu.android": {
        "app_name": "斗鱼",
        "app_name_en": "Douyu",
        "developer": "斗鱼",
        "category": "Entertainment",
    },

    "com.duowan.kiwi": {
        "app_name": "虎牙直播",
        "app_name_en": "Huya Live",
        "developer": "虎牙",
        "category": "Entertainment",
    },

    "com.cctor.nosey": {
        "app_name": "皮皮虾",
        "app_name_en": "Pipixia",
        "developer": "字节跳动",
        "category": "Entertainment",
    },

    "com.quanmin.quanmin": {
        "app_name": "最右",
        "app_name_en": "Zuiyou",
        "developer": "最右",
        "category": "Social",
    },

    "com.jimuapp.android": {
        "app_name": "积目",
        "app_name_en": "Jimu",
        "developer": "积目科技",
        "category": "Social",
    },

    "com.netease.cloudmusic": {
        "app_name": "网易云音乐",
        "app_name_en": "NetEase Cloud Music",
        "developer": "网易",
        "category": "Music & Audio",
    },

    "com.kugou.android": {
        "app_name": "酷狗音乐",
        "app_name_en": "Kugou Music",
        "developer": "腾讯音乐",
        "category": "Music & Audio",
    },

    "cn.kuwo.player": {
        "app_name": "酷我音乐",
        "app_name_en": "Kuwo Music",
        "developer": "腾讯音乐",
        "category": "Music & Audio",
    },

    "com.ximalaya.ting.android": {
        "app_name": "喜马拉雅",
        "app_name_en": "Himalaya",
        "developer": "喜马拉雅",
        "category": "Music & Audio",
    },

    "com.ximalaya.ting.lite": {
        "app_name": "喜马拉雅极速版",
        "app_name_en": "Himalaya Lite",
        "developer": "喜马拉雅",
        "category": "Music & Audio",
    },

    "fm.qingting.qtradio": {
        "app_name": "蜻蜓FM",
        "app_name_en": "Qingting FM",
        "developer": "蜻蜓FM",
        "category": "Music & Audio",
    },

    "com.lizhi.android": {
        "app_name": "荔枝",
        "app_name_en": "Lizhi FM",
        "developer": "荔枝",
        "category": "Music & Audio",
    },

    "com.changba": {
        "app_name": "唱吧",
        "app_name_en": "Changba",
        "developer": "唱吧",
        "category": "Music & Audio",
    },

    "cn.tiankang.app": {
        "app_name": "天籁K歌",
        "app_name_en": "Tianlai KTV",
        "developer": "天籁K歌",
        "category": "Music & Audio",
    },

    "com.tudou.radio": {
        "app_name": "荔枝播客",
        "app_name_en": "Lizhi Podcast",
        "developer": "荔枝",
        "category": "Music & Audio",
    },

    "com.ss.android.article.audio": {
        "app_name": "番茄畅听",
        "app_name_en": "Tomato Audio",
        "developer": "字节跳动",
        "category": "Music & Audio",
    },

    "com.baidu.music": {
        "app_name": "百度音乐",
        "app_name_en": "Baidu Music",
        "developer": "百度",
        "category": "Music & Audio",
    },

    "com.tencent.musician": {
        "app_name": "腾讯音乐人",
        "app_name_en": "Tencent Musician",
        "developer": "腾讯",
        "category": "Music & Audio",
    },

    "com.didi.ethereal": {
        "app_name": "音悦台",
        "app_name_en": "Yinyuetai",
        "developer": "音悦台",
        "category": "Music & Audio",
    },

    "com.tencent.wesing": {
        "app_name": "WeSing国际版",
        "app_name_en": "WeSing International",
        "developer": "腾讯",
        "category": "Music & Audio",
    },

    "com.spotify.music": {
        "app_name": "Spotify",
        "app_name_en": "Spotify",
        "developer": "Spotify AB",
        "category": "Music & Audio",
    },

    "com.ss.android.article.news": {
        "app_name": "今日头条",
        "app_name_en": "Jinri Toutiao / TopBuzz",
        "developer": "字节跳动",
        "category": "News & Magazines",
    },

    "com.ss.android.article.lite": {
        "app_name": "今日头条极速版",
        "app_name_en": "Toutiao Lite",
        "developer": "字节跳动",
        "category": "News & Magazines",
    },

    "com.netease.newsreader.activity": {
        "app_name": "网易新闻",
        "app_name_en": "NetEase News",
        "developer": "网易",
        "category": "News & Magazines",
    },

    "com.sohu.newsclient": {
        "app_name": "搜狐新闻",
        "app_name_en": "Sohu News",
        "developer": "搜狐",
        "category": "News & Magazines",
    },

    "com.sina.news": {
        "app_name": "新浪新闻",
        "app_name_en": "Sina News",
        "developer": "新浪",
        "category": "News & Magazines",
    },

    "com.ifeng.news2": {
        "app_name": "凤凰新闻",
        "app_name_en": "Ifeng News",
        "developer": "凤凰新媒体",
        "category": "News & Magazines",
    },

    "com.yidian.zixun": {
        "app_name": "一点资讯",
        "app_name_en": "Yidian Zixun / Particle News",
        "developer": "一点资讯",
        "category": "News & Magazines",
    },

    "com.qutoutiao.android": {
        "app_name": "趣头条",
        "app_name_en": "Qutoutiao",
        "developer": "趣头条",
        "category": "News & Magazines",
    },

    "com.cankaoxiaoxi.app1": {
        "app_name": "参考消息",
        "app_name_en": "Cankao Xiaoxi",
        "developer": "参考消息",
        "category": "News & Magazines",
    },

    "com.people.news": {
        "app_name": "人民日报",
        "app_name_en": "People's Daily",
        "developer": "人民日报社",
        "category": "News & Magazines",
    },

    "cn.xinhua.news": {
        "app_name": "新华社",
        "app_name_en": "Xinhua News",
        "developer": "新华社",
        "category": "News & Magazines",
    },

    "com.ctr.app": {
        "app_name": "澎湃新闻",
        "app_name_en": "The Paper / Pengpai",
        "developer": "澎湃新闻",
        "category": "News & Magazines",
    },

    "com.tencent.reading": {
        "app_name": "QQ阅读",
        "app_name_en": "QQ Reader",
        "developer": "阅文集团",
        "category": "Books & Reference",
    },

    "com.jjwxc.reader": {
        "app_name": "晋江小说阅读",
        "app_name_en": "Jinjiang / JJWXC",
        "developer": "晋江文学城",
        "category": "Books & Reference",
    },

    "com.dragon.read": {
        "app_name": "番茄小说",
        "app_name_en": "Tomato Novel",
        "developer": "字节跳动",
        "category": "Books & Reference",
    },

    "com.happyelements.quickread": {
        "app_name": "追书神器",
        "app_name_en": "ZhuiShu",
        "developer": "追书神器",
        "category": "Books & Reference",
    },

    "com.taofen8.android": {
        "app_name": "豆瓣阅读",
        "app_name_en": "Douban Read",
        "developer": "豆瓣",
        "category": "Books & Reference",
    },

    "com.baidu.news": {
        "app_name": "百度新闻",
        "app_name_en": "Baidu News",
        "developer": "百度",
        "category": "News & Magazines",
    },

    "com.sankuai.meituan": {
        "app_name": "美团",
        "app_name_en": "Meituan",
        "developer": "美团",
        "category": "Food & Drink",
    },

    "com.sankuai.meituan.takeout": {
        "app_name": "美团外卖",
        "app_name_en": "Meituan Waimai",
        "developer": "美团",
        "category": "Food & Drink",
    },

    "me.ele": {
        "app_name": "饿了么",
        "app_name_en": "Ele.me",
        "developer": "阿里巴巴",
        "category": "Food & Drink",
    },

    "com.dianping.v1": {
        "app_name": "大众点评",
        "app_name_en": "Dianping",
        "developer": "美团",
        "category": "Food & Drink",
    },

    "com.lfk.lucky.android": {
        "app_name": "瑞幸咖啡",
        "app_name_en": "Luckin Coffee",
        "developer": "瑞幸咖啡",
        "category": "Food & Drink",
    },

    "com.yek.android.kfc": {
        "app_name": "肯德基",
        "app_name_en": "KFC China",
        "developer": "百胜中国",
        "category": "Food & Drink",
    },

    "com.mcdonalds.gma.cn": {
        "app_name": "麦当劳",
        "app_name_en": "McDonald's China",
        "developer": "金拱门",
        "category": "Food & Drink",
    },

    "com.starbucks.cn": {
        "app_name": "星巴克中国",
        "app_name_en": "Starbucks China",
        "developer": "星巴克",
        "category": "Food & Drink",
    },

    "com.xiangha": {
        "app_name": "下厨房",
        "app_name_en": "Xiachufang",
        "developer": "下厨房",
        "category": "Food & Drink",
    },

    "cn.missevan": {
        "app_name": "猫耳FM",
        "app_name_en": "MissEvan / Missevan",
        "developer": "猫耳FM",
        "category": "Entertainment",
    },

    "com.meituan.merchant": {
        "app_name": "美团开店宝",
        "app_name_en": "Meituan Merchant",
        "developer": "美团",
        "category": "Business",
    },

    "com.eleme": {
        "app_name": "饿了么商家版",
        "app_name_en": "Ele.me Merchant",
        "developer": "阿里巴巴",
        "category": "Business",
    },

    "com.ht.canyin": {
        "app_name": "哗啦啦",
        "app_name_en": "Hualala POS",
        "developer": "哗啦啦",
        "category": "Food & Drink",
    },

    "com.xingbianli.app": {
        "app_name": "便利蜂",
        "app_name_en": "Bianlifeng",
        "developer": "便利蜂",
        "category": "Food & Drink",
    },

    "com.hellobike.convenience": {
        "app_name": "盒马",
        "app_name_en": "Hema / Freshippo",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.mt.mtxx.mtxx": {
        "app_name": "美图秀秀",
        "app_name_en": "Meitu",
        "developer": "美图",
        "category": "Photography",
    },

    "ctrip.android.view": {
        "app_name": "携程旅行",
        "app_name_en": "Ctrip / Trip.com",
        "developer": "携程",
        "category": "Travel & Local",
    },

    "com.taobao.trip": {
        "app_name": "飞猪",
        "app_name_en": "Fliggy",
        "developer": "阿里巴巴",
        "category": "Travel & Local",
    },

    "com.sdo.cainiao.br": {
        "app_name": "滴滴出行",
        "app_name_en": "DiDi Chuxing",
        "developer": "滴滴",
        "category": "Maps & Navigation",
    },

    "com.didi.es.psngr": {
        "app_name": "花小猪打车",
        "app_name_en": "Huaxiaozhu",
        "developer": "滴滴",
        "category": "Maps & Navigation",
    },

    "com.didapinche.booking": {
        "app_name": "滴滴顺风车",
        "app_name_en": "DiDi Hitch",
        "developer": "滴滴",
        "category": "Travel & Local",
    },

    "com.didi.merchant": {
        "app_name": "滴滴车主",
        "app_name_en": "DiDi Driver",
        "developer": "滴滴",
        "category": "Maps & Navigation",
    },

    "com.mdd.car": {
        "app_name": "嘀嗒出行",
        "app_name_en": "Dida Chuxing",
        "developer": "嘀嗒出行",
        "category": "Travel & Local",
    },

    "com.autonavi.minimap": {
        "app_name": "高德地图",
        "app_name_en": "Amap / AutoNavi",
        "developer": "阿里巴巴",
        "category": "Maps & Navigation",
    },

    "com.mapbar.android.mapbarmap": {
        "app_name": "图吧导航",
        "app_name_en": "Mapbar",
        "developer": "图吧",
        "category": "Maps & Navigation",
    },

    "com.hellobike.atlas": {
        "app_name": "哈啰",
        "app_name_en": "Hello Inc.",
        "developer": "哈啰出行",
        "category": "Travel & Local",
    },

    "com.mobike.mobikeapp": {
        "app_name": "美团单车",
        "app_name_en": "Meituan Bike / Mobike",
        "developer": "美团",
        "category": "Travel & Local",
    },

    "so.ofo.labofo": {
        "app_name": "滴滴青桔",
        "app_name_en": "DiDi Qingju",
        "developer": "滴滴",
        "category": "Travel & Local",
    },

    "com.tongcheng.android": {
        "app_name": "同程旅行",
        "app_name_en": "Tongcheng Travel",
        "developer": "同程旅行",
        "category": "Travel & Local",
    },

    "com.elong.air": {
        "app_name": "艺龙旅行",
        "app_name_en": "eLong Travel",
        "developer": "同程旅行",
        "category": "Travel & Local",
    },

    "com.tuniu.app": {
        "app_name": "途牛旅游",
        "app_name_en": "Tuniu",
        "developer": "途牛",
        "category": "Travel & Local",
    },

    "com.mfw.roadbook": {
        "app_name": "马蜂窝",
        "app_name_en": "Mafengwo",
        "developer": "马蜂窝",
        "category": "Travel & Local",
    },

    "com.sdu.didi.psngr": {
        "app_name": "滴滴出行国际版",
        "app_name_en": "DiDi Rider",
        "developer": "滴滴",
        "category": "Maps & Navigation",
    },

    "com.cmcc.qingqi.android": {
        "app_name": "青桔单车",
        "app_name_en": "Qingju Bike",
        "developer": "滴滴",
        "category": "Travel & Local",
    },

    "cn.com.hichina.android": {
        "app_name": "阿里云",
        "app_name_en": "Alibaba Cloud",
        "developer": "阿里巴巴",
        "category": "Tools",
    },

    "com.baidu.netdisk": {
        "app_name": "百度网盘",
        "app_name_en": "Baidu Netdisk",
        "developer": "百度",
        "category": "Productivity",
    },

    "com.tencent.weiyun": {
        "app_name": "微云",
        "app_name_en": "Weiyun",
        "developer": "腾讯",
        "category": "Productivity",
    },

    "cn.wps.moffice_eng": {
        "app_name": "WPS Office",
        "app_name_en": "WPS Office",
        "developer": "金山办公",
        "category": "Productivity",
    },

    "com.intsig.camscanner": {
        "app_name": "扫描全能王",
        "app_name_en": "CamScanner",
        "developer": "合合信息",
        "category": "Productivity",
    },

    "com.intsig.lic": {
        "app_name": "名片全能王",
        "app_name_en": "CamCard",
        "developer": "合合信息",
        "category": "Business",
    },

    "com.moji.mjweather": {
        "app_name": "墨迹天气",
        "app_name_en": "Moji Weather",
        "developer": "墨迹天气",
        "category": "Weather",
    },

    "com.iflytek.inputmethod": {
        "app_name": "讯飞输入法",
        "app_name_en": "iFlytek Input",
        "developer": "科大讯飞",
        "category": "Tools",
    },

    "com.sohu.inputmethod.sogou": {
        "app_name": "搜狗输入法",
        "app_name_en": "Sogou Input",
        "developer": "搜狗",
        "category": "Tools",
    },

    "com.baidu.input": {
        "app_name": "百度输入法",
        "app_name_en": "Baidu Input",
        "developer": "百度",
        "category": "Tools",
    },

    "com.youdao.dict": {
        "app_name": "网易有道词典",
        "app_name_en": "Youdao Dictionary",
        "developer": "网易",
        "category": "Education",
    },

    "com.youdao.note": {
        "app_name": "有道云笔记",
        "app_name_en": "Youdao Note",
        "developer": "网易",
        "category": "Productivity",
    },

    "com.qingting.av": {
        "app_name": "讯飞听见",
        "app_name_en": "iFlytek Hear",
        "developer": "科大讯飞",
        "category": "Productivity",
    },

    "com.tencent.docs": {
        "app_name": "腾讯文档",
        "app_name_en": "Tencent Docs",
        "developer": "腾讯",
        "category": "Productivity",
    },

    "com.alibaba.aliyun": {
        "app_name": "阿里云",
        "app_name_en": "Alibaba Cloud",
        "developer": "阿里巴巴",
        "category": "Tools",
    },

    "com.baidu.searchbox": {
        "app_name": "百度",
        "app_name_en": "Baidu Search",
        "developer": "百度",
        "category": "Tools",
    },

    "com.baidu.searchbox.lite": {
        "app_name": "百度极速版",
        "app_name_en": "Baidu Lite",
        "developer": "百度",
        "category": "Tools",
    },

    "com.tencent.wifihelper": {
        "app_name": "腾讯WiFi管家",
        "app_name_en": "Tencent WiFi Manager",
        "developer": "腾讯",
        "category": "Tools",
    },

    "com.cleanmaster.mguard": {
        "app_name": "猎豹清理大师",
        "app_name_en": "Clean Master",
        "developer": "猎豹移动",
        "category": "Tools",
    },

    "com.cleanmaster.security": {
        "app_name": "猎豹安全大师",
        "app_name_en": "CM Security",
        "developer": "猎豹移动",
        "category": "Tools",
    },

    "com.qihoo360.mobilesafe": {
        "app_name": "360手机卫士",
        "app_name_en": "360 Mobile Security",
        "developer": "奇虎360",
        "category": "Tools",
    },

    "com.qihoo.appstore": {
        "app_name": "360手机助手",
        "app_name_en": "360 App Store",
        "developer": "奇虎360",
        "category": "Tools",
    },

    "com.qihoo360.camera": {
        "app_name": "360智能摄像机",
        "app_name_en": "360 Smart Camera",
        "developer": "奇虎360",
        "category": "Tools",
    },

    "com.xt.retouch": {
        "app_name": "醒图",
        "app_name_en": "Xingtu / Hypic",
        "developer": "字节跳动",
        "category": "Photography",
    },

    "com.meitu.meiyancamera": {
        "app_name": "美颜相机",
        "app_name_en": "Meiyan Camera",
        "developer": "美图",
        "category": "Photography",
    },

    "com.cam001.selfie": {
        "app_name": "潮自拍",
        "app_name_en": "Trendy Selfie",
        "developer": "美图",
        "category": "Photography",
    },

    "com.yaozh.mv": {
        "app_name": "黄油相机",
        "app_name_en": "ButterCam",
        "developer": "黄油相机",
        "category": "Photography",
    },

    "com.picsart.studio": {
        "app_name": "PicsArt",
        "app_name_en": "PicsArt",
        "developer": "PicsArt",
        "category": "Photography",
    },

    "com.bytedance.lightenshare": {
        "app_name": "轻颜相机",
        "app_name_en": "Ulike / Lighten",
        "developer": "字节跳动",
        "category": "Photography",
    },

    "com.netease.mobimail": {
        "app_name": "网易邮箱大师",
        "app_name_en": "NetEase Mail Master",
        "developer": "网易",
        "category": "Productivity",
    },

    "com.netease.mail": {
        "app_name": "网易邮箱",
        "app_name_en": "NetEase Mail",
        "developer": "网易",
        "category": "Productivity",
    },

    "com.tencent.potential": {
        "app_name": "腾讯手机管家极速版",
        "app_name_en": "Tencent Manager Lite",
        "developer": "腾讯",
        "category": "Tools",
    },

    "com.android.contacts": {
        "app_name": "联系人",
        "app_name_en": "Contacts",
        "developer": "Android",
        "category": "Communication",
    },

    "com.tencent.mtt": {
        "app_name": "QQ浏览器",
        "app_name_en": "QQ Browser",
        "developer": "腾讯",
        "category": "Browser",
    },

    "com.baidu.browser.apps": {
        "app_name": "百度浏览器",
        "app_name_en": "Baidu Browser",
        "developer": "百度",
        "category": "Browser",
    },

    "com.qihoo.browser": {
        "app_name": "360浏览器",
        "app_name_en": "360 Browser",
        "developer": "奇虎360",
        "category": "Browser",
    },

    "com.sogou.browser": {
        "app_name": "搜狗浏览器",
        "app_name_en": "Sogou Browser",
        "developer": "搜狗",
        "category": "Browser",
    },

    "com.quark.browser": {
        "app_name": "夸克",
        "app_name_en": "Quark Browser",
        "developer": "阿里巴巴",
        "category": "Browser",
    },

    "com.ijinshan.browser_fast": {
        "app_name": "猎豹浏览器",
        "app_name_en": "Cheetah Browser",
        "developer": "猎豹移动",
        "category": "Browser",
    },

    "com.android.chrome": {
        "app_name": "Chrome浏览器",
        "app_name_en": "Chrome",
        "developer": "Google",
        "category": "Browser",
    },

    "com.tencent.tmgp.sgame": {
        "app_name": "王者荣耀",
        "app_name_en": "Honor of Kings",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.pubgmhd": {
        "app_name": "和平精英",
        "app_name_en": "Game for Peace / PUBG Mobile CN",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.cod": {
        "app_name": "使命召唤手游",
        "app_name_en": "Call of Duty Mobile CN",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.netease.onmyoji": {
        "app_name": "阴阳师",
        "app_name_en": "Onmyoji",
        "developer": "网易",
        "category": "Game",
    },

    "com.hypergryph.arknights": {
        "app_name": "明日方舟",
        "app_name_en": "Arknights",
        "developer": "鹰角网络",
        "category": "Game",
    },

    "com.netease.id5": {
        "app_name": "第五人格",
        "app_name_en": "Identity V",
        "developer": "网易",
        "category": "Game",
    },

    "com.netease.party": {
        "app_name": "蛋仔派对",
        "app_name_en": "Eggy Party",
        "developer": "网易",
        "category": "Game",
    },

    "com.netease.xyq": {
        "app_name": "梦幻西游",
        "app_name_en": "Fantasy Westward Journey",
        "developer": "网易",
        "category": "Game",
    },

    "com.netease.dhxy": {
        "app_name": "大话西游",
        "app_name_en": "Westward Journey Online II",
        "developer": "网易",
        "category": "Game",
    },

    "com.tencent.tmgp.speedmobile": {
        "app_name": "QQ飞车",
        "app_name_en": "QQ Speed",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.dfm": {
        "app_name": "三角洲行动",
        "app_name_en": "Delta Force Mobile",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.qqgame": {
        "app_name": "QQ游戏",
        "app_name_en": "QQ Game Center",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.happyfish": {
        "app_name": "欢乐斗地主",
        "app_name_en": "Happy Landlord",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.qqdzz": {
        "app_name": "欢乐斗地主",
        "app_name_en": "Happy Landlord",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.happymj": {
        "app_name": "欢乐麻将",
        "app_name_en": "Happy Mahjong",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.happyelements.happyeliminate": {
        "app_name": "开心消消乐",
        "app_name_en": "Happy Elimination",
        "developer": "乐元素",
        "category": "Game",
    },

    "com.netease.l10": {
        "app_name": "我的世界中国版",
        "app_name_en": "Minecraft China",
        "developer": "网易",
        "category": "Game",
    },

    "com.tencent.tmgp.wefly": {
        "app_name": "光与夜之恋",
        "app_name_en": "Light and Night",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.pape.nikke": {
        "app_name": "胜利女神：新的希望",
        "app_name_en": "Goddess of Victory: Nikke CN",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.wuxia": {
        "app_name": "天涯明月刀手游",
        "app_name_en": "Moonlight Blade Mobile",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.projectg": {
        "app_name": "金铲铲之战",
        "app_name_en": "Teamfight Tactics Mobile",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.qqx5": {
        "app_name": "QQ炫舞",
        "app_name_en": "QQ Dance",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.netease.kw": {
        "app_name": "荒野行动",
        "app_name_en": "Knives Out / Wild Action",
        "developer": "网易",
        "category": "Game",
    },

    "com.netease.bx.nzm": {
        "app_name": "逆战",
        "app_name_en": "Assault Fire",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.netease.hyxd": {
        "app_name": "荒野行动",
        "app_name_en": "Knives Out",
        "developer": "网易",
        "category": "Game",
    },

    "com.lilithgames.rok.cn": {
        "app_name": "万国觉醒",
        "app_name_en": "Rise of Kingdoms",
        "developer": "莉莉丝",
        "category": "Game",
    },

    "com.lilithgames.afk.cn": {
        "app_name": "剑与远征",
        "app_name_en": "AFK Arena",
        "developer": "莉莉丝",
        "category": "Game",
    },

    "com.tencent.tmgp.starp": {
        "app_name": "元梦之星",
        "app_name_en": "DreamStar",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.netease.tzz": {
        "app_name": "天谕",
        "app_name_en": "Revelation",
        "developer": "网易",
        "category": "Game",
    },

    "com.herogame.gplay.lastdayrulessurvival": {
        "app_name": "末日生存",
        "app_name_en": "Last Day Rules",
        "developer": "Hero Game",
        "category": "Game",
    },

    "com.tencent.tmgp.mtp": {
        "app_name": "魂斗罗：归来",
        "app_name_en": "Contra Returns",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.dragonnest": {
        "app_name": "龙之谷手游",
        "app_name_en": "Dragon Nest Mobile",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.netease.egame": {
        "app_name": "率土之滨",
        "app_name_en": "Infinite Borders",
        "developer": "网易",
        "category": "Game",
    },

    "com.tencent.tmgp.jxqy": {
        "app_name": "剑侠情缘",
        "app_name_en": "JX Online",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.wanmei.wmsj": {
        "app_name": "完美世界",
        "app_name_en": "Perfect World Mobile",
        "developer": "完美世界",
        "category": "Game",
    },

    "com.tencent.tmgp.zhuxian": {
        "app_name": "诛仙",
        "app_name_en": "Jade Dynasty",
        "developer": "完美世界",
        "category": "Game",
    },

    "com.yongshi.wsz.qq": {
        "app_name": "三国杀",
        "app_name_en": "Sanguosha",
        "developer": "游卡桌游",
        "category": "Game",
    },

    "com.pwrd.xy2": {
        "app_name": "新笑傲江湖",
        "app_name_en": "New Swordsman",
        "developer": "完美世界",
        "category": "Game",
    },

    "com.tencent.tmgp.wuxia": {
        "app_name": "天涯明月刀",
        "app_name_en": "Moonlight Blade",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.shimmergames.porcn": {
        "app_name": "波西亚时光",
        "app_name_en": "My Time at Portia",
        "developer": "帕斯亚科技",
        "category": "Game",
    },

    "com.tencent.tmgp.wuxia2": {
        "app_name": "剑网3",
        "app_name_en": "JX3 Online",
        "developer": "金山",
        "category": "Game",
    },

    "com.igg.android": {
        "app_name": "王国纪元",
        "app_name_en": "Lords Mobile CN",
        "developer": "IGG",
        "category": "Game",
    },

    "com.xd.identityv": {
        "app_name": "第五人格",
        "app_name_en": "Identity V",
        "developer": "网易",
        "category": "Game",
    },

    "com.funcell.aoi.cn": {
        "app_name": "碧蓝航线",
        "app_name_en": "Azur Lane",
        "developer": "哔哩哔哩",
        "category": "Game",
    },

    "com.netease.yys2": {
        "app_name": "决战！平安京",
        "app_name_en": "Onmyoji Arena",
        "developer": "网易",
        "category": "Game",
    },

    "com.tencent.tmgp.pubg": {
        "app_name": "绝地求生手游",
        "app_name_en": "PUBG Mobile",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.arenaofvalor": {
        "app_name": "传说对决",
        "app_name_en": "Arena of Valor",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.netease.yjwq": {
        "app_name": "永劫无间手游",
        "app_name_en": "Naraka: Bladepoint Mobile",
        "developer": "网易",
        "category": "Game",
    },

    "com.tencent.tmgp.yxzj": {
        "app_name": "王者荣耀国际版",
        "app_name_en": "Arena of Valor",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.jx3": {
        "app_name": "剑侠世界3",
        "app_name_en": "JX World 3",
        "developer": "金山",
        "category": "Game",
    },

    "com.centauri.eyou.smbb": {
        "app_name": "植物大战僵尸2中国版",
        "app_name_en": "PvZ 2 CN",
        "developer": "拓维信息",
        "category": "Game",
    },

    "com.popcap.pvz2cthd": {
        "app_name": "植物大战僵尸2",
        "app_name_en": "Plants vs Zombies 2",
        "developer": "拓维信息",
        "category": "Game",
    },

    "com.ea.game.pvz2_row": {
        "app_name": "植物大战僵尸2国际版",
        "app_name_en": "PvZ 2 International",
        "developer": "EA",
        "category": "Game",
    },

    "com.tencent.tmgp.supercell.clashroyale": {
        "app_name": "皇室战争",
        "app_name_en": "Clash Royale CN",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.supercell.clashofclans": {
        "app_name": "部落冲突",
        "app_name_en": "Clash of Clans CN",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.supercell.brawlstars": {
        "app_name": "荒野乱斗",
        "app_name_en": "Brawl Stars CN",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.projectc": {
        "app_name": "无畏契约手游",
        "app_name_en": "VALORANT Mobile CN",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.tmgp.xgame3": {
        "app_name": "暗区突围",
        "app_name_en": "Arena Breakout",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.stc.nm": {
        "app_name": "黎明觉醒：生机",
        "app_name_en": "Undawn",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.netease.ma20": {
        "app_name": "光遇",
        "app_name_en": "Sky: Children of the Light CN",
        "developer": "网易",
        "category": "Game",
    },

    "com.tencent.tmgp.djs": {
        "app_name": "地下城与勇士手游",
        "app_name_en": "DNF Mobile",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.netease.rxjh": {
        "app_name": "逆水寒",
        "app_name_en": "Justice Online",
        "developer": "网易",
        "category": "Game",
    },

    "com.gotokeep.keep": {
        "app_name": "Keep",
        "app_name_en": "Keep",
        "developer": "北京卡路里科技",
        "category": "Health & Fitness",
    },

    "com.codoon.health": {
        "app_name": "咕咚",
        "app_name_en": "Codoon",
        "developer": "咕咚",
        "category": "Health & Fitness",
    },

    "com.thejoyrun.joyrunner": {
        "app_name": "悦跑圈",
        "app_name_en": "Joyrun",
        "developer": "悦跑圈",
        "category": "Health & Fitness",
    },

    "com.xiaobu.joyrun": {
        "app_name": "小步点",
        "app_name_en": "Xiaobu",
        "developer": "小步点",
        "category": "Health & Fitness",
    },

    "com.boohee.one": {
        "app_name": "薄荷健康",
        "app_name_en": "Boohee",
        "developer": "薄荷科技",
        "category": "Health & Fitness",
    },

    "com.hypergryph.healthy": {
        "app_name": "好轻",
        "app_name_en": "Haoqing Scale",
        "developer": "好轻",
        "category": "Health & Fitness",
    },

    "com.dnurse.patient.android": {
        "app_name": "糖护士",
        "app_name_en": "Dnurse",
        "developer": "糖护士",
        "category": "Medical",
    },

    "com.pingan.health": {
        "app_name": "平安健康",
        "app_name_en": "Ping An Health / PA Good Doctor",
        "developer": "平安健康",
        "category": "Medical",
    },

    "com.dxy.idoctor": {
        "app_name": "丁香医生",
        "app_name_en": "DXY Doctor",
        "developer": "丁香园",
        "category": "Medical",
    },

    "com.yuntang.healthy": {
        "app_name": "麦迪健康",
        "app_name_en": "MyDi Health",
        "developer": "麦迪健康",
        "category": "Medical",
    },

    "cn.dxy.medicinehelper": {
        "app_name": "用药助手",
        "app_name_en": "Medication Assistant",
        "developer": "丁香园",
        "category": "Medical",
    },

    "cn.dxy.android.aspirin": {
        "app_name": "丁香园",
        "app_name_en": "DXY",
        "developer": "丁香园",
        "category": "Medical",
    },

    "com.haodf.patient": {
        "app_name": "好大夫在线",
        "app_name_en": "Haodf Patient",
        "developer": "好大夫在线",
        "category": "Medical",
    },

    "com.haodf.doctor": {
        "app_name": "好大夫医生版",
        "app_name_en": "Haodf Doctor",
        "developer": "好大夫在线",
        "category": "Medical",
    },

    "com.weidong.health": {
        "app_name": "微医",
        "app_name_en": "WeDoctor",
        "developer": "微医",
        "category": "Medical",
    },

    "com.chunyu.doctor": {
        "app_name": "春雨医生",
        "app_name_en": "Chunyu Doctor",
        "developer": "春雨医生",
        "category": "Medical",
    },

    "com.xes.ios.jzt": {
        "app_name": "学而思",
        "app_name_en": "Xueersi / TAL",
        "developer": "好未来",
        "category": "Education",
    },

    "com.xes.teacher": {
        "app_name": "学而思培优",
        "app_name_en": "Xueersi Peiyou",
        "developer": "好未来",
        "category": "Education",
    },

    "com.yuanfudao.android": {
        "app_name": "猿辅导",
        "app_name_en": "Yuanfudao",
        "developer": "猿力教育",
        "category": "Education",
    },

    "com.zuoyebang.airclass": {
        "app_name": "作业帮",
        "app_name_en": "Zuoyebang",
        "developer": "作业帮",
        "category": "Education",
    },

    "com.zuoyebang.zhushou": {
        "app_name": "作业帮家长版",
        "app_name_en": "Zuoyebang Parent",
        "developer": "作业帮",
        "category": "Education",
    },

    "com.xiaoyuan.search": {
        "app_name": "小猿搜题",
        "app_name_en": "Xiaoyuan Search",
        "developer": "猿力教育",
        "category": "Education",
    },

    "com.xiaoyuan.orange": {
        "app_name": "猿题库",
        "app_name_en": "Yuan Question Bank",
        "developer": "猿力教育",
        "category": "Education",
    },

    "com.jiongji.andriod.card": {
        "app_name": "百词斩",
        "app_name_en": "Baicizhan",
        "developer": "成都超有爱科技",
        "category": "Education",
    },

    "com.duolingo": {
        "app_name": "多邻国",
        "app_name_en": "Duolingo",
        "developer": "Duolingo",
        "category": "Education",
    },

    "com.liulishuo.engzo": {
        "app_name": "流利说",
        "app_name_en": "Liulishuo / LAIX",
        "developer": "流利说",
        "category": "Education",
    },

    "com.luojilab.player": {
        "app_name": "得到",
        "app_name_en": "Dedao / iGet",
        "developer": "得到",
        "category": "Education",
    },

    "com.luojilab.vdodownload": {
        "app_name": "得到",
        "app_name_en": "Dedao",
        "developer": "得到",
        "category": "Education",
    },

    "com.chaoxing.mobile": {
        "app_name": "超星学习通",
        "app_name_en": "Chaoxing / SuperStar",
        "developer": "超星",
        "category": "Education",
    },

    "com.zhihu.know": {
        "app_name": "知乎大学",
        "app_name_en": "Zhihu University",
        "developer": "知乎",
        "category": "Education",
    },

    "com.wmzq.mobile": {
        "app_name": "腾讯课堂",
        "app_name_en": "Tencent Class",
        "developer": "腾讯",
        "category": "Education",
    },

    "com.netease.open": {
        "app_name": "网易公开课",
        "app_name_en": "NetEase Open Course",
        "developer": "网易",
        "category": "Education",
    },

    "com.netease.cloudclass": {
        "app_name": "网易云课堂",
        "app_name_en": "NetEase Cloud Classroom",
        "developer": "网易",
        "category": "Education",
    },

    "com.genshuixue.teacher": {
        "app_name": "跟谁学",
        "app_name_en": "GSX / Gaotu",
        "developer": "高途",
        "category": "Education",
    },

    "com.yy.onion": {
        "app_name": "洋葱学园",
        "app_name_en": "Onion Academy",
        "developer": "洋葱学园",
        "category": "Education",
    },

    "com.niceboost.vip": {
        "app_name": "作业帮直播课",
        "app_name_en": "Zuoyebang Live",
        "developer": "作业帮",
        "category": "Education",
    },

    "com.hujiang.njj": {
        "app_name": "沪江",
        "app_name_en": "Hujiang",
        "developer": "沪江",
        "category": "Education",
    },

    "com.hujiang.cctalk": {
        "app_name": "CCtalk",
        "app_name_en": "CCtalk",
        "developer": "沪江",
        "category": "Education",
    },

    "com.zybang.parent": {
        "app_name": "作业帮",
        "app_name_en": "Zuoyebang",
        "developer": "作业帮",
        "category": "Education",
    },

    "com.xiaoniuhy.student": {
        "app_name": "小牛学堂",
        "app_name_en": "XiaoNiu Academy",
        "developer": "小牛学堂",
        "category": "Education",
    },

    "com.genshuixue.student": {
        "app_name": "跟谁学学生版",
        "app_name_en": "Gaotu Student",
        "developer": "高途",
        "category": "Education",
    },

    "com.icourse.app": {
        "app_name": "爱课程",
        "app_name_en": "iCourse",
        "developer": "爱课程",
        "category": "Education",
    },

    "com.coursera.android": {
        "app_name": "Coursera",
        "app_name_en": "Coursera",
        "developer": "Coursera",
        "category": "Education",
    },

    "cn.xuexi.android": {
        "app_name": "学习强国",
        "app_name_en": "Xuexi Qiangguo",
        "developer": "中央宣传部",
        "category": "Education",
    },

    "com.lianjia.beike": {
        "app_name": "贝壳找房",
        "app_name_en": "Beike / KE Holdings",
        "developer": "贝壳找房",
        "category": "House & Home",
    },

    "com.lianjia.home": {
        "app_name": "链家",
        "app_name_en": "Lianjia",
        "developer": "贝壳找房",
        "category": "House & Home",
    },

    "com.anjuke.android.app": {
        "app_name": "安居客",
        "app_name_en": "Anjuke",
        "developer": "58同城",
        "category": "House & Home",
    },

    "com.fang.soufun": {
        "app_name": "房天下",
        "app_name_en": "Fang.com",
        "developer": "房天下",
        "category": "House & Home",
    },

    "com.ziroom.ziroomcustomer": {
        "app_name": "自如",
        "app_name_en": "Ziroom",
        "developer": "自如",
        "category": "House & Home",
    },

    "com.soufun.app": {
        "app_name": "房天下",
        "app_name_en": "Fang",
        "developer": "房天下",
        "category": "House & Home",
    },

    "com.iwjw.app": {
        "app_name": "我爱我家",
        "app_name_en": "5i5j / Woaiwojia",
        "developer": "我爱我家",
        "category": "House & Home",
    },

    "com.centaline.android": {
        "app_name": "中原地产",
        "app_name_en": "Centaline",
        "developer": "中原地产",
        "category": "House & Home",
    },

    "com.tujia.app": {
        "app_name": "途家民宿",
        "app_name_en": "Tujia",
        "developer": "途家",
        "category": "Travel & Local",
    },

    "com.xiaozhu.app": {
        "app_name": "小猪民宿",
        "app_name_en": "Xiaozhu",
        "developer": "小猪",
        "category": "Travel & Local",
    },

    "com.tujia.hotel": {
        "app_name": "途家",
        "app_name_en": "Tujia",
        "developer": "途家",
        "category": "Travel & Local",
    },

    "com.sf.activity": {
        "app_name": "顺丰速运",
        "app_name_en": "SF Express",
        "developer": "顺丰",
        "category": "Productivity",
    },

    "com.cainiao.wireless": {
        "app_name": "菜鸟",
        "app_name_en": "Cainiao",
        "developer": "阿里巴巴",
        "category": "Productivity",
    },

    "com.cainiao.guoguo": {
        "app_name": "菜鸟裹裹",
        "app_name_en": "Cainiao Guoguo",
        "developer": "阿里巴巴",
        "category": "Productivity",
    },

    "com.lalamove.huolala.client": {
        "app_name": "货拉拉",
        "app_name_en": "Lalamove / Huolala",
        "developer": "货拉拉",
        "category": "Maps & Navigation",
    },

    "com.zhongtong.app": {
        "app_name": "中通快递",
        "app_name_en": "ZTO Express",
        "developer": "中通快递",
        "category": "Productivity",
    },

    "com.yto.stop": {
        "app_name": "圆通速递",
        "app_name_en": "YTO Express",
        "developer": "圆通速递",
        "category": "Productivity",
    },

    "com.yunda.androidapp": {
        "app_name": "韵达速递",
        "app_name_en": "Yunda Express",
        "developer": "韵达速递",
        "category": "Productivity",
    },

    "com.sto.android": {
        "app_name": "申通快递",
        "app_name_en": "STO Express",
        "developer": "申通快递",
        "category": "Productivity",
    },

    "com.jtexpress.app": {
        "app_name": "极兔速递",
        "app_name_en": "J&T Express",
        "developer": "极兔速递",
        "category": "Productivity",
    },

    "com.deppon.app": {
        "app_name": "德邦快递",
        "app_name_en": "Deppon Express",
        "developer": "德邦快递",
        "category": "Productivity",
    },

    "com.jingdong.logistics": {
        "app_name": "京东物流",
        "app_name_en": "JD Logistics",
        "developer": "京东",
        "category": "Productivity",
    },

    "com.kuaidi100.quick": {
        "app_name": "快递100",
        "app_name_en": "Kuaidi100",
        "developer": "快递100",
        "category": "Productivity",
    },

    "com.ichinait.guibao": {
        "app_name": "快递柜",
        "app_name_en": "Express Locker",
        "developer": "蜂巢",
        "category": "Productivity",
    },

    "com.fcbox.hivebox": {
        "app_name": "丰巢",
        "app_name_en": "Hive Box / Fengchao",
        "developer": "丰巢",
        "category": "Productivity",
    },

    "com.dada.passenger": {
        "app_name": "达达秒送",
        "app_name_en": "Dada Now",
        "developer": "达达",
        "category": "Shopping",
    },

    "com.flashbox.app": {
        "app_name": "闪送",
        "app_name_en": "Shansong",
        "developer": "闪送",
        "category": "Maps & Navigation",
    },

    "com.uu.client": {
        "app_name": "UU跑腿",
        "app_name_en": "UU Errand",
        "developer": "UU跑腿",
        "category": "Maps & Navigation",
    },

    "com.wuba": {
        "app_name": "58同城",
        "app_name_en": "58.com",
        "developer": "58同城",
        "category": "Lifestyle",
    },

    "com.ganji.android": {
        "app_name": "赶集网",
        "app_name_en": "Ganji",
        "developer": "58同城",
        "category": "Lifestyle",
    },

    "com.zhilianzhaopin.app": {
        "app_name": "智联招聘",
        "app_name_en": "Zhaopin",
        "developer": "智联招聘",
        "category": "Business",
    },

    "com.lietou.mobile": {
        "app_name": "猎聘",
        "app_name_en": "Liepin",
        "developer": "猎聘",
        "category": "Business",
    },

    "com.zhipin.app": {
        "app_name": "Boss直聘",
        "app_name_en": "Boss Zhipin",
        "developer": "Boss直聘",
        "category": "Business",
    },

    "com.zhaopin.social": {
        "app_name": "智联招聘",
        "app_name_en": "Zhaopin",
        "developer": "智联招聘",
        "category": "Business",
    },

    "com.job.android": {
        "app_name": "前程无忧",
        "app_name_en": "51Job",
        "developer": "前程无忧",
        "category": "Business",
    },

    "com.chinahr.android": {
        "app_name": "中华英才网",
        "app_name_en": "ChinaHR",
        "developer": "中华英才网",
        "category": "Business",
    },

    "com.lagou.app": {
        "app_name": "拉勾招聘",
        "app_name_en": "Lagou",
        "developer": "拉勾",
        "category": "Business",
    },

    "com.mianbaoban.app": {
        "app_name": "脉脉",
        "app_name_en": "Maimai",
        "developer": "脉脉",
        "category": "Business",
    },

    "com.dajie.app": {
        "app_name": "大街",
        "app_name_en": "Dajie",
        "developer": "大街",
        "category": "Business",
    },

    "com.xiwu.tao": {
        "app_name": "淘工作",
        "app_name_en": "Tao Jobs",
        "developer": "阿里巴巴",
        "category": "Business",
    },

    "com.xiaomi.smarthome": {
        "app_name": "米家",
        "app_name_en": "Mi Home / Xiaomi Home",
        "developer": "小米",
        "category": "Lifestyle",
    },

    "com.xiaomi.router": {
        "app_name": "小米WiFi",
        "app_name_en": "Mi WiFi",
        "developer": "小米",
        "category": "Tools",
    },

    "com.huawei.smarthome": {
        "app_name": "华为智慧生活",
        "app_name_en": "Huawei Smart Life / AI Life",
        "developer": "华为",
        "category": "Lifestyle",
    },

    "com.haier.uhome": {
        "app_name": "海尔智家",
        "app_name_en": "Haier Smart Home",
        "developer": "海尔",
        "category": "Lifestyle",
    },

    "com.midea.ai": {
        "app_name": "美的美居",
        "app_name_en": "Midea Smart Home",
        "developer": "美的",
        "category": "Lifestyle",
    },

    "com.smart.gree": {
        "app_name": "格力+",
        "app_name_en": "Gree+",
        "developer": "格力",
        "category": "Lifestyle",
    },

    "com.tcl.smart": {
        "app_name": "TCL智慧生活",
        "app_name_en": "TCL Smart Home",
        "developer": "TCL",
        "category": "Lifestyle",
    },

    "com.hisense.smart": {
        "app_name": "海信爱家",
        "app_name_en": "Hisense Smart Home",
        "developer": "海信",
        "category": "Lifestyle",
    },

    "com.yeelight.cherry": {
        "app_name": "Yeelight",
        "app_name_en": "Yeelight",
        "developer": "亿联客",
        "category": "Lifestyle",
    },

    "com.roborock.smart": {
        "app_name": "石头",
        "app_name_en": "Roborock",
        "developer": "石头科技",
        "category": "Lifestyle",
    },

    "com.eco.global.app": {
        "app_name": "萤石云视频",
        "app_name_en": "EZVIZ",
        "developer": "海康威视",
        "category": "Tools",
    },

    "com.hikvision.open": {
        "app_name": "海康互联",
        "app_name_en": "Hik-Connect",
        "developer": "海康威视",
        "category": "Tools",
    },

    "com.imou.life": {
        "app_name": "乐橙",
        "app_name_en": "Imou Life",
        "developer": "大华",
        "category": "Tools",
    },

    "com.greenpoints.android": {
        "app_name": "中国移动",
        "app_name_en": "China Mobile",
        "developer": "中国移动",
        "category": "Tools",
    },

    "com.sinovatech.unicom.ui": {
        "app_name": "中国联通",
        "app_name_en": "China Unicom",
        "developer": "中国联通",
        "category": "Tools",
    },

    "cn.com.ctc.telecom": {
        "app_name": "中国电信",
        "app_name_en": "China Telecom",
        "developer": "中国电信",
        "category": "Tools",
    },

    "com.chinatelecom.bestpayclient": {
        "app_name": "翼支付",
        "app_name_en": "BestPay / Yizhifu",
        "developer": "中国电信",
        "category": "Finance",
    },

    "com.cmcc.kuanbo": {
        "app_name": "咪咕视频",
        "app_name_en": "Migu Video",
        "developer": "中国移动",
        "category": "Entertainment",
    },

    "com.cmcc.migumusic": {
        "app_name": "咪咕音乐",
        "app_name_en": "Migu Music",
        "developer": "中国移动",
        "category": "Music & Audio",
    },

    "com.cmcc.migubook": {
        "app_name": "咪咕阅读",
        "app_name_en": "Migu Reader",
        "developer": "中国移动",
        "category": "Books & Reference",
    },

    "com.cmcc.qtouch": {
        "app_name": "和包",
        "app_name_en": "HeBao / CM Pay",
        "developer": "中国移动",
        "category": "Finance",
    },

    "cn.com.ctc.work": {
        "app_name": "电信营业厅",
        "app_name_en": "Telecom Business Hall",
        "developer": "中国电信",
        "category": "Tools",
    },

    "com.sinovatech.unicom.work": {
        "app_name": "联通营业厅",
        "app_name_en": "Unicom Business Hall",
        "developer": "中国联通",
        "category": "Tools",
    },

    "com.greenpoints.work": {
        "app_name": "移动营业厅",
        "app_name_en": "Mobile Business Hall",
        "developer": "中国移动",
        "category": "Tools",
    },

    "com.miui.home": {
        "app_name": "MIUI桌面",
        "app_name_en": "MIUI Home",
        "developer": "小米",
        "category": "System",
    },

    "com.miui.securitycenter": {
        "app_name": "手机管家",
        "app_name_en": "Security Center",
        "developer": "小米",
        "category": "System",
    },

    "com.miui.cleaner": {
        "app_name": "垃圾清理",
        "app_name_en": "Cleaner",
        "developer": "小米",
        "category": "System",
    },

    "com.miui.gallery": {
        "app_name": "相册",
        "app_name_en": "Mi Gallery",
        "developer": "小米",
        "category": "System",
    },

    "com.miui.video": {
        "app_name": "小米视频",
        "app_name_en": "Mi Video",
        "developer": "小米",
        "category": "Entertainment",
    },

    "com.miui.player": {
        "app_name": "音乐",
        "app_name_en": "Mi Music",
        "developer": "小米",
        "category": "Music & Audio",
    },

    "com.miui.notes": {
        "app_name": "便签",
        "app_name_en": "Mi Notes",
        "developer": "小米",
        "category": "System",
    },

    "com.miui.calculator": {
        "app_name": "计算器",
        "app_name_en": "Mi Calculator",
        "developer": "小米",
        "category": "System",
    },

    "com.miui.compass": {
        "app_name": "指南针",
        "app_name_en": "Mi Compass",
        "developer": "小米",
        "category": "System",
    },

    "com.miui.weather2": {
        "app_name": "天气",
        "app_name_en": "Mi Weather",
        "developer": "小米",
        "category": "Weather",
    },

    "com.miui.cloudservice": {
        "app_name": "小米云服务",
        "app_name_en": "Mi Cloud",
        "developer": "小米",
        "category": "System",
    },

    "com.miui.backup": {
        "app_name": "小米换机",
        "app_name_en": "Mi Mover",
        "developer": "小米",
        "category": "Tools",
    },

    "com.miui.screenrecorder": {
        "app_name": "屏幕录制",
        "app_name_en": "Screen Recorder",
        "developer": "小米",
        "category": "System",
    },

    "com.miui.voiceassist": {
        "app_name": "小爱同学",
        "app_name_en": "XiaoAi Assistant",
        "developer": "小米",
        "category": "Tools",
    },

    "com.xiaomi.account": {
        "app_name": "小米账户",
        "app_name_en": "Xiaomi Account",
        "developer": "小米",
        "category": "System",
    },

    "com.xiaomi.gamecenter": {
        "app_name": "小米游戏中心",
        "app_name_en": "Mi Game Center",
        "developer": "小米",
        "category": "Game",
    },

    "com.xiaomi.market": {
        "app_name": "小米应用商店",
        "app_name_en": "Mi App Store",
        "developer": "小米",
        "category": "Tools",
    },

    "com.xiaomi.community": {
        "app_name": "小米社区",
        "app_name_en": "Mi Community",
        "developer": "小米",
        "category": "Social",
    },

    "com.xiaomi.miplay": {
        "app_name": "小米视频",
        "app_name_en": "Mi Play",
        "developer": "小米",
        "category": "Entertainment",
    },

    "com.xiaomi.scanner": {
        "app_name": "扫一扫",
        "app_name_en": "Mi Scanner",
        "developer": "小米",
        "category": "Tools",
    },

    "com.xiaomi.mico": {
        "app_name": "小爱音箱",
        "app_name_en": "Mi AI Speaker",
        "developer": "小米",
        "category": "Tools",
    },

    "com.huawei.android.launcher": {
        "app_name": "华为桌面",
        "app_name_en": "Huawei Home",
        "developer": "华为",
        "category": "System",
    },

    "com.huawei.systemmanager": {
        "app_name": "手机管家",
        "app_name_en": "Phone Manager",
        "developer": "华为",
        "category": "System",
    },

    "com.huawei.appmarket": {
        "app_name": "华为应用市场",
        "app_name_en": "Huawei AppGallery",
        "developer": "华为",
        "category": "Tools",
    },

    "com.huawei.gamebox": {
        "app_name": "华为游戏中心",
        "app_name_en": "Huawei Game Center",
        "developer": "华为",
        "category": "Game",
    },

    "com.huawei.music": {
        "app_name": "华为音乐",
        "app_name_en": "Huawei Music",
        "developer": "华为",
        "category": "Music & Audio",
    },

    "com.huawei.video": {
        "app_name": "华为视频",
        "app_name_en": "Huawei Video",
        "developer": "华为",
        "category": "Entertainment",
    },

    "com.huawei.browser": {
        "app_name": "华为浏览器",
        "app_name_en": "Huawei Browser",
        "developer": "华为",
        "category": "Browser",
    },

    "com.huawei.wallet": {
        "app_name": "华为钱包",
        "app_name_en": "Huawei Wallet",
        "developer": "华为",
        "category": "Finance",
    },

    "com.huawei.health": {
        "app_name": "华为运动健康",
        "app_name_en": "Huawei Health",
        "developer": "华为",
        "category": "Health & Fitness",
    },

    "com.huawei.cloud": {
        "app_name": "华为云空间",
        "app_name_en": "Huawei Cloud",
        "developer": "华为",
        "category": "Productivity",
    },

    "com.huawei.himovie": {
        "app_name": "华为视频",
        "app_name_en": "Huawei Video",
        "developer": "华为",
        "category": "Entertainment",
    },

    "com.huawei.phoneservice": {
        "app_name": "服务",
        "app_name_en": "HiCare",
        "developer": "华为",
        "category": "System",
    },

    "com.huawei.hwdetectrepair": {
        "app_name": "智能检测",
        "app_name_en": "Smart Diagnosis",
        "developer": "华为",
        "category": "System",
    },

    "com.huawei.hwid": {
        "app_name": "华为账号",
        "app_name_en": "Huawei ID",
        "developer": "华为",
        "category": "System",
    },

    "com.huawei.intelligent": {
        "app_name": "智慧助手·今天",
        "app_name_en": "Huawei Assistant",
        "developer": "华为",
        "category": "Tools",
    },

    "com.huawei.vassistant": {
        "app_name": "智慧语音",
        "app_name_en": "Celia Voice",
        "developer": "华为",
        "category": "Tools",
    },

    "com.huawei.themes": {
        "app_name": "主题",
        "app_name_en": "Huawei Themes",
        "developer": "华为",
        "category": "System",
    },

    "com.huawei.scanner": {
        "app_name": "智慧视觉",
        "app_name_en": "AI Lens",
        "developer": "华为",
        "category": "Tools",
    },

    "com.huawei.lives": {
        "app_name": "畅连",
        "app_name_en": "MeeTime",
        "developer": "华为",
        "category": "Communication",
    },

    "com.huawei.notepad": {
        "app_name": "备忘录",
        "app_name_en": "Notepad",
        "developer": "华为",
        "category": "Productivity",
    },

    "com.huawei.calculator": {
        "app_name": "计算器",
        "app_name_en": "Calculator",
        "developer": "华为",
        "category": "System",
    },

    "com.huawei.compass": {
        "app_name": "指南针",
        "app_name_en": "Compass",
        "developer": "华为",
        "category": "System",
    },

    "com.huawei.recorder": {
        "app_name": "录音机",
        "app_name_en": "Recorder",
        "developer": "华为",
        "category": "System",
    },

    "com.huawei.himovie.overseas": {
        "app_name": "华为视频国际版",
        "app_name_en": "Huawei Video",
        "developer": "华为",
        "category": "Entertainment",
    },

    "com.huawei.hwsearch": {
        "app_name": "智慧搜索",
        "app_name_en": "Petal Search",
        "developer": "华为",
        "category": "Tools",
    },

    "com.huawei.maps.app": {
        "app_name": "花瓣地图",
        "app_name_en": "Petal Maps",
        "developer": "华为",
        "category": "Maps & Navigation",
    },

    "com.huawei.wear": {
        "app_name": "华为穿戴",
        "app_name_en": "Huawei Wear",
        "developer": "华为",
        "category": "Health & Fitness",
    },

    "com.oppo.launcher": {
        "app_name": "OPPO桌面",
        "app_name_en": "OPPO Launcher",
        "developer": "OPPO",
        "category": "System",
    },

    "com.oppo.market": {
        "app_name": "OPPO软件商店",
        "app_name_en": "OPPO App Market",
        "developer": "OPPO",
        "category": "Tools",
    },

    "com.oppo.gamecenter": {
        "app_name": "OPPO游戏中心",
        "app_name_en": "OPPO Game Center",
        "developer": "OPPO",
        "category": "Game",
    },

    "com.oppo.music": {
        "app_name": "OPPO音乐",
        "app_name_en": "OPPO Music",
        "developer": "OPPO",
        "category": "Music & Audio",
    },

    "com.oppo.video": {
        "app_name": "OPPO视频",
        "app_name_en": "OPPO Video",
        "developer": "OPPO",
        "category": "Entertainment",
    },

    "com.oppo.browser": {
        "app_name": "OPPO浏览器",
        "app_name_en": "OPPO Browser",
        "developer": "OPPO",
        "category": "Browser",
    },

    "com.oppo.wallet": {
        "app_name": "OPPO钱包",
        "app_name_en": "OPPO Wallet",
        "developer": "OPPO",
        "category": "Finance",
    },

    "com.oppo.health": {
        "app_name": "OPPO健康",
        "app_name_en": "OPPO Health",
        "developer": "OPPO",
        "category": "Health & Fitness",
    },

    "com.oppo.cloud": {
        "app_name": "OPPO云服务",
        "app_name_en": "OPPO Cloud",
        "developer": "OPPO",
        "category": "Productivity",
    },

    "com.oppo.community": {
        "app_name": "OPPO社区",
        "app_name_en": "OPPO Community",
        "developer": "OPPO",
        "category": "Social",
    },

    "com.oppo.gallery3d": {
        "app_name": "OPPO相册",
        "app_name_en": "OPPO Gallery",
        "developer": "OPPO",
        "category": "System",
    },

    "com.oppo.filemanager": {
        "app_name": "OPPO文件管理",
        "app_name_en": "OPPO File Manager",
        "developer": "OPPO",
        "category": "System",
    },

    "com.oppo.notes": {
        "app_name": "OPPO便签",
        "app_name_en": "OPPO Notes",
        "developer": "OPPO",
        "category": "Productivity",
    },

    "com.oppo.safe": {
        "app_name": "OPPO安全中心",
        "app_name_en": "OPPO Security Center",
        "developer": "OPPO",
        "category": "System",
    },

    "com.oppo.weather": {
        "app_name": "OPPO天气",
        "app_name_en": "OPPO Weather",
        "developer": "OPPO",
        "category": "Weather",
    },

    "com.oppo.assistant": {
        "app_name": "OPPO助手",
        "app_name_en": "OPPO Assistant",
        "developer": "OPPO",
        "category": "Tools",
    },

    "com.oppo.account": {
        "app_name": "OPPO账号",
        "app_name_en": "OPPO Account",
        "developer": "OPPO",
        "category": "System",
    },

    "com.oppo.findn": {
        "app_name": "OPPO折叠屏专区",
        "app_name_en": "OPPO Fold",
        "developer": "OPPO",
        "category": "System",
    },

    "com.coloros.compass": {
        "app_name": "指南针",
        "app_name_en": "Compass",
        "developer": "OPPO",
        "category": "System",
    },

    "com.coloros.calculator": {
        "app_name": "计算器",
        "app_name_en": "Calculator",
        "developer": "OPPO",
        "category": "System",
    },

    "com.coloros.recorder": {
        "app_name": "录音",
        "app_name_en": "Recorder",
        "developer": "OPPO",
        "category": "System",
    },

    "com.coloros.soundrecorder": {
        "app_name": "录音机",
        "app_name_en": "Sound Recorder",
        "developer": "OPPO",
        "category": "System",
    },

    "com.coloros.assistant": {
        "app_name": "小布助手",
        "app_name_en": "Breeno Assistant",
        "developer": "OPPO",
        "category": "Tools",
    },

    "com.coloros.smartsidebar": {
        "app_name": "智能侧边栏",
        "app_name_en": "Smart Sidebar",
        "developer": "OPPO",
        "category": "System",
    },

    "com.coloros.alarmclock": {
        "app_name": "时钟",
        "app_name_en": "Clock",
        "developer": "OPPO",
        "category": "System",
    },

    "com.vivo.launcher": {
        "app_name": "vivo桌面",
        "app_name_en": "vivo Launcher",
        "developer": "vivo",
        "category": "System",
    },

    "com.vivo.appstore": {
        "app_name": "vivo应用商店",
        "app_name_en": "vivo App Store",
        "developer": "vivo",
        "category": "Tools",
    },

    "com.vivo.game": {
        "app_name": "vivo游戏中心",
        "app_name_en": "vivo Game Center",
        "developer": "vivo",
        "category": "Game",
    },

    "com.vivo.music": {
        "app_name": "vivo音乐",
        "app_name_en": "vivo Music",
        "developer": "vivo",
        "category": "Music & Audio",
    },

    "com.vivo.video": {
        "app_name": "vivo视频",
        "app_name_en": "vivo Video",
        "developer": "vivo",
        "category": "Entertainment",
    },

    "com.vivo.browser": {
        "app_name": "vivo浏览器",
        "app_name_en": "vivo Browser",
        "developer": "vivo",
        "category": "Browser",
    },

    "com.vivo.wallet": {
        "app_name": "vivo钱包",
        "app_name_en": "vivo Wallet",
        "developer": "vivo",
        "category": "Finance",
    },

    "com.vivo.health": {
        "app_name": "vivo健康",
        "app_name_en": "vivo Health",
        "developer": "vivo",
        "category": "Health & Fitness",
    },

    "com.vivo.cloud": {
        "app_name": "vivo云服务",
        "app_name_en": "vivo Cloud",
        "developer": "vivo",
        "category": "Productivity",
    },

    "com.vivo.community": {
        "app_name": "vivo社区",
        "app_name_en": "vivo Community",
        "developer": "vivo",
        "category": "Social",
    },

    "com.vivo.gallery": {
        "app_name": "vivo相册",
        "app_name_en": "vivo Gallery",
        "developer": "vivo",
        "category": "System",
    },

    "com.vivo.filemanager": {
        "app_name": "vivo文件管理",
        "app_name_en": "vivo File Manager",
        "developer": "vivo",
        "category": "System",
    },

    "com.vivo.notes": {
        "app_name": "vivo便签",
        "app_name_en": "vivo Notes",
        "developer": "vivo",
        "category": "Productivity",
    },

    "com.vivo.security": {
        "app_name": "vivo管家",
        "app_name_en": "vivo Security",
        "developer": "vivo",
        "category": "System",
    },

    "com.vivo.weather": {
        "app_name": "vivo天气",
        "app_name_en": "vivo Weather",
        "developer": "vivo",
        "category": "Weather",
    },

    "com.vivo.assistant": {
        "app_name": "Jovi语音",
        "app_name_en": "Jovi Assistant",
        "developer": "vivo",
        "category": "Tools",
    },

    "com.vivo.account": {
        "app_name": "vivo账号",
        "app_name_en": "vivo Account",
        "developer": "vivo",
        "category": "System",
    },

    "com.vivo.easyshare": {
        "app_name": "互传",
        "app_name_en": "EasyShare",
        "developer": "vivo",
        "category": "Tools",
    },

    "com.vivo.compass": {
        "app_name": "指南针",
        "app_name_en": "Compass",
        "developer": "vivo",
        "category": "System",
    },

    "com.vivo.calculator": {
        "app_name": "计算器",
        "app_name_en": "Calculator",
        "developer": "vivo",
        "category": "System",
    },

    "com.vivo.recorder": {
        "app_name": "录音机",
        "app_name_en": "Recorder",
        "developer": "vivo",
        "category": "System",
    },

    "com.vivo.clock": {
        "app_name": "时钟",
        "app_name_en": "Clock",
        "developer": "vivo",
        "category": "System",
    },

    "com.vivo.smartscanner": {
        "app_name": "扫一扫",
        "app_name_en": "Smart Scanner",
        "developer": "vivo",
        "category": "Tools",
    },

    "com.vivo.motionsensor": {
        "app_name": "智慧运动",
        "app_name_en": "Smart Motion",
        "developer": "vivo",
        "category": "Health & Fitness",
    },

    "com.oneplus.launcher": {
        "app_name": "一加桌面",
        "app_name_en": "OnePlus Launcher",
        "developer": "一加",
        "category": "System",
    },

    "com.oneplus.gallery": {
        "app_name": "一加相册",
        "app_name_en": "OnePlus Gallery",
        "developer": "一加",
        "category": "System",
    },

    "com.oneplus.community": {
        "app_name": "一加社区",
        "app_name_en": "OnePlus Community",
        "developer": "一加",
        "category": "Social",
    },

    "com.oneplus.note": {
        "app_name": "一加便签",
        "app_name_en": "OnePlus Notes",
        "developer": "一加",
        "category": "Productivity",
    },

    "com.oneplus.security": {
        "app_name": "一加安全中心",
        "app_name_en": "OnePlus Security",
        "developer": "一加",
        "category": "System",
    },

    "com.samsung.android.app.spage": {
        "app_name": "三星生活助手",
        "app_name_en": "Samsung Life",
        "developer": "三星",
        "category": "Tools",
    },

    "com.samsung.android.samsungpay": {
        "app_name": "三星智付",
        "app_name_en": "Samsung Pay CN",
        "developer": "三星",
        "category": "Finance",
    },

    "com.samsung.android.app.watchmanager": {
        "app_name": "三星穿戴",
        "app_name_en": "Galaxy Wearable CN",
        "developer": "三星",
        "category": "Tools",
    },

    "com.jd.wireless": {
        "app_name": "京东",
        "app_name_en": "JD.com",
        "developer": "京东",
        "category": "Shopping",
    },

    "com.xgimi.zhushou": {
        "app_name": "极米",
        "app_name_en": "XGIMI",
        "developer": "极米科技",
        "category": "Tools",
    },

    "com.tplink.tether": {
        "app_name": "TP-Link",
        "app_name_en": "TP-Link Tether",
        "developer": "普联",
        "category": "Tools",
    },

    "com.tp_link.smartlife": {
        "app_name": "TP-Link智能生活",
        "app_name_en": "TP-Link Smart Life",
        "developer": "普联",
        "category": "Tools",
    },

    "com.byd.aeri.caranywhere": {
        "app_name": "比亚迪汽车",
        "app_name_en": "BYD Auto",
        "developer": "比亚迪",
        "category": "Auto & Vehicles",
    },

    "com.nio.app": {
        "app_name": "蔚来",
        "app_name_en": "NIO",
        "developer": "蔚来",
        "category": "Auto & Vehicles",
    },

    "com.xiaopeng.app": {
        "app_name": "小鹏汽车",
        "app_name_en": "XPeng",
        "developer": "小鹏汽车",
        "category": "Auto & Vehicles",
    },

    "com.lixiang.app": {
        "app_name": "理想汽车",
        "app_name_en": "Li Auto",
        "developer": "理想汽车",
        "category": "Auto & Vehicles",
    },

    "com.tesla.cn": {
        "app_name": "Tesla中国",
        "app_name_en": "Tesla China",
        "developer": "特斯拉",
        "category": "Auto & Vehicles",
    },

    "com.wedoapps.car": {
        "app_name": "瓜子二手车",
        "app_name_en": "Guazi Used Cars",
        "developer": "车好多",
        "category": "Auto & Vehicles",
    },

    "com.youxin.car": {
        "app_name": "优信二手车",
        "app_name_en": "UXin",
        "developer": "优信",
        "category": "Auto & Vehicles",
    },

    "com.didi.etaxi": {
        "app_name": "滴滴出行",
        "app_name_en": "DiDi",
        "developer": "滴滴",
        "category": "Auto & Vehicles",
    },

    "com.caocaokeji.app": {
        "app_name": "曹操出行",
        "app_name_en": "CaoCao Mobility",
        "developer": "吉利",
        "category": "Auto & Vehicles",
    },

    "com.shouqiev.app": {
        "app_name": "首汽约车",
        "app_name_en": "Shouqi Limo",
        "developer": "首汽集团",
        "category": "Auto & Vehicles",
    },

    "com.autohome.app": {
        "app_name": "汽车之家",
        "app_name_en": "Autohome",
        "developer": "汽车之家",
        "category": "Auto & Vehicles",
    },

    "com.pcauto.app": {
        "app_name": "太平洋汽车",
        "app_name_en": "PCauto",
        "developer": "太平洋汽车",
        "category": "Auto & Vehicles",
    },

    "com.yiche.app": {
        "app_name": "易车",
        "app_name_en": "Yiche",
        "developer": "易车",
        "category": "Auto & Vehicles",
    },

    "com.dongchedi.app": {
        "app_name": "懂车帝",
        "app_name_en": "Dongchedi",
        "developer": "字节跳动",
        "category": "Auto & Vehicles",
    },

    "cn.etool.car": {
        "app_name": "瓜子二手车",
        "app_name_en": "Guazi",
        "developer": "车好多",
        "category": "Auto & Vehicles",
    },

    "com.tuhu.app": {
        "app_name": "途虎养车",
        "app_name_en": "Tuhu",
        "developer": "途虎养车",
        "category": "Auto & Vehicles",
    },

    "com.parkingwang.app": {
        "app_name": "停车王",
        "app_name_en": "Parking King",
        "developer": "停车王",
        "category": "Auto & Vehicles",
    },

    "com.hellobike.bike": {
        "app_name": "哈啰",
        "app_name_en": "Hello Bike",
        "developer": "哈啰出行",
        "category": "Auto & Vehicles",
    },

    "com.baidu.tieba": {
        "app_name": "百度贴吧",
        "app_name_en": "Baidu Tieba",
        "developer": "百度",
        "category": "Social",
    },

    "com.baidu.haokan": {
        "app_name": "好看视频",
        "app_name_en": "Haokan Video",
        "developer": "百度",
        "category": "Entertainment",
    },

    "com.baidu.wenku": {
        "app_name": "百度文库",
        "app_name_en": "Baidu Wenku",
        "developer": "百度",
        "category": "Productivity",
    },

    "com.baidu.iknow": {
        "app_name": "百度知道",
        "app_name_en": "Baidu Knows",
        "developer": "百度",
        "category": "Social",
    },

    "com.baidu.baike": {
        "app_name": "百度百科",
        "app_name_en": "Baidu Baike",
        "developer": "百度",
        "category": "Books & Reference",
    },

    "com.baidu.translate": {
        "app_name": "百度翻译",
        "app_name_en": "Baidu Translate",
        "developer": "百度",
        "category": "Tools",
    },

    "com.sina.weibolite": {
        "app_name": "微博极速版",
        "app_name_en": "Weibo Lite",
        "developer": "新浪",
        "category": "Social",
    },

    "com.sina.weibog3": {
        "app_name": "微博国际版",
        "app_name_en": "Weibo International",
        "developer": "新浪",
        "category": "Social",
    },

    "com.tencent.portfolio": {
        "app_name": "自选股",
        "app_name_en": "Tencent Stock",
        "developer": "腾讯",
        "category": "Finance",
    },

    "com.tencent.stock": {
        "app_name": "腾讯自选股",
        "app_name_en": "Tencent Stock",
        "developer": "腾讯",
        "category": "Finance",
    },

    "com.tencent.ims": {
        "app_name": "腾讯企点",
        "app_name_en": "Tencent Qidian",
        "developer": "腾讯",
        "category": "Business",
    },

    "com.tencent.qqmail": {
        "app_name": "QQ邮箱",
        "app_name_en": "QQ Mail",
        "developer": "腾讯",
        "category": "Productivity",
    },

    "com.tencent.gamehelper.sgame": {
        "app_name": "王者营地",
        "app_name_en": "Honor of Kings Camp",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.tencent.gamehelper.pubgm": {
        "app_name": "和平精英助手",
        "app_name_en": "Game for Peace Helper",
        "developer": "腾讯",
        "category": "Game",
    },

    "com.xunlei.downloadprovider": {
        "app_name": "迅雷",
        "app_name_en": "Xunlei / Thunder",
        "developer": "迅雷",
        "category": "Tools",
    },

    "com.xunlei.kankan": {
        "app_name": "迅雷看看",
        "app_name_en": "Xunlei Kankan",
        "developer": "迅雷",
        "category": "Entertainment",
    },

    "com.xunlei.cloud": {
        "app_name": "迅雷云盘",
        "app_name_en": "Xunlei Cloud",
        "developer": "迅雷",
        "category": "Productivity",
    },

    "com.alibaba.work": {
        "app_name": "阿里卖家",
        "app_name_en": "Alibaba Seller",
        "developer": "阿里巴巴",
        "category": "Business",
    },

    "com.taobao.qianniu": {
        "app_name": "千牛",
        "app_name_en": "Qianniu",
        "developer": "阿里巴巴",
        "category": "Business",
    },

    "com.taobao.live": {
        "app_name": "点淘",
        "app_name_en": "Diantao / Taobao Live",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.taobao.mobile.dinghuo": {
        "app_name": "钉货",
        "app_name_en": "Dinghuo",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.alibaba.icbu.seller": {
        "app_name": "阿里国际站卖家",
        "app_name_en": "Alibaba.com Seller",
        "developer": "阿里巴巴",
        "category": "Business",
    },

    "com.sankuai.movie": {
        "app_name": "猫眼",
        "app_name_en": "Maoyan",
        "developer": "美团",
        "category": "Entertainment",
    },

    "com.taobao.movie.android": {
        "app_name": "淘票票",
        "app_name_en": "Taopiaopiao",
        "developer": "阿里巴巴",
        "category": "Entertainment",
    },

    "com.ctrip.english": {
        "app_name": "Trip.com",
        "app_name_en": "Trip.com",
        "developer": "携程",
        "category": "Travel & Local",
    },

    "com.netease.global": {
        "app_name": "网易buff",
        "app_name_en": "NetEase BUFF",
        "developer": "网易",
        "category": "Shopping",
    },

    "com.tongqu.app": {
        "app_name": "童趣",
        "app_name_en": "Tongqu",
        "developer": "童趣",
        "category": "Education",
    },

    "com.qyer.android.jinnang": {
        "app_name": "穷游",
        "app_name_en": "Qyer",
        "developer": "穷游网",
        "category": "Travel & Local",
    },

    "com.fanli.android": {
        "app_name": "返利",
        "app_name_en": "Fanli",
        "developer": "返利网",
        "category": "Shopping",
    },

    "com.daxuesheng.sdk": {
        "app_name": "啥都不剩",
        "app_name_en": "Shadou Busheng",
        "developer": "大学生",
        "category": "Lifestyle",
    },

    "com.taobao.etaocoupon": {
        "app_name": "一淘",
        "app_name_en": "Yitao",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },

    "com.smzdm.client.android": {
        "app_name": "什么值得买",
        "app_name_en": "SMZDM",
        "developer": "值得买科技",
        "category": "Shopping",
    },

    "com.bw30.zsch": {
        "app_name": "什么值得买",
        "app_name_en": "SMZDM",
        "developer": "值得买科技",
        "category": "Shopping",
    },

    "com.hexin.plat.android": {
        "app_name": "同花顺",
        "app_name_en": "THS",
        "developer": "同花顺",
        "category": "Finance",
    },

    "com.htsc.trade": {
        "app_name": "涨乐财富通",
        "app_name_en": "HTSC Wealth",
        "developer": "华泰证券",
        "category": "Finance",
    },

    "com.gf.client": {
        "app_name": "广发易淘金",
        "app_name_en": "GF Securities",
        "developer": "广发证券",
        "category": "Finance",
    },

    "com.cicc.wm": {
        "app_name": "中金财富",
        "app_name_en": "CICC Wealth",
        "developer": "中金公司",
        "category": "Finance",
    },

    "com.csc.mobile": {
        "app_name": "中信建投",
        "app_name_en": "CSC",
        "developer": "中信建投",
        "category": "Finance",
    },

    "com.gtja.mobile": {
        "app_name": "国泰君安",
        "app_name_en": "GTJA",
        "developer": "国泰君安",
        "category": "Finance",
    },

    "com.essence.mobile": {
        "app_name": "安信证券",
        "app_name_en": "Essence Securities",
        "developer": "安信证券",
        "category": "Finance",
    },

    "com.zxsc.mobile": {
        "app_name": "招商证券",
        "app_name_en": "CMS",
        "developer": "招商证券",
        "category": "Finance",
    },

    "com.cnstock.app": {
        "app_name": "上海证券报",
        "app_name_en": "Shanghai Securities News",
        "developer": "上证报",
        "category": "Finance",
    },

    "com.nbd.app": {
        "app_name": "每日经济新闻",
        "app_name_en": "NBD / National Business Daily",
        "developer": "每日经济新闻",
        "category": "News & Magazines",
    },

    "com.jrj.app": {
        "app_name": "金融界",
        "app_name_en": "JRJ",
        "developer": "金融界",
        "category": "Finance",
    },

    "com.cs.com.cn": {
        "app_name": "中证网",
        "app_name_en": "CS.com.cn",
        "developer": "中国证券报",
        "category": "Finance",
    },

    "com.tencent.weterm": {
        "app_name": "腾讯加速器",
        "app_name_en": "Tencent Accelerator",
        "developer": "腾讯",
        "category": "Tools",
    },

    "com.tencent.qqsecure": {
        "app_name": "腾讯手机管家",
        "app_name_en": "Tencent Security",
        "developer": "腾讯",
        "category": "Tools",
    },

    "com.tencent.token": {
        "app_name": "腾讯身份验证器",
        "app_name_en": "Tencent Authenticator",
        "developer": "腾讯",
        "category": "Tools",
    },

    "com.tencent.wifimanager": {
        "app_name": "腾讯WiFi管家",
        "app_name_en": "Tencent WiFi",
        "developer": "腾讯",
        "category": "Tools",
    },

    # =========================================================================
    # --- VPN & Proxy (Digital Forensics Hotspot) ---
    # =========================================================================
    "com.expressvpn.vpn": {
        "app_name": "ExpressVPN",
        "app_name_en": "ExpressVPN",
        "developer": "Express VPN International Ltd",
        "category": "VPN & Proxy",
    },
    "com.nordvpn.android": {
        "app_name": "NordVPN",
        "app_name_en": "NordVPN",
        "developer": "Nord Security",
        "category": "VPN & Proxy",
    },
    "com.surfshark.vpnclient.android": {
        "app_name": "Surfshark",
        "app_name_en": "Surfshark VPN",
        "developer": "Surfshark",
        "category": "VPN & Proxy",
    },
    "ch.protonvpn.android": {
        "app_name": "ProtonVPN",
        "app_name_en": "ProtonVPN",
        "developer": "Proton AG",
        "category": "VPN & Proxy",
    },
    "com.windscribe.vpn": {
        "app_name": "Windscribe",
        "app_name_en": "Windscribe VPN",
        "developer": "Windscribe",
        "category": "VPN & Proxy",
    },
    "com.anchorfree.hotspotshield": {
        "app_name": "Hotspot Shield",
        "app_name_en": "Hotspot Shield VPN",
        "developer": "AnchorFree / Pango",
        "category": "VPN & Proxy",
    },
    "com.tunnelbear.android": {
        "app_name": "TunnelBear",
        "app_name_en": "TunnelBear VPN",
        "developer": "TunnelBear / McAfee",
        "category": "VPN & Proxy",
    },
    "com.privatevpn.android": {
        "app_name": "PrivateVPN",
        "app_name_en": "PrivateVPN",
        "developer": "PrivateVPN",
        "category": "VPN & Proxy",
    },
    "com.ipvanish.vpn": {
        "app_name": "IPVanish",
        "app_name_en": "IPVanish VPN",
        "developer": "Ziff Davis",
        "category": "VPN & Proxy",
    },
    "com.cyberghost.vpn": {
        "app_name": "CyberGhost",
        "app_name_en": "CyberGhost VPN",
        "developer": "CyberGhost",
        "category": "VPN & Proxy",
    },
    "com.purevpn.vpn": {
        "app_name": "PureVPN",
        "app_name_en": "PureVPN",
        "developer": "PureVPN",
        "category": "VPN & Proxy",
    },
    "com.goldenfrog.vyprvpn": {
        "app_name": "VyprVPN",
        "app_name_en": "VyprVPN",
        "developer": "Golden Frog",
        "category": "VPN & Proxy",
    },
    "com.hideme.android": {
        "app_name": "Hide.me",
        "app_name_en": "Hide.me VPN",
        "developer": "Hide.me VPN",
        "category": "VPN & Proxy",
    },
    "net.mullvad.mullvadvpn": {
        "app_name": "Mullvad",
        "app_name_en": "Mullvad VPN",
        "developer": "Mullvad VPN AB",
        "category": "VPN & Proxy",
    },
    "net.ivpn.client": {
        "app_name": "IVPN",
        "app_name_en": "IVPN",
        "developer": "IVPN Limited",
        "category": "VPN & Proxy",
    },
    "com.privateinternetaccess.android": {
        "app_name": "PIA",
        "app_name_en": "Private Internet Access",
        "developer": "Kape Technologies",
        "category": "VPN & Proxy",
    },
    "com.strongvpn": {
        "app_name": "StrongVPN",
        "app_name_en": "StrongVPN",
        "developer": "StrongVPN",
        "category": "VPN & Proxy",
    },
    "org.getlantern.lantern": {
        "app_name": "Lantern",
        "app_name_en": "Lantern",
        "developer": "Brave New Software",
        "category": "VPN & Proxy",
    },
    "com.psiphon3": {
        "app_name": "Psiphon",
        "app_name_en": "Psiphon",
        "developer": "Psiphon Inc.",
        "category": "VPN & Proxy",
    },
    "com.psiphon3.subscription": {
        "app_name": "Psiphon Pro",
        "app_name_en": "Psiphon Pro",
        "developer": "Psiphon Inc.",
        "category": "VPN & Proxy",
    },
    "com.v2ray.ang": {
        "app_name": "v2rayNG",
        "app_name_en": "v2rayNG",
        "developer": "v2rayNG Project",
        "category": "VPN & Proxy",
    },
    "com.github.shadowsocks": {
        "app_name": "Shadowsocks",
        "app_name_en": "Shadowsocks",
        "developer": "Shadowsocks Community",
        "category": "VPN & Proxy",
    },
    "com.github.shadowsocks.plugin": {
        "app_name": "Shadowsocks Plugin",
        "app_name_en": "Shadowsocks Plugin",
        "developer": "Shadowsocks Community",
        "category": "VPN & Proxy",
    },
    "com.github.kr328.clash": {
        "app_name": "Clash for Android",
        "app_name_en": "Clash for Android",
        "developer": "Kr328 / Clash Community",
        "category": "VPN & Proxy",
    },
    "com.github.kr328.clash.foss": {
        "app_name": "Clash for Android FOSS",
        "app_name_en": "Clash FOSS",
        "developer": "Kr328 / Clash Community",
        "category": "VPN & Proxy",
    },
    "com.github.metacubex.clash.meta": {
        "app_name": "Clash Meta for Android",
        "app_name_en": "Clash Meta Android",
        "developer": "MetaCubeX",
        "category": "VPN & Proxy",
    },
    "io.nekohasekai.sfa": {
        "app_name": "sing-box",
        "app_name_en": "sing-box",
        "developer": "SagerNet Project",
        "category": "VPN & Proxy",
    },
    "app.hiddify.com": {
        "app_name": "Hiddify",
        "app_name_en": "Hiddify",
        "developer": "Hiddify",
        "category": "VPN & Proxy",
    },
    "com.wireguard.android": {
        "app_name": "WireGuard",
        "app_name_en": "WireGuard",
        "developer": "WireGuard Project",
        "category": "VPN & Proxy",
    },
    "de.blinkt.openvpn": {
        "app_name": "OpenVPN for Android",
        "app_name_en": "OpenVPN for Android",
        "developer": "Arne Schwabe",
        "category": "VPN & Proxy",
    },
    "net.openvpn.openvpn": {
        "app_name": "OpenVPN Connect",
        "app_name_en": "OpenVPN Connect",
        "developer": "OpenVPN Inc.",
        "category": "VPN & Proxy",
    },
    "org.outline.android.client": {
        "app_name": "Outline",
        "app_name_en": "Outline",
        "developer": "Jigsaw / Google",
        "category": "VPN & Proxy",
    },
    "moe.matsuri.lite": {
        "app_name": "Matsuri",
        "app_name_en": "Matsuri",
        "developer": "Matsuri Project",
        "category": "VPN & Proxy",
    },
    "io.nekohasekai.nekoray": {
        "app_name": "Nekoray",
        "app_name_en": "Nekoray",
        "developer": "Nekoray Project",
        "category": "VPN & Proxy",
    },
    "com.netch": {
        "app_name": "Netch",
        "app_name_en": "Netch",
        "developer": "Netch Project",
        "category": "VPN & Proxy",
    },
    "com.github.txthinking.brook": {
        "app_name": "Brook",
        "app_name_en": "Brook",
        "developer": "Brook Community",
        "category": "VPN & Proxy",
    },
    "com.tachyon.sstap": {
        "app_name": "SSTap",
        "app_name_en": "SSTap",
        "developer": "SSTap Project",
        "category": "VPN & Proxy",
    },
    "io.github.xray.client": {
        "app_name": "Xray",
        "app_name_en": "Xray Client",
        "developer": "Xray Project",
        "category": "VPN & Proxy",
    },
    "com.hysteria.network": {
        "app_name": "Hysteria",
        "app_name_en": "Hysteria",
        "developer": "Hysteria Community",
        "category": "VPN & Proxy",
    },
    "com.trojan.client": {
        "app_name": "Trojan",
        "app_name_en": "Trojan Client",
        "developer": "Trojan-GFW Project",
        "category": "VPN & Proxy",
    },
    "net.i2p.android.router": {
        "app_name": "I2P",
        "app_name_en": "I2P Router",
        "developer": "I2P Project",
        "category": "VPN & Proxy",
    },
    "org.torproject.android": {
        "app_name": "Orbot",
        "app_name_en": "Orbot",
        "developer": "The Tor Project",
        "category": "VPN & Proxy",
    },
    "org.torproject.torbrowser": {
        "app_name": "Tor Browser",
        "app_name_en": "Tor Browser",
        "developer": "The Tor Project",
        "category": "VPN & Proxy",
    },
    "org.torproject.torbrowser_alpha": {
        "app_name": "Tor Browser Alpha",
        "app_name_en": "Tor Browser Alpha",
        "developer": "The Tor Project",
        "category": "VPN & Proxy",
    },
    "info.guardianproject.orfox": {
        "app_name": "Orfox",
        "app_name_en": "Orfox",
        "developer": "Guardian Project",
        "category": "VPN & Proxy",
    },
    "com.brave.browser": {
        "app_name": "Brave",
        "app_name_en": "Brave Browser",
        "developer": "Brave Software",
        "category": "VPN & Proxy",
    },
    "com.opera.browser": {
        "app_name": "Opera",
        "app_name_en": "Opera Browser",
        "developer": "Opera Software",
        "category": "VPN & Proxy",
    },
    "com.opera.mini.native": {
        "app_name": "Opera Mini",
        "app_name_en": "Opera Mini",
        "developer": "Opera Software",
        "category": "VPN & Proxy",
    },
    "com.opera.app.freevpn": {
        "app_name": "Opera VPN",
        "app_name_en": "Opera VPN",
        "developer": "Opera Software",
        "category": "VPN & Proxy",
    },
    "com.riseup.net": {
        "app_name": "Riseup VPN",
        "app_name_en": "Riseup VPN",
        "developer": "Riseup Networks",
        "category": "VPN & Proxy",
    },
    "com.bitmask.app": {
        "app_name": "Bitmask",
        "app_name_en": "Riseup Bitmask",
        "developer": "LEAP Encryption Access Project",
        "category": "VPN & Proxy",
    },
    "calyx.vpn": {
        "app_name": "Calyx VPN",
        "app_name_en": "Calyx VPN",
        "developer": "The Calyx Institute",
        "category": "VPN & Proxy",
    },
    "com.guardianproject.orbot": {
        "app_name": "Orbot Mini",
        "app_name_en": "Orbot Mini",
        "developer": "Guardian Project",
        "category": "VPN & Proxy",
    },
    "com.freevpn.vpn": {
        "app_name": "FreeVPN",
        "app_name_en": "FreeVPN",
        "developer": "FreeVPN.org",
        "category": "VPN & Proxy",
    },
    "com.supervpn.vpn": {
        "app_name": "SuperVPN",
        "app_name_en": "SuperVPN",
        "developer": "SuperSoftTech",
        "category": "VPN & Proxy",
    },
    "com.betternet": {
        "app_name": "Betternet",
        "app_name_en": "Betternet VPN",
        "developer": "Betternet LLC",
        "category": "VPN & Proxy",
    },
    "com.turbovpn.vpn": {
        "app_name": "Turbo VPN",
        "app_name_en": "Turbo VPN",
        "developer": "Turbo VPN",
        "category": "VPN & Proxy",
    },
    "com.thundervpn.vpn": {
        "app_name": "Thunder VPN",
        "app_name_en": "Thunder VPN",
        "developer": "Signal Lab",
        "category": "VPN & Proxy",
    },
    "com.avast.vpn": {
        "app_name": "Avast SecureLine VPN",
        "app_name_en": "Avast SecureLine VPN",
        "developer": "Avast",
        "category": "VPN & Proxy",
    },
    "com.avira.vpn": {
        "app_name": "Avira Phantom VPN",
        "app_name_en": "Avira Phantom VPN",
        "developer": "Avira / Norton",
        "category": "VPN & Proxy",
    },
    "com.vpn.unlimited": {
        "app_name": "VPN Unlimited",
        "app_name_en": "VPN Unlimited",
        "developer": "KeepSolid Inc.",
        "category": "VPN & Proxy",
    },
    "com.urbanvpn.android": {
        "app_name": "Urban VPN",
        "app_name_en": "Urban VPN",
        "developer": "Urban VPN",
        "category": "VPN & Proxy",
    },
    "com.vpnglobal.vpn": {
        "app_name": "VPN 360",
        "app_name_en": "VPN 360",
        "developer": "VPN 360",
        "category": "VPN & Proxy",
    },
    "com.vpnpro.vpn": {
        "app_name": "Snap VPN",
        "app_name_en": "Snap VPN",
        "developer": "Snap VPN",
        "category": "VPN & Proxy",
    },

    # =========================================================================
    # --- Cryptocurrency Wallets & Exchanges ---
    # =========================================================================
    "com.wallet.crypto.trustapp": {
        "app_name": "Trust Wallet",
        "app_name_en": "Trust Wallet",
        "developer": "Trust Wallet / Binance",
        "category": "Crypto",
    },
    "io.metamask": {
        "app_name": "MetaMask",
        "app_name_en": "MetaMask",
        "developer": "ConsenSys",
        "category": "Crypto",
    },
    "com.binance.dev": {
        "app_name": "Binance",
        "app_name_en": "Binance",
        "developer": "Binance",
        "category": "Crypto",
    },
    "com.binance.us": {
        "app_name": "Binance.US",
        "app_name_en": "Binance.US",
        "developer": "Binance",
        "category": "Crypto",
    },
    "com.coinbase.android": {
        "app_name": "Coinbase",
        "app_name_en": "Coinbase",
        "developer": "Coinbase Inc.",
        "category": "Crypto",
    },
    "com.coinbase.wallet": {
        "app_name": "Coinbase Wallet",
        "app_name_en": "Coinbase Wallet",
        "developer": "Coinbase Inc.",
        "category": "Crypto",
    },
    "com.coinbase.pro": {
        "app_name": "Coinbase Pro",
        "app_name_en": "Coinbase Pro",
        "developer": "Coinbase Inc.",
        "category": "Crypto",
    },
    "com.okinc.okex.gp": {
        "app_name": "OKX",
        "app_name_en": "OKX",
        "developer": "OKX",
        "category": "Crypto",
    },
    "com.bybit.app": {
        "app_name": "Bybit",
        "app_name_en": "Bybit",
        "developer": "Bybit",
        "category": "Crypto",
    },
    "com.kubi.kucoin": {
        "app_name": "KuCoin",
        "app_name_en": "KuCoin",
        "developer": "KuCoin",
        "category": "Crypto",
    },
    "com.bitget.exchange": {
        "app_name": "Bitget",
        "app_name_en": "Bitget",
        "developer": "Bitget",
        "category": "Crypto",
    },
    "com.gateio.gateio": {
        "app_name": "Gate.io",
        "app_name_en": "Gate.io",
        "developer": "Gate.io",
        "category": "Crypto",
    },
    "com.htc.otc": {
        "app_name": "HTX / 火币",
        "app_name_en": "HTX (Huobi)",
        "developer": "HTX / Huobi Global",
        "category": "Crypto",
    },
    "com.bitfinex.bfxapp": {
        "app_name": "Bitfinex",
        "app_name_en": "Bitfinex",
        "developer": "Bitfinex",
        "category": "Crypto",
    },
    "com.kraken.app": {
        "app_name": "Kraken",
        "app_name_en": "Kraken",
        "developer": "Kraken",
        "category": "Crypto",
    },
    "com.gemini.android.app": {
        "app_name": "Gemini",
        "app_name_en": "Gemini Exchange",
        "developer": "Gemini Trust Company",
        "category": "Crypto",
    },
    "co.mona.android": {
        "app_name": "Crypto.com",
        "app_name_en": "Crypto.com",
        "developer": "Crypto.com",
        "category": "Crypto",
    },
    "com.crypto.exchange": {
        "app_name": "Crypto.com Exchange",
        "app_name_en": "Crypto.com Exchange",
        "developer": "Crypto.com",
        "category": "Crypto",
    },
    "com.defi.wallet": {
        "app_name": "Crypto.com DeFi Wallet",
        "app_name_en": "Crypto.com DeFi Wallet",
        "developer": "Crypto.com",
        "category": "Crypto",
    },
    "piuk.blockchain.android": {
        "app_name": "Blockchain.com",
        "app_name_en": "Blockchain.com Wallet",
        "developer": "Blockchain.com",
        "category": "Crypto",
    },
    "exodusmovement.exodus": {
        "app_name": "Exodus",
        "app_name_en": "Exodus Wallet",
        "developer": "Exodus",
        "category": "Crypto",
    },
    "org.electrum.electrum": {
        "app_name": "Electrum",
        "app_name_en": "Electrum Bitcoin Wallet",
        "developer": "Electrum Project",
        "category": "Crypto",
    },
    "com.mycelium.wallet": {
        "app_name": "Mycelium",
        "app_name_en": "Mycelium Wallet",
        "developer": "Mycelium",
        "category": "Crypto",
    },
    "com.samourai.wallet": {
        "app_name": "Samourai Wallet",
        "app_name_en": "Samourai Wallet",
        "developer": "Samourai Wallet",
        "category": "Crypto",
    },
    "io.bluewallet.bluewallet": {
        "app_name": "BlueWallet",
        "app_name_en": "BlueWallet",
        "developer": "BlueWallet",
        "category": "Crypto",
    },
    "com.muun.wallet": {
        "app_name": "Muun",
        "app_name_en": "Muun Wallet",
        "developer": "Muun",
        "category": "Crypto",
    },
    "fr.acinq.phoenix": {
        "app_name": "Phoenix Wallet",
        "app_name_en": "Phoenix Lightning Wallet",
        "developer": "ACINQ",
        "category": "Crypto",
    },
    "com.breez.client": {
        "app_name": "Breez",
        "app_name_en": "Breez Lightning Wallet",
        "developer": "Breez",
        "category": "Crypto",
    },
    "com.zeusln.zeus": {
        "app_name": "Zeus LN",
        "app_name_en": "Zeus Lightning Wallet",
        "developer": "Zeus LN",
        "category": "Crypto",
    },
    "im.token.app": {
        "app_name": "imToken",
        "app_name_en": "imToken Wallet",
        "developer": "imToken",
        "category": "Crypto",
    },
    "com.tokenpocket.app": {
        "app_name": "TokenPocket",
        "app_name_en": "TokenPocket Wallet",
        "developer": "TokenPocket",
        "category": "Crypto",
    },
    "so.onekey.app.wallet": {
        "app_name": "OneKey",
        "app_name_en": "OneKey Wallet",
        "developer": "OneKey",
        "category": "Crypto",
    },
    "com.ledger.live": {
        "app_name": "Ledger Live",
        "app_name_en": "Ledger Live",
        "developer": "Ledger",
        "category": "Crypto",
    },
    "io.trezor.suite": {
        "app_name": "Trezor Suite",
        "app_name_en": "Trezor Suite",
        "developer": "Trezor",
        "category": "Crypto",
    },
    "com.bitpie": {
        "app_name": "比特派",
        "app_name_en": "Bitpie Wallet",
        "developer": "Bitpie",
        "category": "Crypto",
    },
    "com.safepal.wallet": {
        "app_name": "Safepal",
        "app_name_en": "Safepal Wallet",
        "developer": "Safepal",
        "category": "Crypto",
    },
    "com.coinomi.wallet": {
        "app_name": "Coinomi",
        "app_name_en": "Coinomi Wallet",
        "developer": "Coinomi",
        "category": "Crypto",
    },
    "co.edgesecure.app": {
        "app_name": "Edge",
        "app_name_en": "Edge Wallet",
        "developer": "Edge / Airbitz",
        "category": "Crypto",
    },
    "com.breadwallet": {
        "app_name": "BRD",
        "app_name_en": "BRD / Bread Wallet",
        "developer": "Breadwinner AG",
        "category": "Crypto",
    },
    "io.atomicwallet": {
        "app_name": "Atomic Wallet",
        "app_name_en": "Atomic Wallet",
        "developer": "Atomic Wallet",
        "category": "Crypto",
    },
    "com.guarda.wallet": {
        "app_name": "Guarda",
        "app_name_en": "Guarda Wallet",
        "developer": "Guarda",
        "category": "Crypto",
    },
    "com.zelcash.wallet": {
        "app_name": "Zelcore",
        "app_name_en": "Zelcore Wallet",
        "developer": "Zelcore",
        "category": "Crypto",
    },
    "app.phantom": {
        "app_name": "Phantom",
        "app_name_en": "Phantom Wallet",
        "developer": "Phantom Technologies",
        "category": "Crypto",
    },
    "com.solflare.mobile": {
        "app_name": "Solflare",
        "app_name_en": "Solflare Wallet",
        "developer": "Solflare",
        "category": "Crypto",
    },
    "com.backpack.app": {
        "app_name": "Backpack",
        "app_name_en": "Backpack Wallet",
        "developer": "Backpack",
        "category": "Crypto",
    },
    "com.chainapsis.keplr": {
        "app_name": "Keplr",
        "app_name_en": "Keplr Wallet",
        "developer": "Chainapsis",
        "category": "Crypto",
    },
    "com.cosmostation.wallet": {
        "app_name": "Cosmostation",
        "app_name_en": "Cosmostation Wallet",
        "developer": "Cosmostation",
        "category": "Crypto",
    },
    "com.terra.station": {
        "app_name": "Terra Station",
        "app_name_en": "Terra Station",
        "developer": "Terraform Labs",
        "category": "Crypto",
    },
    "io.yoroi": {
        "app_name": "Yoroi",
        "app_name_en": "Yoroi Wallet",
        "developer": "EMURGO",
        "category": "Crypto",
    },
    "io.flint.wallet": {
        "app_name": "Flint",
        "app_name_en": "Flint Wallet",
        "developer": "DCSpark",
        "category": "Crypto",
    },
    "com.uniswap.mobile": {
        "app_name": "Uniswap",
        "app_name_en": "Uniswap",
        "developer": "Uniswap Labs",
        "category": "Crypto",
    },
    "com.oneinch.android": {
        "app_name": "1inch",
        "app_name_en": "1inch Wallet",
        "developer": "1inch Network",
        "category": "Crypto",
    },
    "com.pancakeswap.android": {
        "app_name": "PancakeSwap",
        "app_name_en": "PancakeSwap",
        "developer": "PancakeSwap",
        "category": "Crypto",
    },
    "com.aave.android": {
        "app_name": "Aave",
        "app_name_en": "Aave",
        "developer": "Aave Labs",
        "category": "Crypto",
    },
    "com.wasabiwallet": {
        "app_name": "Wasabi Wallet",
        "app_name_en": "Wasabi Wallet",
        "developer": "zkSNACKs",
        "category": "Crypto",
    },
    "com.tether.wallet": {
        "app_name": "Tether Wallet",
        "app_name_en": "Tether Wallet",
        "developer": "Tether Operations",
        "category": "Crypto",
    },
    "com.enjin.wallet": {
        "app_name": "Enjin Wallet",
        "app_name_en": "Enjin Wallet",
        "developer": "Enjin",
        "category": "Crypto",
    },
    "com.wavesplatform.wallet": {
        "app_name": "Waves Wallet",
        "app_name_en": "Waves.Exchange",
        "developer": "Waves Platform",
        "category": "Crypto",
    },
    "com.mixin.one": {
        "app_name": "Mixin Messenger",
        "app_name_en": "Mixin Wallet",
        "developer": "Mixin",
        "category": "Crypto",
    },
    "com.xverse.wallet": {
        "app_name": "Xverse",
        "app_name_en": "Xverse Wallet",
        "developer": "Xverse",
        "category": "Crypto",
    },
    "app.unisat.wallet": {
        "app_name": "UniSat",
        "app_name_en": "UniSat Wallet",
        "developer": "UniSat",
        "category": "Crypto",
    },
    "com.hyperpay.wallet": {
        "app_name": "HyperPay",
        "app_name_en": "HyperPay Wallet",
        "developer": "HyperPay",
        "category": "Crypto",
    },

    # =========================================================================
    # --- Encrypted / Private Messengers ---
    # =========================================================================
    "org.thoughtcrime.securesms": {
        "app_name": "Signal",
        "app_name_en": "Signal",
        "developer": "Signal Foundation",
        "category": "Encrypted Messenger",
    },
    "org.telegram.messenger": {
        "app_name": "Telegram",
        "app_name_en": "Telegram",
        "developer": "Telegram FZ-LLC",
        "category": "Encrypted Messenger",
    },
    "org.thunderdog.challegram": {
        "app_name": "Telegram X",
        "app_name_en": "Telegram X",
        "developer": "Telegram FZ-LLC",
        "category": "Encrypted Messenger",
    },
    "com.whatsapp": {
        "app_name": "WhatsApp",
        "app_name_en": "WhatsApp",
        "developer": "Meta Platforms Inc.",
        "category": "Encrypted Messenger",
    },
    "com.whatsapp.w4b": {
        "app_name": "WhatsApp Business",
        "app_name_en": "WhatsApp Business",
        "developer": "Meta Platforms Inc.",
        "category": "Encrypted Messenger",
    },
    "com.wickr.pro": {
        "app_name": "Wickr Me",
        "app_name_en": "Wickr Me",
        "developer": "Wickr / AWS",
        "category": "Encrypted Messenger",
    },
    "com.wickr.pro.enterprise": {
        "app_name": "Wickr Pro",
        "app_name_en": "Wickr Pro",
        "developer": "Wickr / AWS",
        "category": "Encrypted Messenger",
    },
    "com.wire": {
        "app_name": "Wire",
        "app_name_en": "Wire",
        "developer": "Wire Swiss GmbH",
        "category": "Encrypted Messenger",
    },
    "ch.threema.app": {
        "app_name": "Threema",
        "app_name_en": "Threema",
        "developer": "Threema GmbH",
        "category": "Encrypted Messenger",
    },
    "network.loki.messenger": {
        "app_name": "Session",
        "app_name_en": "Session",
        "developer": "Oxen Project",
        "category": "Encrypted Messenger",
    },
    "im.vector.app": {
        "app_name": "Element",
        "app_name_en": "Element (Matrix)",
        "developer": "Element / New Vector",
        "category": "Encrypted Messenger",
    },
    "org.briarproject.briar.android": {
        "app_name": "Briar",
        "app_name_en": "Briar",
        "developer": "Briar Project",
        "category": "Encrypted Messenger",
    },
    "net.jami": {
        "app_name": "Jami",
        "app_name_en": "Jami",
        "developer": "Savoir-faire Linux",
        "category": "Encrypted Messenger",
    },
    "chat.simplex.app": {
        "app_name": "SimpleX Chat",
        "app_name_en": "SimpleX Chat",
        "developer": "SimpleX Chat",
        "category": "Encrypted Messenger",
    },
    "im.status.ethereum": {
        "app_name": "Status",
        "app_name_en": "Status",
        "developer": "Status.im",
        "category": "Encrypted Messenger",
    },
    "com.radicalapps.dust": {
        "app_name": "Dust",
        "app_name_en": "Dust (formerly Cyber Dust)",
        "developer": "Radical App LLC",
        "category": "Encrypted Messenger",
    },
    "com.coverme.messenger": {
        "app_name": "CoverMe",
        "app_name_en": "CoverMe",
        "developer": "CoverMe",
        "category": "Encrypted Messenger",
    },
    "com.brosix.android": {
        "app_name": "Brosix",
        "app_name_en": "Brosix",
        "developer": "Brosix",
        "category": "Encrypted Messenger",
    },
    "com.viber.voip": {
        "app_name": "Viber",
        "app_name_en": "Viber",
        "developer": "Rakuten Viber",
        "category": "Encrypted Messenger",
    },
    "jp.naver.line.android": {
        "app_name": "LINE",
        "app_name_en": "LINE",
        "developer": "LINE Corporation",
        "category": "Encrypted Messenger",
    },
    "com.kakao.talk": {
        "app_name": "KakaoTalk",
        "app_name_en": "KakaoTalk",
        "developer": "Kakao Corp.",
        "category": "Encrypted Messenger",
    },
    "com.zing.zalo": {
        "app_name": "Zalo",
        "app_name_en": "Zalo",
        "developer": "VNG Corporation",
        "category": "Encrypted Messenger",
    },
    "com.keybase.android": {
        "app_name": "Keybase",
        "app_name_en": "Keybase",
        "developer": "Keybase / Zoom",
        "category": "Encrypted Messenger",
    },
    "im.tox.antox": {
        "app_name": "Antox (Tox)",
        "app_name_en": "Antox / Tox",
        "developer": "Tox Project",
        "category": "Encrypted Messenger",
    },
    "com.cwtch.im": {
        "app_name": "Cwtch",
        "app_name_en": "Cwtch",
        "developer": "Open Privacy",
        "category": "Encrypted Messenger",
    },
    "im.quicksy.client": {
        "app_name": "Quicksy",
        "app_name_en": "Quicksy",
        "developer": "Daniel Gultsch",
        "category": "Encrypted Messenger",
    },
    "eu.siacs.conversations": {
        "app_name": "Conversations",
        "app_name_en": "Conversations (XMPP)",
        "developer": "Daniel Gultsch",
        "category": "Encrypted Messenger",
    },
    "chat.fluffy.fluffychat": {
        "app_name": "FluffyChat",
        "app_name_en": "FluffyChat",
        "developer": "FluffyChat Community",
        "category": "Encrypted Messenger",
    },
    "org.smssecure.smssecure": {
        "app_name": "SMSSecure",
        "app_name_en": "SMSSecure",
        "developer": "SMSSecure Community",
        "category": "Encrypted Messenger",
    },
    "info.guardianproject.otr.app.im": {
        "app_name": "ChatSecure",
        "app_name_en": "ChatSecure",
        "developer": "Guardian Project",
        "category": "Encrypted Messenger",
    },
    "com.olvid.android": {
        "app_name": "Olvid",
        "app_name_en": "Olvid",
        "developer": "Olvid",
        "category": "Encrypted Messenger",
    },
    "org.snikket.android": {
        "app_name": "Snikket",
        "app_name_en": "Snikket",
        "developer": "Snikket",
        "category": "Encrypted Messenger",
    },
    "im.zig.android": {
        "app_name": "Zom",
        "app_name_en": "Zom",
        "developer": "Zom",
        "category": "Encrypted Messenger",
    },
    "com.skype.raider": {
        "app_name": "Skype",
        "app_name_en": "Skype",
        "developer": "Microsoft",
        "category": "Encrypted Messenger",
    },
    "com.discord": {
        "app_name": "Discord",
        "app_name_en": "Discord",
        "developer": "Discord Inc.",
        "category": "Encrypted Messenger",
    },
    "com.snapchat.android": {
        "app_name": "Snapchat",
        "app_name_en": "Snapchat",
        "developer": "Snap Inc.",
        "category": "Encrypted Messenger",
    },
    "com.instagram.android": {
        "app_name": "Instagram",
        "app_name_en": "Instagram",
        "developer": "Meta Platforms Inc.",
        "category": "Encrypted Messenger",
    },
    "com.facebook.orca": {
        "app_name": "Facebook Messenger",
        "app_name_en": "Messenger",
        "developer": "Meta Platforms Inc.",
        "category": "Encrypted Messenger",
    },

    # =========================================================================
    # --- AI Tools ---
    # =========================================================================
    "com.openai.chatgpt": {
        "app_name": "ChatGPT",
        "app_name_en": "ChatGPT",
        "developer": "OpenAI",
        "category": "AI Tool",
    },
    "com.openai.openai": {
        "app_name": "OpenAI",
        "app_name_en": "OpenAI",
        "developer": "OpenAI",
        "category": "AI Tool",
    },
    "com.google.android.apps.bard": {
        "app_name": "Google Gemini",
        "app_name_en": "Gemini",
        "developer": "Google",
        "category": "AI Tool",
    },
    "com.microsoft.copilot": {
        "app_name": "Microsoft Copilot",
        "app_name_en": "Microsoft Copilot",
        "developer": "Microsoft",
        "category": "AI Tool",
    },
    "ai.perplexity.app.android": {
        "app_name": "Perplexity",
        "app_name_en": "Perplexity AI",
        "developer": "Perplexity AI",
        "category": "AI Tool",
    },
    "com.poe.android": {
        "app_name": "Poe",
        "app_name_en": "Poe",
        "developer": "Quora / Poe",
        "category": "AI Tool",
    },
    "ai.character.app": {
        "app_name": "Character.AI",
        "app_name_en": "Character.AI",
        "developer": "Character Technologies",
        "category": "AI Tool",
    },
    "ai.replika.app": {
        "app_name": "Replika",
        "app_name_en": "Replika",
        "developer": "Luka Inc.",
        "category": "AI Tool",
    },
    "com.jasper.ai": {
        "app_name": "Jasper",
        "app_name_en": "Jasper AI",
        "developer": "Jasper",
        "category": "AI Tool",
    },
    "com.writesonic.app": {
        "app_name": "Writesonic",
        "app_name_en": "Writesonic",
        "developer": "Writesonic",
        "category": "AI Tool",
    },
    "com.copy.ai": {
        "app_name": "Copy.AI",
        "app_name_en": "Copy.AI",
        "developer": "Copy.AI",
        "category": "AI Tool",
    },
    "com.notion.ai": {
        "app_name": "Notion",
        "app_name_en": "Notion",
        "developer": "Notion Labs",
        "category": "AI Tool",
    },
    "com.dreamstudio.app": {
        "app_name": "DreamStudio",
        "app_name_en": "DreamStudio (Stable Diffusion)",
        "developer": "Stability AI",
        "category": "AI Tool",
    },
    "com.leonardo.ai": {
        "app_name": "Leonardo.AI",
        "app_name_en": "Leonardo.AI",
        "developer": "Leonardo.AI",
        "category": "AI Tool",
    },
    "com.runway.ml": {
        "app_name": "Runway",
        "app_name_en": "Runway ML",
        "developer": "Runway",
        "category": "AI Tool",
    },
    "com.pika.art": {
        "app_name": "Pika",
        "app_name_en": "Pika Art",
        "developer": "Pika Labs",
        "category": "AI Tool",
    },
    "com.synthesia.io": {
        "app_name": "Synthesia",
        "app_name_en": "Synthesia",
        "developer": "Synthesia",
        "category": "AI Tool",
    },
    "com.heygen.app": {
        "app_name": "HeyGen",
        "app_name_en": "HeyGen",
        "developer": "HeyGen",
        "category": "AI Tool",
    },
    "com.elevenlabs.app": {
        "app_name": "ElevenLabs",
        "app_name_en": "ElevenLabs",
        "developer": "ElevenLabs",
        "category": "AI Tool",
    },
    "com.suno.ai": {
        "app_name": "Suno",
        "app_name_en": "Suno AI",
        "developer": "Suno",
        "category": "AI Tool",
    },
    "com.udio.app": {
        "app_name": "Udio",
        "app_name_en": "Udio",
        "developer": "Udio",
        "category": "AI Tool",
    },
    "com.moonshot.kimi": {
        "app_name": "Kimi",
        "app_name_en": "Kimi / Moonshot",
        "developer": "月之暗面",
        "category": "AI Tool",
    },
    "com.larus.nova": {
        "app_name": "豆包",
        "app_name_en": "Doubao",
        "developer": "字节跳动",
        "category": "AI Tool",
    },
    "com.baidu.yanyuan": {
        "app_name": "文心一言",
        "app_name_en": "ERNIE Bot / Wenxin Yiyan",
        "developer": "百度",
        "category": "AI Tool",
    },
    "com.alibaba.tongyi": {
        "app_name": "通义千问",
        "app_name_en": "Tongyi Qianwen",
        "developer": "阿里巴巴",
        "category": "AI Tool",
    },
    "com.iflytek.spark": {
        "app_name": "讯飞星火",
        "app_name_en": "iFlytek Spark",
        "developer": "科大讯飞",
        "category": "AI Tool",
    },
    "com.zhipu.chatglm": {
        "app_name": "智谱清言",
        "app_name_en": "ChatGLM / Zhipu Qingyan",
        "developer": "智谱AI",
        "category": "AI Tool",
    },
    "com.tiangong.ai": {
        "app_name": "天工",
        "app_name_en": "Tiangong AI",
        "developer": "昆仑万维",
        "category": "AI Tool",
    },
    "com.qihoo.zhinao": {
        "app_name": "360智脑",
        "app_name_en": "360 AI Brain",
        "developer": "360",
        "category": "AI Tool",
    },
    "com.deepseek.chat": {
        "app_name": "DeepSeek",
        "app_name_en": "DeepSeek",
        "developer": "深度求索",
        "category": "AI Tool",
    },
    "com.baichuan.ai": {
        "app_name": "百川智能",
        "app_name_en": "Baichuan AI",
        "developer": "百川智能",
        "category": "AI Tool",
    },
    "com.minimax.chat": {
        "app_name": "海螺AI",
        "app_name_en": "Hailuo AI / MiniMax",
        "developer": "MiniMax",
        "category": "AI Tool",
    },
    "com.metaso.ai": {
        "app_name": "秘塔AI",
        "app_name_en": "MetaSo AI",
        "developer": "秘塔科技",
        "category": "AI Tool",
    },
    "com.immersivetranslate.android": {
        "app_name": "沉浸式翻译",
        "app_name_en": "Immersive Translate",
        "developer": "沉浸式翻译",
        "category": "AI Tool",
    },
    "com.anthropic.claude": {
        "app_name": "Claude",
        "app_name_en": "Claude",
        "developer": "Anthropic",
        "category": "AI Tool",
    },
    "com.xinghuo.app": {
        "app_name": "星火大模型",
        "app_name_en": "Spark LLM",
        "developer": "科大讯飞",
        "category": "AI Tool",
    },
    "com.hunyuan.app": {
        "app_name": "腾讯混元",
        "app_name_en": "Tencent Hunyuan",
        "developer": "腾讯",
        "category": "AI Tool",
    },
    "com.lingyiwandu.app": {
        "app_name": "万知",
        "app_name_en": "Wanzhi (01.AI)",
        "developer": "零一万物",
        "category": "AI Tool",
    },

    # =========================================================================
    # --- Privacy / Security Tools ---
    # =========================================================================
    "ch.protonmail.android": {
        "app_name": "Proton Mail",
        "app_name_en": "Proton Mail",
        "developer": "Proton AG",
        "category": "Privacy & Security",
    },
    "com.protonvpn.android": {
        "app_name": "Proton VPN",
        "app_name_en": "Proton VPN",
        "developer": "Proton AG",
        "category": "Privacy & Security",
    },
    "com.proton.drive": {
        "app_name": "Proton Drive",
        "app_name_en": "Proton Drive",
        "developer": "Proton AG",
        "category": "Privacy & Security",
    },
    "me.proton.android.calendar": {
        "app_name": "Proton Calendar",
        "app_name_en": "Proton Calendar",
        "developer": "Proton AG",
        "category": "Privacy & Security",
    },
    "de.tutao.tutanota": {
        "app_name": "Tuta Mail",
        "app_name_en": "Tuta (Tutanota)",
        "developer": "Tutao GmbH",
        "category": "Privacy & Security",
    },
    "com.startmail.app": {
        "app_name": "StartMail",
        "app_name_en": "StartMail",
        "developer": "StartMail",
        "category": "Privacy & Security",
    },
    "com.mailboxorg.app": {
        "app_name": "Mailbox.org",
        "app_name_en": "Mailbox.org",
        "developer": "Mailbox.org",
        "category": "Privacy & Security",
    },
    "com.x8bit.bitwarden": {
        "app_name": "Bitwarden",
        "app_name_en": "Bitwarden",
        "developer": "Bitwarden Inc.",
        "category": "Privacy & Security",
    },
    "com.onepassword.android": {
        "app_name": "1Password",
        "app_name_en": "1Password",
        "developer": "1Password",
        "category": "Privacy & Security",
    },
    "com.lastpass.lpandroid": {
        "app_name": "LastPass",
        "app_name_en": "LastPass",
        "developer": "LastPass",
        "category": "Privacy & Security",
    },
    "com.lastpass.authenticator": {
        "app_name": "LastPass Authenticator",
        "app_name_en": "LastPass Authenticator",
        "developer": "LastPass",
        "category": "Privacy & Security",
    },
    "com.dashlane": {
        "app_name": "Dashlane",
        "app_name_en": "Dashlane",
        "developer": "Dashlane",
        "category": "Privacy & Security",
    },
    "keepass2android.keepass2android": {
        "app_name": "KeePass2Android",
        "app_name_en": "KeePass2Android",
        "developer": "Philipp Crocoll",
        "category": "Privacy & Security",
    },
    "com.kunzisoft.keepass.libre": {
        "app_name": "KeePassDX",
        "app_name_en": "KeePassDX",
        "developer": "Kunzisoft",
        "category": "Privacy & Security",
    },
    "com.authy.authy": {
        "app_name": "Authy",
        "app_name_en": "Authy 2FA",
        "developer": "Twilio",
        "category": "Privacy & Security",
    },
    "com.google.android.apps.authenticator2": {
        "app_name": "Google Authenticator",
        "app_name_en": "Google Authenticator",
        "developer": "Google",
        "category": "Privacy & Security",
    },
    "com.azure.authenticator": {
        "app_name": "Microsoft Authenticator",
        "app_name_en": "Microsoft Authenticator",
        "developer": "Microsoft",
        "category": "Privacy & Security",
    },
    "com.duosecurity.duomobile": {
        "app_name": "Duo Mobile",
        "app_name_en": "Duo Mobile",
        "developer": "Cisco / Duo Security",
        "category": "Privacy & Security",
    },
    "com.beemdevelopment.aegis": {
        "app_name": "Aegis",
        "app_name_en": "Aegis Authenticator",
        "developer": "Beem Development",
        "category": "Privacy & Security",
    },
    "org.fedorahosted.freeotp": {
        "app_name": "FreeOTP",
        "app_name_en": "FreeOTP",
        "developer": "Red Hat",
        "category": "Privacy & Security",
    },
    "com.andotp.app": {
        "app_name": "andOTP",
        "app_name_en": "andOTP",
        "developer": "andOTP",
        "category": "Privacy & Security",
    },
    "org.cryptomator": {
        "app_name": "Cryptomator",
        "app_name_en": "Cryptomator",
        "developer": "Cryptomator / Skymatic",
        "category": "Privacy & Security",
    },
    "com.nordlocker.android": {
        "app_name": "NordLocker",
        "app_name_en": "NordLocker",
        "developer": "Nord Security",
        "category": "Privacy & Security",
    },
    "com.axcrypt.android": {
        "app_name": "AxCrypt",
        "app_name_en": "AxCrypt",
        "developer": "AxCrypt AB",
        "category": "Privacy & Security",
    },
    "com.symantec.norton": {
        "app_name": "Norton 360",
        "app_name_en": "Norton 360",
        "developer": "NortonLifeLock",
        "category": "Privacy & Security",
    },
    "com.wsandroid.suite.mcafee": {
        "app_name": "McAfee Security",
        "app_name_en": "McAfee Mobile Security",
        "developer": "McAfee",
        "category": "Privacy & Security",
    },
    "com.bitdefender.antivirus": {
        "app_name": "Bitdefender",
        "app_name_en": "Bitdefender Mobile Security",
        "developer": "Bitdefender",
        "category": "Privacy & Security",
    },
    "com.kms.free": {
        "app_name": "Kaspersky",
        "app_name_en": "Kaspersky Mobile Security",
        "developer": "Kaspersky",
        "category": "Privacy & Security",
    },
    "com.avast.android.mobilesecurity": {
        "app_name": "Avast Mobile Security",
        "app_name_en": "Avast Mobile Security",
        "developer": "Avast",
        "category": "Privacy & Security",
    },
    "com.antivirus.tablet": {
        "app_name": "AVG AntiVirus",
        "app_name_en": "AVG AntiVirus",
        "developer": "AVG",
        "category": "Privacy & Security",
    },
    "org.malwarebytes.antimalware": {
        "app_name": "Malwarebytes",
        "app_name_en": "Malwarebytes",
        "developer": "Malwarebytes",
        "category": "Privacy & Security",
    },
    "com.sophos.xg.mobile": {
        "app_name": "Sophos Intercept X",
        "app_name_en": "Sophos Intercept X",
        "developer": "Sophos",
        "category": "Privacy & Security",
    },
    "com.lookout": {
        "app_name": "Lookout",
        "app_name_en": "Lookout Security",
        "developer": "Lookout Inc.",
        "category": "Privacy & Security",
    },
    "com.lsdroid.cerberus": {
        "app_name": "Cerberus",
        "app_name_en": "Cerberus Anti-Theft",
        "developer": "LSDroid",
        "category": "Privacy & Security",
    },
    "com.prey": {
        "app_name": "Prey",
        "app_name_en": "Prey Anti-Theft",
        "developer": "Prey Inc.",
        "category": "Privacy & Security",
    },
    "com.google.android.apps.adm": {
        "app_name": "Find My Device",
        "app_name_en": "Find My Device",
        "developer": "Google",
        "category": "Privacy & Security",
    },
    "com.alienmanfc6.wheresmyandroid": {
        "app_name": "Where's My Droid",
        "app_name_en": "Where's My Droid",
        "developer": "Alienman Technologies",
        "category": "Privacy & Security",
    },
    "com.keepsafe": {
        "app_name": "Keepsafe",
        "app_name_en": "Keepsafe Photo Vault",
        "developer": "Keepsafe",
        "category": "Privacy & Security",
    },
    "com.thinkyeah.apphider": {
        "app_name": "App Hider",
        "app_name_en": "App Hider",
        "developer": "App Hider Team",
        "category": "Privacy & Security",
    },
    "com.calculator.vault": {
        "app_name": "Calculator Vault",
        "app_name_en": "Calculator Vault",
        "developer": "Hide Apps",
        "category": "Privacy & Security",
    },
    "com.hideitpro": {
        "app_name": "Hide It Pro",
        "app_name_en": "Hide It Pro",
        "developer": "Anuj Tenani",
        "category": "Privacy & Security",
    },
    "com.newsoftwares.folderlock_v1": {
        "app_name": "Folder Lock",
        "app_name_en": "Folder Lock",
        "developer": "NewSoftwares",
        "category": "Privacy & Security",
    },
    "com.ccs.encapp": {
        "app_name": "Encrypt App",
        "app_name_en": "File Encryptor",
        "developer": "CCS",
        "category": "Privacy & Security",
    },
    "com.photovault.lockmyphoto": {
        "app_name": "LockMyPix",
        "app_name_en": "LockMyPix Photo Vault",
        "developer": "fourchars",
        "category": "Privacy & Security",
    },
    "com.gallery.vault": {
        "app_name": "Gallery Vault",
        "app_name_en": "Gallery Vault",
        "developer": "Gallery Vault",
        "category": "Privacy & Security",
    },
    "com.freevpn.applock": {
        "app_name": "AppLock",
        "app_name_en": "AppLock",
        "developer": "DoMobile Lab",
        "category": "Privacy & Security",
    },
    "com.sp.protector.free": {
        "app_name": "Smart AppLock",
        "app_name_en": "Smart AppLock",
        "developer": "Smart AppLock",
        "category": "Privacy & Security",
    },
    "com.nqmobile.safetynet": {
        "app_name": "NQ Mobile Security",
        "app_name_en": "NQ Mobile Security",
        "developer": "NQ Mobile",
        "category": "Privacy & Security",
    },
    "com.cheetah.accleaner": {
        "app_name": "CCleaner",
        "app_name_en": "CCleaner",
        "developer": "Piriform / Avast",
        "category": "Privacy & Security",
    },
    "com.sdmaid.basic": {
        "app_name": "SD Maid",
        "app_name_en": "SD Maid",
        "developer": "darken",
        "category": "Privacy & Security",
    },

    # =========================================================================
    # --- Root / Device Modification Tools ---
    # =========================================================================
    "com.topjohnwu.magisk": {
        "app_name": "Magisk",
        "app_name_en": "Magisk",
        "developer": "topjohnwu",
        "category": "Root & Mod",
    },
    "eu.chainfire.supersu": {
        "app_name": "SuperSU",
        "app_name_en": "SuperSU",
        "developer": "Chainfire",
        "category": "Root & Mod",
    },
    "eu.chainfire.supersu.pro": {
        "app_name": "SuperSU Pro",
        "app_name_en": "SuperSU Pro",
        "developer": "Chainfire",
        "category": "Root & Mod",
    },
    "com.kingroot.kinguser": {
        "app_name": "KingRoot",
        "app_name_en": "KingRoot",
        "developer": "KingRoot Studio",
        "category": "Root & Mod",
    },
    "com.kingo.root": {
        "app_name": "KingoRoot",
        "app_name_en": "KingoRoot",
        "developer": "Kingosoft",
        "category": "Root & Mod",
    },
    "com.geohot.towelroot": {
        "app_name": "Towelroot",
        "app_name_en": "Towelroot",
        "developer": "Geohot",
        "category": "Root & Mod",
    },
    "com.regawmod.framaroot": {
        "app_name": "Framaroot",
        "app_name_en": "Framaroot",
        "developer": "RegawMOD",
        "category": "Root & Mod",
    },
    "me.twrp.twrpapp": {
        "app_name": "TWRP",
        "app_name_en": "TWRP Official App",
        "developer": "Team Win",
        "category": "Root & Mod",
    },
    "com.cgollner.flashify": {
        "app_name": "Flashify",
        "app_name_en": "Flashify",
        "developer": "Christian Gollner",
        "category": "Root & Mod",
    },
    "com.koushikdutta.rommanager": {
        "app_name": "ROM Manager",
        "app_name_en": "ROM Manager",
        "developer": "ClockworkMod",
        "category": "Root & Mod",
    },
    "eu.chainfire.flash": {
        "app_name": "FlashFire",
        "app_name_en": "FlashFire",
        "developer": "Chainfire",
        "category": "Root & Mod",
    },
    "de.robv.android.xposed.installer": {
        "app_name": "Xposed Installer",
        "app_name_en": "Xposed Installer",
        "developer": "rovo89",
        "category": "Root & Mod",
    },
    "org.lsposed.manager": {
        "app_name": "LSPosed Manager",
        "app_name_en": "LSPosed Manager",
        "developer": "LSPosed Team",
        "category": "Root & Mod",
    },
    "org.meowcat.edxposed.manager": {
        "app_name": "EdXposed Manager",
        "app_name_en": "EdXposed Manager",
        "developer": "Elder Drivers",
        "category": "Root & Mod",
    },
    "me.weishu.exp": {
        "app_name": "TaiChi / 太极",
        "app_name_en": "TaiChi",
        "developer": "Weishu / 维术",
        "category": "Root & Mod",
    },
    "io.va.exposed": {
        "app_name": "VirtualXposed",
        "app_name_en": "VirtualXposed",
        "developer": "Weishu / 维术",
        "category": "Root & Mod",
    },
    "com.vmos.pro": {
        "app_name": "VMOS Pro",
        "app_name_en": "VMOS Pro",
        "developer": "VMOS",
        "category": "Root & Mod",
    },
    "com.vmos.app": {
        "app_name": "VMOS",
        "app_name_en": "VMOS",
        "developer": "VMOS",
        "category": "Root & Mod",
    },
    "com.lbe.parallel.intl": {
        "app_name": "Parallel Space",
        "app_name_en": "Parallel Space",
        "developer": "LBE Tech",
        "category": "Root & Mod",
    },
    "com.ludashi.dualspace": {
        "app_name": "Dual Space",
        "app_name_en": "Dual Space",
        "developer": "Ludashi",
        "category": "Root & Mod",
    },
    "com.oasisfeng.island": {
        "app_name": "Island",
        "app_name_en": "Island",
        "developer": "Oasis Feng",
        "category": "Root & Mod",
    },
    "net.typeblog.shelter": {
        "app_name": "Shelter",
        "app_name_en": "Shelter",
        "developer": "PeterCxy",
        "category": "Root & Mod",
    },
    "com.oasisfeng.island.shelter": {
        "app_name": "Insular",
        "app_name_en": "Insular",
        "developer": "Oasis Feng",
        "category": "Root & Mod",
    },
    "com.applisto.appcloner": {
        "app_name": "App Cloner",
        "app_name_en": "App Cloner",
        "developer": "AppListo",
        "category": "Root & Mod",
    },
    "com.dimonvideo.luckypatcher": {
        "app_name": "Lucky Patcher",
        "app_name_en": "Lucky Patcher",
        "developer": "ChelpuS",
        "category": "Root & Mod",
    },
    "org.sbtools.gamehack": {
        "app_name": "GameGuardian",
        "app_name_en": "GameGuardian",
        "developer": "SB Tools",
        "category": "Root & Mod",
    },
    "com.sbgamehacker": {
        "app_name": "SB Game Hacker",
        "app_name_en": "SB Game Hacker",
        "developer": "SB Tools",
        "category": "Root & Mod",
    },
    "eu.faircode.xlua": {
        "app_name": "XPrivacyLua",
        "app_name_en": "XPrivacyLua",
        "developer": "M66B / FairCode",
        "category": "Root & Mod",
    },
    "com.devadvance.rootcloak": {
        "app_name": "RootCloak",
        "app_name_en": "RootCloak",
        "developer": "devadvance",
        "category": "Root & Mod",
    },
    "com.kdrag0n.usnf": {
        "app_name": "Universal SafetyNet Fix",
        "app_name_en": "Universal SafetyNet Fix",
        "developer": "kdrag0n",
        "category": "Root & Mod",
    },
    "com.shamiko.app": {
        "app_name": "Shamiko",
        "app_name_en": "Shamiko",
        "developer": "LSPosed Team",
        "category": "Root & Mod",
    },
    "com.windy.magiskhide": {
        "app_name": "MagiskHide Props Config",
        "app_name_en": "MagiskHide Props Config",
        "developer": "Didgeridoohan",
        "category": "Root & Mod",
    },
    "com.finalwire.aid64": {
        "app_name": "AIDA64",
        "app_name_en": "AIDA64",
        "developer": "FinalWire",
        "category": "Root & Mod",
    },
    "com.cpuid.cpu_z": {
        "app_name": "CPU-Z",
        "app_name_en": "CPU-Z",
        "developer": "CPUID",
        "category": "Root & Mod",
    },
    "com.termux": {
        "app_name": "Termux",
        "app_name_en": "Termux",
        "developer": "Termux Project",
        "category": "Root & Mod",
    },
    "com.termux.api": {
        "app_name": "Termux:API",
        "app_name_en": "Termux:API",
        "developer": "Termux Project",
        "category": "Root & Mod",
    },
    "com.android.vending.billing.InAppBillingService.LUCK": {
        "app_name": "Lucky Patcher (Legacy)",
        "app_name_en": "Lucky Patcher Legacy",
        "developer": "ChelpuS",
        "category": "Root & Mod",
    },
    "com.byyoung.setting": {
        "app_name": "爱玩机工具箱",
        "app_name_en": "AIWANJI Toolbox",
        "developer": "byyoung",
        "category": "Root & Mod",
    },
    "com.fox2code.mmm": {
        "app_name": "Fox's Magisk Module Manager",
        "app_name_en": "Magisk Module Manager",
        "developer": "Fox2Code",
        "category": "Root & Mod",
    },
    "com.solohsu.android.edxp.manager": {
        "app_name": "EdXposed Manager",
        "app_name_en": "EdXposed",
        "developer": "Elder Drivers",
        "category": "Root & Mod",
    },
    "com.keramidas.TitaniumBackup": {
        "app_name": "Titanium Backup",
        "app_name_en": "Titanium Backup",
        "developer": "Titanium Track",
        "category": "Root & Mod",
    },

    # =========================================================================
    # --- Dating / Social Discovery ---
    # =========================================================================
    "com.tinder": {
        "app_name": "Tinder",
        "app_name_en": "Tinder",
        "developer": "Match Group",
        "category": "Dating",
    },
    "com.bumble.app": {
        "app_name": "Bumble",
        "app_name_en": "Bumble",
        "developer": "Bumble Inc.",
        "category": "Dating",
    },
    "com.hinge.app": {
        "app_name": "Hinge",
        "app_name_en": "Hinge",
        "developer": "Match Group",
        "category": "Dating",
    },
    "com.okcupid.okcupid": {
        "app_name": "OkCupid",
        "app_name_en": "OkCupid",
        "developer": "Match Group",
        "category": "Dating",
    },
    "com.grindrapp.android": {
        "app_name": "Grindr",
        "app_name_en": "Grindr",
        "developer": "Grindr LLC",
        "category": "Dating",
    },
    "com.her.app": {
        "app_name": "HER",
        "app_name_en": "HER",
        "developer": "HER",
        "category": "Dating",
    },
    "com.scruff.app": {
        "app_name": "Scruff",
        "app_name_en": "Scruff",
        "developer": "Perry Street Software",
        "category": "Dating",
    },
    "com.jackd.android": {
        "app_name": "Jack'd",
        "app_name_en": "Jack'd",
        "developer": "Perry Street Software",
        "category": "Dating",
    },
    "com.hornet.android": {
        "app_name": "Hornet",
        "app_name_en": "Hornet",
        "developer": "Hornet Networks",
        "category": "Dating",
    },
    "com.blued.android": {
        "app_name": "Blued",
        "app_name_en": "Blued",
        "developer": "Blue City",
        "category": "Dating",
    },
    "com.taimi.android": {
        "app_name": "Taimi",
        "app_name_en": "Taimi",
        "developer": "Taimi",
        "category": "Dating",
    },
    "com.feeld.android": {
        "app_name": "Feeld",
        "app_name_en": "Feeld",
        "developer": "Feeld Ltd",
        "category": "Dating",
    },
    "com.pure.dating": {
        "app_name": "Pure",
        "app_name_en": "Pure",
        "developer": "Pure",
        "category": "Dating",
    },
    "com.happn.android": {
        "app_name": "Happn",
        "app_name_en": "Happn",
        "developer": "Happn",
        "category": "Dating",
    },
    "com.coffeemeetsbagel": {
        "app_name": "Coffee Meets Bagel",
        "app_name_en": "Coffee Meets Bagel",
        "developer": "Coffee Meets Bagel",
        "category": "Dating",
    },
    "com.pof.android": {
        "app_name": "Plenty of Fish",
        "app_name_en": "Plenty of Fish",
        "developer": "Match Group",
        "category": "Dating",
    },
    "com.match.android.matchmobile": {
        "app_name": "Match",
        "app_name_en": "Match.com",
        "developer": "Match Group",
        "category": "Dating",
    },
    "com.zoosk.zoosk": {
        "app_name": "Zoosk",
        "app_name_en": "Zoosk",
        "developer": "Zoosk",
        "category": "Dating",
    },
    "com.eharmony": {
        "app_name": "eHarmony",
        "app_name_en": "eHarmony",
        "developer": "eHarmony Inc.",
        "category": "Dating",
    },
    "com.blk.dating": {
        "app_name": "BLK",
        "app_name_en": "BLK Dating",
        "developer": "Match Group",
        "category": "Dating",
    },
    "com.chispa.android": {
        "app_name": "Chispa",
        "app_name_en": "Chispa Dating",
        "developer": "Match Group",
        "category": "Dating",
    },
    "com.shaadi.android": {
        "app_name": "Shaadi.com",
        "app_name_en": "Shaadi",
        "developer": "Shaadi.com",
        "category": "Dating",
    },
    "com.muzmatch.android": {
        "app_name": "Muzz",
        "app_name_en": "Muzz (Muzmatch)",
        "developer": "Muzz",
        "category": "Dating",
    },
    "com.badoo.mobile": {
        "app_name": "Badoo",
        "app_name_en": "Badoo",
        "developer": "Bumble Inc.",
        "category": "Dating",
    },
    "com.yeeha.live": {
        "app_name": "Yeeha",
        "app_name_en": "Yeeha Live",
        "developer": "Yeeha",
        "category": "Dating",
    },
    "com.livu.app": {
        "app_name": "LivU",
        "app_name_en": "LivU",
        "developer": "LivU",
        "category": "Dating",
    },
    "com.azarlive.android": {
        "app_name": "Azar",
        "app_name_en": "Azar",
        "developer": "Hyperconnect",
        "category": "Dating",
    },
    "com.mico.chat": {
        "app_name": "MICO",
        "app_name_en": "MICO",
        "developer": "MICO World",
        "category": "Dating",
    },
    "com.holla.app": {
        "app_name": "HOLLA",
        "app_name_en": "HOLLA",
        "developer": "HOLLA",
        "category": "Dating",
    },
    "com.ome.tv": {
        "app_name": "OmeTV",
        "app_name_en": "OmeTV",
        "developer": "Maksym Lytvynenko",
        "category": "Dating",
    },
    "com.yubo.app": {
        "app_name": "Yubo",
        "app_name_en": "Yubo",
        "developer": "Yubo",
        "category": "Dating",
    },
    "com.hoop.snap": {
        "app_name": "Hoop",
        "app_name_en": "Hoop",
        "developer": "Hoop",
        "category": "Dating",
    },
    "com.wink.chat": {
        "app_name": "Wink",
        "app_name_en": "Wink",
        "developer": "Wink",
        "category": "Dating",
    },
    "com.wooplus.android": {
        "app_name": "WooPlus",
        "app_name_en": "WooPlus",
        "developer": "WooPlus",
        "category": "Dating",
    },
    "com.seeking.android": {
        "app_name": "Seeking",
        "app_name_en": "Seeking Arrangement",
        "developer": "Seeking",
        "category": "Dating",
    },
    "com.ashleymadison.android": {
        "app_name": "Ashley Madison",
        "app_name_en": "Ashley Madison",
        "developer": "Ruby Corp",
        "category": "Dating",
    },
    "com.gleeden.android": {
        "app_name": "Gleeden",
        "app_name_en": "Gleeden",
        "developer": "Gleeden",
        "category": "Dating",
    },
    "com.frim.app": {
        "app_name": "FRIM",
        "app_name_en": "FRIM",
        "developer": "FRIM",
        "category": "Dating",
    },
    "com.tango": {
        "app_name": "Tango",
        "app_name_en": "Tango Live",
        "developer": "Tango",
        "category": "Dating",
    },
    "com.liveme.android": {
        "app_name": "LiveMe",
        "app_name_en": "LiveMe",
        "developer": "LiveMe",
        "category": "Dating",
    },
    "com.uplive.app": {
        "app_name": "Uplive",
        "app_name_en": "Uplive",
        "developer": "Asia Innovations",
        "category": "Dating",
    },
    "com.bigo.live": {
        "app_name": "BIGO LIVE",
        "app_name_en": "BIGO LIVE",
        "developer": "BIGO Technology",
        "category": "Dating",
    },
    "com.chamet.live": {
        "app_name": "Chamet",
        "app_name_en": "Chamet",
        "developer": "Chamet",
        "category": "Dating",
    },
    "com.tagged.app": {
        "app_name": "Tagged",
        "app_name_en": "Tagged",
        "developer": "Match Group",
        "category": "Dating",
    },
    "com.meetme.app": {
        "app_name": "MeetMe",
        "app_name_en": "MeetMe",
        "developer": "MeetMe Group",
        "category": "Dating",
    },
    "com.skout.android": {
        "app_name": "Skout",
        "app_name_en": "Skout",
        "developer": "MeetMe Group",
        "category": "Dating",
    },
    "com.jaumo.app": {
        "app_name": "Jaumo",
        "app_name_en": "Jaumo Dating",
        "developer": "Jaumo",
        "category": "Dating",
    },
    "com.lovoo.android": {
        "app_name": "Lovoo",
        "app_name_en": "Lovoo",
        "developer": "Lovoo / Meet Group",
        "category": "Dating",
    },

    # =========================================================================
    # --- Network Analysis / Forensics Tools ---
    # =========================================================================
    "com.overlook.android.fing": {
        "app_name": "Fing",
        "app_name_en": "Fing Network Scanner",
        "developer": "Fing / Domotz",
        "category": "Network Tool",
    },
    "com.farproc.wifi.analyzer": {
        "app_name": "WiFi Analyzer",
        "app_name_en": "WiFi Analyzer",
        "developer": "farproc",
        "category": "Network Tool",
    },
    "io.wifimap.wifimap": {
        "app_name": "WiFi Map",
        "app_name_en": "WiFi Map",
        "developer": "WiFi Map LLC",
        "category": "Network Tool",
    },
    "com.instabridge.android": {
        "app_name": "Instabridge",
        "app_name_en": "Instabridge",
        "developer": "Instabridge",
        "category": "Network Tool",
    },
    "com.guoshi.httpcanary": {
        "app_name": "HttpCanary",
        "app_name_en": "HttpCanary",
        "developer": "HttpCanary",
        "category": "Network Tool",
    },
    "com.guoshi.httpcanary.plugin": {
        "app_name": "HttpCanary Plugin",
        "app_name_en": "HttpCanary Plugin",
        "developer": "HttpCanary",
        "category": "Network Tool",
    },
    "app.greyshirts.sslcapture": {
        "app_name": "Packet Capture",
        "app_name_en": "Packet Capture",
        "developer": "Grey Shirts",
        "category": "Network Tool",
    },
    "net.techet.netanalyzerlite.an": {
        "app_name": "Network Analyzer",
        "app_name_en": "Network Analyzer",
        "developer": "Jiri Techet",
        "category": "Network Tool",
    },
    "com.ddm.iptools": {
        "app_name": "IP Tools",
        "app_name_en": "IP Tools",
        "developer": "D.D.M.",
        "category": "Network Tool",
    },
    "com.nutsaboutnets.androidtools": {
        "app_name": "Network Tools",
        "app_name_en": "NetX Network Tools",
        "developer": "Nuts About Nets",
        "category": "Network Tool",
    },
    "com.paget96.netspeedindicator": {
        "app_name": "NetSpeed Indicator",
        "app_name_en": "NetSpeed Indicator",
        "developer": "Paget96",
        "category": "Network Tool",
    },
    "com.evozi.network": {
        "app_name": "Network Info II",
        "app_name_en": "Network Info II",
        "developer": "Evozi",
        "category": "Network Tool",
    },
    "com.carusto.PacketSender": {
        "app_name": "Packet Sender",
        "app_name_en": "Packet Sender",
        "developer": "Carusto",
        "category": "Network Tool",
    },
    "com.pcap.reader": {
        "app_name": "Pcap Reader",
        "app_name_en": "PCAP Reader",
        "developer": "Pcap Tools",
        "category": "Network Tool",
    },
    "com.ddm.portdroid": {
        "app_name": "PortDroid",
        "app_name_en": "PortDroid",
        "developer": "D.D.M.",
        "category": "Network Tool",
    },
    "com.termux.networking": {
        "app_name": "Nmap (via Termux)",
        "app_name_en": "Nmap",
        "developer": "Nmap Project",
        "category": "Network Tool",
    },
    "com.netsparker.android": {
        "app_name": "Netsparker",
        "app_name_en": "Netsparker",
        "developer": "Netsparker",
        "category": "Network Tool",
    },
    "com.zimperium.zanti": {
        "app_name": "zANTI",
        "app_name_en": "zANTI",
        "developer": "Zimperium",
        "category": "Network Tool",
    },
    "org.csploit.android": {
        "app_name": "cSploit",
        "app_name_en": "cSploit",
        "developer": "cSploit Team",
        "category": "Network Tool",
    },
    "com.dsploit.android": {
        "app_name": "dSploit",
        "app_name_en": "dSploit",
        "developer": "dSploit Team",
        "category": "Network Tool",
    },
    "net.ponury.wifikill": {
        "app_name": "WiFi Kill",
        "app_name_en": "WiFi Kill",
        "developer": "Ponury",
        "category": "Network Tool",
    },
    "com.netcut.android": {
        "app_name": "NetCut",
        "app_name_en": "NetCut",
        "developer": "Arcai",
        "category": "Network Tool",
    },
    "com.droidsheep.app": {
        "app_name": "DroidSheep",
        "app_name_en": "DroidSheep",
        "developer": "DroidSheep Project",
        "category": "Network Tool",
    },
    "com.faceniff.app": {
        "app_name": "FaceNiff",
        "app_name_en": "FaceNiff",
        "developer": "FaceNiff",
        "category": "Network Tool",
    },
    "com.pdanet": {
        "app_name": "PdaNet+",
        "app_name_en": "PdaNet+",
        "developer": "June Fabrics",
        "category": "Network Tool",
    },
    "com.foxfi": {
        "app_name": "FoxFi",
        "app_name_en": "FoxFi Tethering",
        "developer": "FoxFi Software",
        "category": "Network Tool",
    },
    "com.opengarden": {
        "app_name": "FireChat",
        "app_name_en": "FireChat / Open Garden",
        "developer": "Open Garden",
        "category": "Network Tool",
    },
    "com.sand.airdroid": {
        "app_name": "AirDroid",
        "app_name_en": "AirDroid",
        "developer": "Sand Studio",
        "category": "Network Tool",
    },
    "com.sand.airmirror": {
        "app_name": "AirMirror",
        "app_name_en": "AirMirror",
        "developer": "Sand Studio",
        "category": "Network Tool",
    },
    "com.teamviewer.teamviewer.market.mobile": {
        "app_name": "TeamViewer",
        "app_name_en": "TeamViewer Remote Control",
        "developer": "TeamViewer",
        "category": "Network Tool",
    },
    "com.anydesk.anydeskandroid": {
        "app_name": "AnyDesk",
        "app_name_en": "AnyDesk Remote Desktop",
        "developer": "AnyDesk Software",
        "category": "Network Tool",
    },
    "com.splashtop.remote.pad": {
        "app_name": "Splashtop",
        "app_name_en": "Splashtop Remote",
        "developer": "Splashtop",
        "category": "Network Tool",
    },
    "com.logmein.rescue": {
        "app_name": "GoToAssist",
        "app_name_en": "GoToAssist / LogMeIn",
        "developer": "LogMeIn",
        "category": "Network Tool",
    },
    "com.connectwise.control": {
        "app_name": "ConnectWise Control",
        "app_name_en": "ConnectWise Control",
        "developer": "ConnectWise",
        "category": "Network Tool",
    },
    "com.logmein.ignition": {
        "app_name": "LogMeIn",
        "app_name_en": "LogMeIn",
        "developer": "LogMeIn",
        "category": "Network Tool",
    },

    # =========================================================================
    # --- Spyware / Stalkerware (commonly found in forensics) ---
    # =========================================================================
    "com.spyzie.app": {
        "app_name": "Spyzie",
        "app_name_en": "Spyzie",
        "developer": "Spyzie",
        "category": "Spyware",
    },
    "com.mspy.android": {
        "app_name": "mSpy",
        "app_name_en": "mSpy",
        "developer": "mSpy",
        "category": "Spyware",
    },
    "com.flexispy.android": {
        "app_name": "FlexiSPY",
        "app_name_en": "FlexiSPY",
        "developer": "FlexiSPY",
        "category": "Spyware",
    },
    "com.hoverwatch.android": {
        "app_name": "Hoverwatch",
        "app_name_en": "Hoverwatch",
        "developer": "Hoverwatch",
        "category": "Spyware",
    },
    "com.thetruthspy.android": {
        "app_name": "TheTruthSpy",
        "app_name_en": "TheTruthSpy",
        "developer": "TheTruthSpy",
        "category": "Spyware",
    },
    "com.xnspy.android": {
        "app_name": "XNSpy",
        "app_name_en": "XNSpy",
        "developer": "XNSpy",
        "category": "Spyware",
    },
    "com.cocospy.android": {
        "app_name": "Cocospy",
        "app_name_en": "Cocospy",
        "developer": "Cocospy",
        "category": "Spyware",
    },
    "com.spyic.android": {
        "app_name": "Spyic",
        "app_name_en": "Spyic",
        "developer": "Spyic",
        "category": "Spyware",
    },
    "com.umobix.android": {
        "app_name": "uMobix",
        "app_name_en": "uMobix",
        "developer": "uMobix",
        "category": "Spyware",
    },
    "com.eyezylive.android": {
        "app_name": "eyeZy",
        "app_name_en": "eyeZy",
        "developer": "eyeZy",
        "category": "Spyware",
    },
    "com.phone.monitor": {
        "app_name": "Phone Monitor",
        "app_name_en": "Phone Monitor",
        "developer": "Unknown",
        "category": "Spyware",
    },
    "com.spapp.app": {
        "app_name": "Spapp Monitoring",
        "app_name_en": "Spapp Monitoring",
        "developer": "Spapp Monitoring",
        "category": "Spyware",
    },
    "com.phonesheriff.app": {
        "app_name": "PhoneSheriff",
        "app_name_en": "PhoneSheriff",
        "developer": "PhoneSheriff",
        "category": "Spyware",
    },
    "com.mobistealth.app": {
        "app_name": "MobiStealth",
        "app_name_en": "MobiStealth",
        "developer": "MobiStealth",
        "category": "Spyware",
    },
    "com.copy9.app": {
        "app_name": "Copy9",
        "app_name_en": "Copy9",
        "developer": "Copy9",
        "category": "Spyware",
    },
    "com.ikeymonitor.app": {
        "app_name": "iKeyMonitor",
        "app_name_en": "iKeyMonitor",
        "developer": "iKeyMonitor",
        "category": "Spyware",
    },
    "com.highstermobile.pro": {
        "app_name": "Highster Mobile",
        "app_name_en": "Highster Mobile",
        "developer": "Highster Mobile",
        "category": "Spyware",
    },
    "com.ddiutilites.auto": {
        "app_name": "DDI Utilities",
        "app_name_en": "DDI Utilities",
        "developer": "DDI Utilities",
        "category": "Spyware",
    },
    "com.systemservice.update": {
        "app_name": "System Update",
        "app_name_en": "System Update (Covert)",
        "developer": "Unknown",
        "category": "Spyware",
    },
    "com.system.sync.service": {
        "app_name": "System Sync Service",
        "app_name_en": "System Sync (Covert)",
        "developer": "Unknown",
        "category": "Spyware",
    },

    # =========================================================================
    # --- Chinese Gambling / Porn / Illegal Apps (Forensics) ---
    # =========================================================================
    "com.hg168.app": {
        "app_name": "皇冠体育",
        "app_name_en": "Crown Sports Betting",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.tyc.app": {
        "app_name": "太阳城",
        "app_name_en": "Sun City Casino",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.yl.app": {
        "app_name": "永利娱乐",
        "app_name_en": "Wynn Casino",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.js88.app": {
        "app_name": "金沙娱乐场",
        "app_name_en": "Sands Casino",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.mgm.app": {
        "app_name": "美高梅",
        "app_name_en": "MGM Casino",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.xpj.app": {
        "app_name": "新葡京",
        "app_name_en": "Grand Lisboa Casino",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.am银河.app": {
        "app_name": "澳门银河",
        "app_name_en": "Galaxy Macau Casino",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.jdb168.app": {
        "app_name": "金多宝",
        "app_name_en": "Jin Duo Bao Lottery",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.bet365.android": {
        "app_name": "Bet365",
        "app_name_en": "Bet365",
        "developer": "Bet365",
        "category": "Gambling",
    },
    "com.betway.android": {
        "app_name": "Betway",
        "app_name_en": "Betway",
        "developer": "Betway",
        "category": "Gambling",
    },
    "com.williamhill.android": {
        "app_name": "William Hill",
        "app_name_en": "William Hill",
        "developer": "William Hill",
        "category": "Gambling",
    },
    "com.paddypower.android": {
        "app_name": "Paddy Power",
        "app_name_en": "Paddy Power",
        "developer": "Paddy Power",
        "category": "Gambling",
    },
    "com.betfair.android": {
        "app_name": "Betfair",
        "app_name_en": "Betfair",
        "developer": "Betfair",
        "category": "Gambling",
    },
    "com.tencent.jkchess": {
        "app_name": "金铲铲棋牌",
        "app_name_en": "Jin Chan Chan Card Game",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.yy.qipai": {
        "app_name": "YY棋牌",
        "app_name_en": "YY Card Games",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.jj.qipai": {
        "app_name": "JJ棋牌",
        "app_name_en": "JJ Card Game",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.dezhoupuke.app": {
        "app_name": "德州扑克大师",
        "app_name_en": "Texas Holdem Master",
        "developer": "Unknown",
        "category": "Gambling",
    },
    "com.liveporn.app": {
        "app_name": "夜色直播",
        "app_name_en": "Adult Live Stream",
        "developer": "Unknown",
        "category": "Adult Content",
    },
    "com.sex.live": {
        "app_name": "色情直播",
        "app_name_en": "Adult Live",
        "developer": "Unknown",
        "category": "Adult Content",
    },
    "com.meitu91.app": {
        "app_name": "91视频",
        "app_name_en": "91 Video",
        "developer": "Unknown",
        "category": "Adult Content",
    },
    "com.bobocam.app": {
        "app_name": "波波视频",
        "app_name_en": "Bobo Adult Video",
        "developer": "Unknown",
        "category": "Adult Content",
    },
    "com.avnight.app": {
        "app_name": "AV Night",
        "app_name_en": "AV Night",
        "developer": "Unknown",
        "category": "Adult Content",
    },
    "com.lululu.app": {
        "app_name": "撸撸社",
        "app_name_en": "Lululu Adult",
        "developer": "Unknown",
        "category": "Adult Content",
    },
    "com.chengren.app": {
        "app_name": "成人视频",
        "app_name_en": "Adult Video",
        "developer": "Unknown",
        "category": "Adult Content",
    },
    "com.pornhub.android": {
        "app_name": "Pornhub",
        "app_name_en": "Pornhub",
        "developer": "Aylo",
        "category": "Adult Content",
    },
    "com.xvideos.android": {
        "app_name": "XVideos",
        "app_name_en": "XVideos",
        "developer": "XVideos",
        "category": "Adult Content",
    },
    "com.chuanxiao.app": {
        "app_name": "云联惠",
        "app_name_en": "Yunlianhui (Ponzi)",
        "developer": "Unknown",
        "category": "Ponzi Scheme",
    },
    "com.plustoken.app": {
        "app_name": "PlusToken",
        "app_name_en": "PlusToken (Ponzi)",
        "developer": "Unknown",
        "category": "Ponzi Scheme",
    },
    "com.wotoken.app": {
        "app_name": "WoToken",
        "app_name_en": "WoToken (Ponzi)",
        "developer": "Unknown",
        "category": "Ponzi Scheme",
    },
    "com.shanzhu.app": {
        "app_name": "善心汇",
        "app_name_en": "Shanxinhui (Ponzi)",
        "developer": "Unknown",
        "category": "Ponzi Scheme",
    },

    # =========================================================================
    # --- More Chinese Bank Apps ---
    # =========================================================================
    "cn.com.cmbc.newmbank": {
        "app_name": "招商银行",
        "app_name_en": "China Merchants Bank",
        "developer": "招商银行",
        "category": "Finance",
    },
    "com.hxb.mobilebank": {
        "app_name": "华夏银行",
        "app_name_en": "Huaxia Bank",
        "developer": "华夏银行",
        "category": "Finance",
    },
    "cn.com.bankofbeijing.mobilebanking": {
        "app_name": "北京银行",
        "app_name_en": "Bank of Beijing",
        "developer": "北京银行",
        "category": "Finance",
    },
    "com.bankofshanghai.mobilebank": {
        "app_name": "上海银行",
        "app_name_en": "Bank of Shanghai",
        "developer": "上海银行",
        "category": "Finance",
    },
    "com.jsb.mobilebank": {
        "app_name": "江苏银行",
        "app_name_en": "Jiangsu Bank",
        "developer": "江苏银行",
        "category": "Finance",
    },
    "com.zjtlcb.mobilebank": {
        "app_name": "浙江泰隆商业银行",
        "app_name_en": "Zhejiang Tailong Bank",
        "developer": "浙江泰隆商业银行",
        "category": "Finance",
    },
    "com.czb.mobilebank": {
        "app_name": "浙商银行",
        "app_name_en": "CZB",
        "developer": "浙商银行",
        "category": "Finance",
    },
    "com.boc.bank": {
        "app_name": "中国银行缤纷生活",
        "app_name_en": "BOC Life",
        "developer": "中国银行",
        "category": "Finance",
    },
    "com.hxb.mbank": {
        "app_name": "华夏银行",
        "app_name_en": "HXB Mobile",
        "developer": "华夏银行",
        "category": "Finance",
    },
    "com.bankofgz.mobilebank": {
        "app_name": "广州银行",
        "app_name_en": "Bank of Guangzhou",
        "developer": "广州银行",
        "category": "Finance",
    },
    "com.sz.bank": {
        "app_name": "深圳农商银行",
        "app_name_en": "Shenzhen Rural Bank",
        "developer": "深圳农商银行",
        "category": "Finance",
    },
    "com.cqbank.mobile": {
        "app_name": "重庆银行",
        "app_name_en": "Chongqing Bank",
        "developer": "重庆银行",
        "category": "Finance",
    },
    "com.cbhb.mobile": {
        "app_name": "渤海银行",
        "app_name_en": "CBHB",
        "developer": "渤海银行",
        "category": "Finance",
    },
    "com.hrbcb.mobile": {
        "app_name": "哈尔滨银行",
        "app_name_en": "Harbin Bank",
        "developer": "哈尔滨银行",
        "category": "Finance",
    },
    "com.bankofcd.mobile": {
        "app_name": "成都银行",
        "app_name_en": "Bank of Chengdu",
        "developer": "成都银行",
        "category": "Finance",
    },
    "com.njcb.mobile": {
        "app_name": "南京银行",
        "app_name_en": "Bank of Nanjing",
        "developer": "南京银行",
        "category": "Finance",
    },
    "com.hzbank.mobile": {
        "app_name": "杭州银行",
        "app_name_en": "Bank of Hangzhou",
        "developer": "杭州银行",
        "category": "Finance",
    },
    "com.tccb.mobile": {
        "app_name": "天津银行",
        "app_name_en": "Bank of Tianjin",
        "developer": "天津银行",
        "category": "Finance",
    },
    "com.sdb.mobile": {
        "app_name": "深圳发展银行",
        "app_name_en": "Shenzhen Dev Bank",
        "developer": "深圳发展银行",
        "category": "Finance",
    },
    "com.gdb.mobile": {
        "app_name": "广发银行",
        "app_name_en": "Guangfa Bank / CGB",
        "developer": "广发银行",
        "category": "Finance",
    },

    # =========================================================================
    # --- City Service / Government Apps ---
    # =========================================================================
    "com.iflytek.cbg": {
        "app_name": "国家反诈中心",
        "app_name_en": "National Anti-Fraud Center",
        "developer": "公安部",
        "category": "Government",
    },
    "cn.gov.tax.its": {
        "app_name": "个人所得税",
        "app_name_en": "Individual Income Tax",
        "developer": "国家税务总局",
        "category": "Government",
    },
    "cn.gov.samr.market": {
        "app_name": "全国12315平台",
        "app_name_en": "12315 Consumer Platform",
        "developer": "国家市场监督管理总局",
        "category": "Government",
    },
    "com.example.shanghai.gov": {
        "app_name": "随申办",
        "app_name_en": "Shanghai Government Services",
        "developer": "上海市政府",
        "category": "Government",
    },
    "com.example.beijing.gov": {
        "app_name": "北京通",
        "app_name_en": "Beijing Government Services",
        "developer": "北京市政府",
        "category": "Government",
    },
    "com.example.guangdong.gov": {
        "app_name": "粤省事",
        "app_name_en": "Guangdong Government Services",
        "developer": "广东省政府",
        "category": "Government",
    },
    "com.example.zhejiang.gov": {
        "app_name": "浙里办",
        "app_name_en": "Zhejiang Government Services",
        "developer": "浙江省政府",
        "category": "Government",
    },
    "com.example.jiangsu.gov": {
        "app_name": "江苏政务服务",
        "app_name_en": "Jiangsu Government Services",
        "developer": "江苏省政府",
        "category": "Government",
    },
    "com.example.sichuan.gov": {
        "app_name": "天府通办",
        "app_name_en": "Sichuan Government Services",
        "developer": "四川省政府",
        "category": "Government",
    },
    "com.example.shenzhen.gov": {
        "app_name": "i深圳",
        "app_name_en": "Shenzhen Government Services",
        "developer": "深圳市政府",
        "category": "Government",
    },
    "com.example.guangzhou.gov": {
        "app_name": "穗好办",
        "app_name_en": "Guangzhou Government Services",
        "developer": "广州市政府",
        "category": "Government",
    },
    "com.example.hangzhou.gov": {
        "app_name": "浙里办·杭州",
        "app_name_en": "Hangzhou Government Services",
        "developer": "杭州市政府",
        "category": "Government",
    },
    "com.icbc": {
        "app_name": "交管12123",
        "app_name_en": "Traffic Management 12123",
        "developer": "公安部交通管理局",
        "category": "Government",
    },
    "com.ebooc.sz.bus": {
        "app_name": "深圳通",
        "app_name_en": "Shenzhen Tong",
        "developer": "深圳通",
        "category": "Travel & Local",
    },
    "com.yw.seu": {
        "app_name": "国务院",
        "app_name_en": "State Council of China",
        "developer": "国务院办公厅",
        "category": "Government",
    },
    "com.tmri.app.main": {
        "app_name": "交管12123",
        "app_name_en": "Traffic 12123",
        "developer": "公安部交通管理科学研究所",
        "category": "Government",
    },
    "com.hikvision.ga": {
        "app_name": "公安110",
        "app_name_en": "Police 110",
        "developer": "公安部",
        "category": "Government",
    },
    "com.gongshang.gov": {
        "app_name": "国家企业信用信息公示",
        "app_name_en": "National Enterprise Credit Info",
        "developer": "国家市场监督管理总局",
        "category": "Government",
    },

    # =========================================================================
    # --- Additional Life / Consumer Apps ---
    # =========================================================================
    "com.greenhouse.app": {
        "app_name": "多抓鱼",
        "app_name_en": "Duozhuayu",
        "developer": "多抓鱼",
        "category": "Shopping",
    },
    "com.chaoshi.app": {
        "app_name": "天猫超市",
        "app_name_en": "Tmall Supermarket",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },
    "com.taobao.tmallgou": {
        "app_name": "天猫国际",
        "app_name_en": "Tmall Global",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },
    "com.rtmart.app": {
        "app_name": "大润发优鲜",
        "app_name_en": "RT-Mart Fresh",
        "developer": "高鑫零售",
        "category": "Shopping",
    },
    "com.taobao.ju": {
        "app_name": "聚划算",
        "app_name_en": "Juhuasuan",
        "developer": "阿里巴巴",
        "category": "Shopping",
    },
    "com.pdd.app": {
        "app_name": "拼多多商家版",
        "app_name_en": "PDD Merchant",
        "developer": "拼多多",
        "category": "Shopping",
    },
    "com.baipiao.app": {
        "app_name": "什么值得买",
        "app_name_en": "SMZDM",
        "developer": "值得买科技",
        "category": "Shopping",
    },
    "com.woshipm.app": {
        "app_name": "人人都是产品经理",
        "app_name_en": "Woshipm",
        "developer": "人人都是产品经理",
        "category": "News & Magazines",
    },
    "com.iresearch.app": {
        "app_name": "艾瑞咨询",
        "app_name_en": "iResearch",
        "developer": "艾瑞咨询",
        "category": "News & Magazines",
    },
    "com.huxiu.app": {
        "app_name": "虎嗅",
        "app_name_en": "Huxiu",
        "developer": "虎嗅",
        "category": "News & Magazines",
    },
    "com.geekpark.app": {
        "app_name": "极客公园",
        "app_name_en": "GeekPark",
        "developer": "极客公园",
        "category": "News & Magazines",
    },
    "com.36kr.app": {
        "app_name": "36氪",
        "app_name_en": "36Kr",
        "developer": "36氪",
        "category": "News & Magazines",
    },
    "com.cls.dayu": {
        "app_name": "财联社",
        "app_name_en": "CLS / Cailian Press",
        "developer": "财联社",
        "category": "News & Magazines",
    },
    "com.yicai.app": {
        "app_name": "第一财经",
        "app_name_en": "Yicai / CBN",
        "developer": "第一财经",
        "category": "News & Magazines",
    },
    "com.caixin.app": {
        "app_name": "财新",
        "app_name_en": "Caixin",
        "developer": "财新传媒",
        "category": "News & Magazines",
    },
    "com.jianshu.app": {
        "app_name": "简书",
        "app_name_en": "Jianshu",
        "developer": "简书",
        "category": "Social",
    },
    "com.luojilab.docs": {
        "app_name": "石墨文档",
        "app_name_en": "Shimo Docs",
        "developer": "石墨文档",
        "category": "Productivity",
    },
    "com.dingyi.app": {
        "app_name": "钉钉文档",
        "app_name_en": "DingTalk Docs",
        "developer": "阿里巴巴",
        "category": "Productivity",
    },
    "com.xmpp.app": {
        "app_name": "飞书文档",
        "app_name_en": "Feishu Docs",
        "developer": "字节跳动",
        "category": "Productivity",
    },
    "com.processon.app": {
        "app_name": "ProcessOn",
        "app_name_en": "ProcessOn",
        "developer": "ProcessOn",
        "category": "Productivity",
    },
    "com.mubu.app": {
        "app_name": "幕布",
        "app_name_en": "Mubu",
        "developer": "幕布",
        "category": "Productivity",
    },
    "com.xmind.app": {
        "app_name": "XMind",
        "app_name_en": "XMind",
        "developer": "XMind",
        "category": "Productivity",
    },
    "com.baby.tree": {
        "app_name": "宝宝树",
        "app_name_en": "Babytree",
        "developer": "宝宝树",
        "category": "Parenting",
    },
    "com.mama.cn": {
        "app_name": "妈妈网",
        "app_name_en": "Mama.cn",
        "developer": "妈妈网",
        "category": "Parenting",
    },
    "com.qinbaobao.app": {
        "app_name": "亲宝宝",
        "app_name_en": "Qinbaobao",
        "developer": "亲宝宝",
        "category": "Parenting",
    },
    "com.ibaby.app": {
        "app_name": "育学园",
        "app_name_en": "iBaby / Yuxueyuan",
        "developer": "育学园",
        "category": "Parenting",
    },
    "com.babytime.app": {
        "app_name": "宝宝时光",
        "app_name_en": "Baby Time",
        "developer": "宝宝时光",
        "category": "Parenting",
    },
    "com.boo.chong": {
        "app_name": "波奇宠物",
        "app_name_en": "Boqi Pet",
        "developer": "波奇宠物",
        "category": "Pet",
    },
    "com.taoqibao.app": {
        "app_name": "淘气宝宠物",
        "app_name_en": "Taoqibao Pet",
        "developer": "淘气宝",
        "category": "Pet",
    },
    "com.chongwuba.app": {
        "app_name": "宠物吧",
        "app_name_en": "Pet Bar",
        "developer": "宠物吧",
        "category": "Pet",
    },
    "com.rabbit.app": {
        "app_name": "兔子宠物",
        "app_name_en": "Rabbit Pet",
        "developer": "兔子宠物",
        "category": "Pet",
    },
    "com.maomeng.app": {
        "app_name": "猫盟",
        "app_name_en": "Cat Alliance",
        "developer": "猫盟",
        "category": "Pet",
    },
    "com.jobtong.app": {
        "app_name": "Boss直聘",
        "app_name_en": "BOSS Zhipin",
        "developer": "BOSS直聘",
        "category": "Business",
    },
    "com.kanzhun.app": {
        "app_name": "看准",
        "app_name_en": "Kanzhun",
        "developer": "看准网",
        "category": "Business",
    },
    "com.haoyun.app": {
        "app_name": "好孕妈",
        "app_name_en": "Good Pregnancy",
        "developer": "好孕妈",
        "category": "Parenting",
    },
    "com.zhipin.boss": {
        "app_name": "店长直聘",
        "app_name_en": "Dianzhang Zhipin",
        "developer": "BOSS直聘",
        "category": "Business",
    },
    "com.kanzhun.zhipin": {
        "app_name": "看准直聘",
        "app_name_en": "Kanzhun Zhipin",
        "developer": "看准网",
        "category": "Business",
    },
    "com.baijiahulian.app": {
        "app_name": "猎聘同道",
        "app_name_en": "Liepin Tongdao",
        "developer": "猎聘",
        "category": "Business",
    },
    "com.job51.app": {
        "app_name": "前程无忧",
        "app_name_en": "51Job",
        "developer": "前程无忧",
        "category": "Business",
    },
    "com.guazi.app": {
        "app_name": "瓜子二手车",
        "app_name_en": "Guazi Used Car",
        "developer": "车好多",
        "category": "Auto & Vehicles",
    },
    "com.yiche.autohome": {
        "app_name": "汽车报价大全",
        "app_name_en": "Auto Price Guide",
        "developer": "汽车之家",
        "category": "Auto & Vehicles",
    },
    "com.che168.app": {
        "app_name": "二手车之家",
        "app_name_en": "Used Car Home",
        "developer": "汽车之家",
        "category": "Auto & Vehicles",
    },
    "com.renrenche.app": {
        "app_name": "人人车",
        "app_name_en": "Renrenche",
        "developer": "人人车",
        "category": "Auto & Vehicles",
    },
    "com.dayangche.app": {
        "app_name": "大搜车",
        "app_name_en": "Dasouche",
        "developer": "大搜车",
        "category": "Auto & Vehicles",
    },
    "com.maodoo.app": {
        "app_name": "毛豆新车",
        "app_name_en": "Maodoo New Car",
        "developer": "车好多",
        "category": "Auto & Vehicles",
    },
    "com.bilibili.comic": {
        "app_name": "哔哩哔哩漫画",
        "app_name_en": "Bilibili Comics",
        "developer": "哔哩哔哩",
        "category": "Entertainment",
    },
    "com.kuaikan.comic": {
        "app_name": "快看漫画",
        "app_name_en": "Kuaikan Comics",
        "developer": "快看漫画",
        "category": "Entertainment",
    },
    "com.u17.comic": {
        "app_name": "有妖气漫画",
        "app_name_en": "U17 Comics",
        "developer": "有妖气",
        "category": "Entertainment",
    },
    "com.dongman.comic": {
        "app_name": "咚漫",
        "app_name_en": "Dongman Comics",
        "developer": "咚漫",
        "category": "Entertainment",
    },
    "com.tencent.comic": {
        "app_name": "腾讯动漫",
        "app_name_en": "Tencent Comics",
        "developer": "腾讯",
        "category": "Entertainment",
    },
    "com.netease.comic": {
        "app_name": "网易漫画",
        "app_name_en": "NetEase Comics",
        "developer": "网易",
        "category": "Entertainment",
    },
    "com.zhangyue.iReader": {
        "app_name": "掌阅",
        "app_name_en": "iReader",
        "developer": "掌阅科技",
        "category": "Books & Reference",
    },
    "com.iflytek.ebook": {
        "app_name": "讯飞有声书",
        "app_name_en": "iFlytek Audio Book",
        "developer": "科大讯飞",
        "category": "Books & Reference",
    },
    "com.qidian.reader": {
        "app_name": "起点读书",
        "app_name_en": "Qidian Reader",
        "developer": "阅文集团",
        "category": "Books & Reference",
    },
    "com.dureader.app": {
        "app_name": "多看阅读",
        "app_name_en": "Duokan Reader",
        "developer": "小米",
        "category": "Books & Reference",
    },
    "com.shuqi.reader": {
        "app_name": "书旗小说",
        "app_name_en": "Shuqi Novel",
        "developer": "书旗小说",
        "category": "Books & Reference",
    },
    "com.zhongzheng.app": {
        "app_name": "中证估值",
        "app_name_en": "China Bond Valuation",
        "developer": "中证指数",
        "category": "Finance",
    },
    "com.lufax.app": {
        "app_name": "陆金所",
        "app_name_en": "Lufax / Lu.com",
        "developer": "陆金所",
        "category": "Finance",
    },
    "com.ppdai.app": {
        "app_name": "拍拍贷",
        "app_name_en": "PPDai",
        "developer": "拍拍贷",
        "category": "Finance",
    },
    "com.renrendai.app": {
        "app_name": "人人贷",
        "app_name_en": "Renrendai",
        "developer": "人人贷",
        "category": "Finance",
    },
    "com.yirendai.app": {
        "app_name": "宜人贷",
        "app_name_en": "Yirendai",
        "developer": "宜信",
        "category": "Finance",
    },
    "com.jimubox.app": {
        "app_name": "积木盒子",
        "app_name_en": "Jimubox",
        "developer": "积木盒子",
        "category": "Finance",
    },
    "com.wecash.app": {
        "app_name": "我来贷",
        "app_name_en": "WeLab",
        "developer": "WeLab",
        "category": "Finance",
    },
    "com.qufenqi.app": {
        "app_name": "趣分期",
        "app_name_en": "Qufenqi",
        "developer": "趣分期",
        "category": "Finance",
    },
    "com.fenqile.app": {
        "app_name": "分期乐",
        "app_name_en": "Fenqile",
        "developer": "乐信",
        "category": "Finance",
    },
    "com.aixuedai.app": {
        "app_name": "爱学贷",
        "app_name_en": "Aixuedai",
        "developer": "爱学贷",
        "category": "Finance",
    },
    "com.zhongan.app": {
        "app_name": "众安保险",
        "app_name_en": "ZhongAn Insurance",
        "developer": "众安保险",
        "category": "Finance",
    },
    "com.pingan.insurance": {
        "app_name": "平安保险",
        "app_name_en": "Ping An Insurance",
        "developer": "中国平安",
        "category": "Finance",
    },
    "com.taikang.insurance": {
        "app_name": "泰康在线",
        "app_name_en": "Taikang Online Insurance",
        "developer": "泰康保险",
        "category": "Finance",
    },
    "com.cpic.insurance": {
        "app_name": "太平洋保险",
        "app_name_en": "CPIC Insurance",
        "developer": "太平洋保险",
        "category": "Finance",
    },
    "com.picc.insurance": {
        "app_name": "人保保险",
        "app_name_en": "PICC Insurance",
        "developer": "中国人保",
        "category": "Finance",
    },
    "com.chinalife.insurance": {
        "app_name": "中国人寿",
        "app_name_en": "China Life Insurance",
        "developer": "中国人寿",
        "category": "Finance",
    },
    "com.hanxin.app": {
        "app_name": "还信用卡",
        "app_name_en": "Credit Card Repay",
        "developer": "51信用卡",
        "category": "Finance",
    },
    "com.u51.app": {
        "app_name": "51信用卡管家",
        "app_name_en": "51 Credit Card Manager",
        "developer": "51信用卡",
        "category": "Finance",
    },
    "com.zhangdan.app": {
        "app_name": "随手记",
        "app_name_en": "Suishouji",
        "developer": "随手记",
        "category": "Finance",
    },
    "com.walletkeeper.app": {
        "app_name": "挖财记账",
        "app_name_en": "Wacai Bookkeeping",
        "developer": "挖财",
        "category": "Finance",
    },
    "com.qianbao.app": {
        "app_name": "钱宝",
        "app_name_en": "Qianbao",
        "developer": "钱宝",
        "category": "Finance",
    },

    # =========================================================================
    # --- Educational Apps ---
    # =========================================================================
    "com.yy.talk": {
        "app_name": "英语流利说",
        "app_name_en": "LAIX / Liulishuo",
        "developer": "流利说",
        "category": "Education",
    },
    "com.openlanguage.app": {
        "app_name": "开言英语",
        "app_name_en": "Open Language",
        "developer": "开言英语",
        "category": "Education",
    },
    "com.boxfish.app": {
        "app_name": "盒子鱼英语",
        "app_name_en": "BoxFish English",
        "developer": "盒子鱼",
        "category": "Education",
    },
    "com.vipkid.app": {
        "app_name": "VIPKID",
        "app_name_en": "VIPKID",
        "developer": "VIPKID",
        "category": "Education",
    },
    "com.ttt.app": {
        "app_name": "英语趣配音",
        "app_name_en": "English Dubbing",
        "developer": "杭州菲助科技",
        "category": "Education",
    },
    "com.xunfei.speaking": {
        "app_name": "口语100",
        "app_name_en": "Speaking 100",
        "developer": "科大讯飞",
        "category": "Education",
    },
    "com.aixuexi.app": {
        "app_name": "爱学习",
        "app_name_en": "Aixuexi",
        "developer": "爱学习",
        "category": "Education",
    },
    "com.xiaoe.app": {
        "app_name": "小鹅通",
        "app_name_en": "XiaoE Tech",
        "developer": "小鹅通",
        "category": "Education",
    },
    "com.zhixue.app": {
        "app_name": "知学",
        "app_name_en": "Zhixue",
        "developer": "知学云",
        "category": "Education",
    },
    "com.edu.people.cn": {
        "app_name": "人教点读",
        "app_name_en": "PEP E-textbook",
        "developer": "人民教育出版社",
        "category": "Education",
    },
    "com.xdf.app": {
        "app_name": "新东方",
        "app_name_en": "New Oriental",
        "developer": "新东方",
        "category": "Education",
    },
    "com.xdf.koolearn": {
        "app_name": "新东方在线",
        "app_name_en": "Koolearn / New Oriental Online",
        "developer": "新东方在线",
        "category": "Education",
    },
    "com.koolearn.app": {
        "app_name": "酷学",
        "app_name_en": "Koolearn App",
        "developer": "新东方在线",
        "category": "Education",
    },

    # =========================================================================
    # --- More Investment / Stock Apps ---
    # =========================================================================
    "com.wind.mobile": {
        "app_name": "Wind金融终端",
        "app_name_en": "Wind Financial Terminal",
        "developer": "万得",
        "category": "Finance",
    },
    "com.choice.mobile": {
        "app_name": "Choice数据",
        "app_name_en": "Choice Data",
        "developer": "东方财富",
        "category": "Finance",
    },
    "com.10jqka.finance": {
        "app_name": "同花顺期货通",
        "app_name_en": "THS Futures",
        "developer": "同花顺",
        "category": "Finance",
    },
    "com.wenhua.finance": {
        "app_name": "文华财经",
        "app_name_en": "Wenhua Finance",
        "developer": "文华财经",
        "category": "Finance",
    },
    "com.bohaifinance.app": {
        "app_name": "渤海期货",
        "app_name_en": "Bohai Futures",
        "developer": "渤海期货",
        "category": "Finance",
    },
    "com.futu.mobile": {
        "app_name": "富途牛牛",
        "app_name_en": "Futu MooMoo",
        "developer": "富途控股",
        "category": "Finance",
    },
    "com.tigerbrokers.app": {
        "app_name": "老虎证券",
        "app_name_en": "Tiger Brokers",
        "developer": "老虎证券",
        "category": "Finance",
    },
    "com.webull.app": {
        "app_name": "微牛",
        "app_name_en": "Webull",
        "developer": "Webull",
        "category": "Finance",
    },
    "com.robinhood.android": {
        "app_name": "Robinhood",
        "app_name_en": "Robinhood",
        "developer": "Robinhood Markets",
        "category": "Finance",
    },
    "com.interactivebrokers.android": {
        "app_name": "盈透证券",
        "app_name_en": "Interactive Brokers",
        "developer": "Interactive Brokers",
        "category": "Finance",
    },
    "com.chongdiantou.app": {
        "app_name": "充电头网",
        "app_name_en": "Chongdiantou",
        "developer": "充电头网",
        "category": "Lifestyle",
    },
    "com.smarthome.app": {
        "app_name": "智家365",
        "app_name_en": "Smart Home 365",
        "developer": "欧瑞博",
        "category": "Lifestyle",
    },
    "com.orvibo.app": {
        "app_name": "欧瑞博",
        "app_name_en": "ORVIBO Smart Home",
        "developer": "欧瑞博",
        "category": "Lifestyle",
    },
    "com.aqara.app": {
        "app_name": "Aqara Home",
        "app_name_en": "Aqara Home",
        "developer": "绿米联创",
        "category": "Lifestyle",
    },
    "com.yunmi.app": {
        "app_name": "云米",
        "app_name_en": "Viomi Smart Home",
        "developer": "云米科技",
        "category": "Lifestyle",
    },
    "com.roborock.sweeper": {
        "app_name": "石头扫地机",
        "app_name_en": "Roborock Vacuum",
        "developer": "石头科技",
        "category": "Lifestyle",
    },
    "com.dreame.app": {
        "app_name": "追觅",
        "app_name_en": "Dreame",
        "developer": "追觅科技",
        "category": "Lifestyle",
    },
    "com.narwal.app": {
        "app_name": "云鲸",
        "app_name_en": "Narwal",
        "developer": "云鲸智能",
        "category": "Lifestyle",
    },
    "com.ecovacs.app": {
        "app_name": "科沃斯",
        "app_name_en": "Ecovacs Home",
        "developer": "科沃斯",
        "category": "Lifestyle",
    },
    "com.inwatch.app": {
        "app_name": "华米手表",
        "app_name_en": "Zepp / Amazfit",
        "developer": "华米科技",
        "category": "Health & Fitness",
    },
    "com.honor.health": {
        "app_name": "荣耀运动健康",
        "app_name_en": "Honor Health",
        "developer": "荣耀",
        "category": "Health & Fitness",
    },
    "com.xiaomi.wearable": {
        "app_name": "小米穿戴",
        "app_name_en": "Xiaomi Wear",
        "developer": "小米",
        "category": "Health & Fitness",
    },
    "com.bong.cn": {
        "app_name": "bong手环",
        "app_name_en": "bong Fitness",
        "developer": "bong",
        "category": "Health & Fitness",
    },
    "cn.youth.news": {
        "app_name": "中青看点",
        "app_name_en": "Youth News",
        "developer": "中国青年报",
        "category": "News & Magazines",
    },
    "com.jiemian.news": {
        "app_name": "界面新闻",
        "app_name_en": "Jiemian News",
        "developer": "界面新闻",
        "category": "News & Magazines",
    },
    "com.lanjinger.news": {
        "app_name": "蓝鲸新闻",
        "app_name_en": "Lanjinger",
        "developer": "蓝鲸传媒",
        "category": "News & Magazines",
    },
    "com.guancha.news": {
        "app_name": "观察者网",
        "app_name_en": "Guancha.cn",
        "developer": "观察者网",
        "category": "News & Magazines",
    },
    "com.thecover.news": {
        "app_name": "封面新闻",
        "app_name_en": "The Cover News",
        "developer": "封面新闻",
        "category": "News & Magazines",
    },
    "com.chinanews.app": {
        "app_name": "中国新闻网",
        "app_name_en": "Chinanews",
        "developer": "中国新闻社",
        "category": "News & Magazines",
    },
    "com.huanqiu.news": {
        "app_name": "环球网",
        "app_name_en": "Huanqiu / Global Times",
        "developer": "环球网",
        "category": "News & Magazines",
    },
}
# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def scrape(db: AppDatabase) -> int:
    """Insert hard-coded Chinese app mappings into the database.

    Only inserts entries whose ``package_name`` is not already present,
    so it is safe to call this function multiple times without creating
    duplicates.

    Parameters
    ----------
    db : AppDatabase
        An open database instance (caller manages lifecycle).

    Returns
    -------
    int
        Number of **new** records inserted.
    """
    # Build the full record list with the correct 'source' field.
    records: list[dict] = []
    for package_name, info in CN_APP_DICT.items():
        records.append(
            {
                "package_name": package_name,
                "app_name": info["app_name"],
                "app_name_en": info.get("app_name_en"),
                "developer": info.get("developer"),
                "category": info.get("category"),
                "source": "cn_manual",
            }
        )

    # Determine which packages already exist in the database.
    all_packages = list(CN_APP_DICT.keys())
    existing_packages = {r["package_name"] for r in db.search_batch(all_packages)}
    new_records = [r for r in records if r["package_name"] not in existing_packages]

    if new_records:
        db.upsert_batch(new_records)

    return len(new_records)


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Chinese Manual App Scraper — self-test")
    print("=" * 60)

    db = AppDatabase()  # defaults to apps.db alongside database.py
    try:
        new_count = scrape(db)
        print(f"\nTotal new apps added: {new_count}")
        print(f"Total apps in database: {db.count()}")
        print(f"Total entries in CN_APP_DICT: {len(CN_APP_DICT)}")
    finally:
        db.close()
