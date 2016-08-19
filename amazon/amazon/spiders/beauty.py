import scrapy
from amazon.items import AmazonItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

"""==========================================================================================="""
"""=======================================BEGIN SPIDERS======================================="""
"""==========================================================================================="""

class Fragrance(scrapy.Spider):
	"""FRAGRANCE"""
	
	name = "beauty1"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1374298031_pg_1?rh=n%3A1355016031%2Cn%3A%211355017031%2Cn%3A1374298031&page=1&ie=UTF8&qid=1470241674"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1374298031_pg_{pagenum}?rh=n%3A1355016031%2Cn%3A%211355017031%2Cn%3A1374298031&page={pagenum}&ie=UTF8&qid=1470241674'
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
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Beauty, Health & Gourmet"
		item['subcategory'] = "Fragrance"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class DietNutrition(scrapy.Spider):
	"""DIET & NUTRITION"""
	
	name = "beauty2"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1374489031_pg_1?rh=n%3A1350384031%2Cn%3A%211350385031%2Cn%3A1374489031&page=1&ie=UTF8&qid=1470241676"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1374489031_pg_{pagenum}?rh=n%3A1350384031%2Cn%3A%211350385031%2Cn%3A1374489031&page={pagenum}&ie=UTF8&qid=1470241676'
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
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Beauty, Health & Gourmet"
		item['subcategory'] = "Diet & Nutrition"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class HouseholdSupplies(scrapy.Spider):
	"""HOUSEHOLD SUPPLIES"""
	
	name = "beauty3"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1374515031_pg_1?rh=n%3A1350384031%2Cn%3A%211350385031%2Cn%3A1374515031&page=1&ie=UTF8&qid=1470241677"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1374515031_pg_{pagenum}?rh=n%3A1350384031%2Cn%3A%211350385031%2Cn%3A1374515031&page={pagenum}&ie=UTF8&qid=1470241677'
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
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Beauty, Health & Gourmet"
		item['subcategory'] = "Household Supplies"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class PersonalCare(scrapy.Spider):
	"""PERSONAL CARE"""
	
	name = "beauty4"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_3150028031_pg_1?rh=n%3A1350384031%2Cn%3A%211350385031%2Cn%3A3150026031%2Cn%3A3150028031&page=1&ie=UTF8&qid=1470241678"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_3150028031_pg_{pagenum}?rh=n%3A1350384031%2Cn%3A%211350385031%2Cn%3A3150026031%2Cn%3A3150028031&page={pagenum}&ie=UTF8&qid=1470241678'
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
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Beauty, Health & Gourmet"
		item['subcategory'] = "Personal Care"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class HealthCareDevices(scrapy.Spider):
	"""HEALTH CARE DEVICES"""
	
	name = "beauty5"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_3150027031_pg_1?rh=n%3A1350384031%2Cn%3A%211350385031%2Cn%3A3150026031%2Cn%3A3150027031&page=1&ie=UTF8&qid=1470241679"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_3150027031_pg_{pagenum}?rh=n%3A1350384031%2Cn%3A%211350385031%2Cn%3A3150026031%2Cn%3A3150027031&page={pagenum}&ie=UTF8&qid=1470241679'
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
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Beauty, Health & Gourmet"
		item['subcategory'] = "Health Care Devices"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class MensGrooming(scrapy.Spider):
	"""MENS GROOMING"""
	
	name = "beauty6"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_5122801031_pg_1?rh=n%3A1350384031%2Cn%3A%211499773031%2Cn%3A%211499774031%2Cn%3A5122801031&page=1&ie=UTF8&qid=1470241680"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_5122801031_pg_{pagenum}?rh=n%3A1350384031%2Cn%3A%211499773031%2Cn%3A%211499774031%2Cn%3A5122801031&page={pagenum}&ie=UTF8&qid=1470241680'
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
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Beauty, Health & Gourmet"
		item['subcategory'] = "Men's Grooming"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class CoffeeTeaBeverage(scrapy.Spider):
	"""COFFEE TEA & BEVERAGES"""
	
	name = "beauty7"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4859478031_pg_1?rh=n%3A2454178031%2Cn%3A%212454179031%2Cn%3A4859478031&page=1&ie=UTF8&qid=1470241688"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4859478031_pg_{pagenum}?rh=n%3A2454178031%2Cn%3A%212454179031%2Cn%3A4859478031&page={pagenum}&ie=UTF8&qid=1470241688'
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
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Beauty, Health & Gourmet"
		item['subcategory'] = "Coffee, Tea & Beverages"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class SnackFoods(scrapy.Spider):
	"""SNACK FOODS"""
	
	name = "beauty8"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4859498031_pg_1?rh=n%3A2454178031%2Cn%3A%212454179031%2Cn%3A4859498031&page=1&ie=UTF8&qid=1470241689"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4859498031_pg_{pagenum}?rh=n%3A2454178031%2Cn%3A%212454179031%2Cn%3A4859498031&page={pagenum}&ie=UTF8&qid=1470241689'
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
		item['description'] = hxs.select('//div[@id="productDescription"]//text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Beauty, Health & Gourmet"
		item['subcategory'] = "Snack Foods"
		items.append(item)
		return items

"""=======================================Spider End======================================="""





