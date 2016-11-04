import scrapy
from amazon.items import *
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

"""==========================================================================================="""
"""=======================================BEGIN SPIDERS======================================="""
"""==========================================================================================="""

class OfferItemX(scrapy.Spider):
	"""Main Offer Item"""
	name = "offer1"
	allowed_domains = ["amazon.in"]
	start_urls = ["http://www.amazon.in/"]

	def parse(self, response):
		mainlink = response.selector.xpath('//div[@class="cropped-image-map-center-alignment"]/span')
		items = []
		for i in mainlink:
			item = OfferItem()
			item['image'] = i.xpath('a/img/@src').extract()
			item['link'] = i.xpath('a/@href').extract()
			items.append(item)
		return items

"""=======================================Spider End======================================="""

class OfferItemY(scrapy.Spider):
	"""Limited Offer Item"""
	name = "offer2"
	allowed_domains = ["amazon.in"]
	start_urls = ["http://www.amazon.in/"]

	def parse(self, response):
		main = response.selector.xpath('//div[@class="billboard"]')
		items = []
		for j in main:
			item = OfferItem()
			item['image'] = j.xpath('div/a/img/@src').extract()
			item['link'] = j.xpath('div/a/@href').extract()
			items.append(item)
		return items

"""=======================================Spider End======================================="""









