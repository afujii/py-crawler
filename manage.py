#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server, Shell, prompt_bool
from core import app, db
from core.routes import site
from crawler.runner import run_spiders


# 注册路由
app.register_blueprint(site)


# 创建 Manager 实例
manager = Manager(app)


# 启动服务器
manager.add_command('runserver', Server('0.0.0.0', port=2333))


# 进入交互式命令模式
manager.add_command('shell', Shell(make_context=lambda: dict(
    app=app,
    db=db,
    routes=site,
    run_spiders=run_spiders,
)))


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
