import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://flight.naver.com/'
browser.get(url)

# 출발도시 선택기능 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]').click()
time.sleep(1)
# 국내 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
# 세부도시 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[1]').click()

# 도착도시 선택기능 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(1)
# 국내 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
# 제주 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]').click()


# 가는날/오는날 선택기능
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
# 가는 날짜 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[4]/button').click()
# 오는 날짜 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[5]/button').click()


# 인원 선택기능 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[3]/button').click()
time.sleep(1)
# 인원 성인 + 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[3]/div/div[1]/div[1]/button[2]').click()
# 다시 인원 선택 눌러서 확정해주기
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[3]/button').click()
# 항공권 검색 버튼 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# 검색결과 페이지가 로딩될 때까지 최대 10초 기다려주겠음
browser.implicitly_wait(10)
# 이거나 아래꺼나.. 근데 아래꺼는 위에 import 뭐 많이 해야됨..

# url = 'https://flight.naver.com/flights/domestic/SEL-CJU-20220223/CJU-SEL-20220224?adult=2&fareType=YC'
# browser.get(url)

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC


# WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button'))




prev_height = browser.execute_script("return document.body.scrollHeight")
# 지금 현재 스크롤의 길이(브라우저의 높이 값)를 prev머시기에 저장 선언

while 1 :
    # 현재 높이에서 브라우저 최대 길이까지 반복하는 구문
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 스크롤링 한 뒤의 현재 길이값을 curr에 저장 선언

    # p스크롤과 c스크롤의 길이가 다르면 '저장 후 스크롤' 반복
    # 같으면 아래 if문으로 종료 후 끝내기
    if curr_height == prev_height :
        break


page_url = browser.page_source   # 브라우저 페이지 소스 가져오기
soup = BeautifulSoup(page_url, "lxml")
flights = soup.find_all("div", {"class":"result"})


for flight in flights :
    print("항공사 :", flight.b.get_text())
    print(flight.find("div", {"class":"route"}).get_text())