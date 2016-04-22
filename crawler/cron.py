# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from crawler.spiders import douban_spider


# 定时任务
def run_spiders():
    process = CrawlerProcess()
    process.crawl(douban_spider.DoubanSpider)
    process.start()
