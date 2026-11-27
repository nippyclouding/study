import pandas as pd
import numpy as np

import pandas as pd
from scipy import stats

df = pd.DataFrame({
    'A': [50, 51, 49, 52, 48, 50, 51, 49, 50, 52, 48, 54],
    'B': [52, 53, 54, 51, 55, 52, 53, 54, 52, 53, 51, 56],
    'C': [54, 55, 56, 53, 55, 54, 56, 55, 54, 55, 53, 53]
})

print(df)

print(df)
print(df.shape)  # (30, 2)

from scipy import stats


stats.bartlett(df['A'], df['B'], df['C'])[1]
stats.levene(df['A'], df['B'], df['C'])[1]
stats.f_oneway(df['A'], df['B'], df['C'])[1]

