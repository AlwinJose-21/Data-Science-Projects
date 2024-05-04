import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/customer1.txt', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'loc']
print(df)
df1 = df.groupby('prof')['prof'].count().sort_values(ascending=False)
print(df1)
df2 = df.loc[df['loc'] == 'india'].groupby('prof')['prof'].count().sort_values(ascending=False)
print(df2)
