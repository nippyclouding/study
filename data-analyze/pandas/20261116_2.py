# 2과목 - 이진 분류

import pandas as pd
import numpy as np

path1 = './datas/2.csv파일/2유형/이진분류/타이타닉/titanic_train.csv'
path2 = './datas/2.csv파일/2유형/이진분류/타이타닉/titanic_test.csv'

given = pd.read_csv(path1)
submit = pd.read_csv(path2)

# EDA
print(given.shape, submit.shape)
print(given.head())
print(submit.head())

print(given.isnull().sum())
print(submit.isnull().sum())

print(given.info())
print(submit.info())


# preprocessing
given_x = given.drop(columns=['PassengerId', 'Survived'])
given_y = given['Survived']
submit_x = submit.drop('PassengerId', axis = 1)

print(given_x.info())
print(given_y.info())

concat_x = pd.concat([given_x, submit_x])

print(concat_x.info())
print(concat_x.shape)
print(concat_x.isnull().sum())

age_mean = concat_x['Age'].mean()
fare_mean = concat_x['Fare'].mean()
embarked_mode = concat_x['Embarked'].mode()[0]

concat_x['Age'] = concat_x['Age'].fillna(age_mean)
concat_x['Fare'] = concat_x['Fare'].fillna(fare_mean)
concat_x['Embarked'] = concat_x['Embarked'].fillna(embarked_mode)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

concat_x['Sex'] = encoder.fit_transform(concat_x['Sex'])
concat_x['Embarked'] = encoder.fit_transform(concat_x['Embarked'])

given_x = concat_x[:given_x.shape[0]]
submit_x = concat_x[given_x.shape[0]:]

print(given_x.head())
print(submit_x.head())
print(given_x.shape, submit_x.shape)

# train/val split
from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(given_x, given_y, test_size=0.2, stratify=given_y, random_state=42)

print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)

# 학습
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

model.fit(x_train, y_train)

# 0 또는 1 중 하나로 예측
y_predict = model.predict(x_val)

# 1일 확률 예측
y_proba = model.predict_proba(x_val)[:,1]

# 성능
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score

print(roc_auc_score(y_val, y_proba))
print(accuracy_score(y_val, y_predict))
print(f1_score(y_val, y_predict))


# 제출

model = RandomForestClassifier()
model.fit(given_x, given_y)

submit_y = model.predict(submit_x)
df = pd.DataFrame(submit_y, columns=['pred'])
df.to_csv('20261116_2.csv', index=False)