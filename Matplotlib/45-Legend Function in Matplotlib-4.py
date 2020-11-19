#legend
import matplotlib.pyplot as plt
import numpy as np
t = np.array([1,2,3,4])
line1, = plt.plot(t**2,t,color="cyan")
line2, = plt.plot(t**3,t,color="blue")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.legend([line1,line2],["suares","qubes"])
plt.show()