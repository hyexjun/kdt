import time, pyautogui
from selenium import webdriver  # 구글드라이버 selenium
from selenium.webdriver.common.keys import Keys  # keys입력에 관한 메소드
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait  # 출력화면이 나타날때까지 대기하는 메소드
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 브라우저 화면의 상태를 알려주는 메소드


browser = webdriver.Chrome()
browser.maximize_window()
url ='https://www.yanolja.com/'
browser.get(url)

# 야놀자 검색버튼 클릭
browser.find_element_by_xpath('//*[@id="__next"]/section/header/div/div[3]/button[1]').click()

# 검색창 키워드박스 클릭
ser = browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[1]/input')
ser.send_keys("제주도 리조트")


browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[2]/button[1]').click()  # 날짜랑 인원 선택 누르기
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[6]').click()  # 가는날
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[5]/td[1]').click()  # 오는날
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[4]/button').click()  # 설정 확인 누르기

# 검색 필터 설정 후 돋보기 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[1]/div/button[2]').click()
time.sleep(5)

# 결과 너무 많아서 5성급 이상으로 필터 버튼 누를거임
browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/div[1]/header/div/section/div/section[2]/div[2]/button[1]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div/main/div/section/div/section[2]/div/button[1]').click()
browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div/main/div/section/div/section[2]/div/button[1]').click()
time.sleep(2)
# 필터설정 적용하기 클릭
browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div/main/div/div/div/button').click()
browser.implicitly_wait(10)

# 근데 5성급하니까 ㅋㅋ 13개밖에 없어서 스크롤 내려갈 게 없다..ㅎ
prev_height = browser.execute_script("return document.body.scrollHeight")
while True :
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    pyautogui.scroll(-prev_height)
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height :
        break
    prev_height = curr_height
    # 근데 이거 이프문 안에 엘스로 넣으면 안되나?


page_url = browser.page_source
soup = BeautifulSoup(page_url, "lxml")
resorts = soup.find_all("div", {"class":"PlaceListItemText_container__fUIgA text-unit"})

num = 1
for resort in resorts :
    rName = resort.find("div", {"class":"PlaceListTitle_container__qe7XH"}).strong.get_text()
    rRate = resort.find("span", {"class":"PlaceListScore_rating__3Glxf"}).get_text()
    rPrice = resort.find("span", {"class":"PlacePriceInfo_salePrice__28VZD"}).get_text()
    print("-"*30)
    print("[",num,"]",rName)
    print(rRate,"점")
    print(rPrice)
    num +=1

