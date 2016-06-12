# -*- coding: utf-8 -*-

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from crawler.spiders import MoviesSpider


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})


# 执行所有爬虫
def run_spiders():
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(MoviesSpider)
        reactor.stop()

    crawl()
    reactor.run()
