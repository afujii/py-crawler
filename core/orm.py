# -*- coding: utf-8 -*-

__author__ = 'HowardWong'

from settings import Database
from sqlalchemy import Column, String, Float, Date, Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)


def get_url(db):
	return 'mysql+mysqlconnector://' \
	+ db.username +':' + db.password \
	+ '@' + db.url + '/' + db.dbname

#Init
Base = declarative_base()

#Init DataBase Reflect
class Ranking(Base):
	__tablename__ = 'ranking'

	id = Column(Integer, primary_key=True)
	title = Column(String(20)) # 标题
	pic_url = Column(String(200)) # 图片链接
	point = Column(Float) # 评分
	description = Column(String(1000)) # 描述
	ranking = Column(Integer) # 排名

class Movies(Base):
	__tablename__ = 'Movies'

	id = Column(Integer, primary_key=True)
	title = Column(String(20)) # 电影名
	pic_url = Column(String(200)) # 图片链接
	point = Column(Float) # 评分
	description = Column(String(1000)) # 描述
	type = Column(Integer) # 上映否？即将上映、已经上映
	classify = Column(Integer) # 分类
	director = Column(String(100)) # 导演
	actor = Column(String(200)) # 演员
	release_time = Column(Date) # 上映时间



engine = create_engine(get_url(Database()), echo=True)
init_db()
