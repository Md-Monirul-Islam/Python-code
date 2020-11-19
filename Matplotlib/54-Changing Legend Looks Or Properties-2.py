import matplotlib.pyplot as plt
import numpy as np
t = np.array([1,2,3,4])
plt.plot(t**2,t,color="cyan",label="1")
plt.plot(t**3,t,color="green",label="2")
plt.plot(t,t**2,color="black",label="3")
plt.plot(t,t**3,color="yellow",label="4")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.grid()
#plt.legend(shadow=True) #default is None,present is False
#plt.legend(frameon=True) #default is None,present is True
plt.legend(ncol=4,columnspacing=5) #default is None,present is 2.0
plt.show()