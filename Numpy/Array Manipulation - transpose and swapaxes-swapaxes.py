import numpy as np
arra1 = np.array([[1,2],[3,4]])
print(arra1)
print(np.swapaxes(arra1,0,1))


array2 = np.array([[1,2,3]])
print(array2)
print(np.swapaxes(array2,1,0))
print(np.swapaxes(array2,0,1))
print(array2.shape)

#3 dimentional
array3 = np.arange(1,25).reshape((2,3,4))
print(array3)
print(np.swapaxes(array3,1,2))
print(np.swapaxes(array3,1,2).shape)

print(array3.swapaxes(1,2))