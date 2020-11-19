#legend
import numpy as np
import matplotlib.pyplot as plt
t = np.array([1,2,3,4])
plt.plot(t**2,t,color="g")
plt.plot(t**3,t,color="k")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.legend(("squares","qubes"))
plt.show()