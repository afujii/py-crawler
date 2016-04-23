# Crawler <small>-- A movie crawler and ranking project.</small>

### Directories

``` bash
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

### How to install

``` bash
# 1. install non-python dependencies
crawler$ sudo apt-get install python-dev python-pip \
    libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

# 2. enable virtualenv
crawler$ virtualenv env
crawler$ source env/bin/activate

# 3. install python dependencies
(env)crawler$ cat requirements.txt
  Flask
  Flask-Script
  Flask-SQLAlchemy
  Scrapy
  # Flask-Cache
  # blinker
  # markdown
(env)crawler$ pip install -r requirements.txt
```

### How To Use

``` bash
# 1. migrate database
# use sqlite3 database at /tmp/crawler.sqlite3
(env)crawler$ python manage.py migrate

# 2. run spiders
# can also use `scrapy crawl`
(env)crawler$ python manage.py runcron

# 3. run server
# visit http://localhost:2333/
(env)crawler$ python manage.py runserver

# 4. erase all database tables
(env)crawler$ python manage.py dropdb
```

### How to use Linux system cron (optional)

``` bash
# add env variable
crawler$ echo 'export EDITOR="vi"' >> ~/.bashrc
crawler$ source ~/.bashrc

# list system cron
crawler$ crontab -l

# add system cron
# cron file name should be: name + 'cron'
crawler$ cat crawlercron
  # Cron 命令顺序
  # 分 0-59
  # 时 0-23
  # 日 1-31
  # 月 1-12
  # 周 0-6 周日开始
  # 命令

  # 每 30 分钟执行一次
  # 30 * * * * source /path/to/project/env/bin/active && python /path/to/project/manage.py runcron
crawler$ crontab crawlercron

# delete system cron
crawler$ crontab -r
```

### How to use Scrapy (optional, use `python manage.py runcron` instead)

``` bash
(env)crawler$ scrapy crawl douban -o crawler/outputs/douban.json
```

### How to generate dir tree

``` bash
crawler$ tree -L 2 -I '*pyc' --dirsfirst
```
