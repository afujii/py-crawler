# -*- coding: utf-8 -*-

from core import views


# associate with views
def register_routes(app):
    app.add_url_rule('/', view_func=views.Home.as_view('home'))
    app.add_url_rule('/about', view_func=views.About.as_view('about'))
