import re
import os
import pickle

from administer_data import models
from administer_data.scraping.softbank.sb_scrape_class_info import SBscraping as sb
# from administer_data.scraping.data import softbank_data as sb_data


class BaseDataRecoder():

    default_src_file = "test_base"

    @classmethod
    def save_data_to_pkl_file(cls, data, file_path):
        with open(
                os.path.join("./administer_data/scraping/data/",
                             file_path + ".pkl"), 'wb') as f:
            pickle.dump(data, f)

    @classmethod
    def load_data_from_pkl_file(cls, file_path):
        with open(
                os.path.join('./administer_data/scraping/data/',
                             file_path + ".pkl"), 'rb') as f:
            data_pkl = pickle.load(f)
        return data_pkl

    @classmethod
    def save_fixed_data_to_model(cls, src_file=default_src_file):
        """ 
        pklファイルに保存されたデータからインスタンスを作成しモデルに保存する関数
        scrapingする関数の呼び出しや情報のUPDATEとかもできたらいいなと思っている
        """
        data = cls.load_data_from_pkl_file(file_path=src_file)
        # 任意の処理

    # def dict_to_pkl_file():
    #     # print(sb_data.data)

    #     sb.save_data_file_pkl(sb_data.data, "softbank-2022_11_26_14_50_49")
    #     # sb.save_data_file_pkl(sb_data.data, "softbank_test")

    @classmethod
    def fix_data(cls, src_file=default_src_file):
        data = cls.load_data_from_pkl_file(src_file)
        # print(data)
        for key, info_xs in data.items():
            # 任意の処理
            pass

        # print(data)
        cls.save_data_to_pkl_file(data, file_path=src_file + "_fixed")
