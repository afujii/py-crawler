# -*- coding: utf-8 -*-

import time
import hashlib
from flask import views, request
from core.models import db, User
from core.base import res


class LoginApi(views.MethodView):
    def post(self):
        params = request.form
        user = User.query.filter_by(
            username = params['username'],
            password = params['password']
        ).first()

        if user is None:
            return res(404)
        else:
            return res(200, {
                'auth_key': hashlib.sha1(user.username).hexdigest()
            })


class RegisterApi(views.MethodView):
    def post(self):
        params = request.form
        user = User(
            username = params['username'],
            password = params['password']
        )
        db.session.add(user)
        db.session.commit()
        return res(200, {
            'auth_user': user.username
        })
