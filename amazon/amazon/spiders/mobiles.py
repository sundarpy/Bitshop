import scrapy
from amazon.items import AmazonItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

"""==========================================================================================="""
"""=======================================BEGIN SPIDERS======================================="""
"""==========================================================================================="""

class AndroidMobiles(scrapy.Spider):
	"""ANDROID MOBILES"""
	
	name = "mobiles1"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4916280031_pg_1?rh=n%3A976419031%2Cn%3A%211499770031%2Cn%3A%211499772031%2Cn%3A4916280031&page=1&ie=UTF8&qid=1470213455"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4916280031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%211499770031%2Cn%3A%211499772031%2Cn%3A4916280031&page={pagenum}&ie=UTF8&qid=1470213455'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Mobiles & Tablets"
		item['subcategory'] = "Android Mobiles"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class WindowsMobiles(scrapy.Spider):
	"""WINDOWS MOBILES"""
	
	name = "mobiles2"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4916281031_pg_1?rh=n%3A976419031%2Cn%3A%211499770031%2Cn%3A%211499772031%2Cn%3A4916281031&page=1&ie=UTF8&qid=1470213457"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4916281031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%211499770031%2Cn%3A%211499772031%2Cn%3A4916281031&page={pagenum}&ie=UTF8&qid=1470213457'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Mobiles & Tablets"
		item['subcategory'] = "Windows Mobiles"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class MobileAccessories(scrapy.Spider):
	"""MOBILE ACCESSORIES"""
	
	name = "mobiles3"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389402031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389402031&page=1&ie=UTF8&qid=1470219583"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389402031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389402031&page={pagenum}&ie=UTF8&qid=1470219583'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Mobiles & Tablets"
		item['subcategory'] = "Mobile Accessories"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Tablets(scrapy.Spider):
	"""TABLETS"""
	
	name = "mobiles4"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1375458031_pg_1?rh=n%3A976392031%2Cn%3A%21976393031%2Cn%3A1375458031&page=1&ie=UTF8&qid=1470219686"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1375458031_pg_{pagenum}?rh=n%3A976392031%2Cn%3A%21976393031%2Cn%3A1375458031&page={pagenum}&ie=UTF8&qid=1470219686'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Mobiles & Tablets"
		item['subcategory'] = "Tablets"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class TabletAccessories(scrapy.Spider):
	"""TABLET ACCESSORIES"""
	
	name = "mobiles5"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1375328031_pg_1?rh=n%3A976392031%2Cn%3A%21976393031%2Cn%3A1375248031%2Cn%3A1375328031&page=1&ie=UTF8&qid=1470219790"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1375328031_pg_{pagenum}?rh=n%3A976392031%2Cn%3A%21976393031%2Cn%3A1375248031%2Cn%3A1375328031&page={pagenum}&ie=UTF8&qid=1470219790'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Mobiles & Tablets"
		item['subcategory'] = "Tablet Accessories"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class WearableDevices(scrapy.Spider):
	"""WEARABLE DEVICES"""
	
	name = "mobiles6"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_5571477031_pg_1?rh=n%3A976419031%2Cn%3A%211499770031%2Cn%3A%211499771031%2Cn%3A5571477031&page=1&ie=UTF8&qid=1470219778"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_5571477031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%211499770031%2Cn%3A%211499771031%2Cn%3A5571477031&page={pagenum}&ie=UTF8&qid=1470219778'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Mobiles & Tablets"
		item['subcategory'] = "Wearable Devices"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class LandlinePhones(scrapy.Spider):
	"""LANDLINE PHONES"""
	
	name = "mobiles7"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389490031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389481031%2Cn%3A1389490031&page=1&ie=UTF8&qid=1470219767"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389490031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389481031%2Cn%3A1389490031&page={pagenum}&ie=UTF8&qid=1470219767'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-section a-spacing-none a-inline-block s-position-relative"]/a/@href')
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
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Mobiles & Tablets"
		item['subcategory'] = "Wearable Devices"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

