from django.test import TestCase

from ..scraping.savedata_old import save_data
from ..scraping.scraping import ScrapingBase, ScrapingSeleBase
from ..scraping.sb_scraping import SBgetAreaURLs, SBgetShopURLs, SBgetShopInfo
from ..scraping.sb_scraping import SBscraping

import json, os, pickle

# Create your tests here.

# class ScrapingTest(TestCase):
#     def test_save_data(self):
#         save_data()


class TestSB(TestCase):
    """ 
    manage.py test administer_data.tests.TestSB
    """
    pref_key = "13"

    def test_get_area_ids_by_pref(self):
        expected_dic = {
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
        SBscraping.get_area_ids_by_pref(self.key)
        result = SBscraping.show_sb_area_ids()
        print(result)
        # self.assertEqual(result, expected_dic)

    def test_get_area_ids(self):
        SBscraping.get_area_ids(debug=True)
        result = SBscraping.show_sb_area_ids()
        print(result)
        result = {
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
            },
            ('14', '神奈川県'): {
                ('14', '141011'): '横浜市鶴見区（2）',
                ('14', '141020'): '横浜市神奈川区（2）',
                ('14', '141038'): '横浜市西区（5）',
                ('14', '141046'): '横浜市中区（3）',
                ('14', '141054'): '横浜市南区（0）',
                ('14', '141062'): '横浜市保土ケ谷区（1）',
                ('14', '141071'): '横浜市磯子区（2）',
                ('14', '141089'): '横浜市金沢区（3）',
                ('14', '141097'): '横浜市港北区（6 ）',
                ('14', '141101'): '横浜市戸塚区（3）',
                ('14', '141119'): '横浜市港南区（3）',
                ('14', '141127'): '横浜市旭区（3）',
                ('14', '141135'): '横浜市緑区（2）',
                ('14', '141143'): '横浜市瀬谷区（1）',
                ('14', '141151'): '横浜市栄区（0）',
                ('14', '141160'): '横浜市泉区（1）',
                ('14', '141178'): '横浜市青葉区（4）',
                ('14', '141186'): '横浜市都筑区（5）',
                ('14', '141313'): '川崎市川崎区（3）',
                ('14', '141321'): '川崎市幸区（2）',
                ('14', '141330'): '川崎市中原区（4）',
                ('14', '141348'): '川崎市高津区（2）',
                ('14', '141356'): '川崎市多摩区（3）',
                ('14', '141364'): '川崎市宮前区（2）',
                ('14', '141372'): '川崎市麻生区（1）',
                ('14', '141518'): '相模原市緑区（4）',
                ('14', '141526'): '相模原市中央区（5）',
                ('14', '141534'): '相模原市南区（2）',
                ('14', '142018'): '横須賀市（5）',
                ('14', '142034'): '平塚市（4）',
                ('14', '142042'): '鎌倉市（2）',
                ('14', '142051'): '藤沢市（6）',
                ('14', '142069'): '小田原市（4）',
                ('14', '142077'): '茅ヶ崎市（2）',
                ('14', '142085'): '逗子市（1）',
                ('14', '142107'): '三浦市（0）',
                ('14', '142115'): '秦野市（1）',
                ('14', '142123'): '厚木市（4）',
                ('14', '142131'): '大和市（4）',
                ('14', '142140'): '伊勢原市（2）',
                ('14', '142158'): '海老名市（2）',
                ('14', '142166'): '座間市（2）',
                ('14', '142174'): '南足柄市（0）',
                ('14', '142182'): '綾瀬市（1）',
                ('14', '143014'): '三浦郡葉山町（0）',
                ('14', '143219'): '高座郡寒川町（1）',
                ('14', '143413'): '中郡大磯町（0）',
                ('14', '143421'): ' 中郡二宮町（0）',
                ('14', '143618'): '足柄上郡中井町（0）',
                ('14', '143626'): '足柄上郡大井町（1）',
                ('14', '143634'): '足柄上郡松田町（0）',
                ('14', '143642'): '足柄上郡山北町（0）',
                ('14', '143669'): '足柄上郡開成町（0）',
                ('14', '143821'): '足柄下郡箱根町（0）',
                ('14', '143839'): '足柄下郡真鶴町（0）',
                ('14', '143847'): '足柄下郡湯河原町（0）',
                ('14', '144011'): '愛甲郡愛川町（1）',
                ('14', '144029'): '愛甲郡清川村（0）'
            }
        }

    def test_get_area_urls(self):
        SBscraping.get_area_urls(debug=True)
        result = SBscraping.show_sb_area_urls()
        print(result)
        """ 
        {('13', '東京都'): {
            ('13', '131016'): 'https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131016&cid=tpsk_191119_mobile', 
            ('13', '131024'): 'https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131024&cid=tpsk_191119_mobile', 
            ('13', '131032'): 'https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131032&cid=tpsk_191119_mobile', 
            ('13', '131041'): 'https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131041&cid=tpsk_191119_mobile', 
        }}"""

    def test_get_shop_urls(self):
        expected_dic = {
            ('13', '東京都'): {
                (('13', '131016'), '千代田区（4）'): [],
                (('13', '131024'), '中央区（5）'): [
                    'https://www.softbank.jp/shop/search/detail/TD31/?cid=tpsk_191119_mobile'
                ]
            },
            ('14', '神奈川県'): {
                (('14', '141011'), '横浜市鶴見区（2）'): [
                    'https://www.softbank.jp/shop/search/detail/T216/?cid=tpsk_191119_mobile'
                ],
                (('14', '141020'), '横浜市神奈川区（2）'): []
            }
        }
        SBscraping.get_shop_urls(debug=True)
        result = SBscraping.show_sb_shop_urls()
        print(result)

    def test_get_shop_infos_by_area(self):
        key = (('14', '141011'), '横浜市鶴見区（2）')
        value_ls = [
            'https://www.softbank.jp/shop/search/detail/T216/?cid=tpsk_191119_mobile'
        ]
        expected_dic = {
            (('14', '141011'), '横浜市鶴見区（2）'): {
                'ソフトバンク鶴見': {
                    'class_name': 'ソフトバンク鶴見',
                    'phone_number': '045-505-0500',
                    'has_parking': 'None',
                    'is_barrier_free': '○',
                    'address': '神奈川県横浜市鶴見区鶴見中央４丁目１５‐７'
                }
            }
        }

        SBscraping.get_shop_infos_by_area(key, value_ls)
        result = SBscraping.show_sb_shop_infos()
        print(result)

    def test_get_shop_infos(self):
        expected_dic = {
            (('13', '131016'), '千代田区（4）'): {},
            (('13', '131024'), '中央区（5）'): {
                'ソフトバンク銀座': {
                    'class_name': 'ソフトバンク銀座',
                    'phone_number': '03-6252-3333',
                    'has_parking': 'None',
                    'is_barrier_free': '－',
                    'address': '東京都中央区銀座５丁目７番８号'
                }
            },
            (('14', '141011'), '横浜市鶴見区（2）'): {
                'ソフトバンク鶴見': {
                    'class_name': 'ソフトバンク鶴見',
                    'phone_number': '045-505-0500',
                    'has_parking': 'None',
                    'is_barrier_free': '○',
                    'address': '神奈川県横浜市鶴見区鶴見中央４丁目１５‐７'
                }
            },
            (('14', '141020'), '横浜市神奈川区（2）'): {}
        }
        SBscraping.get_shop_infos(debug=True)
        result = SBscraping.show_sb_shop_infos()
        print(result)
        self.assertEqual(result, expected_dic)

    def test_get_shop_info_from_url(self):
        expected_dic = {
            'class_name': 'ソフトバンク神楽坂',
            'phone_number': '03-5229-7150',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都新宿区神楽坂６丁目４７ 照井ビル１Ｆ'
        }
        url = "https://www.softbank.jp/shop/search/detail/T1G0/"
        result = SBgetShopInfo.scrape_shop_info(url)
        print(result)
        self.assertEqual(result, expected_dic)

    def test_softbank_scrape(self):
        """ 
        softbankの店舗情報の取得、一番規模大きい結合テストに相当？
        """
        sb = SBscraping()

        #東京都のみで実行
        sb.get_area_ids(debug=True)
        # print(SBscraping.show_sb_area_ids())

        sb.get_area_urls()
        # print(SBscraping.show_sb_area_urls())

        sb.get_shop_urls()
        # print(SBscraping.show_sb_shop_urls())

        sb.get_shop_infos()
        result = sb.show_sb_shop_infos()

        sb.quit_driver()

        print(result)

    def test_save_load_by_pkl(self):
        dic = {
            (('13', '131016'), '千代田区（4）'): {},
            (('13', '131024'), '中央区（5）'): {
                'ソフトバンク銀座': {
                    'class_name': 'ソフトバンク銀座',
                    'phone_number': '03-6252-3333',
                    'has_parking': 'None',
                    'is_barrier_free': '－',
                    'address': '東京都中央区銀座５丁目７番８号'
                }
            },
            (('14', '141011'), '横浜市鶴見区（2）'): {
                'ソフトバンク鶴見': {
                    'class_name': 'ソフトバンク鶴見',
                    'phone_number': '045-505-0500',
                    'has_parking': 'None',
                    'is_barrier_free': '○',
                    'address': '神奈川県横浜市鶴見区鶴見中央４丁目１５‐７'
                }
            },
            (('14', '141020'), '横浜市神奈川区（2）'): {}
        }

        # with open("./administer_data/data/softbank.pkl", 'wb') as f:
        #         pickle.dump(dic, f)
        SBscraping.save_data_file_pkl(dic)

        # with open('./administer_data/data/softbank.pkl', 'rb') as f:
        #     dict_pkl = pickle.load(f)
        load_dic = SBscraping.load_data_file_pkl()

        self.assertEqual(dic, load_dic)
        for i in load_dic.items():
            print(i)


