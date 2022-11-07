import sys, bs4, requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_NUM = "100"


class ScrapingBase:
    TIMEOUT = 10
    HEADER = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
    }

    # HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
    #                           AppleWebKit/537.36 (KHTML, like Gecko)
    #                           Chrome/105.0.0.0 Safari/537.36'}
    @classmethod
    def url_from_format(cls, url_format: str, **kwargs) -> str:
        """
        url_format.format(**kwargs)をする。formatした結果のURLを返す
        """
        url = ""
        try:
            url = url_format.format(kwargs)
        except Exception as e:
            print("ERROR_FORMAT:{}".format(e))
        return url

    @classmethod
    def crawl_data(cls, url: str):
        #result = requests.get(url, timeout=TIMEOUT, headers=HEADER)
        result = requests.get(url, timeout=cls.TIMEOUT, headers=cls.HEADER)
        result.raise_for_status()
        return result

    @classmethod
    def scrape_data(cls, url: str, selector: str) -> list:
        """urlからselectorに該当する要素を全て抽出して返す関数"""
        ret = None
        try:
            result = cls.crawl_data(url)
        except Exception as e:
            print("ERROR_DOWNLOAD:{}".format(e))
        else:
            soup = bs4.BeautifulSoup(result.content, 'html.parser')
            ret = soup.select(selector)
        return ret


class ScrapingSeleBase(ScrapingBase):

    @classmethod
    def init_driver(cls):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)
        wait = WebDriverWait(driver=driver, timeout=5)
        return driver, wait
    
    @classmethod
    def quit_driver(cls, driver):
        driver.close()
        driver.quit()

    @classmethod
    def crawl_data(cls, url: str, selector: str):
        driver, wait = cls.init_driver()
        driver.get(url)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        result = driver.page_source.encode('utf-8')
        cls.quit_driver(driver)
        return result

    @classmethod
    def scrape_data(cls, url: str, selector: str):
        """urlからselectorに該当する要素を抽出して返す関数"""
        ret = None
        try:
            result = cls.crawl_data(url, selector)
        except Exception as e:
            print("ERROR_DOWNLOAD\n{}".format(e))
        else:
            soup = bs4.BeautifulSoup(result, 'html.parser')
            ret = soup.select(selector)
        return ret


#グーグル検索から検索結果のリストを返す関数
def search_google(words):
    """
    検索する言葉を受け取ってlink_list, title_listを返す
    """
    link_list = []
    title_list = []

    TIMEOUT = 10
    HEADER = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
    }


    try:
        url = "https://www.google.co.jp/search?q=" + words + "&num=" + SEARCH_NUM + "&start=0"
        result = requests.get(url, timeout=TIMEOUT, headers=HEADER)

        result.raise_for_status()
    except Exception as e:
        print("ERROR_DOWNLOAD:{}".format(e))
    else:

        soup = bs4.BeautifulSoup(result.content, 'html.parser')
        # developer toolのelementsタブ 要素右クリから copy-> copy selector(beautiful soupはセレクターで動くので)
        links = soup.select(
            "#rso > div > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a")
        titles = soup.select(
            "#rso > div > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3")

        link_list = [link_tag.get("href") for link_tag in links]
        title_list = [title_tag.get_text() for title_tag in titles]

        #デバッグ用のprint
        #print("length {}, {}".format(len(link_list), len(title_list)))

        #タイトルとリンクが不一致の場合、
        if len(link_list) != len(title_list):
            return [], []

    return link_list, title_list


#"""
def main():

    words = input("検索ワードを入力してください")
    print(search_google(words))


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nprogram was ended.\n")
        sys.exit()
#"""
