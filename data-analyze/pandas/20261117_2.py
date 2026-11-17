# https://www.kaggle.com/code/lllmjkl/py-t1-5-expected-questions/edit?fromFork=1

import pandas as pd
import numpy as np

path = '/kaggle/input/bigdatacertificationkr/basic1.csv'
df = pd.read_csv(path)

print(df.shape)
print(df.info())
print(df.head())
print(df.isnull().sum())

condition1 = df['f4'] == 'ENFJ'
condition2 = df['f4'] == 'INFP'


# 표본표준편차 계산 요구 시 df[].std()
# 모표준편차 계산 요구 시 np.std()
std1 = df[condition1]['f1'].std()
std2 = df[condition2]['f1'].std()

print(np.trunc(np.abs(std1 - std2)))