import time
from selenium import webdriver  # 구글드라이버 selenium
from selenium.webdriver.common.keys import Keys  # keys입력에 관한 메소드
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait  # 출력화면이 나타날때까지 대기하는 메소드
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 브라우저 화면의 상태를 알려주는 메소드


browser = webdriver.Chrome()  # 크롬드라이버 로딩
browser.maximize_window()  # 윈도우 창 최대화
url ='https://flight.naver.com/'
browser.get(url)  # url로 이동

# 출발선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]').click()
# 창이 열리는데 시간이 걸림. 시간지연
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[1]').click()

# 도착선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]').click()

# 가는날 / 오는날 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[4]/button').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[5]/button').click()

# 인원선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[3]/button').click()
time.sleep(2)
# 인원1명 추가
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[3]/div/div[1]/div[1]/button[2]').click()

# 인원 항공권 선택 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# 항공권 검색 버튼 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# 항공권 검색시간 지연 필요
# 브라우저 화면에 해당 태그가 나타날때까지 대기, 최대 10초간 대기 함.
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div')))
# time.sleep(10)


# ---------------------------------
# 스크롤해서 내리면 데이터 계속 증가되는 형태로 구성되어 있음.
# 현재 브라우저 높이 값
prev_height = browser.execute_script("return document.body.scrollHeight") 

while True:
    # 현재 높이에서 브라우저 최대높이까지 스크롤해서 내림.
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 데이터가 나타날때까지 대기하고 있음.
    time.sleep(2)
    # 화면을 스크롤해서 내려온 화면높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 현재높이와 이전높이가 같은지 비교해서 같으면 더이상 스크롤이 없으므로 빠져 나옴.
    if curr_height == prev_height:
        break
    # 현재높이를 이전높이에 적용하고 계속적으로 반복
    prev_height = curr_height


# 스크롤을 내리는 명령어를 넣어야 함.

# 출력
# 브라우저 페이지 소스 가져옴.
page_url = browser.page_source

soup = BeautifulSoup(page_url, "lxml")
flights = soup.find_all("div", {"class":"result"})

for flight in flights:
    print("항공사 :",flight.b.get_text())
    print("시간 :",flight.find("div",{"class":"route"}).get_text())
    print("금액 :",flight.find("div",{"class":"domestic_item__2B--k"}).get_text())
    print("-"*20)


# 현재개수 : 20
print("검색 된 항공권 개수 :", len(flights))


# print(browser.page_source)