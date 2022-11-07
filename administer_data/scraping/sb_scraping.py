import re, time
from .scraping import ScrapingBase, ScrapingSeleBase


class SBgetAreaURLs(ScrapingSeleBase):
    """
    検索する都道府県を指定して、絞り込み検索のところから各地域のURLのid部分を抽出
    {pref, area}の組を取得
    """
    pref_url_format = "https://www.softbank.jp/shop/search/list/?pref={0[pref]}"
    area_option_selecter = "#contents > section > div > div.shop-page-u96-loaded-contents.is-loaded > div.shop-page-u96-shop-search-container > div.shop-page-u96-shop-search-pulldown > div:nth-child(2) > select > option"

    pref_id_dict = {
        "01": "北海道",
        "02": "青森県",
        "03": "岩手県",
        "04": "宮城県",
        "05": "秋田県",
        "06": "山形県",
        "07": "福島県",
        "08": "茨城県",
        "09": "栃木県",
        "10": "群馬県",
        "11": "埼玉県",
        "12": "千葉県",
        "13": "東京都",
        "14": "神奈川県",
        "15": "新潟県",
        "16": "富山県",
        "17": "石川県",
        "18": "福井県",
        "19": "山梨県",
        "20": "長野県",
        "21": "岐阜県",
        "22": "静岡県",
        "23": "愛知県",
        "24": "三重県",
        "25": "滋賀県",
        "26": "京都府",
        "27": "大阪府",
        "28": "兵庫県",
        "29": "奈良県",
        "30": "和歌山県",
        "31": "鳥取県",
        "32": "島根県",
        "33": "岡山県",
        "34": "広島県",
        "35": "山口県",
        "36": "徳島県",
        "37": "香川県",
        "38": "愛媛県",
        "39": "高知県",
        "40": "福岡県",
        "41": "佐賀県",
        "42": "長崎県",
        "43": "熊本県",
        "44": "大分県",
        "45": "宮崎県",
        "46": "鹿児島県",
        "47": "沖縄県"
    }

    @classmethod
    def check_pref_dict_key(cls, key: str) -> bool:
        """
        keyはstr型、二桁じゃないとだめ、"01"~"47"
        """
        if not 0 < int(key) < 48:
            return False
        return key in cls.pref_id_dict.keys()

    @classmethod
    def shape_data(cls, pref_key: str, tags: list):
        """ 
        空白改行まみれの地域の文字列を整形, 辞書にまとめて返す
        {(pref_key, area_key): 地域名}
        """
        ret = {}
        area_re = re.compile(r'.+')
        del_space_re = re.compile(r'\s')
        for option_tag in tags:
            exist_value = option_tag.get("value")
            if not exist_value:
                continue
            area_txt = area_re.search(option_tag.text).group()
            area_txt = del_space_re.sub("", area_txt)
            ret[pref_key, exist_value] = area_txt
        return ret

    @classmethod
    def scrape_area_keys(cls, key: str) -> dict:
        """
        県ごとのkeyを受け取って県と地域のkey、地域名の辞書を返す
        """
        if type(key) != str:
            raise TypeError("key must be str object")
        if not cls.check_pref_dict_key(key):
            print("Error:invalid key")
            return {}
        url = cls.url_from_format(cls.pref_url_format, **{"pref": key})
        area_option_tags = cls.scrape_data(url, cls.area_option_selecter)
        area_options = cls.shape_data(key, area_option_tags)
        return area_options


class SBgetShopURLs(ScrapingSeleBase):
    """
    areaで取得した各地域のidから生成されたURLを受け取り、
    該当する店舗たちのURLを取得する
    """
    # ソフトバンク 東京都北区
    # https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131172&cid=tpsk_191119_mobile
    area_url_format = "https://www.softbank.jp/shop/search/list/?spadv=on&pref={0[pref]}&area={0[area]}&cid=tpsk_191119_mobile"
    shop_link_selector = "#js-shop-list > ul > li > div.shop-page-u96-shop-list-item_headder > h3 > a"

    # test_args = {
    #     "tokyo-kita": {
    #         "pref": 13,
    #         "area": 131172,
    #     },
    # }
    # test_area_url = ScrapingBase.url_from_format(area_url_format,
    #                                              **test_args["tokyo-kita"])

    @classmethod
    def debug_check_st_var(cls):
        """ 生成した各パラメータ確認用 """
        print(cls.area_url)
        print(cls.shop_link_selector)

    @classmethod
    def gene_area_url(cls, pref_key: str, area_key: str):
        dic = {"pref": pref_key, "area": area_key}
        return cls.url_from_format(cls.area_url_format, **dic)

    @classmethod
    def scrape_shop_urls(cls, url: str) -> list:
        """
        areaのurlから店舗のurlのリストを返す
        """
        # shop_links_a = cls.scrape_data(cls.test_area_url,cls.shop_link_selector)
        shop_links = []
        shop_link_tags = cls.scrape_data(url, cls.shop_link_selector)
        if shop_link_tags:
            base_url = "https://www.softbank.jp"
            shop_links = [
                base_url + link_tag.get("href") for link_tag in shop_link_tags
            ]
        return shop_links


