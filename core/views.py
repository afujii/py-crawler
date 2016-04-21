# -*- coding: utf-8 -*-

from flask import render_template, request, views


class Home(views.MethodView):
    def get(self):
        print request.args
        return render_template('index.html')

    def post(self):
        print request.form


class About(views.MethodView):
    def get(self):
        print request.args
        return render_template('about.html')

    def post(self):
        print request.form
