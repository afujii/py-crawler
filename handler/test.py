# -*- coding: utf-8 -*-

import base
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class DmozSpider(scrapy.spiders.Spider):
    name = "test"
    allowed_domains = ["rankList.org"]
    start_urls = [
        "http://www.mtime.com/hotest/"
    ]

    def parse(self, response):
      filename = response.url.split("/")[-2]
      result = response.selector.css('.mtiplist .picbox a img')[0].xpath('@src')[0].extract()
      with open(filename, 'wb') as f:
          f.write(result)