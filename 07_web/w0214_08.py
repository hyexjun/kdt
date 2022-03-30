import requests

url = 'http://www.melon.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}

res = requests.get(url, headers=headers)
# reg.raise_for_status() #에러가 있으면 종료, 없으면 계속 실행

print(res.text)
with open ('melon.html', 'w', encoding='utf-8') as f:
    f.write(res.text)