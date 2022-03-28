import requests, re, csv
from bs4 import BeautifulSoup

num = 1
for page in range(1,6):
    url='https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor='.format(page)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')


    # 파일 저장
    fileName = "coupang_laptop_list.csv"
    f = open(fileName, "w", encoding="utf-8-sig", newline="")
    file = csv.writer(f)
    thead = "번호 상품명 상품가격 평점 후기 url".split(" ")
    file.writerow(thead)


    items = soup.find_all("li",{"class":re.compile("^search-product")})
    num = 1
    for item in items:
        # 상품명
        name = item.find("div",{"class":"name"}).get_text()

        # 가격
        price = item.find("strong",{"class":"price-value"}).get_text()
           
        # 별점
        rating = item.find("em",{"class":"rating"})
        if rating:
            rate = rating.get_text()
        else:
            continue    
            # print("[ 평점 없음 ]")

        # 후기 수
        totalcount = item.find("span",{"class":"rating-total-count"})
        if totalcount:
            tcnt = totalcount.get_text()
            tcnt = tcnt[1:-1]  # (20) -> 20
        else:
            continue
            # print("[ 상품평 없음 ]")
        
        # url
        pro_url = item.find("a")['href']    

        data = [num, name, price, rate, tcnt, "https://www.coupang.com"+pro_url]
        print(data)
        num += 1
        file.writerow(data)