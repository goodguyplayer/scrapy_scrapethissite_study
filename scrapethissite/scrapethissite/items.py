# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import w3lib.html


class ScrapethissiteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CountryItem(scrapy.Item):
    name = scrapy.Field()
    capital = scrapy.Field()
    population = scrapy.Field()
    area = scrapy.Field()