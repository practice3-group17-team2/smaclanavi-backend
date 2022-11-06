import re
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
    def is_in_pref_dict(cls, key:str) -> bool:
        """
        keyはstr型、二桁じゃないとだめ、"01"~"47"
        """
        if not 0 < int(key) < 48:
            return False
        return key in cls.pref_id_dict.keys()
    
    @classmethod
    def shape_data(cls, tags:list):
        """ 
        空白改行まみれの地域の文字列を整形, 辞書にまとめて返す
        key = tag.get("value")
        value = tag.text
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
            ret[exist_value] = area_txt
        return ret


    @classmethod
    def scrape_area_urls(cls, url):
        # if not cls.is_in_pref_dict(key):
        #     print("Error:invalid key")
        #     return []
        area_option_tags = cls.scrape_data(url, cls.area_option_selecter)
        area_options = cls.shape_data(area_option_tags)
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

    test_args = {
        "tokyo-kita": {
            "pref": 13,
            "area": 131172,
        },
    }
    test_area_url = ScrapingBase.url_from_format(area_url_format,
                                                 **test_args["tokyo-kita"])

    @classmethod
    def debug_check_st_var(cls):
        """ 生成した各パラメータ確認用 """
        print(cls.area_url)
        print(cls.shop_link_selector)

    @classmethod
    def scrape_shop_urls(cls, url) -> list:
        """ 店舗のurlのリストを返す """
        # shop_links_a = cls.scrape_data(cls.test_area_url,cls.shop_link_selector)
        shop_link_tags = cls.scrape_data(url, cls.shop_link_selector)
        base_url = "https://www.softbank.jp"
        shop_links = [base_url+link_tag.get("href") for link_tag in shop_link_tags]
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
    def scrape_info(cls, url):
        """ 
        クラス変数のセレクターの辞書をループ回してスクレイピング、各種情報を取得
        """
        datas = {}
        for key, selector in cls.shop_selectors.items():
            tmp_data = cls.scrape_data(url, selector)

            # tagはbeautifulsoupのTagクラス
            tmp_data = tmp_data[0].string
            tmp_data = str(tmp_data).replace("　", " ")
            datas[key] = tmp_data
        return datas
