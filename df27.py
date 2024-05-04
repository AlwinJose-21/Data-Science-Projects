import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/missing_data1.csv', sep=',')

print(df)
print(df.isna().sum())
print("*" * 100)
df.dropna(inplace=True, ignore_index=True)
print(df)
print(df.isna().sum())
print(df.shape)
