import requests
from bs4 import BeautifulSoup

url = "https://shoppinghow.kakao.com/siso/p/bestRank/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

bestItem = soup.find_all()