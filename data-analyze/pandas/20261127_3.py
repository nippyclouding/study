path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/1_1_library.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/1_2_delivery.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/1_3_student.csv'
path4 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/2_1_maintenance_test.csv'
path5 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/2_1_maintenance_train.csv'
path6 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/3_1_exam_score.csv'
path7 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/3_2_student_learning.csv'

import pandas as pd
import numpy as np


# 1유형 1
df = pd.read_csv(path1)
condition = df['title'].str.contains('Python') | df['title'].str.contains('파이썬') | df['title'].str.contains('python')
print(df[condition].shape[0]) # 95

condition_2 = df['available'] == 'Y'
print(df.head())
print(df.info())
condition_3 = (df['publication_year'] >= 2021) & (df['rating'] > 4.0)
print(df[condition_2 & condition_3].shape[0]) # 127
# 대출 순서가 y인 것만 구한다는 1번과 독립인 조건이겠지 라고 판단해서 df에 적용 (1번 결과에 적용하지 않음)

# 1유형 2
df = pd.read_csv(path2)
df['weekday_orders'] = df['weekday_orders'].fillna(df['weekday_orders'].mean())
df['weekend_orders'] = df['weekend_orders'].fillna(df['weekend_orders'].mean())
df['total_orders'] = df['weekday_orders'] + df['weekend_orders']

grouped_series = df.groupby('district')['total_orders'].mean()
grouped_series.sort_values(ascending=False, inplace=True)
print(grouped_series.head())
print(grouped_series.index[0], grouped_series.index[1]) # 강남구 송파구

idx_nm1 = grouped_series.index[0]
idx_nm2 = grouped_series.index[1]

value1 = grouped_series[idx_nm1]
value2 = grouped_series[idx_nm2]

n1 = len(grouped_series)
n2 = len(grouped_series)
print(n1, n2)


s1 = np.var(grouped_series, ddof=1)
s2 = np.var(grouped_series, ddof=1)
print(s1, s2)

sp = (((n1 - 1) * (s1 ** 2)) + ((n2 - 1) * (s2 ** 2))) / (n1 + n2 + 1)
print(round(sp, 3))
# 두 자치구를 구하라는데 맞을까 .. 

# 1유형 3 : 이 문제는 틀렸다고 해줘. 실전에 나온다고 하면 무조건 틀릴거같아. 
df = pd.read_csv(path3)
print(df.head())

def check(df) :
    condition = df['phone'].str.len() <= 3
    df.loc[condition, 'sub'] = df.loc[condition, 'phone']
    df.loc[condition, 'phone'] = df.loc[condition, 'age']
    df.loc[condition, 'age'] = df.loc[condition, 'extra']
    df['age'] = pd.to_numeric(df['age'])
    return df
check(df)
print(df.head())

print(round(df['age'].mean()))

print(np.abs(df.groupby('department_code')['department_code'].count() - df.groupby('department_code')['sub'].count()).idxmax())


# 2유형

# eda -> preprocessing -> train_test_split -> modeling -> predict -> submit

given = pd.read_csv(path5)
submit_x = pd.read_csv(path4)

print("=" * 100)
print(given.shape)
print("=" * 100)
print(given.head())
print("=" * 100)
print(given.isnull().sum())
print("=" * 100)
print(given.info())

print("=" * 100)
print(submit_x.shape)
print("=" * 100)
print(submit_x.head())
print("=" * 100)
print(submit_x.isnull().sum())
print("=" * 100)
print(submit_x.info())


drop_list = ['id', 'Maintenance_Cost']
given_x = given.drop(drop_list, axis=1) # subset = dropna
given_y = given['Maintenance_Cost']

submit_x = submit_x.drop('id', axis=1)

from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(given_x, given_y, random_state=42)
print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=42)
model.fit(x_train, y_train)

from sklearn.metrics import r2_score, root_mean_squared_error

y_predict = model.predict(x_val)
r2 = r2_score(y_val, y_predict)
rmsle = root_mean_squared_error(y_val, y_predict)
print(r2, rmsle)

model = RandomForestRegressor(random_state=42)
model.fit(given_x, given_y)


submit_y = model.predict(submit_x)
print(submit_y.shape)
df = pd.DataFrame(submit_y, columns=['pred'])
df.to_csv('result.csv', index=False)





# 3-1
df = pd.read_csv(path6)
print(df.shape)
print(df.head())

from scipy import stats

pvalue =stats.ttest_1samp(df['Final'], 70)[1]
# 3-1-1
print(round(pvalue, 3))


# 귀무가설 : 기말고사 점수가 중간고사 점수보다 증가 x
# 대립가설 : 기말고사 점수가 중간고사 점수보다 증가 o
pvalue =stats.ttest_rel(df['Midterm'], df['Final'], alternative='less')[1]
# 3-1-2
print(round(pvalue, 3))

# 3-1-3번은 모르겠다


# 3-2
df = pd.read_csv(path7)
print(df.shape)
print(df.head())

import statsmodels.formula.api as smf

df_droped = df.drop('ID', axis=1)
model = smf.logit('Passed ~ Study_Hours + Attendance + Previous_Score', data = df_droped).fit()

print(model.summary())

print(round(np.exp(model.params['Study_Hours']),3))

data = pd.DataFrame({
    'Study_Hours' : [6],
    'Attendance' : [85],
    'Previous_Score' : [75]
})

print(round(model.predict(data), 3)) # 0.691



condition = df_droped['Passed'] > 0.5

from sklearn.metrics import accuracy_score

pred = model.predict(df_droped)
print(pred)
pred_datas = pred >= 0.5
accuracy = accuracy_score(df['Passed'], pred_datas)
print(round(accuracy, 3))

