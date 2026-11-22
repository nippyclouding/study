import pandas as pd
import numpy as np

df = pd.DataFrame({
    "공부시간": [
        1, 2, 2, 3, 3, 4, 4, 3, 4, 4,
        5, 5, 5, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 9, 9, 9, 10, 10, 10, 11,
        11, 8, 9, 10, 11, 8, 6, 5, 4, 3,
        2, 1, 9, 10, 7, 6, 5, 8, 4, 7
    ],
    "수면시간": [
        10, 9, 8, 9, 8, 9, 8, 7, 7, 6,
        8, 7, 6, 8, 7, 6, 7, 6, 5, 8,
        6, 5, 4, 6, 5, 4, 6, 5, 4, 5,
        4, 7, 7, 7, 6, 8, 5, 5, 5, 6,
        7, 8, 3, 3, 4, 4, 4, 3, 6, 9
    ],
    "합격여부": [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 1, 0, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 0, 1, 1, 1, 0, 1, 1, 0, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 0, 0
    ]
})

print(df.shape)  # (50, 3)



df_study_train = df['공부시간'][:40]
df_study_test = df['공부시간'][40:]

df_sleep_train = df['수면시간'][:40]
df_sleep_test = df['수면시간'][40:]

df_passed_train = df['합격여부'][:40]
df_passed_test = df['합격여부'][40:]


df_train = pd.DataFrame({})
df_train['공부시간']= df_study_train
df_train['수면시간']= df_sleep_train
df_train['합격여부']= df_passed_train

df_test = pd.DataFrame({})
df_test['공부시간']= df_study_test
df_test['수면시간']= df_sleep_test
df_test['합격여부']= df_passed_test



import statsmodels.formula.api as smf

model = smf.logit('합격여부 ~ 공부시간 + 수면시간', data = df_train).fit()
print(model.summary())

# 3 증가할 때는 회귀계수 * 3
print(round(np.exp(0.9736 * 3), 3))

print(round(-2 * -8.0961, 3))

test_predict = model.predict(df_test[['공부시간','수면시간']])
print(test_predict.head())

from sklearn.metrics import accuracy_score

test_result = (test_predict >= 0.5)
accuracy = accuracy_score(df_test['합격여부'], test_result)

print(round(accuracy, 3))