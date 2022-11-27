# manage.py test administer_data.tests.test_savedata
from django.test import TestCase

import re
from administer_data.scraping.softbank import sb_savedata

# manage.py test administer_data.tests.test_savedata.TestSbSaveData
class TestSbSaveData(TestCase):
    file_name = "save_test_sb"
    file_name_fixed = file_name +"_fixed"


    # manage.py test administer_data.tests.test_savedata.TestSbSaveData.test_create_and_fix_data
    def _test_create_and_fix_data(self):
        sb_savedata.fix_data(self.file_name)

    def _test_save_data(self):
        sb_savedata.save_fixed_data_to_model(self.file_name_fixed)
    
    def reg(self):
        text = "横浜市鶴見区（2）"
        print(re.split(r'.+?市.+?区|.+?[市区町村]', text))

    def test_save_load_by_pkl(self):
        dic = {
            (('13', '131016'), '千代田区（4）'): {},
            (('13', '131024'), '中央区（5）'): {
                'ソフトバンク銀座': {
                    'class_name': 'ソフトバンク銀座',
                    'phone_number': '03-6252-3333',
                    'has_parking': 'None',
                    'is_barrier_free': '－',
                    'address': '東京都中央区銀座５丁目７番８号',
                    'site_url': 'https://www.softbank.jp/shop/search/detail/TD31/?cid=tpsk_191119_mobile'
                }
            },
            (('14', '141011'), '横浜市鶴見区（2）'): {
                'ソフトバンク鶴見': {
                    'class_name': 'ソフトバンク鶴見',
                    'phone_number': '045-505-0500',
                    'has_parking': 'None',
                    'is_barrier_free': '○',
                    'address': '神奈川県横浜市鶴見区鶴見中央４丁目１５‐７',
                    'site_url': 'https://www.softbank.jp/shop/search/detail/T216/?cid=tpsk_191119_mobile'
                }
            },
            (('14', '141020'), '横浜市神奈川区（2）'): {}
        }

        sb_savedata.save_data_to_pkl_file(dic, self.file_name)
        load_dic = sb_savedata.load_data_from_pkl_file(self.file_name)

        self.assertEqual(dic, load_dic)
        # for i in load_dic.items():
        #     print(i)