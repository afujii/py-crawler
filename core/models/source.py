# -*- coding: utf-8 -*-

from core import db


# 来源
class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(256))
