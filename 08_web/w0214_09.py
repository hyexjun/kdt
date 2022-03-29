import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status() # 에러가 있으면 종료, 없으면 계속 실행

# xml 형태로 파싱되어 저장
soup = BeautifulSoup(res.text, 'lxml')
# print(soup)
# print('타이틀 : ', soup.title) #타이틀 태그 검색
# print('타이틀 : ', soup.title.get_text)  #태그의 글자 출력

print(soup.a)
print(soup.a.attrs)
print(soup.a['onclick'])
print(soup.a.span.get_text())
