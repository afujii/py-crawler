# -*- coding: utf-8 -*-

# app info
APP_NAME = 'crawler'

# flask config
DEBUG = True
SECRET_KEY = 'crawler'

# mysql connection
# SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/crawler'

# sqlite3 connection
SQLALCHEMY_DATABASE_URI = 'sqlite:///./database.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = True
