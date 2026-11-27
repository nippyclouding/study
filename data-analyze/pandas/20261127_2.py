path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_1_math.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_2_sales.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_3_spam.csv'

path4 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/2_1_gas_test.csv'
path5 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/2_1_gas_train.csv'

path6 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/3_1_employee.csv'
path7 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/3_2_house.csv'

import pandas as pd
import numpy as np

df = pd.read_csv(path2)

print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.info())

df['year'] = df['order_date'].str[:4]
df['month'] = df['order_date'].str[5:7]
print(df['year'].head(), df['month'].head())

grouped_list = ['year', 'month']

grouped_series = df.groupby(grouped_list)['price'].sum()

print(grouped_series.head())
grouped_series.sort_values(ascending=False, inplace=True)

print(grouped_series.iloc[1])

# 매출기준네번째로높은연도/월을찾고해당연도/월의카테고리별 총매출액을집계한뒤, 그중가장높은총매출액을구한다.

print(grouped_series.index[3], grouped_series.iloc[3])

grouped_list = ['year', 'month', 'category']
grouped_list = df.groupby(grouped_list)['price'].max()


print(grouped_list.shape)
print(grouped_list)
