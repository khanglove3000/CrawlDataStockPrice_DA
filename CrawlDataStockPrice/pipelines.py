# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from symtable import Symbol
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
# useful for handling different item types with a single interface
import sqlite3
from models import *

class CrawldatastockpricePipeline:
    def process_item(self, item, spider):
        return item

class SaveSymbolPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        symbol = Symbol()
        symbol.name = item['symbol']
        symbol.urlsymbol = item['urlsymbol']
        try:
            session.add(symbol)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item

class LoadSymbol(object):
    # Database Connectivity
    def connectDB():
        try:
            con = sqlite3.connect("cafef.db")
            cursor = con.cursor()
            print("Connected to Database Successfully")
            #Data fetching Process-(One Record)
            query = "SELECT * from symbol"
            x = cursor.execute(query).fetchall()
            print("Executed")
            return x
        except:
            print("Database Error")

