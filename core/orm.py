# -*- coding: utf-8 -*-

__author__ = 'HowardWong'

from settings import Database
from sqlalchemy import Column, String, Integer,create_engine
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
	name = Column(String(20))
	ranking = Column(Integer)

engine = create_engine(get_url(Database()), echo=True)
init_db()