import pandas as pd
import numpy as np

path1 = './datas/2.csv파일/2유형/이진분류/타이타닉/titanic_train.csv'
path2 = './datas/2.csv파일/2유형/이진분류/타이타닉/titanic_test.csv'

given = pd.read_csv(path1)
submit = pd.read_csv(path2)


# 1. EDA
print(given.shape, submit.shape)
print(given.info())
print(submit.info())
print(given.isnull().sum())
print(submit.isnull().sum())


# 2. 전처리
given_x = given.drop(['PassengerId', 'Survived'], axis = 1)
given_y = given['Survived']

submit_x = submit.drop(['PassengerId'], axis = 1)

# 실험용, 제출용 데이터 concat
concat_x = pd.concat([given_x, submit_x])
# concat_x = pd.concat(['given_x', 'submit_x']) => 'given_x', 'submit_x' 문자열을 넣는 것이 아니다.

# 결측치 처리
embarked_mode = concat_x['Embarked'].mode()[0]
age_mean = concat_x['Age'].mean()
fare_mean = concat_x['Fare'].mean()

concat_x['Embarked'] = concat_x['Embarked'].fillna(embarked_mode)
concat_x['Fare'] = concat_x['Fare'].fillna(fare_mean)
concat_x['Age'] = concat_x['Age'].fillna(age_mean)

# 범주형 변수 인코딩 
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
concat_x['Sex'] = encoder.fit_transform(concat_x['Sex'])
concat_x['Embarked'] = encoder.fit_transform(concat_x['Embarked'])

# 인코딩 후 분리 
given_x = concat_x[:given_x.shape[0]]
submt_x = concat_x[given_x.shape[0]:]

print(given_x.isnull().sum(), submt_x.isnull().sum())


# 3. 훈련용/검증용 데이터 분리
from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(given_x, given_y, test_size=0.2, stratify=given_y, random_state=42)

print("given 데이터 훈련/검증용 분리")
print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)

# 4. 모델 학습
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)

# 5. 성능 측정

y_proba = model.predict_proba(x_val)[:,1]
y_predict = model.predict(x_val)

from sklearn.metrics import roc_auc_score, accuracy_score, f1_score

roc_auc = roc_auc_score(y_val, y_proba)
accuracy = accuracy_score(y_val, y_predict)
f1 = f1_score(y_val, y_predict)

print(roc_auc, accuracy, f1)

# 6. 제출
model = RandomForestClassifier()
model.fit(given_x, given_y) # 재학습, 80:20 데이터 분류 이전의 모든 데이터를 학습

submit_y = model.predict(submt_x)
print(submit_y.shape)
# print(submit_y.head()) 'numpy.ndarray' object has no attribute 'head'

df = pd.DataFrame(submit_y, columns=['pred'])
print(df.head())

df.to_csv('20261115_3.csv', index=False)
