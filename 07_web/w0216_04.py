from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.naver.com")

browser.find_element_by_class_name("link_login").click()
browser.back()      # 페이지 뒤로 가기
browser.forward()   # 페이지 앞으로 가기
browser.refresh()   # 페이지 새로고침

browser.get("https://www.daum.net")
elem = browser.find_element_by_class_name("tf_keyword")
elem
elem.send_keys("시가총액")
elem.send_keys(Keys.ENTER)
browser.find_element_by_class_name("tf_keyword").clear()   # clear 뒤 () 빼먹으면 작동 안합니다..
elem
elem.send_keys("부동산")