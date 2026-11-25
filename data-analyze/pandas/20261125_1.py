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

# 독립변수 : Age, Diabetes_History, Glucose
# 종속변수 : Outcome

import statsmodels.formula.api as smf

model = smf.logit('Outcome ~ Age + Diabetes_History', data=df).fit()

print(model.summary())

answer = np.exp(model.params['Diabetes_History[T.Pre]'] * 1)
print(round(answer, 3)) # 2.011

df['predict'] = model.predict(df)
df.sort_values(['predict', 'ID'], ascending=[False, True], inplace=True)
print(df['Glucose'].iloc[0]) 

# .iloc[0]과 [0]의 차이
df['Glucose'].iloc[0]  # 첫 번째 위치의 데이터
df['Glucose'].loc[0]   # 인덱스 라벨이 0인 데이터

print(df['Glucose'].head())
# 답 : 158


from sklearn.metrics import recall_score

condition = df['predict'] >= 0.5
recall = recall_score(df['Outcome'], condition) # 시리즈끼리 비교
print(round(recall, 3))