path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_1_emission.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_2_indoor.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_3_marketing.csv'
path4 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/2_1_game_level_test.csv'
path5 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/2_1_game_level_train.csv'
path6 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/3_1_diabetes.csv'
path7 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/3_2_promotion.csv'

import pandas as pd
import numpy as np

df = pd.read_csv(path1)


#1. 

print(df.shape)
print(df.head())
print(df.value_counts('year'))
print(df.groupby(['year', 'country'])['emission'])

#3.
df = pd.read_csv(path3)
condition = df['transaction_code'].str[:1] == 'C'

df['cancel'] = np.where(condition, 'T', 'F')

df['amount'] = np.where(df['cancel'] == 'T', df['amount'] * -1, df['amount'])



condition = np.abs(df['amount']) != df['amount']
df_copy = df[condition].copy()
print(df_copy.head())
print(df_copy.shape)


df_copy['amount'] = df_copy['amount'] * -1
df_copy['cancel_sum'] = df_copy.groupby('customer_id')['amount'].sum()
print(df_copy['cancel_sum'])
df_copy['abs'] = np.abs(df_copy['cancel_sum'])
df_copy.sort_values('cancel_sum', ascending=False, inplace=True)
print(df_copy['cancel_sum'].head())


# 235899
print(df.groupby('product_code')['amount'].sum().sort_values(ascending=False).iloc[0])