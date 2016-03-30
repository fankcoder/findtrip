import scrapy
from findtrip.items import FindtripItem

class QuaSpider(scrapy.Spider):
    name = "Qua"
    start_urls = [
        "http://www.qua.com/flights/PEK-XMN/2016-05-12?m=CNY&from=flight_home"
    ]
        
    def parse(self, response):

        sel = scrapy.Selector(response)
        
        dataList = sel.xpath("//div[@class='m-fly-item s-oneway']")
        items = []
        for index,each in enumerate(dataList):
            flight_each = "//div[@id='list-box']/div["+str(index+1)+"]"
            detail_span = "//div[@class='fl-detail-nav']/ul/li[1]/span[@class='nav-label']"
            f_route_div = "//div[@class='m-fl-info-bd']/div"

            airports = sel.xpath(flight_each + f_route_div + '/p[3]//text()').extract()
            company = sel.xpath(flight_each + f_route_div + '/p[1]//text()').extract()
            flight_time = sel.xpath(flight_each + f_route_div + '/p[2]//text()').extract()
            passtime = sel.xpath(flight_each + f_route_div + '/p[4]//text()').extract()
            price = sel.xpath(flight_each + "//div[@class='fl-price-box']//em//text()").extract()

            item = FindtripItem()
            item['company'] = company
            item['flight_time'] = flight_time
            item['airports'] = airports
            item['passtime'] = passtime
            item['price'] = price
            items.append(item)
        return items
