# -*- coding: utf-8 -*-

import scrapy
import json
from core.models import db, Movie, Category
from crawler.spiders.subjects_spider import save_subject_detail


class MoviesSpider(scrapy.Spider):
    name = 'MoviesSpider'
    allowed_domains = ['douban.com']
    start_urls = [
        'https://frodo.douban.com/jsonp/subject_collection/movie_showing/items?os=ios&callback=&start=0&count=99999',
        'https://frodo.douban.com/jsonp/subject_collection/movie_latest/items?os=ios&callback=&start=0&count=99999',
        # 'https://api.douban.com/v2/movie/coming_soon',
        # 'https://api.douban.com/v2/movie/in_theaters',
        # 'https://api.douban.com/v2/movie/top250',
    ]

    def parse(self, response):
        res = json.loads(response.body)
        subject_type = res['subject_collection']['id']  # movie_showing or movie_latest
        for subject in res['subject_collection_items']:
            subject_id = subject['id']
            try:
                save_subject_detail(subject_id, subject_type)
            except StandardError, e:
                pass
