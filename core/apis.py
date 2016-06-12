# -*- coding: utf-8 -*-

import time
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
            return res(200, user)


class RegisterApi(views.MethodView):
    def post(self):
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()
        return res(200)
