import pandas as pd
import numpy as np

df = pd.DataFrame({'score' : [81, 83, 82, 80, 79, 82, 81, 84, 78, 82, 80, 83, 81, 79, 82, 84, 80, 81, 83, 79, 82, 81, 80, 84, 78, 82, 81, 83, 78, 82]})
a = 0.05

# 1. 정규성 검정
from scipy import stats

p_value = stats.shapiro(df['score'])[1]
print(p_value)

if p_value < a :
    print("1. 정규성 불만족")
elif p_value >= a : 
    print("1. 정규성 만족")

print(round(p_value, 3))

# 2. 시험 점수가 80점과 같은지 검정
# 정규성 만족 : 단일 표본 t 대응, ttest_1samp()

# 귀무가설 : 학생들의 시험 점수가 80점과 같다.
# 대립가설 : 학생들의 시험 점수가 80점과 다르다. (양측 검정)

p_value = stats.ttest_1samp(df['score'], 80)[1]

if p_value < a :
    print("2. 귀무가설 불만족")
elif p_value >= a : 
    print("2. 귀무가설 만족")
print(round(p_value, 3))

# 정규성을 만족하지 않을 경우 : 윌콕슨 부호 순위
p_value = stats.wilcoxon(df['score'] - 80)[1] # 비모수 검정에서는 - 80 반영 필요 


# 3. 학생들의 실제 시험 점수가 80보다 낮은지 검정
# 귀무 가설 : 학생들의 실제 시험 점수 평균이 80보다 낮다
# 대립 가설 : 학생들의 실제 시험 점수 평균이 80보다 낮지 않다

p_value = stats.ttest_1samp(df['score'], 80, alternative = 'less')[1]

if p_value < a :
    print("귀무가설 만족, 평균 시험 80점 미만이라고 할 수 있다.")
else : 
    print("귀무가설 불만족, 평균 시험 80점 미만이라고 할 수 없다.")

print(round(p_value, 3))