import requests

# url="https://www.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
url = "https://www.melon.com/chart/rise/index.htm"
res = requests.get(url)
res = requests.get(url, headers=headers)
# print("응답 코드 : ", res.status_code)
# res.raise_for_status()
print(res.text)             # 이것이 웹 크롤링이다...
f = open("mel.html", "w", encoding="utf-8")
f.write(res.text)