import enum
from bs4 import BeautifulSoup
import requests

url = 'https://comic.naver.com/webtoon/weekday'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url, headers=headers)   # 5, 6번줄 뭔가 했더니 크롤링 막아둔 사이트 스크래핑하는 치트키 ㅋㅋㅋ
res.raise_for_status()                     # 에러 시 종료되는 구문=
soup = BeautifulSoup(res.text, "lxml")     # text를 lxml 파싱해서 soup에 담기, 선언

div1 = soup.find("div", {"id":"content"})
# cartoons = div1.find("div", {"class":"list_area daily_all"})
div2 = div1.find("div", {"class":"list_area daily_all"})
cartoons = div2.find_all("li")

for idx, cartoon in enumerate(cartoons) :
    name1 = cartoon.find("img")["title"]
    print(idx+1, " : ", name1)

print("웹툰 총 개수 : ", len(cartoons))
# print(cartoons[0])