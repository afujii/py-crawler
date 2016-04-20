# -*- coding: utf-8 -*-

__author__ = 'HowardWong'

from settings import DATABASE
from sqlalchemy.orm import sessionmaker

# Database Config
def get_engine():
    tpl = 'mysql+mysqldb://{username}:{password}@{host}:{port}/{dbname}?charset=utf8'
    return create_engine(tpl.format(**DATABASE), echo=True)

def init_db(engine):
    Base.metadata.create_all(engine)

def drop_db(engine):
    Base.metadata.drop_all(engine)

db_engine = get_engine()
db_session = sessionmaker(bind=db_engine)

init_db(db_engine)
