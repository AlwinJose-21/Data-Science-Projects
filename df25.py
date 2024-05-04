import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/missing_data1.csv', sep=',')
print(df)
print(df.isna().sum())
print("*" * 100)
# x = df['Calories'].mean()
# x = df['Calories'].median()
x = df['Calories'].mode()[0]
print(x)
df['Calories'].fillna(x, inplace=True)
print(df)
