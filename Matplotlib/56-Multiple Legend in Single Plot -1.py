import numpy as np
import matplotlib.pyplot as plt
t = np.array([1,2,3,4])
l1, = plt.plot(t**2,t,color="g")
l2, = plt.plot(t**3,t,color="c")
l3, = plt.plot(t,t**2,color="k")
l4, = plt.plot(t,t**3,color="red")
plt.legend((l1,l2),["label_1","label_2"],loc="upper right")
plt.legend((l3,l4),["label_3","label_4"])
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.show()