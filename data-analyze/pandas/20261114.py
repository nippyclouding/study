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


# 스케일링 : 회귀 모델 - 랜덤 포레스트 모델은 수치형 변수에 대해 given, submit 데이터 둘 다 스케일링이 필수적인 것은 아니다.
# 스케일링 시 r2_score 0.8869022054401667, 스케일링을 하지 않을 경우 r2_score 0.8620703938554899

# given 데이터 수치형 변수 스케일링
numeric_list = ['기온', '강수량', '풍속', '습도'] 
# 종속변수 전력소비량은 스케일링하지 않아야 한다.
# 종속변수 전력소비량까지 스케일링하게 되면 모델이 예측하는 값도 스케일링되어 예측이 된다. 

given[numeric_list] = scaler.fit_transform(given[numeric_list])

print("given 인코딩, 스케일링 확인")
print(given.head())

print("submit 인코딩, 스케일링 전")
print(submit.head())

# submit 데이터 범주형 변수 인코딩
# 제출용 데이터에서는 스케일링, 인코딩을 새로 하지 않고 기존에 스케일링된 내역을 따라간다, fit_transform()이 아닌 transform()만 사용
submit['건물코드'] = encoder.transform(submit['건물코드'])

# submit 데이터 수치형 변수 인코딩
# fit_transform()이 아닌 transform()만 사용 시 이전 fit_transform()과 동일한 파라미터를 전달해야 한다.
submit[numeric_list] = scaler.transform(submit[numeric_list])
#submit['기온'] = scaler.transform(submit[['기온']])
#submit['강수량'] = scaler.transform(submit[['강수량']])
#submit['풍속'] = scaler.transform(submit[['풍속']])
#submit['습도'] = scaler.transform(submit[['습도']])


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
r2_score = r2_score(y_val, y_predict)
print("rmse : ", rmse)
print("r2_score", r2_score)


# 6. 제출

y_submit = model.predict(submit)
print(y_submit.shape)
result = pd.DataFrame(y_submit, columns = ['pred'])

result.to_csv('20261114.csv', index=False)



# -----------------------------------------------------------------------------------------------
# given 데이터의 범주형 변수에 a, b, c 데이터가 있고 
# submit 데이터의 범주형 변수에 a, b, c, d 데이터가 있을 경우 
# given 데이터를 fit_transform() 인코딩 후 submit 데이터를 transform() 인코딩 시 에러가 발생한다.

# 이 경우 given, submit 독립변수 데이터를 concat한다.
x = given.drop('전력소비량', axis = 1)
y = given['전력소비량']

concat_given_submit = pd.concat([x, submit]) # axis = 0 생략, 기본값, 행들을 합친다.

# concat_given_submit 속에는 범주형, 수치형 데이터들이 함께 있다.
# pd.get_dummies(데이터 프레임) 을 통해 데이터 프레임 속 범주형 변수만 원 핫 인코딩을 실행할 수 있다.
concat_given_submit = pd.get_dummies(concat_given_submit)

# 위처럼 두 데이터를 concat 이후 pd.get_dummies로 인코딩 시 submit 데이터에 a, b, c, d가 있어도 인코딩이 가능하다.
# 인코딩 후 다시 x, submit 으로 분리한다.

x = concat_given_submit[:x.shape[0]]
submit = concat_given_submit[given.shape[0]:]
# -----------------------------------------------------------------------------------------------