# -*- coding: utf-8 -*-

from core import db


# 电影
class InTheaters(db.Model):

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
