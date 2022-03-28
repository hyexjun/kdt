import requests
from bs4 import BeautifulSoup
import re

num = 1
for page in range(1,6):
    url='https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor='.format(page)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')

    # ul1 = soup.find("ul",{"id":"productList"})
    items = soup.find_all("li",{"class":re.compile("^search-product")})

    for item in items:

        # 상품명, 가격
        name = item.find("div",{"class":"name"}).get_text()
        price = item.find("strong",{"class":"price-value"}).get_text()
        pro_url = item.find("a")['href']
        
        # 평점이 없는 경우 발생
        rating = item.find("em",{"class":"rating"})
        # <em>5.0</em></em>
        if rating:
            # rating글자 추출
            rate = rating.get_text()
            
        else:
            continue    
            # print("[ 평점 없음 ]")

        # 상품평
        totalcount = item.find("span",{"class":"rating-total-count"})
        if totalcount:
            tcnt = totalcount.get_text()
            # print(tcnt)
            tcnt = tcnt[1:-1]  # (20) -> 20 
            # print(tcnt)
            if int(tcnt)>=1000 and float(rate) >=5.0:
                print(num,"-"*30)
                print("상품명 :",name)
                print("상품가격 :",price)  
                print("평점 :",rating.get_text())
                print("상품평 :",tcnt)
                print("https://www.coupang.com"+pro_url)
                num += 1
            else:
                continue    
        
        else:
            continue
            # print("[ 상품평 없음 ]")