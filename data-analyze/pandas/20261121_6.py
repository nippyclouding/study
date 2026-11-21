import pandas as pd

df = pd.DataFrame({
    "A": [50, 51, 49, 52, 48, 50, 51, 49, 50, 52, 48, 54],
    "B": [52, 53, 54, 51, 55, 52, 53, 54, 52, 53, 51, 65],
    "C": [54, 55, 56, 53, 55, 54, 56, 55, 54, 55, 53, 53]
})


from scipy import stats
p_value_1 = stats.bartlett(df['A'], df['B'], df['C'])[1]
print(round(p_value_1, 3))

p_value_2 = stats.levene(df['A'], df['B'], df['C'])[1]
print(round(p_value_2, 3))

p_value_3 = stats.f_oneway(df['A'], df['B'], df['C'])[1]
print(round(p_value_3, 3))
