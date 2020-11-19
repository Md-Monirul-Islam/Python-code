import numpy as np
import matplotlib.pyplot as plt
t = np.array([1,2,3,4])
plt.plot(t**2,t,color="c",label="1")
plt.plot(t**3,t,color="g",label="2")
plt.plot(t,t**2,color="r",label="3")
plt.plot(t,t**3,color="k",label=4)
plt.xlim(0,4)
plt.ylim(0,4)
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.grid()
plt.legend(loc=(1,1))
plt.tight_layout()
plt.show()