from django.test import TestCase

from .savedata import save_data
from .scraping import SBgetShopURLs as sss
from .scraping import ScrapingSeleBase as ssb
from .scraping import IsNeedSele
from .scraping import SBgetShopInfo
from .scraping import SBgetShopURLs

# Create your tests here.

# class ScrapingTest(TestCase):
#     def test_save_data(self):
#         save_data()

class TestDefault(TestCase):
    def test_scrape_shop_info(self):
        """ 
        店舗単体の情報取得
        """
        # 赤羽店
        url = "https://www.softbank.jp/shop/search/detail/TD20/"
        data = SBgetShopInfo.scraping_info(url)
        print(data)

    def test_scrape_shops(self):
        """ 
        エリアから店舗を取得して、そこから各店舗の情報取得
        """
        datas = {}
        base_url = "https://www.softbank.jp"
        url = "https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131172&cid=tpsk_191119_mobile"
        shop_url_xs= SBgetShopURLs.scraping_shop_urls(url)
        print(shop_url_xs,"\n"*3)

        for shop_url in shop_url_xs:
            shop_url = base_url+shop_url
            data = SBgetShopInfo.scraping_info(shop_url)
            datas[data["name"]] = data
        print(datas)




class TestIsNeedSele(TestCase):
    """ 
    urlとセレクターを使ってseleniumなしで
    スクレイピングできるか試すクラス 
    """
    url  = "https://www.softbank.jp/shop/search/detail/TD20/"
    # selecter = ""
    selecter = "#contents > div.bgWh > div > div > div.column-matchHeight > div > div:nth-child(1) > section > table > tbody > tr:nth-child(1) > td"
    def test_isneed_selenium(self):
        result = IsNeedSele.test(self.url, self.selecter)
        print(result)
        self.assertNotEqual(result, [])

""" 
class URLTest(TestCase):
    # def test_check_st_var(self):
    #     sss.debug_check_st_var()

    def test_scraping_shop(self):
        url = "https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131172&cid=tpsk_191119_mobile"
        # 想定した答え
        ls = [
            '/shop/search/detail/TD43/?cid=tpsk_191119_mobile',
            '/shop/search/detail/TD20/?cid=tpsk_191119_mobile'
        ]
        result = sss.scraping_shop_urls(url)
        print(result)
        # 結果
        # ['/shop/search/detail/TD43/?cid=tpsk_191119_mobile',
        # '/shop/search/detail/TD20/?cid=tpsk_191119_mobile']
        self.assertEqual(result, ls)
 """


    
    # def test_scrape_data(self):
    #     print("aiueo", sss.scrape_data(sss.area_url, sss.shop_link_selecter))

    # def test_scraping_sele_crawling(self):
    #     ssb.crawling_data(sss.area_url)

    # def test_scraping_sele(self):
    #     print(ssb.scrape_data(sss.area_url, sss.shop_link_selecter))
   