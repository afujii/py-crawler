# -*- coding: utf-8 -*-

from flask import Blueprint, request
import json
import core.views as Views
from core.base import res
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
site.add_url_rule('/', view_func=Views.InTheatersView.as_view('index'))
site.add_url_rule('/login', view_func=Views.LoginView.as_view('login'))
site.add_url_rule('/in-theaters', view_func=Views.InTheatersView.as_view('in-theaters'))
site.add_url_rule('/coming-soon', view_func=Views.ComingSoonView.as_view('coming-soon'))
site.add_url_rule('/rank', view_func=Views.RankView.as_view('rank'))

@site.route('/api/login', methods=['POST'])
def login():
    params = request.form
    u = User.query.filter_by(
        username = params['username'],
        password = params['password']).first()
    if u is None:
        return res(-1)
    else:
        return res(200, u)

@site.route('/api/register', methods=['POST'])
def register():
    u = User(**request.form)
    u.is_expired = 0
    u.register_time = time.time()*1000
    db.session.add(u)
    db.session.commit()
    return res(200)
