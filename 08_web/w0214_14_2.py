import requests
from bs4 import BeautifulSoup

res = requests.get('http://corners.gmarket.co.kr/Bestsellers')
res.raise_for_status()
soup = BeautifulSoup(res.content, "html.parser")


data = soup.select('div.best-list')
dataitems = data[1]
products = dataitems.select('ul>li')

for idx, product in enumerate(products) :
    title = product.select_one('a.itemname')
    price = product.select_one('div.s-price>strong')

    print(str(idx+1) + ":", title.get_text(), "//", price.get_text())