import pandas as pd
import numpy as np

path1 = './datas/2.csv파일/2유형/회귀/전기사용량/elec_train.csv'
path2 = './datas/2.csv파일/2유형/회귀/전기사용량/elec_test.csv'

df_given = pd.read_csv(path1)
df_submit = pd.read_csv(path2)

# 회귀 모델

# EDA -> 전처리 -> 훈련, 검증 데이터 구분 -> 학습 -> 평가 -> 적용

# 1. EDA
df_given.info()
print(df_given.shape)
print(df_given.isnull().sum())

df_submit.info()
print(df_submit.shape)
print(df_submit.isnull().sum())



# 2. 전처리

# 2-1. 결측치 수정 (건물코드, 기온은 결측치 없음)
df_given['강수량'] = df_given['강수량'].fillna(df_given['강수량'].mean())
df_given['습도'] = df_given['습도'].fillna(df_given['습도'].mean())
df_given['풍속'] = df_given['풍속'].fillna(df_given['풍속'].mode()[0])

print(df_given.isnull().sum())

df = df_given.copy()


# 2-2. 독립, 종속 변수 분리
df_x = df.drop(['전력소비량'], axis = 1)
df_y = df['전력소비량']

print(df_x.head())
print(df_y.head())

# 2-3. 수치형 변수 스케일링 (정규화, 표준화) / 범주형 변수 인코딩
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

standardScaler = StandardScaler()
minmaxScaler = MinMaxScaler()
labelEncoder = LabelEncoder()

df_x['건물코드'] = labelEncoder.fit_transform(df_x['건물코드'])
# 범주형 변수 스케일링 시 encoder.fit_transform(df['']) : df 속에 1차원 리스트를 전달해야 한다.

df_x['기온'] = standardScaler.fit_transform(df_x[['기온']])
df_x['강수량'] = standardScaler.fit_transform(df_x[['강수량']])
df_x['풍속'] = standardScaler.fit_transform(df_x[['풍속']])
df_x['습도'] = standardScaler.fit_transform(df_x[['습도']])

# scaler_list = ['기온', '강수량', '풍속', '습도']
# df_x[scaler_list] = standardScaler.fit_transform(df_x[scaler_list])
# 수치형 변수 스케일링 시 scaler.fit_transform(df[['']]) : df 속에 2차원 리스트를 전달해야 한다. 

# 랜덤 포레스트 모델은 문자열을 그대로 처리할 수 없기 때문에 제출할 데이터 df_submit에도 스케일링 처리가 필요하다.
df_submit['건물코드'] = labelEncoder.fit_transform(df_submit['건물코드'])

df_submit[['기온', '강수량', '풍속', '습도']] = standardScaler.fit_transform(df_submit[['기온', '강수량', '풍속', '습도']])
# df_submit[['기온', '강수량', '풍속', '습도']] 과 같이 결과 데이터에 여러 열을 컬럼으로 지정할 경우 이차원 리스트 적용 필요
# scaler.fit_transform(df[[]]) 에서는 반드시 이차원 리스트 적용 필요


# 3. 훈련, 검증 데이터 구분
from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(df_x, df_y, test_size = 0.2)

print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)



# 4. 학습
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(x_train, y_train)


# 5. 성능 측정
from sklearn.metrics import mean_squared_error, r2_score

y_predict = model.predict(x_val)

mse = mean_squared_error(y_predict, y_val) # 예측값, 실제값의 파라미터 순서는 상관 x
print(mse)

r2score = r2_score(y_val, y_predict) # 예측값, 실제값의 파라미터 순서가 중요 : 실제값, 예측값 // 실제 시험에서는 실제값 val -> 예측값 predict로 통일하여 사용하기
print(r2score)


# 6. 제출
df_answer = model.predict(df_submit) # 제출할 y 도출

result = pd.DataFrame(df_answer, columns=['pred']) # 결과 컬럼명 : pred
result.to_csv('20261112.csv', index=False)