# -*- coding: utf-8 -*-

import scrapy, json, requests
from datetime import datetime
from core.models import db, Movie
from crawler.items import SubjectItem
from bs4 import BeautifulSoup


# SUBJECT_API = 'https://api.douban.com/v2/movie/subject/'
SUBJECT_API = 'https://movie.douban.com/subject/%s/'


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['douban.com']
    start_urls = []

    def __init__(self, category=None, *args, **kwargs):
        super(SubjectsSpider, self).__init__(*args, **kwargs)
        for subject in subjects:
            id = subject['id']
            self.start_urls.append('https://api.douban.com/v2/movie/subject/%s/' % id)

    def parse(self, response):
        res = json.loads(response.body)
        print res


def save_subject_detail(id, type):
    s = BeautifulSoup(requests.get(SUBJECT_API % id).text, 'html.parser')

    try:
        movie = Movie()
        movie.title =        s.body.find(attrs={'property':'v:itemreviewed'}).get_text(),
        movie.summary =      s.body.find(attrs={'property':'v:summary'}).get_text(),
        movie.director =     s.body.find(attrs={'rel':'v:directedBy'}).get_text(),
        movie.actors =       ','.join(map(lambda x: x.get_text(), s.body.find_all(attrs={'rel':'v:starring'}))),
        movie.rating =       s.body.find(attrs={'property':'v:average'}).get_text(),
        movie.rating_count = s.body.find(attrs={'property':'v:votes'}).get_text(),
        movie.cover =        s.body.find(attrs={'rel':'v:image'}).attrs['src'],
        movie.show_at =      datetime.strptime(s.body.find(attrs={'property':'v:initialReleaseDate'}).get_text()[0:10], '%Y-%m-%d'),
        movie.crawl_at =     datetime.utcnow(),
        movie.genres =       ','.join(map(lambda x: x.get_text(), s.body.find_all(attrs={'property':'v:genre'}))),
        db.session.add(movie)
        db.session.commit()
        print movie
    except StandardError, e:
        print 'parse subject error', e
        raise e
