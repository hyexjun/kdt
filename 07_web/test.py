from bs4 import BeautifulSoup
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 출력화면이 나타날때까지 대기하는 메소드
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 브라우저 화면의 상태를 알려주는 메소드


browser = webdriver.Chrome()
browser.maximize_window()
url1 = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=287335759'
url2 = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=268589558'
url3 = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=280454816'
url4 = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=248506731'
url5 = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=289685914'
browser.get(url1)


# 더보기로 목차 펼치기
browser.find_element_by_xpath('//*[@id="div_TOC_Short"]/p/a[2]').click()


# 브라우저 페이지 소스 가져옴.
page_url = browser.page_source

# soup = BeautifulSoup(page_url, "lxml")
# indexs = soup.find_all("div", {"id":"div_TOC_All"})

# for idx in indexs:
#     print("목차 :",indexs.p.get_text())
