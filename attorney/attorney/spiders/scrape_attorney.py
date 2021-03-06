import scrapy
from ..items import AttorneyItem

class ScrapeAttorneySpider(scrapy.Spider):
    name = 'scrape_attorney'

    start_urls = ['https://www.martindale.com/search/attorneys/?term=2&sort=compositeName&sortType=DESC']





    def parse(self, response):
        # item = AttorneyItem()
        attorney_name = response.css('.detail_title a').css('::text').extract()
        attorney_location = response.css('.detail_location').css('::text').extract()

       
        attorney_name = attorney_name
        location = attorney_location



        yield {
            "name": attorney_name,
            "location": location


        }

### CLI code to run the code: scrapy crawl scrape_attorney
### code to export the result to csv: scrapy crawl scrape_attorney -o item.csv
### code to export the result to json: scrapy crawl scrape_attorney -o item.json. 
### I included both the csv and json outputs
