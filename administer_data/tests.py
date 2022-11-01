from django.test import TestCase

from .savedata import save_data
from .scraping import SoftbankShopScraping as sss
from .scraping import ScrapingSeleBase as ssb

# Create your tests here.

# class ScrapingTest(TestCase):
#     def test_save_data(self):
#         save_data()


class URLTest(TestCase):
    # def test_check_st_var(self):
    #     sss.check_st_var()

    def test_scraping_shop(self):
        # 想定した答え
        ls = [
            '/shop/search/detail/TD43/?cid=tpsk_191119_mobile',
            '/shop/search/detail/TD20/?cid=tpsk_191119_mobile'
        ]
        result = sss.scraping_shop()
        print(result)
        # 結果
        # ['/shop/search/detail/TD43/?cid=tpsk_191119_mobile',
        # '/shop/search/detail/TD20/?cid=tpsk_191119_mobile']
        self.assertEqual(result, ls)

    """ 
    def test_scrape_data(self):
        print("aiueo", sss.scrape_data(sss.area_url, sss.shop_link_selecter))

    def test_scraping_sele_crawling(self):
        ssb.crawling_data(sss.area_url)

    def test_scraping_sele(self):
        print(ssb.scrape_data(sss.area_url, sss.shop_link_selecter))
    """


# url = "https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131172&cid=tpsk_191119_mobile"
# selecter = "#js-shop-list > ul > li > div.shop-page-u96-shop-list-item_headder > h3 > a"
# selecter = "#js-shop-list > ul.shop-page-u96-shop-list"