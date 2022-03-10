from email.base64mime import header_encode
import requests
from bs4 import BeautifulSoup


for page in range(0,4):
    

    url="https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu&page={}".format(page+1)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,'lxml')
    cartoons = soup.find("div",{"id":"content"}).find_all("td",{"class":"title"})

    for idx,title in enumerate(cartoons):
        star = title.find_next_sibling("td")
        rating = star.find_all("div",{"class":"rating_type"})
        text = title.find("a").get_text()
        
        for t in rating:
            rate = t.find("strong").get_text()
            print(page+1,"페이지",idx+1,":",text,"// 평점 :",rate)
