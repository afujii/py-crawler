# -*- coding: utf-8 -*-

import scrapy
import json
from core.models import db, Movie

'''
detail:
https://api.douban.com/v2/movie/subject/
'''
class MoviesSpider(scrapy.Spider):
    name = 'MoviesSpider'
    allowed_domains = ['douban.com']
    start_urls = [
        'https://api.douban.com/v2/movie/coming_soon',
        'https://api.douban.com/v2/movie/in_theaters',
        'https://api.douban.com/v2/movie/top250',
    ]

    def parse(self, response):
        res = json.loads(response.body)
        for subject in res['subjects']:
            m = Movie()
            db.session.add(m)
            r = requests.get('https://api.douban.com/v2/movie/subject/'+subject['id'])

