import pandas as pd
df1 = pd.read_csv('C:/Users/Hp/Downloads/student',sep=',',header=None)
df2 = pd.read_csv('C:/Users/Hp/Downloads/results',sep=',',header=None)
df1.columns= ['Name','rollno']
print(df1)
df2.columns=['rollno','result']
print(df2)
df3 = pd.merge(df1,df2,on='rollno',how='inner') \
    .loc[df2['result']=='pass'] [['Name','rollno','result']]
print(df3)