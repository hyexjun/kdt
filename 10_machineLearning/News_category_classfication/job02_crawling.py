from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time

def crawl_title():
    try:
        title = driver.find_element_by_xpath('//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt[2]/a'.format(j, i)).text
        title = re.compile('[^가-힣a-zA-Z ]').sub(' ', title)
        title_list.append(title)
    except NoSuchElementException:
        print('NoSuchElementException')
        title = driver.find_element_by_xpath('//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt/a'.format(j, i)).text
        title = re.compile('[^가-힣a-zA-Z ]').sub(' ', title)
        title_list.append(title)

option = webdriver.ChromeOptions()
#options.add_argument('headless')
option.add_argument('lang=ko_KR')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=option)
driver.implicitly_wait(10)

category = ['Politics', 'Economic', 'Social',
            'Culture', 'World', 'IT']
page_num = [242, 374, 486, 71, 76, 125]
#//*[@id="section_body"]/ul[3]/li[5]/dl/dt/a
df_title = pd.DataFrame()
for l in range(1, 2):
    for k in range(1, page_num[l]+1):
        url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}#&date=%2000:00:00&page={}'.format(l, k)
        title_list = []
        driver.get(url)
        #time.sleep(0.5)
        for j in range(1, 5):
            for i in range(1, 6):
                try:
                    crawl_title()
                except StaleElementReferenceException:
                    driver.get(url)
                    time.sleep(0.5)
                    crawl_title()
                except:
                    print('error')

    df_section_title = pd.DataFrame(title_list, columns=['title'])
    df_section_title['category'] = category[l]
    df_title = pd.concat([df_title, df_section_title], axis='rows', ignore_index=True)
driver.close()
df_title.info()
print(df_title.category.value_counts())
df_title.to_csv('./crawling_data/naver_news_title_20220330.csv')
# naver_news_section명.csv