import numpy as np
#flatten
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
print(a.flatten())
print(a.flatten(order='F'))
print(a.flatten(order='A'))

#ravel
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(np.ravel(b))
print(np.ravel(a,order="F"))