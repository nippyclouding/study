path1 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/1_1_library.csv'
path2 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/1_2_delivery.csv'
path3 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/1_3_student.csv'
path4 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/2_1_maintenance_test.csv'
path5 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/2_1_maintenance_train.csv'
path6 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/3_1_exam_score.csv'
path7 = '/Users/nippyclouding/Desktop/빅데이터분석기사/2_26년12회_실습파일/2.csv파일/3_2_student_learning.csv'

def rtn(data) :
    print(round(data, 3))
import pandas as pd
import numpy as np

df = pd.read_csv(path6)

from scipy import stats

p_value = stats.ttest_1samp(df['Final'], 70)[1]
rtn(p_value)

# 귀무가설 : 기말고사 점수와 중간고사 점수가 동일
# 대립가설 : 기말고사 점수가 중간고사 점수보다 클 것이다.

rtn(stats.ttest_rel(df['Final'], df['Midterm'], alternative='greater')[1])

# 집단 a : 보충학습을 한 학생, 집단 b : 보충학습을 하지 않은 학생
condition = df['Supplementary'] == 'Y'
pvalue = stats.ttest_ind(df[condition]['Final'], df[~condition]['Final'])[1]
confidence_interval = stats.ttest_ind(df[condition]['Final'], df[~condition]['Final']).confidence_interval().low
rtn(confidence_interval)



df = pd.read_csv(path7)

df_dropped = df.drop('ID', axis=1)

import statsmodels.formula.api as smf
model = smf.logit('Passed ~ Study_Hours + Attendance + Previous_Score', data=df_dropped).fit()
print(model.llf * -2) # 로그우도 * -2 = 잔차 오차

rtn(np.exp(model.params['Study_Hours']))

data = pd.DataFrame(
    {
        'Study_Hours' : [6],
        'Attendance' : [85],
        'Previous_Score' : [75]
    }
)

print(model.predict(data).iloc[0])
rtn(model.predict(data))

from sklearn.metrics import accuracy_score

df_dropped_passed = df_dropped.drop('Passed', axis=1)

# 실제
df['Passed']
# 예측
model.predict(df_dropped_passed)

pred = model.predict(df_dropped_passed) >= 0.5

rtn(accuracy_score(df['Passed'], pred))