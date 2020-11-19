import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10])
b = np.reshape(a,(5,2))
print(b)
print(b.shape)
c = np.reshape(a,(5,2),order="F")
#print(help(np.reshape))
print(c)
#resize
d = np.arange(1,10+1)
#print(help(np.resize))
print(d)
print(np.resize(d,(3,4)))