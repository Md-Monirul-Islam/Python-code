import numpy as np
a = np.array([[3,1],[1,2]])
b = np.array([9,8])
print(np.linalg.solve(a,b))
x = np.array([[6,2,-5],[3,3,-2],[7,5,-3]])
y = np.array([13,13,26])
print(np.linalg.solve(x,y))
print(np.dot(x,y))
print(np.add(x,y))