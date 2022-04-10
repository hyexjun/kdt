import requests, csv, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# url = "https://m.sports.naver.com/beijing2022/medal/index"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

browser = webdriver.Chrome()
browser.get('https://m.sports.naver.com/beijing2022/medal/index')
browser.find_element_by_class_name("Medal_button_more__2oy_Q").click()

time.sleep(5)
soup = BeautifulSoup(browser.page_source, "lxml")   # 소스를 바로 가져옴

with open("naver_oly.html", "w", encoding="utf-8") as f :
    # f.write(browser.page_source)    # 이거 너무 소스가 더러워서
    f.write(soup.prettify())          # 이걸로 다시 해봄..

print("프로그램 저장 완료")