class TestURLNeedSele(TestCase):
    """ 
    manage.py test administer_data.tests.TestURLNeedSele
    urlとセレクターを使ってseleniumなしで
    スクレイピングできるか試すクラス 
    """
    urls = {
        "softbank": {
            "area_urls": "https://www.softbank.jp/shop/search/list/?pref=13",
            "shop_urls":
            "https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131172&cid=tpsk_191119_mobile",
            "shop_infos": "",
        },
        "docomo": {},
        "au": {}
    }

    url = urls["softbank"]["area_urls"]

    selectors = {
        "softbank": {
            "area_urls":
            "#contents > section > div > div.shop-page-u96-loaded-contents.is-loaded > div.shop-page-u96-shop-search-container > div.shop-page-u96-shop-search-pulldown > div:nth-child(2) > select > option",
            "shop_urls":
            "#js-shop-list > ul > li > div.shop-page-u96-shop-list-item_headder > h3 > a",
            "shop_infos": "",
        },
        "docomo": {},
        "au": {}
    }

    selector = selectors["softbank"]["area_urls"]

    def test_isneed_selenium(self):
        """ 
        manage.py test administer_data.tests.TestURLNeedSele.test_isneed_selenium
        こいつがassertion出さないならseleniumの必要はない
        """
        result = ScrapingBase.scrape_data(self.url, self.selector)
        print("Test debug print:", result)
        self.assertNotEqual(result, [])
        return result

    def test_selenium(self):
        """
        manage.py test administer_data.tests.TestURLNeedSele.test_selenium
        """
        result = ScrapingSeleBase.scrape_data(self.url, self.selector)
        ScrapingSeleBase.quit_driver()
        print("Test debug print:", result)
        self.assertNotEqual(result, [])
        return result

    # def compare_bs4_sele(self):
    #     tmp1 = ScrapingBase.scrape_data(self.url, self.selector)
    #     tmp2 = ScrapingSeleBase.scrape_data(self.url, self.selector)
    #     ScrapingSeleBase.quit_driver()
    #     self.assertEqual(tmp1, tmp2)