class SBgetShopInfo(ScrapingBase):
    """
    shopURLで取得したURLから
    店舗名、住所、電話番号、設備などを取得

    name, organizer, phone_num, address, lecture, 
    price, site_url, has_parking, is_barrier_free 
    """
    base_table_sel = "#contents > div.bgWh > div > div > div.column-matchHeight > div > div:nth-child(1) > section > table > tbody"
    shop_selectors = {
        "name":
        base_table_sel + " > tr:nth-child(1) > td",
        "phone":
        base_table_sel + " > tr:nth-child(4) > td > span",
        "parking":
        base_table_sel + " > tr:nth-child(5) > td",
        "barrier_free":
        base_table_sel + " > tr:nth-child(6) > td",
        "address":
        "#contents > section.shop-page-u96-detail-section.bgWh > div > div.shop-page-u96-detail > div.shop-page-u96-detail-box-left > p",
    }

    @classmethod
    def scrape_shop_info(cls, url: str):
        """ 
        引数のurlのページに対してクラス変数のセレクターの辞書をループで回してスクレイピング、各種情報を取得
        """
        datas = {}
        for key, selector in cls.shop_selectors.items():
            tmp_data = cls.scrape_data(url, selector)

            # tagはbeautifulsoupのTagクラス
            tmp_data = tmp_data[0].string
            tmp_data = str(tmp_data).replace("　", " ")
            datas[key] = tmp_data
        return datas


dprint = print


