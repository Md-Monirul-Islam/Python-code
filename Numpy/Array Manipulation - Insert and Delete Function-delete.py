import numpy as np
a = np.arange(1,11)
print(a)
print(np.delete(a,3))

#2dimentional
b = np.array([[1,2],[3,4]])
print(b)
print(np.delete(b,2))
print(np.delete(b,1,axis=0))
print(np.delete(b,1,axis=1))