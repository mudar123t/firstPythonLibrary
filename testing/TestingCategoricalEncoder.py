import pandas as pd
from sklearn.preprocessing import LabelEncoder
from dataMnp import CategoricalEncoder


data = {
    'A': ['foo', 'bar', 'baz', 'foo', 'baz'],
    'B': ['one', 'one', 'two', 'three', 'two'],
    'C': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df1 = CategoricalEncoder.one_hot_encode(df.copy(), ['A', 'B'])
print(df1)

df2 = CategoricalEncoder.label_encode(df.copy(), ['A', 'B'])
print(df2)