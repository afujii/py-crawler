#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid

from flask import Flask, current_app
from flask.ext.script import Server, Shell, Manager, Command, prompt_bool

from core import app, database

manager = Manager(app)

def _make_context():
    return dict(db=db)
manager.add_command('shell', Shell(make_context=_make_context))

manager.add_command('runserver', Server('0.0.0.0', port=8080))

@manager.command
def migrage():
    database.create_all()

@manager.command
def dropdb():
    if prompt_bool('Drop database?'):
        database.drop_all()

if __name__ == '__main__':
    manager.run()
