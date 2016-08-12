# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Field

class AmazonItem(scrapy.Item):
	title = scrapy.Field()
	sellingprice = scrapy.Field()
	offerprice = scrapy.Field()
	saleprice = scrapy.Field()
	description = scrapy.Field()
	image = scrapy.Field()
	link = scrapy.Field()
	seller = scrapy.Field()
	sellrating = scrapy.Field()
	starating = scrapy.Field()
	COD = scrapy.Field()
	category = scrapy.Field()
	subcategory = scrapy.Field()