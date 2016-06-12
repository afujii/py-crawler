# -*- coding: utf-8 -*-

from flask import views, request
from core.models import User
from core.base import res


class LoginApi(views.MethodView):
    def post(self):
        params = request.form
        u = User.query.filter_by(
            username = params['username'],
            password = params['password']).first()
        if u is None:
            return res(-1)
        else:
            return res(200, u)


class RegisterApi(views.MethodView):
    def post(self):
        u = User(**request.form)
        u.is_expired = 0
        u.register_time = time.time()*1000
        db.session.add(u)
        db.session.commit()
        return res(200)
