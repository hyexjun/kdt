# 풀빌라 9.5이상 리뷰 100
# 이름, 평점, 리뷰, 금액, url링크

import requests
from bs4 import BeautifulSoup


url="https://www.goodchoice.kr/product/result?keyword=%ED%92%80%EB%B9%8C%EB%9D%BC"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# ul > li 상품 전체 리스트 가져오기
items = soup.find("div",{"id":"poduct_list_area"}).find_all("li",{"class":"list_4 adcno3"})

cnt = 1
for item in items :
    name = item.find("img",{"class":"lazy"})["alt"]
    price = item.find("div",{"class":"price"}).b.get_text()
    # score = items[0].find("p",{"class":"score"}).em.get_text()
    # review = items[0].find("p",{"class":"score"}).find("span").next_sibling.strip()

    if item.find("p", {"class":"score"}).em :
        score = item.find("p", {"class":"score"}).em.get_text()
    else :
        continue

    if item.find("p",{"class":"score"}).find("span").next_sibling.strip() :
        review = item.find("p",{"class":"score"}).find("span").next_sibling.strip()
        review = review[1:-1]   # 슬라이싱으로 양쪽 괄호 제거함
        # 여기서 검색 필터로 리뷰 수 50개 이상, 혹은 평점 9.0 이상 등 필요할 경우 if절 추가
        if int(review) >= 100 :
            pass
        else :
            continue       # 100개 미만은 패스..
    else :
        continue

    print("순번 :", cnt)
    print("상품 :", name)
    print("금액 :", price)
    print("평점 :", score,"점")
    print("후기 수 :", review,"개")
    print("-----"*10)
    cnt += 1

