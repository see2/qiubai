import scrapy

from qiubai.items import QiubaiItem

class QiuBaiSpider(scrapy.Spider):
    name="qiubai"
    start_urls=[
            "https://qiushibaike.com/" ,
    ]

    def parse(self, response):
        n=0
        for ele in response.xpath('//div[contains(@class,"article block untagged mb15")]'):
            n=n+1
            print n
            authors = ele.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
            contents = ele.xpath('.//div[@class="content"]/span[1]/text()').extract()
            yield QiubaiItem(author=authors, content=contents)
