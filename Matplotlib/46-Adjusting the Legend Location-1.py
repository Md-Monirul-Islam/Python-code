import matplotlib.pyplot as plt
import numpy as np
t = np.array([1,2,3,4])
plt.plot(t**2,t,color="c",label="squares")
plt.plot(t**3,t,color="g",label="qubes")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.legend(loc="upper right",ncol=2) #ncol is optional
plt.show()