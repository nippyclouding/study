import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler, StandardScaler

path = './datas/2.csv파일/1유형/employee.csv'

df = pd.read_csv(path)
print(df.info())
print(df.isnull().sum())
print(df.shape)
print(df.head(10))


# series_company_salary_mean = df.groupby('Company')['Salary'].mean() => 오류
series_company_salary_mean = df.groupby('Company')['Salary'].transform('mean')
print(type(series_company_salary_mean))
print(series_company_salary_mean.head(10))

df['Salary'] = df['Salary'].fillna(np.trunc(series_company_salary_mean))


print(df.isnull().sum())


series_company_salary_mean = df.groupby('Company')['Salary'].mean()
print(np.trunc(series_company_salary_mean))

col_name = series_company_salary_mean.idxmax()

print(col_name)
print(int(series_company_salary_mean[col_name])) 
# 시리즈['a'] 출력 시 시리즈 인덱스 중 'a' 라는 인덱스의 데이터 출력