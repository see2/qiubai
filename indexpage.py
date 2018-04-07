import scrapy
class QiuBaiSpider(scrapy.Spider)
	name="qiubai"
	star_urls=[
		"http://qiushibaike.com/" ,
	]

	def parse(self, response):
		print response.xpath('//div[@class="content"]').extract()
