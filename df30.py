import numpy as np
import pandas as pd

df=pd.read_csv('C:/Users/Hp/Downloads/missing_data1.csv',sep=',')
print(df)
print(df.isna().sum())
print("*"*100)
# df.loc[7,'Duration']=45
# print(df)
# x = df['Duration'].mode()[0]
# df.loc[7,'Duration'] = x
# print(df)
#calories above 400 wrong format
x = df['Calories'].mean()
for i in df.index:
    if df.loc[i,'Calories'] > 400:
        df.loc[i,'Calories'] = x
print(df)