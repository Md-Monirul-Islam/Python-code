import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a)
print(a[4])
print(a[-5])
print(a[3:6])
print(a[::-1])

#2 dimentional array
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b[0][0])
print(b[-1][-1])
print(b[1])


#3dimention
c = [[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
d = np.array(c)
print(d)
print(d[0][2][1])
print(d[-1][-3][-3])