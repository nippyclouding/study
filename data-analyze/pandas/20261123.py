#'/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/1.ipynb파일/10_Exam_lab.ipynb'
path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_1_math.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_2_sales.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/1_3_spam.csv'

path4 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/2_1_gas_test.csv'
path5 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/2_1_gas_train.csv'

path6 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/3_1_employee.csv'
path7 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년10회_실습파일_/2.csv파일/3_2_house.csv'

import pandas as pd
import numpy as np

print("=" * 50)
# 1-1
df = pd.read_csv(path1)

print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.info())

print(df['Subtopic'].value_counts)

# 1번 정답 0.468

print("=" * 50)

# 1-2
df = pd.read_csv(path2)

print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.info())

#df['year'] = df['order_date'].str.split('-')[0]
#df['month'] = df['order_date'].str.split('-')[1]

#df_grouped = df.groupby[['year', 'month']]('price').sum()
#df_grouped.value_sorts('price', ascending = False)

#print(int(np.trunc(df_grouped.head().iloc[1])))

# ? 

print("=" * 50)

# 1-2
df = pd.read_csv(path3)
print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.info())


df_split = df['Message'].str.split(' ')
print(df_split.head())
print(df_split.info())

# df['count'] = df_split.groupby['Message']()
print("=" * 50)

submit_x = pd.read_csv(path4)
given = pd.read_csv(path5)

# EDA
print("=" * 50)
print(given.shape)
print("=" * 50)
print(given.head())
print("=" * 50)
print(given.isnull().sum())
print("=" * 50)
print(given.info())
print("=" * 50)
print("=" * 50)
print("=" * 50)
print("=" * 50)

print(submit_x.shape)
print("=" * 50)
print(submit_x.head())
print("=" * 50)
print(submit_x.isnull().sum())
print("=" * 50)
print(submit_x.info())
print("=" * 50)



# preprocessing

given_cp = given.copy()
given_cp = given_cp[given_cp['GAS_TOTL'] != 0]
gas_mean = given_cp['GAS_TOTL'].mean()
print('gas_mean', gas_mean)

condition = given['GAS_TOTL'] == 0
given[condition]['GAS_TOTL'] = gas_mean

given_x = given.drop('GAS_TOTL', axis = 1)
given_y = given['GAS_TOTL']
print(given['GAS_TOTL'] == 0)

concat_x = pd.concat([given_x, submit_x])

concat_x = pd.get_dummies(concat_x)

given_x = concat_x[:given_x.shape[0]]
submit_x = concat_x[given_x.shape[0]:]

# train_test_split
from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(given_x, given_y, random_state = 42)
print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)


# modeling
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state = 42)
model.fit(x_train, y_train)


# metrics
from sklearn.metrics import root_mean_squared_error, r2_score

y_predict = model.predict(x_val)

rmse = root_mean_squared_error(y_val, y_predict)
r2 = r2_score(y_val, y_predict)
print(rmse, r2)

# remodeling / submit

model = RandomForestRegressor(random_state=42)
model.fit(given_x, given_y)

submit_y = model.predict(submit_x)
df = pd.DataFrame(submit_y, columns = ['pred'])
df.to_csv('result.csv', index=False)
print(df.shape)


print("=" * 50)

df = pd.read_csv(path6)
import statsmodels.formula.api as smf

model = smf.logit('Attrition ~ Age + MonthlyIncome + OverTime', data = df).fit()

print(model.summary())

# 3-1-1
print(round(0.0347, 3)) # 답 : 0.035

# 3-1-2
print(round(np.exp(0.0055 * 1), 3))  # 답 : 1.006


new_data = pd.DataFrame({
    'Age' : [45],
    'MonthlyIncome' : [4500],
    'OverTime' : [1]
})

# 3-1-3
print(round(model.predict(new_data), 3)) # 답 : 0.072


print("=" * 50)
df = pd.read_csv(path7)

import statsmodels.formula.api as smf

model = smf.ols('Price ~ Area + Stories + Wall', data = df).fit()
print(model.summary())
print(round(model.params.sum(), 3)) # 3-2-1 답 : 201.912

# 유의하지 않은 변수 : P>|t|값이 0.005보다 큰 컬럼 = Wall

model = smf.ols('Price ~ Area + Stories', data = df.drop(['Wall'], axis = 1)).fit()

print(model.summary()) # 3-2-2 정답 : 0.910

new_data = pd.DataFrame({
    'Area' : [120],
    'Stories' : [2.5],
    'Price' : [1]
})

print(round(model.predict(new_data), 3))  # 정답 3-2-3 : 808.856 