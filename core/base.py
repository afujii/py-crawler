# -*- coding: utf-8 -*-

from orm import *

def merge(obj):
    try:
        session = DB_Session()
        session.merge(obj)
        session.commit()
    except Exception, e:
        print e
    else:
        pass
    finally:
        session.close()
