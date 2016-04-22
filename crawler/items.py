# -*- coding: utf-8 -*-

import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    info = scrapy.Field()
    rating = scrapy.Field()
    cover = scrapy.Field()
