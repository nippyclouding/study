path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_1_math.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_2_sales.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_3_spam.csv'


import pandas as pd
import numpy as np

print("=" * 50)
# 1-3
df = pd.read_csv(path3)

print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.info())

df['count'] = df['Message'].str.split().str.len()
print(df.head())

category_series = df.groupby('Category')['count'].mean()
print(category_series.head())

print(round(np.abs(category_series['spam'] - category_series['ham']), 3)) # 9.502