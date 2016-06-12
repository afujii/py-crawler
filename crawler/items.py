# -*- coding: utf-8 -*-

import scrapy


class InTheatersItem(scrapy.Item):
    id = scrapy.Field()


class ComingSoonItem(scrapy.Item):
    id = scrapy.Field()


class RankItem(scrapy.Item):
    id = scrapy.Field()


class SubjectItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    cover = scrapy.Field()
    summary = scrapy.Field()
