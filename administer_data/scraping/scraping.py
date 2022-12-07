import bs4
from bs4.element import ResultSet
import requests
import sys

from pyppeteer import launch
import asyncio

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_NUM = "100"


class ScrapingBase:
    TIMEOUT = 10
    UA = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
    HEADER = {'User-Agent': UA}

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
    async def crawl_data(cls, url: str, selecter):
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        # selecterの要素が読まれるまで待機
        await page.waitForSelector(selecter, visible=True)
        html = await page.content()
        await browser.close()
        return html

    @classmethod
    def scrape_data(cls, url: str, selector: str):
        """urlからselectorに該当する要素を全て抽出して返す関数"""
        ret = ResultSet(None, [])
        try:
            # result = cls.crawl_data(url)
            html = asyncio.get_event_loop().run_until_complete(cls.crawl_data(url, selector))
        except Exception as e:
            print("ERROR_DOWNLOAD:{}\n{}".format(url, e))
        else:
            # soup = bs4.BeautifulSoup(result.content, 'html.parser')
            soup = bs4.BeautifulSoup(html, 'html.parser')
            ret = soup.select(selector)
        return ret


class ScrapingSeleBase(ScrapingBase):

    options = Options()
    options.headless = True
    options.add_argument('--user-agent=' + ScrapingBase.UA)
    driver = webdriver.Chrome(chrome_options=options)
    wait = WebDriverWait(driver=driver, timeout=2)

    @classmethod
    def quit_driver(cls):
        cls.driver.close()
        cls.driver.quit()

    @classmethod
    def crawl_data(cls, url: str, selector: str):
        driver = cls.driver
        wait = cls.wait

        driver.get(url)
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        result = driver.page_source.encode('utf-8')
        return result

    @classmethod
    def scrape_data(cls, url: str, selector: str):
        """urlからselectorに該当する要素を抽出して返す関数"""
        ret = ResultSet(None, [])
        try:
            result = cls.crawl_data(url, selector)
        except Exception as e:
            print("ERROR_DOWNLOAD:{}\n{}".format(url, e))
        else:
            soup = bs4.BeautifulSoup(result, 'html.parser')
            ret = soup.select(selector)
        return ret
