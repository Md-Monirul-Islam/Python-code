import matplotlib.pyplot as plt
x = [1,12,22,21,20,21]
y = [1,11,21,31]
#plt.hist(x,y,ec="red",bottom=10)
#plt.hist(x,y,ec="red",bottom=[1,3,5])
#plt.hist(x,y,ec="red",histtype="step")
#plt.hist(x,y,ec="red",align="left")  #by default is mid
#plt.hist(x,y,edgecolor="cyan",orientation="horizontal")  #by default is vertical
#plt.hist(x,y,ec="yellow",rwidth=0.8)
#plt.hist(x,y,ec="red",log=True,color="cyan")  #by default is False
print(plt.hist(x,y,ec="red",color="cyan"))
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Population age count")
plt.show()