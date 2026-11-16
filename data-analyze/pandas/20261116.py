# http://kaggle.com/code/agileteam/py-t1-4-expected-questions
# 왜도와 첨도 구하기
# 문제 : train.csv의 SalePrice 컬럼에 대해 다음 네 값을 구해 모두 더한 뒤, 소수점 둘째 자리까지 반올림해 출력하시오.
# 1. 원래 SalePrice의 왜도
# 2. 원래 SalePrice의 첨도
# 3. SalePrice를 log1p로 변환(스케일링)한 뒤의 왜도
# 4. log1p 변환 후의 첨도

import pandas as pd
import numpy as np

path = '/kaggle/input/house-prices-advanced-regression-techniques/train.csv'
df = pd.read_csv(path)

# 왜도 : skew()
skew = df['SalePrice'].skew()

# 첨도 : kurt()
kurt = df['SalePrice'].kurt()

# log1p 변환 : np.log1p()
log1p = np.log1p(df['SalePrice'])

# log1p 스케일링 후 왜도, 첨도
log1p_skew = log1p.skew()
log1p_kurt = log1p.kurt()


# round(data, n) : 반올림하여 n번째 자리까지 표현
print(round(skew + kurt + log1p_skew + log1p_kurt, 2))
