import requests
from bs4 import BeautifulSoup 

url = "https://play.google.com/store/movies/top"
headers = {
    
}

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

with open("movie.html", "w", encoding="utf8") as f:
    # f.write(res.text)
    f.write(soup.prettify()) #html문서를 예쁘게 출력 