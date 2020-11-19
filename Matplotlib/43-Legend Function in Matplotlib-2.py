#legend
import matplotlib.pyplot as plt
import numpy as np
t = np.array([1,2,3,4])
plt.plot(t**2,t,color="g",label="squares")
plt.plot(t**3,t,color="r",label="qubes")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.legend()
plt.show()