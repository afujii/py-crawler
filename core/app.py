# -*- coding: utf-8 -*-

from flask import Flask
from core import settings
from core import routes

# create app
app = Flask(settings.APP_NAME)
app.config.from_object(settings)

# setup routes
routes.register_routes(app)
