import time, smtplib, requests, csv
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

fileName = "220217_시가총액_1-50위.csv"
f = open(fileName, "w", encoding="utf-8-sig", newline="")
file = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
file.writerow(title)

data_rows = soup.find("table", {"class":"type_2"}).find("tbody").find_all("tr")

for row in data_rows :
    columns = row.find_all("td")
    if len(columns) <= 1 :
        continue
    data = [column.get_text().strip() for column in columns]
    # print(data)
    file.writerow(data)

# ------------------여기부터 네이버 로그인하기!

browser = webdriver.Chrome()
browser.maximize_window()
url ='https://www.naver.com/'
browser.get(url)
browser.find_element_by_class_name("link_login").click()

input_js = 'document.getElementById("id").value="{id}"; document.getElementById("pw").value="{pw}";'.format(id="parkhj929", pw="nP@ssuu0rd****")   # 여기에 자기꺼 입력 ㅎ
time.sleep(3)
browser.execute_script(input_js)
time.sleep(2)
browser.find_element_by_id("log.login").click()
time.sleep(10)   # 자꾸 꺼져서 일단 ..



smtpName = "smtp.naver.com"
smtpPort = 587
sendEmail = "parkhj929@naver.com"
passWord = "nP@ssuu0rd****"
recvEmail = "onulee@naver.com"

title = "파이썬으로 이메일 보내기 확인"
content = "파이썬으로 이메일을 보냅니다."

# MIME 객체 선언
msg = MIMEText(content)
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subject'] = title


# 메일 서버로 접속
s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()
s.login(sendEmail, passWord)
s.sendmail(sendEmail, recvEmail, msg.as_string())
s.close()