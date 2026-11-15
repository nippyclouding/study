#https://www.kaggle.com/code/lllmjkl/py-t1-3-map-expected-questions/edit

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

path = '/kaggle/input/bigdatacertificationkr/basic1.csv'
df = pd.read_csv(path)

# 1. EDA
print(df.info())
print(df.shape)
print(df.isnull().sum())

print("결측치 비율 : ", df.isnull().sum() / df.shape[0] ) # 해당 열의 null 데이터 개수 / 해당 열의 전체 행 개수
print(df.head())

# 2. 전처리 
df = df.drop('f3', axis = 1)

df['f1'] = df['f1'].fillna(df.groupby('city')['f1'].transform('median'))

print(np.trunc(df['f1'].mean()))




# 컬럼별 결측치 비율
null_ratio = df.isnull().sum() / df.shape[0]

# 결측치 비율이 80% 초과인 컬럼 추출
drop_columns = null_ratio[null_ratio > 0.8].index
# df[condition].index : index(key) 값 리턴

# 해당 컬럼 삭제
df = df.drop(drop_columns, axis=1)