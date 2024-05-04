import pandas as pd

friends = [{'name': 'Jone', 'age': 20, 'job': 'student'},
           {'name': 'Jenny', 'age': 30, 'job': None},
           {'name': 'nate', 'age': 30, 'job': 'teacher'}]
df = pd.DataFrame(friends)
df = df[['name', 'age', 'job']]
print(df.head())
df.to_csv('freinds.csv', header=True, index=False, na_rep='headmaster')
