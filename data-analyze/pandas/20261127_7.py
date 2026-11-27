
import pandas as pd

df = pd.DataFrame({
    'A': [
        77.5, 100.8, 71.5, 104.9, 82.9, 75.4, 63.1, 80.4, 74.0, 74.9,
        91.5, 86.1, 80.5, 74.5, 68.2, 76.8, 72.3, 71.5, 119.0, 81.5,
        61.0, 77.9, 94.6, 85.1, 71.2, 78.5, 64.8, 77.6, 78.7, 67.4
    ],
    'B': [
        76.5, 71.9, 70.5, 70.4, 77.8, 96.1, 89.1, 87.9, 79.1, 72.1,
        88.9, 74.9, 94.0, 68.4, 91.8, 73.3, 97.2, 90.8, 71.4, 75.2,
        68.2, 107.8, 71.4, 70.7, 84.6, 93.6, 72.4, 77.3, 87.5, 63.7
    ]
})

print(df)
import numpy as np

from scipy import stats

pvalue_1 = stats.shapiro(df['A'])[1]
pvalue_2 = stats.shapiro(df['B'])[1]

print(pvalue_1, pvalue_2)
print(round(max(pvalue_1, pvalue_2), 3))


df['log_a'] = np.log(df['A'])
df['log_b'] = np.log(df['B'])


# 1. 분산 구해서 f 통계량 구하기

print(df['log_a'].var(), df['log_b'].var()) # log_a var가 더 크다.

var_a = df['log_a'].var()
var_b = df['log_b'].var()

f = var_a / var_b
print(round(f, 3))

df1 = len(df['log_a']) - 1
df2 = len(df['log_b']) - 1

pvalue = 2 * min (
    1 - stats.f.cdf(f, df1, df2), stats.f.cdf(f, df1, df2)
)

print(round(stats.ttest_ind(df['log_a'], df['log_b'])[1],3))