import pandas as pd
from datetime import datetime, timedelta
from dataMnp import DateTimeHandler


data = {
    'start_datetime': [datetime(2022, 1, 1, 12, 0), datetime(2022, 1, 2, 10, 30),
                       datetime(2022, 1, 3, 9, 15), datetime(2022, 1, 4, 8, 0),
                       datetime(2022, 1, 5, 7, 45)],
    'end_datetime': [datetime(2022, 1, 1, 13, 30), datetime(2022, 1, 2, 12, 45),
                     datetime(2022, 1, 3, 11, 0), datetime(2022, 1, 4, 10, 30),
                     datetime(2022, 1, 5, 10, 15)]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df1 = DateTimeHandler.extract_date(df.copy(), 'start_datetime')
print(df1)


df2 = DateTimeHandler.calculate_time_difference(df.copy(), 'start_datetime', 'end_datetime', unit='hours')
print(df2)