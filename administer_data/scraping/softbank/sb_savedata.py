import re
import os
import pickle

from administer_data import models
from administer_data.scraping.save_data import BaseDataRecoder
# from administer_data.scraping.data import softbank_data as sb_data


class SoftBankDataRecorder(BaseDataRecoder):
    """ save and load """

    @classmethod
    def save_data_to_pkl_file(cls, data, file_path):
        return super().save_data_to_pkl_file(data, "softbank/" + file_path)

    @classmethod
    def load_data_from_pkl_file(cls, file_path):
        return super().load_data_from_pkl_file("softbank/" + file_path)


class SoftBankClassDataRecorder(SoftBankDataRecorder):
    """ fix and save to model class data"""
    default_src_file = "test_cls_save"

    @classmethod
    def save_fixed_data_to_model(cls, src_file=default_src_file):
        """ 
        pklファイルに保存されたデータからインスタンスを作成しモデルに保存する関数
        scrapingする関数の呼び出しや情報のUPDATEとかもできたらいいなと思っている
        """
        data = cls.load_data_from_pkl_file(file_path=src_file)
        # area = (pref_id, area_id), area_name(店舗数))
        # class_info_xs = {
        # "店舗名": {
        #     'phone_number':
        #     'class_name':
        #     'has_parking':
        #     'is_barrier_free':
        #     'address':
        # }

        city_name_pattern = re.compile(r'[^0-9（）]+')

        org, _ = models.ClassOrganizer.objects.get_or_create(
            organizer_name="ソフトバンク")
        pref = models.Prefecture.objects.get(pref_name="東京都")

        for area, class_info_xs in data.items():
            if not class_info_xs:
                continue

            city_name = city_name_pattern.match(area[1]).group()
            city, _ = models.City.objects.get_or_create(city_name=city_name,
                                                        prefecture=pref)

            for class_info in class_info_xs.values():
                class_info = models.ClassInfo.objects.create(
                    city=city, class_organizer=org, **class_info)

        # print(models.City.objects.all())

    # def dict_to_pkl_file():
    #     # print(sb_data.data)

    #     sb.save_data_file_pkl(sb_data.data, "softbank-2022_11_26_14_50_49")
    #     # sb.save_data_file_pkl(sb_data.data, "softbank_test")

    @classmethod
    def fix_data(cls, src_file=default_src_file):
        data = cls.load_data_from_pkl_file(src_file)
        # print(data)
        for area, class_info_xs in data.items():
            for class_info in class_info_xs.values():
                if class_info["has_parking"] in ["None", "－"]:
                    class_info["has_parking"] = False
                else:
                    class_info["has_parking"] = True

                if class_info["is_barrier_free"] == "－":
                    class_info["is_barrier_free"] = False
                else:
                    class_info["is_barrier_free"] = True

        # print(data)
        cls.save_data_to_pkl_file(data, file_path=src_file + "_fixed")


class SoftBankLecDataRecorder(SoftBankDataRecorder):
    # default_src_file = "test_lec_save"

    @classmethod
    def create_lecture_instance(cls):
        """ 講義の保存のためにタグ付け的な役割のものを作成しないといけない """
        ls = ["スマホ 体験編", "画面の見方", "マップ＆カメラ", "ネット＆アプリ", "より快適な設定", "アプリを使ってみよう", "タブレット"]

        for txt in ls:
            models.Lecture.objects.get_or_create(lecture_content=txt,
                                                 is_target_old=False)

    @classmethod
    def save_fixed_data_to_model(cls, src_file) -> None:
        """
        fixedかどうかはわからん
        """
        n_classes_data = cls.load_data_from_pkl_file(src_file)
        # word_xs = ["画面"]
        # unit_type_xs = ["iPhone", "Android", "タブレット"]
        # print(n_classes_data)

        for classinfo_id, lec_data_xs in n_classes_data.items():
            for data in lec_data_xs:
                # lec_titleについてmodels.Lectureの検索語彙を変えるために分岐
                if re.search("触ってみよう", data["lec_title"]):
                    txt = "体験編"
                elif re.search("画面", data["lec_title"]):
                    txt = "画面"
                elif re.search("マップ", data["lec_title"]):
                    txt = "マップ"
                elif re.search("ネット", data["lec_title"]):
                    txt = "ネット"
                elif re.search("設定", data["lec_title"]):
                    txt = "設定"
                elif re.match("アプリ", data["lec_title"]):
                    txt = "アプリを使ってみよう"
                elif re.search("タブレット", data["lec_title"]):
                    txt = "タブレット"
                else:
                    print("以下の講義の検索キーワードは無効です")
                    print(f"{classinfo_id}:\n {data}\n---\n")
                    continue

                created_lec = models.Lecture.objects.get(
                    lecture_content__contains=txt)
                held_class = models.ClassInfo.objects.get(id=classinfo_id)

                if re.search("iPhone", data["lecture_content"]):
                    unit = "ip"
                elif re.search("Android", data["lecture_content"]):
                    unit = "an"
                elif re.search("タブレット", data["lecture_content"]):
                    unit = "ta"
                else:
                    unit = "ot"

                models.UpcomingLecInfos.objects.get_or_create(
                    lecture_content=created_lec,
                    which_class_held=held_class,
                    target_unit_type=unit,
                    defaults={
                        "is_personal_lec": False,
                        "can_select_date": False
                    })
        pass

    @classmethod
    def fix_data(cls, src_file):
        pass
