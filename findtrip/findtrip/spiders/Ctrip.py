# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from random import choice
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree

def findTrip():
    url = "http://flights.ctrip.com/booking/XMN-BJS-day-1.html?DDate1=2016-04-18"
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
    driver = webdriver.PhantomJS(executable_path=u'/home/icgoo/pywork/spider/phantomjs',desired_capabilities=dcap)

    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(5)
    page = driver.page_source # .decode('utf-8','ignore')
    html = etree.HTML(page)
    
    fligint_div = "//div[@id='J_flightlist2']/div"
    items = html.xpath(fligint_div)
    for index,item in enumerate(items):
        company = html.xpath(fligint_div+'['+str(index+1)+']'+"//tr//div[@class='info-flight J_flight_no']")
        print company


if __name__ == '__main__':
    findTrip()
