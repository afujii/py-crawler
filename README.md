# Crawler <small>-- A movie crawler and ranking project.</small>

### Directories

```
crawler/
    ├── core
    │   ├── migrations
    │   ├── static
    │   ├── templates
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes.py
    │   ├── settings.py
    │   └── views.py
    ├── crawler
    │   ├── outputs
    │   ├── spiders
    │   ├── __init__.py
    │   ├── cron.py
    │   ├── items.py
    │   ├── pipelines.py
    │   └── settings.py
    ├── env
    │   ├── bin
    │   ├── include
    │   ├── lib
    │   └── pip-selfcheck.json
    ├── tests
    │   ├── __init__.py
    │   └── test.py
    ├── LICENSE
    ├── README.md
    ├── crawlercron
    ├── manage.py
    ├── requirements.txt
    └── scrapy.cfg
```

### How To Use

``` bash
# 0. enable virtualenv
virtualenv env && source env/bin/activate

# 1. install dependencies
pip install -r requirements.txt

# 2. migrate database
python manage.py migrate

# 3. run spiders
python manage.py runcron

# 4. run server
python manage.py runserver

# 5. erase database
python manage.py dropdb
```

# How to use Linux system cron

``` bash
# add env variable
echo 'export EDITOR="vi"' >> ~/.bashrc && source ~/.bashrc

# list system cron
crontab -l

# add system cron
crontab crawlercron

# delete system cron
crontab -r
```

### How to use Scrapy (no need, use `python manage.py runcron` instead)

``` bash
scrapy crawl douban -o crawler/outputs/douban.json
```

### How to generate dir tree

```
tree -L 2 -I '*pyc' --dirsfirst
```
