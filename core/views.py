# -*- coding: utf-8 -*-

from flask import render_template, views, abort
from jinja2 import TemplateNotFound
from core.models import Movie, InTheaters, ComingSoon, Ranking, db


class LoginView(views.MethodView):
    def get(self):
        return render_template('login.html')


class InTheatersView(views.MethodView):
    def get(self):
        try:
            list = db.session.query(InTheaters, Movie).join(Movie, Movie.id==InTheaters.movie_id).all()
            movies = []
            for l in list:
                movies.append(list[1])
            # movies = Movie.query.order_by(Movie.rating.desc()).all()
            return render_template('in-theaters.html', movies=movies)
        except TemplateNotFound:
            abort(404)

    def post(self):
        return 'POST'


class ComingSoonView(views.MethodView):
    def get(self):
        try:
            list = db.session.query(ComingSoon, Movie).join(Movie, Movie.id==ComingSoon.movie_id).all()
            movies = []
            for l in list:
                movies.append(list[1])
            # movies = Movie.query.order_by(Movie.rating.desc()).all()
            return render_template('coming-soon.html', movies=movies)
        except TemplateNotFound:
            abort(404)

    def post(self):
        return 'POST'


class RankView(views.MethodView):
    def get(self):
        try:
            list = db.session.query(Ranking, Movie).join(Movie, Movie.id==Ranking.movie_id).all()
            movies = []
            for l in list:
                movies.append(list[1])
            # movies = Movie.query.order_by(Movie.rating.desc()).all()
            return render_template('rank.html', movies=movies)
        except TemplateNotFound:
            abort(404)

    def post(self):
        return 'POST'
