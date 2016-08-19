import scrapy
from amazon.items import AmazonItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

"""==========================================================================================="""
"""=======================================BEGIN SPIDERS======================================="""
"""==========================================================================================="""

class WatchesMen(scrapy.Spider):
	"""MENS WATCHES"""
	
	name = "jewel1"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_2563504031_pg_1?rh=n%3A1350387031%2Cn%3A%211350388031%2Cn%3A2563504031&page=1&ie=UTF8&qid=1470292188"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_2563504031_pg_{pagenum}?rh=n%3A1350387031%2Cn%3A%211350388031%2Cn%3A2563504031&page={pagenum}&ie=UTF8&qid=1470292188'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Men's Watches"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class WatchesWomen(scrapy.Spider):
	"""WOMENS WATCHES"""
	
	name = "jewel2"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_2563505031_pg_1?rh=n%3A1350387031%2Cn%3A%211350388031%2Cn%3A2563505031&page=1&ie=UTF8&qid=1470292190"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_2563505031_pg_{pagenum}?rh=n%3A1350387031%2Cn%3A%211350388031%2Cn%3A2563505031&page={pagenum}&ie=UTF8&qid=1470292190'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Women's Watches"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class PremiumWatches(scrapy.Spider):
	"""PREMIUM WATCHES"""
	
	name = "jewel3"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_3543331031_pg_1?rh=n%3A1350387031%2Cn%3A%211499791031%2Cn%3A%211499793031%2Cn%3A3543331031&page=1&ie=UTF8&qid=1470292191"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_3543331031_pg_{pagenum}?rh=n%3A1350387031%2Cn%3A%211499791031%2Cn%3A%211499793031%2Cn%3A3543331031&page={pagenum}&ie=UTF8&qid=1470292191'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Premium Watches"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class MensSunglasses(scrapy.Spider):
	"""MENS SUNGLASSES"""
	
	name = "jewel4"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1968036031_pg_1?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968032031%2Cn%3A1968036031&page=1&ie=UTF8&qid=1470292196"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1968036031_pg_{pagenum}?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968032031%2Cn%3A1968036031&page={pagenum}&ie=UTF8&qid=1470292196'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Men's Sunglasses"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class WomensSunglasses(scrapy.Spider):
	"""WOMENS SUNGLASSES"""
	
	name = "jewel5"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_1968401031_pg_1?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1953602031%2Cn%3A1968397031%2Cn%3A1968401031&page=1&ie=UTF8&qid=1470292202"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_1968401031_pg_{pagenum}?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1953602031%2Cn%3A1968397031%2Cn%3A1968401031&page={pagenum}&ie=UTF8&qid=1470292202'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Women's Sunglasses"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class EyeFrames(scrapy.Spider):
	"""EYE FRAMES"""
	
	name = "jewel6"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_7424748031_pg_1?rh=n%3A1571271031%2Cn%3A%211597453031%2Cn%3A%211597455031%2Cn%3A7424748031&page=1&ie=UTF8&qid=1470293323"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_7424748031_pg_{pagenum}?rh=n%3A1571271031%2Cn%3A%211597453031%2Cn%3A%211597455031%2Cn%3A7424748031&page={pagenum}&ie=UTF8&qid=1470293323'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Eye Frames"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class WomenJewellery(scrapy.Spider):
	"""JEWELLERY WOMEN"""
	
	name = "jewel7"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_7124358031_pg_1?rh=n%3A1951048031%2Cn%3A%211951049031%2Cn%3A7124358031&page=1&ie=UTF8&qid=1470293326"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_7124358031_pg_{pagenum}?rh=n%3A1951048031%2Cn%3A%211951049031%2Cn%3A7124358031&page={pagenum}&ie=UTF8&qid=1470293326'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Women's Jewellery"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class MenJewellery(scrapy.Spider):
	"""JEWELLERY MEN"""
	
	name = "jewel8"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_7124359031_pg_1?rh=n%3A1951048031%2Cn%3A%211951049031%2Cn%3A7124359031&page=1&ie=UTF8&qid=1470293328"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_7124359031_pg_{pagenum}?rh=n%3A1951048031%2Cn%3A%211951049031%2Cn%3A7124359031&page={pagenum}&ie=UTF8&qid=1470293328'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Men's Jewellery"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class PreciousJewellery(scrapy.Spider):
	"""PRECIOUS JEWELLERY"""
	
	name = "jewel9"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_5210069031_pg_1?rh=n%3A1951048031%2Cn%3A%212152573031%2Cn%3A%212152575031%2Cn%3A5210069031&page=1&ie=UTF8&qid=1470293329"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_5210069031_pg_{pagenum}?rh=n%3A1951048031%2Cn%3A%212152573031%2Cn%3A%212152575031%2Cn%3A5210069031&page={pagenum}&ie=UTF8&qid=1470293329'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Precious Jewellery"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class FashionJewellery(scrapy.Spider):
	"""FASHION JEWELLERY"""
	
	name = "jewel10"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_5210079031_pg_1?rh=n%3A1951048031%2Cn%3A%212152573031%2Cn%3A%212152575031%2Cn%3A5210079031&page=1&ie=UTF8&qid=1470293330"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_5210079031_pg_{pagenum}?rh=n%3A1951048031%2Cn%3A%212152573031%2Cn%3A%212152575031%2Cn%3A5210079031&page={pagenum}&ie=UTF8&qid=1470293330'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Fashion Jewellery"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class TraditionalJewellery(scrapy.Spider):
	"""TRADITIONAL IMITATION JEWELLERY"""
	
	name = "jewel11"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_3543375031_pg_1?rh=n%3A1951048031%2Cn%3A%212152573031%2Cn%3A%212152575031%2Cn%3A3543375031&page=1&ie=UTF8&qid=1470293331"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_3543375031_pg_{pagenum}?rh=n%3A1951048031%2Cn%3A%212152573031%2Cn%3A%212152575031%2Cn%3A3543375031&page={pagenum}&ie=UTF8&qid=1470293331'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Traditional Imitation Jewellery"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class FreshTrending(scrapy.Spider):
	"""FRESH & TRENDING"""
	
	name = "jewel12"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_3700238031_pg_1?rh=n%3A6648217031%2Cn%3A%216648222031%2Cn%3A%216648224031%2Cn%3A3700238031&page=1&ie=UTF8&qid=1470295352"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_3700238031_pg_{pagenum}?rh=n%3A6648217031%2Cn%3A%216648222031%2Cn%3A%216648224031%2Cn%3A3700238031&page={pagenum}&ie=UTF8&qid=1470295352'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Fresh & Trending"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class GiftStore(scrapy.Spider):
	"""GIFT STORE"""
	
	name = "jewel13"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_3588507031_pg_1?rh=n%3A1951048031%2Cn%3A%212152573031%2Cn%3A%212152575031%2Cn%3A3588507031&page=1&ie=UTF8&qid=1470295364"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_3588507031_pg_{pagenum}?rh=n%3A1951048031%2Cn%3A%212152573031%2Cn%3A%212152575031%2Cn%3A3588507031&page={pagenum}&ie=UTF8&qid=1470295364'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Gift Store"
		items.append(item)
		return items

"""=======================================Spider End======================================="""

class GoldSilverCoins(scrapy.Spider):
	"""GOLD & SILVER COINS"""
	
	name = "jewel14"
	next_page = 1
	allowed_domains = ["amazon.in"]
	start_urls = [
		"http://www.amazon.in/s/ref=lp_8609763031_pg_1?rh=n%3A6648217031%2Cn%3A%216648222031%2Cn%3A%216648224031%2Cn%3A8609763031&page=1&ie=UTF8&qid=1470295367"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://www.amazon.in/s/ref=lp_8609763031_pg_{pagenum}?rh=n%3A6648217031%2Cn%3A%216648222031%2Cn%3A%216648224031%2Cn%3A8609763031&page={pagenum}&ie=UTF8&qid=1470295367'
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
		item['category'] = "Jewellery, Watches & Eyewear"
		item['subcategory'] = "Gold & Silver Coins"
		items.append(item)
		return items

"""=======================================Spider End======================================="""




