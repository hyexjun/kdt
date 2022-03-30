import time
import pyautogui
from selenium import webdriver  # 구글드라이버 selenium
from selenium.webdriver.common.keys import Keys  # keys입력에 관한 메소드
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait  # 출력화면이 나타날때까지 대기하는 메소드
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 브라우저 화면의 상태를 알려주는 메소드


browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://land.naver.com/'
browser.get(url)


# 검색창 키워드박스 클릭
ser = browser.find_element_by_xpath('//*[@id="queryInputHeader"]')
ser.send_keys("신대방 우성 1차")

# 검색 필터 설정 후 돋보기 클릭
browser.find_element_by_xpath(
    '//*[@id="header"]/div[1]/div/div[1]/div/fieldset/a[1]').click()
browser.implicitly_wait(10)


page_url = browser.page_source
soup = BeautifulSoup(page_url, "lxml")
woosungs = soup.find_all("div", {"class": "item_inner"})

print(woosungs)
