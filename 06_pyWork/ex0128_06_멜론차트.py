import requests
from bs4 import BeautifulSoup


url = "https://www.melon.com/chart/index.htm"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

ranks = soup.tbody.find_all("tr")  # tr 태그가 리스트로 우르르

for i, rank in enumerate(ranks) :
    rank_num = rank.find("span",{"class":"rank"}).get_text()
    rank_txt = rank.find("div",{"class":"ellipsis rank01"}).span.a.get_text()
    print("{}위 : {}".format(rank_num,rank_txt))