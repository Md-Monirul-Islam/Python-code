import numpy as np
import matplotlib.pyplot as plt
t = np.array([1,2,3,4])
plt.plot(t**2,t,color="c",label="101")
plt.plot(t**3,t,color="g",label="102")
plt.plot(t,t**2,color="k",label="103")
plt.plot(t,t**3,color="b",label="104")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.legend(loc="upper right",ncol=2)
plt.show()