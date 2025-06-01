import pandas as pd
import numpy as np
from dataMnp import OutlierHandler

data = {
    'A': [1, 2, 3, 4, 5, 100],
    'B': [10, 20, 30, 40, 50, 1000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


df1 = OutlierHandler.change_outliers_value(df.copy(), replace_value=999)
print(df1)

df2 = OutlierHandler.change_outliers_value(df.copy())
print(df2)