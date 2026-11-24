path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_1_emission.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_2_indoor.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_3_marketing.csv'
path4 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/2_1_game_level_test.csv'
path5 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/2_1_game_level_train.csv'
path6 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/3_1_diabetes.csv'
path7 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/3_2_promotion.csv'

import pandas as pd
import numpy as np

# 1 - 1 
df = pd.read_csv(path1)

year_emission_series = df.groupby(['year', 'country'])['emission'].sum()
year_emission_series.sort_values(ascending=False, inplace=True)
#print(year_emission_series.head())
#print(year_emission_series.value_counts())


df_new = pd.DataFrame()
df_new = year_emission_series.reset_index()
#print(df_new)

#print(df_new.groupby('country')['year'].count())
#select country, count(*) from .. 
#group by country



# 1 - 2
df = pd.read_csv(path2)
print(df.isnull().sum())

# 최대인 열 : S2_Temp

s2_temp_median = df['S2_Temp'].median()
df['S2_Temp'] = df['S2_Temp'].fillna(s2_temp_median)
print(df.isnull().sum())

print(df['S2_Temp'].head())

print(round(df['S2_Temp'].mean(), 3)) # 25.135



# 1 - 3 
df = pd.read_csv(path3)

def judge_cancel (row) :
    if row.str[:1] == 'C' :
        row['cancel'] = 'T'
    else :
        row['cancel'] = 'F'
#judge_cancel(df['transaction_code'])



# 2
given = pd.read_csv(path5)
submit_x = pd.read_csv(path4)

# eda
print("*" * 100)
print(given.shape)
print(submit_x.shape)

print(given.head())
print(submit_x.head())

# preprocessing
print("*" * 100)
print(given.isnull().sum())    # 결측치 없음
print(submit_x.isnull().sum()) # 결측치 없음

given_x = given.drop('Game_Level', axis=1)
given_y = given['Game_Level']

concat_x = pd.concat([given_x, submit_x])
print(concat_x.shape)

print(concat_x.info())
concat_x = pd.get_dummies(concat_x)

given_x = concat_x[:given_x.shape[0]]
submit_x = concat_x[given_x.shape[0]:]
print(given_x.shape, submit_x.shape)

# train_test_split
print("*" * 100)
from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(given_x, given_y, stratify=given_y, test_size=0.2, random_state=42)

print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)

# modeling
print("*" * 100)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)

# metrics
print("*" * 100)
from sklearn.metrics import f1_score, precision_score, accuracy_score, roc_auc_score

y_predict = model.predict(x_val)
y_proba = model.predict_proba(x_val) # [:,1] 을 쓰지 않는다

auc_roc = roc_auc_score(y_val, y_proba, average='macro', multi_class='ovr')
f1 = f1_score(y_val, y_predict, average = 'macro')
precision = precision_score(y_val, y_predict, average='macro')
accuracy = accuracy_score(y_val, y_predict)

print(auc_roc, f1, precision, accuracy)

# submit
print("*" * 100)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(given_x, given_y)

submit_y = model.predict(submit_x) # 확률을 요구 시 predict_proba, 현재는 0, 1, 2 등 결과값을 요구
print(submit_y.shape)
print(submit_y)
df = pd.DataFrame(submit_y, columns=['pred'])
df.to_csv('result.csv', index=False)


# 3 - 1

df = pd.read_csv(path6)

import statsmodels.formula.api as smf

model = smf.logit('Outcome ~ Age + Diabetes_History', data = df).fit()

print(model.summary())
print(round(np.exp(model.params['Diabetes_History[T.Pre]'] * 1), 3))
# 답 : 2.011

# 3 - 2
df['prob'] = model.predict(df)
print(df['prob'].head())

df.sort_values(['prob', 'ID'], ascending=[False, True], inplace=True)

print(df.head())
