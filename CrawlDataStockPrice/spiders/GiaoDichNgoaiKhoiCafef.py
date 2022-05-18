import scrapy
from pipelines import LoadSymbol
import numpy as np
from CrawlGiaoDichNgoaiKhoi import CrawlGiaoDichNgoaiKhoi


class GiaoDichNgoaiKhoiCafefSpider(scrapy.Spider):
    name = 'GiaoDichNgoaiKhoiCafef'
    allowed_domains = ['s.cafef.vn']
    start_urls = ['http://s.cafef.vn/']
    run = LoadSymbol.connectDB()
    urlhistorys = []

    for id, symbol, urlsymbol in run:
        urlhistorys.append(urlsymbol)

    start_urls = urlhistorys

    def parse(self, response):
        url = response.url
        symbol = response.xpath('//*[@id="symbolbox"]/text()').get().split()[0]
        filename = 'GiaiDichNgoaiKhoi_Cafef.csv'
        CrawlGiaoDichNgoaiKhoi(symbol, url, filename)