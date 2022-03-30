import re
import requests
from bs4 import BeautifulSoup

# for page in range(0, 5) :
    # url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(page+1)
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# ul1 = soup.find("ul", {"id":"productList"})
# ul2 = soup.select('ul.productList')

items = soup.find_all("li", {"class":re.compile("^search-product")})

for item in items :
    name = item.find("div", {"class":"name"}).get_text()
    print("상품명 :", name)

    price = item.find("strong", {"class":"price-value"}).get_text()
    print("가격 :", price,"원")
    
    rating = item.find("em", {"class":"rating"})
    if rating :   # 그냥 프린트로 하면 평점 없는 애들 때문에 에러 나옴 그래서 rating이 있으면 출력으로 수정
        rate = rating.get_text()
        if float(rate) >= 4.5 :
            print("별점 :", rate)
        else :
            continue
    else :
        print("별점 없음")
    
    totalcount = item.find("span", {"class":"rating-total-count"})
    if totalcount :
        tcnt = totalcount.get_text()
        tcnt = tcnt[1:-1]

        if int(tcnt) >= 200 :
            print("후기 수 :", tcnt)
        else :
            continue
    else :
        print("상품평 없음")