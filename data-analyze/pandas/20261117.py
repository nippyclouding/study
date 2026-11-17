import pandas as pd
import numpy as np

df = pd.read_csv("./datas/2.csv파일/1유형/hr_data.csv")

print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())

# df['Email'].str.split("@")[1] 처럼 .str[1]을 하지 않을 경우 1번째 인덱스의 행 한 줄이 출력된다.
df['Domain'] = df['Email'].str.split("@").str[1]
print(df.head())

condition1 = df['Domain'] == "bilearner.com"

# condition이라는 Boolean 조건을 만족하는 행만 필터링하여 새로운 DataFrame을 반환
# boolean 이 적용된 데이터프레임 결과는 '데이터프레임'

df = df[condition1] 
print("도메인이 bilearner.com 인 직원의 수 : ", int(df.shape[0])) # 도메인이 bilearner.com 인 직원의 수

condition2 = df['Name'].str.len() >= 6
df = df[condition2]

print("이름의 문자 길이가 6자리 이상인 직원의 수 : ", int(df.shape[0]))