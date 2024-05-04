import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/sample4.txt', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'phno', 'loc']
print(df)
df1 = df.loc[df['age'] == 22][['fname', 'lname', 'age', 'phno']]
print(df1)
print("*" * 100)
df2 = df.loc[df['age'] > 22]
print(df2)
print("*" * 100)
df3 = df.loc[df['loc'] == 'Chennai'][['fname', 'lname', 'age', 'phno']]
print(df3)
print("*" * 100)
df4 = df.loc[(df['loc'] == 'Chennai') & (df['age'] > 23)][['fname', 'lname', 'age', 'phno']]
print(df4)
