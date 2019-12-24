import pandas as pd

order_df = pd.DataFrame([[1000, 2546, 103], [1001, 4352, 101], [1002, 342, 101]], columns = ['id', 'item_id', 'customer_id'])
order_df.index = [101, 102, 103]

customer_df = pd.DataFrame([['Tanaka'], ['Suzuki'], ['Kato']], columns = ['name'])
customer_df.index = [101, 102, 103]

print(pd.merge(order_df, customer_df, left_on = 'customer_id', right_index = True, how = 'inner'), '\n')

import numpy as np
import math

np.random.seed(0)
columns = ['apple', 'orange', 'banana', 'strawberry', 'kiwifruit']

df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

df.index = range(1, 11)

print(df)
print(df.describe())
print(df.describe().loc[['50%']])
