import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
print(a[2:7])
print(a[::-1])
print(a[1::2])

#2 dimentional

b = np.array([[1,2],[3,4],[5,6]])
print(b)
print(b[1:,1:])
print(b[:,:])

c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(c[:,:])
print(c[1:,1:])
print(c[1:,2:])
print(c[::1,::3])

#3 dimention
d = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(d[:,:,:])
print(d[:,:,2:3])
print(d[:,1:,::2])