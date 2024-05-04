import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/customer1.txt', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'loc']
print(df)
print(df.isna().sum())
# fill
# fillna()
print("*"*100)
df1=df.fillna('india')
print(df1)
print(df1.isna().sum())