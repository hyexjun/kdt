import requests, csv
from bs4 import BeautifulSoup

# 웹스크래핑 기본형태
url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 파일 저장
fileName = "시가총액_20220216.csv"
f = open(fileName, "w", encoding="utf-8-sig", newline="")  # newline 공백처리로 중간에 있는 엔터키 생략하고 연달아 가겠다는 뜻
file = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
file.writerow(title)

data_rows = soup.find("table", {"class":"type_2"}).find("tbody").find_all("tr")
# print(soup.prettify())   # 터미널에 들여쓰기 예쁘게 보여주는 명령어


for row in data_rows :
    # columns = row.find_all("td", {"class":"number"})
    columns = row.find_all("td")
    # data를 list 형태로 넘어오게 하려면 22번줄처럼. [1, 삼성전자, 74500 ... ]
    # data = [column.get_text().strip() for column in columns]

    if len(columns) <= 1 :    # td가 1개만 있을 때는 내용이 없으므로 제외..
        continue


    # data = []   # writerow로 저장하려면 list 형태여야 함. 리스트 빈집 제공..
    data = [column.get_text().strip() for column in columns]
    # 32번줄처럼 빈 리스트집에 append 안 쓰고 [] 안에서 for문 돌리면 자동 append와 같은 개념

    # for column in columns :
    #     data = data.append(column.get_text().strip())
    #     print(data)

    print(data)           # 터미널에서 눈으로 보는 용
    file.writerow(data)   # 파일용