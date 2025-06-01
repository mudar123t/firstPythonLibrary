import pandas as pd
import numpy as np
from dataMnp import scaler


data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df1 = scaler.min_max_scaling(df.copy())
print(df1)


df2 = scaler.standard_scaling(df.copy())
print(df2)