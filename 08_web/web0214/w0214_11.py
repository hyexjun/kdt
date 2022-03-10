import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

ol1 = soup.find("ol", {"id":"realTimeRankFavorite"})
cartoons = ol1.find_all("li")

for idx, cartoon in enumerate(cartoons) :
    print(cartoon.find("a").get_text())