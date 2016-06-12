# -*- coding: utf-8 -*-

import scrapy


class InTheatersItem(scrapy.Item):
    id = scrapy.Field()


class ComingSoonItem(scrapy.Item):
    id = scrapy.Field()


class RankItem(scrapy.Item):
    id = scrapy.Field()


class MovieItem(scrapy.Item):
    pass


class SubjectItem(scrapy.Item):
    pass
