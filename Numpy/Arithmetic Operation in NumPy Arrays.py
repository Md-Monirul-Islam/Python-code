import numpy as np
a = np.arange(1,10)
print(a)
print(a+2)
print(a*2)
print(a/2)
print(a-2)
print(a**2)
print(a%2)

#2 dimentional
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b*2)
print(b-2)
print(b/2)
print(b+2)
print(b**2)

#another
x = np.arange(1,5)
y = np.array([4,5,6,7])
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#another
m = np.array([[1,2,3],[4,5,6]])
n = np.array([[1,2,1],[2,1,1]])
print(m)
print(n)
print(m+n)
print(m%n)
print(np.add(m,n))
print(np.subtract(m,n))