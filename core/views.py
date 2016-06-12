# -*- coding: utf-8 -*-

from flask import render_template, views, abort
from jinja2 import TemplateNotFound
from core.models import Movie


class InTheatersView(views.MethodView):
    def get(self):
        try:
            movies = Movie.query.order_by(Movie.rating.desc()).all()
            return render_template('in-theaters.html', movies=movies)
        except TemplateNotFound:
            abort(404)

    def post(self):
        return 'POST'


class ComingSoonView(views.MethodView):
    def get(self):
        try:
            movies = Movie.query.order_by(Movie.rating.desc()).all()
            return render_template('coming-soon.html', movies=movies)
        except TemplateNotFound:
            abort(404)

    def post(self):
        return 'POST'


class RankView(views.MethodView):
    def get(self):
        try:
            movies = Movie.query.order_by(Movie.rating.desc()).all()
            return render_template('rank.html', movies=movies)
        except TemplateNotFound:
            abort(404)

    def post(self):
        return 'POST'
