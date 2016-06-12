# -*- coding: utf-8 -*-

from flask import Blueprint
import core.views as Views

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
site.add_url_rule('/in-theaters', view_func=Views.InTheatersView.as_view('in-theaters'))
site.add_url_rule('/coming-soon', view_func=Views.ComingSoonView.as_view('coming-soon'))
site.add_url_rule('/rank', view_func=Views.RankView.as_view('rank'))
