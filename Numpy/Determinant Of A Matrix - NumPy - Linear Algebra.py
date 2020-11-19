import numpy as np
a = np.array([[1,2],[3,4]])
print(a)
print(np.linalg.det(a))
print(round(np.linalg.det(a)))
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(np.linalg.det(b))
#print(help(np.linalg.det))