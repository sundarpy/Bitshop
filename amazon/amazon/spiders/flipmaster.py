import scrapy
from amazon.items import FlipkartItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

"""==========================================================================================="""
"""=======================================BEGIN SPIDERS======================================="""
"""==========================================================================================="""

"""========Flipkart Spiders========"""
"""Flipkart Spider for everything"""
class FlipSpider(scrapy.Spider):
	"""All Flipkart Products"""
	handle_httpstatus_list = [400, 404, 403, 500]
	name = "flipkart"
	next_page = 1
	allowed_domains = ["flipkart.com"]
	start_urls = [
		"http://www.flipkart.com/brands"
		]

	def parse(self, response):
		ulink = response.xpath('//ul[@class="unit brand-list gu5"]/li/a/@href')
		for href in ulink:
			uRl = response.urljoin(href.extract())
			yield scrapy.Request(uRl, dont_filter=True, callback=self.parse_link, meta={'urx':href.extract()})

	def create_ajax_request(self, page_number, ur):
		ajax_template = ur.replace("sid=all","page={pagenum}&sid=all")
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse_link)

	def parse_link(self, response):
		ulink2 = response.xpath('//a[@class="_2cLu-l"]/@href')
		linker = str(response.meta["redirect_urls"]).replace("[","").replace("]","")
		for href2 in ulink2:
			uRl2 = response.urljoin(href2.extract())
			yield scrapy.Request(uRl2, dont_filter=True, callback=self.parse_products, meta={'url':href2.extract()})
		self.next_page += 1
		yield self.create_ajax_request(self.next_page, linker)

	def parse_products(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = FlipkartItem()
		item['title'] = hxs.select('//h1[@class="_3eAQiD"]/text()').extract()
		item['brand'] = response.meta["url"].replace("~brand/pr?sid=all","").replace("https://www.flipkart.com/all/","")
		item['sellingprice'] = hxs.select('//div[@class="_3auQ3N _16fZeb"]/text()').extract()
		item['offerprice'] = hxs.select('//div[@class="_1vC4OE _37U4_g"]/text()').extract()[0]
		item['link'] = response.meta["url"]
		item['image'] = hxs.select('//div[@class="_20J1N6 _28LkJV"]/div/@*[2]').extract()
		item['feature'] = hxs.select('//div[@cass="_2PF8IO"]/ul/li/text()').extract()
		item['description'] = hxs.select('//div[@class="bzeytq _3cTEY2"]/text()').extract()
		item['seller'] = hxs.select('//div[@class="_34wn58"]/div[2]/a/span/span[2]/text()').extract()
		item['sellrating'] = hxs.select('//div[@class="_34wn58"]/div[4]/span/span[2]/text()').extract()
		item['starating'] = hxs.select('//div[@class="hGSR34 _3n7T7i"]/text()').extract()
		item['cashod'] = 'Available.'
		item['category'] = hxs.select('//div[@class="_1HEvv0"]/a/text()').extract()[1]
		item['subcategory'] = hxs.select('//div[@class="_1HEvv0"]/a/text()').extract()[2]
		items.append(item)
		return items

"""=======================================Spider End======================================="""

