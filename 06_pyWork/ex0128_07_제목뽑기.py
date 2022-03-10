import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=sun"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# cartoons = soup.find_all("td",{"class":"title"})
# 왜 여기는 앞의 tr?을 안 써도 되는지??
# cartoons = soup.tbody.find("tr")

# 하던거 . 안 됨
# cartoons = soup.find_all("td",{"class":"title"}).a.get_text()
# for cartoon in cartoons :
#     print(cartoon.a.get_text())


# cartoons2 = soup.fall_all("span", {"class":"star"})
# for cartoon2 in cartoons2 :
#     print(cartoon2.strong.get_text())
    

# 되는 방법 1 슬라이싱
cartoons = soup.find_all("tr")

for cartoon in cartoons[2::]:
    title= cartoon.find("td",{"class":"title"}).a.get_text()
    num = cartoon.find("div",{"class":"rating_type"}).strong.get_text()
    print(title, num)
    
    
# 되는 방법 2 예외처리
# title = soup.find_all("tr")
# for t in title:
#     try:
#         w_title = t.find("td",{"class":"title"}).a.get_text()
#         print(w_title)
#     except:
#         pass