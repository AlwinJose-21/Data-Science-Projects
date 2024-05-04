import numpy as np
import pandas as pd

lst = [[101, "lal", "Jose", 21, "Actor", "Kochi", 2100],
       [102, "Mini", "Lal", 30, "Actress", "Thrissur", 3000],
       [103, "Simon", "Peter", 24, "Musician", "Trivandum", 4000],
       [104, "Sony", "Girl", 40, "Civil Engineer", "Irinjalakuda", 3000],
       [105, "Tom", "Thomas", 36, "Contractor", "Kasargod", 2000],
       [106, "Yami", "Das", 23, "Engineer", "Thrissur", 2000],
       [107, "Unni", "K", 40, "Teacher", "Thrissur", 2100]]
df = pd.DataFrame(lst, columns=['id', 'fname', 'lname', 'age', 'prof', 'loc', 'salary'])
print(df)
# newdfname = olddfname.rename(columns={'oldcolname','newcolname'})
df1 = df.rename(columns={'loc': 'Place'})
print(df1)
# newdfname = olddfname[['colnames']]
df2 = df[['fname', 'lname', 'age', 'prof']]
print(df2)
