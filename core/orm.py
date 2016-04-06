# -*- coding: utf-8 -*-

__author__ = 'HowardWong'

import sys
sys.path.append('..')
from sqlalchemy import Column, String, Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

class Database(object):
	url = '127.0.0.1:3306'
	dbname = 'test'
	username = 'root'
	password = 'root'

def get_url(db):
	return 'mysql+mysqlconnector://'
	+ db.username +':' + db.password
	+ '@' + db.url + '/' + db.dbname

Base = declarative_base()

#Init DataBase Invoke
class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(20))


engine = create_engine(get_url(Database()), echo=True)
DB_Session = sessionmaker(bind=engine)
init_db()