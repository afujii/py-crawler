# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from orm import *

DB_Session = sessionmaker(bind=engine)
def merge(obj):
	try:
		session = DBSession()
		session.merge(obj)
		session.commit()
	except Exception, e:
		print e
	else:
		pass
	finally:
		session.close()
