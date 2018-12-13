import scrapy
#run file by 'scrapy crawl <name_of_the_spider> -o <output_file_name>.json'
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
                "recordright": ''.join(row.css('div.fightCardFighterBout.right div.fightCardRecord::text').getall()).strip(),
                "recordleft": ''.join(row.css("div.fightCardFighterBout.left div.fightCardRecord::text").getall()).strip(),
                "nameright": row.css("div.fightCardFighterName.right a::text").extract_first()      
            }
            #recordright is only grabbing the \n.....
            #''.join(row.css('div.fightCardFighterBout.right div.fightCardRecord::text').getall()).strip()



            #Resources
            #https://www.reddit.com/r/scrapy/comments/a5gs19/first_time_using_scrapy_cant_seem_to_scrape_mma/ebnmiv7/?context=3
            #https://medium.com/@mottet.dev/scrapy-and-scrapyrt-how-to-create-your-own-api-from-almost-any-website-ecfb0058ad64
            