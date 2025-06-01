import pandas as pd
from dataMnp import FeatureEngineer


data = {
    'A': [1.23e6, 4.56e7, 7.89e8],
    'B': [2, 4, 6],
    'C': [3, 5, 7]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


try:
    df1 = FeatureEngineer.change_scientific_notation(df.copy(), 'A')
    print(df1)
except (ValueError, TypeError) as e:
    print(f"\nError: {e}")


columns_to_multiply = [('B', 'C')]
df2 = FeatureEngineer.multiply2Col(df.copy(), columns_to_multiply)
print(df2)
