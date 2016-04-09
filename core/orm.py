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
	title = Column(String(20))
	pic_url = Column(String(200))
	point = Column(Float)
	description = Column(String(1000))
	ranking = Column(Integer)

class Movies(Base):
	__tablename__ = 'Movies'

	id = Column(Integer, primary_key=True)
	title = Column(String(20))
	pic_url = Column(String(200))
	point = Column(Float)
	description = Column(String(1000))
	type = Column(Integer)
	classify = Column(Integer)
	director = Column(String(100))
	actor = Column(String(200))
	release_time = Column(Date)



engine = create_engine(get_url(Database()), echo=True)
init_db()