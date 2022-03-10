# 풀빌라 9.5점 이상
# 이름, 평점, 리뷰, 금액, url

import requests
from bs4 import BeautifulSoup
import re

url='https://www.goodchoice.kr/product/result?keyword=%ED%92%80%EB%B9%8C%EB%9D%BC'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')


items = soup.find_all("div",{"class":re.compile("^stage")})
for item in items :
    name = item.find("div", {"class":"name"}).get_text()
    # 이름에 평점 다 나와버리는.. ? ;;
    price = item.find("div", {"class":"price"}).b.get_text()

    print(name)
    print(price)
    print("----------------------------------")