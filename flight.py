from selenium import webdriver 
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path = r'/Users/noyechan/Desktop/파이썬/selenium/sellenium/chromedriver')
browser.maximize_window() # 창 최대화

browser.get("https://flight.naver.com/flights/")

#가는 날 선택 클릭 
browser.find_element_by_link_text("가는날 선택").click()

# #이번달 27,28일 선택
# browser.find_elements_by_link_text("27")[0].click() #[0] -> 이번달 
# browser.find_elements_by_link_text("28")[0].click() #[0] -> 이번달 

# #다음달 27,28일 선택
# browser.find_elements_by_link_text("27")[1].click() #[0] -> 이번달 
# browser.find_elements_by_link_text("28")[1].click() #[0] -> 이번달 

# 이번달27,다음달28일
browser.find_elements_by_link_text("27")[0].click() #[0] -> 이번달 
browser.find_elements_by_link_text("28")[1].click() #[0] -> 이번달 

browser.find_element_by_link_text("도착").click() #[0] -> 이번달 
browser.find_element_by_link_text("시드니").click() #[0] -> 이번달 

browser.find_element_by_link_text("항공권 검색").click() #[0] -> 이번달 

try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[3]/div[1]/div[7]/ul/li[1]")))
    # 성공했을 때 동작 수행 
    print(elem.text) #첫번째 결과 출력 
finally:
    browser.quit()

# elem = browser.find_element_by_xpath("//*[@id='content']/div[3]/div[1]/div[7]/ul/li[1]")
# print(elem.text)