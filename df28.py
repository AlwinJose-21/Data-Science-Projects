import numpy as np
import pandas as pd
df = pd.read_csv('C:/Users/Hp/Downloads/heart_missing.csv',sep=',')
print(df)
print("*"*100)
df.dropna(inplace=True, ignore_index=True)
print(df)
print(df.isna().sum())
print(df.shape)