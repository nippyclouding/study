# 다중 분류 모델 개발

import pandas as pd
import numpy as np

path1 = 'datas/2.csv파일/2유형/다중분류/휴대폰가격/phone_price_train.csv'
path2 = 'datas/2.csv파일/2유형/다중분류/휴대폰가격/phone_price_test.csv'

given = pd.read_csv(path1)
submit = pd.read_csv(path2)


# EDA -> preprocessing -> divide -> training -> evaluate -> predict

# 1. EDA
print(given.shape) 
print(given.head())
print(given.isnull().sum())
print(given.info())

print(submit.shape) 
print(submit.head())
print(submit.isnull().sum())
print(submit.info())

# 2. preprocessing
# 범주형 변수는 없으므로 수치형 변수만 전처리
# 결측치가 없으므로 따로 결측치 처리를 하지 않는다.

from sklearn.preprocessing import MinMaxScaler, StandardScaler

scaler = MinMaxScaler()

columns_x = given.columns.tolist()
columns_x.remove('price_range')

given_x = given.drop('price_range', axis = 1)
given_y = given['price_range']
submit_x = submit.copy()


concat_x = pd.concat([given_x, submit_x])
concat_x[columns_x] = scaler.fit_transform(concat_x[columns_x])

given_x = concat_x[:given_x.shape[0]]
submit_x = concat_x[given_x.shape[0]:]

# given[columns_x] = scaler.fit_transform(given[columns_x])
# submit[columns_x] = scaler.transform(submit[columns_x])

# 3. divide
from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(given_x, given_y, test_size=0.2, stratify=given_y, random_state = 42)

print(x_train.shape, x_val.shape, y_train.shape, y_train.shape)

# 4. training
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

model.fit(x_train, y_train)


# 5. evaluate 
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score, precision_score

y_predict = model.predict(x_val)
y_proba = model.predict_proba(x_val)

roc = roc_auc_score(y_val, y_proba, average = 'macro', multi_class = 'ovr')
f1 = f1_score(y_val, y_predict, average = 'macro')
precision = precision_score(y_val, y_predict, average = 'macro')
accuracy = accuracy_score(y_val, y_predict) # accuracy_score은 별도 추가하는 파라미터가 없으며 추가 시 에러 발생

print(roc, f1, accuracy, precision)


# 6. predict

model = RandomForestClassifier(random_state = 42)
model.fit(given_x, given_y)

submit_y = model.predict(concat_x)
df = pd.DataFrame(submit_y, columns = ['pred'])
df.to_csv('20261119.csv', index=False)