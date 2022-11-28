import bs4
import os
import pickle
import re
import time

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from administer_data.scraping.scraping import ScrapingBase
from administer_data.scraping.scraping import ScrapingSeleBase


class SBLecInfoScraper(ScrapingSeleBase):

    options = Options()
    options.headless = True
    options.add_argument('--user-agent=' + ScrapingBase.UA)
    driver = webdriver.Chrome(chrome_options=options)
    wait = WebDriverWait(driver=driver, timeout=2)

    @classmethod
    def crawl_data(cls, url: str, selector: str, need_to_click: bool = False):
        """
        b_selectorを押した後のhtmlを返す
        """
        driver = cls.driver
        wait = cls.wait

        driver.get(url)
        if need_to_click:
            driver.find_element(By.CSS_SELECTOR, selector).click()
        else:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        result = driver.page_source.encode('utf-8')
        return result

    @classmethod
    def scrape_data(cls, url: str, selector: str):
        """urlからselectorに該当する要素を全て抽出して返す関数"""
        ret = []
        try:
            result = cls.crawl_data(url, selector)
        except Exception as e:
            print("ERROR_DOWNLOAD:{}\n{}".format(url, e))
        else:
            soup = bs4.BeautifulSoup(result, 'html.parser')
            ret = soup.select(selector)
            # ret.append("aaieuaojf") # can add to resultSet
            # print(type(ret[0])) # <class 'bs4.element.Tag'>
        return ret
    
    @classmethod
    def scrape_clicked_data(cls, url: str, selector: str, button_selector: str):
        """urlからselectorに該当する要素を全て抽出して返す関数"""
        ret = []
        try:
            result = cls.crawl_data(url, button_selector, need_to_click=True)
        except Exception as e:
            print("ERROR_DOWNLOAD:{}\n{}".format(url, e))
        else:
            soup = bs4.BeautifulSoup(result, 'html.parser')
            ret = soup.select(selector)
            # ret.append("aaieuaojf") # can add to resultSet
            # print(type(ret[0])) # <class 'bs4.element.Tag'>
        return ret

    lec_info_by_class_url_format = "https://spcr.reserve.mb.softbank.jp/spad-self/reservation/{0[class_id]}"
    lec_info_selector = "#middle-category-card-row > div"
    # 動作確認用のタイトルのセレクタ
    # lec_info_selector = "#middle-category-card-row > div > div > div.new-category-card-body > div.category-card-body-title"
    button_selector_format = "#tab-1 > div > div > div:nth-child({}) > div > div > label"
    getting_num_of_button_selector = "#tab-1 > div > div > div > div > div > label"

    @classmethod
    def get_lec_info_divs_by_class(cls, class_id):
        result = []
        url = cls.url_from_format(cls.lec_info_by_class_url_format,
                                  **{"class_id": class_id})

        categorys = ScrapingBase.scrape_data(url, cls.getting_num_of_button_selector)
        categorys_length = len(categorys)
        print(categorys_length)

        for nth in range(1, categorys_length+1):
            button_selector = cls.button_selector_format.format(nth)
            result += cls.scrape_clicked_data(url, cls.lec_info_selector, button_selector) 
        return result

    @classmethod
    def get_lec_info_from_div(cls, info_divs) -> dict:
        
        pass
