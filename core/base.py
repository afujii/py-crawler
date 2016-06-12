# -*- coding: utf-8 -*-
from flask import request
import json, uuid, os
from jsonpickle import encode
from core.orm import User, Blog
from app import config

path = os.path.join(os.path.abspath('.'), 'file')

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS
def save_file(file):
  newname = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
  file.save(os.path.join(path, newname))
  return newname
# preposition handler
def request_body(func):
  def wrapper(*args, **kw):
    params = {}
    if request.args:
      params = request.args
    elif request.form:
      params = request.form
    return func(params, *args, **kw)
  return wrapper
# filter extra attribute in objects extends flask.ext.SQLAlchemy
extra_attr = [
  '_sa_instance_state'
]
def remove_extra_attr(obj):
  if isinstance(obj, dict):
    for e in obj:
      remove_extra_attr(obj[e])
  elif isinstance(obj, list):
    for e in obj:
      remove_extra_attr(e)
  else:
    for attr in extra_attr:
      if hasattr(obj, attr):
        obj.__delattr__(attr)
def res(status, data=None, message=None):
  r = {'status' : status}
  if data:
    remove_extra_attr(data)
    r['data'] = data
  if message:
    r['message'] = message
  return encode(r, unpicklable=False, max_depth=5)
