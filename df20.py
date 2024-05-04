import numpy as np
import pandas as pd

dic1 = {'id': [1, 2, 3, 4, 5],
        'fname': ['Vinay', 'Arjun', 'Mohan', 'Vipin', 'Sabir'],
        'lname': ['k', 'p', 's', 'k', 'r'],
        'age': [21, 21, 23, 25, 24]}
dic2 = {'id': [3, 4, 5, 6, 7],
        'prof': ['bigdata', 'python', 'data analyst', 'bigdata', 'python'],
        'salary': [2100, 2000, 4000, 2100, 3000],
        'loc': ['A', 'B', 'C', 'D', 'E']}
df1 = pd.DataFrame(dic1)
df2 = pd.DataFrame(dic2)
print(df1)
print(df2)
print("*"*100)
df3 = pd.merge(df1,df2,on='id',how='inner')
print(df3)
print("*"*100)
df3 = pd.merge(df1,df2,on='id',how='inner')[['fname','lname','prof','salary']]
print(df3)
df4 = pd.merge(df1,df2,on='id',how='inner') \
       .sort_values('age',ascending=False) \
       [['fname','lname','age','prof','salary']].head(2)
print(df4)
df5 = pd.merge(df1,df2,on='id',how='inner').loc[df2['prof']=='bigdata'].sort_values('age',ascending=False) \
       [['fname','lname','age','prof','salary']].head(1)
print(df5)
df6 = pd.merge(df1,df2,on='id',how='inner').sort_values('salary').head(1)
print(df6)
