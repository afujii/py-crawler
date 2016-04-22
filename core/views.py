# -*- coding: utf-8 -*-

import json
from flask import render_template, request, views, abort
from jinja2 import TemplateNotFound
from core.models import Movie


class Index(views.MethodView):
    def get(self):
        try:
            movies = Movie.query.order_by(Movie.rating.desc()).all()
            return render_template('index.html', movies=movies)
        except TemplateNotFound:
            abort(404)
