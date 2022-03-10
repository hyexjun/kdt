import requests
from bs4 import BeautifulSoup

url="https://www.naver.com/"
res=requests.get(url)
res.raise_for_status()

print(res.text)
# text를 lxml로 파싱해서 정보를 제공 받음
soup=BeautifulSoup(res.text, "lxml")
print(soup.title.get_text())   # 타이틀 태그에 있는 글자 싸그리 긁어와잉

# print(soup.a.span.get_text())
# print(soup.a["href"])
print(soup.a.attrs)