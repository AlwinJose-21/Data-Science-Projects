import numpy as np
import pandas as pd

df=pd.read_csv('C:/Users/Hp/Downloads/missing_data1.csv',sep=',')
print(df)
print(df.isna().sum())
# df.dropna(subset=['Date'],inplace=True,ignore_index=True)
df.dropna(subset=['Calories'],inplace=True,ignore_index=True)
print(df)