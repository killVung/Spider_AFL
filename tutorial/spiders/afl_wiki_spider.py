import scrapy
from tutorial.items import AFLItem

class AFL_wiki_Spider(scrapy.Spider):
    name = "AFL-wiki"
    start_urls = [
        "https://en.wikipedia.org/wiki/Australian_Football_League#Current_clubs"
    ]
    def parse(self,response):
        sel = response.xpath('//table[preceding-sibling::h3/span[@id="Current_clubs"] and following-sibling::h3/span[@id="Former_clubs"]]')[0]
        #This would point toward the table below Current clubs and above former clubs
        print("--------------------------------")
        #Specify the tables row of the football clubs
        for club_selector_table_row in sel.xpath('tr')[1:len(sel.xpath('tr'))-1]:
            item = AFLItem()
            club_selector_information = club_selector_table_row.xpath('*')

            club_name_selector = club_selector_information[0]
            club_name = club_name_selector.xpath('a/@title')[0].extract()
            item['name'] = club_name

            club_state_selector = club_selector_information[2]
            club_state = club_state_selector.xpath('a/text()')[0].extract()
            item['state'] = club_state

            club_stadium_selector = club_selector_information[3]
            club_stadium = club_stadium_selector.xpath('a/@title')[0].extract()
            item['stadium'] = club_stadium

            club_establish_selector = club_selector_information[4]
            club_establish = club_establish_selector.xpath('text()')[0].extract()
            item['establish'] = club_establish
            
            yield item



        print("--------------------------------")
