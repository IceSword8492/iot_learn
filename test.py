import numpy as np
import pandas as pd
def make (i, c, s):
    np.random.seed(s)
    df = pd.DataFrame()
    for co in c:
        df[co] = np.random.choice(range(1, 101), len(i))
    df.index = i
    return df
columns = ["apple", "orange", "banana"]
df_data1 = make(range(1, 5), columns, 0)
df_data2 = make(range(1, 5), columns, 1)
print(pd.concat([df_data1, df_data2], axis = 1, keys = ['X', 'Y']))
