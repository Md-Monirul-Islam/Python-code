import numpy as np
#2 dimentional
array1 = np.arange(1,11).reshape(5,2)
print(array1)
print(np.transpose(array1))
print(array1.shape)
print(np.transpose(array1).shape)
print(np.transpose(array1,axes=(0,1)))
print(np.transpose(array1,axes=(0,1)))


#3 dimentional

array2 = np.arange(1,25).reshape(2,3,4)
print(array2)
print(np.transpose(array2))
print(array2.shape)
print(np.transpose(array2).shape)
print(array2.size)
print(np.transpose(array2,axes=(1,2,0)))

#1 dimentional

array3 = np.arange(1,10)
print(array3)
print(np.transpose(array3))


