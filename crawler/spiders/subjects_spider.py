# -*- coding: utf-8 -*-

import scrapy
import json
from core.models import db, Movie
from crawler.items import SubjectItem


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['douban.com']
    start_urls = []

    def __init__(self, category=None, *args, **kwargs):
        super(SubjectsSpider, self).__init__(*args, **kwargs)
        for subject in subjects:
            id = subject['id']
            self.start_urls.append('https://api.douban.com/v2/movie/subject/%s' % id)

    def parse(self, response):
        res = json.loads(response.body)
        print res
