import scrapy
from amazon.items import AmazonItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

"""==========================================================================================="""
"""=======================================BEGIN SPIDERS======================================="""
"""==========================================================================================="""

class Innerwear(scrapy.Spider):
	"""MENS INNERWEAR"""
	
	name = "clothing1"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1968126031_pg_1?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968126031&page=1&ie=UTF8&qid=1470242868"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1968126031_pg_{pagenum}?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968126031&page={pagenum}&ie=UTF8&qid=1470242868'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-row a-spacing-none"]/a/@href')
		if self.next_page <= 50:
			for href in ulink:
				uRl = response.urljoin(href.extract())
				yield scrapy.Request(uRl, callback=self.parse_products, meta={'url':href.extract()})
			self.next_page += 1
			yield self.create_ajax_request(self.next_page)

	def parse_products(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AmazonItem()
		item['title'] = hxs.select('//div[@class="a-section a-spacing-none"]/h1/span[@id="productTitle"]/text()').extract()
		item['brand'] = hxs.select('//a[@id="brand"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Clothing & Accessories"
		item['subcategory'] = "Men's Innerwear"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class WomensIntimate(scrapy.Spider):
	"""WOMENS INTIMATE APPAREL"""
	
	name = "clothing2"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4725138031_pg_1?rh=n%3A1571271031%2Cn%3A%211571273031%2Cn%3A%211975997031%2Cn%3A4725138031&page=1&ie=UTF8&qid=1470242869"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4725138031_pg_{pagenum}?rh=n%3A1571271031%2Cn%3A%211571273031%2Cn%3A%211975997031%2Cn%3A4725138031&page={pagenum}&ie=UTF8&qid=1470242869'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-row a-spacing-none"]/a/@href')
		if self.next_page <= 50:
			for href in ulink:
				uRl = response.urljoin(href.extract())
				yield scrapy.Request(uRl, callback=self.parse_products, meta={'url':href.extract()})
			self.next_page += 1
			yield self.create_ajax_request(self.next_page)

	def parse_products(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AmazonItem()
		item['title'] = hxs.select('//div[@class="a-section a-spacing-none"]/h1/span[@id="productTitle"]/text()').extract()
		item['brand'] = hxs.select('//a[@id="brand"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Clothing & Accessories"
		item['subcategory'] = "Women's Intimate Apparel"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Kids(scrapy.Spider):
	"""KIDS"""
	
	name = "clothing3"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4091091031_pg_1?rh=n%3A1571271031%2Cn%3A%211571273031%2Cn%3A%211975997031%2Cn%3A4091091031&page=1&ie=UTF8&qid=1470242869"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4091091031_pg_{pagenum}?rh=n%3A1571271031%2Cn%3A%211571273031%2Cn%3A%211975997031%2Cn%3A4091091031&page={pagenum}&ie=UTF8&qid=1470242869'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-row a-spacing-none"]/a/@href')
		if self.next_page <= 50:
			for href in ulink:
				uRl = response.urljoin(href.extract())
				yield scrapy.Request(uRl, callback=self.parse_products, meta={'url':href.extract()})
			self.next_page += 1
			yield self.create_ajax_request(self.next_page)

	def parse_products(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AmazonItem()
		item['title'] = hxs.select('//div[@class="a-section a-spacing-none"]/h1/span[@id="productTitle"]/text()').extract()
		item['brand'] = hxs.select('//a[@id="brand"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Clothing & Accessories"
		item['subcategory'] = "Kids"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Men(scrapy.Spider):
	"""MEN"""
	
	name = "clothing4"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1968024031_pg_1?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031&page=1&ie=UTF8&qid=1470242870"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1968024031_pg_{pagenum}?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031&page={pagenum}&ie=UTF8&qid=1470242870'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-row a-spacing-none"]/a/@href')
		if self.next_page <= 50:
			for href in ulink:
				uRl = response.urljoin(href.extract())
				yield scrapy.Request(uRl, callback=self.parse_products, meta={'url':href.extract()})
			self.next_page += 1
			yield self.create_ajax_request(self.next_page)

	def parse_products(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AmazonItem()
		item['title'] = hxs.select('//div[@class="a-section a-spacing-none"]/h1/span[@id="productTitle"]/text()').extract()
		item['brand'] = hxs.select('//a[@id="brand"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Clothing & Accessories"
		item['subcategory'] = "Men"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Women(scrapy.Spider):
	"""WOMEN"""
	
	name = "clothing5"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1953602031_pg_1?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1953602031&page=1&ie=UTF8&qid=1470242872"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1953602031_pg_{pagenum}?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1953602031&page={pagenum}&ie=UTF8&qid=1470242872'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-row a-spacing-none"]/a/@href')
		if self.next_page <= 50:
			for href in ulink:
				uRl = response.urljoin(href.extract())
				yield scrapy.Request(uRl, callback=self.parse_products, meta={'url':href.extract()})
			self.next_page += 1
			yield self.create_ajax_request(self.next_page)

	def parse_products(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AmazonItem()
		item['title'] = hxs.select('//div[@class="a-section a-spacing-none"]/h1/span[@id="productTitle"]/text()').extract()
		item['brand'] = hxs.select('//a[@id="brand"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Clothing & Accessories"
		item['subcategory'] = "Women"
		items.append(item)
		return items

"""=======================================Spider End======================================="""









