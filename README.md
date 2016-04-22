# Crawler <small>-- A movie crawler and ranking project.</small>

### Directories

```
crawler/
   ├── core/
   │   ├── __init__.py
   │   ├── app.py
   │   ├── crawler.py
   │   ├── models.py
   │   ├── routes.py
   │   ├── settings.py
   │   └── views.py
   ├── env/
   ├── migrations/
   ├── spider/
   ├── static/
   ├── templates/
   │   ├── about.html
   │   └── index.html
   ├── tests/
   │   ├── __init__.py
   │   └── test.py
   ├── LICENSE
   ├── README.md
   ├── database.sqlite3
   ├── manage.py
   └── requirements.txt
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
scrapy runspider crawler.py -o result.json
```
