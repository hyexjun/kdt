import select
from bs4 import BeautifulSoup
import requests

# for page in range(0, 4) :

    # url = 'https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu&page={}'.format(page+1)
url = 'https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu&page=1'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url, headers=headers)   # 5, 6번줄 뭔가 했더니 크롤링 막아둔 사이트 스크래핑하는 치트키 ㅋㅋㅋ
res.raise_for_status()                     # 에러 시 종료되는 구문=
soup = BeautifulSoup(res.text, "lxml")     # text를 lxml 파싱해서 soup에 담기, 선언

div1 = soup.find("div", {"id":"content"})
td1 = div1.find("td", {"class":"title"})
cartoons = div1.find_all("td", {"class":"title"})
    
# for idx, cartoon in enumerate(cartoons) :
#     print(page+1, "페이지", idx+1, " : ", cartoon.find("a").get_text())

for idx, cartoon in enumerate(cartoons) :
    print(idx+1, " : ", cartoon.find("a").get_text())

star = soup.find_all("div", {"class":"rating_type"})
# star2 = soup.select_one('.rating_type > strong').text
print(star)

