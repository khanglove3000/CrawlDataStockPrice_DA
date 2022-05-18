from decimal import Clamped
from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

class Symbol(Base):
    __tablename__ = "symbol"
    id = Column(Integer, primary_key=True)
    name = Column('name', String(5), unique=True)
    urlsymbol = Column('urlsymbol', Text())


class HistoricalData(Base):
    __tablename__ = "historydata"
    id = Column(Integer, primary_key=True)
    date = Column('date', Text())
    open = Column('open', Text())
    high = Column('high', Text())
    low = Column('low', Text())
    close = Column('close', Text())
    #adjclose = Column('adjclose', Text())
    #volume = Column('volume', Text())
    #symbol = Column('symbol', Text())
    name = Column('name', Text())