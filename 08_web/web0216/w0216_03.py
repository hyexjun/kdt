from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버를 사용하겠다!
browser = webdriver.Chrome()  # 만약 같은 위치가 아니라면 괄호 안에 크롬드라이버exe 있는 경로 넣어주기
browser.get("https://www.naver.com")

# 브라우저 해당 페이지의 html 소스 중 id가 query인 녀석 찾아다가 elem이라고 하기
elem = browser.find_element_by_id("query")
elem   # 걍 이게 터미널에 정보 출력? 이라는데 몰겠음
elem.send_keys("시가총액")     # elem에 시가총액이라는 키를 보내기
elem.send_keys(Keys.ENTER)    # 보낸 그 키에 엔터처리하기


# elem = browser.find_element_by_class_name("spnew ico_logo")
elem = browser.find_element_by_xpath('//*[@id="header_wrap"]/div/div[1]/div[1]/div/h1/a')
elem.click()

elem = browser.find_element_by_id("query")
elem.send_keys("쿠팡")
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_class_name("direct_link")
elem.click()