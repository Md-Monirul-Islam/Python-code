import matplotlib.pyplot as plt
import numpy

a = numpy.arange(0,10,.5)
plt.plot(a,"go:",a**3,"r^--",a**2,"c+-")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.show()