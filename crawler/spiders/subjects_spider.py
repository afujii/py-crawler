# -*- coding: utf-8 -*-

import scrapy, json, requests
from datetime import datetime
from core.models import db, Movie
from crawler.items import SubjectItem
from bs4 import BeautifulSoup


# SUBJECT_API = 'https://api.douban.com/v2/movie/subject/'
SUBJECT_API = 'https://movie.douban.com/subject/%s/'

def save_subject_detail(id, type):
    response = requests.get(SUBJECT_API % id).text
    s = BeautifulSoup(response, 'html.parser')

    try:
        movie = Movie()
        movie.title =        s.body.find(attrs={'property':'v:itemreviewed'}).get_text().strip()
        movie.summary =      s.body.find(attrs={'property':'v:summary'}).get_text().strip()
        movie.director =     s.body.find(attrs={'rel':'v:directedBy'}).get_text().strip()
        movie.actors =       ','.join(map(lambda x: x.get_text().strip(), s.body.find_all(attrs={'rel':'v:starring'})))
        movie.rating =       s.body.find(attrs={'property':'v:average'}).get_text().strip()
        movie.rating_count = s.body.find(attrs={'property':'v:votes'}).get_text().strip()
        movie.cover =        s.body.find(attrs={'rel':'v:image'}).attrs['src'].strip()
        movie.show_at =      datetime.strptime(s.body.find(attrs={'property':'v:initialReleaseDate'}).get_text()[0:10], '%Y-%m-%d')
        movie.crawl_at =     datetime.utcnow()
        movie.genres =       ','.join(map(lambda x: x.get_text(), s.body.find_all(attrs={'property':'v:genre'}))).strip()
        movie.category = type
        print 'saving movie => ', movie.title
        db.session.add(movie)
        db.session.commit()
    except StandardError, e:
        print 'parse subject error', e
        raise e
