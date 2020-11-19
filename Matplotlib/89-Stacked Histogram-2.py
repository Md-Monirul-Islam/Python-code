import matplotlib.pyplot as plt
import numpy
x = numpy.random.randn(1000)
y = numpy.sin(x)
z = numpy.cos(x)
#plt.hist(x,bins="auto",edgecolor="k",alpha=0.5)
#plt.hist(y,bins="auto",ec="k")
#plt.hist(z,bins="auto",ec="k")
plt.hist([x,y,z],bins="auto",ec="k",stacked=True)
plt.xlabel("Age")
plt.ylabel("Population count")
plt.title("Population age count")
plt.show()