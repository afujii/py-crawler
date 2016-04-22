# Crawler <small>-- A movie crawler and ranking project.</small>

### Directories

```
crawler/
    ├── core
    │   ├── __init__.py
    │   ├── app.py
    │   ├── models.py
    │   ├── routes.py
    │   ├── settings.py
    │   └── views.py
    ├── crawler
    │   ├── spiders
    │   ├── __init__.py
    │   ├── items.py
    │   ├── pipelines.py
    │   └── settings.py
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

```
tree -L 2 -I '*pyc' --dirsfirst
```
