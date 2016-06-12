# -*- coding: utf-8 -*-

import scrapy
import json
from core.models import db, Movie
from crawler.spiders.subjects_spider import save_subject_detail


class MoviesSpider(scrapy.Spider):
    name = 'MoviesSpider'
    allowed_domains = ['douban.com']
    start_urls = [
        'https://frodo.douban.com/jsonp/subject_collection/movie_showing/items?os=ios&callback=&start=0&count=30',
        'https://api.douban.com/v2/movie/coming_soon',
        'https://api.douban.com/v2/movie/in_theaters',
        # 'https://api.douban.com/v2/movie/top250',
    ]

    def parse(self, response):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        res = json.loads(response.body)

        for subject in res['subjects']:
            pass
            # save_subject_detail(subject['id'])
