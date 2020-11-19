import matplotlib.pyplot as plt
import numpy as np
t = [0,30,45,60,90]
x = [i*(np.pi/180) for i in t]
plt.plot(x,np.sin(x),marker="+",markersize=15,label="sin")
plt.plot(x,np.cos(x),marker="*",markersize=15,label="cos")
#plt.xticks(t)
plt.title("sin and cos graph")
plt.xlabel("angle")
plt.ylabel("sin and cos value")
plt.legend()
plt.show()