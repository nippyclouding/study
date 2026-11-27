path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_1_math.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_2_sales.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_3_spam.csv'

path4 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/2_1_gas_test.csv'
path5 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/2_1_gas_train.csv'

path6 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/3_1_employee.csv'
path7 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/3_2_house.csv'

import pandas as pd
import numpy as np

df = pd.read_csv(path1)

print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.info())

grouped_series = df.groupby('Subtopic')['Answer'].sum() / df.groupby('Subtopic')['Answer'].count()
print(grouped_series.head())
print(grouped_series.info())
grouped_series.sort_values(ascending=False, inplace=True)
print(round(grouped_series.iloc[2], 3))