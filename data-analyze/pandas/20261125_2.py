path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_1_emission.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_2_indoor.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/1_3_marketing.csv'
path4 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/2_1_game_level_test.csv'
path5 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/2_1_game_level_train.csv'
path6 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/3_1_diabetes.csv'
path7 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_25년11회_실습파일/2.csv파일/3_2_promotion.csv'

import pandas as pd
import numpy as np

df = pd.read_csv(path7)

# 독립변수 : Visit_Count, Page_Time, Click_Count, Ad_Spend, Conversion_Count
# 종속변수 : Sales

# 1. t 검정 수행, 평균이 300초 : 단일 표본 t검정

from scipy import stats

p_value = stats.ttest_1samp(df['Page_Time'], 300)[1]
print(round(p_value, 3)) # 0.332

# 양측검정 : alternative=two-sided
# 단측검정 : alternative=less, greater (왼쪽 측정 시 less, 오른쪽 측정 시 greater)


print(df.info())
# 상관계수 행렬


# Sales 종속 변수, 나머지를 독립변수
import statsmodels.formula.api as smf

model = smf.ols('Sales ~ Visit_Count + Page_Time + Click_Count + Ad_Spend + Conversion_Count', data=df).fit()

print(model.summary())
min_column = model.pvalues.drop('Intercept').idxmin()
print(round(model.params[min_column],3))
# 가장 통계적으로 유의한 변수 : p_value가 0.005보다 작은 것 중 