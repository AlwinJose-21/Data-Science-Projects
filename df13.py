import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/sample4.txt', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'phno', 'loc']
print(df)
print("*" * 100)
df1 = df.sort_values(by='age', ascending=False) \
         [['fname', 'lname', 'age', 'phno']].head(2)
print(df1)
print("*" * 100)
df2 = df.sort_values(by='age') \
         [['fname', 'lname', 'age', 'loc']].head(1)
print(df2)
print("*" * 100)
df3 = df.loc[df['loc'] == 'Chennai'] \
        .sort_values(by='age', ascending=False) \
         [['fname', 'lname', 'age']].head(1)
print(df3)
