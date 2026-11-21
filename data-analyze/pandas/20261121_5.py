import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [
        77.5, 100.8, 71.5, 104.9, 82.9, 75.4, 63.1, 80.4, 74.0, 74.9,
        91.5, 86.1, 80.5, 74.5, 68.2, 76.8, 72.3, 71.5, 119.0, 81.5,
        61.0, 77.9, 94.6, 85.1, 71.2, 78.5, 64.8, 77.6, 78.7, 67.4
    ],
    "B": [
        76.5, 71.9, 70.5, 70.4, 77.8, 96.1, 89.1, 87.9, 79.1, 72.1,
        88.9, 74.9, 94.0, 68.4, 91.8, 73.3, 97.2, 90.8, 71.4, 75.2,
        68.2, 107.8, 71.4, 70.7, 84.6, 93.6, 72.4, 77.3, 87.5, 63.7
    ]
})

from scipy import stats
p_value_a = stats.shapiro(df['A'])[1]
p_value_b = stats.shapiro(df['B'])[1]


print(p_value_a, p_value_b)
print(max(p_value_a, p_value_b))
print(round(p_value_b, 3))


log_a = np.log(df['A']).var()
log_b = np.log(df['B']).var()

f_stat = (log_a / log_b) if log_a > log_b else (log_b / log_a)
print(round(f_stat, 3))


len_free_a = df['A'].shape[0] - 1
len_free_b = df['B'].shape[0] - 1

# 단측 검정 - 우측
p_value_right =1 - stats.f.cdf(f_stat, len_free_a, len_free_b)
# 단측 검정 - 좌측 
p_value_left = stats.f.cdf(f_stat, len_free_a, len_free_b)

# 양측 검정
p_value = 2 * min(p_value_right, p_value_left)



# 3.
log_a = np.log(df['A'])
log_b = np.log(df['B'])



print(round(stats.ttest_ind(log_a, log_b)[1], 3))