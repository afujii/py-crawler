from sqlalchemy import Column, String, Float, Integer, BigInteger, create_engine, types
from sqlalchemy.ext.declarative import declarative_base

# Declarative base class instance
Base = declarative_base()

# Database Schema
class Ranking(Base):
    __tablename__ = 'ranking'

    id = Column(Integer, primary_key=True)
    title = Column(String(20)) # 标题
    pic_url = Column(String(200)) # 图片链接
    point = Column(Float) # 评分
    description = Column(String(1000)) # 描述
    ranking = Column(Integer) # 排名
    source = Column(Integer) # 来源
    crawl_time = Column(BigInteger) # 爬取时间

class Movies(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(20)) # 电影名
    pic_url = Column(String(200)) # 图片链接
    point = Column(Float) # 评分
    description = Column(String(1000)) # 描述
    type = Column(Integer) # 上映否？即将上映、已经上映
    classify = Column(Integer) # 分类
    director = Column(String(100)) # 导演
    actor = Column(String(200)) # 演员
    release_time = Column(BigInteger) # 上映时间
    urls = Column(String(2000)) # 电影相关链接
    source = Column(Integer) # 来源
    crawl_time = Column(BigInteger) # 爬取时间

class Source(Base):
    __tablename__ = 'source'

    id = Column(Integer, primary_key=True)
    name = Column(String(200)) # 电影名称
    url = Column(String(200)) # 网站链接
