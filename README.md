# Crawler <small>-- A movie crawler and ranking project.</small>

### Directories

```
crawler/
    ├── core
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── app.py
    │   ├── app.pyc
    │   ├── models.py
    │   ├── models.pyc
    │   ├── routes.py
    │   ├── routes.pyc
    │   ├── settings.py
    │   ├── settings.pyc
    │   ├── views.py
    │   └── views.pyc
    ├── crawler
    │   ├── spiders
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── items.py
    │   ├── items.pyc
    │   ├── pipelines.py
    │   ├── settings.py
    │   └── settings.pyc
    ├── env
    │   ├── bin
    │   ├── include
    │   ├── lib
    │   └── pip-selfcheck.json
    ├── migrations
    ├── outputs
    │   └── douban.json
    ├── static
    ├── templates
    │   ├── about.html
    │   └── index.html
    ├── tests
    │   ├── __init__.py
    │   └── test.py
    ├── LICENSE
    ├── README.md
    ├── database.sqlite3
    ├── manage.py
    ├── manage.pyc
    ├── requirements.txt
    └── scrapy.cfg
```

### How To Use

``` bash
# install dependencies
pip install -r requirements.txt

# run server
python manage.py runserver

# migrate database
python manage.py migrate

# erase database
python manage.py erase
```

### How to run spider

``` bash
scrapy crawl douban -o outputs/douban.json
```


### How to generate dir tree
