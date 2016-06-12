# -*- coding: utf-8 -*-

from core import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


# 分类
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(256))


# 来源
class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(256))


# 电影
class Movie(db.Model):
    def __init__(self, title='', info='', rating='', cover=''):
        self.title = title
        self.info = info
        self.rating = rating
        self.cover = cover

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)  # 分类 id
    source_id = db.Column(db.Integer)  # 来源 id
    title = db.Column(db.String(256))  # 电影名
    info = db.Column(db.String(1024))  # 描述
    director = db.Column(db.String(256))  # 导演
    actor = db.Column(db.String(256))  # 演员
    rating = db.Column(db.Float)  # 评分
    cover = db.Column(db.String(256))  # 图片链接
    crawl_time = db.Column(db.Date)  # 爬取时间


# 即将上映
class ComingSoon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    will_show_at = db.Column(db.Date)


# 正在上映
class InTheaters(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)  # 分类 id
    show_at = db.Column(db.Date)  # 上映时间


# 分类排名
class Ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    want_count = db.Column(db.Integer)
    view_count = db.Column(db.Integer)
