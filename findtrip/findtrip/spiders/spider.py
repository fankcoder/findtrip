import scrapy

class ftripSpider(scrapy.Spider):
    name = "findtrip"
    start_urls = [
        "http://www.qua.com/flights/PEK-XMN/2016-04-06?m=CNY&from=flight_home"
    ]

    def parse(self, response):
        
