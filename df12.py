import numpy as np
import pandas as pd

lst = [[101, "Lal", "Jose", 21, "Actor", "Kochi", 2100],
       [102, "Mini", "Lal", 30, "Actress", "Thrissur", 3000],
       [103, "Simon", "Peter", 24, "Musician", "Trivandum", 4000],
       [104, "Sony", "Girl", 40, "Civil Engineer", "Irinjalakuda", 3000],
       [105, "Tom", "Thomas", 36, "Contractor", "Kasargod", 2000],
       [106, "Yami", "Das", 23, "Engineer", "Thrissur", 2000],
       [107, "Unni", "K", 40, "Teacher", "Thrissur", 2100]]
df = pd.DataFrame(lst, columns=['id', 'fname', 'lname', 'age', 'prof', 'loc', 'salary'])
# syntax
# newdf=olddf.sort_values(by='colname')
df1 = df.sort_values(by='age')
print(df1)
print("*"*100)
df2 = df.sort_values(by='age', ascending=False)
print(df2)
print("*"*100)
df3 = df.sort_values(by='salary', ascending=False)
print(df3)
print("*"*100)
df4 = df.sort_values(by='fname')
print(df4)