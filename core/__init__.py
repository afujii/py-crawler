# -*- coding: utf-8 -*-

from flask import Flask
from core import settings
from flask_sqlalchemy import SQLAlchemy

app = Flask(settings.APP_NAME)
app.config.from_object(settings)

db = SQLAlchemy(app)
