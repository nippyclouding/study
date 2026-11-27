import pandas as pd

df = pd.DataFrame({
    'user_id': [101, 102, 103, 104, 105, 106],
    'usage_time': [
        '1시간 30분',
        '2시간 15분',
        '45분',
        '3시간',
        '1시간 50분',
        '2시간 5분'
    ]
})

# usage_time을 분 단위 숫자로 변환해 total_minutes 컬럼을 생성한다.
print(df.info())
pd.to_datetime(df['usage_time'], format="%H시간 %M분")


# 전체 고객의 평균 이용 시간을 구한다.



# 평균 이용 시간을 반올림하여 소수 셋째 자리까지 출력한다.