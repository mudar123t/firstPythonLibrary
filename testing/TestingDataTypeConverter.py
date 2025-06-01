import pandas as pd
from dataMnp import DataTypeConverter


data = {
    'A': ['1', '2', '3', '4', '5'],
    'B': [1.1, 2.2, 3.3, 4.4, 5.5],
    'C': [1, 2, 3, 4, 5],
    'D': ['foo', 'bar', 'baz', 'qux', 'quux']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df1 = DataTypeConverter.convert_to_numeric(df.copy(), ['A', 'B', 'C'])
print(df1)

df2 = DataTypeConverter.convert_to_categorical(df.copy(), ['D'])
print(df2)
