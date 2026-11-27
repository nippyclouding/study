path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_1_emission.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_2_indoor.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_3_marketing.csv'
path4 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/2_1_game_level_test.csv'
path5 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/2_1_game_level_train.csv'
path6 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/3_1_diabetes.csv'
path7 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/3_2_promotion.csv'

import pandas as pd
import numpy as np

df = pd.read_csv(path6)
df_dropped = df.drop('ID', axis=1)

import statsmodels.formula.api as smf

model = smf.logit('Outcome ~ Age + Diabetes_History', data=df_dropped).fit()
print(model.summary())
print(round(np.exp(model.params['Diabetes_History[T.Pre]']), 3)) # 2.023

df['predict'] = model.predict(df_dropped)
df.sort_values(['predict', 'ID'], ascending=[False, True], inplace=True)
print(int(df['Glucose'].iloc[0])) # 89


# 실제
df['Outcome']
# 예측
pred = df['predict'] >= 0.5

from sklearn.metrics import recall_score

recall = recall_score(df['Outcome'], pred)
print(round(recall, 3))