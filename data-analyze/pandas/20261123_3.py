path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_1_math.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_2_sales.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_3_spam.csv'


import pandas as pd
import numpy as np

print("=" * 50)
# 1-1
df = pd.read_csv(path2)

print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.info())

df['year'] = df['order_date'].str[:4]
print(df['year'].head())

df['month'] = df['order_date'].str[5:7]
print(df['month'].head())

price_series = df.groupby(['year', 'month'])['price'].sum()

price_series.sort_values(ascending=False, inplace=True)

print(price_series.head())

print(price_series.iloc[1]) # 두 번째로 높은 총 매출액


print(price_series.head(4)) # 2024-11

condition = (df['year'] == '2024') & (df['month'] == '11')

price_series = df[condition].groupby('category')['price'].sum()
price_series.sort_values(ascending=False, inplace=True)

print(int(np.trunc(price_series[0]))) # 6906.46
