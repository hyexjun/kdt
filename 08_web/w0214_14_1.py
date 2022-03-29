import requests
from bs4 import BeautifulSoup

url = 'http://corners.gmarket.co.kr/Bestsellers'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url, headers=headers)   # 5, 6번줄 뭔가 했더니 크롤링 막아둔 사이트 스크래핑하는 치트키 ㅋㅋㅋ
res.raise_for_status()                     # 에러 시 종료되는 구문=
soup = BeautifulSoup(res.text, "lxml")     # text를 lxml 파싱해서 soup에 담기, 선언



divItem = soup.find_all("div", {"class":"thumb"})
# 템 이름 나왔으면 조켓다.........
# for n in divItem :
#     temName = n.find("a").get_text()
#     print(temName)


# 돈은 잘만 나온다.............
divPrice = soup.find_all("div", {"class":"s-price"})
# for p in divPrice :
#     price = p.find("strong").get_text()
#     print(price)

# 합치기!!
for i, k in zip(divItem, divPrice) :
    temName = i.find("a").get_text()
    price = k.find("strong").get_text()
    print("상품명 :",temName,", 가격 :",price)




# for num in range(0, 100) :
#     itemNum = soup.find_all("p", {"id":"no{}".format(num)})
#     print(itemNum)