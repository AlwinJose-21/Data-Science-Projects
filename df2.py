import numpy as np
import pandas as pd

dic = {'id': [101, 102, 103, 104, 105],
       'fname': ['vinay', 'arjun', 'amal', 'vipin', 'vineeth'],
       'lname': ['k', 's', 'p', 'a', 'd'],
       'age': [21, 23, 21, 24, 25],
       'marks': [100, 90, 57, 90, 99]}
df = pd.DataFrame(dic)
print(df)
print(type(df))
print(df.shape)
print(df.head())
print(df.tail())
df['Location']=['Tcr','Ijk','Erk','Goa','Tcr']
print(df)