class TestSBgetAreaURLs(TestCase):
    """
    manage.py test administer_data.tests.TestSBgetAreaURLs
    """
    # url = "https://www.softbank.jp/shop/search/list/?pref=13"
    key = '13'

    def test_scrape_area_urls(self):
        expected_dic = {
            ('13', '131016'): '千代田区（4）',
            ('13', '131024'): '中央区（5）',
            ('13', '131032'): '港区（7）',
            ('13', '131041'): '新宿区（9）',
            ('13', '131059'): '文京 区（2）',
            ('13', '131067'): '台東区（4）',
            ('13', '131075'): '墨田区（4）',
            ('13', '131083'): '江東区（9）',
            ('13', '131091'): '品川区（10）',
            ('13', '131105'): '目黒区（5）',
            ('13', '131113'): '大田区（11）',
            ('13', '131121'): '世田谷区（15）',
            ('13', '131130'): '渋谷区（6）',
            ('13', '131148'): '中野区（4）',
            ('13', '131156'): '杉並区（7）',
            ('13', '131164'): '豊島区（8）',
            ('13', '131172'): '北区（4）',
            ('13', '131181'): '荒川区（4）',
            ('13', '131199'): '板橋区（7 ）',
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
            ('13', '132101'): '小金井市（1 ）',
            ('13', '132110'): '小平市（3）',
            ('13', '132128'): '日野市（3）',
            ('13', '132136'): '東村山市（3）',
            ('13', '132144'): '国分寺市（3）',
            ('13', '132152'): '国立市（2）',
            ('13', '132187'): '福生市（1）',
            ('13', '132195'): '狛江市（1）',
            ('13', '132209'): '東大和市（1）',
            ('13', '132217'): '清瀬市（1）',
            ('13', '132225'): '東久留米市（2）',
            ('13', '132233'): '武蔵村山市（1）',
            ('13', '132241'): '多摩市（3）',
            ('13', '132250'): '稲城市（2）',
            ('13', '132276'): '羽村市（2）',
            ('13', '132284'): 'あきる野市（0）',
            ('13', '132292'): '西東京市（3）',
            ('13', '133035'): '西多摩郡瑞穂町（1）',
            ('13', '133051'): '西多摩郡日の出 町（1）',
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

        # result = SBgetAreaURLs.scrape_area_keys(self.url)
        result = SBgetAreaURLs.scrape_area_keys(self.key)
        print(result)
        # self.assertEqual(result, expected_dic)


class TestSBgetShopURLs(TestCase):
    """
    manage.py test administer_data.tests.TestSBgetShopURLs
    """

    def test_scrape_shop_urls(self):
        # 東京都北区のURL
        url = "https://www.softbank.jp/shop/search/list/?spadv=on&pref=13&area=131172&cid=tpsk_191119_mobile"
        expected_ls = [
            '/shop/search/detail/TD43/?cid=tpsk_191119_mobile',
            '/shop/search/detail/TD20/?cid=tpsk_191119_mobile'
        ]
        result = SBgetShopURLs.scrape_shop_urls(url)
        print(result)
        # 結果
        # ['/shop/search/detail/TD43/?cid=tpsk_191119_mobile',
        # '/shop/search/detail/TD20/?cid=tpsk_191119_mobile']
        self.assertEqual(result, expected_ls)


class TestSBgetShopInfo(TestCase):

    def test_scrape_shop_info(self):
        """ 
        店舗単体の情報取得
        """
        # 赤羽店
        url = "https://www.softbank.jp/shop/search/detail/TD20/"
        data = SBgetShopInfo.scrape_shop_info(url)
        print(data)
