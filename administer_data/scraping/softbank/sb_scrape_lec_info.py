import bs4
from bs4.element import ResultSet
import os
import pickle
import re
import time
from typing import List

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from administer_data import models
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
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        result = driver.page_source.encode('utf-8')
        return result

    @classmethod
    def scrape_data(cls, url: str, selector: str):
        """urlからselectorに該当する要素を全て抽出して返す関数"""
        ret = ResultSet(None, [])
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
    def scrape_clicked_data(cls, url: str, selector: str,
                            button_selector: str):
        """urlからselectorに該当する要素を全て抽出して返す関数"""
        ret = ResultSet(None, [])
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
        """
        class_id(ex:TD20)を受け取って情報を含むdivのリストを返す関数
        """
        result = ResultSet(None, [])
        url = cls.url_from_format(cls.lec_info_by_class_url_format,
                                  **{"class_id": class_id})

        categorys = ScrapingBase.scrape_data(
            url, cls.getting_num_of_button_selector)
        categorys_length = len(categorys)
        # print(categorys_length)

        for nth in range(1, categorys_length + 1):
            button_selector = cls.button_selector_format.format(nth)
            result += cls.scrape_clicked_data(url, cls.lec_info_selector,
                                              button_selector)
        return result

    @classmethod
    def get_lec_info_from_divs(cls, info_divs: ResultSet) -> List[dict]:
        """
        get_lec_info_divs_by_classの結果のresultSetを受け取って情報の辞書のリストを返す関数
        """
        data = []

        for i, div in enumerate(map(str, info_divs)):
            soup = bs4.BeautifulSoup(div, 'html.parser')

            time_selector = "div[id^=tagParent] > div > div.col-lg-8.col-12 > div.category-card-option > div > div > div:nth-child(1) > div > div.category-card-option-item-value"
            ret_time = soup.select_one(time_selector)

            num_of_members_selector = "div[id^=tagParent] > div > div.col-lg-8.col-12 > div.category-card-option > div > div > div:nth-child(2) > div > div.category-card-option-item-value"
            num_of_members = soup.select_one(num_of_members_selector)

            titile_selector = "div.category-card-body-title"
            ret_title = soup.select_one(titile_selector)

            category_selector = "div.new-category-card-header"
            ret_category = soup.select_one(category_selector)

            # print(f"title: {ret_title}")
            # print(f"time: {ret_time}")
            # print(f"members: {num_of_members}")

            tmp = {}
            tmp["lec_title"] = ret_title.text
            tmp["required_time"] = ret_time.text
            tmp["lecture_content"] = ret_category.text
            tmp["num_of_members"] = num_of_members.text
            data.append(tmp)

        return data

    @classmethod
    def get_lec_info_by_class(cls, class_id) -> List[dict]:
        """
        class_idを受け取って講義情報の辞書のリストを返す関数
        """
        info_divs = cls.get_lec_info_divs_by_class(class_id)
        data = cls.get_lec_info_from_divs(info_divs)
        return data

    @classmethod
    def _get_class_id_and_uuid(self) -> List[tuple]:
        """
        URLの教室識別用のIDとモデル内のUUIDのタプルのリストを返す
        class_id:TD20
        i.id: d10みたいなuuid
        """
        result = []
        re_class_id = re.compile("detail/(.+)/")
        org_sb = models.ClassOrganizer.objects.get(organizer_name="ソフトバンク")
        objs = models.ClassInfo.objects.filter(class_organizer=org_sb)
        # print(objs[:5])
        for i in objs:
            class_id = re_class_id.split(i.site_url)[1]
            result.append((class_id, str(i.id)))
        return result

    @classmethod
    def get_overall_lec_info(cls, debug=False):
        """
        データベースに入っているソフトバンクの店舗全体に対して情報を取得し、結果の辞書を返す
        {class_info.id(uuid):[
                {講義の情報},
                {講義の情報}
        ]}
        debug = Trueの場合長さ3の結果が返る
        """
        result_dic = {}
        ids = cls._get_class_id_and_uuid()

        if debug==True:
            ids = ids[:3]

        for class_id, uuid_ in ids:
            tmp = cls.get_lec_info_by_class(class_id)
            result_dic[uuid_] = tmp
            time.sleep(0.05)

        return result_dic


