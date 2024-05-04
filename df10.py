import pandas as pd

lst = [[101, "Lal", "Jose", 21, "Actor", "Kochi", 2100],
       [102, "Mini", "Lal", 30, "Actress", "Thrissur", 3000],
       [103, "Simon", "Peter", 24, "Bigdata", "Trivandum", 4000],
       [104, "Sony", "Girl", 40, "Civil Engineer", "Irinjalakuda", 3000],
       [105, "Tom", "Thomas", 25, "Contractor", "Kasargod", 2000],
       [106, "Yami", "Das", 23, "Engineer", "Thrissur", 2000],
       [107, "Unni", "K", 40, "Teacher", "Thrissur", 2100]]
df = pd.DataFrame(lst, columns=['id', 'fname', 'lname', 'age', 'prof', 'loc', 'salary'])
print("*" * 100)
# newdfname=olddfname.loc[olddf['colname']condition]
df1 = df.loc[df['age'] > 27]
print(df1)
print('*' * 100)
df2 = df.loc[df['age'] == 25][['fname', 'lname', 'age', 'salary']]
print(df2)
print('*' * 100)
df3 = df.loc[df['prof'] == 'Bigdata']
print(df3)
print("*" * 100)
# newdfname = olddfname.loc[(olddf['colname']condition1)&(olddf['colname']condition2)]
df4 = df.loc[(df['age'] > 27) & (df['prof'] == 'Teacher')]
print(df4)
print("*"*100)
df5 = df.loc[(df['salary'] > 1500) & (df['prof'] == 'Teacher')][['fname', 'lname', 'age', 'loc']]
print(df5)
