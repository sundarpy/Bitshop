import scrapy
from amazon.items import AmazonItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

"""==========================================================================================="""
"""=======================================BEGIN SPIDERS======================================="""
"""==========================================================================================="""

class DigitalSLRs(scrapy.Spider):
	"""DSLRS"""
	
	name = "cameras1"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389177031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389175031%2Cn%3A1389177031&page=1&ie=UTF8&qid=1470227401"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389177031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389175031%2Cn%3A1389177031&page={pagenum}&ie=UTF8&qid=1470227401'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Digital SLRs"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class DigitalCameras(scrapy.Spider):
	"""DIGITAL CAMERAS"""
	
	name = "cameras2"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389181031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389175031%2Cn%3A1389181031&page=1&ie=UTF8&qid=1470227893"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389181031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389175031%2Cn%3A1389181031&page={pagenum}&ie=UTF8&qid=1470227893'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Point & Shoot Digital Cameras"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Lenses(scrapy.Spider):
	"""LENSES"""
	
	name = "cameras3"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389197031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389197031&page=1&ie=UTF8&qid=1470227711"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389197031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389197031&page={pagenum}&ie=UTF8&qid=1470227711'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Lenses"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Surveillance(scrapy.Spider):
	"""SURVEILLANCE CAMERAS"""
	
	name = "cameras4"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389203031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389203031&page=1&ie=UTF8&qid=1470227836"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389203031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389203031&page={pagenum}&ie=UTF8&qid=1470227836'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Surveillance Cameras"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Binoculars(scrapy.Spider):
	"""BINOCULARS"""
	
	name = "cameras5"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389159031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389159031&page=1&ie=UTF8&qid=1470228367"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389159031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389159031&page={pagenum}&ie=UTF8&qid=1470228367'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Binoculars, Telescopes & Optics"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Camcorders(scrapy.Spider):
	"""CAMCORDERS"""
	
	name = "cameras6"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389174031_pg_2?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389174031&page=2&ie=UTF8&qid=1470228545"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389174031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388977031%2Cn%3A1389174031&page={pagenum}&ie=UTF8&qid=1470228545'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Camcorders"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Televisons(scrapy.Spider):
	"""TELEVISIONS"""
	
	name = "cameras7"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389396031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389375031%2Cn%3A1389396031&page=1&ie=UTF8&qid=1470228842"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389396031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389375031%2Cn%3A1389396031&page={pagenum}&ie=UTF8&qid=1470228842'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Televisions"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Headphones(scrapy.Spider):
	"""HEADPHONES"""
	
	name = "cameras8"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1388921031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388867031%2Cn%3A1388878031%2Cn%3A1388921031&page=1&ie=UTF8&qid=1470228844"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1388921031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388867031%2Cn%3A1388878031%2Cn%3A1388921031&page={pagenum}&ie=UTF8&qid=1470228844'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Headphones"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Speakers(scrapy.Spider):
	"""SPEAKERS"""
	
	name = "cameras9"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389365031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389335031%2Cn%3A1389365031&page=1&ie=UTF8&qid=1470228845"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389365031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389335031%2Cn%3A1389365031&page={pagenum}&ie=UTF8&qid=1470228845'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Speakers"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class HomeTheater(scrapy.Spider):
	"""HOME THEATER"""
	
	name = "cameras10"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389375031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389375031&page=1&ie=UTF8&qid=1470228846"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389375031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389375031&page={pagenum}&ie=UTF8&qid=1470228846'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Home Theater, TV & Video"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class PortableMediaPlayers(scrapy.Spider):
	"""PORTABLE MEDIA PLAYERS"""
	
	name = "cameras11"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1389433031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389433031&page=1&ie=UTF8&qid=1470228847"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1389433031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389433031&page={pagenum}&ie=UTF8&qid=1470228847'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Portable Media Players"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class AudioVideoAccessories(scrapy.Spider):
	"""HOME AUDIO & VIDEO ACCESSORIES"""
	
	name = "cameras12"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1388878031_pg_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388867031%2Cn%3A1388878031&page=1&ie=UTF8&qid=1470228847"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1388878031_pg_{pagenum}?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1388867031%2Cn%3A1388878031&page={pagenum}&ie=UTF8&qid=1470228847'
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
		item['category'] = "Cameras, Audio & Video"
		item['subcategory'] = "Home Audio & Video Accessories"
		items.append(item)
		return items

"""=======================================Spider End======================================="""



