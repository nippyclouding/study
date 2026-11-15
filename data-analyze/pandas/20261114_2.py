import pandas as pd
import numpy as np

from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor




path1 = pd.read_csv('./datas/2.csv파일/2유형/회귀/집값예측/house_price_train.csv')
path2 = pd.read_csv('./datas/2.csv파일/2유형/회귀/집값예측/house_price_test.csv')

given = pd.DataFrame(path1)
submit = pd.DataFrame(path2)

# 1. EDA
print(given.info())
print(given['Neighborhood'].value_counts())
print(given['KitchenQual'].value_counts())
print(given.groupby('Neighborhood').size())


print(submit.info())


# 2. preprocessing
print("LotFrontage 결측치 대체")
print(given['LotFrontage'].head())
given['LotFrontage'] = given['LotFrontage'].fillna(given['LotFrontage'].mean())
print(given['LotFrontage'].head())

print("given 독립, 종속변수 분리")
x = given.drop(['Id', 'SalePrice'], axis = 1)
y = given['SalePrice']

submit = submit.drop('Id', axis = 1)

print("given, submit 스케일링, 인코딩")
# y 값은 스케일링, 인코딩하지 않는다, 모델 학습 시 전처리된 값으로 y를 학습하면 제출 시에도 전처리된 값으로 제출이 된다.

# list_encoding = ['Neighborhood', 'KitchenQual'] 범주형 변수 인코딩은 리스트로 불가, 하나씩 가능하다.
list_scaling = ['LotFrontage', 'OverallQual', 'YearBuilt', 'YearRemodAdd', 'Fireplaces', 'GarageCars', 'GarageArea']


scaler = MinMaxScaler()
#x[list_scaling] = scaler.fit_transform(x[list_scaling])
# 수치형 변수 전처리를 하지 않았을 경우가 했을 때보다 성능이 더 좋다 (r2_score 0.79 -> 0.80으로 증가)

encoder = LabelEncoder()


print("인코딩, fit_transform, x의 범주형 변수와 다른 범주형 변수가 submit에 포함되어 있어 concat")
concat_given_submit = pd.concat([x, submit])
concat_given_submit['KitchenQual'] = encoder.fit_transform(concat_given_submit['KitchenQual'])
concat_given_submit['Neighborhood'] = encoder.fit_transform(concat_given_submit['Neighborhood'])

print("범주형 변수 인코딩 후 다시 분리")
x = concat_given_submit[:x.shape[0]]
submit = concat_given_submit[x.shape[0]:]

print("concat 데이터프레임으로 인코딩을 했기 때문에 제출용 변수는 재인코딩 필요가 없다")
#submit['KitchenQual'] = encoder.transform(submit['KitchenQual'])
#submit['Neighborhood'] = encoder.transform(submit['Neighborhood'])


# 3. 훈련/검증용 데이터 분리
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size = 0.2, random_state = 42)

print(x_train.shape, y_train.shape, x_val.shape, y_val.shape)


# 4. 학습
model = RandomForestRegressor()
model.fit(x_train, y_train)


# 5. 성능 측정 
y_predict = model.predict(x_val)
r2 = r2_score(y_val, y_predict)

mse = mean_squared_error(y_val, y_predict)

rmse = root_mean_squared_error(y_val, y_predict)

print(r2, mse, rmse)

# 6. 제출

model = RandomForestRegressor()
model.fit(x, y)


y_submit = model.predict(submit)
print(y_submit.shape)

df = pd.DataFrame(y_submit, columns = ['pred'])

df.to_csv('20261114_2.csv', index = False)
