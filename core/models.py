# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from core.app import app


db = SQLAlchemy(app)


# Database Schema
class Ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))  # 标题
    pic_url = db.Column(db.String(200))  # 图片链接
    point = db.Column(db.Float)  # 评分
    description = db.Column(db.String(1000))  # 描述
    ranking = db.Column(db.Integer)  # 排名
    source = db.Column(db.Integer)  # 来源
    crawl_time = db.Column(db.BigInteger)  # 爬取时间


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))  # 电影名
    pic_url = db.Column(db.String(200))  # 图片链接
    point = db.Column(db.Float)  # 评分
    description = db.Column(db.String(1000))  # 描述
    type = db.Column(db.Integer)  # 上映否？即将上映、已经上映
    classify = db.Column(db.Integer)  # 分类
    director = db.Column(db.String(100))  # 导演
    actor = db.Column(db.String(200))  # 演员
    release_time = db.Column(db.BigInteger)  # 上映时间
    urls = db.Column(db.String(2000))  # 电影相关链接
    source = db.Column(db.Integer)  # 来源
    crawl_time = db.Column(db.BigInteger)  # 爬取时间


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))  # 电影名称
    url = db.Column(db.String(200))  # 网站链接
