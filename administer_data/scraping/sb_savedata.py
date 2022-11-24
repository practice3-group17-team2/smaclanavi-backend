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

    # print(data)
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
    # area_name_pattern = re.compile(r'((.+?)市(.+?)区|(.+?)[市区町村])')

    for area, class_info_xs in data.items():
        print(f"area {area}")
        print(f"class_info_xs {class_info_xs}\n")

        if not class_info_xs:
            continue

        city_name = city_name_pattern.match(area[1]).group()
        # print(f"city_name {city_name}")

        # area_name_xs = area_name_pattern.split(city_name)# [1:-1]
        # print("area_name_xs", area_name_xs)
        # area_name = area_name_xs[-1]
        # print("area_name", area_name)

        city, created = models.City.objects.get_or_create(city_name=city_name)

        if created: print(f"{city} created!!!")
        
        for class_info in class_info_xs.values():
            class_info = models.ClassInfo.objects.create(city=city, **class_info)
            # print(f"class_name: {class_info.class_name}\n")

    [print(i) for i in models.ClassInfo.objects.all()]
    sb.quit_driver()

def dict_to_pkl_file():
    sb.save_data_file_pkl(sb_data.data)

def fix_data():
    data = sb.load_data_file_pkl()
    for area, class_info_xs in data.items():
        print(f"Before:\narea {area}")
        print(f"class_info_xs {class_info_xs}\n")

        for class_info in class_info_xs.values():
            if class_info["has_parking"] in ["None", "－"]:
                class_info["has_parking"] = False
            else:
                class_info["has_parking"] = True
            
            if class_info["is_barrier_free"] == "－":
                class_info["is_barrier_free"] = False
            else:
                class_info["is_barrier_free"] = True
            
            print(f"class_info {class_info}")

        print("\n")
        
        print(f"After:\nclass_info_xs {class_info_xs}")
        print("\n\n")

    sb.save_data_file_pkl(data)
    sb.quit_driver()

def create_and_fix_data():
    dict_to_pkl_file()
    fix_data()

if __name__ == "__main__":
    save_data()
