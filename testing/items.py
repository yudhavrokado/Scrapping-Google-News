# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()\
    titel = scrapy.Field()
    date_post = scrapy.Field()
    link = scrapy.Field()
    scrape_date = scrapy.Field()
    pass
