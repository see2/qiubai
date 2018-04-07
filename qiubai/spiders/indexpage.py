import scrapy
class QiuBaiSpider(scrapy.Spider):
	name="qiubai"
	start_urls=[
		"http://qiushibaike.com/" ,
	]

	def parse(self, response):
		print response.xpath('//div[@class="content"]').extract()
