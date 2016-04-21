# -*- coding: utf-8 -*-

import sys, os
from apscheduler.schedulers.blocking import BlockingScheduler


# 在这里配置任务
task_list = [
    {'name':'test','corn':'0 0 23 * * *'},
]


def crawl(name):
    def func():
        os.system('scrapy crawl ' + name)
    return func


def format_cron(cron):
    cron_tuple = cron.split(' ')
    return {
        'second':cron_tuple[0],
        'minute':cron_tuple[1],
        'hour':cron_tuple[2],
        'day':cron_tuple[3],
        'month':cron_tuple[4],
        'week':cron_tuple[5]
    }


def run():
    # path = sys.path[0]
    scheduler = BlockingScheduler()
    for task in task_list:
        scheduler.add_job(crawl(task.get('name')), 'cron', **format_cron(task.get('corn')))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
