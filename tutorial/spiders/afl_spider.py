import scrapy

class AFLSpider(scrapy.Spider):
    name = "AFL"
    start_urls = [
        "http://www.afl.com.au/"
    ]

    def parse(self,response):
        for sel in response.xpath('//ul[@class="team-logos"]/li/a'):
            club = sel.xpath('text()').extract()
            link = sel.xpath('@href').extract()
            print(club,link)
