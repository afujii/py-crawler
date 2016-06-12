# -*- coding: utf-8 -*-

# app info
APP_NAME = 'crawler'

# flask config
DEBUG = True
SECRET_KEY = 'crawler'

# scrapy settings for crawler project
# BOT_NAME = 'crawler'
#
# SPIDER_MODULES = ['handler']
# NEWSPIDER_MODULE = 'handler'

# database config
# DATABASE = {
#     'username': 'root',
#     'password': '',
#     'host': '127.0.0.1',
#     'port': '3306',
#     'dbname': 'crawler',
# }

# SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/crawler'
SQLALCHEMY_DATABASE_URI = 'sqlite:///./database.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = True
