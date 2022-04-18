import pandas as pd

d1=pd.read_csv('./crawling_data/naver_news_title1.csv', sep=',', index_col=False, dtype='unicode')
d2=pd.read_csv('./crawling_data/naver_news_title2.csv', sep=',', index_col=False, dtype='unicode')
d3=pd.read_csv('./crawling_data/naver_news_title3.csv', sep=',', index_col=False, dtype='unicode')
d4=pd.read_csv('./crawling_data/naver_news_title4.csv', sep=',', index_col=False, dtype='unicode')


df = pd.concat([d1,d2,d3,d4], ignore_index=True)

df.to_csv('./crawling_data/naver_news.csv')