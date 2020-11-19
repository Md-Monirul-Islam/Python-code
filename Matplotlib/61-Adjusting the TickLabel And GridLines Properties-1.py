import numpy
import matplotlib.pyplot as plt
t = numpy.array([1,2,3,4])
plt.plot(t**2,t,color="blue",label="label_1")
plt.plot(t**3,t,color="cyan",label="label-2")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("first plot")
plt.minorticks_on()
plt.grid()
plt.legend()
#plt.tick_params(labelsize=20)
#plt.tick_params(labelcolor="green")
#plt.tick_params(colors="blue",width=10)
#plt.tick_params(labeltop=True,labelright=True,labelrotation=20)
#plt.tick_params(grid_color="blue",grid_alpha=0.5)  #grid_alpha is by default 1
plt.tick_params(grid_color="green",grid_linestyle="-.")
plt.show()