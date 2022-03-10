from email import header
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

rank01 = soup.find('li', {'class':'rank01'})
rank02 = rank01.find_next_sibling('li')
print(rank02)