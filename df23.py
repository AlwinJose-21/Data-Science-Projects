import numpy as np
import pandas as pd

df=pd.read_csv('C:/Users/Hp/Downloads/missing_data1.csv',sep=',')
print(df)
print(df.isna().sum())
# df1 = df.fillna(150)
# print(df1)
# df.fillna(150,inplace=True)
# print(df.isna().sum())
df['Calories'].fillna(150, inplace=True)
df['Date'].fillna('2020-12-08', inplace=True)
print(df)
print(df.isna().sum())
