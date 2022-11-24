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

    for key, value in data.items():
        #TestSaveData.objects.create(title=title_ls[i], url=link_ls[i])
        print("key", key)
        print("value", value, "\n\n\n")

        if not value:
            continue

        city_name = city_name_pattern.match(key[1]).group()
        print("city_name", city_name)

        # area_name_xs = area_name_pattern.split(city_name)# [1:-1]
        # print("area_name_xs", area_name_xs)

        # area_name = area_name_xs[-1]
        # print("area_name", area_name)

        city = models.City.objects.get_or_create(city_name=city_name)
        
        
        # models.ClassInfo.objects.create()
    print(models.City.objects.all())
if __name__ == "__main__":
    save_data()
