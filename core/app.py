from flask import Flask

DEBUG = True
SECRET_KEY = 'crawler'

app = Flask('crawler')
app.config.from_object(__name__)
