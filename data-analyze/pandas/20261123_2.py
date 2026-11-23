#'/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/1.ipynb파일/10_Exam_lab.ipynb'
path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_1_math.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_2_sales.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_3_spam.csv'


import pandas as pd
import numpy as np

print("=" * 50)
# 1-1
df = pd.read_csv(path1)

print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.info())

print(df['Subtopic'].value_counts())

print(df.head(20))

grouped_series = df.groupby('Subtopic')['Answer'].sum() / df.groupby('Subtopic')['Answer'].count()
print(grouped_series.head(20))
print(grouped_series.info())

grouped_series.sort_values(ascending = False, inplace=True)
print(grouped_series.head(20))

print(round(grouped_series.iloc[2], 3))