# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class DmozItem(scrapy.Item):
	title = scrapy.Field()
        area = scrapy.Field()
        age = scrapy.Field()
        quality = scrapy.Field()
	shape = scrapy.Field()
	project = scrapy.Field()
	price  = scrapy.Field()
	env = scrapy.Field()
	security = scrapy.Field()
	image_urls = scrapy.Field()
        images = scrapy.Field()
        pass
