import numpy as np
#matrix addition
a = np.array([[1,2],[3,4]])
b = np.array([[10,20],[30,40]])
print(a)
print(b)
print(a+b)
#matrix multiply
print(a*b) #this method is the array multiply.Its not matrix
print(a.dot(b)) # this is the matrix multiply method
#print(help(np.dot))
print(np.dot(a,b))
print(a.transpose())