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


class HockeyTeamItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    wins = scrapy.Field()
    losses = scrapy.Field()
    ot_losses = scrapy.Field()
    win_perc = scrapy.Field()
    goals_for = scrapy.Field()
    goals_against = scrapy.Field()
    more_less = scrapy.Field()


class FilmItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
    awards = scrapy.Field()
    nominations = scrapy.Field()
    best_picture = scrapy.Field()