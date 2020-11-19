import numpy as np
a = np.arange(1,10)
print(a)
index = np.array([2,4,5])
print(a[index])
print(a[[2,4,5]])
print(a[[1,2,4,2,1]])

#2 dimention
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[[0,2],[2,0]])
print(b[[0,1,2],[0,2,1]])

#booean indexing
d = np.array([[1,-2,3],[5,-8,9]])
print(d)
print(d[d<0])
print(d[d>0])
print(d[d<0]*2)