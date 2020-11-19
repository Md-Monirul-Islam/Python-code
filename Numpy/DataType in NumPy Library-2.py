import numpy as np
a = np.float32(1)
print(a)
print(a.dtype)

# another
b = np.array([1,2,3],dtype='f')
print(b,b.dtype)
#change dtype
print(b.astype(int))