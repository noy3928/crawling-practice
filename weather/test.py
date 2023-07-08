from selenium import webdriver 
import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path = r'/Users/noyechan/Desktop/파이썬/selenium/sellenium/chromedriver')
driver.get("https://www.weather.go.kr/w/index.do")

searchBar = driver.find_element_by_css_selector("input.input")
searchBar.send_keys("부산") # 서치바에 도시 입력
searchBar.send_keys(Keys.ENTER) # 서치바 엔터
time.sleep(1)

firstPlace = driver.find_elements_by_css_selector("li.place")
firstPlace[0].click()
    #서치바에 나온 첫번째 검색 결과
    #첫번째 검색결과 클릭
time.sleep(1) # 4초가 지난 후에 
tmp = driver.find_element_by_xpath("//*[@id='current-weather']/div[2]/ul[1]/li[1]/span[4]").text

print(tmp)

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()