from scrapy import Spider
# from spiders.CrawlDatLenhCafef import CrawldatlenhcafefSpider
# from spiders.HistorydataCafef import HistorydatacafefSpider
# from spiders.GiaoDichNgoaiKhoiCafef import GiaoDichNgoaiKhoiCafefSpider
from spiders.KetQuaKinhDoanh import CrawldatlenhcafefSpider
from spiders.CrawlKQKDCafef import CrawlKQKD5Spider
# scrapy api
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner,CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(CrawlKQKD5Spider)
crawl()
reactor.run()