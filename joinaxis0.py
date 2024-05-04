import numpy as np

a = np.array([0, 6, 5, 1])
b = np.array([1, 2, 3, 4])
# combine two array
c=np.concatenate((a,b))
print(c)