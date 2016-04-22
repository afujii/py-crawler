# -*- coding: utf-8 -*-

from flask import Blueprint
from core.views import Index

# Blueprint component
site = Blueprint(
    name='site',
    import_name=__name__,
    template_folder='templates',
    static_folder='static',
    url_prefix=None
)


# associate with views
site.add_url_rule('/', view_func=Index.as_view('index'))
