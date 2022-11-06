import sys, bs4, requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_NUM = "100"


class ScrapingBase:
    TIMEOUT = 10
    HEADER = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
    }

    # HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
    #                           AppleWebKit/537.36 (KHTML, like Gecko)
    #                           Chrome/105.0.0.0 Safari/537.36'}
    @classmethod
    def url_from_format(cls, url_format: str, **kwargs) -> str:
        """url_format.format(**kwargs)をするだけの関数"""
        url = ""
        try:
            url = url_format.format(kwargs)
        except Exception as e:
            print("ERROR_FORMAT:{}".format(e))
        return url

    @classmethod
    def crawl_data(cls, url: str):
        #result = requests.get(url, timeout=TIMEOUT, headers=HEADER)
        result = requests.get(url, timeout=cls.TIMEOUT, headers=cls.HEADER)
        result.raise_for_status()
        return result

    @classmethod
    def scrape_data(cls, url: str, selector: str) -> list:
        """urlからselectorに該当する要素を抽出して返す関数"""
        ret = None
        try:
            result = cls.crawl_data(url)
        except Exception as e:
            print("ERROR_DOWNLOAD:{}".format(e))
        else:
            soup = bs4.BeautifulSoup(result.content, 'html.parser')
            ret = soup.select(selector)
        return ret


class ScrapingSeleBase(ScrapingBase):

    @classmethod
    def init_driver(cls):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)
        wait = WebDriverWait(driver=driver, timeout=300)
        return driver, wait
    
    @classmethod
    def quit_driver(cls, driver):
        driver.close()
        driver.quit()

    @classmethod
    def crawl_data(cls, url: str, selector: str):
        driver, wait = cls.init_driver()
        driver.get(url)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        result = driver.page_source.encode('utf-8')
        cls.quit_driver(driver)
        return result

    @classmethod
    def scrape_data(cls, url: str, selector: str) -> list:
        """urlからselectorに該当する要素を抽出して返す関数"""
        ret = None
        try:
            result = cls.crawl_data(url, selector)
        except Exception as e:
            print("ERROR_DOWNLOAD:{}".format(e))
        else:
            soup = bs4.BeautifulSoup(result, 'html.parser')
            ret = soup.select(selector)
        return ret



class SBgetAreaURLs(ScrapingBase):
    """
    検索する都道府県を指定して、絞り込み検索のところから各地域のURLのid部分を抽出
    {pref, area}の組を取得
    """
    pref_url_format = "https://www.softbank.jp/shop/search/list/?pref={0[pref]}"

    pref_dict = {
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
        return key in cls.pref_dict.keys

    @classmethod
    def scrape_area_urls(cls, url):
        pass

    


    


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
        shop_links_a = cls.scrape_data(url, cls.shop_link_selector)
        shop_links = [link_tag.get("href") for link_tag in shop_links_a]
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


#グーグル検索から検索結果のリストを返す関数
def search_google(words):
    sb = ScrapingBase
    """
    検索する言葉を受け取ってlink_list, title_listを返す
    """
    link_list = []
    title_list = []

    try:
        url = "https://www.google.co.jp/search?q=" + words + "&num=" + SEARCH_NUM + "&start=0"
        result = requests.get(url, timeout=sb.TIMEOUT, headers=sb.HEADER)

        result.raise_for_status()
    except Exception as e:
        print("ERROR_DOWNLOAD:{}".format(e))
    else:

        soup = bs4.BeautifulSoup(result.content, 'html.parser')
        # developer toolのelementsタブ 要素右クリから copy-> copy selector(beautiful soupはセレクターで動くので)
        links = soup.select(
            "#rso > div > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a")
        titles = soup.select(
            "#rso > div > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3")

        link_list = [link_tag.get("href") for link_tag in links]
        title_list = [title_tag.get_text() for title_tag in titles]

        #デバッグ用のprint
        #print("length {}, {}".format(len(link_list), len(title_list)))

        #タイトルとリンクが不一致の場合、
        if len(link_list) != len(title_list):
            return [], []

    return link_list, title_list


#"""
def main():

    words = input("検索ワードを入力してください")
    print(search_google(words))


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nprogram was ended.\n")
        sys.exit()
#"""
