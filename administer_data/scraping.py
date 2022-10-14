import sys, bs4, requests

SEARCH_NUM = "100"
TIMEOUT = 10
HEADER = {
    'User-Agent':
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
}

# HEADER      = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}


#グーグル検索から検索結果のリストを返す関数
def search_google(words):
    """
    検索する言葉を受け取ってlink_list, title_listを返す
    """
    link_list = []
    title_list = []

    try:
        url = "https://www.google.co.jp/search?q=" + words + "&num=" + SEARCH_NUM + "&start=0"
        result = requests.get(url, timeout=TIMEOUT, headers=HEADER)

        result.raise_for_status()
    except Exception as e:
        print("ERROR_DOWNLOAD:{}".format(e))
    else:

        soup = bs4.BeautifulSoup(result.content, 'html.parser')
        # developer toolのelementsタブ 要素右クリから copy-> copy selecter(beautiful soupはセレクターで動くので)
        links = soup.select(
            "#rso > div > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a")
        titles = soup.select(
            "#rso > div > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3")

        link_list = [link_tag.get("href") for link_tag in links]
        title_list = [title_tag.get_text() for title_tag in titles]

        print("length {}, {}".format(len(link_list), len(title_list)))
        #タイトルとリンクが不一致の場合、
        if len(link_list) != len(title_list):
            return [], []

    return link_list, title_list


def main():

    words = input("検索ワードを入力してください")
    print(search_google(words))


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nprogram was ended.\n")
        sys.exit()
