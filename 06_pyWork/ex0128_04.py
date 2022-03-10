import requests
from bs4 import BeautifulSoup
import soupsieve


url = "https://www.naver.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.find("a",{"class":"link_login"}).attrs)

# login_naver = soup.find("i",{"class":"ico_naver"})
# print(login_naver.find("span",{"class":"blind"}).get_text())

a1= soup.find("div",{"id":"account"})
# print(a1.next_sibling.next_sibling)
print(a1.find_next_sibling("div").previous_sibling.previous_sibling)
print(a1.find_next_sibling("div").find_previous("div"))