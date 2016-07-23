import scrapy
from tutorial.items import AFLItem

class AFLSpider(scrapy.Spider):
    name = "AFL"
    start_urls = [
        "http://www.afl.com.au/"
    ]



    def parse(self,response):
        for sel in response.xpath('//ul[@class="team-logos"]/li/a'):
            name = sel.xpath('text()').extract()[0]
            link = sel.xpath('@href').extract()[0]
            item = AFLItem()
            item['name'] = name
            item['link'] = link
            request = scrapy.Request(link,callback=self.parse_football_logo)
            request.meta['item'] = item

            yield request

    def parse_football_logo(self,response):
        item = response.meta['item']
        logoURL = response.xpath('//div[@class="logo"]/img/@src').extract()[0]
        if ("http://s.afl.com.au/" not in logoURL):
            logoURL = response.urljoin(logoURL)
        item['logoURL'] = logoURL
        return item
