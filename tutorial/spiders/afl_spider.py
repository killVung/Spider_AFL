import scrapy
from tutorial.items import AFLItem

class AFLSpider(scrapy.Spider):
    name = "AFL"
    start_urls = [
        "http://www.afl.com.au/"
    ]

    def parse(self,response):
        for sel in response.xpath('//ul[@class="team-logos"]/li/a'):
            item = AFLItem()
            item['club'] = sel.xpath('text()').extract()
            item['link'] = sel.xpath('@href').extract()
            yield item
