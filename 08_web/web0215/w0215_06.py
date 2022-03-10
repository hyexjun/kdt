import csv
import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# csv파일 이름 지정
filename ="시가총액1-200.csv"
# 파일 저장 설정
f = open(filename,"w",encoding="utf-8-sig",newline="")
# 파일 저장
writer = csv.writer(f)
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
print(type(title))
writer.writerow(title)

# 주식정보 테이블 검색
data_rows = soup.find("table",{"class":"type_2"}).tbody.find_all("tr")

# 주식 정보 가져옴.
for row in data_rows:
    # 주식 정보 컬럼을 모두 가져옴. 총 13개 -> 12개사용
    columns = row.find_all("td")  # 1개, 13개
    if len(columns) <= 1:
        continue
    data = [column.get_text().strip() for column in columns ]
    # data type: list
    writer.writerow(data)
    # print(data)

print("프로그램 종료")  