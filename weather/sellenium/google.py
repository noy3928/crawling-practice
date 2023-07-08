#셀레니움
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

#플라스크
from flask import Flask, render_template,jsonify, request
app = Flask(__name__)
#파이몽고
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')


driver = webdriver.Chrome(executable_path = r'/Users/noyechan/Desktop/파이썬/selenium/sellenium/chromedriver')
driver.get("https://www.weather.go.kr/w/index.do")


# 주문 목록보기(Read) API
@app.route('/temp', methods=['GET'])
def view_orders():
    info = list(db.weatherTemper.find({}, {'_id': False}))
    print(info)
    
    return jsonify({'result':'success','information': info})

## API 역할을 하는 부분
@app.route('/temp', methods=['POST'])
def saving():
    city_name = request.form['sample_name']
    tmpList = []

    searchBar = driver.find_element_by_css_selector("input.input")
    searchBar.send_keys(city_name) # 서치바에 도시 입력
    searchBar.send_keys(Keys.ENTER) # 서치바 엔터
    time.sleep(1)

    firstPlace = driver.find_elements_by_css_selector("li.place")
    firstPlace[0].click()
    #서치바에 나온 첫번째 검색 결과
    #첫번째 검색결과 클릭
    time.sleep(1) # 4초가 지난 후에 
    tmp = driver.find_element_by_xpath("//*[@id='current-weather']/div[2]/ul[1]/li[1]/span[4]").text

    print(tmp)
    #현 시간부터 12시간 이내의 날씨를 불러오기.

    doc = {
        'name' : city_name,
        'tmp' : tmp,
    }
    
    db.weatherTemper.insert_one(doc)
    
    return jsonify({'msg':'완료'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)


##########################셀레니움 코드##########################




# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()