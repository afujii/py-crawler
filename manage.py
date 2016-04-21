#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Server, Shell, Manager, Command, prompt_bool
from core.app import app
from core.models import db


manager = Manager(app)


manager.add_command('runserver', Server('0.0.0.0', port=2333))


def _make_context():
    return dict(db=db)
manager.add_command('shell', Shell(make_context=_make_context))


@manager.command
def migrate():
    db.create_all()


@manager.command
def erase():
    if prompt_bool('Drop database?'):
        db.drop_all()


if __name__ == '__main__':
    manager.run()
