import numpy as np
a = np.arange(1,11)
print(a)
print(np.append(a,333))

#2dimentional
b = np.array([[1,2],[3,4]])
print(np.append(b,[[7,8]],axis=0))
print(np.append(b,[[9],[10]],axis=1))