import numpy as np
import matplotlib.pyplot as plt
t = np.array([1,2,3,4])
plt.plot(t**2,t,color="cyan",label="101")
plt.plot(t**3,t,color="blue",label="102")
plt.xlim(0,5)
plt.grid()
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
#print(plt.xticks())
#print(plt.xticks([2,4]))
plt.xticks([2,4],["A","B"])
plt.show()