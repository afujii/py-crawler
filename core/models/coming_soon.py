# -*- coding: utf-8 -*-

from core import db


# 排名
class ComingSoon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    will_show_at = db.Column(db.Date)
