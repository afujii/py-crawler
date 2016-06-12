# -*- coding: utf-8 -*-

from jsonpickle import encode


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
