import pandas as pd

def check(p_value) :
    a = 0.05
    if (p_value < a) : 
        print("귀무가설 기각, 평균 80점 만족 x")
    elif (p_value >= a) : 
        print("귀무가설 기각 x, 평균 80점이라고 볼 수 있다")

df = pd.DataFrame({
    'score' : [81, 83, 82, 80, 79, 82, 81, 84, 78, 82,
               80, 83, 81, 79, 82, 84, 80, 81, 83, 79,
               82, 81, 80, 84, 78, 82, 81, 83, 78, 82]
})

# 1. 정규성 검정 - 샤피로 윌크 테스트로 p-value 값 구하기

# h0 : 데이터프레임이 정규성을 만족한다
# 유의수준 a : 5%

from scipy import stats

a = 0.05

print(stats.shapiro(df['score']))

p_value = stats.shapiro(df['score'])
p_value = stats.shapiro(df['score'])[1]

print(round(p_value, 3))

if (p_value < a) :
    print("귀무가설 기각, 정규성 만족 x")
elif (p_value >= a) : 
    print("귀무가설 기각 x, 정규성 만족 o")





# 귀무가설 : 평균 시험 점수가 80점과 같다
# 대립가설 : 평균 시험점수가 80점과 다르다
print(stats.ttest_1samp(df['score'], 80))

t_stat = stats.ttest_1samp(df['score'], 80)[0]
p_value = stats.ttest_1samp(df['score'], 80)[1]
print(round(p_value, 3))

if (p_value < a) : 
    print("귀무가설 기각, 평균 80점 만족 x")
elif (p_value >= a) : 
    print("귀무가설 기각 x, 평균 80점이라고 볼 수 있다")





# 귀무가설 : 평균 시험 점수가 80점보다 높다
# 대립가설 : 평균 시험점수가 80점보다 높지 않다
# alternative는 귀무가설이 아니라 대립가설의 방향을 지정
p_value = round(stats.ttest_1samp(df['score'], 80, alternative='less')[1], 3)
print(p_value)

if (p_value < a) : 
    print("귀무가설 기각, 평균 80점보다 높지 않다")
elif (p_value >= a) : 
    print("귀무가설 기각 x, 평균 80점보다 높다")
