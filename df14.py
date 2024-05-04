import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/customer1.txt', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'loc']
print(df)
print("*"*100)
df1 = df.fillna('india')
print(df1)
print("First","*"*100)
df2 = df1.loc[df1['loc'] == 'india'][['fname', 'lname', 'age', 'prof']]
print(df2)
print("Second","*"*100)
df3 = df1.loc[(df1['loc'] == 'uk') & (df1['age'] > 50)][['fname', 'lname', 'age', 'prof']]
print(df3)
print("Third","*"*100)
df4 = df1.sort_values(by='age', ascending=False)[['fname', 'lname', 'age', 'prof']].head(5)
print(df4)
print("Fourth","*"*100)
df5 = df1.sort_values(by='age')[['fname', 'lname', 'age', 'loc']].head(3)
print(df5)
print("Fifth","*"*100)
df6 = df1.loc[df1['prof'] == 'Teacher'][['fname', 'lname', 'age']]
print(df6)
print("Sixth","*"*100)
df7 = df1.loc[(df1['loc'] == 'india') & (df1['prof'] == 'Dancer')][['fname', 'lname', 'age']]
print(df7)
print("Seventh","*"*100)
df8 = df1.loc[df1['loc'] == 'india'].sort_values(by='age', ascending=False)[['fname', 'lname', 'age', 'prof']].head(3)
print(df8)
print("Eighth","*"*100)
df9 = df1.loc[(df1['loc'] == 'india') & (df1['prof'] == 'Dancer')].sort_values(by='age') \
         [['fname', 'lname', 'age']].head(1)
print(df9)
print("Nineth","*"*100)
df10 = df1.loc[df1['loc'] == 'us'].sort_values(by='age').head(5)
print(df10)
print("Tenth","*"*100)
df11 = df1.loc[df1['prof'] == 'Pilot'].sort_values(by='age')[['fname', 'lname', 'age', 'loc']].head(1)
print(df11)
print("Eleventh","*"*100)
df12 = df1.loc[(df1['age'] > 25) & (df1['age']< 40)] [['fname', 'lname', 'age', 'prof']]
print(df12)
