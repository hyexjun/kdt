import pandas as pd
import glob
data_paths = glob.glob('./crawling_data/*')
print(data_paths)
df = pd.DataFrame()
for path in data_paths[1:]:
    df_temp = pd.read_csv(path, index_col=0)
    df = pd.concat([df, df_temp], ignore_index=True, axis='rows')
df_temp = pd.read_csv(data_paths[0])
df = pd.concat([df, df_temp], ignore_index=True, axis='rows')
df.info()
df.to_csv('./crawling_data/naver_news_220330.csv', index=False)