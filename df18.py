import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/Temperature',sep=' ',header=None)
df.columns =['year','temp']
print(df)
df1 = df.groupby('year')['temp'].max() \
    .sort_values(ascending=False)
print(df1)
df2 = df.groupby('year')['temp'].min() \
    .sort_values()
print(df2)
df3 = df.groupby('year')['temp'].sum()
print(df3)
df4 = df.groupby('year')['temp'].mean()
print(df4)