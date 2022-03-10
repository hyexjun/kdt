import FinanceDataReader as fdr

df = fdr.DataReader('005930','2020-01-01', '2022-01-19')
df.reset_index(inplace=True)
#close 값이 제일 낮은 row의 date 구하기
lowdayindex= df['Close'].argmin()
lowday = df.loc[lowdayindex]['Date']
# name= df['Name']
    
print(df)