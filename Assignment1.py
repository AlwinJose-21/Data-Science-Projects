import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/customer1.txt', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'loc']
print(df)
print("*"*100)
df1 = df.fillna('india')
print(df1.count())
print("*"*100)
df2 = df1.drop_duplicates()
print(df2)
print("*"*100)
df3 = df1.sort_values('age', ascending=False)[['fname', 'lname', 'prof', 'loc']].head(10)
print(df3)
print("*"*100)
df4 = df1.sort_values('age')[['fname', 'lname', 'prof', 'loc']].head(5)
print(df4)
print("*"*100)
df5 = df1.groupby('loc')['loc'].count().sort_values(ascending=False)
print(df5)
print("*"*100)
df6 = df1.loc[df1['loc'] == 'australia']
print(df6)
print("*"*100)
df7 = df1.groupby('age')['age'].count().sort_values(ascending=False)
print(df7)
print("*"*100)
df8 = df1.groupby('prof')['prof'].count().sort_values(ascending=False)
print(df8)
print("*"*100)
df9A = df1.loc[df1['loc'] == 'india'].count()
print(df9A)
print("*"*100)
df9B = df1.loc[df1['loc'] == 'india'].groupby('prof')['prof'].count().sort_values(ascending=False)
print(df9B)
print("*"*100)
df9C = df1.loc[df1['loc'] == 'india'].sort_values('age', ascending=False)[['fname', 'lname', 'age', 'prof']].head(3)
print(df9C)
print("*"*100)
df9D = df1.loc[df1['loc'] == 'india'].sort_values('age')[['fname', 'lname', 'age', 'prof']].head(3)
print(df9D)
print("*"*100)
df9E = df1.loc[(df1['loc'] == 'india') & (df1['age'] > 40)]
print(df9E)
print("*"*100)
df9F = df1.loc[(df1['loc'] == 'india') & (df1['age'] > 30) & (df1['age'] < 40)].groupby('prof')['prof'].count()
print(df9F)
print("*"*100)
df10A = df1.loc[df1['loc'] == 'us'].count()
print(df10A)
print("*"*100)
df10B = df1.loc[df1['loc'] == 'us'].groupby('age')['prof'].count()
print(df10B)
print("*"*100)
df10C = df1.loc[df1['loc'] == 'us'].groupby('prof')['prof'].count().sort_values(ascending=False)
print(df10C)
print("*"*100)
df10D = df1.loc[(df1['loc'] == 'us')&(df1['prof']=='Civil engineer')&(df1['age']>30)]
print(df10D)
print("*"*100)