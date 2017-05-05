# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PronlolItem(scrapy.Item):
    title = scrapy.Field()
    videolink = scrapy.Field()
    playcount = scrapy.Field()
    tags = scrapy.Field()
    pass
