import numpy as np

a = np.array([41, 42, 43, 44, 45, 46, 47])
# filter
b = a > 42
c = a[b]
print(c)
