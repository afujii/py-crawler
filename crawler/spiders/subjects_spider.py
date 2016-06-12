# -*- coding: utf-8 -*-

import scrapy, datetime, json, requests
from core.models import db, Movie, Category
from crawler.items import SubjectItem
from bs4 import BeautifulSoup

SUBJECT_API = 'https://api.douban.com/v2/movie/subject/'

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


def save_subject_detail(id):
    res = json.loads(requests.get(SUBJECT_API+id).text)
    m = Movie()
    #query id of category
    cate = res['genres'][0]
    c = Category.query.filter_by(category=cate).first()
    if c:
        cate = c.id
    else:
        temp = Category(category=cate)
        db.session.add(temp)
        db.session.commit()
        cate = temp.id
    m.category_id = cate
    m.source_id = 0
    m.title = res['title']
    m.summary = res['summary']
    m.director = ','.join(map(lambda x: x['name'], res['directors']))
    m.rating = res['rating']['average']
    m.cover = res['images']['large']
    # m.crawl_time = datetime.datetime
    db.session.add(m)
    db.session.commit()
    return 'successfully save id ' + id
