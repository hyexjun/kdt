import requests
from bs4 import BeautifulSoup

# naver html 소스코드를 모두 가져옴.
res = requests.get('https://www.kakaocorp.com')

print('소스코드 길이 : ', len(res.text))
print('모든 소스 코드 출력 : ')
print(res.text)
with open('01_naver.html', 'w', encoding='utf-8') as f:
    f.write(res.text)
