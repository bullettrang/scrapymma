import scrapy

class EventSpider(scrapy.Spider):
    name = "event"  #every spider needs a name

    def start_requests(self):
        url = "https://www.tapology.com/fightcenter/events/54138-ufc-fight-night-143"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.css(".fightCard .fightCardBout"):
            yield {
                "number": row.css("div.fightCardBoutNumber::text").extract_first(),
                "nameleft": row.css("div.fightCardFighterName.left a::text").extract_first(),
                "recordright":row.css("div.right div.fightCardRecord::text").extract_first(),
                "recordleft": row.css("div.fightCardFighterBout.left div.fightCardRecord::text").extract_first(),
                "nameright": row.css("div.fightCardFighterName.right a::text").extract_first()      
            }
            #recordright is only grabbing the \n.....