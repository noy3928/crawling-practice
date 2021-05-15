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
print(tmp)
print(hue)
print(wind[1].text)



# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()