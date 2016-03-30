# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from random import choice
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree
from washctrip import wash

def findTrip(fromCity,toCity,date):
    #url = "http://www.qua.com/flights/PEK-XMN/2016-04-06?from=home"
    #url = "http://www.qua.com/flights/PEK-XMN/2016-04-06?m=CNY&from=home"
    url_head = "http://www.qua.com/flights/"
    url_tail = "?m=CNY&from=home"
    url = url_head + fromCity +'-'+ toCity +'/'+ date + url_tail

    ua_list = [
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
            "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36"
            ]

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.resourceTimeout"] = 15 
    dcap["phantomjs.page.settings.loadImages"] = False
    dcap["phantomjs.page.settings.userAgent"] = choice(ua_list)
    driver = webdriver.PhantomJS(executable_path=u'./phantomjs',desired_capabilities=dcap)
    #driver = webdriver.Firefox()
    #driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(5)

    origin_page = driver.page_source # .decode('utf-8','ignore')
    origin_html = etree.HTML(origin_page)
    items = origin_html.xpath("//div[@class='fl-detail-nav']/ul/li[1]")
    items = origin_html.xpath("//div[@class='m-fly-item s-oneway']")
    items = origin_html.xpath("//div[@id='list-box']/div")
    print len(items)

    detail = []
    for index,item in enumerate(items):
        flight_each = "//div[@id='list-box']/div["+str(index+1)+"]"
        detail_span = "//div[@class='fl-detail-nav']/ul/li[1]/span[@class='nav-label']"
        detail_span = "//div[@class='fl-detail-nav']/ul/li[1]"
        f_route_div = "//div[@class='m-fl-info-bd']/div"

        #driver.find_element_by_xpath(flight_each+detail_span).click() # 数据由js来控制,点击后加载数据
        #driver.find_element_by_xpath(flight_each+"/div[2]/div[1]/ul/li[1]/span").click() # 数据由js来控制,点击后加载数据
        print driver.find_element_by_xpath(flight_each+detail_span)
        element = driver.find_element_by_xpath(flight_each+detail_span)
        hover = ActionChains(driver).move_to_element_with_offset(element,0,20)
        hover.perform()
        element.click()

        true_page = driver.page_source
        true_html = etree.HTML(true_page)

        #test = true_html.xpath(flight_each + "//div[@class='m-fl-info-bd']/div/p[2]//text()") #get airflight and company
        #print test
        company = true_html.xpath(flight_each + f_route_div + '/p[1]//text()') #get airflight and company
        flight_time = true_html.xpath(flight_each + f_route_div + '/p[2]//text()')
        airports = true_html.xpath(flight_each + f_route_div + '/p[3]//text()')
        passtime = true_html.xpath(flight_each + f_route_div + '/p[4]//text()')
        price = true_html.xpath(flight_each + "//div[@class='fl-price-box']//em//text()")

        company = wash(company)
        flight_time = wash(flight_time)
        airports = wash(airports)
        passtime = wash(passtime)

        detail.append(
                dict(
                    company=company,
                    flight_time=flight_time,
                    airports=airports,
                    passtime=passtime,
                    price=price
                    ))
    driver.close()
    return detail

if __name__ == '__main__':
    fromCity = "PEK" #replace beijing by 'PEK'
    toCity = "XMN"
    date = "2016-04-06"  #example 2016-04-06
    data = findTrip(fromCity, toCity, date) 
    #construction
    #print data[0]
    for each in data:
        print each
