import matplotlib.pyplot as plt
x = [1,12,22,21,20,21]
y = [1,11,21,31]
n,bin_1,patches = plt.hist(x,y,edgecolor="red",color="cyan")
#print(n,"\n",bin_1,"\n",patches)
#print(patches[1])
patches[0].set_facecolor("yellow")
patches[1].set_fc("orange")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Population age count")
plt.show()