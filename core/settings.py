# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
BOT_NAME = 'crawler'

SPIDER_MODULES = ['handler']
NEWSPIDER_MODULE = 'handler'

class Database(object):
	url = '127.0.0.1:3306'
	dbname = 'test'
	username = 'root'
	password = 'root'