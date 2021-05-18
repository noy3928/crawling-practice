from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request


driver = webdriver.Chrome(executable_path = r'/Users/noyechan/Desktop/파이썬/selenium/sellenium/chromedriver')
driver.get("https://www.weather.go.kr/w/index.do")


tmp = driver.find_element_by_css_selector(".tmp").text
hue = driver.find_element_by_css_selector("span.val").text
wind = driver.find_elements_by_css_selector("span.val")
tmp1 = driver.find_elements_by_css_selector("g.highcharts-label")
feelTmp = driver.find_element_by_xpath("//ul[@class='item s-item  ']/li[2]/span[2]")

print(tmp)
print(hue)
print(wind[1].text)
print(tmp1[85])
print(feelTmp.text)
# for i in range(len(tmp1)):
#     print(tmp1[i].text)



# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()