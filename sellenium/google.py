from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request


driver = webdriver.Chrome(executable_path = r'/Users/noyechan/Desktop/파이썬/selenium/sellenium/chromedriver')
driver.get("https://www.weather.go.kr/w/index.do")
elem = driver.find_element_by_xpath("//li[@class = 'cmp-cur-weather']")
print("---")
print(elem.get_attribute('text'))
print("---")



# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()