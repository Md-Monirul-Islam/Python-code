import matplotlib.pyplot as plt
import numpy as np
#t = np.linspace(-np.pi,np.pi)
t = np.arange(0,4*np.pi,0.5)
plt.plot(t,np.sin(t),marker="+",label="sin",linestyle="-.")
plt.plot(t,np.cos(t),marker="*",label="cos",linestyle=":")
plt.title("sin and cos graph")
plt.xlabel("angle")
plt.ylabel("sin and cos value")
plt.legend()
plt.show()