# -*- coding: utf-8 -*-

# app config
DEBUG = True
SECRET_KEY = 'crawler'

# Scrapy settings for crawler project
BOT_NAME = 'crawler'

SPIDER_MODULES = ['handler']
NEWSPIDER_MODULE = 'handler'

DATABASE = {
    'username': 'root',
    'password': '',
    'host': '127.0.0.1',
    'port': '3306',
    'dbname': 'crawler',
}
