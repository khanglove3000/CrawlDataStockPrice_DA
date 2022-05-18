# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,  Field
import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime

def remove_quotes(text):
    # strip the unicode quotes
    return text


class CafefItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    
class Symbol(scrapy.Item):
    symbol = scrapy.Field(
        input_processor=MapCompose(remove_quotes),
        # TakeFirst return the first value not the whole list
        output_processor=TakeFirst()
    )
    urlsymbol = scrapy.Field(
        input_processor=MapCompose(remove_quotes),
        # TakeFirst return the first value not the whole list
        output_processor=TakeFirst()
    )
  
class HistoryDataCafef(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    date = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    close = scrapy.Field()
    # adjclose = scrapy.Field()
    # volume = scrapy.Field()
    pass