import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/patent', sep=' ', header=None)
df.columns = ['patents', 'subpatents']
print(df)
df1 = df.groupby('patents')['patents'].count() \
        .sort_values(ascending=False)
print(df1)
