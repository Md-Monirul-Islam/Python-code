import numpy as np
a = np.array([[1,2],[3,4]])
print(np.linalg.matrix_power(a,2))
print(np.dot(a,a))
print(np.linalg.matrix_power(a,3))
print(np.linalg.matrix_power(a,0))
print(np.linalg.matrix_power(a,-2))
print(np.linalg.inv(a))