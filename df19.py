import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/customer5.txt', sep=',', header=None)
df.columns = ['id','fname','lname','age','prof','loc','salary']
print(df)
df1 = df.groupby('prof')['salary'].max()
print(df1)
df2 = df.groupby('prof')['salary'].sum()
print(df2)
df3 = df.groupby('loc')['salary'].min()
print(df3)
df4 = df.groupby('age')['salary'].max()
print(df4)
df5 = df.groupby('prof')['salary'].mean()
print(df5)
df6 = df.groupby('prof')['age'].max()
print(df6)
df7 = df.groupby('loc')['age'].min()
print(df7)
df8 = df['prof'].value_counts()
print(df8)