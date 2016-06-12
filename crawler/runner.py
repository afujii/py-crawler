# -*- coding: utf-8 -*-

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from crawler.spiders.movies_spider import MoviesSpider
from crawler.spiders.subjects_spider import SubjectsSpider


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


# 执行电影详情爬虫
def crawl_subjects(subjects):
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(SubjectsSpider)
        reactor.stop()

    crawl()
    reactor.run()
