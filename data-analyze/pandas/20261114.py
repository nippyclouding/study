import pandas as pd
import numpy as np

path1 = './datas/2.csv파일/2유형/회귀/전기사용량/elec_train.csv'
path2 = './datas/2.csv파일/2유형/회귀/전기사용량/elec_test.csv'

given = pd.read_csv(path1)
submit = pd.read_csv(path2)

# EDA -> 전처리 -> 훈련/검증 데이터 분리 -> 학습 -> 평가 -> 제출

# 1. EDA
print("1-1. EDA")
print(given.info())
print(submit.info())

print(given.isnull().sum())
print(submit.isnull().sum())

print(given.shape, submit.shape)

print(given.head())

print(submit.head())


# 결측치 처리 
# submit에는 결측치가 없으며 given 데이터만 결측치를 처리해준다.
print("1-2. 결측치 처리")
given['강수량'] = given['강수량'].fillna(given['강수량'].mean())
given['풍속'] = given['풍속'].fillna(given['풍속'].mean())
given['습도'] = given['습도'].fillna(given['습도'].mean())

print(given.head())

# 2. 전처리 : 범주형은 encoding, 수치형은 scaling
print("2-1. 전처리")

from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

encoder = LabelEncoder()
scaler = MinMaxScaler() # StandardScaler()

print("given 인코딩, 스케일링 전")
print(given.head())

# given 데이터 범주형 변수 인코딩
given['건물코드'] = encoder.fit_transform(given['건물코드'])

# given 데이터 수치형 변수 스케일링
numeric_list = ['기온', '강수량', '풍속', '습도', '전력소비량']
given[numeric_list] = scaler.fit_transform(given[numeric_list])

print("given 인코딩, 스케일링 확인")
print(given.head())

print("submit 인코딩, 스케일링 전")
print(submit.head())

# submit 데이터 범주형 변수 인코딩
submit['건물코드'] = encoder.fit_transform(submit['건물코드'])

# submit 데이터 수치형 변수 인코딩
submit['기온'] = scaler.fit_transform(submit[['기온']])
submit['강수량'] = scaler.fit_transform(submit[['강수량']])
submit['풍속'] = scaler.fit_transform(submit[['풍속']])
submit['습도'] = scaler.fit_transform(submit[['습도']])


print("submit 인코딩, 스케일링 확인")
print(submit.head())


# 3. 훈련/검증 데이터 분리
x = given.drop('전력소비량', axis = 1)
y = given['전력소비량']

print(x.head())
print(y.head())

from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size = 0.2)

# 4. 학습
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(x_train, y_train)



# 5. 평가
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, root_mean_squared_error

y_predict = model.predict(x_val)
rmse = root_mean_squared_error(y_val, y_predict)
print("rmse : ", rmse)


# 6. 제출

y_submit = model.predict(submit)
print(y_submit.shape)
result = pd.DataFrame(y_submit, columns = ['pred'])

result.to_csv('20261114.csv', index=False)

