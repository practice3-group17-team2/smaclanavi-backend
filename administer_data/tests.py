from django.test import TestCase

from .savedata import save_data
from .scraping.scraping import ScrapingBase, ScrapingSeleBase
from .scraping.sb_scraping import SBgetAreaURLs, SBgetShopURLs, SBgetShopInfo

# Create your tests here.

# class ScrapingTest(TestCase):
#     def test_save_data(self):
#         save_data()


""" 
manage.py test administer_data.tests.TestSB
"""
class TestSB(TestCase):

    

    def test_scrape_shops(self):
        """ 
        エリアから店舗を取得して、そこから各店舗の情報取得
        """
        datas = {}
        base_url = "https://www.softbank.jp"
        url = "https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131172&cid=tpsk_191119_mobile"
        shop_url_xs = SBgetShopURLs.scrape_shop_urls(url)
        print(shop_url_xs, "\n" * 3)

        for shop_url in shop_url_xs:
            data = SBgetShopInfo.scrape_info(shop_url)
            datas[data["name"]] = data
        print(datas)


"""
manage.py test administer_data.tests.TestURLNeedSele
"""
class TestURLNeedSele(TestCase):
    """ 
    urlとセレクターを使ってseleniumなしで
    スクレイピングできるか試すクラス 
    """
    urls = {
        "softbank": {
            "area_urls": "https://www.softbank.jp/shop/search/list/?pref=13",
            "shop_urls": "https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131172&cid=tpsk_191119_mobile",
            "shop_infos": "",
        },
        "docomo": {},
        "au": {}
    }

    url = urls["softbank"]["area_urls"]

    selectors = {
        "softbank": {
            "area_urls": "#contents > section > div > div.shop-page-u96-loaded-contents.is-loaded > div.shop-page-u96-shop-search-container > div.shop-page-u96-shop-search-pulldown > div:nth-child(2) > select > option",
            "shop_urls": "#js-shop-list > ul > li > div.shop-page-u96-shop-list-item_headder > h3 > a",
            "shop_infos": "",
        },
        "docomo": {},
        "au": {}
    }

    selector = selectors["softbank"]["area_urls"]

    # manage.py test administer_data.tests.TestURLNeedSele.test_isneed_selenium
    def test_isneed_selenium(self):
        """ 
        こいつがassertion出さないならseleniumの必要はない
        """
        result = ScrapingBase.scrape_data(self.url, self.selector)
        print("Test debug print:", result)
        self.assertNotEqual(result, [])
        return result

    # manage.py test administer_data.tests.TestURLNeedSele.test_selenium
    """ def test_selenium(self):
        result = ScrapingSeleBase.scrape_data(self.url, self.selector)
        print("Test debug print:", result)
        self.assertNotEqual(result, [])
        return result

    def compare_bs4_sele(self):
        tmp1 = ScrapingBase.scrape_data(self.url, self.selector)
        tmp2 = ScrapingSeleBase.scrape_data(self.url, self.selector)
        self.assertEqual(tmp1, tmp2) """


class TestSBgetShopInfo(TestCase):
    def test_scrape_shop_info(self):
        """ 
        店舗単体の情報取得
        """
        # 赤羽店
        url = "https://www.softbank.jp/shop/search/detail/TD20/"
        data = SBgetShopInfo.scrape_info(url)
        print(data)


"""
manage.py test administer_data.tests.TestSBgetShopURLs
"""
class TestSBgetShopURLs(TestCase):
    def test_scrape_shop_urls(self):
        # 東京都北区のURL
        url = "https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131172&cid=tpsk_191119_mobile"
        # 想定した答え
        ls = [
            '/shop/search/detail/TD43/?cid=tpsk_191119_mobile',
            '/shop/search/detail/TD20/?cid=tpsk_191119_mobile'
        ]
        result = SBgetShopURLs.scrape_shop_urls(url)
        print(result)
        # 結果
        # ['/shop/search/detail/TD43/?cid=tpsk_191119_mobile',
        # '/shop/search/detail/TD20/?cid=tpsk_191119_mobile']
        self.assertEqual(result, ls)


"""
manage.py test administer_data.tests.TestSBgetAreaURLs
"""
class TestSBgetAreaURLs(TestCase):
    url = "https://www.softbank.jp/shop/search/list/?pref=13"
    def test_scrape_area_urls(self):
        result = SBgetAreaURLs.scrape_area_urls(self.url)
        print(result)
