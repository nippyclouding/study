import pandas as pd
import numpy as np

path1 = pd.read_csv('./datas/2.csv파일/2유형/회귀/집값예측/house_price_train.csv')
path2 = pd.read_csv('./datas/2.csv파일/2유형/회귀/집값예측/house_price_test.csv')

given = pd.DataFrame(path1)
submit = pd.DataFrame(path2)

# 1. EDA
print("given info : " , given.info())
print("submit info : " , submit.info())

print(given.shape, submit.shape)

print("given null : " , given.isnull().sum())
print("given has only null in LotFrontage coloumn")
# print("submit null : " , submit.isnull().sum())
# print("submit data's columns datas are not null")

print(given['LotFrontage'].head())

# 2. preprocessing

# LotFrontage 은 수치형이기에 mean 값으로 결측치를 채운다. (범주형일 경우 mode() 등 사용)
lotFrontage_mean = given['LotFrontage'].mean()
given['LotFrontage'] = given['LotFrontage'].fillna(lotFrontage_mean)

print(given['LotFrontage'].head())

# 독립, 종속 변수 분리
given_x = given.drop(['Id', 'SalePrice'], axis = 1)
given_y = given['SalePrice']

submit_x = submit.drop('Id', axis = 1)

# 범주형 변수 인코딩 전 concat
concat_x = pd.concat([given_x, submit_x])
print(concat_x.shape)


# 범주형 변수 인코딩 (수치형 변수는 랜덤 포레스트 모델 사용 시 스케일링을 별도로 하지 않아도 된다)
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

# 범주형 변수 : Neighborhood, KitchenQual

concat_x['Neighborhood'] = encoder.fit_transform(concat_x['Neighborhood'])
concat_x['KitchenQual'] = encoder.fit_transform(concat_x['KitchenQual'])

# concat_x 분리
given_x = concat_x[:given_x.shape[0]]
submit_x = concat_x[given_x.shape[0]:]


# 3. 훈련/학습 데이터 분리
from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(given_x, given_y, test_size=0.2, random_state = 42) # test_size =0.2가 잘 외워지지 않는다. 암기하기


# 4. 학습
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state = 42)

model.fit(x_train, y_train)

# 5. 검증
y_predict = model.predict(x_val)

from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error
r2 = r2_score(y_val, y_predict)
mse = mean_squared_error(y_val, y_predict)
rmse = root_mean_squared_error(y_val, y_predict)

print("r2 : ", r2)
print("mse : ", mse)
print("rmse : ", rmse)


# 6. 제출
model = RandomForestRegressor()
model.fit(given_x, given_y)

submit_y = model.predict(submit_x)
print(submit_y.shape)
df = pd.DataFrame(submit_y, columns=['pred'])

df.to_csv('20261115.csv', index=False)