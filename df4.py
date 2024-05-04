import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Hp/Downloads/movies_cleaned_pandas.csv',sep=',',header=None)
df.columns=['id','Movies name','Year of release','Rating','Duration']
print(df)