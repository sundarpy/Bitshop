import scrapy
from amazon.items import AmazonItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

"""==========================================================================================="""
"""=======================================BEGIN SPIDERS======================================="""
"""==========================================================================================="""

class Puzzles(scrapy.Spider):
	"""PUZZLES"""
	
	name = "toys1"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1378470031_pg_1?rh=n%3A1350380031%2Cn%3A%211350381031%2Cn%3A1378470031&page=1&ie=UTF8&qid=1470233193"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1378470031_pg_{pagenum}?rh=n%3A1350380031%2Cn%3A%211350381031%2Cn%3A1378470031&page={pagenum}&ie=UTF8&qid=1470233193'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['sellingprice'] = hxs.select('//span[@class="a-text-strike"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@class="content pdClearfix"]//node()').extract()
		item['image'] = hxs.select('//div[@class="imgTagWrapper"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//span[@class="a-icon-alt"]/text()')[3].extract()
		item['COD'] = hxs.select('//span[@id="cod_eligible_message"]//text()').extract()
		item['category'] = "Toys & Baby Products"
		item['subcategory'] = "Puzzles"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class SoftToys(scrapy.Spider):
	"""SOFT TOYS"""
	
	name = "toys2"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1378445031_pg_1?rh=n%3A1350380031%2Cn%3A%211350381031%2Cn%3A1378445031&page=1&ie=UTF8&qid=1470233194"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1378445031_pg_{pagenum}?rh=n%3A1350380031%2Cn%3A%211350381031%2Cn%3A1378445031&page={pagenum}&ie=UTF8&qid=1470233194'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['sellingprice'] = hxs.select('//span[@class="a-text-strike"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@class="content pdClearfix"]//node()').extract()
		item['image'] = hxs.select('//div[@class="imgTagWrapper"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//span[@class="a-icon-alt"]/text()')[3].extract()
		item['COD'] = hxs.select('//span[@id="cod_eligible_message"]//text()').extract()
		item['category'] = "Toys & Baby Products"
		item['subcategory'] = "Soft Toys"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class DieCastToyVehicles(scrapy.Spider):
	"""DIE-CAST TOY VEHICLES"""
	
	name = "toys3"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1378242031_pg_1?rh=n%3A1350380031%2Cn%3A%211350381031%2Cn%3A1378242031&page=1&ie=UTF8&qid=1470233195"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1378242031_pg_{pagenum}?rh=n%3A1350380031%2Cn%3A%211350381031%2Cn%3A1378242031&page={pagenum}&ie=UTF8&qid=1470233195'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['sellingprice'] = hxs.select('//span[@class="a-text-strike"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@class="content pdClearfix"]//node()').extract()
		item['image'] = hxs.select('//div[@class="imgTagWrapper"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//span[@class="a-icon-alt"]/text()')[3].extract()
		item['COD'] = hxs.select('//span[@id="cod_eligible_message"]//text()').extract()
		item['category'] = "Toys & Baby Products"
		item['subcategory'] = "Die-Cast & Toy Vehicles"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class LearningEducation(scrapy.Spider):
	"""LEARNING & EDUCATION"""
	
	name = "toys4"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1378342031_pg_1?rh=n%3A1350380031%2Cn%3A%211350381031%2Cn%3A1378342031&page=1&ie=UTF8&qid=1470233195"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1378342031_pg_{pagenum}?rh=n%3A1350380031%2Cn%3A%211350381031%2Cn%3A1378342031&page={pagenum}&ie=UTF8&qid=1470233195'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['sellingprice'] = hxs.select('//span[@class="a-text-strike"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@class="content pdClearfix"]//node()').extract()
		item['image'] = hxs.select('//div[@class="imgTagWrapper"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//span[@class="a-icon-alt"]/text()')[3].extract()
		item['COD'] = hxs.select('//span[@id="cod_eligible_message"]//text()').extract()
		item['category'] = "Toys & Baby Products"
		item['subcategory'] = "Learning & Education"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Diapers(scrapy.Spider):
	"""DIAPERS"""
	
	name = "toys5"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1953345031_pg_1?rh=n%3A1571274031%2Cn%3A%211571275031%2Cn%3A1953345031&page=1&ie=UTF8&qid=1470233198"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1953345031_pg_{pagenum}?rh=n%3A1571274031%2Cn%3A%211571275031%2Cn%3A1953345031&page={pagenum}&ie=UTF8&qid=1470233198'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['sellingprice'] = hxs.select('//span[@class="a-text-strike"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@class="content pdClearfix"]//node()').extract()
		item['image'] = hxs.select('//div[@class="imgTagWrapper"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//span[@class="a-icon-alt"]/text()')[3].extract()
		item['COD'] = hxs.select('//span[@id="cod_eligible_message"]//text()').extract()
		item['category'] = "Toys & Baby Products"
		item['subcategory'] = "Diapering & Nappy Changing"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Bedding(scrapy.Spider):
	"""BEDDING"""
	
	name = "toys6"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1953359031_pg_1?rh=n%3A1571274031%2Cn%3A%211571275031%2Cn%3A1953359031&page=1&ie=UTF8&qid=1470233198"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1953359031_pg_{pagenum}?rh=n%3A1571274031%2Cn%3A%211571275031%2Cn%3A1953359031&page={pagenum}&ie=UTF8&qid=1470233198'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['sellingprice'] = hxs.select('//span[@class="a-text-strike"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@class="content pdClearfix"]//node()').extract()
		item['image'] = hxs.select('//div[@class="imgTagWrapper"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//span[@class="a-icon-alt"]/text()')[3].extract()
		item['COD'] = hxs.select('//span[@id="cod_eligible_message"]//text()').extract()
		item['category'] = "Toys & Baby Products"
		item['subcategory'] = "Bedding, Furniture & Room Decor"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Strollers(scrapy.Spider):
	"""STROLLERS"""
	
	name = "toys7"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1953480031_pg_1?rh=n%3A1571274031%2Cn%3A%211571275031%2Cn%3A1953480031&page=1&ie=UTF8&qid=1470233199"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1953480031_pg_{pagenum}?rh=n%3A1571274031%2Cn%3A%211571275031%2Cn%3A1953480031&page={pagenum}&ie=UTF8&qid=1470233199'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['sellingprice'] = hxs.select('//span[@class="a-text-strike"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@class="content pdClearfix"]//node()').extract()
		item['image'] = hxs.select('//div[@class="imgTagWrapper"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//span[@class="a-icon-alt"]/text()')[3].extract()
		item['COD'] = hxs.select('//span[@id="cod_eligible_message"]//text()').extract()
		item['category'] = "Toys & Baby Products"
		item['subcategory'] = "Strollers & Prams"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Feeding(scrapy.Spider):
	"""FEEDING"""
	
	name = "toys8"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1953448031_pg_1?rh=n%3A1571274031%2Cn%3A%211571275031%2Cn%3A1953448031&page=1&ie=UTF8&qid=1470233200"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1953448031_pg_{pagenum}?rh=n%3A1571274031%2Cn%3A%211571275031%2Cn%3A1953448031&page={pagenum}&ie=UTF8&qid=1470233200'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['sellingprice'] = hxs.select('//span[@class="a-text-strike"]/text()').extract()
		item['offerprice'] = hxs.select('//span[@id="priceblock_ourprice"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="fbExpandableSection"]//node()').extract()
		item['image'] = hxs.select('//div[@class="imgTagWrapper"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//span[@class="a-icon-alt"]/text()')[3].extract()
		item['COD'] = hxs.select('//span[@id="cod_eligible_message"]//text()').extract()
		item['category'] = "Toys & Baby Products"
		item['subcategory'] = "Feeding"
		items.append(item)
		return items

"""=======================================Spider End======================================="""









