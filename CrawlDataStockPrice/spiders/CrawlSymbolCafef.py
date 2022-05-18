import scrapy
# -*- coding: utf-8 -*-
from selenium import webdriver
import scrapy
import os, time

from sqlite3 import Error
from ..items import *
from scrapy.loader import ItemLoader

from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

option = webdriver.ChromeOptions()
option.add_argument('headless')

class CrawlsymbolcafefSpider(scrapy.Spider):
    name = 'CrawlSymbolCafef'
    allowed_domains = ['s.cafef.vn']
    start_urls = ['https://s.cafef.vn/lich-su-kien.chn']
    driver = webdriver.Chrome(executable_path="D:\chromedriver", options=option)
    baseUrl = 'http://s.cafef.vn'

    def parse(self, response):
        self.driver.get(response.url)
        for i in range(2, 15):
            for a in self.driver.find_elements_by_xpath('.//tr/td[@class="leftcell normal"]/a'):
                symbol = a.text
                loader = ItemLoader(item=Symbol(), response=response)
                urlsymbol = a.get_attribute('href')
                loader.add_value('symbol', symbol)
                loader.add_value('urlsymbol', urlsymbol)
                yield loader.load_item()
            nextpage = self.driver.find_elements_by_xpath('.//td[@align="center"]/input[@value=' + str(i) + ']')[0]
            time.sleep(2)
            nextpage.click()
        self.driver.quit()
            

