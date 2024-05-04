import numpy as np
import pandas as pd

lst = [[101, "Lal", "Jose", 21, "Python", "Kochi", 2100],
       [102, "Mini", "Lal", 30, "Bigdata", "Thrissur", 3000],
       [103, "Simon", "Peter", 24, "Bigdata", "Trivandum", 4000],
       [104, "Sony", "K", 24, "Python", "Thrissur", 3000],
       [105, "Tom", "Thomas", 36, "Bigdata", "Kasargod", 2000]]

df = pd.DataFrame(lst, columns=['id', 'fname', 'lname', 'age', 'prof', 'loc', 'salary'])

print(df.count())
df1 = df.groupby('prof')['prof'].count()
print(df1)
df2 = df.groupby('age')['age'].count()
print(df2)
df2 = df.groupby('age')['age'].count().sort_values()
print(df2)
df2 = df.groupby('age')['age'].count().sort_values(ascending=False)
print(df2)
