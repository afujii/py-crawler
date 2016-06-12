# -*- coding: utf-8 -*-

from flask import Blueprint
import json
import core.views as Views
from core.base import res
import core.apis as Apis

# Blueprint component
site = Blueprint(
    name='site',
    import_name=__name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/site',
    url_prefix=None,
)


# associate with views
site.add_url_rule('/',            view_func=Views.LoginView.as_view('index'))
site.add_url_rule('/login',       view_func=Views.LoginView.as_view('login'))
site.add_url_rule('/in-theaters', view_func=Views.InTheatersView.as_view('in-theaters'))
site.add_url_rule('/coming-soon', view_func=Views.ComingSoonView.as_view('coming-soon'))
site.add_url_rule('/rank',        view_func=Views.RankView.as_view('rank'))

# associate with apis
site.add_url_rule('/api/login',    view_func=Apis.LoginApi.as_view('login_api'))
site.add_url_rule('/api/register', view_func=Apis.RegisterApi.as_view('register_api'))
