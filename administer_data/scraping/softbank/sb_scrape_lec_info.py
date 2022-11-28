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

from ..scraping import ScrapingBase, ScrapingSeleBase


class SBLecInfoScraper(ScrapingSeleBase):

    options = Options()
    options.headless = True
    options.add_argument('--user-agent=' + ScrapingBase.UA)
    driver = webdriver.Chrome(chrome_options=options)
    wait = WebDriverWait(driver=driver, timeout=2)

    @classmethod
    def crawl_data(cls, url: str, b_selector: str):
        driver = cls.driver
        wait = cls.wait

        driver.get(url)
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        driver.find_element(By.CSS_SELECTOR, b_selector).click()
        result = driver.page_source.encode('utf-8')
        return result

    @classmethod
    def scrape_data(cls, url: str, selector: str, button_selecter: str):
        """urlからselectorに該当する要素を全て抽出して返す関数"""
        ret = []
        try:
            result = cls.crawl_data(url, button_selecter)
        except Exception as e:
            print("ERROR_DOWNLOAD:{}\n{}".format(url, e))
        else:
            soup = bs4.BeautifulSoup(result, 'html.parser')
            ret = soup.select(selector)
            # ret.append("aaieuaojf") # can add to resultSet
            # print(type(ret[0])) # <class 'bs4.element.Tag'>
        return ret

    lec_info_by_class_url_format = "https://spcr.reserve.mb.softbank.jp/spad-self/reservation/{0[class_id]}"
    lec_info_selecter = "#middle-category-card-row > div"
    # lec_info_selecter = "#middle-category-card-row > div > div > div.new-category-card-header.text-lg-left"
    button_selecter = "#tab-1 > div > div > div:nth-child(1) > div > div > label"

    @classmethod
    def get_lec_info_divs_by_class(cls, class_id):
        result = None
        url = cls.url_from_format(cls.lec_info_by_class_url_format,
                                  **{"class_id": class_id})
        result = cls.scrape_data(url, cls.lec_info_selecter,
                                 cls.button_selecter)
        return result
