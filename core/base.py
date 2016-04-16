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


x = Ranking(title='测试电影', pic_url='139.129.35.112',
	point=9.9, description='sfdfghjk', ranking=1, source=1, crawl_time=12345678)

merge(x)