class SBscraping(SBgetAreaURLs, SBgetShopURLs, SBgetShopInfo):
    """
    実際にスクレイピングを行うクラス
    sb_pref_ids: 県のIDのリスト

    sb_area_ids: {(県のID,地域のID) : 地域名}の辞書型

    sb_area_urls: sb_area_idsをもとに生成されたurlの辞書

    sb_shop_urls: area_urlから取得したshop_urlを格納する辞書

    sb_shop_datas: shop_urlから取得した各種情報を格納する辞書
        {店名：{
            店名：
            電話番号：
            住所：
            駐車場：
            バリアフリー：
        }}
    """
    sb_pref_ids = ["{:02}".format(i) for i in range(1, 48)]

    sb_area_ids = {}

    sb_area_urls = {}

    sb_shop_urls = {}

    sb_shop_datas = {}

    @classmethod
    def show_sb_area_ids(cls):
        return cls.sb_area_ids

    @classmethod
    def show_sb_area_urls(cls):
        return cls.sb_area_urls

    @classmethod
    def show_sb_shop_urls(cls):
        return cls.sb_shop_urls

    @classmethod
    def show_sb_shop_datas(cls):
        return cls.sb_shop_datas

    @classmethod
    def get_area_ids_by_pref(cls, pref_key: str) -> None:
        """ 
        sb_area_idsをpref_keyごとに取得、更新する関数
        """
        if cls.check_pref_dict_key(pref_key):
            cls.sb_area_ids[
                pref_key, SBgetAreaURLs.
                pref_id_dict[pref_key]] = SBgetAreaURLs.scrape_area_keys(
                    pref_key)
        else:
            KeyError("Error: invalid keys by get_area_ids_by_pref")

    @classmethod
    def get_area_ids(cls, debug=False) -> None:
        """
        複数の県に対してget_area_ids_by_prefを回してsb_area_idsを
        取得、更新する関数
        """
        if debug:
            # 東京都、神奈川県に設定
            cls.sb_pref_ids = ['13', '14']
        for pref_key in cls.sb_pref_ids:
            cls.get_area_ids_by_pref(pref_key)
            time.sleep(30)

    @classmethod
    def get_area_urls(cls, debug=False) -> None:
        """
        sb_area_idsから全国のarea_urlを取得し、sb_area_urlsに格納
        """
        if debug:
            tmp = {
                ('13', '東京都'): {
                    ('13', '131016'): '千代田区（4）',
                    ('13', '131024'): '中央区（5）',
                    ('13', '131032'): '港区（7）',
                    ('13', '131041'): '新宿区（9）',
                    ('13', '131059'): '文京区（2）',
                    ('13', '131067'): '台東区（4）',
                    ('13', '131075'): '墨田区（4）',
                    ('13', '131083'): '江東区（9）',
                    ('13', '131091'): '品川区（10 ）',
                    ('13', '131105'): '目黒区（5）',
                    ('13', '131113'): '大田区（11）',
                    ('13', '131121'): '世田谷区（15）',
                    ('13', '131130'): '渋谷区（6）',
                    ('13', '131148'): '中野区（4）',
                    ('13', '131156'): '杉並区（7）',
                    ('13', '131164'): '豊島区（8）',
                    ('13', '131172'): '北区（4）',
                    ('13', '131181'): '荒川区（4）',
                    ('13', '131199'): '板橋区（7）',
                    ('13', '131202'): '練馬区（9）',
                    ('13', '131211'): '足立区（8）',
                    ('13', '131229'): '葛飾区（5）',
                    ('13', '131237'): '江戸川区（8）',
                    ('13', '132012'): '八王子市（9）',
                    ('13', '132021'): '立川市（3）',
                    ('13', '132039'): '武蔵野市（4）',
                    ('13', '132047'): '三鷹市（1）',
                    ('13', '132055'): '青梅市（1）',
                    ('13', '132063'): '府中市（2）',
                    ('13', '132071'): '昭島市（1）',
                    ('13', '132080'): '調布市（4）',
                    ('13', '132098'): '町田市（8）',
                    ('13', '132101'): '小金井市（1）',
                    ('13', '132110'): '小平市（3）',
                    ('13', '132128'): '日野市（3）',
                    ('13', '132136'): '東村山市（3）',
                    ('13', '132144'): '国分寺市（3）',
                    ('13', '132152'): '国立市（2）',
                    ('13', '132187'): '福生市（1）',
                    ('13', '132195'): '狛江市（1）',
                    ('13', '132209'): '東大和市（1）',
                    ('13', '132217'): '清 瀬市（1）',
                    ('13', '132225'): '東久留米市（2）',
                    ('13', '132233'): '武蔵村山市（1）',
                    ('13', '132241'): '多摩市（3）',
                    ('13', '132250'): '稲城市（2）',
                    ('13', '132276'): '羽村市（2）',
                    ('13', '132284'): 'あきる野市（0）',
                    ('13', '132292'): '西東京市（3）',
                    ('13', '133035'): '西多摩郡瑞穂町（1）',
                    ('13', '133051'): '西多摩郡日の出町（1）',
                    ('13', '133078'): '西多摩郡檜原村（0）',
                    ('13', '133086'): '西多摩郡奥多摩町（0）',
                    ('13', '133612'): '大島町（0）',
                    ('13', '133621'): '利島村（0）',
                    ('13', '133639'): '新島村（0）',
                    ('13', '133647'): '神津島村（0）',
                    ('13', '133817'): '三宅村（0）',
                    ('13', '133825'): '御蔵島村（0）',
                    ('13', '134015'): '八丈町（0）',
                    ('13', '134023'): '青ヶ島村（0）',
                    ('13', '134210'): '小笠原村（0）'
                }
            }
            cls.sb_area_ids = tmp
        for key, area_ids_by_pref in cls.sb_area_ids.items():
            tmp = {}
            for area_id_tuple in area_ids_by_pref.keys():
                pref_id, area_id = area_id_tuple
                tmp[area_id_tuple] = SBgetShopURLs.gene_area_url(
                    pref_id, area_id)
            cls.sb_area_urls[key] = tmp

    @classmethod
    def get_shop_datas_by_area(cls):
        """
        sb_area_urlからshopのデータをsb_shop_datasに格納
        """
        for area_url in cls.sb_area_urls:
            shop_urls = SBgetShopURLs.scrape_shop_urls(area_url)
            for shop_url in shop_urls:
                datas = SBgetShopInfo.scrape_shop_info(shop_url)
                cls.sb_shop_datas[datas["name"]] = datas
