import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
brower = webdriver.Chrome(options=options)
brower.maximize_window()
brower.get(url)

page_url = brower.page_source
soup = BeautifulSoup(page_url, "lxml")
print("접속 정보 :", soup.find("div", {"id":"detected_value"})).a["href"]