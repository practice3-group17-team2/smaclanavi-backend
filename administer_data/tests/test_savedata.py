# python manage.py test administer_data.tests.test_savedata
import datetime
import re

from django.test import TestCase

from administer_data.scraping.softbank.sb_savedata import SoftBankClassDataRecorder
from administer_data.scraping.softbank.sb_savedata import SoftBankLecDataRecorder
from administer_data.scraping.softbank.sb_scrape_lec_info import SBLecInfoScraper


# python manage.py test administer_data.tests.test_savedata.TestSbSaveLecData
class TestSbSaveLecData(TestCase):
    file_name = "test_lec_save"

    def _make_pkl_file_from_dict_xs(self):
        # class_id = "TD20"
        # file_name = f"lec_{datetime.datetime.now().strftime('%y_%m_%d_%H_%M')}"
        file_name = self.file_name

        dict_xs = SBLecInfoScraper.get_overall_lec_info(debug=True)
        SBLecInfoScraper.quit_driver()
        SoftBankLecDataRecorder.save_data_to_pkl_file(dict_xs, file_name)

        loaded_file = SoftBankLecDataRecorder.load_data_from_pkl_file(file_name)
        self.assertEqual(loaded_file, dict_xs)

    def test_print_lec_pkl_file(self):
        # file_name = "lec_22_12_02_07_22"
        file_name = "test_lec_save_sb_all"
        loaded_file = SoftBankLecDataRecorder.load_data_from_pkl_file(file_name)
        # print(type(loaded_file[0]))  # <class 'dict'>
        print(*loaded_file.items(), sep="\n")  # 内容の表示

    def _test_fix_data(self):
        pass


# python manage.py test administer_data.tests.test_savedata.TestSbSaveClassData
class TestSbSaveClassData(TestCase):
    file_name = "test_cls_save"
    file_name_fixed = file_name + "_fixed"

    # python manage.py test administer_data.tests.test_savedata.TestSbSaveClassData.test_create_and_fix_data
    def _test_create_and_fix_data(self):
        SoftBankClassDataRecorder.fix_data(self.file_name)

    def test_save_data(self):
        SoftBankClassDataRecorder.save_fixed_data_to_model(self.file_name_fixed)

    def reg(self):
        text = "横浜市鶴見区（2）"
        print(re.split(r'.+?市.+?区|.+?[市区町村]', text))

    def _test_save_load_by_pkl(self):
        dic = {
            (('13', '131016'), '千代田区（4）'): {},
            (('13', '131024'), '中央区（5）'): {
                'ソフトバンク銀座': {
                    'class_name':
                    'ソフトバンク銀座',
                    'phone_number':
                    '03-6252-3333',
                    'has_parking':
                    'None',
                    'is_barrier_free':
                    '－',
                    'address':
                    '東京都中央区銀座５丁目７番８号',
                    'site_url':
                    'https://www.softbank.jp/shop/search/detail/TD31/?cid=tpsk_191119_mobile'
                }
            },
            (('14', '141011'), '横浜市鶴見区（2）'): {
                'ソフトバンク鶴見': {
                    'class_name':
                    'ソフトバンク鶴見',
                    'phone_number':
                    '045-505-0500',
                    'has_parking':
                    'None',
                    'is_barrier_free':
                    '○',
                    'address':
                    '神奈川県横浜市鶴見区鶴見中央４丁目１５‐７',
                    'site_url':
                    'https://www.softbank.jp/shop/search/detail/T216/?cid=tpsk_191119_mobile'
                }
            },
            (('14', '141020'), '横浜市神奈川区（2）'): {}
        }

        SoftBankClassDataRecorder.save_data_to_pkl_file(dic, self.file_name)
        load_dic = SoftBankClassDataRecorder.load_data_from_pkl_file(self.file_name)

        self.assertEqual(dic, load_dic)
