import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Hp/Downloads/customer1.txt', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'loc']
print(df)
# fname,lname,age,prof
df1 =df[['fname','lname','age','prof']]
print(df1)