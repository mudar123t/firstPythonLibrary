import pandas as pd
import numpy as np
from dataMnp import MissingValueHandler

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 10, 20, np.nan, 50],
    'C': ['foo', 'bar', np.nan, np.nan, 'baz']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df1 = MissingValueHandler.impute_mean(df.copy())
print(df1)

df2 = MissingValueHandler.impute_median(df.copy())
print(df2)

df3 = MissingValueHandler.impute_constant(df.copy(), 55)
print(df3)

df4 = MissingValueHandler.delete_missing(df.copy())
print(df4)