#leegnd
import matplotlib.pyplot as plt
import numpy as np
t = np.array([1,2,3,4])
plt.plot(t**2,t,color="green")
plt.plot(t**3,t,color="cyan")
plt.title("first plot")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()
