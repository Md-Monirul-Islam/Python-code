import matplotlib.pyplot as plt
x = [1,12,22,21,20,21]
y = [1,11,21,31]
#plt.hist(x,y,ec="red",weights=[2,1,2,1,2,2]
plt.hist(x,y,ec="red",cumulative=True)
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Population age count")
plt.show()