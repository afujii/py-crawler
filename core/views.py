# -*- coding: utf-8 -*-

from flask import render_template, request, views, abort
from jinja2 import TemplateNotFound
from core.models import Movie, InTheaters, ComingSoon, Ranking, db


class LoginView(views.MethodView):
    def get(self):
        return render_template('login.html')


class InTheatersView(views.MethodView):
    def get(self):
        movies = Movie.query.filter_by(category='movie_showing').order_by(Movie.rating.desc()).all()
        return render_template('in-theaters.html', movies=movies)


class ComingSoonView(views.MethodView):
    def get(self):
        movies = Movie.query.filter_by(category='movie_latest').order_by(Movie.rating_count.desc()).all()
        return render_template('coming-soon.html', movies=movies)


class RankView(views.MethodView):
    def get(self):
        # sort = request.args['sort']
        movies = Movie.query.order_by(Movie.rating.desc(), Movie.rating_count.desc()).all()
        # filter all genres
        genres = set()
        for m in movies:
            for g in m.genres.split(','):
                genres.add(g)
        return render_template('rank.html', movies=movies, genres=genres)
