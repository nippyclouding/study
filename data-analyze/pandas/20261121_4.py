import pandas as pd

df = pd.DataFrame({
    "non_part": [
        49.1, 51.0, 50.0, 52.3, 50.4, 51.5, 47.7, 47.2, 49.9, 47.5,
        49.7, 52.2, 52.3, 49.9, 48.7, 50.5, 45.1, 48.8, 53.4, 51.5
    ],
    "part": [
        53.0, 47.0, 49.5, 50.8, 53.0, 54.5, 52.1, 56.0, 50.0, 44.6,
        58.3, 43.7, 49.1, 56.5, 50.0, 49.3, 51.1, 59.4, 54.3, 48.3
    ]
})
a = 0.05

from scipy import stats

# 1.
p_value_non_part = stats.shapiro(df['non_part'])[1]
print(round(p_value_non_part, 3))

print("non_part 정규성 불만족") if p_value_non_part < a else print("non_part 정규성 만족")

p_value_part = stats.shapiro(df['part'])[1]
print(round(p_value_part, 3))

print("part 정규성 불만족") if p_value_part < a else print("part 정규성 만족")


# 2. 
p_value = stats.levene(df['non_part'], df['part'])[1]
print(round(p_value, 3))

print("등분산 불만족") if p_value < a else print("등분산 만족")

# 3.두 집단 간 기록에 차이가 있는지 : 
# 귀무가설 : 두 집단 간 기록에 차이가 없다.
# 대립가설 : 두 집단 간 기록에 차이가 있다.
# 독립 표본 t검정 (두 집단 간 평균 비교)

# 정규성을 만족하기 때문에 ttest_ind 사용 가능, 정규성 만족한다고 볼 수 없을 경우 맨휘트니 기법 사용
p_value = stats.ttest_ind(df['non_part'], df['part'], equal_var=False)[1]
print(round(p_value, 3))

print("귀무가설 기각") if p_value < a else print("귀무가설 채택")