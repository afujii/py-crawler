# -*- coding: utf-8 -*-

from core import db


# 排名
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(256))
