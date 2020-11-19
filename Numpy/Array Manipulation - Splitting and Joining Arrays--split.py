import numpy as np
a = np.arange(1,10)
print(a)
print(np.split(a,3))

#2dimentional
b = np.arange(1,13).reshape(6,2)
print(b)
print(np.split(b,2))
#vsplit
print(np.vsplit(b,2))


#hsplit
c = np.arange(1,13).reshape(2,6)
print(c)
print(np.hsplit(c,3))
print(np.hsplit(c,3))
print(np.split(c,3,axis=1))
