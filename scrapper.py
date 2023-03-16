from link_spy.link_spy.spiders.link_spider import DynamicLinkSpider
from scrapy.crawler import CrawlerProcess
import sys

async def parse_link():
    if 'twisted.internet.reactor' in sys.modules:
        del sys.modules['twisted.internet.reactor']
    spider = DynamicLinkSpider()
    process = CrawlerProcess()
    process.crawl(DynamicLinkSpider)
    process.start()
