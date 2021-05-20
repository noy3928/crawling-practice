from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request


driver = webdriver.Chrome(executable_path = r'/Users/noyechan/Desktop/파이썬/selenium/sellenium/chromedriver')
driver.get("https://www.weather.go.kr/w/index.do")

time.sleep(4)

# elem = driver.find_elements_by_xpath("//*[@id='digital-forecast']/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[2]/ul[1]")

elem = driver.find_elements_by_css_selector("ul.item")

for i in range(12):
    tmp = elem[i].find_elements_by_tag_name("li")
    print(tmp[0].text, tmp[3].text)

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()