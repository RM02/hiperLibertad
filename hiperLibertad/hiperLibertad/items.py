# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HiperlibertadItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    oldprice = scrapy.Field()
    category = scrapy.Field()
    sku = scrapy.Field()
    url = scrapy.Field()
    stock = scrapy.Field()
    description = scrapy.Field()
