import scrapy
from pipelines import LoadSymbol
import numpy as np
from CrawlKQKD import CrawlDataKQKD


class CrawldatlenhcafefSpider(scrapy.Spider):
    name = 'ketquakinhdoanh'
    allowed_domains = ['s.cafef.vn']
    start_urls = ['http://s.cafef.vn/']
    run = LoadSymbol.connectDB()
    urlhistorys = []

    for id, symbol, urlsymbol in run[:5]:
        urlhistorys.append(urlsymbol)

    start_urls = urlhistorys

    def parse(self, response):
        url = response.url
        symbol = response.xpath('//*[@id="symbolbox"]/text()').get().split()[0]
        filename = 'KeQuaKinhDoanh.csv'
        CrawlDataKQKD(symbol, url, filename)