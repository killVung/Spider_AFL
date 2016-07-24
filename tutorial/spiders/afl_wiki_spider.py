import scrapy
from tutorial.items import AFLItem

class AFL_wiki_Spider(scrapy.Spider):
    name = "AFL-wiki"
    start_urls = [
        "https://en.wikipedia.org/wiki/Australian_Football_League#Current_clubs"
    ]
    def parse(self,response):
        sel = response.xpath('//table[preceding-sibling::h3]')[0]
        print("--------------------------------")


        for row in sel.xpath('tr'):
            print(row.extract())
        print("--------------------------------")
