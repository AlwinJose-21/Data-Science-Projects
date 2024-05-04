import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/customer1.txt', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'loc']
print(df)
df1 = df[['fname', 'lname', 'age', 'loc']].head(50)
print(df1)
df2 = df[['fname','lname','age','prof']].tail(10)
print(df2)
df3=df.iloc[2]
print(df3)
df4=df.iloc[2:9]
print(df4)
df5=df.iloc[2:40:3]
print(df5)