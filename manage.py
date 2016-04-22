#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Server, Shell, Manager, prompt_bool
from core import app
from core.models import db
from crawler.cron import run_spiders
from core.routes import site


app.register_blueprint(site)


# 创建 Manager 实例
manager = Manager(app)


# 启动服务器
manager.add_command('runserver', Server('0.0.0.0', port=2333))


# 进入交互式命令模式
def _make_context():
    return dict(db=db)
manager.add_command('shell', Shell(make_context=_make_context))


# 创建表结构
@manager.command
def migrate():
    db.create_all()


# 删除数据库
@manager.command
def dropdb():
    if prompt_bool('Drop database?'):
        db.drop_all()


# 执行定时任务
@manager.command
def runcron():
    # the script will block here until all crawling jobs are finished
    run_spiders()


# 启动服务
if __name__ == '__main__':
    manager.run()
