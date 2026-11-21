import pandas as pd
import numpy as np

path1 = './datas/2.csv파일/2유형/회귀/집값예측/house_price_train.csv'
path2 = './datas/2.csv파일/2유형/회귀/집값예측/house_price_test.csv'

given = pd.read_csv(path1)
submit_x = pd.read_csv(path2)

# EDA
print(given.shape)
print(given.head())
print(given.isnull().sum())
print(given.info())

print(submit_x.shape)
print(submit_x.head())
print(submit_x.isnull().sum())
print(submit_x.info())


# Preprocessing : fillna -> preprocessing
given_x = given.drop('SalePrice', axis = 1)
given_y = given['SalePrice']

concat_x = pd.concat([given_x, submit_x])
print(concat_x.shape)
print(concat_x.isnull().sum())

mean_LotFrontage = concat_x['LotFrontage'].mean()
concat_x['LotFrontage'] = concat_x['LotFrontage'].fillna(mean_LotFrontage)
print(concat_x.isnull().sum())

print("Labeling columns : Neighborhood, KitchenQual")

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

concat_x['Neighborhood'] = encoder.fit_transform(concat_x['Neighborhood'])
concat_x['KitchenQual'] = encoder.fit_transform(concat_x['KitchenQual']) 
# 인코딩, 스케일링 시 fit가 아니라 fit_transform

given_x = concat_x[:given_x.shape[0]]
submit_x = concat_x[given_x.shape[0]:]

# train_test_split
from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(given_x, given_y, test_size=0.2, random_state=42)

print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)

# train
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=42)
model.fit(x_train, y_train)

# evaluate
y_predict = model.predict(x_val)

from sklearn.metrics import root_mean_squared_error, mean_squared_error, mean_absolute_error, r2_score

rmse = root_mean_squared_error(y_val, y_predict)
mse = mean_squared_error(y_val, y_predict)
mae = mean_absolute_error(y_val, y_predict)
r2 = r2_score(y_val, y_predict)

print(rmse, mse, mae, r2)

# submit
model.fit(given_x, given_y)

submit_y = model.predict(submit_x)

df = pd.DataFrame(submit_y, columns = ['pred'])
df.to_csv('result.csv', index=False)
