# -*- coding: utf-8 -*-

import scrapy
import json
from core import db
from core.models import Movie


class MoviesSpider(scrapy.Spider):
    name = 'MoviesSpider'
    allowed_domains = ['douban.com']
    start_urls = [
        'https://api.douban.com/v2/movie/coming_soon',
        'https://api.douban.com/v2/movie/in_theaters',
    ]

    def __init__(self):
        self.file = open('items.json', 'wb')

    def parse(self, response):
        res = json.loads(response.body)
        for subject in res['subjects']:
            print subject['id'], subject['title']
            # crawl_subjects(res['subjects'])
        self.file.write(response.body + '\n')
