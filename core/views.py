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
        # filter all genres
        all_movies = Movie.query.all()
        genres = set()
        for m in all_movies:
            for g in m.genres.split(','):
                genres.add(g)
        # display sorted
        sort = request.args.get('sort') or ''
        movies = Movie.query.filter(Movie.genres.like('%' + sort + '%')).order_by(Movie.rating.desc(), Movie.rating_count.desc()).all()
        if sort == u'全部' or not sort:
            return render_template('rank.html', movies=all_movies, genres=genres)
        else:
            return render_template('rank.html', movies=movies, genres=genres)
