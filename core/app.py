import Flask

DEBUG = true
SECRECT_KEY = 'ha...ha...ha'

app = Flask(__name__)
app.config.from_object(__name__)
