from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

url = "http://www.qua.com/flights/PEK-XMN/2016-04-06?from=home"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)
company = driver.find_element_by_xpath("//div[@class='fl-ca-ct']")
print company.text
hover = ActionChains(driver).move_to_element(company)
hover.perform()
air = driver.find_element_by_xpath("//div[@class='tip-cont']")
if air:
    print air.text
driver.close()
