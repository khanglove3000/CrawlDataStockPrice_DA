import scrapy
from pipelines import LoadSymbol
import numpy as np
from CrawKetQuaKinhDoanh5Cafef import ThongTinTaiChinh

class CrawlKQKD5Spider(scrapy.Spider):
    name = 'ketquakinhdoanhCafef'
    allowed_domains = ['s.cafef.vn']
    start_urls = ['http://s.cafef.vn/']
    run = LoadSymbol.connectDB()
    urlhistorys = []
    
    listsymbols = ['HPG','HSG','FLC']
    for id, symbol, urlsymbol in run:
        urlhistorys.append(urlsymbol)
    
    start_urls = urlhistorys

    def parse(self, response):
        url = response.url
        symbol = response.xpath('//*[@id="symbolbox"]/text()').get().split()[0]
        # chisochitieu_file = 'chisochitieu.csv'
        # chisochitieu = ThongTinTaiChinh(symbol, url, chisochitieu_file)
        #chisochitieu.chisochitieu()
        
        thongtintaichinh_KQKD_TS_theonam = 'thongtintaichinh_KQKD_TS_theonam.csv'
        thongtintaichinh_nam = ThongTinTaiChinh(symbol, url, thongtintaichinh_KQKD_TS_theonam)
        thongtintaichinh_nam.Nam()