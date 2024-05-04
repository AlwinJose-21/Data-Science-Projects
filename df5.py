import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Hp/Downloads/missing_data1.csv',sep=',')
print(df.columns)
print(df.isna().sum())
df1=df.fillna('100')
print("*"*100)
print(df1.isna().sum())