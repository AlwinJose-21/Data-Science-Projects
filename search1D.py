import numpy as np
a = np.array([2,1,5,4,5,9,6])
# where
b=np.where(a==1)
print(b)
b=np.where(a>5)
print(b)
b=np.where(a%2==0)
print(b)