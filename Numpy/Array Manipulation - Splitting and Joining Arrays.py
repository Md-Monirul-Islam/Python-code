import numpy as np
a = np.arange(1,5)
b = np.arange(1,5)
c = np.arange(1,7)
print(np.concatenate((a,b,c)))
d = np.zeros(8)
print(np.zeros(8))
print(np.concatenate((a,b),out=d))

#2 dimentional
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[5,6]])
print(np.concatenate((array1,array2)))
print(np.concatenate((array1,array2.T),axis=1))

m = np.arange(5)
n = np.arange(5)
o = np.arange(6)
#vstack
print(np.vstack((m,n)))
print(np.vstack((array1,array2)))
#hstack
print(np.hstack((m,n)))
print(np.hstack((array1,array2.T)))