import scrapy
from pipelines import LoadSymbol
from CrawlDataHistory import CrawlDataSymbol


class HistorydatacafefSpider(scrapy.Spider):
    name = 'HistorydataCafef'

    allowed_domains = ['s.cafef.vn']
    run = LoadSymbol.connectDB()
    urlhistorys = []
   
    for id, symbol, urlsymbol in run:
        urlhistorys.append(urlsymbol)

    start_urls = urlhistorys

    def parse(self, response):
        url = response.url
        symbol = response.xpath('//*[@id="symbolbox"]/text()').get().split()[0]
        filename = 'HistoryData_Cafef.csv'
        CrawlDataSymbol(symbol, url, filename)