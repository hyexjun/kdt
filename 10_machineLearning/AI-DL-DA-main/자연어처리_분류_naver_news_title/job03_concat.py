
import pandas as pd
import glob

data_paths = glob.glob('./crawling_data/*')  # glob 모듈의 glob 함수는 사용자가 제시한 조건에 맞는 파일명을 리스트 형식으로 반환한다.
print(data_paths)
df= pd.DataFrame()

# df_list = []
for path in data_paths[2:8]:
    df_temp = pd.read_csv(path, index_col=0)
    df = pd.concat([df, df_temp], ignore_index=True, axis='rows')

# df_temp = pd.read_csv(data_paths[0])  # ???
df = pd.concat([df, df_temp], ignore_index=True, axis='rows')
df.info()
df.to_csv('./crawling_data/naver_news_220330.csv', index=False)