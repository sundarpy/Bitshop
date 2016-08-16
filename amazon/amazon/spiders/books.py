import scrapy
from amazon.items import AmazonItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

"""==========================================================================================="""
"""=======================================BEGIN SPIDERS======================================="""
"""==========================================================================================="""

class LiteratureFiction(scrapy.Spider):
	"""LITERATURE AND FICTION"""
	name = "books1"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1318157031_pg_1?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318157031&page=1&ie=UTF8&qid=1470055527"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1318157031_pg_{pagenum}?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318157031&page={pagenum}&ie=UTF8&qid=1470055527'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-column a-span12 a-text-center"]/a/@href')
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
		item['offerprice'] = hxs.select('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Books"
		item['subcategory'] = "Literature & Fiction"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class ChildrensYoungAdult(scrapy.Spider):
	"""CHILDREN'S & YOUNG ADULT"""
	name = "books2"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1318073031_pg_1?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031&page=1&ie=UTF8&qid=1470055538"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1318073031_pg_{pagenum}?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031&page={pagenum}&ie=UTF8&qid=1470055538'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-column a-span12 a-text-center"]/a/@href')
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
		item['offerprice'] = hxs.select('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Books"
		item['subcategory'] = "Children's & Young Adult"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Textbooks(scrapy.Spider):
	"""TEXTBOOKS"""
	name = "books3"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4149418031_pg_1?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A4149418031&page=1&ie=UTF8&qid=1470055578"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4149418031_pg_{pagenum}?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A4149418031&page={pagenum}&ie=UTF8&qid=1470055578'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-column a-span12 a-text-center"]/a/@href')
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
		item['offerprice'] = hxs.select('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Books"
		item['subcategory'] = "Textbooks"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class ExamCentral(scrapy.Spider):
	"""EXAM CENTRAL"""
	name = "books4"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4149751031_pg_1?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A4149751031&page=1&ie=UTF8&qid=1470055595"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4149751031_pg_{pagenum}?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A4149751031&page={pagenum}&ie=UTF8&qid=1470055595'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-column a-span12 a-text-center"]/a/@href')
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
		item['offerprice'] = hxs.select('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Books"
		item['subcategory'] = "Exam Central"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class EducationalSoftware(scrapy.Spider):
	"""EDUCATIONAL SOFTWARE"""
	name = "books5"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_5490084031_pg_1?rh=n%3A976451031%2Cn%3A%21976452031%2Cn%3A5490084031&page=1&ie=UTF8&qid=1470055702"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_5490084031_pg_{pagenum}?rh=n%3A976451031%2Cn%3A%21976452031%2Cn%3A5490084031&page={pagenum}&ie=UTF8&qid=1470055702'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-column a-span12 a-text-center"]/a/@href')
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
		item['offerprice'] = hxs.select('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Books"
		item['subcategory'] = "Educational Software"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class IndianLanguages(scrapy.Spider):
	"""BOOKS IN INDIAN LANGUAGE"""
	name = "books6"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4932325031_pg_1?rh=n%3A976389031%2Cn%3A%211318447031%2Cn%3A%211318449031%2Cn%3A4932325031&page=1&ie=UTF8&qid=1470055725"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4932325031_pg_{pagenum}?rh=n%3A976389031%2Cn%3A%211318447031%2Cn%3A%211318449031%2Cn%3A4932325031&page={pagenum}&ie=UTF8&qid=1470055725'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-column a-span12 a-text-center"]/a/@href')
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
		item['offerprice'] = hxs.select('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Books"
		item['subcategory'] = "Books in Indian Language"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Hindi(scrapy.Spider):
	"""HINDI"""
	name = "books7"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4506102031_pg_1?rh=n%3A976389031%2Cn%3A%211318447031%2Cn%3A%211318449031%2Cn%3A4506102031&page=1&ie=UTF8&qid=1470055795"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4506102031_pg_{pagenum}?rh=n%3A976389031%2Cn%3A%211318447031%2Cn%3A%211318449031%2Cn%3A4506102031&page={pagenum}&ie=UTF8&qid=1470055795'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-column a-span12 a-text-center"]/a/@href')
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
		item['offerprice'] = hxs.select('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Books"
		item['subcategory'] = "Hindi"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Marathi(scrapy.Spider):
	"""MARATHI"""
	name = "books8"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_8880352031_pg_1?rh=n%3A976389031%2Cn%3A%211318447031%2Cn%3A%211318449031%2Cn%3A8880352031&page=1&ie=UTF8&qid=1470055792"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_8880352031_pg_{pagenum}?rh=n%3A976389031%2Cn%3A%211318447031%2Cn%3A%211318449031%2Cn%3A8880352031&page={pagenum}&ie=UTF8&qid=1470055792'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-column a-span12 a-text-center"]/a/@href')
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
		item['offerprice'] = hxs.select('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Books"
		item['subcategory'] = "Marathi"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class Tamil(scrapy.Spider):
	"""TAMIL"""
	name = "books9"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_4506103031_pg_1?rh=n%3A976389031%2Cn%3A%211318447031%2Cn%3A%211318449031%2Cn%3A4506103031&page=1&ie=UTF8&qid=1470055775"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_4506103031_pg_{pagenum}?rh=n%3A976389031%2Cn%3A%211318447031%2Cn%3A%211318449031%2Cn%3A4506103031&page={pagenum}&ie=UTF8&qid=1470055775'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="a-column a-span12 a-text-center"]/a/@href')
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
		item['offerprice'] = hxs.select('//span[@class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"]/text()').extract()
		item['saleprice'] = hxs.select('//span[@id="priceblock_saleprice"]/text()').extract()
		item['description'] = hxs.select('//div[@id="productDescription"]/p[1]/text()').extract()
		item['feature'] = hxs.select('//ul[@class="a-vertical a-spacing-none"]/li/span/text()').extract()
		item['image'] = hxs.select('//span[@class="a-button-text"]/img/@src').extract()
		item['link'] = response.meta["url"]
		item['seller'] = hxs.select('//div[@id="merchant-info"]/a[1]/text()').extract()
		item['sellrating'] = hxs.select('//div[@id="merchant-info"]/text()').extract()
		item['starating'] = hxs.select('//a[@class="a-link-normal"]/i/span/text()').extract()[0]
		item['COD'] = "Available"
		item['category'] = "Books"
		item['subcategory'] = "Tamil"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

