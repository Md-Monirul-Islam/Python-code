import numpy as np
a = np.array([[29,4],[61,8]])
d = np.array([[8,9],[6,8]])
b = np.matrix("29 4;61 8")
c = np.matrix("8 9;6,8")
print(b+c)
print(a+d)