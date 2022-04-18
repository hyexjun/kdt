from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

category = ['Politics', 'Economic', 'Social',
            'Culture', 'World', 'IT']

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

df_titles = pd.DataFrame()

for i in range(6):
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i)
    resp = requests.get(url, headers=headers)

    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tags = soup.select('.cluster_text_headline')
    titles = []
    for title_tag in title_tags:
        titles.append(re.compile('[^가-힣a-zA-Z ]').sub(' ', title_tag.text))
    df_section_titles = pd.DataFrame(titles, columns=['title'])
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([df_titles, df_section_titles], axis='rows', ignore_index=True)
print(df_titles.head())
df_titles.info()
print(df_titles['category'].value_counts())
df_titles.to_csv('./crawling_data/naver_headline_news220331.csv', index=False)
print('Hi')
