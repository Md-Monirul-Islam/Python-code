import numpy as np
a = np.arange(1,11)
print(a)
print(np.insert(a,3,100))
print(np.insert(a,4,50.50))
print(np.insert(a,(2,5),50))

#dimentional
b = np.array([[1,2],[4,5]])
print(b)
print(np.insert(b,2,40))
print(np.insert(b,2,50,axis=0))
print(np.insert(b,2,[7,8],axis=0))
print(help(np.insert))