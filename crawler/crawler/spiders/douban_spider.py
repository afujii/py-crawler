# -*- coding: utf-8 -*-

import scrapy
import json
from crawler.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://frodo.douban.com/jsonp/subject_collection/movie_showing/items?os=ios&callback=&start=0&count=30']

    def parse(self, response):
        res = json.loads(response.body)
        for movie in res['subject_collection_items']:
            print movie['title']
            info_dict = {
                'title': movie['title'] or '',
                'info': movie['info'] or '',
                'rating': movie['rating'] and movie['rating']['value'] or -1,
                'cover': movie['cover'] and movie['cover']['url'] or ''
            }
            yield DoubanItem(**info_dict)
