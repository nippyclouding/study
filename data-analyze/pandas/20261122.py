import pandas as pd
import numpy as np



given = pd.read_csv('datas/2.csv파일/2유형/다중분류/휴대폰가격/phone_price_train.csv')
submit_x = pd.read_csv('datas/2.csv파일/2유형/다중분류/휴대폰가격/phone_price_test.csv')

# eda
print("GIVEN EDA")
print(given.shape)
print(given.head())
print(given.isnull().sum())
print(given.info())

print("SUBMIT_X EDA")
print(submit_x.shape)
print(submit_x.head())
print(submit_x.isnull().sum())
print(submit_x.info())

# preprocessing

given_x = given.drop('price_range', axis = 1)
given_y = given['price_range']

concat_x = pd.concat([given_x, submit_x])

print(concat_x.isnull().sum())

concat_x = pd.get_dummies(concat_x, dtype=int)

given_x = concat_x[:given_x.shape[0]]
submit_x = concat_x[given_x.shape[0]:]

# train_test_split
from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(given_x, given_y, test_size=0.2, stratify=given_y, random_state=42)
print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)

# model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)

# test
y_predict = model.predict(x_val)
y_proba = model.predict_proba(x_val) # 다중 분류는 [:,1] 를 하지 않고 이진 분류에서만 적용

from sklearn.metrics import roc_auc_score, f1_score, precision_score, accuracy_score

roc_auc = roc_auc_score(y_val, y_proba, average = 'macro', multi_class='ovr')
precision = precision_score(y_val, y_predict, average = 'macro')
f1 = f1_score(y_val, y_predict, average = 'macro')
accuracy = accuracy_score(y_val, y_predict)

print(roc_auc, precision, f1, accuracy)

# submit

model = RandomForestClassifier(random_state=42)
model.fit(given_x, given_y)

y_predict = model.predict(submit_x)

df = pd.DataFrame(y_predict, columns=['pred'])
df.to_csv('result.csv', index=False)

