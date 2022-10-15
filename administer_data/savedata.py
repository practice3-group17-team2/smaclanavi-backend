from administer_data.scraping import search_google
from administer_data.models import TestSaveData

def save_data():
    """ 
    scrapingする関数を呼び出してその結果を保存する関数、情報のUPDATEとかもできたらいいなと思っている
    """
    test_word = "スマホ教室" #任意の言葉、なんでもいい、仮置き
    link_ls, title_ls = search_google(test_word)

    for i in range(len(link_ls)):
        if i==5:
            break
        TestSaveData.objects.create(title=title_ls[i], url=link_ls[i])


if __name__ == "__main__":
    save_data()
