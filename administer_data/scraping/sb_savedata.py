import re

from administer_data.scraping.sb_scraping import SBscraping as sb
from administer_data import models
from administer_data.scraping.data import softbank_data as sb_data


def save_data():
    """ 
    pklファイルに保存されたデータからインスタンスを作成しモデルに保存する関数
    scrapingする関数の呼び出しや情報のUPDATEとかもできたらいいなと思っている
    """
    data = sb.load_data_file_pkl(file_path="softbank.pkl")
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

    org, _ = models.ClassOrganizer.objects.get_or_create(organizer_name="ソフトバンク")
    pref = models.Prefecture.objects.get(pref_name="東京都")

    for area, class_info_xs in data.items():
        if not class_info_xs:
            continue

        city_name = city_name_pattern.match(area[1]).group()
        city, _ = models.City.objects.get_or_create(city_name=city_name, prefecture=pref)

        for class_info in class_info_xs.values():
            class_info = models.ClassInfo.objects.create(city=city, class_organizer=org,
                                                         **class_info)

    sb.quit_driver()


def dict_to_pkl_file():
    sb.save_data_file_pkl(sb_data.data)


def fix_data():
    data = sb.load_data_file_pkl()
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

    sb.save_data_file_pkl(data)
    sb.quit_driver()


def create_and_fix_data():
    dict_to_pkl_file()
    fix_data()


if __name__ == "__main__":
    save_data()
