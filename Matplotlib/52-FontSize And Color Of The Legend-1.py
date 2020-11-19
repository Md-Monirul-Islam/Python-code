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
#plt.legend(fontsize="xx-large",edgecolor="c",facecolor="red") #facecolor and edgecolor use both.
plt.legend(facecolor="white",fontsize=20,framealpha=1) #without grid line in bbox.
plt.show()