import pandas as pd

df1 = pd.read_csv('C:/Users/Hp/Downloads/custom.txt', sep=',', header=None)
df2 = pd.read_csv('C:/Users/Hp/Downloads/order.txt', sep=',', header=None)
df1.columns = ['id', 'name', 'age', 'loc', 'salary']
df2.columns = ['oid', 'dat', 'id', 'amount']
print(df1)
print(df2)
df3 = pd.merge(df1, df2, on='id', how='inner').sort_values('salary', ascending=False) \
    [['name', 'age', 'loc', 'dat', 'amount']].head(1)
print(df3)
df4 = pd.merge(df1, df2, on='id', how='inner').sort_values('dat', ascending=False) \
    [['name', 'age', 'dat', 'amount']].head(3)
print(df4)
