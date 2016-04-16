# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from core.orm import Ranking
import core.base as base
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

x = Ranking(title='测试电影', pic_url='139.129.35.112',
	point=9.9, description='sfdfghjk', ranking=1, source=1, crawl_time=12345678)

base.merge(x)

class DmozSpider(scrapy.spiders.Spider):
    name = "test"
    allowed_domains = ["rankList.org"]
    start_urls = [
        "http://www.mtime.com/hotest/"
    ]
    def parse(self, response):
    	pass