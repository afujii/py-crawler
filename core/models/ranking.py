# -*- coding: utf-8 -*-

from core import db


# 排名
class Ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    want_count = db.Column(db.Integer)
    view_count = db.Column(db.Integer)
