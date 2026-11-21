# https://www.kaggle.com/code/agileteam/py-t1-6-expected-questions
# 결측치 제거 및 그룹 합계에서 조건에 맞는 값 찾아 출력
# basic1.csv에서 f1 컬럼이 결측인 행을 제거한 뒤, city와 f2를 기준으로 묶어(그룹화) 합계를 구하시오. 
# 그 결과에서 city가 '경기'이면서 f2가 0인 그룹의 f1 합계를 출력하시오.

import pandas as pd
import numpy as np

path = '/kaggle/input/bigdatacertificationkr/basic1.csv'

df = pd.read_csv(path)

print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())


# f1 컬럼이 결측인 행을 제거
df_cleaned = df.dropna(subset = ['f1'], axis=0)

# city와 f2를 기준으로 묶어(그룹화) 합계

grouped_list = ['city', 'f2']
result_series = df_cleaned.groupby(grouped_list)['f1'].sum()
print(result_series.head())

# city가 '경기'이면서 f2가 0인 그룹의 f1 합계
result_sum = result_series.loc[('경기', 0)]

print(result_sum)
 

