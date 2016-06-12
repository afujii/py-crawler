# -*- coding: utf-8 -*-

from core import db


# 电影
class InTheaters(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)  # 分类 id
    show_at = db.Column(db.Date)  # 上映时间
