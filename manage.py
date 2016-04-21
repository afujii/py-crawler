#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Server, Shell, Manager, prompt_bool
from core import app, models


# create manager
manager = Manager(app.app)


# run the app
manager.add_command('runserver', Server('0.0.0.0', port=2333))


# enter shell env
def _make_context():
    return dict(db=models.db)
manager.add_command('shell', Shell(make_context=_make_context))


# migrate models into database
@manager.command
def migrate():
    models.db.create_all()


# erase database
@manager.command
def erase():
    if prompt_bool('Drop database?'):
        models.db.drop_all()


# run the manager
if __name__ == '__main__':
    manager.run()
