from selenium import webdriver
import time
from random import choice
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree

url = "http://www.qua.com/flights/PEK-XMN/2016-04-06?from=home"
ua_list = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36"
        ]

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.resourceTimeout"] = 15 
dcap["phantomjs.page.settings.loadImages"] = False
dcap["phantomjs.page.settings.userAgent"] = choice(ua_list)
driver = webdriver.PhantomJS(executable_path=u'./phantomjs',desired_capabilities=dcap)
#driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)

origin_page = driver.page_source # .decode('utf-8','ignore')
origin_html = etree.HTML(origin_page)
items = origin_html.xpath("//div[@class='fl-detail-nav']/ul/li[1]")
items = origin_html.xpath("//div[@class='m-fly-item s-oneway']")

detail = []
for index,item in enumerate(items):
    flight_each = "//div[@id='list-box']/div["+str(index+1)+"]"
    detail_span = "//div[@class='fl-detail-nav']/ul/li[1]/span[@class='nav-label']"
    f_route_div = "//div[@class='m-fl-info-bd']/div"

    #driver.find_element_by_xpath(each_div+"//div[@class='fl-detail-nav']/ul/li[1]/span[@class='nav-label']").click() #click each span to get data
    driver.find_element_by_xpath(flight_each+detail_span).click()
    true_page = driver.page_source
    true_html = etree.HTML(true_page)

    #test = true_html.xpath(flight_each + "//div[@class='m-fl-info-bd']/div/p[2]//text()") #get airflight and company
    #print test
    company = true_html.xpath(flight_each + f_route_div + '/p[1]//text()') #get airflight and company
    company = map(lambda x: x.split(), company)
    flight_time = true_html.xpath(flight_each + f_route_div + '/p[2]//text()')
    flight_time = map(lambda x: x.split(), flight_time)
    airports = true_html.xpath(flight_each + f_route_div + '/p[3]//text()')
    airports = map(lambda x: x.split(), airports)
    passtime = true_html.xpath(flight_each + f_route_div + '/p[4]//text()')
    passtime = map(lambda x : x.split(), passtime)
    detail.append(
            dict(
                company=company,
                flight_time=flight_time,
                airports=airports,
                passtime=passtime
                ))
print detail[0]

driver.close()
