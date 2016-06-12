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
            # list = db.session.query(InTheaters, Movie).join(Movie, Movie.id==InTheaters.movie_id).all()
            # movies = []
            # for l in list:
            #     movies.append(list[1])
            movies = Movie.query.filter_by(category='movie_showing').order_by(Movie.rating.desc()).all()
            print(movies)
            return render_template('in-theaters.html', movies=movies)
        except TemplateNotFound:
            abort(404)


class ComingSoonView(views.MethodView):
    def get(self):
        try:
            movies = Movie.query.filter_by(category='movie_latest').order_by(Movie.rating_count.desc()).all()
            return render_template('coming-soon.html', movies=movies)
        except TemplateNotFound:
            abort(404)


class RankView(views.MethodView):
    def get(self):
        try:
            movies = Movie.query.order_by(Movie.rating.desc(), Movie.rating_count.desc()).all()
            # filter all genres
            genres = set()
            for m in movies:
                for g in m.genres.split(','):
                    genres.add(g)
            return render_template('rank.html', movies=movies, genres=genres)
        except TemplateNotFound:
            abort(404)
