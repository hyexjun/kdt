import requests
from bs4 import BeautifulSoup

url="http://browse.auction.co.kr/search?keyword=tv&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=tv&acode=SRP_SU_0100&arraycategory=&encKeyword=tv"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 평점이 4.5 이상이면서,
# 후기가 500개 이상인 것,
# 구매가 1000개 이상인 것

items = soup.find_all("div",{"class":"section--itemcard_info"})
# print(items[0])

cnt = 1
for item in items :
    name = item.find("span", {"class":"text--title"}).get_text()
    price = item.find("span", {"class":"price_seller"}).strong.get_text()

    if item.find("li", {"class":"item awards"}) :
        score = item.find("li", {"class":"item awards"}).get_text()
        score = score[5:-2]
        if float(score) >= 4.5 :
            pass
        else :
            continue
    else :
        continue


    if item.find("span", {"class":"text--reviewcnt"}) :
        review = item.find("span", {"class":"text--reviewcnt"}).get_text().strip()
        review = review[3:].replace(",","")
        if int(review) >= 500 :
            pass
        else :
            continue
    else :
        continue


    if item.find("span", {"class":"text--buycnt"}) :
        buy = item.find("span", {"class":"text--buycnt"}).get_text().strip()
        buy = buy[3:].replace(",","")
        if int(buy) >= 1000 :
            pass
        else :
            continue
    else :
        continue
    
    print("[",cnt,"]")
    print("상품 :", name)
    print("금액 :", price,"원")
    print("평점 :", score,"점")
    print("후기 :", review,"개")
    print("구매 :", buy,"개")
    print("-----"*10)
    cnt += 1