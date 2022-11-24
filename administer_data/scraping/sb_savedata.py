from administer_data.scraping.sb_scraping import SBscraping as sb
from administer_data import models
import re

def save_data():
    """ 
    scrapingする関数を呼び出してその結果を保存する関数、情報のUPDATEとかもできたらいいなと思っている
    """
    data = sb.load_data_file_pkl()
    # test_word = "スマホ教室" #任意の言葉、なんでもいい、仮置き
    # link_ls, title_ls = search_google(test_word)


    # print(data)
    # key = (pref_id, area_id), area_name(店舗数))
    # value = {
    # "店舗名": {
    #     name:
    #     phone:
    #     parking:
    #     barrier_free:
    #     address
    # }
    city_name_pattern = re.compile(r'[^0-9（）]+')
    # area_name_pattern = re.compile(r'((.+?)市(.+?)区|(.+?)[市区町村])')

    models.City.objects.create(city_name="中央区")

    for key, value in data.items():
        print("\n\n\n")
        #TestSaveData.objects.create(title=title_ls[i], url=link_ls[i])
        print("key", key)
        print("value", value)

        if not value:
            continue

        city_name = city_name_pattern.match(key[1]).group()
        print("city_name", city_name)

        # area_name_xs = area_name_pattern.split(city_name)# [1:-1]
        # print("area_name_xs", area_name_xs)

        # area_name = area_name_xs[-1]
        # print("area_name", area_name)

        # class_name = value[]
        city, created = models.City.objects.get_or_create(city_name=city_name)

        if created: print("created!!!")
        print(city)
        
        
        # class_info = models.ClassInfo.objects.create(class_name=city=city)
        # print(class_info.class_name)

    # print(models.ClassInfo.objects.all())

def fix_data():
    data = sb.load_data_file_pkl()
    new_data_dict = {}
    for area, class_info_xs in data.items():
        print(f"area {area}")
        print(f"class_info_xs {class_info_xs}")

        for class_info in class_info_xs.values():
            # class_name = class_info["name"]
            class_info["class_name"] = class_info.pop("name")
            class_info["phone_number"] = class_info.pop("phone")
            class_info["has_parking"] = class_info.pop("parking")
            class_info["is_barrier_free"] = class_info.pop("barrier_free")
            print(f"class_info {class_info}")

        print("\n")
        
        print(f"class_info_xs {class_info_xs}")
        print("\n\n")

    # sb.save_data_file_pkl(data, file_path="softbank_fixed.pkl")
if __name__ == "__main__":
    save_data()
